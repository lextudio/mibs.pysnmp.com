# SNMP MIB module (AcBoard) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AcBoard
# Produced by pysmi-1.5.4 at Mon Oct 14 20:45:00 2024
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

(DateAndTime,
 DisplayString,
 TAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TAddress",
    "TextualConvention")


# MODULE-IDENTITY

acBoard = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1)
)
acBoard.setRevisions(
        ("2004-01-26 11:53",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AudioCodes_ObjectIdentity = ObjectIdentity
audioCodes = _AudioCodes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003)
)
_AcRegistrations_ObjectIdentity = ObjectIdentity
acRegistrations = _AcRegistrations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 7)
)
_AcGeneric_ObjectIdentity = ObjectIdentity
acGeneric = _AcGeneric_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 8)
)
_AcProducts_ObjectIdentity = ObjectIdentity
acProducts = _AcProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9)
)
_AcBoardMibs_ObjectIdentity = ObjectIdentity
acBoardMibs = _AcBoardMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10)
)
_BoardConfiguration_ObjectIdentity = ObjectIdentity
boardConfiguration = _BoardConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1)
)
_BoardTDMBusSettings_ObjectIdentity = ObjectIdentity
boardTDMBusSettings = _BoardTDMBusSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 1)
)


class _PCMLawSelect_Type(Integer32):
    """Custom type pCMLawSelect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("aLaw", 1),
          ("muLaw", 3))
    )


_PCMLawSelect_Type.__name__ = "Integer32"
_PCMLawSelect_Object = MibScalar
pCMLawSelect = _PCMLawSelect_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 1, 1),
    _PCMLawSelect_Type()
)
pCMLawSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pCMLawSelect.setStatus("obsolete")


class _TDMBusClockSource_Type(Integer32):
    """Custom type tDMBusClockSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4,
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
              19)
        )
    )
    namedValues = NamedValues(
        *(("acTDMBusClockSource-ATM-OC12", 19),
          ("acTDMBusClockSource-ATM-OC3", 17),
          ("acTDMBusClockSource-ATM-OC3-B", 18),
          ("acTDMBusClockSource-BITS", 15),
          ("acTDMBusClockSource-H110-A", 8),
          ("acTDMBusClockSource-H110-B", 9),
          ("acTDMBusClockSource-Internal", 1),
          ("acTDMBusClockSource-MVIP", 3),
          ("acTDMBusClockSource-NetReference1", 10),
          ("acTDMBusClockSource-NetReference2", 11),
          ("acTDMBusClockSource-Network", 4),
          ("acTDMBusClockSource-Network-B", 16),
          ("acTDMBusClockSource-SC-2M", 12),
          ("acTDMBusClockSource-SC-4M", 13),
          ("acTDMBusClockSource-SC-8M", 14))
    )


_TDMBusClockSource_Type.__name__ = "Integer32"
_TDMBusClockSource_Object = MibScalar
tDMBusClockSource = _TDMBusClockSource_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 1, 2),
    _TDMBusClockSource_Type()
)
tDMBusClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tDMBusClockSource.setStatus("obsolete")


class _TDMBusEnableFallBack_Type(Integer32):
    """Custom type tDMBusEnableFallBack based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_TDMBusEnableFallBack_Type.__name__ = "Integer32"
_TDMBusEnableFallBack_Object = MibScalar
tDMBusEnableFallBack = _TDMBusEnableFallBack_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 1, 3),
    _TDMBusEnableFallBack_Type()
)
tDMBusEnableFallBack.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tDMBusEnableFallBack.setStatus("obsolete")


class _TDMBusLocalReference_Type(Integer32):
    """Custom type tDMBusLocalReference based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 27),
    )


_TDMBusLocalReference_Type.__name__ = "Integer32"
_TDMBusLocalReference_Object = MibScalar
tDMBusLocalReference = _TDMBusLocalReference_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 1, 4),
    _TDMBusLocalReference_Type()
)
tDMBusLocalReference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tDMBusLocalReference.setStatus("obsolete")


class _IdlePCMPattern_Type(Integer32):
    """Custom type idlePCMPattern based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IdlePCMPattern_Type.__name__ = "Integer32"
_IdlePCMPattern_Object = MibScalar
idlePCMPattern = _IdlePCMPattern_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 1, 5),
    _IdlePCMPattern_Type()
)
idlePCMPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    idlePCMPattern.setStatus("obsolete")


class _IdleABCD_Type(Integer32):
    """Custom type idleABCD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_IdleABCD_Type.__name__ = "Integer32"
_IdleABCD_Object = MibScalar
idleABCD = _IdleABCD_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 1, 6),
    _IdleABCD_Type()
)
idleABCD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    idleABCD.setStatus("obsolete")


class _TDMBusMasterSlaveSelection_Type(Integer32):
    """Custom type tDMBusMasterSlaveSelection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("acH110BusSecondaryMasterMode", 2),
          ("acTDMBusMasterMode", 1),
          ("acTDMBusSlaveMode", 0))
    )


_TDMBusMasterSlaveSelection_Type.__name__ = "Integer32"
_TDMBusMasterSlaveSelection_Object = MibScalar
tDMBusMasterSlaveSelection = _TDMBusMasterSlaveSelection_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 1, 7),
    _TDMBusMasterSlaveSelection_Type()
)
tDMBusMasterSlaveSelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tDMBusMasterSlaveSelection.setStatus("obsolete")


class _TDMBusNetRefSpeed_Type(Integer32):
    """Custom type tDMBusNetRefSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2)
        )
    )
    namedValues = NamedValues(
        *(("acTH110BusNetReferenceSpeed-20488khz", 2),
          ("acTH110BusNetReferenceSpeed-8khz", 0))
    )


_TDMBusNetRefSpeed_Type.__name__ = "Integer32"
_TDMBusNetRefSpeed_Object = MibScalar
tDMBusNetRefSpeed = _TDMBusNetRefSpeed_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 1, 8),
    _TDMBusNetRefSpeed_Type()
)
tDMBusNetRefSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tDMBusNetRefSpeed.setStatus("obsolete")


class _TDMBusOutputStartingChannel_Type(Integer32):
    """Custom type tDMBusOutputStartingChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_TDMBusOutputStartingChannel_Type.__name__ = "Integer32"
_TDMBusOutputStartingChannel_Object = MibScalar
tDMBusOutputStartingChannel = _TDMBusOutputStartingChannel_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 1, 9),
    _TDMBusOutputStartingChannel_Type()
)
tDMBusOutputStartingChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tDMBusOutputStartingChannel.setStatus("obsolete")


class _BoardTDMBusOutputPort_Type(Integer32):
    """Custom type boardTDMBusOutputPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_BoardTDMBusOutputPort_Type.__name__ = "Integer32"
_BoardTDMBusOutputPort_Object = MibScalar
boardTDMBusOutputPort = _BoardTDMBusOutputPort_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 1, 10),
    _BoardTDMBusOutputPort_Type()
)
boardTDMBusOutputPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    boardTDMBusOutputPort.setStatus("obsolete")


class _TDMBusSpeed_Type(Integer32):
    """Custom type tDMBusSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("acTDMBusSpeed-16Mbps", 4),
          ("acTDMBusSpeed-2Mbps", 0),
          ("acTDMBusSpeed-4Mbps", 2),
          ("acTDMBusSpeed-8Mbps", 3))
    )


_TDMBusSpeed_Type.__name__ = "Integer32"
_TDMBusSpeed_Object = MibScalar
tDMBusSpeed = _TDMBusSpeed_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 1, 11),
    _TDMBusSpeed_Type()
)
tDMBusSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tDMBusSpeed.setStatus("obsolete")


class _TDMBusType_Type(Integer32):
    """Custom type tDMBusType based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("aNALOG-BUS", 6),
          ("mVIP-BUS", 0),
          ("qSLAC-BUS", 3),
          ("sC-BUS", 1),
          ("uSE-EXT-BUS", 5),
          ("uSE-FRAMERS", 2),
          ("uSE-H110-BUS", 4),
          ("uSE-PSTN-SW-ONLY", 8))
    )


_TDMBusType_Type.__name__ = "Integer32"
_TDMBusType_Object = MibScalar
tDMBusType = _TDMBusType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 1, 12),
    _TDMBusType_Type()
)
tDMBusType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tDMBusType.setStatus("obsolete")


class _AcOverrideDefaultIdlePCMPattern_Type(Integer32):
    """Custom type acOverrideDefaultIdlePCMPattern based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("useDefaults", 0),
          ("useIdlePCMPattern", 1))
    )


_AcOverrideDefaultIdlePCMPattern_Type.__name__ = "Integer32"
_AcOverrideDefaultIdlePCMPattern_Object = MibScalar
acOverrideDefaultIdlePCMPattern = _AcOverrideDefaultIdlePCMPattern_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 1, 13),
    _AcOverrideDefaultIdlePCMPattern_Type()
)
acOverrideDefaultIdlePCMPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acOverrideDefaultIdlePCMPattern.setStatus("obsolete")


class _AcOverrideDefaultIdleABCDPattern_Type(Integer32):
    """Custom type acOverrideDefaultIdleABCDPattern based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("useDefaults", 0),
          ("useIdleABCDPattern", 1))
    )


_AcOverrideDefaultIdleABCDPattern_Type.__name__ = "Integer32"
_AcOverrideDefaultIdleABCDPattern_Object = MibScalar
acOverrideDefaultIdleABCDPattern = _AcOverrideDefaultIdleABCDPattern_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 1, 14),
    _AcOverrideDefaultIdleABCDPattern_Type()
)
acOverrideDefaultIdleABCDPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acOverrideDefaultIdleABCDPattern.setStatus("obsolete")
_NetworkSettings_ObjectIdentity = ObjectIdentity
networkSettings = _NetworkSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 2)
)


class _BaseUDPPort_Type(Integer32):
    """Custom type baseUDPPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64000),
    )


_BaseUDPPort_Type.__name__ = "Integer32"
_BaseUDPPort_Object = MibScalar
baseUDPPort = _BaseUDPPort_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 2, 1),
    _BaseUDPPort_Type()
)
baseUDPPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    baseUDPPort.setStatus("obsolete")
_DefaultGatewayAddr_Type = IpAddress
_DefaultGatewayAddr_Object = MibScalar
defaultGatewayAddr = _DefaultGatewayAddr_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 2, 2),
    _DefaultGatewayAddr_Type()
)
defaultGatewayAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    defaultGatewayAddr.setStatus("obsolete")
_BoardIPAddr_Type = IpAddress
_BoardIPAddr_Object = MibScalar
boardIPAddr = _BoardIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 2, 3),
    _BoardIPAddr_Type()
)
boardIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardIPAddr.setStatus("obsolete")
_BoardSubNetAddr_Type = IpAddress
_BoardSubNetAddr_Object = MibScalar
boardSubNetAddr = _BoardSubNetAddr_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 2, 4),
    _BoardSubNetAddr_Type()
)
boardSubNetAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardSubNetAddr.setStatus("obsolete")
_AcSyslogServerIP_Type = IpAddress
_AcSyslogServerIP_Object = MibScalar
acSyslogServerIP = _AcSyslogServerIP_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 2, 5),
    _AcSyslogServerIP_Type()
)
acSyslogServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSyslogServerIP.setStatus("obsolete")


class _AcMGControlProtocolType_Type(Integer32):
    """Custom type acMGControlProtocolType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("controlProtocol-H323", 4),
          ("controlProtocol-MEGACO", 2),
          ("controlProtocol-MGCP", 1),
          ("controlProtocol-None", 0),
          ("controlProtocol-SIP", 8))
    )


_AcMGControlProtocolType_Type.__name__ = "Integer32"
_AcMGControlProtocolType_Object = MibScalar
acMGControlProtocolType = _AcMGControlProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 2, 6),
    _AcMGControlProtocolType_Type()
)
acMGControlProtocolType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acMGControlProtocolType.setStatus("obsolete")
_AcSNMPManagerIP_Type = IpAddress
_AcSNMPManagerIP_Object = MibScalar
acSNMPManagerIP = _AcSNMPManagerIP_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 2, 7),
    _AcSNMPManagerIP_Type()
)
acSNMPManagerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSNMPManagerIP.setStatus("obsolete")


class _AcDisableWEBConfig_Type(Integer32):
    """Custom type acDisableWEBConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 0))
    )


_AcDisableWEBConfig_Type.__name__ = "Integer32"
_AcDisableWEBConfig_Object = MibScalar
acDisableWEBConfig = _AcDisableWEBConfig_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 2, 8),
    _AcDisableWEBConfig_Type()
)
acDisableWEBConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acDisableWEBConfig.setStatus("obsolete")


class _AcEnableSyslog_Type(Integer32):
    """Custom type acEnableSyslog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AcEnableSyslog_Type.__name__ = "Integer32"
_AcEnableSyslog_Object = MibScalar
acEnableSyslog = _AcEnableSyslog_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 2, 9),
    _AcEnableSyslog_Type()
)
acEnableSyslog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acEnableSyslog.setStatus("obsolete")


class _AcContrlProtocolTransportType_Type(Integer32):
    """Custom type acContrlProtocolTransportType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("acCPTransport-SCTP-IP", 2),
          ("acCPTransport-TCP-IP", 1),
          ("acCPTransport-UDP-IP", 0))
    )


_AcContrlProtocolTransportType_Type.__name__ = "Integer32"
_AcContrlProtocolTransportType_Object = MibScalar
acContrlProtocolTransportType = _AcContrlProtocolTransportType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 2, 10),
    _AcContrlProtocolTransportType_Type()
)
acContrlProtocolTransportType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acContrlProtocolTransportType.setStatus("obsolete")


class _AcCPControlDiffServ_Type(Integer32):
    """Custom type acCPControlDiffServ based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AcCPControlDiffServ_Type.__name__ = "Integer32"
_AcCPControlDiffServ_Object = MibScalar
acCPControlDiffServ = _AcCPControlDiffServ_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 2, 11),
    _AcCPControlDiffServ_Type()
)
acCPControlDiffServ.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acCPControlDiffServ.setStatus("obsolete")
_SnmpManagers_ObjectIdentity = ObjectIdentity
snmpManagers = _SnmpManagers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 2, 21)
)
_SnmpManagersTable_Object = MibTable
snmpManagersTable = _SnmpManagersTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 2, 21, 1)
)
if mibBuilder.loadTexts:
    snmpManagersTable.setStatus("obsolete")
_SnmpManagersEntry_Object = MibTableRow
snmpManagersEntry = _SnmpManagersEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 2, 21, 1, 1)
)
snmpManagersEntry.setIndexNames(
    (0, "AcBoard", "snmpManagerIndex"),
)
if mibBuilder.loadTexts:
    snmpManagersEntry.setStatus("obsolete")


class _SnmpManagerIndex_Type(Integer32):
    """Custom type snmpManagerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_SnmpManagerIndex_Type.__name__ = "Integer32"
_SnmpManagerIndex_Object = MibTableColumn
snmpManagerIndex = _SnmpManagerIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 2, 21, 1, 1, 1),
    _SnmpManagerIndex_Type()
)
snmpManagerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpManagerIndex.setStatus("obsolete")


class _SnmpManagerIsUsed_Type(Integer32):
    """Custom type snmpManagerIsUsed based on Integer32"""
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


_SnmpManagerIsUsed_Type.__name__ = "Integer32"
_SnmpManagerIsUsed_Object = MibTableColumn
snmpManagerIsUsed = _SnmpManagerIsUsed_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 2, 21, 1, 1, 2),
    _SnmpManagerIsUsed_Type()
)
snmpManagerIsUsed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpManagerIsUsed.setStatus("obsolete")
_SnmpManagerIp_Type = IpAddress
_SnmpManagerIp_Object = MibTableColumn
snmpManagerIp = _SnmpManagerIp_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 2, 21, 1, 1, 3),
    _SnmpManagerIp_Type()
)
snmpManagerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpManagerIp.setStatus("obsolete")


class _SnmpManagerTrapPort_Type(Integer32):
    """Custom type snmpManagerTrapPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SnmpManagerTrapPort_Type.__name__ = "Integer32"
_SnmpManagerTrapPort_Object = MibTableColumn
snmpManagerTrapPort = _SnmpManagerTrapPort_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 2, 21, 1, 1, 4),
    _SnmpManagerTrapPort_Type()
)
snmpManagerTrapPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpManagerTrapPort.setStatus("obsolete")


class _SnmpManagerTrapSendingEnable_Type(Integer32):
    """Custom type snmpManagerTrapSendingEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SnmpManagerTrapSendingEnable_Type.__name__ = "Integer32"
_SnmpManagerTrapSendingEnable_Object = MibTableColumn
snmpManagerTrapSendingEnable = _SnmpManagerTrapSendingEnable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 2, 21, 1, 1, 5),
    _SnmpManagerTrapSendingEnable_Type()
)
snmpManagerTrapSendingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpManagerTrapSendingEnable.setStatus("obsolete")
_AcNTPSettings_ObjectIdentity = ObjectIdentity
acNTPSettings = _AcNTPSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 2, 22)
)
_AcNTPServerIPAddress_Type = IpAddress
_AcNTPServerIPAddress_Object = MibScalar
acNTPServerIPAddress = _AcNTPServerIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 2, 22, 1),
    _AcNTPServerIPAddress_Type()
)
acNTPServerIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acNTPServerIPAddress.setStatus("obsolete")


class _AcNTPUtcOffset_Type(Integer32):
    """Custom type acNTPUtcOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-43200, 43200),
    )


_AcNTPUtcOffset_Type.__name__ = "Integer32"
_AcNTPUtcOffset_Object = MibScalar
acNTPUtcOffset = _AcNTPUtcOffset_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 2, 22, 2),
    _AcNTPUtcOffset_Type()
)
acNTPUtcOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acNTPUtcOffset.setStatus("deprecated")


class _AcNTPUpdateInterval_Type(Integer32):
    """Custom type acNTPUpdateInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcNTPUpdateInterval_Type.__name__ = "Integer32"
_AcNTPUpdateInterval_Object = MibScalar
acNTPUpdateInterval = _AcNTPUpdateInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 2, 22, 3),
    _AcNTPUpdateInterval_Type()
)
acNTPUpdateInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acNTPUpdateInterval.setStatus("deprecated")
_AcWEBAccess_ObjectIdentity = ObjectIdentity
acWEBAccess = _AcWEBAccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 2, 23)
)
_AcWEBAccessTable_Object = MibTable
acWEBAccessTable = _AcWEBAccessTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 2, 23, 1)
)
if mibBuilder.loadTexts:
    acWEBAccessTable.setStatus("obsolete")
_AcWEBAccessEntry_Object = MibTableRow
acWEBAccessEntry = _AcWEBAccessEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 2, 23, 1, 1)
)
acWEBAccessEntry.setIndexNames(
    (0, "AcBoard", "acWEBAccessIndex"),
)
if mibBuilder.loadTexts:
    acWEBAccessEntry.setStatus("obsolete")


class _AcWEBAccessRowStatus_Type(Integer32):
    """Custom type acWEBAccessRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_AcWEBAccessRowStatus_Type.__name__ = "Integer32"
_AcWEBAccessRowStatus_Object = MibTableColumn
acWEBAccessRowStatus = _AcWEBAccessRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 2, 23, 1, 1, 1),
    _AcWEBAccessRowStatus_Type()
)
acWEBAccessRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acWEBAccessRowStatus.setStatus("obsolete")


class _AcWEBAccessAction_Type(Integer32):
    """Custom type acWEBAccessAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_AcWEBAccessAction_Type.__name__ = "Integer32"
_AcWEBAccessAction_Object = MibTableColumn
acWEBAccessAction = _AcWEBAccessAction_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 2, 23, 1, 1, 2),
    _AcWEBAccessAction_Type()
)
acWEBAccessAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acWEBAccessAction.setStatus("obsolete")


class _AcWEBAccessActionResult_Type(Integer32):
    """Custom type acWEBAccessActionResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_AcWEBAccessActionResult_Type.__name__ = "Integer32"
_AcWEBAccessActionResult_Object = MibTableColumn
acWEBAccessActionResult = _AcWEBAccessActionResult_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 2, 23, 1, 1, 3),
    _AcWEBAccessActionResult_Type()
)
acWEBAccessActionResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acWEBAccessActionResult.setStatus("obsolete")


class _AcWEBAccessIndex_Type(Integer32):
    """Custom type acWEBAccessIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_AcWEBAccessIndex_Type.__name__ = "Integer32"
_AcWEBAccessIndex_Object = MibTableColumn
acWEBAccessIndex = _AcWEBAccessIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 2, 23, 1, 1, 4),
    _AcWEBAccessIndex_Type()
)
acWEBAccessIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acWEBAccessIndex.setStatus("obsolete")


class _AcWEBAccessUserName_Type(OctetString):
    """Custom type acWEBAccessUserName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 26),
    )


_AcWEBAccessUserName_Type.__name__ = "OctetString"
_AcWEBAccessUserName_Object = MibTableColumn
acWEBAccessUserName = _AcWEBAccessUserName_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 2, 23, 1, 1, 5),
    _AcWEBAccessUserName_Type()
)
acWEBAccessUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acWEBAccessUserName.setStatus("obsolete")


class _AcWEBAccessUserCode_Type(OctetString):
    """Custom type acWEBAccessUserCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 26),
    )


_AcWEBAccessUserCode_Type.__name__ = "OctetString"
_AcWEBAccessUserCode_Object = MibTableColumn
acWEBAccessUserCode = _AcWEBAccessUserCode_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 2, 23, 1, 1, 6),
    _AcWEBAccessUserCode_Type()
)
acWEBAccessUserCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acWEBAccessUserCode.setStatus("obsolete")
_AuxiliarySettings_ObjectIdentity = ObjectIdentity
auxiliarySettings = _AuxiliarySettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 3)
)


class _EnableDiagnostics_Type(Integer32):
    """Custom type enableDiagnostics based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("acDiagnostics-BuiltInTest", 1),
          ("acDiagnostics-BuiltInTestWithSDRAM", 3),
          ("acDiagnostics-BuiltInTestwithPartialFlash", 2),
          ("acDiagnostics-Disabled", 0))
    )


_EnableDiagnostics_Type.__name__ = "Integer32"
_EnableDiagnostics_Object = MibScalar
enableDiagnostics = _EnableDiagnostics_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 3, 1),
    _EnableDiagnostics_Type()
)
enableDiagnostics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableDiagnostics.setStatus("obsolete")
_TrunkSettings_ObjectIdentity = ObjectIdentity
trunkSettings = _TrunkSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 4)
)
_TrunkSettingsTable_Object = MibTable
trunkSettingsTable = _TrunkSettingsTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    trunkSettingsTable.setStatus("obsolete")
_TrunkSettingsEntry_Object = MibTableRow
trunkSettingsEntry = _TrunkSettingsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 4, 1, 1)
)
trunkSettingsEntry.setIndexNames(
    (0, "AcBoard", "trunkId"),
)
if mibBuilder.loadTexts:
    trunkSettingsEntry.setStatus("obsolete")


class _TrunkId_Type(Integer32):
    """Custom type trunkId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_TrunkId_Type.__name__ = "Integer32"
_TrunkId_Object = MibTableColumn
trunkId = _TrunkId_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 4, 1, 1, 1),
    _TrunkId_Type()
)
trunkId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkId.setStatus("obsolete")


class _ClockMaster_Type(Integer32):
    """Custom type clockMaster based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("acCLOCK-MASTER-OFF", 0),
          ("acCLOCK-MASTER-ON", 1))
    )


_ClockMaster_Type.__name__ = "Integer32"
_ClockMaster_Object = MibTableColumn
clockMaster = _ClockMaster_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 4, 1, 1, 2),
    _ClockMaster_Type()
)
clockMaster.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clockMaster.setStatus("obsolete")


class _FramingMethod_Type(Integer32):
    """Custom type framingMethod based on Integer32"""
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
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("e1-FRAMING-DDF", 2),
          ("e1-FRAMING-MFF-CRC4", 3),
          ("e1-FRAMING-MFF-CRC4-EXT", 4),
          ("e1-FRAMING-NIL", 5),
          ("eXTENDED-SUPER-FRAME", 0),
          ("sUPER-FRAME", 1),
          ("t1-FRAMING-ESF", 8),
          ("t1-FRAMING-ESF-CRC6", 9),
          ("t1-FRAMING-ESF-CRC6-JT", 11),
          ("t1-FRAMING-F12", 7),
          ("t1-FRAMING-F4", 6),
          ("t1-FRAMING-F72", 10),
          ("t1-FRAMING-NIL", 12))
    )


_FramingMethod_Type.__name__ = "Integer32"
_FramingMethod_Object = MibTableColumn
framingMethod = _FramingMethod_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 4, 1, 1, 3),
    _FramingMethod_Type()
)
framingMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    framingMethod.setStatus("obsolete")


class _ProtocolType_Type(Integer32):
    """Custom type protocolType based on Integer32"""
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
              34,
              35,
              36)
        )
    )
    namedValues = NamedValues(
        *(("e1CasR2", 8),
          ("e1EuroISDN", 1),
          ("e1Mfcr2", 7),
          ("e1RawCAS", 9),
          ("e1Transparent30", 6),
          ("e1Transparent31", 5),
          ("j1-TRANSPARENT", 15),
          ("nONE", 0),
          ("pROTOCOL-TYPE-E1-AUSTEL-ISDN", 17),
          ("pROTOCOL-TYPE-E1-EXTRA-30", 30),
          ("pROTOCOL-TYPE-E1-EXTRA-31", 31),
          ("pROTOCOL-TYPE-E1-HKT-ISDN", 18),
          ("pROTOCOL-TYPE-E1-IUA", 29),
          ("pROTOCOL-TYPE-E1-KOR-ISDN", 19),
          ("pROTOCOL-TYPE-E1-QSIG", 21),
          ("pROTOCOL-TYPE-E1-TNZ-22", 22),
          ("pROTOCOL-TYPE-T1-DMS100-MERIDIAN-ISDN", 35),
          ("pROTOCOL-TYPE-T1-EURO-ISDN", 34),
          ("pROTOCOL-TYPE-T1-EXTRA-23", 23),
          ("pROTOCOL-TYPE-T1-EXTRA-32", 32),
          ("pROTOCOL-TYPE-T1-EXTRA-33", 33),
          ("pROTOCOL-TYPE-T1-HKT-ISDN", 20),
          ("pROTOCOL-TYPE-T1-IUA", 28),
          ("pROTOCOL-TYPE-T1-NI1-ISDN", 36),
          ("pROTOCOL-TYPE-T1-NTT-ISDN", 16),
          ("pROTOCOL-TYPE-V5-1-AN", 24),
          ("pROTOCOL-TYPE-V5-1-LE", 25),
          ("pROTOCOL-TYPE-V5-2-AN", 26),
          ("pROTOCOL-TYPE-V5-2-LE", 27),
          ("t1-4EssISDN", 11),
          ("t1-5Ess-10-ISDN", 13),
          ("t1-5Ess-9-ISDN", 12),
          ("t1-Dms100-ISDN", 14),
          ("t1-NI2ISDN", 10),
          ("t1Cas", 2),
          ("t1RawCas", 3),
          ("t1Transparent", 4))
    )


_ProtocolType_Type.__name__ = "Integer32"
_ProtocolType_Object = MibTableColumn
protocolType = _ProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 4, 1, 1, 4),
    _ProtocolType_Type()
)
protocolType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    protocolType.setStatus("obsolete")


class _TerminationSide_Type(Integer32):
    """Custom type terminationSide based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("acNETWORK-TERMINATION-SIDE", 1),
          ("acUSER-TERMINATION-SIDE", 0))
    )


_TerminationSide_Type.__name__ = "Integer32"
_TerminationSide_Object = MibTableColumn
terminationSide = _TerminationSide_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 4, 1, 1, 5),
    _TerminationSide_Type()
)
terminationSide.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    terminationSide.setStatus("obsolete")


class _DchConfig_Type(Integer32):
    """Custom type dchConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("acDCH-CONFIG-BACKUP", 1),
          ("acDCH-CONFIG-NFAS", 2),
          ("acDCH-CONFIG-PRIMARY", 0),
          ("acDCH-NOT-ISDN-TRUNK", 3))
    )


_DchConfig_Type.__name__ = "Integer32"
_DchConfig_Object = MibTableColumn
dchConfig = _DchConfig_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 4, 1, 1, 6),
    _DchConfig_Type()
)
dchConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dchConfig.setStatus("obsolete")


class _LineCode_Type(Integer32):
    """Custom type lineCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("acAMI", 1),
          ("acB8ZS", 0),
          ("acHDB3", 2))
    )


_LineCode_Type.__name__ = "Integer32"
_LineCode_Object = MibTableColumn
lineCode = _LineCode_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 4, 1, 1, 7),
    _LineCode_Type()
)
lineCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lineCode.setStatus("obsolete")


class _LineBuildOutLoss_Type(Integer32):
    """Custom type lineBuildOutLoss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ac0DB", 0),
          ("ac15DB", 2),
          ("ac22-5DB", 3),
          ("ac7-5DB", 1))
    )


_LineBuildOutLoss_Type.__name__ = "Integer32"
_LineBuildOutLoss_Object = MibTableColumn
lineBuildOutLoss = _LineBuildOutLoss_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 4, 1, 1, 8),
    _LineBuildOutLoss_Type()
)
lineBuildOutLoss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lineBuildOutLoss.setStatus("obsolete")


class _LineBuildOutOverwrite_Type(Integer32):
    """Custom type lineBuildOutOverwrite based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("acNO-OVER-WRITE", 0),
          ("acOVER-WRITE", 1))
    )


_LineBuildOutOverwrite_Type.__name__ = "Integer32"
_LineBuildOutOverwrite_Object = MibTableColumn
lineBuildOutOverwrite = _LineBuildOutOverwrite_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 4, 1, 1, 9),
    _LineBuildOutOverwrite_Type()
)
lineBuildOutOverwrite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lineBuildOutOverwrite.setStatus("obsolete")


class _LineBuildOutXPM0_Type(Integer32):
    """Custom type lineBuildOutXPM0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_LineBuildOutXPM0_Type.__name__ = "Integer32"
_LineBuildOutXPM0_Object = MibTableColumn
lineBuildOutXPM0 = _LineBuildOutXPM0_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 4, 1, 1, 10),
    _LineBuildOutXPM0_Type()
)
lineBuildOutXPM0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lineBuildOutXPM0.setStatus("obsolete")


class _LineBuildOutXPM1_Type(Integer32):
    """Custom type lineBuildOutXPM1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_LineBuildOutXPM1_Type.__name__ = "Integer32"
_LineBuildOutXPM1_Object = MibTableColumn
lineBuildOutXPM1 = _LineBuildOutXPM1_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 4, 1, 1, 11),
    _LineBuildOutXPM1_Type()
)
lineBuildOutXPM1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lineBuildOutXPM1.setStatus("obsolete")


class _LineBuildOutXPM2_Type(Integer32):
    """Custom type lineBuildOutXPM2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_LineBuildOutXPM2_Type.__name__ = "Integer32"
_LineBuildOutXPM2_Object = MibTableColumn
lineBuildOutXPM2 = _LineBuildOutXPM2_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 4, 1, 1, 12),
    _LineBuildOutXPM2_Type()
)
lineBuildOutXPM2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lineBuildOutXPM2.setStatus("obsolete")


class _TraceLevel_Type(Integer32):
    """Custom type traceLevel based on Integer32"""
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
              7,
              8,
              10,
              11,
              12,
              15)
        )
    )
    namedValues = NamedValues(
        *(("acFULL-ISDN-TRACE", 1),
          ("acFULL-ISDN-TRACE-WITH-DUPLICATION", 5),
          ("acISDN-Q921-RAW-DATA-TRACE", 7),
          ("acISDN-Q931-Q921-RAW-DATA-TRACE", 8),
          ("acISDN-Q931-RAW-DATA-TRACE", 6),
          ("acLAYER3-ISDN-TRACE", 2),
          ("acLAYER3-ISDN-TRACE-NO-DUPLICATION", 4),
          ("acNO-TRACE", 0),
          ("acONLY-ISDN-Q931-MSGS-TRACE", 3),
          ("acSS7-AAL", 15),
          ("acSS7-MTP2", 10),
          ("acSS7-MTP2-AND-APPLI", 11),
          ("acSS7-MTP2-SL-L3-NO-MSU", 12))
    )


_TraceLevel_Type.__name__ = "Integer32"
_TraceLevel_Object = MibTableColumn
traceLevel = _TraceLevel_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 4, 1, 1, 13),
    _TraceLevel_Type()
)
traceLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    traceLevel.setStatus("obsolete")


class _AcV5InterfaceTrunkGroupId_Type(Integer32):
    """Custom type acV5InterfaceTrunkGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_AcV5InterfaceTrunkGroupId_Type.__name__ = "Integer32"
_AcV5InterfaceTrunkGroupId_Object = MibTableColumn
acV5InterfaceTrunkGroupId = _AcV5InterfaceTrunkGroupId_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 4, 1, 1, 14),
    _AcV5InterfaceTrunkGroupId_Type()
)
acV5InterfaceTrunkGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acV5InterfaceTrunkGroupId.setStatus("obsolete")


class _AcV5LinkIdOld_Type(Integer32):
    """Custom type acV5LinkIdOld based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AcV5LinkIdOld_Type.__name__ = "Integer32"
_AcV5LinkIdOld_Object = MibTableColumn
acV5LinkIdOld = _AcV5LinkIdOld_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 4, 1, 1, 15),
    _AcV5LinkIdOld_Type()
)
acV5LinkIdOld.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acV5LinkIdOld.setStatus("obsolete")


class _AcPMStatus_Type(Integer32):
    """Custom type acPMStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AcPMStatus_Type.__name__ = "Integer32"
_AcPMStatus_Object = MibTableColumn
acPMStatus = _AcPMStatus_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 4, 1, 1, 16),
    _AcPMStatus_Type()
)
acPMStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMStatus.setStatus("obsolete")


class _AcLedStatusColor_Type(Integer32):
    """Custom type acLedStatusColor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("green", 2),
          ("off", 0),
          ("red", 1))
    )


_AcLedStatusColor_Type.__name__ = "Integer32"
_AcLedStatusColor_Object = MibTableColumn
acLedStatusColor = _AcLedStatusColor_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 4, 1, 1, 17),
    _AcLedStatusColor_Type()
)
acLedStatusColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLedStatusColor.setStatus("obsolete")


class _AcLedStatusRate_Type(Integer32):
    """Custom type acLedStatusRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("blink", 1),
          ("steady", 0))
    )


_AcLedStatusRate_Type.__name__ = "Integer32"
_AcLedStatusRate_Object = MibTableColumn
acLedStatusRate = _AcLedStatusRate_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 4, 1, 1, 18),
    _AcLedStatusRate_Type()
)
acLedStatusRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLedStatusRate.setStatus("obsolete")


class _AcIsdnNfasInterfaceId_Type(Integer32):
    """Custom type acIsdnNfasInterfaceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AcIsdnNfasInterfaceId_Type.__name__ = "Integer32"
_AcIsdnNfasInterfaceId_Object = MibTableColumn
acIsdnNfasInterfaceId = _AcIsdnNfasInterfaceId_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 4, 1, 1, 19),
    _AcIsdnNfasInterfaceId_Type()
)
acIsdnNfasInterfaceId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acIsdnNfasInterfaceId.setStatus("obsolete")


class _AcTrunkCasTableIndex_Type(Integer32):
    """Custom type acTrunkCasTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AcTrunkCasTableIndex_Type.__name__ = "Integer32"
_AcTrunkCasTableIndex_Object = MibTableColumn
acTrunkCasTableIndex = _AcTrunkCasTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 4, 1, 1, 20),
    _AcTrunkCasTableIndex_Type()
)
acTrunkCasTableIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acTrunkCasTableIndex.setStatus("obsolete")


class _AcTrunkAdminState_Type(Integer32):
    """Custom type acTrunkAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("lock", 0),
          ("unLock", 1))
    )


_AcTrunkAdminState_Type.__name__ = "Integer32"
_AcTrunkAdminState_Object = MibTableColumn
acTrunkAdminState = _AcTrunkAdminState_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 4, 1, 1, 21),
    _AcTrunkAdminState_Type()
)
acTrunkAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acTrunkAdminState.setStatus("obsolete")


class _AcPSTNIuaInterfaceId_Type(Integer32):
    """Custom type acPSTNIuaInterfaceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPSTNIuaInterfaceId_Type.__name__ = "Integer32"
_AcPSTNIuaInterfaceId_Object = MibTableColumn
acPSTNIuaInterfaceId = _AcPSTNIuaInterfaceId_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 4, 1, 1, 22),
    _AcPSTNIuaInterfaceId_Type()
)
acPSTNIuaInterfaceId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPSTNIuaInterfaceId.setStatus("obsolete")


class _AcIsdnQ931LayerResponseBehavior_Type(Integer32):
    """Custom type acIsdnQ931LayerResponseBehavior based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483647, 2147483647),
    )


_AcIsdnQ931LayerResponseBehavior_Type.__name__ = "Integer32"
_AcIsdnQ931LayerResponseBehavior_Object = MibTableColumn
acIsdnQ931LayerResponseBehavior = _AcIsdnQ931LayerResponseBehavior_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 4, 1, 1, 23),
    _AcIsdnQ931LayerResponseBehavior_Type()
)
acIsdnQ931LayerResponseBehavior.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acIsdnQ931LayerResponseBehavior.setStatus("obsolete")


class _AcIsdnIncomingCallsBehavior_Type(Integer32):
    """Custom type acIsdnIncomingCallsBehavior based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcIsdnIncomingCallsBehavior_Type.__name__ = "Integer32"
_AcIsdnIncomingCallsBehavior_Object = MibTableColumn
acIsdnIncomingCallsBehavior = _AcIsdnIncomingCallsBehavior_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 4, 1, 1, 24),
    _AcIsdnIncomingCallsBehavior_Type()
)
acIsdnIncomingCallsBehavior.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acIsdnIncomingCallsBehavior.setStatus("obsolete")


class _AcIsdnOutgoingCallsBehavior_Type(Integer32):
    """Custom type acIsdnOutgoingCallsBehavior based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AcIsdnOutgoingCallsBehavior_Type.__name__ = "Integer32"
_AcIsdnOutgoingCallsBehavior_Object = MibTableColumn
acIsdnOutgoingCallsBehavior = _AcIsdnOutgoingCallsBehavior_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 4, 1, 1, 25),
    _AcIsdnOutgoingCallsBehavior_Type()
)
acIsdnOutgoingCallsBehavior.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acIsdnOutgoingCallsBehavior.setStatus("obsolete")


class _AcIsdnGeneralCCBehavior_Type(Integer32):
    """Custom type acIsdnGeneralCCBehavior based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AcIsdnGeneralCCBehavior_Type.__name__ = "Integer32"
_AcIsdnGeneralCCBehavior_Object = MibTableColumn
acIsdnGeneralCCBehavior = _AcIsdnGeneralCCBehavior_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 4, 1, 1, 26),
    _AcIsdnGeneralCCBehavior_Type()
)
acIsdnGeneralCCBehavior.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acIsdnGeneralCCBehavior.setStatus("obsolete")


class _AcIsdnNfasGroupNumber_Type(Integer32):
    """Custom type acIsdnNfasGroupNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_AcIsdnNfasGroupNumber_Type.__name__ = "Integer32"
_AcIsdnNfasGroupNumber_Object = MibTableColumn
acIsdnNfasGroupNumber = _AcIsdnNfasGroupNumber_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 4, 1, 1, 27),
    _AcIsdnNfasGroupNumber_Type()
)
acIsdnNfasGroupNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acIsdnNfasGroupNumber.setStatus("obsolete")
_MGCPSettings_ObjectIdentity = ObjectIdentity
mGCPSettings = _MGCPSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 5)
)
_CallAgentIP_Type = IpAddress
_CallAgentIP_Object = MibScalar
callAgentIP = _CallAgentIP_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 5, 1),
    _CallAgentIP_Type()
)
callAgentIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    callAgentIP.setStatus("obsolete")


class _CallAgentPort_Type(Integer32):
    """Custom type callAgentPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_CallAgentPort_Type.__name__ = "Integer32"
_CallAgentPort_Object = MibScalar
callAgentPort = _CallAgentPort_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 5, 2),
    _CallAgentPort_Type()
)
callAgentPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    callAgentPort.setStatus("obsolete")


class _CallAgentDomainName_Type(OctetString):
    """Custom type callAgentDomainName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CallAgentDomainName_Type.__name__ = "OctetString"
_CallAgentDomainName_Object = MibScalar
callAgentDomainName = _CallAgentDomainName_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 5, 3),
    _CallAgentDomainName_Type()
)
callAgentDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    callAgentDomainName.setStatus("obsolete")
_RedundantAgentIP_Type = IpAddress
_RedundantAgentIP_Object = MibScalar
redundantAgentIP = _RedundantAgentIP_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 5, 4),
    _RedundantAgentIP_Type()
)
redundantAgentIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redundantAgentIP.setStatus("obsolete")


class _RedundantAgentPort_Type(Integer32):
    """Custom type redundantAgentPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_RedundantAgentPort_Type.__name__ = "Integer32"
_RedundantAgentPort_Object = MibScalar
redundantAgentPort = _RedundantAgentPort_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 5, 5),
    _RedundantAgentPort_Type()
)
redundantAgentPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redundantAgentPort.setStatus("obsolete")


class _RedundantCallAgentDomainName_Type(OctetString):
    """Custom type redundantCallAgentDomainName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_RedundantCallAgentDomainName_Type.__name__ = "OctetString"
_RedundantCallAgentDomainName_Object = MibScalar
redundantCallAgentDomainName = _RedundantCallAgentDomainName_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 5, 6),
    _RedundantCallAgentDomainName_Type()
)
redundantCallAgentDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redundantCallAgentDomainName.setStatus("obsolete")


class _DePopulatedChannelsNumber_Type(Integer32):
    """Custom type dePopulatedChannelsNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_DePopulatedChannelsNumber_Type.__name__ = "Integer32"
_DePopulatedChannelsNumber_Object = MibScalar
dePopulatedChannelsNumber = _DePopulatedChannelsNumber_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 5, 7),
    _DePopulatedChannelsNumber_Type()
)
dePopulatedChannelsNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dePopulatedChannelsNumber.setStatus("obsolete")


class _GateWayName_Type(OctetString):
    """Custom type gateWayName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_GateWayName_Type.__name__ = "OctetString"
_GateWayName_Object = MibScalar
gateWayName = _GateWayName_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 5, 8),
    _GateWayName_Type()
)
gateWayName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gateWayName.setStatus("obsolete")


class _EndPointName_Type(OctetString):
    """Custom type endPointName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_EndPointName_Type.__name__ = "OctetString"
_EndPointName_Object = MibScalar
endPointName = _EndPointName_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 5, 9),
    _EndPointName_Type()
)
endPointName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    endPointName.setStatus("obsolete")


class _MGCPCommunicationLayerTimeout_Type(Integer32):
    """Custom type mGCPCommunicationLayerTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_MGCPCommunicationLayerTimeout_Type.__name__ = "Integer32"
_MGCPCommunicationLayerTimeout_Object = MibScalar
mGCPCommunicationLayerTimeout = _MGCPCommunicationLayerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 5, 10),
    _MGCPCommunicationLayerTimeout_Type()
)
mGCPCommunicationLayerTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mGCPCommunicationLayerTimeout.setStatus("obsolete")
_AcDefaultChannelSettings_ObjectIdentity = ObjectIdentity
acDefaultChannelSettings = _AcDefaultChannelSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 6)
)


class _AcChDefaultDJBufMinDelay_Type(Integer32):
    """Custom type acChDefaultDJBufMinDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 150),
    )


_AcChDefaultDJBufMinDelay_Type.__name__ = "Integer32"
_AcChDefaultDJBufMinDelay_Object = MibScalar
acChDefaultDJBufMinDelay = _AcChDefaultDJBufMinDelay_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 6, 1),
    _AcChDefaultDJBufMinDelay_Type()
)
acChDefaultDJBufMinDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acChDefaultDJBufMinDelay.setStatus("obsolete")


class _AcChDefaultDJBufOptFactor_Type(Integer32):
    """Custom type acChDefaultDJBufOptFactor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 13),
    )


_AcChDefaultDJBufOptFactor_Type.__name__ = "Integer32"
_AcChDefaultDJBufOptFactor_Object = MibScalar
acChDefaultDJBufOptFactor = _AcChDefaultDJBufOptFactor_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 6, 2),
    _AcChDefaultDJBufOptFactor_Type()
)
acChDefaultDJBufOptFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acChDefaultDJBufOptFactor.setStatus("obsolete")


class _AcChDefaultCallerIDType_Type(Integer32):
    """Custom type acChDefaultCallerIDType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              16,
              17,
              18)
        )
    )
    namedValues = NamedValues(
        *(("callerIDStandard-Bellcore", 0),
          ("callerIDStandard-DTMF-Based-ETSI", 16),
          ("callerIDStandard-Denmark", 17),
          ("callerIDStandard-ETSI", 1),
          ("callerIDStandard-Indian", 18),
          ("callerIDStandard-NTT", 2))
    )


_AcChDefaultCallerIDType_Type.__name__ = "Integer32"
_AcChDefaultCallerIDType_Object = MibScalar
acChDefaultCallerIDType = _AcChDefaultCallerIDType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 6, 3),
    _AcChDefaultCallerIDType_Type()
)
acChDefaultCallerIDType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acChDefaultCallerIDType.setStatus("obsolete")


class _AcChDefaultFaxModemBypassM_Type(Integer32):
    """Custom type acChDefaultFaxModemBypassM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_AcChDefaultFaxModemBypassM_Type.__name__ = "Integer32"
_AcChDefaultFaxModemBypassM_Object = MibScalar
acChDefaultFaxModemBypassM = _AcChDefaultFaxModemBypassM_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 6, 4),
    _AcChDefaultFaxModemBypassM_Type()
)
acChDefaultFaxModemBypassM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acChDefaultFaxModemBypassM.setStatus("obsolete")


class _AcChDefaultFaxModemRelayVolume_Type(Integer32):
    """Custom type acChDefaultFaxModemRelayVolume based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-18, -3),
    )


_AcChDefaultFaxModemRelayVolume_Type.__name__ = "Integer32"
_AcChDefaultFaxModemRelayVolume_Object = MibScalar
acChDefaultFaxModemRelayVolume = _AcChDefaultFaxModemRelayVolume_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 6, 5),
    _AcChDefaultFaxModemRelayVolume_Type()
)
acChDefaultFaxModemRelayVolume.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acChDefaultFaxModemRelayVolume.setStatus("obsolete")


class _AcChDefaultFaxRelayECMEnable_Type(Integer32):
    """Custom type acChDefaultFaxRelayECMEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AcChDefaultFaxRelayECMEnable_Type.__name__ = "Integer32"
_AcChDefaultFaxRelayECMEnable_Object = MibScalar
acChDefaultFaxRelayECMEnable = _AcChDefaultFaxRelayECMEnable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 6, 6),
    _AcChDefaultFaxRelayECMEnable_Type()
)
acChDefaultFaxRelayECMEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acChDefaultFaxRelayECMEnable.setStatus("obsolete")


class _AcChDefaultFaxRelayMaxRate_Type(Integer32):
    """Custom type acChDefaultFaxRelayMaxRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("acRate12000bps", 4),
          ("acRate14400bps", 5),
          ("acRate2400bps", 0),
          ("acRate4800bps", 1),
          ("acRate7200bps", 2),
          ("acRate9600bps", 3))
    )


_AcChDefaultFaxRelayMaxRate_Type.__name__ = "Integer32"
_AcChDefaultFaxRelayMaxRate_Object = MibScalar
acChDefaultFaxRelayMaxRate = _AcChDefaultFaxRelayMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 6, 7),
    _AcChDefaultFaxRelayMaxRate_Type()
)
acChDefaultFaxRelayMaxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acChDefaultFaxRelayMaxRate.setStatus("obsolete")


class _AcChDefaultFaxTransportMode_Type(Integer32):
    """Custom type acChDefaultFaxTransportMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("byPassEnable", 2),
          ("disable", 0),
          ("eventsOnly", 3),
          ("relayEnable", 1))
    )


_AcChDefaultFaxTransportMode_Type.__name__ = "Integer32"
_AcChDefaultFaxTransportMode_Object = MibScalar
acChDefaultFaxTransportMode = _AcChDefaultFaxTransportMode_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 6, 8),
    _AcChDefaultFaxTransportMode_Type()
)
acChDefaultFaxTransportMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acChDefaultFaxTransportMode.setStatus("obsolete")


class _AcChDefaultModemRelayRedundancyDepth_Type(Integer32):
    """Custom type acChDefaultModemRelayRedundancyDepth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AcChDefaultModemRelayRedundancyDepth_Type.__name__ = "Integer32"
_AcChDefaultModemRelayRedundancyDepth_Object = MibScalar
acChDefaultModemRelayRedundancyDepth = _AcChDefaultModemRelayRedundancyDepth_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 6, 9),
    _AcChDefaultModemRelayRedundancyDepth_Type()
)
acChDefaultModemRelayRedundancyDepth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acChDefaultModemRelayRedundancyDepth.setStatus("obsolete")


class _AcChDefaultModemRelayMaxRate_Type(Integer32):
    """Custom type acChDefaultModemRelayMaxRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ac12000", 4),
          ("ac14400", 5),
          ("ac2400", 0),
          ("ac4800", 1),
          ("ac7200", 2),
          ("ac9600", 3))
    )


_AcChDefaultModemRelayMaxRate_Type.__name__ = "Integer32"
_AcChDefaultModemRelayMaxRate_Object = MibScalar
acChDefaultModemRelayMaxRate = _AcChDefaultModemRelayMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 6, 10),
    _AcChDefaultModemRelayMaxRate_Type()
)
acChDefaultModemRelayMaxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acChDefaultModemRelayMaxRate.setStatus("obsolete")


class _AcChDefaultUseT38orFRF11_Type(Integer32):
    """Custom type acChDefaultUseT38orFRF11 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("acT38", 1),
          ("fRF11", 0))
    )


_AcChDefaultUseT38orFRF11_Type.__name__ = "Integer32"
_AcChDefaultUseT38orFRF11_Object = MibScalar
acChDefaultUseT38orFRF11 = _AcChDefaultUseT38orFRF11_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 6, 11),
    _AcChDefaultUseT38orFRF11_Type()
)
acChDefaultUseT38orFRF11.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acChDefaultUseT38orFRF11.setStatus("obsolete")


class _AcChDefaultV21ModemTransportType_Type(Integer32):
    """Custom type acChDefaultV21ModemTransportType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("byPassEnable", 2),
          ("disable", 0),
          ("eventsOnly", 3),
          ("relayEnable", 1))
    )


_AcChDefaultV21ModemTransportType_Type.__name__ = "Integer32"
_AcChDefaultV21ModemTransportType_Object = MibScalar
acChDefaultV21ModemTransportType = _AcChDefaultV21ModemTransportType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 6, 12),
    _AcChDefaultV21ModemTransportType_Type()
)
acChDefaultV21ModemTransportType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acChDefaultV21ModemTransportType.setStatus("obsolete")


class _AcChDefaultV22ModemTransportType_Type(Integer32):
    """Custom type acChDefaultV22ModemTransportType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("byPassEnable", 2),
          ("disable", 0),
          ("eventsOnly", 3),
          ("relayEnable", 1))
    )


_AcChDefaultV22ModemTransportType_Type.__name__ = "Integer32"
_AcChDefaultV22ModemTransportType_Object = MibScalar
acChDefaultV22ModemTransportType = _AcChDefaultV22ModemTransportType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 6, 13),
    _AcChDefaultV22ModemTransportType_Type()
)
acChDefaultV22ModemTransportType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acChDefaultV22ModemTransportType.setStatus("obsolete")


class _AcChDefaultV23ModemTransportType_Type(Integer32):
    """Custom type acChDefaultV23ModemTransportType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("byPassEnable", 2),
          ("disable", 0),
          ("eventsOnly", 3),
          ("relayEnable", 1))
    )


_AcChDefaultV23ModemTransportType_Type.__name__ = "Integer32"
_AcChDefaultV23ModemTransportType_Object = MibScalar
acChDefaultV23ModemTransportType = _AcChDefaultV23ModemTransportType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 6, 14),
    _AcChDefaultV23ModemTransportType_Type()
)
acChDefaultV23ModemTransportType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acChDefaultV23ModemTransportType.setStatus("obsolete")


class _AcChDefaultV32ModemTransportType_Type(Integer32):
    """Custom type acChDefaultV32ModemTransportType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("byPassEnable", 2),
          ("disable", 0),
          ("eventsOnly", 3),
          ("relayEnable", 1))
    )


_AcChDefaultV32ModemTransportType_Type.__name__ = "Integer32"
_AcChDefaultV32ModemTransportType_Object = MibScalar
acChDefaultV32ModemTransportType = _AcChDefaultV32ModemTransportType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 6, 15),
    _AcChDefaultV32ModemTransportType_Type()
)
acChDefaultV32ModemTransportType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acChDefaultV32ModemTransportType.setStatus("obsolete")


class _AcChDefaultV34ModemTransportType_Type(Integer32):
    """Custom type acChDefaultV34ModemTransportType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("byPassEnable", 2),
          ("disable", 0),
          ("eventsOnly", 3),
          ("relayEnable", 1))
    )


_AcChDefaultV34ModemTransportType_Type.__name__ = "Integer32"
_AcChDefaultV34ModemTransportType_Object = MibScalar
acChDefaultV34ModemTransportType = _AcChDefaultV34ModemTransportType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 6, 16),
    _AcChDefaultV34ModemTransportType_Type()
)
acChDefaultV34ModemTransportType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acChDefaultV34ModemTransportType.setStatus("obsolete")


class _AcChDefaultFaxModemBypassCoderType_Type(Integer32):
    """Custom type acChDefaultFaxModemBypassCoderType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("g711Alaw-64", 0),
          ("g711Mulaw", 1),
          ("g726-32", 4),
          ("g726-40", 5))
    )


_AcChDefaultFaxModemBypassCoderType_Type.__name__ = "Integer32"
_AcChDefaultFaxModemBypassCoderType_Object = MibScalar
acChDefaultFaxModemBypassCoderType = _AcChDefaultFaxModemBypassCoderType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 6, 17),
    _AcChDefaultFaxModemBypassCoderType_Type()
)
acChDefaultFaxModemBypassCoderType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acChDefaultFaxModemBypassCoderType.setStatus("obsolete")


class _AcChDefaultFaxRelayRedundancyDepth_Type(Integer32):
    """Custom type acChDefaultFaxRelayRedundancyDepth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcChDefaultFaxRelayRedundancyDepth_Type.__name__ = "Integer32"
_AcChDefaultFaxRelayRedundancyDepth_Object = MibScalar
acChDefaultFaxRelayRedundancyDepth = _AcChDefaultFaxRelayRedundancyDepth_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 6, 18),
    _AcChDefaultFaxRelayRedundancyDepth_Type()
)
acChDefaultFaxRelayRedundancyDepth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acChDefaultFaxRelayRedundancyDepth.setStatus("obsolete")


class _AcChDefaultT38ProtectionMode_Type(Integer32):
    """Custom type acChDefaultT38ProtectionMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("fEC", 1),
          ("redundancyPackets", 0))
    )


_AcChDefaultT38ProtectionMode_Type.__name__ = "Integer32"
_AcChDefaultT38ProtectionMode_Object = MibScalar
acChDefaultT38ProtectionMode = _AcChDefaultT38ProtectionMode_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 6, 19),
    _AcChDefaultT38ProtectionMode_Type()
)
acChDefaultT38ProtectionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acChDefaultT38ProtectionMode.setStatus("obsolete")


class _AcChDefaultDTMFVolume_Type(Integer32):
    """Custom type acChDefaultDTMFVolume based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-31, 0),
    )


_AcChDefaultDTMFVolume_Type.__name__ = "Integer32"
_AcChDefaultDTMFVolume_Object = MibScalar
acChDefaultDTMFVolume = _AcChDefaultDTMFVolume_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 6, 20),
    _AcChDefaultDTMFVolume_Type()
)
acChDefaultDTMFVolume.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acChDefaultDTMFVolume.setStatus("obsolete")


class _AcChDefaultDTMFTransportType_Type(Integer32):
    """Custom type acChDefaultDTMFTransportType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              7)
        )
    )
    namedValues = NamedValues(
        *(("acMuteDTMF", 0),
          ("acRFC2833RalayDTMF", 3),
          ("acRFC2833RelayDecoderMute", 7),
          ("acRelayDTMF", 1),
          ("acTransparentDTMF", 2))
    )


_AcChDefaultDTMFTransportType_Type.__name__ = "Integer32"
_AcChDefaultDTMFTransportType_Object = MibScalar
acChDefaultDTMFTransportType = _AcChDefaultDTMFTransportType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 6, 21),
    _AcChDefaultDTMFTransportType_Type()
)
acChDefaultDTMFTransportType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acChDefaultDTMFTransportType.setStatus("obsolete")


class _AcChDefaultMFTransportType_Type(Integer32):
    """Custom type acChDefaultMFTransportType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("acMuteMF", 0),
          ("acRFC2833RalayMF", 3),
          ("acRelayMF", 1),
          ("acTransparentMF", 2))
    )


_AcChDefaultMFTransportType_Type.__name__ = "Integer32"
_AcChDefaultMFTransportType_Object = MibScalar
acChDefaultMFTransportType = _AcChDefaultMFTransportType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 6, 22),
    _AcChDefaultMFTransportType_Type()
)
acChDefaultMFTransportType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acChDefaultMFTransportType.setStatus("obsolete")


class _AcChDefaultInputGain_Type(Integer32):
    """Custom type acChDefaultInputGain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32, 31),
    )


_AcChDefaultInputGain_Type.__name__ = "Integer32"
_AcChDefaultInputGain_Object = MibScalar
acChDefaultInputGain = _AcChDefaultInputGain_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 6, 23),
    _AcChDefaultInputGain_Type()
)
acChDefaultInputGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acChDefaultInputGain.setStatus("obsolete")


class _AcChDefaultRTPRedundancyDepth_Type(Integer32):
    """Custom type acChDefaultRTPRedundancyDepth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AcChDefaultRTPRedundancyDepth_Type.__name__ = "Integer32"
_AcChDefaultRTPRedundancyDepth_Object = MibScalar
acChDefaultRTPRedundancyDepth = _AcChDefaultRTPRedundancyDepth_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 6, 24),
    _AcChDefaultRTPRedundancyDepth_Type()
)
acChDefaultRTPRedundancyDepth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acChDefaultRTPRedundancyDepth.setStatus("obsolete")


class _AcChDefaultTestMode_Type(Integer32):
    """Custom type acChDefaultTestMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("coderLoopback", 0),
          ("noLoopback", 3),
          ("pCMLoopback", 1),
          ("toneInjection", 2))
    )


_AcChDefaultTestMode_Type.__name__ = "Integer32"
_AcChDefaultTestMode_Object = MibScalar
acChDefaultTestMode = _AcChDefaultTestMode_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 6, 25),
    _AcChDefaultTestMode_Type()
)
acChDefaultTestMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acChDefaultTestMode.setStatus("obsolete")


class _AcChDefaultVoiceVolume_Type(Integer32):
    """Custom type acChDefaultVoiceVolume based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32, 31),
    )


_AcChDefaultVoiceVolume_Type.__name__ = "Integer32"
_AcChDefaultVoiceVolume_Object = MibScalar
acChDefaultVoiceVolume = _AcChDefaultVoiceVolume_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 6, 26),
    _AcChDefaultVoiceVolume_Type()
)
acChDefaultVoiceVolume.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acChDefaultVoiceVolume.setStatus("obsolete")


class _AcChDefaultM_Type(Integer32):
    """Custom type acChDefaultM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_AcChDefaultM_Type.__name__ = "Integer32"
_AcChDefaultM_Object = MibScalar
acChDefaultM = _AcChDefaultM_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 6, 27),
    _AcChDefaultM_Type()
)
acChDefaultM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acChDefaultM.setStatus("obsolete")


class _AcChDefaultFlashHookPeriod_Type(Integer32):
    """Custom type acChDefaultFlashHookPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AcChDefaultFlashHookPeriod_Type.__name__ = "Integer32"
_AcChDefaultFlashHookPeriod_Object = MibScalar
acChDefaultFlashHookPeriod = _AcChDefaultFlashHookPeriod_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 6, 28),
    _AcChDefaultFlashHookPeriod_Type()
)
acChDefaultFlashHookPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acChDefaultFlashHookPeriod.setStatus("obsolete")


class _AcChDefaultDTMFDetectionPoint_Type(Integer32):
    """Custom type acChDefaultDTMFDetectionPoint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AcChDefaultDTMFDetectionPoint_Type.__name__ = "Integer32"
_AcChDefaultDTMFDetectionPoint_Object = MibScalar
acChDefaultDTMFDetectionPoint = _AcChDefaultDTMFDetectionPoint_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 6, 29),
    _AcChDefaultDTMFDetectionPoint_Type()
)
acChDefaultDTMFDetectionPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acChDefaultDTMFDetectionPoint.setStatus("obsolete")


class _AcChDefaultRtpIpTos_Type(Integer32):
    """Custom type acChDefaultRtpIpTos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_AcChDefaultRtpIpTos_Type.__name__ = "Integer32"
_AcChDefaultRtpIpTos_Object = MibScalar
acChDefaultRtpIpTos = _AcChDefaultRtpIpTos_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 6, 30),
    _AcChDefaultRtpIpTos_Type()
)
acChDefaultRtpIpTos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acChDefaultRtpIpTos.setStatus("obsolete")


class _AcChDefaultRtpIpPrecedence_Type(Integer32):
    """Custom type acChDefaultRtpIpPrecedence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AcChDefaultRtpIpPrecedence_Type.__name__ = "Integer32"
_AcChDefaultRtpIpPrecedence_Object = MibScalar
acChDefaultRtpIpPrecedence = _AcChDefaultRtpIpPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 6, 31),
    _AcChDefaultRtpIpPrecedence_Type()
)
acChDefaultRtpIpPrecedence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acChDefaultRtpIpPrecedence.setStatus("obsolete")


class _AcChDefaultEchoCancler_Type(Integer32):
    """Custom type acChDefaultEchoCancler based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AcChDefaultEchoCancler_Type.__name__ = "Integer32"
_AcChDefaultEchoCancler_Object = MibScalar
acChDefaultEchoCancler = _AcChDefaultEchoCancler_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 6, 32),
    _AcChDefaultEchoCancler_Type()
)
acChDefaultEchoCancler.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acChDefaultEchoCancler.setStatus("obsolete")


class _AcChDefaultSilenceSuppression_Type(Integer32):
    """Custom type acChDefaultSilenceSuppression based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sILENCE-COMPRESION-DISABLE", 0),
          ("sILENCE-COMPRESION-ENABLE", 1),
          ("sILENCE-COMPRESION-ENABLE-NOISE-ADAPTATION-DISABLE", 2))
    )


_AcChDefaultSilenceSuppression_Type.__name__ = "Integer32"
_AcChDefaultSilenceSuppression_Object = MibScalar
acChDefaultSilenceSuppression = _AcChDefaultSilenceSuppression_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 6, 33),
    _AcChDefaultSilenceSuppression_Type()
)
acChDefaultSilenceSuppression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acChDefaultSilenceSuppression.setStatus("obsolete")


class _AcChDefaultEchoCanclerHybridLoss_Type(Integer32):
    """Custom type acChDefaultEchoCanclerHybridLoss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("eCHybridLoss0DBM", 2),
          ("eCHybridLoss3DBM", 3),
          ("eCHybridLoss6DBM", 0),
          ("eCHybridLoss9DBM", 1))
    )


_AcChDefaultEchoCanclerHybridLoss_Type.__name__ = "Integer32"
_AcChDefaultEchoCanclerHybridLoss_Object = MibScalar
acChDefaultEchoCanclerHybridLoss = _AcChDefaultEchoCanclerHybridLoss_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 6, 34),
    _AcChDefaultEchoCanclerHybridLoss_Type()
)
acChDefaultEchoCanclerHybridLoss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acChDefaultEchoCanclerHybridLoss.setStatus("obsolete")


class _AcChDefaultPacketizationPeriod_Type(Integer32):
    """Custom type acChDefaultPacketizationPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 80),
    )


_AcChDefaultPacketizationPeriod_Type.__name__ = "Integer32"
_AcChDefaultPacketizationPeriod_Object = MibScalar
acChDefaultPacketizationPeriod = _AcChDefaultPacketizationPeriod_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 6, 35),
    _AcChDefaultPacketizationPeriod_Type()
)
acChDefaultPacketizationPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acChDefaultPacketizationPeriod.setStatus("obsolete")
_ATMSettings_ObjectIdentity = ObjectIdentity
aTMSettings = _ATMSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 7)
)


class _VPMask_Type(Integer32):
    """Custom type vPMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VPMask_Type.__name__ = "Integer32"
_VPMask_Object = MibScalar
vPMask = _VPMask_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 7, 1),
    _VPMask_Type()
)
vPMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vPMask.setStatus("obsolete")


class _VCMask_Type(Integer32):
    """Custom type vCMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_VCMask_Type.__name__ = "Integer32"
_VCMask_Object = MibScalar
vCMask = _VCMask_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 7, 2),
    _VCMask_Type()
)
vCMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vCMask.setStatus("obsolete")


class _ExternalClk_Type(Integer32):
    """Custom type externalClk based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("acATMUtopiaExternalClock", 1),
          ("acATMUtopiaInternalClock", 0))
    )


_ExternalClk_Type.__name__ = "Integer32"
_ExternalClk_Object = MibScalar
externalClk = _ExternalClk_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 7, 3),
    _ExternalClk_Type()
)
externalClk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalClk.setStatus("obsolete")


class _ATMLoopBack_Type(Integer32):
    """Custom type aTMLoopBack based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("loopbackDisabled", 0),
          ("loopbackEnabled", 1))
    )


_ATMLoopBack_Type.__name__ = "Integer32"
_ATMLoopBack_Object = MibScalar
aTMLoopBack = _ATMLoopBack_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 7, 4),
    _ATMLoopBack_Type()
)
aTMLoopBack.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aTMLoopBack.setStatus("obsolete")


class _UtopiaSlave_Type(Integer32):
    """Custom type utopiaSlave based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("aTM-UTOPIA-MASTER", 0),
          ("aTM-UTOPIA-SLAVE", 1))
    )


_UtopiaSlave_Type.__name__ = "Integer32"
_UtopiaSlave_Object = MibScalar
utopiaSlave = _UtopiaSlave_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 7, 5),
    _UtopiaSlave_Type()
)
utopiaSlave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    utopiaSlave.setStatus("obsolete")


class _MultyPhy_Type(Integer32):
    """Custom type multyPhy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("multiPhy", 1),
          ("singlePhy", 0))
    )


_MultyPhy_Type.__name__ = "Integer32"
_MultyPhy_Object = MibScalar
multyPhy = _MultyPhy_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 7, 6),
    _MultyPhy_Type()
)
multyPhy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    multyPhy.setStatus("obsolete")


class _SlavePhyNum_Type(Integer32):
    """Custom type slavePhyNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 31),
    )


_SlavePhyNum_Type.__name__ = "Integer32"
_SlavePhyNum_Object = MibScalar
slavePhyNum = _SlavePhyNum_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 7, 7),
    _SlavePhyNum_Type()
)
slavePhyNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slavePhyNum.setStatus("obsolete")


class _UtopiaBus16_Type(Integer32):
    """Custom type utopiaBus16 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("acATMUtopiaBusWidth16bit", 0),
          ("acATMUtopiaBusWidth8bit", 1))
    )


_UtopiaBus16_Type.__name__ = "Integer32"
_UtopiaBus16_Object = MibScalar
utopiaBus16 = _UtopiaBus16_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 7, 8),
    _UtopiaBus16_Type()
)
utopiaBus16.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    utopiaBus16.setStatus("obsolete")


class _ATMPHYType_Type(Integer32):
    """Custom type aTMPHYType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("acOC3", 0),
          ("acUtopia", 1))
    )


_ATMPHYType_Type.__name__ = "Integer32"
_ATMPHYType_Object = MibScalar
aTMPHYType = _ATMPHYType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 7, 9),
    _ATMPHYType_Type()
)
aTMPHYType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aTMPHYType.setStatus("obsolete")


class _DisablePayloadScrambling_Type(Integer32):
    """Custom type disablePayloadScrambling based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 0))
    )


_DisablePayloadScrambling_Type.__name__ = "Integer32"
_DisablePayloadScrambling_Object = MibScalar
disablePayloadScrambling = _DisablePayloadScrambling_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 7, 10),
    _DisablePayloadScrambling_Type()
)
disablePayloadScrambling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    disablePayloadScrambling.setStatus("obsolete")


class _PHYClkSource_Type(Integer32):
    """Custom type pHYClkSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("acPhyExternalClock", 1),
          ("acPhyInternalClock", 0))
    )


_PHYClkSource_Type.__name__ = "Integer32"
_PHYClkSource_Object = MibScalar
pHYClkSource = _PHYClkSource_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 7, 11),
    _PHYClkSource_Type()
)
pHYClkSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pHYClkSource.setStatus("obsolete")


class _SendIdleCASUponLinkFail_Type(Integer32):
    """Custom type sendIdleCASUponLinkFail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("acATMSendIdleCASUponLinkFail-Disabled", 0),
          ("acATMSendIdleCASUponLinkFail-Enabled", 1))
    )


_SendIdleCASUponLinkFail_Type.__name__ = "Integer32"
_SendIdleCASUponLinkFail_Object = MibScalar
sendIdleCASUponLinkFail = _SendIdleCASUponLinkFail_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 7, 12),
    _SendIdleCASUponLinkFail_Type()
)
sendIdleCASUponLinkFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sendIdleCASUponLinkFail.setStatus("obsolete")


class _MasterSlaveMode_Type(Integer32):
    """Custom type masterSlaveMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("acATM-MasterMode-CO-IWF", 0),
          ("acATM-SlaveMode-CP-IWF", 1))
    )


_MasterSlaveMode_Type.__name__ = "Integer32"
_MasterSlaveMode_Object = MibScalar
masterSlaveMode = _MasterSlaveMode_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 7, 13),
    _MasterSlaveMode_Type()
)
masterSlaveMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    masterSlaveMode.setStatus("obsolete")


class _VccProfile_Type(Integer32):
    """Custom type vccProfile based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ac105VCCs-24CIDsperVCC", 1),
          ("ac14VCCs-240CIDsperVCC", 3),
          ("ac240VCCs-8CIDsperVCC", 0),
          ("ac84VCCs-32CIDsperVCC", 2))
    )


_VccProfile_Type.__name__ = "Integer32"
_VccProfile_Object = MibScalar
vccProfile = _VccProfile_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 7, 14),
    _VccProfile_Type()
)
vccProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vccProfile.setStatus("obsolete")


class _TPNCPVPI_Type(Integer32):
    """Custom type tPNCPVPI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_TPNCPVPI_Type.__name__ = "Integer32"
_TPNCPVPI_Object = MibScalar
tPNCPVPI = _TPNCPVPI_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 7, 15),
    _TPNCPVPI_Type()
)
tPNCPVPI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tPNCPVPI.setStatus("obsolete")


class _TPNCPVCI_Type(Integer32):
    """Custom type tPNCPVCI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_TPNCPVCI_Type.__name__ = "Integer32"
_TPNCPVCI_Object = MibScalar
tPNCPVCI = _TPNCPVCI_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 7, 16),
    _TPNCPVCI_Type()
)
tPNCPVCI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tPNCPVCI.setStatus("obsolete")


class _SAALLink0VPI_Type(Integer32):
    """Custom type sAALLink0VPI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SAALLink0VPI_Type.__name__ = "Integer32"
_SAALLink0VPI_Object = MibScalar
sAALLink0VPI = _SAALLink0VPI_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 7, 17),
    _SAALLink0VPI_Type()
)
sAALLink0VPI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sAALLink0VPI.setStatus("obsolete")


class _SAALLink0VCI_Type(Integer32):
    """Custom type sAALLink0VCI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SAALLink0VCI_Type.__name__ = "Integer32"
_SAALLink0VCI_Object = MibScalar
sAALLink0VCI = _SAALLink0VCI_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 7, 18),
    _SAALLink0VCI_Type()
)
sAALLink0VCI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sAALLink0VCI.setStatus("obsolete")


class _SAALLink1VPI_Type(Integer32):
    """Custom type sAALLink1VPI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SAALLink1VPI_Type.__name__ = "Integer32"
_SAALLink1VPI_Object = MibScalar
sAALLink1VPI = _SAALLink1VPI_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 7, 19),
    _SAALLink1VPI_Type()
)
sAALLink1VPI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sAALLink1VPI.setStatus("obsolete")


class _SAALLink1VCI_Type(Integer32):
    """Custom type sAALLink1VCI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SAALLink1VCI_Type.__name__ = "Integer32"
_SAALLink1VCI_Object = MibScalar
sAALLink1VCI = _SAALLink1VCI_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 7, 20),
    _SAALLink1VCI_Type()
)
sAALLink1VCI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sAALLink1VCI.setStatus("obsolete")
_AcSS7Settings_ObjectIdentity = ObjectIdentity
acSS7Settings = _AcSS7Settings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 8)
)
_AcSS7SettingsTable_Object = MibTable
acSS7SettingsTable = _AcSS7SettingsTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 8, 1)
)
if mibBuilder.loadTexts:
    acSS7SettingsTable.setStatus("obsolete")
_AcSS7SettingsEntry_Object = MibTableRow
acSS7SettingsEntry = _AcSS7SettingsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 8, 1, 1)
)
acSS7SettingsEntry.setIndexNames(
    (0, "AcBoard", "acSS7LinkId"),
)
if mibBuilder.loadTexts:
    acSS7SettingsEntry.setStatus("obsolete")


class _AcSS7LinkId_Type(Integer32):
    """Custom type acSS7LinkId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_AcSS7LinkId_Type.__name__ = "Integer32"
_AcSS7LinkId_Object = MibTableColumn
acSS7LinkId = _AcSS7LinkId_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 8, 1, 1, 1),
    _AcSS7LinkId_Type()
)
acSS7LinkId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSS7LinkId.setStatus("obsolete")


class _AcSS7traceLevel_Type(Integer32):
    """Custom type acSS7traceLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              9,
              10,
              11,
              12,
              15)
        )
    )
    namedValues = NamedValues(
        *(("acFULL-TRACE", 1),
          ("acISDN-IUA-TRACE", 9),
          ("acNO-TRACE", 0),
          ("acSS7-AAL", 15),
          ("acSS7-MTP2", 10),
          ("acSS7-MTP2-AND-APPLI", 11),
          ("acSS7-MTP2-SL-L3-NO-MSU", 12))
    )


_AcSS7traceLevel_Type.__name__ = "Integer32"
_AcSS7traceLevel_Object = MibTableColumn
acSS7traceLevel = _AcSS7traceLevel_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 8, 1, 1, 2),
    _AcSS7traceLevel_Type()
)
acSS7traceLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSS7traceLevel.setStatus("obsolete")
_AcConfigFiles_ObjectIdentity = ObjectIdentity
acConfigFiles = _AcConfigFiles_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 11)
)


class _AcFxsCoefficients_Type(OctetString):
    """Custom type acFxsCoefficients based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AcFxsCoefficients_Type.__name__ = "OctetString"
_AcFxsCoefficients_Object = MibScalar
acFxsCoefficients = _AcFxsCoefficients_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 11, 1),
    _AcFxsCoefficients_Type()
)
acFxsCoefficients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acFxsCoefficients.setStatus("obsolete")


class _AcFxoCoefficients_Type(OctetString):
    """Custom type acFxoCoefficients based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AcFxoCoefficients_Type.__name__ = "OctetString"
_AcFxoCoefficients_Object = MibScalar
acFxoCoefficients = _AcFxoCoefficients_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 11, 2),
    _AcFxoCoefficients_Type()
)
acFxoCoefficients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acFxoCoefficients.setStatus("obsolete")


class _AcCptFile_Type(OctetString):
    """Custom type acCptFile based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AcCptFile_Type.__name__ = "OctetString"
_AcCptFile_Object = MibScalar
acCptFile = _AcCptFile_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 11, 3),
    _AcCptFile_Type()
)
acCptFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acCptFile.setStatus("obsolete")


class _AcVpFile_Type(OctetString):
    """Custom type acVpFile based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AcVpFile_Type.__name__ = "OctetString"
_AcVpFile_Object = MibScalar
acVpFile = _AcVpFile_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 11, 4),
    _AcVpFile_Type()
)
acVpFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acVpFile.setStatus("obsolete")
_AcCasTables_ObjectIdentity = ObjectIdentity
acCasTables = _AcCasTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 11, 21)
)
_AcCasTablesTable_Object = MibTable
acCasTablesTable = _AcCasTablesTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 11, 21, 1)
)
if mibBuilder.loadTexts:
    acCasTablesTable.setStatus("obsolete")
_AcCasTablesEntry_Object = MibTableRow
acCasTablesEntry = _AcCasTablesEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 11, 21, 1, 1)
)
acCasTablesEntry.setIndexNames(
    (0, "AcBoard", "acCasTableIndex"),
)
if mibBuilder.loadTexts:
    acCasTablesEntry.setStatus("obsolete")


class _AcCasTableIndex_Type(Integer32):
    """Custom type acCasTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AcCasTableIndex_Type.__name__ = "Integer32"
_AcCasTableIndex_Object = MibTableColumn
acCasTableIndex = _AcCasTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 11, 21, 1, 1, 1),
    _AcCasTableIndex_Type()
)
acCasTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acCasTableIndex.setStatus("obsolete")


class _AcCasTabeName_Type(OctetString):
    """Custom type acCasTabeName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AcCasTabeName_Type.__name__ = "OctetString"
_AcCasTabeName_Object = MibTableColumn
acCasTabeName = _AcCasTabeName_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 11, 21, 1, 1, 2),
    _AcCasTabeName_Type()
)
acCasTabeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acCasTabeName.setStatus("obsolete")
_AcFxs_ObjectIdentity = ObjectIdentity
acFxs = _AcFxs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 12)
)


class _AcPolarityReversalType_Type(Integer32):
    """Custom type acPolarityReversalType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("hard", 1),
          ("soft", 0))
    )


_AcPolarityReversalType_Type.__name__ = "Integer32"
_AcPolarityReversalType_Object = MibScalar
acPolarityReversalType = _AcPolarityReversalType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 12, 1),
    _AcPolarityReversalType_Type()
)
acPolarityReversalType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPolarityReversalType.setStatus("obsolete")
_MegacoSettings_ObjectIdentity = ObjectIdentity
megacoSettings = _MegacoSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 13)
)


class _MegacoCurrentProfile_Type(Integer32):
    """Custom type megacoCurrentProfile based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_MegacoCurrentProfile_Type.__name__ = "Integer32"
_MegacoCurrentProfile_Object = MibScalar
megacoCurrentProfile = _MegacoCurrentProfile_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 13, 1),
    _MegacoCurrentProfile_Type()
)
megacoCurrentProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    megacoCurrentProfile.setStatus("obsolete")


class _MegacoGatewayName_Type(OctetString):
    """Custom type megacoGatewayName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_MegacoGatewayName_Type.__name__ = "OctetString"
_MegacoGatewayName_Object = MibScalar
megacoGatewayName = _MegacoGatewayName_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 13, 2),
    _MegacoGatewayName_Type()
)
megacoGatewayName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    megacoGatewayName.setStatus("obsolete")


class _MegacoEndpointName_Type(OctetString):
    """Custom type megacoEndpointName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_MegacoEndpointName_Type.__name__ = "OctetString"
_MegacoEndpointName_Object = MibScalar
megacoEndpointName = _MegacoEndpointName_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 13, 3),
    _MegacoEndpointName_Type()
)
megacoEndpointName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    megacoEndpointName.setStatus("obsolete")


class _MegacoTrunkName_Type(OctetString):
    """Custom type megacoTrunkName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_MegacoTrunkName_Type.__name__ = "OctetString"
_MegacoTrunkName_Object = MibScalar
megacoTrunkName = _MegacoTrunkName_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 13, 4),
    _MegacoTrunkName_Type()
)
megacoTrunkName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    megacoTrunkName.setStatus("obsolete")


class _MegacoActiveCallAgentIp_Type(OctetString):
    """Custom type megacoActiveCallAgentIp based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_MegacoActiveCallAgentIp_Type.__name__ = "OctetString"
_MegacoActiveCallAgentIp_Object = MibScalar
megacoActiveCallAgentIp = _MegacoActiveCallAgentIp_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 13, 5),
    _MegacoActiveCallAgentIp_Type()
)
megacoActiveCallAgentIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    megacoActiveCallAgentIp.setStatus("obsolete")


class _MegacoActiveCallAgentPort_Type(Integer32):
    """Custom type megacoActiveCallAgentPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_MegacoActiveCallAgentPort_Type.__name__ = "Integer32"
_MegacoActiveCallAgentPort_Object = MibScalar
megacoActiveCallAgentPort = _MegacoActiveCallAgentPort_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 13, 6),
    _MegacoActiveCallAgentPort_Type()
)
megacoActiveCallAgentPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    megacoActiveCallAgentPort.setStatus("obsolete")
_MegacoCallAgents_ObjectIdentity = ObjectIdentity
megacoCallAgents = _MegacoCallAgents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 13, 7)
)
_MegacoCallAgentsTable_Object = MibTable
megacoCallAgentsTable = _MegacoCallAgentsTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 13, 7, 1)
)
if mibBuilder.loadTexts:
    megacoCallAgentsTable.setStatus("obsolete")
_MegacoCallAgentsEntry_Object = MibTableRow
megacoCallAgentsEntry = _MegacoCallAgentsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 13, 7, 1, 1)
)
megacoCallAgentsEntry.setIndexNames(
    (0, "AcBoard", "megacoCallAgentId"),
)
if mibBuilder.loadTexts:
    megacoCallAgentsEntry.setStatus("obsolete")


class _MegacoCallAgentId_Type(Integer32):
    """Custom type megacoCallAgentId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_MegacoCallAgentId_Type.__name__ = "Integer32"
_MegacoCallAgentId_Object = MibTableColumn
megacoCallAgentId = _MegacoCallAgentId_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 13, 7, 1, 1, 1),
    _MegacoCallAgentId_Type()
)
megacoCallAgentId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    megacoCallAgentId.setStatus("obsolete")


class _MegacoCallAgentIp_Type(OctetString):
    """Custom type megacoCallAgentIp based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_MegacoCallAgentIp_Type.__name__ = "OctetString"
_MegacoCallAgentIp_Object = MibTableColumn
megacoCallAgentIp = _MegacoCallAgentIp_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 13, 7, 1, 1, 2),
    _MegacoCallAgentIp_Type()
)
megacoCallAgentIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    megacoCallAgentIp.setStatus("obsolete")


class _MegacoCallAgentPort_Type(Integer32):
    """Custom type megacoCallAgentPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_MegacoCallAgentPort_Type.__name__ = "Integer32"
_MegacoCallAgentPort_Object = MibTableColumn
megacoCallAgentPort = _MegacoCallAgentPort_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 13, 7, 1, 1, 3),
    _MegacoCallAgentPort_Type()
)
megacoCallAgentPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    megacoCallAgentPort.setStatus("obsolete")


class _MegacoCallAgentIsUsed_Type(Integer32):
    """Custom type megacoCallAgentIsUsed based on Integer32"""
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


_MegacoCallAgentIsUsed_Type.__name__ = "Integer32"
_MegacoCallAgentIsUsed_Object = MibTableColumn
megacoCallAgentIsUsed = _MegacoCallAgentIsUsed_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 13, 7, 1, 1, 4),
    _MegacoCallAgentIsUsed_Type()
)
megacoCallAgentIsUsed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    megacoCallAgentIsUsed.setStatus("obsolete")


class _MegacoCheckLegalityOfMGC_Type(Integer32):
    """Custom type megacoCheckLegalityOfMGC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_MegacoCheckLegalityOfMGC_Type.__name__ = "Integer32"
_MegacoCheckLegalityOfMGC_Object = MibScalar
megacoCheckLegalityOfMGC = _MegacoCheckLegalityOfMGC_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 13, 8),
    _MegacoCheckLegalityOfMGC_Type()
)
megacoCheckLegalityOfMGC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    megacoCheckLegalityOfMGC.setStatus("obsolete")
_AcPSTNParameters_ObjectIdentity = ObjectIdentity
acPSTNParameters = _AcPSTNParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 14)
)


class _AcQ931RELAYMODE_Type(Integer32):
    """Custom type acQ931RELAYMODE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("activateLAPDmessaging", 1),
          ("layer3-IS-IUA", 3),
          ("none", 0))
    )


_AcQ931RELAYMODE_Type.__name__ = "Integer32"
_AcQ931RELAYMODE_Object = MibScalar
acQ931RELAYMODE = _AcQ931RELAYMODE_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 14, 1),
    _AcQ931RELAYMODE_Type()
)
acQ931RELAYMODE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acQ931RELAYMODE.setStatus("obsolete")


class _AcIsdnDuplicateQ931BuffMode_Type(Integer32):
    """Custom type acIsdnDuplicateQ931BuffMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AcIsdnDuplicateQ931BuffMode_Type.__name__ = "Integer32"
_AcIsdnDuplicateQ931BuffMode_Object = MibScalar
acIsdnDuplicateQ931BuffMode = _AcIsdnDuplicateQ931BuffMode_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 14, 2),
    _AcIsdnDuplicateQ931BuffMode_Type()
)
acIsdnDuplicateQ931BuffMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acIsdnDuplicateQ931BuffMode.setStatus("obsolete")


class _AcPSTNCASTableNum_Type(Integer32):
    """Custom type acPSTNCASTableNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_AcPSTNCASTableNum_Type.__name__ = "Integer32"
_AcPSTNCASTableNum_Object = MibScalar
acPSTNCASTableNum = _AcPSTNCASTableNum_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 14, 3),
    _AcPSTNCASTableNum_Type()
)
acPSTNCASTableNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPSTNCASTableNum.setStatus("obsolete")
_AMsConfiguration_ObjectIdentity = ObjectIdentity
aMsConfiguration = _AMsConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 51)
)


class _AmsNumOfConferencePorts_Type(Integer32):
    """Custom type amsNumOfConferencePorts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 480),
    )


_AmsNumOfConferencePorts_Type.__name__ = "Integer32"
_AmsNumOfConferencePorts_Object = MibScalar
amsNumOfConferencePorts = _AmsNumOfConferencePorts_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 51, 1),
    _AmsNumOfConferencePorts_Type()
)
amsNumOfConferencePorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    amsNumOfConferencePorts.setStatus("obsolete")


class _AmsNumOfTestTrunkPorts_Type(Integer32):
    """Custom type amsNumOfTestTrunkPorts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 480),
    )


_AmsNumOfTestTrunkPorts_Type.__name__ = "Integer32"
_AmsNumOfTestTrunkPorts_Object = MibScalar
amsNumOfTestTrunkPorts = _AmsNumOfTestTrunkPorts_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 51, 2),
    _AmsNumOfTestTrunkPorts_Type()
)
amsNumOfTestTrunkPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    amsNumOfTestTrunkPorts.setStatus("obsolete")


class _AmsNumOfLawfulInterceptPorts_Type(Integer32):
    """Custom type amsNumOfLawfulInterceptPorts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 480),
    )


_AmsNumOfLawfulInterceptPorts_Type.__name__ = "Integer32"
_AmsNumOfLawfulInterceptPorts_Object = MibScalar
amsNumOfLawfulInterceptPorts = _AmsNumOfLawfulInterceptPorts_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 51, 3),
    _AmsNumOfLawfulInterceptPorts_Type()
)
amsNumOfLawfulInterceptPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    amsNumOfLawfulInterceptPorts.setStatus("obsolete")


class _AmsNumOfAnnouncementPorts_Type(Integer32):
    """Custom type amsNumOfAnnouncementPorts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 480),
    )


_AmsNumOfAnnouncementPorts_Type.__name__ = "Integer32"
_AmsNumOfAnnouncementPorts_Object = MibScalar
amsNumOfAnnouncementPorts = _AmsNumOfAnnouncementPorts_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 51, 4),
    _AmsNumOfAnnouncementPorts_Type()
)
amsNumOfAnnouncementPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    amsNumOfAnnouncementPorts.setStatus("obsolete")
_AmsApsIpAddress_Type = IpAddress
_AmsApsIpAddress_Object = MibScalar
amsApsIpAddress = _AmsApsIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 51, 5),
    _AmsApsIpAddress_Type()
)
amsApsIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    amsApsIpAddress.setStatus("obsolete")


class _AmsApsPort_Type(Integer32):
    """Custom type amsApsPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64000),
    )


_AmsApsPort_Type.__name__ = "Integer32"
_AmsApsPort_Object = MibScalar
amsApsPort = _AmsApsPort_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 51, 6),
    _AmsApsPort_Type()
)
amsApsPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    amsApsPort.setStatus("obsolete")


class _AmsPrimaryLanguage_Type(Integer32):
    """Custom type amsPrimaryLanguage based on Integer32"""
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
              100)
        )
    )
    namedValues = NamedValues(
        *(("amsLangBad", 100),
          ("amsLangBelgianDutch", 0),
          ("amsLangCantonese", 1),
          ("isoLangBasque", 15),
          ("isoLangCatalan", 16),
          ("isoLangCzech", 19),
          ("isoLangDutch", 10),
          ("isoLangEnglish", 2),
          ("isoLangFrench", 3),
          ("isoLangGallegan", 17),
          ("isoLangGerman", 4),
          ("isoLangGreek", 20),
          ("isoLangHebrew", 18),
          ("isoLangItalian", 5),
          ("isoLangJapanese", 6),
          ("isoLangKorean", 7),
          ("isoLangMalay", 8),
          ("isoLangMandarin", 9),
          ("isoLangPortuguese", 11),
          ("isoLangSpanish", 12),
          ("isoLangTagalog", 13),
          ("isoLangThai", 14),
          ("isoLangTurkish", 21),
          ("isoLangVietnamese", 22))
    )


_AmsPrimaryLanguage_Type.__name__ = "Integer32"
_AmsPrimaryLanguage_Object = MibScalar
amsPrimaryLanguage = _AmsPrimaryLanguage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 51, 7),
    _AmsPrimaryLanguage_Type()
)
amsPrimaryLanguage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    amsPrimaryLanguage.setStatus("obsolete")


class _AmsSecondaryLanguage_Type(Integer32):
    """Custom type amsSecondaryLanguage based on Integer32"""
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
              100)
        )
    )
    namedValues = NamedValues(
        *(("amsLangBad", 100),
          ("amsLangBelgianDutch", 0),
          ("amsLangCantonese", 1),
          ("isoLangBasque", 15),
          ("isoLangCatalan", 16),
          ("isoLangCzech", 19),
          ("isoLangDutch", 10),
          ("isoLangEnglish", 2),
          ("isoLangFrench", 3),
          ("isoLangGallegan", 17),
          ("isoLangGerman", 4),
          ("isoLangGreek", 20),
          ("isoLangHebrew", 18),
          ("isoLangItalian", 5),
          ("isoLangJapanese", 6),
          ("isoLangKorean", 7),
          ("isoLangMalay", 8),
          ("isoLangMandarin", 9),
          ("isoLangPortuguese", 11),
          ("isoLangSpanish", 12),
          ("isoLangTagalog", 13),
          ("isoLangThai", 14),
          ("isoLangTurkish", 21),
          ("isoLangVietnamese", 22))
    )


_AmsSecondaryLanguage_Type.__name__ = "Integer32"
_AmsSecondaryLanguage_Object = MibScalar
amsSecondaryLanguage = _AmsSecondaryLanguage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 51, 8),
    _AmsSecondaryLanguage_Type()
)
amsSecondaryLanguage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    amsSecondaryLanguage.setStatus("obsolete")


class _AmsProfile_Type(Integer32):
    """Custom type amsProfile based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_AmsProfile_Type.__name__ = "Integer32"
_AmsProfile_Object = MibScalar
amsProfile = _AmsProfile_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 51, 9),
    _AmsProfile_Type()
)
amsProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    amsProfile.setStatus("obsolete")


class _AmsAASPackagesProfile_Type(Integer32):
    """Custom type amsAASPackagesProfile based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("h2489Standard", 1),
          ("td5Starndard", 0))
    )


_AmsAASPackagesProfile_Type.__name__ = "Integer32"
_AmsAASPackagesProfile_Object = MibScalar
amsAASPackagesProfile = _AmsAASPackagesProfile_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 51, 10),
    _AmsAASPackagesProfile_Type()
)
amsAASPackagesProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    amsAASPackagesProfile.setStatus("obsolete")
_AcFeatureKey_ObjectIdentity = ObjectIdentity
acFeatureKey = _AcFeatureKey_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 90)
)


class _AcFeatureKeyString_Type(OctetString):
    """Custom type acFeatureKeyString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_AcFeatureKeyString_Type.__name__ = "OctetString"
_AcFeatureKeyString_Object = MibScalar
acFeatureKeyString = _AcFeatureKeyString_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 90, 1),
    _AcFeatureKeyString_Type()
)
acFeatureKeyString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acFeatureKeyString.setStatus("obsolete")


class _AcActiveFeaturesList_Type(OctetString):
    """Custom type acActiveFeaturesList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 484),
    )


_AcActiveFeaturesList_Type.__name__ = "OctetString"
_AcActiveFeaturesList_Object = MibScalar
acActiveFeaturesList = _AcActiveFeaturesList_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 90, 2),
    _AcActiveFeaturesList_Type()
)
acActiveFeaturesList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acActiveFeaturesList.setStatus("obsolete")
_Supplementary_ObjectIdentity = ObjectIdentity
supplementary = _Supplementary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 99)
)


class _SupplementaryField_Type(OctetString):
    """Custom type supplementaryField based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SupplementaryField_Type.__name__ = "OctetString"
_SupplementaryField_Object = MibScalar
supplementaryField = _SupplementaryField_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 1, 99, 1),
    _SupplementaryField_Type()
)
supplementaryField.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    supplementaryField.setStatus("obsolete")
_BoardInformation_ObjectIdentity = ObjectIdentity
boardInformation = _BoardInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 2)
)


class _BoardType_Type(Integer32):
    """Custom type boardType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              8,
              10,
              11,
              12,
              13,
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
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56)
        )
    )
    namedValues = NamedValues(
        *(("aTP-1610", 53),
          ("aTP-260", 54),
          ("aTP-260-UN", 55),
          ("ipMedia3000", 48),
          ("mEDIAPACK-108", 2),
          ("mEDIAPACK-124", 3),
          ("mP-102", 26),
          ("mP-104", 25),
          ("mP-118", 56),
          ("mediant1000", 47),
          ("mediant3000", 49),
          ("stretto3000", 50),
          ("tP-02", 28),
          ("tP-04", 27),
          ("tP-08", 1),
          ("tP-1610-IpMedia", 30),
          ("tP-1610-SB", 29),
          ("tP-240", 8),
          ("tP-240-IpMedia", 21),
          ("tP-260", 42),
          ("tP-260-IpMedia-120Ch", 38),
          ("tP-260-IpMedia-30Ch", 36),
          ("tP-260-IpMedia-60Ch", 37),
          ("tP-260-UN", 43),
          ("tP-260-UN-IpMedia", 35),
          ("tP-260RT-IpMedia-120Ch", 41),
          ("tP-260RT-IpMedia-30Ch", 39),
          ("tP-260RT-IpMedia-60Ch", 40),
          ("tP-2810", 34),
          ("tP-600", 11),
          ("tP-600-IPMEDIA", 12),
          ("tP-610-CL120", 10),
          ("tP-6310", 45),
          ("tP-6310-IpMedia", 51),
          ("tP-6310-SB", 52),
          ("tP-9800-C", 13),
          ("tP-IPMServer2000", 33),
          ("tP-MEDIANT2000", 31),
          ("tP-STRETTO2000", 32),
          ("tP1600", 20),
          ("tP1610", 24),
          ("tPM1100", 22),
          ("tPM1100-PCM", 44),
          ("tPM6300", 46),
          ("tPM800", 16),
          ("tPM800-RDK", 17),
          ("tPM800B", 18),
          ("tPM800B-RDK", 19),
          ("trunkPack-260-IpMedia", 23),
          ("unKnownBoard", 0))
    )


_BoardType_Type.__name__ = "Integer32"
_BoardType_Object = MibScalar
boardType = _BoardType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 2, 1),
    _BoardType_Type()
)
boardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardType.setStatus("obsolete")


class _BoardName_Type(OctetString):
    """Custom type boardName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_BoardName_Type.__name__ = "OctetString"
_BoardName_Object = MibScalar
boardName = _BoardName_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 2, 2),
    _BoardName_Type()
)
boardName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardName.setStatus("obsolete")


class _SerialNum_Type(Integer32):
    """Custom type serialNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SerialNum_Type.__name__ = "Integer32"
_SerialNum_Object = MibScalar
serialNum = _SerialNum_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 2, 3),
    _SerialNum_Type()
)
serialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialNum.setStatus("obsolete")


class _DSPCount_Type(Integer32):
    """Custom type dSPCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DSPCount_Type.__name__ = "Integer32"
_DSPCount_Object = MibScalar
dSPCount = _DSPCount_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 2, 4),
    _DSPCount_Type()
)
dSPCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dSPCount.setStatus("obsolete")


class _ChannelsCount_Type(Integer32):
    """Custom type channelsCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ChannelsCount_Type.__name__ = "Integer32"
_ChannelsCount_Object = MibScalar
channelsCount = _ChannelsCount_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 2, 5),
    _ChannelsCount_Type()
)
channelsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelsCount.setStatus("obsolete")


class _CPUSpeed_Type(Integer32):
    """Custom type cPUSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CPUSpeed_Type.__name__ = "Integer32"
_CPUSpeed_Object = MibScalar
cPUSpeed = _CPUSpeed_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 2, 6),
    _CPUSpeed_Type()
)
cPUSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPUSpeed.setStatus("obsolete")


class _SoftwareVersion_Type(OctetString):
    """Custom type softwareVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SoftwareVersion_Type.__name__ = "OctetString"
_SoftwareVersion_Object = MibScalar
softwareVersion = _SoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 2, 7),
    _SoftwareVersion_Type()
)
softwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareVersion.setStatus("obsolete")


class _TrunkPackSoftwareDate_Type(OctetString):
    """Custom type trunkPackSoftwareDate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_TrunkPackSoftwareDate_Type.__name__ = "OctetString"
_TrunkPackSoftwareDate_Object = MibScalar
trunkPackSoftwareDate = _TrunkPackSoftwareDate_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 2, 8),
    _TrunkPackSoftwareDate_Type()
)
trunkPackSoftwareDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkPackSoftwareDate.setStatus("obsolete")


class _SlotNumber_Type(Integer32):
    """Custom type slotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SlotNumber_Type.__name__ = "Integer32"
_SlotNumber_Object = MibScalar
slotNumber = _SlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 2, 9),
    _SlotNumber_Type()
)
slotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotNumber.setStatus("obsolete")


class _IniFileVersion_Type(Integer32):
    """Custom type iniFileVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IniFileVersion_Type.__name__ = "Integer32"
_IniFileVersion_Object = MibScalar
iniFileVersion = _IniFileVersion_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 2, 10),
    _IniFileVersion_Type()
)
iniFileVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iniFileVersion.setStatus("obsolete")


class _AcDspType_Type(Integer32):
    """Custom type acDspType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcDspType_Type.__name__ = "Integer32"
_AcDspType_Object = MibScalar
acDspType = _AcDspType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 2, 11),
    _AcDspType_Type()
)
acDspType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDspType.setStatus("obsolete")


class _AcFlashVersion_Type(Integer32):
    """Custom type acFlashVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcFlashVersion_Type.__name__ = "Integer32"
_AcFlashVersion_Object = MibScalar
acFlashVersion = _AcFlashVersion_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 2, 12),
    _AcFlashVersion_Type()
)
acFlashVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acFlashVersion.setStatus("obsolete")


class _AcBoardFxsOrFxo_Type(Integer32):
    """Custom type acBoardFxsOrFxo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("fXO", 0),
          ("fXS", 1))
    )


_AcBoardFxsOrFxo_Type.__name__ = "Integer32"
_AcBoardFxsOrFxo_Object = MibScalar
acBoardFxsOrFxo = _AcBoardFxsOrFxo_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 2, 13),
    _AcBoardFxsOrFxo_Type()
)
acBoardFxsOrFxo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acBoardFxsOrFxo.setStatus("obsolete")


class _AcTrunkslCount_Type(Integer32):
    """Custom type acTrunkslCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcTrunkslCount_Type.__name__ = "Integer32"
_AcTrunkslCount_Object = MibScalar
acTrunkslCount = _AcTrunkslCount_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 2, 14),
    _AcTrunkslCount_Type()
)
acTrunkslCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acTrunkslCount.setStatus("obsolete")


class _AcDspVersionTemplate_Type(Integer32):
    """Custom type acDspVersionTemplate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcDspVersionTemplate_Type.__name__ = "Integer32"
_AcDspVersionTemplate_Object = MibScalar
acDspVersionTemplate = _AcDspVersionTemplate_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 2, 15),
    _AcDspVersionTemplate_Type()
)
acDspVersionTemplate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDspVersionTemplate.setStatus("obsolete")


class _AcFirstPortDuplexMode_Type(Integer32):
    """Custom type acFirstPortDuplexMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("forceModeValue", 2),
          ("fullDuplex", 1),
          ("halfDuplex", 0),
          ("notAvailable", 3))
    )


_AcFirstPortDuplexMode_Type.__name__ = "Integer32"
_AcFirstPortDuplexMode_Object = MibScalar
acFirstPortDuplexMode = _AcFirstPortDuplexMode_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 2, 16),
    _AcFirstPortDuplexMode_Type()
)
acFirstPortDuplexMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acFirstPortDuplexMode.setStatus("obsolete")


class _AcFirstPortSpeed_Type(Integer32):
    """Custom type acFirstPortSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              10,
              100)
        )
    )
    namedValues = NamedValues(
        *(("ac100Mbps", 100),
          ("ac10Mbps", 10),
          ("forceModeValue", 2),
          ("notAvailable", 3))
    )


_AcFirstPortSpeed_Type.__name__ = "Integer32"
_AcFirstPortSpeed_Object = MibScalar
acFirstPortSpeed = _AcFirstPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 2, 17),
    _AcFirstPortSpeed_Type()
)
acFirstPortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acFirstPortSpeed.setStatus("obsolete")


class _AcMeanFreeChannels_Type(Integer32):
    """Custom type acMeanFreeChannels based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcMeanFreeChannels_Type.__name__ = "Integer32"
_AcMeanFreeChannels_Object = MibScalar
acMeanFreeChannels = _AcMeanFreeChannels_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 2, 18),
    _AcMeanFreeChannels_Type()
)
acMeanFreeChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acMeanFreeChannels.setStatus("obsolete")


class _AcMaxFreeChannels_Type(Integer32):
    """Custom type acMaxFreeChannels based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcMaxFreeChannels_Type.__name__ = "Integer32"
_AcMaxFreeChannels_Object = MibScalar
acMaxFreeChannels = _AcMaxFreeChannels_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 2, 19),
    _AcMaxFreeChannels_Type()
)
acMaxFreeChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acMaxFreeChannels.setStatus("obsolete")


class _AcSysUpTime_Type(Integer32):
    """Custom type acSysUpTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcSysUpTime_Type.__name__ = "Integer32"
_AcSysUpTime_Object = MibScalar
acSysUpTime = _AcSysUpTime_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 2, 20),
    _AcSysUpTime_Type()
)
acSysUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysUpTime.setStatus("obsolete")


class _AcPhysicalModCount_Type(Integer32):
    """Custom type acPhysicalModCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("first", 2),
          ("second", 1),
          ("soloist", 0))
    )


_AcPhysicalModCount_Type.__name__ = "Integer32"
_AcPhysicalModCount_Object = MibScalar
acPhysicalModCount = _AcPhysicalModCount_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 2, 21),
    _AcPhysicalModCount_Type()
)
acPhysicalModCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPhysicalModCount.setStatus("obsolete")


class _AcBoardTemperature_Type(Integer32):
    """Custom type acBoardTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AcBoardTemperature_Type.__name__ = "Integer32"
_AcBoardTemperature_Object = MibScalar
acBoardTemperature = _AcBoardTemperature_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 2, 22),
    _AcBoardTemperature_Type()
)
acBoardTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acBoardTemperature.setStatus("obsolete")
_ChannelConfiguration_ObjectIdentity = ObjectIdentity
channelConfiguration = _ChannelConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 3)
)
_VoiceSettings_ObjectIdentity = ObjectIdentity
voiceSettings = _VoiceSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 3, 2)
)
_VoiceSettingsTable_Object = MibTable
voiceSettingsTable = _VoiceSettingsTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    voiceSettingsTable.setStatus("obsolete")
_VoiceSettingsEntry_Object = MibTableRow
voiceSettingsEntry = _VoiceSettingsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 3, 2, 1, 1)
)
voiceSettingsEntry.setIndexNames(
    (0, "AcBoard", "cID"),
)
if mibBuilder.loadTexts:
    voiceSettingsEntry.setStatus("obsolete")


class _CID_Type(Integer32):
    """Custom type cID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CID_Type.__name__ = "Integer32"
_CID_Object = MibTableColumn
cID = _CID_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 3, 2, 1, 1, 1),
    _CID_Type()
)
cID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cID.setStatus("deprecated")


class _Coder_Type(Integer32):
    """Custom type coder based on Integer32"""
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
              19,
              20,
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
              34,
              35,
              36,
              37,
              40,
              41,
              42,
              45,
              46,
              47,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              78)
        )
    )
    namedValues = NamedValues(
        *(("aMR-10-2", 56),
          ("aMR-12-2", 57),
          ("aMR-4-75", 50),
          ("aMR-5-15", 51),
          ("aMR-5-9", 52),
          ("aMR-6-7", 53),
          ("aMR-7-4", 54),
          ("aMR-7-95", 55),
          ("acAMRWB-12-65", 68),
          ("acAMRWB-14-25", 69),
          ("acAMRWB-15-85", 70),
          ("acAMRWB-18-25", 71),
          ("acAMRWB-19-85", 72),
          ("acAMRWB-23-05", 73),
          ("acAMRWB-23-85", 74),
          ("acAMRWB-6-6", 66),
          ("acAMRWB-8-85", 67),
          ("acDPNSSCoder", 78),
          ("acG722-48K", 75),
          ("acG722-56K", 76),
          ("acG722-64K", 77),
          ("bV-16", 65),
          ("eVRC", 32),
          ("eVRC-TFO", 33),
          ("g711Alaw", 0),
          ("g711Alaw-5-5", 45),
          ("g711Mulaw", 1),
          ("g711Mulaw-5-5", 46),
          ("g723High", 16),
          ("g723Low", 15),
          ("g726-16", 2),
          ("g726-24", 3),
          ("g726-32", 4),
          ("g726-32-5-5", 47),
          ("g726-40", 5),
          ("g727-16", 6),
          ("g727-24", 8),
          ("g727-24-16", 7),
          ("g727-32", 11),
          ("g727-32-16", 9),
          ("g727-32-24", 10),
          ("g727-40-16", 12),
          ("g727-40-24", 13),
          ("g727-40-32", 14),
          ("g728", 23),
          ("g729", 17),
          ("gSM", 19),
          ("gSM610MS", 20),
          ("hDLCCoder", 24),
          ("iLBC-13", 64),
          ("iLBC-15", 63),
          ("modemAnswer", 41),
          ("modemCall", 42),
          ("netCoder-4-8", 25),
          ("netCoder-5-6", 26),
          ("netCoder-6-4", 27),
          ("netCoder-7-2", 28),
          ("netCoder-8", 29),
          ("netCoder-8-8", 30),
          ("netCoder-9-6", 31),
          ("noCoder", 40),
          ("qCELP-13", 36),
          ("qCELP-13-TFO", 37),
          ("qCELP-8", 34),
          ("qCELP-8-TFO", 35),
          ("transparent", 22))
    )


_Coder_Type.__name__ = "Integer32"
_Coder_Object = MibTableColumn
coder = _Coder_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 3, 2, 1, 1, 2),
    _Coder_Type()
)
coder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coder.setStatus("deprecated")


class _ECE_Type(Integer32):
    """Custom type eCE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_ECE_Type.__name__ = "Integer32"
_ECE_Object = MibTableColumn
eCE = _ECE_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 3, 2, 1, 1, 3),
    _ECE_Type()
)
eCE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eCE.setStatus("deprecated")


class _SCE_Type(Integer32):
    """Custom type sCE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SCE_Type.__name__ = "Integer32"
_SCE_Object = MibTableColumn
sCE = _SCE_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 3, 2, 1, 1, 4),
    _SCE_Type()
)
sCE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sCE.setStatus("deprecated")


class _PFE_Type(Integer32):
    """Custom type pFE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_PFE_Type.__name__ = "Integer32"
_PFE_Object = MibTableColumn
pFE = _PFE_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 3, 2, 1, 1, 5),
    _PFE_Type()
)
pFE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pFE.setStatus("deprecated")


class _HPFE_Type(Integer32):
    """Custom type hPFE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_HPFE_Type.__name__ = "Integer32"
_HPFE_Object = MibTableColumn
hPFE = _HPFE_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 3, 2, 1, 1, 6),
    _HPFE_Type()
)
hPFE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hPFE.setStatus("deprecated")


class _TestMode_Type(Integer32):
    """Custom type testMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("coderLoopback", 0),
          ("noLoopback", 3),
          ("pCMLoopback", 1),
          ("toneInjection", 2))
    )


_TestMode_Type.__name__ = "Integer32"
_TestMode_Object = MibTableColumn
testMode = _TestMode_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 3, 2, 1, 1, 7),
    _TestMode_Type()
)
testMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    testMode.setStatus("deprecated")


class _VoiceVolume_Type(Integer32):
    """Custom type voiceVolume based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_VoiceVolume_Type.__name__ = "Integer32"
_VoiceVolume_Object = MibTableColumn
voiceVolume = _VoiceVolume_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 3, 2, 1, 1, 8),
    _VoiceVolume_Type()
)
voiceVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceVolume.setStatus("deprecated")


class _InputGain_Type(Integer32):
    """Custom type inputGain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_InputGain_Type.__name__ = "Integer32"
_InputGain_Object = MibTableColumn
inputGain = _InputGain_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 3, 2, 1, 1, 9),
    _InputGain_Type()
)
inputGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputGain.setStatus("deprecated")


class _M_Type(Integer32):
    """Custom type m based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_M_Type.__name__ = "Integer32"
_M_Object = MibTableColumn
m = _M_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 3, 2, 1, 1, 10),
    _M_Type()
)
m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m.setStatus("deprecated")


class _RTPRedundancyDepth_Type(Integer32):
    """Custom type rTPRedundancyDepth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_RTPRedundancyDepth_Type.__name__ = "Integer32"
_RTPRedundancyDepth_Object = MibTableColumn
rTPRedundancyDepth = _RTPRedundancyDepth_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 3, 2, 1, 1, 11),
    _RTPRedundancyDepth_Type()
)
rTPRedundancyDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rTPRedundancyDepth.setStatus("deprecated")


class _ECLength_Type(Integer32):
    """Custom type eCLength based on Integer32"""
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
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("eCLength10MSec", 0),
          ("eCLength15Msec", 1),
          ("eCLength20Msec", 2),
          ("eCLength25Msec", 3),
          ("eCLength30Msec", 4),
          ("eCLength35Msec", 5),
          ("eCLength40Msec", 6),
          ("eCLength45Msec", 7),
          ("eCLength50Msec", 8),
          ("eCLength55Msec", 9),
          ("eCLength60Msec", 10))
    )


_ECLength_Type.__name__ = "Integer32"
_ECLength_Object = MibTableColumn
eCLength = _ECLength_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 3, 2, 1, 1, 12),
    _ECLength_Type()
)
eCLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eCLength.setStatus("deprecated")


class _ECHybridLoss_Type(Integer32):
    """Custom type eCHybridLoss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("loss0DB", 2),
          ("loss3DB", 3),
          ("loss6DB", 0),
          ("loss9DB", 1))
    )


_ECHybridLoss_Type.__name__ = "Integer32"
_ECHybridLoss_Object = MibTableColumn
eCHybridLoss = _ECHybridLoss_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 3, 2, 1, 1, 13),
    _ECHybridLoss_Type()
)
eCHybridLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eCHybridLoss.setStatus("deprecated")
_FaxModemSettings_ObjectIdentity = ObjectIdentity
faxModemSettings = _FaxModemSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 3, 3)
)
_FaxModemSettingsTable_Object = MibTable
faxModemSettingsTable = _FaxModemSettingsTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 3, 3, 1)
)
if mibBuilder.loadTexts:
    faxModemSettingsTable.setStatus("obsolete")
_FaxModemSettingsEntry_Object = MibTableRow
faxModemSettingsEntry = _FaxModemSettingsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 3, 3, 1, 1)
)
faxModemSettingsEntry.setIndexNames(
    (0, "AcBoard", "cID"),
)
if mibBuilder.loadTexts:
    faxModemSettingsEntry.setStatus("obsolete")


class _FAXTransportType_Type(Integer32):
    """Custom type fAXTransportType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bypass", 2),
          ("relay", 1),
          ("transparent", 0))
    )


_FAXTransportType_Type.__name__ = "Integer32"
_FAXTransportType_Object = MibTableColumn
fAXTransportType = _FAXTransportType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 3, 3, 1, 1, 1),
    _FAXTransportType_Type()
)
fAXTransportType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fAXTransportType.setStatus("obsolete")


class _AcCallerIDType_Type(Integer32):
    """Custom type acCallerIDType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bypass", 2),
          ("relay", 1),
          ("transparent", 0))
    )


_AcCallerIDType_Type.__name__ = "Integer32"
_AcCallerIDType_Object = MibTableColumn
acCallerIDType = _AcCallerIDType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 3, 3, 1, 1, 2),
    _AcCallerIDType_Type()
)
acCallerIDType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acCallerIDType.setStatus("obsolete")


class _V21ModemTransportType_Type(Integer32):
    """Custom type v21ModemTransportType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bypass", 2),
          ("relay", 1),
          ("transparent", 0))
    )


_V21ModemTransportType_Type.__name__ = "Integer32"
_V21ModemTransportType_Object = MibTableColumn
v21ModemTransportType = _V21ModemTransportType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 3, 3, 1, 1, 3),
    _V21ModemTransportType_Type()
)
v21ModemTransportType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v21ModemTransportType.setStatus("obsolete")


class _V22ModemTransportType_Type(Integer32):
    """Custom type v22ModemTransportType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bypass", 2),
          ("relay", 1),
          ("transparent", 0))
    )


_V22ModemTransportType_Type.__name__ = "Integer32"
_V22ModemTransportType_Object = MibTableColumn
v22ModemTransportType = _V22ModemTransportType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 3, 3, 1, 1, 4),
    _V22ModemTransportType_Type()
)
v22ModemTransportType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v22ModemTransportType.setStatus("obsolete")


class _V23ModemTransportType_Type(Integer32):
    """Custom type v23ModemTransportType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bypass", 2),
          ("relay", 1),
          ("transparent", 0))
    )


_V23ModemTransportType_Type.__name__ = "Integer32"
_V23ModemTransportType_Object = MibTableColumn
v23ModemTransportType = _V23ModemTransportType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 3, 3, 1, 1, 5),
    _V23ModemTransportType_Type()
)
v23ModemTransportType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v23ModemTransportType.setStatus("obsolete")


class _V32ModemTransportType_Type(Integer32):
    """Custom type v32ModemTransportType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bypass", 2),
          ("relay", 1),
          ("transparent", 0))
    )


_V32ModemTransportType_Type.__name__ = "Integer32"
_V32ModemTransportType_Object = MibTableColumn
v32ModemTransportType = _V32ModemTransportType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 3, 3, 1, 1, 6),
    _V32ModemTransportType_Type()
)
v32ModemTransportType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v32ModemTransportType.setStatus("obsolete")


class _V34ModemTransportType_Type(Integer32):
    """Custom type v34ModemTransportType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bypass", 2),
          ("relay", 1),
          ("transparent", 0))
    )


_V34ModemTransportType_Type.__name__ = "Integer32"
_V34ModemTransportType_Object = MibTableColumn
v34ModemTransportType = _V34ModemTransportType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 3, 3, 1, 1, 7),
    _V34ModemTransportType_Type()
)
v34ModemTransportType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v34ModemTransportType.setStatus("obsolete")


class _FaxRelayMaxRate_Type(Integer32):
    """Custom type faxRelayMaxRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ac12000", 4),
          ("ac14400", 5),
          ("ac2400", 0),
          ("ac4800", 1),
          ("ac7200", 2),
          ("ac9600", 3))
    )


_FaxRelayMaxRate_Type.__name__ = "Integer32"
_FaxRelayMaxRate_Object = MibTableColumn
faxRelayMaxRate = _FaxRelayMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 3, 3, 1, 1, 8),
    _FaxRelayMaxRate_Type()
)
faxRelayMaxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faxRelayMaxRate.setStatus("obsolete")


class _ModemRelayMaxRate_Type(Integer32):
    """Custom type modemRelayMaxRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ac12000", 4),
          ("ac14400", 5),
          ("ac2400", 0),
          ("ac4800", 1),
          ("ac7200", 2),
          ("ac9600", 3))
    )


_ModemRelayMaxRate_Type.__name__ = "Integer32"
_ModemRelayMaxRate_Object = MibTableColumn
modemRelayMaxRate = _ModemRelayMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 3, 3, 1, 1, 9),
    _ModemRelayMaxRate_Type()
)
modemRelayMaxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemRelayMaxRate.setStatus("obsolete")


class _FaxRelayECMEnable_Type(Integer32):
    """Custom type faxRelayECMEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_FaxRelayECMEnable_Type.__name__ = "Integer32"
_FaxRelayECMEnable_Object = MibTableColumn
faxRelayECMEnable = _FaxRelayECMEnable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 3, 3, 1, 1, 10),
    _FaxRelayECMEnable_Type()
)
faxRelayECMEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faxRelayECMEnable.setStatus("obsolete")


class _T38FaxRelayProtectionMode_Type(Integer32):
    """Custom type t38FaxRelayProtectionMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("fEC", 1),
          ("redundancyPackets", 0))
    )


_T38FaxRelayProtectionMode_Type.__name__ = "Integer32"
_T38FaxRelayProtectionMode_Object = MibTableColumn
t38FaxRelayProtectionMode = _T38FaxRelayProtectionMode_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 3, 3, 1, 1, 11),
    _T38FaxRelayProtectionMode_Type()
)
t38FaxRelayProtectionMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t38FaxRelayProtectionMode.setStatus("obsolete")


class _FaxRelayRedundancyDepth_Type(Integer32):
    """Custom type faxRelayRedundancyDepth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_FaxRelayRedundancyDepth_Type.__name__ = "Integer32"
_FaxRelayRedundancyDepth_Object = MibTableColumn
faxRelayRedundancyDepth = _FaxRelayRedundancyDepth_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 3, 3, 1, 1, 12),
    _FaxRelayRedundancyDepth_Type()
)
faxRelayRedundancyDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faxRelayRedundancyDepth.setStatus("obsolete")


class _EnhancedFaxRelayRedundancyDepth_Type(Integer32):
    """Custom type enhancedFaxRelayRedundancyDepth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_EnhancedFaxRelayRedundancyDepth_Type.__name__ = "Integer32"
_EnhancedFaxRelayRedundancyDepth_Object = MibTableColumn
enhancedFaxRelayRedundancyDepth = _EnhancedFaxRelayRedundancyDepth_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 3, 3, 1, 1, 13),
    _EnhancedFaxRelayRedundancyDepth_Type()
)
enhancedFaxRelayRedundancyDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enhancedFaxRelayRedundancyDepth.setStatus("obsolete")


class _ModemRelayRedundancyDepth_Type(Integer32):
    """Custom type modemRelayRedundancyDepth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_ModemRelayRedundancyDepth_Type.__name__ = "Integer32"
_ModemRelayRedundancyDepth_Object = MibTableColumn
modemRelayRedundancyDepth = _ModemRelayRedundancyDepth_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 3, 3, 1, 1, 14),
    _ModemRelayRedundancyDepth_Type()
)
modemRelayRedundancyDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemRelayRedundancyDepth.setStatus("obsolete")


class _FaxModemRelayVolume_Type(Integer32):
    """Custom type faxModemRelayVolume based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-18, 15),
    )


_FaxModemRelayVolume_Type.__name__ = "Integer32"
_FaxModemRelayVolume_Object = MibTableColumn
faxModemRelayVolume = _FaxModemRelayVolume_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 3, 3, 1, 1, 15),
    _FaxModemRelayVolume_Type()
)
faxModemRelayVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faxModemRelayVolume.setStatus("obsolete")


class _FaxModemBypassCoderType_Type(Integer32):
    """Custom type faxModemBypassCoderType based on Integer32"""
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
              19,
              20,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31)
        )
    )
    namedValues = NamedValues(
        *(("g711Alaw", 0),
          ("g711Mulaw", 1),
          ("g723High", 16),
          ("g723Low", 15),
          ("g726-16", 2),
          ("g726-24", 3),
          ("g726-32", 4),
          ("g726-40", 5),
          ("g727-16", 6),
          ("g727-24", 8),
          ("g727-24-16", 7),
          ("g727-32", 11),
          ("g727-32-16", 9),
          ("g727-32-24", 10),
          ("g727-40-16", 12),
          ("g727-40-24", 13),
          ("g727-40-32", 14),
          ("g728", 23),
          ("g729", 17),
          ("gSM", 19),
          ("gSM610MS", 20),
          ("hDLCCoder", 24),
          ("netCoder-4-8", 25),
          ("netCoder-5-6", 26),
          ("netCoder-6-4", 27),
          ("netCoder-7-2", 28),
          ("netCoder-8", 29),
          ("netCoder-8-8", 30),
          ("netCoder-9-6", 31),
          ("transparent", 22))
    )


_FaxModemBypassCoderType_Type.__name__ = "Integer32"
_FaxModemBypassCoderType_Object = MibTableColumn
faxModemBypassCoderType = _FaxModemBypassCoderType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 3, 3, 1, 1, 16),
    _FaxModemBypassCoderType_Type()
)
faxModemBypassCoderType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faxModemBypassCoderType.setStatus("obsolete")


class _FaxModemBypassM_Type(Integer32):
    """Custom type faxModemBypassM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FaxModemBypassM_Type.__name__ = "Integer32"
_FaxModemBypassM_Object = MibTableColumn
faxModemBypassM = _FaxModemBypassM_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 3, 3, 1, 1, 17),
    _FaxModemBypassM_Type()
)
faxModemBypassM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faxModemBypassM.setStatus("obsolete")


class _UseT38orFRF11_Type(Integer32):
    """Custom type useT38orFRF11 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("fRF11", 0),
          ("t38", 1))
    )


_UseT38orFRF11_Type.__name__ = "Integer32"
_UseT38orFRF11_Object = MibTableColumn
useT38orFRF11 = _UseT38orFRF11_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 3, 3, 1, 1, 18),
    _UseT38orFRF11_Type()
)
useT38orFRF11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    useT38orFRF11.setStatus("obsolete")
_DJBSettings_ObjectIdentity = ObjectIdentity
dJBSettings = _DJBSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 3, 4)
)
_DJBSettingsTable_Object = MibTable
dJBSettingsTable = _DJBSettingsTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 3, 4, 1)
)
if mibBuilder.loadTexts:
    dJBSettingsTable.setStatus("obsolete")
_DJBSettingsEntry_Object = MibTableRow
dJBSettingsEntry = _DJBSettingsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 3, 4, 1, 1)
)
dJBSettingsEntry.setIndexNames(
    (0, "AcBoard", "cID"),
)
if mibBuilder.loadTexts:
    dJBSettingsEntry.setStatus("obsolete")


class _DJBufMinDelay_Type(Integer32):
    """Custom type dJBufMinDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 150),
    )


_DJBufMinDelay_Type.__name__ = "Integer32"
_DJBufMinDelay_Object = MibTableColumn
dJBufMinDelay = _DJBufMinDelay_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 3, 4, 1, 1, 1),
    _DJBufMinDelay_Type()
)
dJBufMinDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dJBufMinDelay.setStatus("obsolete")


class _DJBufOptFactor_Type(Integer32):
    """Custom type dJBufOptFactor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_DJBufOptFactor_Type.__name__ = "Integer32"
_DJBufOptFactor_Object = MibTableColumn
dJBufOptFactor = _DJBufOptFactor_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 3, 4, 1, 1, 2),
    _DJBufOptFactor_Type()
)
dJBufOptFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dJBufOptFactor.setStatus("obsolete")
_ChannelTDMBusSettings_ObjectIdentity = ObjectIdentity
channelTDMBusSettings = _ChannelTDMBusSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 3, 5)
)
_ChannelTDMBusSettingsTable_Object = MibTable
channelTDMBusSettingsTable = _ChannelTDMBusSettingsTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 3, 5, 1)
)
if mibBuilder.loadTexts:
    channelTDMBusSettingsTable.setStatus("obsolete")
_ChannelTDMBusSettingsEntry_Object = MibTableRow
channelTDMBusSettingsEntry = _ChannelTDMBusSettingsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 3, 5, 1, 1)
)
channelTDMBusSettingsEntry.setIndexNames(
    (0, "AcBoard", "cID"),
)
if mibBuilder.loadTexts:
    channelTDMBusSettingsEntry.setStatus("obsolete")


class _TDMBusInputPort_Type(Integer32):
    """Custom type tDMBusInputPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_TDMBusInputPort_Type.__name__ = "Integer32"
_TDMBusInputPort_Object = MibTableColumn
tDMBusInputPort = _TDMBusInputPort_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 3, 5, 1, 1, 1),
    _TDMBusInputPort_Type()
)
tDMBusInputPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tDMBusInputPort.setStatus("obsolete")


class _TDMBusInputChannel_Type(Integer32):
    """Custom type tDMBusInputChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_TDMBusInputChannel_Type.__name__ = "Integer32"
_TDMBusInputChannel_Object = MibTableColumn
tDMBusInputChannel = _TDMBusInputChannel_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 3, 5, 1, 1, 2),
    _TDMBusInputChannel_Type()
)
tDMBusInputChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tDMBusInputChannel.setStatus("obsolete")


class _TDMBusOutputDisable_Type(Integer32):
    """Custom type tDMBusOutputDisable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_TDMBusOutputDisable_Type.__name__ = "Integer32"
_TDMBusOutputDisable_Object = MibTableColumn
tDMBusOutputDisable = _TDMBusOutputDisable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 3, 5, 1, 1, 3),
    _TDMBusOutputDisable_Type()
)
tDMBusOutputDisable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tDMBusOutputDisable.setStatus("obsolete")


class _TDMBusOutputPort_Type(Integer32):
    """Custom type tDMBusOutputPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TDMBusOutputPort_Type.__name__ = "Integer32"
_TDMBusOutputPort_Object = MibTableColumn
tDMBusOutputPort = _TDMBusOutputPort_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 3, 5, 1, 1, 4),
    _TDMBusOutputPort_Type()
)
tDMBusOutputPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tDMBusOutputPort.setStatus("obsolete")


class _TDMBusOutputChannel_Type(Integer32):
    """Custom type tDMBusOutputChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_TDMBusOutputChannel_Type.__name__ = "Integer32"
_TDMBusOutputChannel_Object = MibTableColumn
tDMBusOutputChannel = _TDMBusOutputChannel_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 3, 5, 1, 1, 5),
    _TDMBusOutputChannel_Type()
)
tDMBusOutputChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tDMBusOutputChannel.setStatus("obsolete")
_TransportSettings_ObjectIdentity = ObjectIdentity
transportSettings = _TransportSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 3, 6)
)
_TransportSettingsTable_Object = MibTable
transportSettingsTable = _TransportSettingsTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 3, 6, 1)
)
if mibBuilder.loadTexts:
    transportSettingsTable.setStatus("obsolete")
_TransportSettingsEntry_Object = MibTableRow
transportSettingsEntry = _TransportSettingsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 3, 6, 1, 1)
)
transportSettingsEntry.setIndexNames(
    (0, "AcBoard", "cID"),
)
if mibBuilder.loadTexts:
    transportSettingsEntry.setStatus("obsolete")


class _UseNIorPCI_Type(Integer32):
    """Custom type useNIorPCI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_UseNIorPCI_Type.__name__ = "Integer32"
_UseNIorPCI_Object = MibTableColumn
useNIorPCI = _UseNIorPCI_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 3, 6, 1, 1, 1),
    _UseNIorPCI_Type()
)
useNIorPCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    useNIorPCI.setStatus("obsolete")


class _DisableSoftIPLoopback_Type(Integer32):
    """Custom type disableSoftIPLoopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_DisableSoftIPLoopback_Type.__name__ = "Integer32"
_DisableSoftIPLoopback_Object = MibTableColumn
disableSoftIPLoopback = _DisableSoftIPLoopback_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 3, 6, 1, 1, 2),
    _DisableSoftIPLoopback_Type()
)
disableSoftIPLoopback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    disableSoftIPLoopback.setStatus("obsolete")


class _UniDirectionalRTP_Type(Integer32):
    """Custom type uniDirectionalRTP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UniDirectionalRTP_Type.__name__ = "Integer32"
_UniDirectionalRTP_Object = MibTableColumn
uniDirectionalRTP = _UniDirectionalRTP_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 3, 6, 1, 1, 3),
    _UniDirectionalRTP_Type()
)
uniDirectionalRTP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uniDirectionalRTP.setStatus("obsolete")
_RTPRTCPSettings_ObjectIdentity = ObjectIdentity
rTPRTCPSettings = _RTPRTCPSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 3, 7)
)
_RTPRTCPSettingsTable_Object = MibTable
rTPRTCPSettingsTable = _RTPRTCPSettingsTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 3, 7, 1)
)
if mibBuilder.loadTexts:
    rTPRTCPSettingsTable.setStatus("obsolete")
_RTPRTCPSettingsEntry_Object = MibTableRow
rTPRTCPSettingsEntry = _RTPRTCPSettingsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 3, 7, 1, 1)
)
rTPRTCPSettingsEntry.setIndexNames(
    (0, "AcBoard", "cID"),
)
if mibBuilder.loadTexts:
    rTPRTCPSettingsEntry.setStatus("obsolete")


class _CNAME_Type(OctetString):
    """Custom type cNAME based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CNAME_Type.__name__ = "OctetString"
_CNAME_Object = MibTableColumn
cNAME = _CNAME_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 3, 7, 1, 1, 1),
    _CNAME_Type()
)
cNAME.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cNAME.setStatus("obsolete")


class _IPPrecedence_Type(Integer32):
    """Custom type iPPrecedence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_IPPrecedence_Type.__name__ = "Integer32"
_IPPrecedence_Object = MibTableColumn
iPPrecedence = _IPPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 3, 7, 1, 1, 2),
    _IPPrecedence_Type()
)
iPPrecedence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iPPrecedence.setStatus("obsolete")


class _IPTOS_Type(Integer32):
    """Custom type iPTOS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_IPTOS_Type.__name__ = "Integer32"
_IPTOS_Object = MibTableColumn
iPTOS = _IPTOS_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 3, 7, 1, 1, 3),
    _IPTOS_Type()
)
iPTOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iPTOS.setStatus("obsolete")


class _LocalRTPPort_Type(Integer32):
    """Custom type localRTPPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LocalRTPPort_Type.__name__ = "Integer32"
_LocalRTPPort_Object = MibTableColumn
localRTPPort = _LocalRTPPort_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 3, 7, 1, 1, 4),
    _LocalRTPPort_Type()
)
localRTPPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localRTPPort.setStatus("obsolete")
_RemoteRTPAddr_Type = IpAddress
_RemoteRTPAddr_Object = MibTableColumn
remoteRTPAddr = _RemoteRTPAddr_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 3, 7, 1, 1, 5),
    _RemoteRTPAddr_Type()
)
remoteRTPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteRTPAddr.setStatus("obsolete")


class _RemoteRTPPort_Type(Integer32):
    """Custom type remoteRTPPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RemoteRTPPort_Type.__name__ = "Integer32"
_RemoteRTPPort_Object = MibTableColumn
remoteRTPPort = _RemoteRTPPort_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 3, 7, 1, 1, 6),
    _RemoteRTPPort_Type()
)
remoteRTPPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteRTPPort.setStatus("obsolete")
_RemoteT38Addr_Type = IpAddress
_RemoteT38Addr_Object = MibTableColumn
remoteT38Addr = _RemoteT38Addr_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 3, 7, 1, 1, 7),
    _RemoteT38Addr_Type()
)
remoteT38Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteT38Addr.setStatus("obsolete")


class _RemoteT38Port_Type(Integer32):
    """Custom type remoteT38Port based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RemoteT38Port_Type.__name__ = "Integer32"
_RemoteT38Port_Object = MibTableColumn
remoteT38Port = _RemoteT38Port_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 3, 7, 1, 1, 8),
    _RemoteT38Port_Type()
)
remoteT38Port.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteT38Port.setStatus("obsolete")


class _RTCPMeanTxInterval_Type(Integer32):
    """Custom type rTCPMeanTxInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 2147483647),
    )


_RTCPMeanTxInterval_Type.__name__ = "Integer32"
_RTCPMeanTxInterval_Object = MibTableColumn
rTCPMeanTxInterval = _RTCPMeanTxInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 3, 7, 1, 1, 9),
    _RTCPMeanTxInterval_Type()
)
rTCPMeanTxInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rTCPMeanTxInterval.setStatus("obsolete")


class _RxRTPPayloadType_Type(Integer32):
    """Custom type rxRTPPayloadType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, 127),
    )


_RxRTPPayloadType_Type.__name__ = "Integer32"
_RxRTPPayloadType_Object = MibTableColumn
rxRTPPayloadType = _RxRTPPayloadType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 3, 7, 1, 1, 10),
    _RxRTPPayloadType_Type()
)
rxRTPPayloadType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxRTPPayloadType.setStatus("obsolete")


class _TxRTPPayloadType_Type(Integer32):
    """Custom type txRTPPayloadType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, 127),
    )


_TxRTPPayloadType_Type.__name__ = "Integer32"
_TxRTPPayloadType_Object = MibTableColumn
txRTPPayloadType = _TxRTPPayloadType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 3, 7, 1, 1, 11),
    _TxRTPPayloadType_Type()
)
txRTPPayloadType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txRTPPayloadType.setStatus("obsolete")
_ChannelStatus_ObjectIdentity = ObjectIdentity
channelStatus = _ChannelStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 4)
)
_ChannelStatusTable_Object = MibTable
channelStatusTable = _ChannelStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 4, 1)
)
if mibBuilder.loadTexts:
    channelStatusTable.setStatus("obsolete")
_ChannelStatusEntry_Object = MibTableRow
channelStatusEntry = _ChannelStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 4, 1, 1)
)
channelStatusEntry.setIndexNames(
    (0, "AcBoard", "cID"),
)
if mibBuilder.loadTexts:
    channelStatusEntry.setStatus("obsolete")


class _RTPActive_Type(Integer32):
    """Custom type rTPActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("notActive", 0))
    )


_RTPActive_Type.__name__ = "Integer32"
_RTPActive_Object = MibTableColumn
rTPActive = _RTPActive_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 4, 1, 1, 1),
    _RTPActive_Type()
)
rTPActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rTPActive.setStatus("deprecated")


class _BypassNIC_Type(Integer32):
    """Custom type bypassNIC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BypassNIC_Type.__name__ = "Integer32"
_BypassNIC_Object = MibTableColumn
bypassNIC = _BypassNIC_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 4, 1, 1, 2),
    _BypassNIC_Type()
)
bypassNIC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bypassNIC.setStatus("deprecated")


class _PendingIdle_Type(Integer32):
    """Custom type pendingIdle based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_PendingIdle_Type.__name__ = "Integer32"
_PendingIdle_Object = MibTableColumn
pendingIdle = _PendingIdle_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 4, 1, 1, 3),
    _PendingIdle_Type()
)
pendingIdle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pendingIdle.setStatus("obsolete")


class _TxSilencePeriod_Type(Integer32):
    """Custom type txSilencePeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_TxSilencePeriod_Type.__name__ = "Integer32"
_TxSilencePeriod_Object = MibTableColumn
txSilencePeriod = _TxSilencePeriod_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 4, 1, 1, 4),
    _TxSilencePeriod_Type()
)
txSilencePeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txSilencePeriod.setStatus("deprecated")


class _RxSilencePeriod_Type(Integer32):
    """Custom type rxSilencePeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_RxSilencePeriod_Type.__name__ = "Integer32"
_RxSilencePeriod_Object = MibTableColumn
rxSilencePeriod = _RxSilencePeriod_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 4, 1, 1, 5),
    _RxSilencePeriod_Type()
)
rxSilencePeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxSilencePeriod.setStatus("deprecated")


class _TxFaxMode_Type(Integer32):
    """Custom type txFaxMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_TxFaxMode_Type.__name__ = "Integer32"
_TxFaxMode_Object = MibTableColumn
txFaxMode = _TxFaxMode_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 4, 1, 1, 6),
    _TxFaxMode_Type()
)
txFaxMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txFaxMode.setStatus("deprecated")


class _RxFaxMode_Type(Integer32):
    """Custom type rxFaxMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_RxFaxMode_Type.__name__ = "Integer32"
_RxFaxMode_Object = MibTableColumn
rxFaxMode = _RxFaxMode_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 4, 1, 1, 7),
    _RxFaxMode_Type()
)
rxFaxMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxFaxMode.setStatus("deprecated")


class _TxDTMFPeriod_Type(Integer32):
    """Custom type txDTMFPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_TxDTMFPeriod_Type.__name__ = "Integer32"
_TxDTMFPeriod_Object = MibTableColumn
txDTMFPeriod = _TxDTMFPeriod_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 4, 1, 1, 8),
    _TxDTMFPeriod_Type()
)
txDTMFPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txDTMFPeriod.setStatus("deprecated")


class _RxDTMFPeriod_Type(Integer32):
    """Custom type rxDTMFPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_RxDTMFPeriod_Type.__name__ = "Integer32"
_RxDTMFPeriod_Object = MibTableColumn
rxDTMFPeriod = _RxDTMFPeriod_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 4, 1, 1, 9),
    _RxDTMFPeriod_Type()
)
rxDTMFPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxDTMFPeriod.setStatus("deprecated")


class _PacketsToDSPCnt_Type(Integer32):
    """Custom type packetsToDSPCnt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PacketsToDSPCnt_Type.__name__ = "Integer32"
_PacketsToDSPCnt_Object = MibTableColumn
packetsToDSPCnt = _PacketsToDSPCnt_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 4, 1, 1, 10),
    _PacketsToDSPCnt_Type()
)
packetsToDSPCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    packetsToDSPCnt.setStatus("deprecated")


class _JitterBufErrorCnt_Type(Integer32):
    """Custom type jitterBufErrorCnt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JitterBufErrorCnt_Type.__name__ = "Integer32"
_JitterBufErrorCnt_Object = MibTableColumn
jitterBufErrorCnt = _JitterBufErrorCnt_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 4, 1, 1, 11),
    _JitterBufErrorCnt_Type()
)
jitterBufErrorCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jitterBufErrorCnt.setStatus("obsolete")


class _JitterBufForcedPacketLost_Type(Integer32):
    """Custom type jitterBufForcedPacketLost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JitterBufForcedPacketLost_Type.__name__ = "Integer32"
_JitterBufForcedPacketLost_Object = MibTableColumn
jitterBufForcedPacketLost = _JitterBufForcedPacketLost_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 4, 1, 1, 12),
    _JitterBufForcedPacketLost_Type()
)
jitterBufForcedPacketLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jitterBufForcedPacketLost.setStatus("obsolete")


class _JitterBufForcedPacketAddition_Type(Integer32):
    """Custom type jitterBufForcedPacketAddition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JitterBufForcedPacketAddition_Type.__name__ = "Integer32"
_JitterBufForcedPacketAddition_Object = MibTableColumn
jitterBufForcedPacketAddition = _JitterBufForcedPacketAddition_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 4, 1, 1, 13),
    _JitterBufForcedPacketAddition_Type()
)
jitterBufForcedPacketAddition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jitterBufForcedPacketAddition.setStatus("obsolete")


class _JitterBufUnderRunCnt_Type(Integer32):
    """Custom type jitterBufUnderRunCnt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JitterBufUnderRunCnt_Type.__name__ = "Integer32"
_JitterBufUnderRunCnt_Object = MibTableColumn
jitterBufUnderRunCnt = _JitterBufUnderRunCnt_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 4, 1, 1, 14),
    _JitterBufUnderRunCnt_Type()
)
jitterBufUnderRunCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jitterBufUnderRunCnt.setStatus("deprecated")


class _JitterBufOverRunCnt_Type(Integer32):
    """Custom type jitterBufOverRunCnt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JitterBufOverRunCnt_Type.__name__ = "Integer32"
_JitterBufOverRunCnt_Object = MibTableColumn
jitterBufOverRunCnt = _JitterBufOverRunCnt_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 4, 1, 1, 15),
    _JitterBufOverRunCnt_Type()
)
jitterBufOverRunCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jitterBufOverRunCnt.setStatus("deprecated")


class _JitterBufAccumDelay_Type(Integer32):
    """Custom type jitterBufAccumDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JitterBufAccumDelay_Type.__name__ = "Integer32"
_JitterBufAccumDelay_Object = MibTableColumn
jitterBufAccumDelay = _JitterBufAccumDelay_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 4, 1, 1, 16),
    _JitterBufAccumDelay_Type()
)
jitterBufAccumDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jitterBufAccumDelay.setStatus("obsolete")


class _FXSorFXO_Type(Integer32):
    """Custom type fXSorFXO based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("fXO", 0),
          ("fXS", 1),
          ("nonAnalogDevice", -1))
    )


_FXSorFXO_Type.__name__ = "Integer32"
_FXSorFXO_Object = MibTableColumn
fXSorFXO = _FXSorFXO_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 4, 1, 1, 17),
    _FXSorFXO_Type()
)
fXSorFXO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fXSorFXO.setStatus("deprecated")


class _ChannelHookState_Type(Integer32):
    """Custom type channelHookState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nonAnalogDevice", -1),
          ("offHook", 0),
          ("onHook", 1))
    )


_ChannelHookState_Type.__name__ = "Integer32"
_ChannelHookState_Object = MibTableColumn
channelHookState = _ChannelHookState_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 4, 1, 1, 18),
    _ChannelHookState_Type()
)
channelHookState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelHookState.setStatus("deprecated")
_Notifications_ObjectIdentity = ObjectIdentity
notifications = _Notifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 5)
)
_Reset_ObjectIdentity = ObjectIdentity
reset = _Reset_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 6)
)


class _RemoteReset_Type(Integer32):
    """Custom type remoteReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RemoteReset_Type.__name__ = "Integer32"
_RemoteReset_Object = MibScalar
remoteReset = _RemoteReset_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 6, 1),
    _RemoteReset_Type()
)
remoteReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteReset.setStatus("obsolete")


class _AcSetDefaults_Type(Integer32):
    """Custom type acSetDefaults based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AcSetDefaults_Type.__name__ = "Integer32"
_AcSetDefaults_Object = MibScalar
acSetDefaults = _AcSetDefaults_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 6, 2),
    _AcSetDefaults_Type()
)
acSetDefaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSetDefaults.setStatus("obsolete")


class _AcgwAdminState_Type(Integer32):
    """Custom type acgwAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locked", 0),
          ("shuttingDown", 1),
          ("unlocked", 2))
    )


_AcgwAdminState_Type.__name__ = "Integer32"
_AcgwAdminState_Object = MibScalar
acgwAdminState = _AcgwAdminState_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 6, 3),
    _AcgwAdminState_Type()
)
acgwAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acgwAdminState.setStatus("obsolete")


class _AcgwAdminStateLockControl_Type(Integer32):
    """Custom type acgwAdminStateLockControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_AcgwAdminStateLockControl_Type.__name__ = "Integer32"
_AcgwAdminStateLockControl_Object = MibScalar
acgwAdminStateLockControl = _AcgwAdminStateLockControl_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 6, 4),
    _AcgwAdminStateLockControl_Type()
)
acgwAdminStateLockControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acgwAdminStateLockControl.setStatus("obsolete")


class _AcSaveConfigToSystem_Type(Integer32):
    """Custom type acSaveConfigToSystem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcSaveConfigToSystem_Type.__name__ = "Integer32"
_AcSaveConfigToSystem_Object = MibScalar
acSaveConfigToSystem = _AcSaveConfigToSystem_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 6, 5),
    _AcSaveConfigToSystem_Type()
)
acSaveConfigToSystem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSaveConfigToSystem.setStatus("obsolete")


class _AcOperationalState_Type(Integer32):
    """Custom type acOperationalState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_AcOperationalState_Type.__name__ = "Integer32"
_AcOperationalState_Object = MibScalar
acOperationalState = _AcOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 6, 6),
    _AcOperationalState_Type()
)
acOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acOperationalState.setStatus("obsolete")


class _RemoteResetControl_Type(Integer32):
    """Custom type remoteResetControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("resetFromBootP", 3),
          ("resetFromFlashAfterBurn", 1),
          ("resetFromFlashNoBurn", 2))
    )


_RemoteResetControl_Type.__name__ = "Integer32"
_RemoteResetControl_Object = MibScalar
remoteResetControl = _RemoteResetControl_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 6, 7),
    _RemoteResetControl_Type()
)
remoteResetControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteResetControl.setStatus("obsolete")
_AcTrap_ObjectIdentity = ObjectIdentity
acTrap = _AcTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 21)
)
_AcBoardTrapGlobals_ObjectIdentity = ObjectIdentity
acBoardTrapGlobals = _AcBoardTrapGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 21, 1)
)


class _AcBoardTrapGlobalsName_Type(Integer32):
    """Custom type acBoardTrapGlobalsName based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_AcBoardTrapGlobalsName_Type.__name__ = "Integer32"
_AcBoardTrapGlobalsName_Object = MibScalar
acBoardTrapGlobalsName = _AcBoardTrapGlobalsName_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 21, 1, 1),
    _AcBoardTrapGlobalsName_Type()
)
acBoardTrapGlobalsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acBoardTrapGlobalsName.setStatus("deprecated")


class _AcBoardTrapGlobalsTextualDescription_Type(OctetString):
    """Custom type acBoardTrapGlobalsTextualDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 200),
    )


_AcBoardTrapGlobalsTextualDescription_Type.__name__ = "OctetString"
_AcBoardTrapGlobalsTextualDescription_Object = MibScalar
acBoardTrapGlobalsTextualDescription = _AcBoardTrapGlobalsTextualDescription_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 21, 1, 2),
    _AcBoardTrapGlobalsTextualDescription_Type()
)
acBoardTrapGlobalsTextualDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acBoardTrapGlobalsTextualDescription.setStatus("deprecated")


class _AcBoardTrapGlobalsSource_Type(OctetString):
    """Custom type acBoardTrapGlobalsSource based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_AcBoardTrapGlobalsSource_Type.__name__ = "OctetString"
_AcBoardTrapGlobalsSource_Object = MibScalar
acBoardTrapGlobalsSource = _AcBoardTrapGlobalsSource_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 21, 1, 3),
    _AcBoardTrapGlobalsSource_Type()
)
acBoardTrapGlobalsSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acBoardTrapGlobalsSource.setStatus("deprecated")


class _AcBoardTrapGlobalsSeverity_Type(Integer32):
    """Custom type acBoardTrapGlobalsSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("cleared", 0),
          ("critical", 5),
          ("indeterminate", 1),
          ("major", 4),
          ("minor", 3),
          ("warning", 2))
    )


_AcBoardTrapGlobalsSeverity_Type.__name__ = "Integer32"
_AcBoardTrapGlobalsSeverity_Object = MibScalar
acBoardTrapGlobalsSeverity = _AcBoardTrapGlobalsSeverity_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 21, 1, 4),
    _AcBoardTrapGlobalsSeverity_Type()
)
acBoardTrapGlobalsSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acBoardTrapGlobalsSeverity.setStatus("deprecated")


class _AcBoardTrapGlobalsUniqID_Type(Integer32):
    """Custom type acBoardTrapGlobalsUniqID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32000),
    )


_AcBoardTrapGlobalsUniqID_Type.__name__ = "Integer32"
_AcBoardTrapGlobalsUniqID_Object = MibScalar
acBoardTrapGlobalsUniqID = _AcBoardTrapGlobalsUniqID_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 21, 1, 5),
    _AcBoardTrapGlobalsUniqID_Type()
)
acBoardTrapGlobalsUniqID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acBoardTrapGlobalsUniqID.setStatus("deprecated")


class _AcBoardTrapGlobalsType_Type(Integer32):
    """Custom type acBoardTrapGlobalsType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("communicationsAlarm", 1),
          ("environmentalAlarm", 5),
          ("equipmentAlarm", 4),
          ("other", 0),
          ("processingErrorAlarm", 3),
          ("qualityOfServiceAlarm", 2))
    )


_AcBoardTrapGlobalsType_Type.__name__ = "Integer32"
_AcBoardTrapGlobalsType_Object = MibScalar
acBoardTrapGlobalsType = _AcBoardTrapGlobalsType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 21, 1, 6),
    _AcBoardTrapGlobalsType_Type()
)
acBoardTrapGlobalsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acBoardTrapGlobalsType.setStatus("deprecated")


class _AcBoardTrapGlobalsProbableCause_Type(Integer32):
    """Custom type acBoardTrapGlobalsProbableCause based on Integer32"""
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
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74)
        )
    )
    namedValues = NamedValues(
        *(("adapterError", 1),
          ("applicationSubsystemFailure", 2),
          ("authenticationFailure", 58),
          ("bandwidthReduced", 3),
          ("breachOfConfidentiality", 59),
          ("cableTamper", 60),
          ("callEstablishmentError", 4),
          ("communicationsProtocolError", 5),
          ("communicationsSubsystemFailure", 6),
          ("configurationOrCustomizationError", 7),
          ("congestion", 8),
          ("corruptData", 9),
          ("cpuCyclesLimitExceeded", 10),
          ("dataSetOrModemError", 11),
          ("degradedSignal", 12),
          ("delayedInformation", 61),
          ("denialOfService", 62),
          ("dteDceInterfaceError", 13),
          ("duplicateInformation", 63),
          ("enclosureDoorOpen", 14),
          ("equipmentMalfunction", 15),
          ("excessiveVibration", 16),
          ("fileError", 17),
          ("fireDetected", 18),
          ("floodDetected", 19),
          ("framingError", 20),
          ("heatingVentCoolingSystemProblem", 21),
          ("humidityUnacceptable", 22),
          ("informationMissing", 64),
          ("informationModificationDetected", 65),
          ("informationOutOfSequence", 66),
          ("inputDeviceError", 24),
          ("inputOutputDeviceError", 23),
          ("intrusionDetection", 67),
          ("keyExpired", 68),
          ("lanError", 25),
          ("leakDetected", 26),
          ("localNodeTransmissionError", 27),
          ("lossOfFrame", 28),
          ("lossOfSignal", 29),
          ("materialSupplyExhausted", 30),
          ("multiplexerProblem", 31),
          ("nonRepudiationFailure", 69),
          ("other", 0),
          ("ouputDeviceError", 33),
          ("outOfHoursActivity", 70),
          ("outOfMemory", 32),
          ("outOfService", 71),
          ("performanceDegraded", 34),
          ("powerProblem", 35),
          ("pressureUnacceptable", 36),
          ("proceduralError", 72),
          ("processorProblem", 37),
          ("pumpFailure", 38),
          ("queueSizeExceeded", 39),
          ("receiveFailure", 40),
          ("receiverFailure", 41),
          ("remoteNodeTransmissionError", 42),
          ("resourceAtOrNearingCapacity", 43),
          ("responseTimeExecessive", 44),
          ("retransmissionRateExcessive", 45),
          ("softwareError", 46),
          ("softwareProgramAbnormallyTerminated", 47),
          ("softwareProgramError", 48),
          ("storageCapacityProblem", 49),
          ("temperatureUnacceptable", 50),
          ("thresholdCrossed", 51),
          ("timingProblem", 52),
          ("toxicLeakDetected", 53),
          ("transmitFailure", 54),
          ("transmitterFailure", 55),
          ("unauthorizedAccessAttempt", 73),
          ("underlyingResourceUnavailable", 56),
          ("unexpectedInformation", 74),
          ("versionMismatch", 57))
    )


_AcBoardTrapGlobalsProbableCause_Type.__name__ = "Integer32"
_AcBoardTrapGlobalsProbableCause_Object = MibScalar
acBoardTrapGlobalsProbableCause = _AcBoardTrapGlobalsProbableCause_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 21, 1, 7),
    _AcBoardTrapGlobalsProbableCause_Type()
)
acBoardTrapGlobalsProbableCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acBoardTrapGlobalsProbableCause.setStatus("deprecated")


class _AcBoardTrapGlobalsAdditionalInfo1_Type(OctetString):
    """Custom type acBoardTrapGlobalsAdditionalInfo1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_AcBoardTrapGlobalsAdditionalInfo1_Type.__name__ = "OctetString"
_AcBoardTrapGlobalsAdditionalInfo1_Object = MibScalar
acBoardTrapGlobalsAdditionalInfo1 = _AcBoardTrapGlobalsAdditionalInfo1_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 21, 1, 8),
    _AcBoardTrapGlobalsAdditionalInfo1_Type()
)
acBoardTrapGlobalsAdditionalInfo1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acBoardTrapGlobalsAdditionalInfo1.setStatus("deprecated")


class _AcBoardTrapGlobalsAdditionalInfo2_Type(OctetString):
    """Custom type acBoardTrapGlobalsAdditionalInfo2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_AcBoardTrapGlobalsAdditionalInfo2_Type.__name__ = "OctetString"
_AcBoardTrapGlobalsAdditionalInfo2_Object = MibScalar
acBoardTrapGlobalsAdditionalInfo2 = _AcBoardTrapGlobalsAdditionalInfo2_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 21, 1, 9),
    _AcBoardTrapGlobalsAdditionalInfo2_Type()
)
acBoardTrapGlobalsAdditionalInfo2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acBoardTrapGlobalsAdditionalInfo2.setStatus("deprecated")


class _AcBoardTrapGlobalsAdditionalInfo3_Type(OctetString):
    """Custom type acBoardTrapGlobalsAdditionalInfo3 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_AcBoardTrapGlobalsAdditionalInfo3_Type.__name__ = "OctetString"
_AcBoardTrapGlobalsAdditionalInfo3_Object = MibScalar
acBoardTrapGlobalsAdditionalInfo3 = _AcBoardTrapGlobalsAdditionalInfo3_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 21, 1, 10),
    _AcBoardTrapGlobalsAdditionalInfo3_Type()
)
acBoardTrapGlobalsAdditionalInfo3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acBoardTrapGlobalsAdditionalInfo3.setStatus("deprecated")
_AcBoardTrapGlobalsDateAndTime_Type = DateAndTime
_AcBoardTrapGlobalsDateAndTime_Object = MibScalar
acBoardTrapGlobalsDateAndTime = _AcBoardTrapGlobalsDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 21, 1, 11),
    _AcBoardTrapGlobalsDateAndTime_Type()
)
acBoardTrapGlobalsDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acBoardTrapGlobalsDateAndTime.setStatus("deprecated")
_AcBoardTrapDefinitions_ObjectIdentity = ObjectIdentity
acBoardTrapDefinitions = _AcBoardTrapDefinitions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 21, 2)
)

# Managed Objects groups


# Notification objects

acBoardFatalError = NotificationType(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 21, 2, 0, 1)
)
acBoardFatalError.setObjects(
      *(("AcBoard", "acBoardTrapGlobalsName"),
        ("AcBoard", "acBoardTrapGlobalsTextualDescription"),
        ("AcBoard", "acBoardTrapGlobalsSource"),
        ("AcBoard", "acBoardTrapGlobalsSeverity"),
        ("AcBoard", "acBoardTrapGlobalsUniqID"),
        ("AcBoard", "acBoardTrapGlobalsType"),
        ("AcBoard", "acBoardTrapGlobalsProbableCause"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo1"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo2"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo3"),
        ("AcBoard", "acBoardTrapGlobalsDateAndTime"))
)
if mibBuilder.loadTexts:
    acBoardFatalError.setStatus(
        "current"
    )

acBoardConfigurationError = NotificationType(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 21, 2, 0, 2)
)
acBoardConfigurationError.setObjects(
      *(("AcBoard", "acBoardTrapGlobalsName"),
        ("AcBoard", "acBoardTrapGlobalsTextualDescription"),
        ("AcBoard", "acBoardTrapGlobalsSource"),
        ("AcBoard", "acBoardTrapGlobalsSeverity"),
        ("AcBoard", "acBoardTrapGlobalsUniqID"),
        ("AcBoard", "acBoardTrapGlobalsType"),
        ("AcBoard", "acBoardTrapGlobalsProbableCause"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo1"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo2"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo3"),
        ("AcBoard", "acBoardTrapGlobalsDateAndTime"))
)
if mibBuilder.loadTexts:
    acBoardConfigurationError.setStatus(
        "current"
    )

acBoardTemperatureAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 21, 2, 0, 3)
)
acBoardTemperatureAlarm.setObjects(
      *(("AcBoard", "acBoardTrapGlobalsName"),
        ("AcBoard", "acBoardTrapGlobalsTextualDescription"),
        ("AcBoard", "acBoardTrapGlobalsSource"),
        ("AcBoard", "acBoardTrapGlobalsSeverity"),
        ("AcBoard", "acBoardTrapGlobalsUniqID"),
        ("AcBoard", "acBoardTrapGlobalsType"),
        ("AcBoard", "acBoardTrapGlobalsProbableCause"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo1"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo2"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo3"),
        ("AcBoard", "acBoardTrapGlobalsDateAndTime"))
)
if mibBuilder.loadTexts:
    acBoardTemperatureAlarm.setStatus(
        "current"
    )

acBoardEvBoardStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 21, 2, 0, 4)
)
acBoardEvBoardStarted.setObjects(
      *(("AcBoard", "acBoardTrapGlobalsName"),
        ("AcBoard", "acBoardTrapGlobalsTextualDescription"),
        ("AcBoard", "acBoardTrapGlobalsSource"),
        ("AcBoard", "acBoardTrapGlobalsSeverity"),
        ("AcBoard", "acBoardTrapGlobalsUniqID"),
        ("AcBoard", "acBoardTrapGlobalsType"),
        ("AcBoard", "acBoardTrapGlobalsProbableCause"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo1"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo2"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo3"),
        ("AcBoard", "acBoardTrapGlobalsDateAndTime"))
)
if mibBuilder.loadTexts:
    acBoardEvBoardStarted.setStatus(
        "current"
    )

acBoardEvResettingBoard = NotificationType(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 21, 2, 0, 5)
)
acBoardEvResettingBoard.setObjects(
      *(("AcBoard", "acBoardTrapGlobalsName"),
        ("AcBoard", "acBoardTrapGlobalsTextualDescription"),
        ("AcBoard", "acBoardTrapGlobalsSource"),
        ("AcBoard", "acBoardTrapGlobalsSeverity"),
        ("AcBoard", "acBoardTrapGlobalsUniqID"),
        ("AcBoard", "acBoardTrapGlobalsType"),
        ("AcBoard", "acBoardTrapGlobalsProbableCause"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo1"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo2"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo3"),
        ("AcBoard", "acBoardTrapGlobalsDateAndTime"))
)
if mibBuilder.loadTexts:
    acBoardEvResettingBoard.setStatus(
        "current"
    )

acFeatureKeyError = NotificationType(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 21, 2, 0, 6)
)
acFeatureKeyError.setObjects(
      *(("AcBoard", "acBoardTrapGlobalsName"),
        ("AcBoard", "acBoardTrapGlobalsTextualDescription"),
        ("AcBoard", "acBoardTrapGlobalsSource"),
        ("AcBoard", "acBoardTrapGlobalsSeverity"),
        ("AcBoard", "acBoardTrapGlobalsUniqID"),
        ("AcBoard", "acBoardTrapGlobalsType"),
        ("AcBoard", "acBoardTrapGlobalsProbableCause"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo1"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo2"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo3"),
        ("AcBoard", "acBoardTrapGlobalsDateAndTime"))
)
if mibBuilder.loadTexts:
    acFeatureKeyError.setStatus(
        "current"
    )

acgwAdminStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 21, 2, 0, 7)
)
acgwAdminStateChange.setObjects(
      *(("AcBoard", "acBoardTrapGlobalsName"),
        ("AcBoard", "acBoardTrapGlobalsTextualDescription"),
        ("AcBoard", "acBoardTrapGlobalsSource"),
        ("AcBoard", "acBoardTrapGlobalsSeverity"),
        ("AcBoard", "acBoardTrapGlobalsUniqID"),
        ("AcBoard", "acBoardTrapGlobalsType"),
        ("AcBoard", "acBoardTrapGlobalsProbableCause"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo1"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo2"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo3"),
        ("AcBoard", "acBoardTrapGlobalsDateAndTime"))
)
if mibBuilder.loadTexts:
    acgwAdminStateChange.setStatus(
        "current"
    )

acBoardCallResourcesAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 21, 2, 0, 8)
)
acBoardCallResourcesAlarm.setObjects(
      *(("AcBoard", "acBoardTrapGlobalsName"),
        ("AcBoard", "acBoardTrapGlobalsTextualDescription"),
        ("AcBoard", "acBoardTrapGlobalsSource"),
        ("AcBoard", "acBoardTrapGlobalsSeverity"),
        ("AcBoard", "acBoardTrapGlobalsUniqID"),
        ("AcBoard", "acBoardTrapGlobalsType"),
        ("AcBoard", "acBoardTrapGlobalsProbableCause"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo1"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo2"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo3"),
        ("AcBoard", "acBoardTrapGlobalsDateAndTime"))
)
if mibBuilder.loadTexts:
    acBoardCallResourcesAlarm.setStatus(
        "current"
    )

acBoardControllerFailureAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 21, 2, 0, 9)
)
acBoardControllerFailureAlarm.setObjects(
      *(("AcBoard", "acBoardTrapGlobalsName"),
        ("AcBoard", "acBoardTrapGlobalsTextualDescription"),
        ("AcBoard", "acBoardTrapGlobalsSource"),
        ("AcBoard", "acBoardTrapGlobalsSeverity"),
        ("AcBoard", "acBoardTrapGlobalsUniqID"),
        ("AcBoard", "acBoardTrapGlobalsType"),
        ("AcBoard", "acBoardTrapGlobalsProbableCause"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo1"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo2"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo3"),
        ("AcBoard", "acBoardTrapGlobalsDateAndTime"))
)
if mibBuilder.loadTexts:
    acBoardControllerFailureAlarm.setStatus(
        "current"
    )

acBoardEthernetLinkAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 21, 2, 0, 10)
)
acBoardEthernetLinkAlarm.setObjects(
      *(("AcBoard", "acBoardTrapGlobalsName"),
        ("AcBoard", "acBoardTrapGlobalsTextualDescription"),
        ("AcBoard", "acBoardTrapGlobalsSource"),
        ("AcBoard", "acBoardTrapGlobalsSeverity"),
        ("AcBoard", "acBoardTrapGlobalsUniqID"),
        ("AcBoard", "acBoardTrapGlobalsType"),
        ("AcBoard", "acBoardTrapGlobalsProbableCause"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo1"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo2"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo3"),
        ("AcBoard", "acBoardTrapGlobalsDateAndTime"))
)
if mibBuilder.loadTexts:
    acBoardEthernetLinkAlarm.setStatus(
        "current"
    )

acBoardOverloadAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 21, 2, 0, 11)
)
acBoardOverloadAlarm.setObjects(
      *(("AcBoard", "acBoardTrapGlobalsName"),
        ("AcBoard", "acBoardTrapGlobalsTextualDescription"),
        ("AcBoard", "acBoardTrapGlobalsSource"),
        ("AcBoard", "acBoardTrapGlobalsSeverity"),
        ("AcBoard", "acBoardTrapGlobalsUniqID"),
        ("AcBoard", "acBoardTrapGlobalsType"),
        ("AcBoard", "acBoardTrapGlobalsProbableCause"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo1"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo2"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo3"),
        ("AcBoard", "acBoardTrapGlobalsDateAndTime"))
)
if mibBuilder.loadTexts:
    acBoardOverloadAlarm.setStatus(
        "current"
    )

acActiveAlarmTableOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 21, 2, 0, 12)
)
acActiveAlarmTableOverflow.setObjects(
      *(("AcBoard", "acBoardTrapGlobalsName"),
        ("AcBoard", "acBoardTrapGlobalsTextualDescription"),
        ("AcBoard", "acBoardTrapGlobalsSource"),
        ("AcBoard", "acBoardTrapGlobalsSeverity"),
        ("AcBoard", "acBoardTrapGlobalsUniqID"),
        ("AcBoard", "acBoardTrapGlobalsType"),
        ("AcBoard", "acBoardTrapGlobalsProbableCause"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo1"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo2"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo3"),
        ("AcBoard", "acBoardTrapGlobalsDateAndTime"))
)
if mibBuilder.loadTexts:
    acActiveAlarmTableOverflow.setStatus(
        "current"
    )

acAtmPortAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 21, 2, 0, 13)
)
acAtmPortAlarm.setObjects(
      *(("AcBoard", "acBoardTrapGlobalsName"),
        ("AcBoard", "acBoardTrapGlobalsTextualDescription"),
        ("AcBoard", "acBoardTrapGlobalsSource"),
        ("AcBoard", "acBoardTrapGlobalsSeverity"),
        ("AcBoard", "acBoardTrapGlobalsUniqID"),
        ("AcBoard", "acBoardTrapGlobalsType"),
        ("AcBoard", "acBoardTrapGlobalsProbableCause"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo1"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo2"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo3"),
        ("AcBoard", "acBoardTrapGlobalsDateAndTime"))
)
if mibBuilder.loadTexts:
    acAtmPortAlarm.setStatus(
        "current"
    )

acAudioProvisioningAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 21, 2, 0, 14)
)
acAudioProvisioningAlarm.setObjects(
      *(("AcBoard", "acBoardTrapGlobalsName"),
        ("AcBoard", "acBoardTrapGlobalsTextualDescription"),
        ("AcBoard", "acBoardTrapGlobalsSource"),
        ("AcBoard", "acBoardTrapGlobalsSeverity"),
        ("AcBoard", "acBoardTrapGlobalsUniqID"),
        ("AcBoard", "acBoardTrapGlobalsType"),
        ("AcBoard", "acBoardTrapGlobalsProbableCause"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo1"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo2"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo3"),
        ("AcBoard", "acBoardTrapGlobalsDateAndTime"))
)
if mibBuilder.loadTexts:
    acAudioProvisioningAlarm.setStatus(
        "current"
    )

acOperationalStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 21, 2, 0, 15)
)
acOperationalStateChange.setObjects(
      *(("AcBoard", "acBoardTrapGlobalsName"),
        ("AcBoard", "acBoardTrapGlobalsTextualDescription"),
        ("AcBoard", "acBoardTrapGlobalsSource"),
        ("AcBoard", "acBoardTrapGlobalsSeverity"),
        ("AcBoard", "acBoardTrapGlobalsUniqID"),
        ("AcBoard", "acBoardTrapGlobalsType"),
        ("AcBoard", "acBoardTrapGlobalsProbableCause"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo1"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo2"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo3"),
        ("AcBoard", "acBoardTrapGlobalsDateAndTime"))
)
if mibBuilder.loadTexts:
    acOperationalStateChange.setStatus(
        "current"
    )

acKeepAlive = NotificationType(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 21, 2, 0, 16)
)
acKeepAlive.setObjects(
      *(("AcBoard", "acBoardTrapGlobalsName"),
        ("AcBoard", "acBoardTrapGlobalsTextualDescription"),
        ("AcBoard", "acBoardTrapGlobalsSource"),
        ("AcBoard", "acBoardTrapGlobalsSeverity"),
        ("AcBoard", "acBoardTrapGlobalsUniqID"),
        ("AcBoard", "acBoardTrapGlobalsType"),
        ("AcBoard", "acBoardTrapGlobalsProbableCause"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo1"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo2"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo3"),
        ("AcBoard", "acBoardTrapGlobalsDateAndTime"))
)
if mibBuilder.loadTexts:
    acKeepAlive.setStatus(
        "current"
    )

acNATTraversalAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 21, 2, 0, 17)
)
acNATTraversalAlarm.setObjects(
      *(("AcBoard", "acBoardTrapGlobalsName"),
        ("AcBoard", "acBoardTrapGlobalsTextualDescription"),
        ("AcBoard", "acBoardTrapGlobalsSource"),
        ("AcBoard", "acBoardTrapGlobalsSeverity"),
        ("AcBoard", "acBoardTrapGlobalsUniqID"),
        ("AcBoard", "acBoardTrapGlobalsType"),
        ("AcBoard", "acBoardTrapGlobalsProbableCause"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo1"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo2"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo3"),
        ("AcBoard", "acBoardTrapGlobalsDateAndTime"))
)
if mibBuilder.loadTexts:
    acNATTraversalAlarm.setStatus(
        "current"
    )

acEnhancedBITStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 21, 2, 0, 18)
)
acEnhancedBITStatus.setObjects(
      *(("AcBoard", "acBoardTrapGlobalsName"),
        ("AcBoard", "acBoardTrapGlobalsTextualDescription"),
        ("AcBoard", "acBoardTrapGlobalsSource"),
        ("AcBoard", "acBoardTrapGlobalsSeverity"),
        ("AcBoard", "acBoardTrapGlobalsUniqID"),
        ("AcBoard", "acBoardTrapGlobalsType"),
        ("AcBoard", "acBoardTrapGlobalsProbableCause"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo1"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo2"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo3"),
        ("AcBoard", "acBoardTrapGlobalsDateAndTime"))
)
if mibBuilder.loadTexts:
    acEnhancedBITStatus.setStatus(
        "current"
    )

acSS7LinkStateChangeAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 21, 2, 0, 19)
)
acSS7LinkStateChangeAlarm.setObjects(
      *(("AcBoard", "acBoardTrapGlobalsName"),
        ("AcBoard", "acBoardTrapGlobalsTextualDescription"),
        ("AcBoard", "acBoardTrapGlobalsSource"),
        ("AcBoard", "acBoardTrapGlobalsSeverity"),
        ("AcBoard", "acBoardTrapGlobalsUniqID"),
        ("AcBoard", "acBoardTrapGlobalsType"),
        ("AcBoard", "acBoardTrapGlobalsProbableCause"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo1"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo2"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo3"),
        ("AcBoard", "acBoardTrapGlobalsDateAndTime"))
)
if mibBuilder.loadTexts:
    acSS7LinkStateChangeAlarm.setStatus(
        "current"
    )

acSS7LinkInhibitStateChangeAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 21, 2, 0, 20)
)
acSS7LinkInhibitStateChangeAlarm.setObjects(
      *(("AcBoard", "acBoardTrapGlobalsName"),
        ("AcBoard", "acBoardTrapGlobalsTextualDescription"),
        ("AcBoard", "acBoardTrapGlobalsSource"),
        ("AcBoard", "acBoardTrapGlobalsSeverity"),
        ("AcBoard", "acBoardTrapGlobalsUniqID"),
        ("AcBoard", "acBoardTrapGlobalsType"),
        ("AcBoard", "acBoardTrapGlobalsProbableCause"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo1"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo2"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo3"),
        ("AcBoard", "acBoardTrapGlobalsDateAndTime"))
)
if mibBuilder.loadTexts:
    acSS7LinkInhibitStateChangeAlarm.setStatus(
        "current"
    )

acSS7LinkBlockStateChangeAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 21, 2, 0, 21)
)
acSS7LinkBlockStateChangeAlarm.setObjects(
      *(("AcBoard", "acBoardTrapGlobalsName"),
        ("AcBoard", "acBoardTrapGlobalsTextualDescription"),
        ("AcBoard", "acBoardTrapGlobalsSource"),
        ("AcBoard", "acBoardTrapGlobalsSeverity"),
        ("AcBoard", "acBoardTrapGlobalsUniqID"),
        ("AcBoard", "acBoardTrapGlobalsType"),
        ("AcBoard", "acBoardTrapGlobalsProbableCause"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo1"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo2"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo3"),
        ("AcBoard", "acBoardTrapGlobalsDateAndTime"))
)
if mibBuilder.loadTexts:
    acSS7LinkBlockStateChangeAlarm.setStatus(
        "current"
    )

acSS7LinkCongestionStateChangeAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 21, 2, 0, 22)
)
acSS7LinkCongestionStateChangeAlarm.setObjects(
      *(("AcBoard", "acBoardTrapGlobalsName"),
        ("AcBoard", "acBoardTrapGlobalsTextualDescription"),
        ("AcBoard", "acBoardTrapGlobalsSource"),
        ("AcBoard", "acBoardTrapGlobalsSeverity"),
        ("AcBoard", "acBoardTrapGlobalsUniqID"),
        ("AcBoard", "acBoardTrapGlobalsType"),
        ("AcBoard", "acBoardTrapGlobalsProbableCause"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo1"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo2"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo3"),
        ("AcBoard", "acBoardTrapGlobalsDateAndTime"))
)
if mibBuilder.loadTexts:
    acSS7LinkCongestionStateChangeAlarm.setStatus(
        "current"
    )

acSS7LinkSetStateChangeAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 21, 2, 0, 23)
)
acSS7LinkSetStateChangeAlarm.setObjects(
      *(("AcBoard", "acBoardTrapGlobalsName"),
        ("AcBoard", "acBoardTrapGlobalsTextualDescription"),
        ("AcBoard", "acBoardTrapGlobalsSource"),
        ("AcBoard", "acBoardTrapGlobalsSeverity"),
        ("AcBoard", "acBoardTrapGlobalsUniqID"),
        ("AcBoard", "acBoardTrapGlobalsType"),
        ("AcBoard", "acBoardTrapGlobalsProbableCause"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo1"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo2"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo3"),
        ("AcBoard", "acBoardTrapGlobalsDateAndTime"))
)
if mibBuilder.loadTexts:
    acSS7LinkSetStateChangeAlarm.setStatus(
        "current"
    )

acSS7RouteSetStateChangeAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 21, 2, 0, 24)
)
acSS7RouteSetStateChangeAlarm.setObjects(
      *(("AcBoard", "acBoardTrapGlobalsName"),
        ("AcBoard", "acBoardTrapGlobalsTextualDescription"),
        ("AcBoard", "acBoardTrapGlobalsSource"),
        ("AcBoard", "acBoardTrapGlobalsSeverity"),
        ("AcBoard", "acBoardTrapGlobalsUniqID"),
        ("AcBoard", "acBoardTrapGlobalsType"),
        ("AcBoard", "acBoardTrapGlobalsProbableCause"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo1"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo2"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo3"),
        ("AcBoard", "acBoardTrapGlobalsDateAndTime"))
)
if mibBuilder.loadTexts:
    acSS7RouteSetStateChangeAlarm.setStatus(
        "current"
    )

acSS7SNSetStateChangeAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 21, 2, 0, 25)
)
acSS7SNSetStateChangeAlarm.setObjects(
      *(("AcBoard", "acBoardTrapGlobalsName"),
        ("AcBoard", "acBoardTrapGlobalsTextualDescription"),
        ("AcBoard", "acBoardTrapGlobalsSource"),
        ("AcBoard", "acBoardTrapGlobalsSeverity"),
        ("AcBoard", "acBoardTrapGlobalsUniqID"),
        ("AcBoard", "acBoardTrapGlobalsType"),
        ("AcBoard", "acBoardTrapGlobalsProbableCause"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo1"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo2"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo3"),
        ("AcBoard", "acBoardTrapGlobalsDateAndTime"))
)
if mibBuilder.loadTexts:
    acSS7SNSetStateChangeAlarm.setStatus(
        "current"
    )

acSS7RedundancyAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 21, 2, 0, 26)
)
acSS7RedundancyAlarm.setObjects(
      *(("AcBoard", "acBoardTrapGlobalsName"),
        ("AcBoard", "acBoardTrapGlobalsTextualDescription"),
        ("AcBoard", "acBoardTrapGlobalsSource"),
        ("AcBoard", "acBoardTrapGlobalsSeverity"),
        ("AcBoard", "acBoardTrapGlobalsUniqID"),
        ("AcBoard", "acBoardTrapGlobalsType"),
        ("AcBoard", "acBoardTrapGlobalsProbableCause"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo1"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo2"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo3"),
        ("AcBoard", "acBoardTrapGlobalsDateAndTime"))
)
if mibBuilder.loadTexts:
    acSS7RedundancyAlarm.setStatus(
        "current"
    )

acPerformanceMonitoringThresholdCrossing = NotificationType(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 21, 2, 0, 27)
)
acPerformanceMonitoringThresholdCrossing.setObjects(
      *(("AcBoard", "acBoardTrapGlobalsName"),
        ("AcBoard", "acBoardTrapGlobalsTextualDescription"),
        ("AcBoard", "acBoardTrapGlobalsSource"),
        ("AcBoard", "acBoardTrapGlobalsSeverity"),
        ("AcBoard", "acBoardTrapGlobalsUniqID"),
        ("AcBoard", "acBoardTrapGlobalsType"),
        ("AcBoard", "acBoardTrapGlobalsProbableCause"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo1"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo2"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo3"),
        ("AcBoard", "acBoardTrapGlobalsDateAndTime"))
)
if mibBuilder.loadTexts:
    acPerformanceMonitoringThresholdCrossing.setStatus(
        "current"
    )

acHTTPDownloadResult = NotificationType(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 21, 2, 0, 28)
)
acHTTPDownloadResult.setObjects(
      *(("AcBoard", "acBoardTrapGlobalsName"),
        ("AcBoard", "acBoardTrapGlobalsTextualDescription"),
        ("AcBoard", "acBoardTrapGlobalsSource"),
        ("AcBoard", "acBoardTrapGlobalsSeverity"),
        ("AcBoard", "acBoardTrapGlobalsUniqID"),
        ("AcBoard", "acBoardTrapGlobalsType"),
        ("AcBoard", "acBoardTrapGlobalsProbableCause"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo1"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo2"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo3"),
        ("AcBoard", "acBoardTrapGlobalsDateAndTime"))
)
if mibBuilder.loadTexts:
    acHTTPDownloadResult.setStatus(
        "current"
    )

acFanTrayAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 21, 2, 0, 29)
)
acFanTrayAlarm.setObjects(
      *(("AcBoard", "acBoardTrapGlobalsName"),
        ("AcBoard", "acBoardTrapGlobalsTextualDescription"),
        ("AcBoard", "acBoardTrapGlobalsSource"),
        ("AcBoard", "acBoardTrapGlobalsSeverity"),
        ("AcBoard", "acBoardTrapGlobalsUniqID"),
        ("AcBoard", "acBoardTrapGlobalsType"),
        ("AcBoard", "acBoardTrapGlobalsProbableCause"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo1"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo2"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo3"),
        ("AcBoard", "acBoardTrapGlobalsDateAndTime"))
)
if mibBuilder.loadTexts:
    acFanTrayAlarm.setStatus(
        "current"
    )

acPowerSupplyAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 21, 2, 0, 30)
)
acPowerSupplyAlarm.setObjects(
      *(("AcBoard", "acBoardTrapGlobalsName"),
        ("AcBoard", "acBoardTrapGlobalsTextualDescription"),
        ("AcBoard", "acBoardTrapGlobalsSource"),
        ("AcBoard", "acBoardTrapGlobalsSeverity"),
        ("AcBoard", "acBoardTrapGlobalsUniqID"),
        ("AcBoard", "acBoardTrapGlobalsType"),
        ("AcBoard", "acBoardTrapGlobalsProbableCause"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo1"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo2"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo3"),
        ("AcBoard", "acBoardTrapGlobalsDateAndTime"))
)
if mibBuilder.loadTexts:
    acPowerSupplyAlarm.setStatus(
        "current"
    )

acPEMAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 21, 2, 0, 31)
)
acPEMAlarm.setObjects(
      *(("AcBoard", "acBoardTrapGlobalsName"),
        ("AcBoard", "acBoardTrapGlobalsTextualDescription"),
        ("AcBoard", "acBoardTrapGlobalsSource"),
        ("AcBoard", "acBoardTrapGlobalsSeverity"),
        ("AcBoard", "acBoardTrapGlobalsUniqID"),
        ("AcBoard", "acBoardTrapGlobalsType"),
        ("AcBoard", "acBoardTrapGlobalsProbableCause"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo1"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo2"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo3"),
        ("AcBoard", "acBoardTrapGlobalsDateAndTime"))
)
if mibBuilder.loadTexts:
    acPEMAlarm.setStatus(
        "current"
    )

acSAMissingAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 21, 2, 0, 32)
)
acSAMissingAlarm.setObjects(
      *(("AcBoard", "acBoardTrapGlobalsName"),
        ("AcBoard", "acBoardTrapGlobalsTextualDescription"),
        ("AcBoard", "acBoardTrapGlobalsSource"),
        ("AcBoard", "acBoardTrapGlobalsSeverity"),
        ("AcBoard", "acBoardTrapGlobalsUniqID"),
        ("AcBoard", "acBoardTrapGlobalsType"),
        ("AcBoard", "acBoardTrapGlobalsProbableCause"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo1"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo2"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo3"),
        ("AcBoard", "acBoardTrapGlobalsDateAndTime"))
)
if mibBuilder.loadTexts:
    acSAMissingAlarm.setStatus(
        "current"
    )

acHASystemFaultAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 21, 2, 0, 33)
)
acHASystemFaultAlarm.setObjects(
      *(("AcBoard", "acBoardTrapGlobalsName"),
        ("AcBoard", "acBoardTrapGlobalsTextualDescription"),
        ("AcBoard", "acBoardTrapGlobalsSource"),
        ("AcBoard", "acBoardTrapGlobalsSeverity"),
        ("AcBoard", "acBoardTrapGlobalsUniqID"),
        ("AcBoard", "acBoardTrapGlobalsType"),
        ("AcBoard", "acBoardTrapGlobalsProbableCause"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo1"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo2"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo3"),
        ("AcBoard", "acBoardTrapGlobalsDateAndTime"))
)
if mibBuilder.loadTexts:
    acHASystemFaultAlarm.setStatus(
        "current"
    )

acHASystemConfigMismatchAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 21, 2, 0, 34)
)
acHASystemConfigMismatchAlarm.setObjects(
      *(("AcBoard", "acBoardTrapGlobalsName"),
        ("AcBoard", "acBoardTrapGlobalsTextualDescription"),
        ("AcBoard", "acBoardTrapGlobalsSource"),
        ("AcBoard", "acBoardTrapGlobalsSeverity"),
        ("AcBoard", "acBoardTrapGlobalsUniqID"),
        ("AcBoard", "acBoardTrapGlobalsType"),
        ("AcBoard", "acBoardTrapGlobalsProbableCause"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo1"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo2"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo3"),
        ("AcBoard", "acBoardTrapGlobalsDateAndTime"))
)
if mibBuilder.loadTexts:
    acHASystemConfigMismatchAlarm.setStatus(
        "current"
    )

acHASystemSwitchOverAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 21, 2, 0, 35)
)
acHASystemSwitchOverAlarm.setObjects(
      *(("AcBoard", "acBoardTrapGlobalsName"),
        ("AcBoard", "acBoardTrapGlobalsTextualDescription"),
        ("AcBoard", "acBoardTrapGlobalsSource"),
        ("AcBoard", "acBoardTrapGlobalsSeverity"),
        ("AcBoard", "acBoardTrapGlobalsUniqID"),
        ("AcBoard", "acBoardTrapGlobalsType"),
        ("AcBoard", "acBoardTrapGlobalsProbableCause"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo1"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo2"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo3"),
        ("AcBoard", "acBoardTrapGlobalsDateAndTime"))
)
if mibBuilder.loadTexts:
    acHASystemSwitchOverAlarm.setStatus(
        "current"
    )

acUserInputAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 21, 2, 0, 36)
)
acUserInputAlarm.setObjects(
      *(("AcBoard", "acBoardTrapGlobalsName"),
        ("AcBoard", "acBoardTrapGlobalsTextualDescription"),
        ("AcBoard", "acBoardTrapGlobalsSource"),
        ("AcBoard", "acBoardTrapGlobalsSeverity"),
        ("AcBoard", "acBoardTrapGlobalsUniqID"),
        ("AcBoard", "acBoardTrapGlobalsType"),
        ("AcBoard", "acBoardTrapGlobalsProbableCause"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo1"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo2"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo3"),
        ("AcBoard", "acBoardTrapGlobalsDateAndTime"))
)
if mibBuilder.loadTexts:
    acUserInputAlarm.setStatus(
        "current"
    )

acDChannelStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 21, 2, 0, 37)
)
acDChannelStatus.setObjects(
      *(("AcBoard", "acBoardTrapGlobalsName"),
        ("AcBoard", "acBoardTrapGlobalsTextualDescription"),
        ("AcBoard", "acBoardTrapGlobalsSource"),
        ("AcBoard", "acBoardTrapGlobalsSeverity"),
        ("AcBoard", "acBoardTrapGlobalsUniqID"),
        ("AcBoard", "acBoardTrapGlobalsType"),
        ("AcBoard", "acBoardTrapGlobalsProbableCause"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo1"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo2"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo3"),
        ("AcBoard", "acBoardTrapGlobalsDateAndTime"))
)
if mibBuilder.loadTexts:
    acDChannelStatus.setStatus(
        "current"
    )

acSonetSectionLOFAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 21, 2, 0, 38)
)
acSonetSectionLOFAlarm.setObjects(
      *(("AcBoard", "acBoardTrapGlobalsName"),
        ("AcBoard", "acBoardTrapGlobalsTextualDescription"),
        ("AcBoard", "acBoardTrapGlobalsSource"),
        ("AcBoard", "acBoardTrapGlobalsSeverity"),
        ("AcBoard", "acBoardTrapGlobalsUniqID"),
        ("AcBoard", "acBoardTrapGlobalsType"),
        ("AcBoard", "acBoardTrapGlobalsProbableCause"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo1"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo2"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo3"),
        ("AcBoard", "acBoardTrapGlobalsDateAndTime"))
)
if mibBuilder.loadTexts:
    acSonetSectionLOFAlarm.setStatus(
        "current"
    )

acSonetSectionLOSAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 21, 2, 0, 39)
)
acSonetSectionLOSAlarm.setObjects(
      *(("AcBoard", "acBoardTrapGlobalsName"),
        ("AcBoard", "acBoardTrapGlobalsTextualDescription"),
        ("AcBoard", "acBoardTrapGlobalsSource"),
        ("AcBoard", "acBoardTrapGlobalsSeverity"),
        ("AcBoard", "acBoardTrapGlobalsUniqID"),
        ("AcBoard", "acBoardTrapGlobalsType"),
        ("AcBoard", "acBoardTrapGlobalsProbableCause"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo1"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo2"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo3"),
        ("AcBoard", "acBoardTrapGlobalsDateAndTime"))
)
if mibBuilder.loadTexts:
    acSonetSectionLOSAlarm.setStatus(
        "current"
    )

acSonetLineAISAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 21, 2, 0, 40)
)
acSonetLineAISAlarm.setObjects(
      *(("AcBoard", "acBoardTrapGlobalsName"),
        ("AcBoard", "acBoardTrapGlobalsTextualDescription"),
        ("AcBoard", "acBoardTrapGlobalsSource"),
        ("AcBoard", "acBoardTrapGlobalsSeverity"),
        ("AcBoard", "acBoardTrapGlobalsUniqID"),
        ("AcBoard", "acBoardTrapGlobalsType"),
        ("AcBoard", "acBoardTrapGlobalsProbableCause"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo1"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo2"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo3"),
        ("AcBoard", "acBoardTrapGlobalsDateAndTime"))
)
if mibBuilder.loadTexts:
    acSonetLineAISAlarm.setStatus(
        "current"
    )

acSonetLineRDIAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 21, 2, 0, 41)
)
acSonetLineRDIAlarm.setObjects(
      *(("AcBoard", "acBoardTrapGlobalsName"),
        ("AcBoard", "acBoardTrapGlobalsTextualDescription"),
        ("AcBoard", "acBoardTrapGlobalsSource"),
        ("AcBoard", "acBoardTrapGlobalsSeverity"),
        ("AcBoard", "acBoardTrapGlobalsUniqID"),
        ("AcBoard", "acBoardTrapGlobalsType"),
        ("AcBoard", "acBoardTrapGlobalsProbableCause"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo1"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo2"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo3"),
        ("AcBoard", "acBoardTrapGlobalsDateAndTime"))
)
if mibBuilder.loadTexts:
    acSonetLineRDIAlarm.setStatus(
        "current"
    )

acSonetIfHwFailureAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 21, 2, 0, 42)
)
acSonetIfHwFailureAlarm.setObjects(
      *(("AcBoard", "acBoardTrapGlobalsName"),
        ("AcBoard", "acBoardTrapGlobalsTextualDescription"),
        ("AcBoard", "acBoardTrapGlobalsSource"),
        ("AcBoard", "acBoardTrapGlobalsSeverity"),
        ("AcBoard", "acBoardTrapGlobalsUniqID"),
        ("AcBoard", "acBoardTrapGlobalsType"),
        ("AcBoard", "acBoardTrapGlobalsProbableCause"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo1"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo2"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo3"),
        ("AcBoard", "acBoardTrapGlobalsDateAndTime"))
)
if mibBuilder.loadTexts:
    acSonetIfHwFailureAlarm.setStatus(
        "current"
    )

acHwFailureAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 21, 2, 0, 43)
)
acHwFailureAlarm.setObjects(
      *(("AcBoard", "acBoardTrapGlobalsName"),
        ("AcBoard", "acBoardTrapGlobalsTextualDescription"),
        ("AcBoard", "acBoardTrapGlobalsSource"),
        ("AcBoard", "acBoardTrapGlobalsSeverity"),
        ("AcBoard", "acBoardTrapGlobalsUniqID"),
        ("AcBoard", "acBoardTrapGlobalsType"),
        ("AcBoard", "acBoardTrapGlobalsProbableCause"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo1"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo2"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo3"),
        ("AcBoard", "acBoardTrapGlobalsDateAndTime"))
)
if mibBuilder.loadTexts:
    acHwFailureAlarm.setStatus(
        "current"
    )

acH248LostConnectionWithCA = NotificationType(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 21, 2, 0, 44)
)
acH248LostConnectionWithCA.setObjects(
      *(("AcBoard", "acBoardTrapGlobalsName"),
        ("AcBoard", "acBoardTrapGlobalsTextualDescription"),
        ("AcBoard", "acBoardTrapGlobalsSource"),
        ("AcBoard", "acBoardTrapGlobalsSeverity"),
        ("AcBoard", "acBoardTrapGlobalsUniqID"),
        ("AcBoard", "acBoardTrapGlobalsType"),
        ("AcBoard", "acBoardTrapGlobalsProbableCause"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo1"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo2"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo3"),
        ("AcBoard", "acBoardTrapGlobalsDateAndTime"))
)
if mibBuilder.loadTexts:
    acH248LostConnectionWithCA.setStatus(
        "current"
    )

acDialPlanFileReplaced = NotificationType(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 21, 2, 0, 45)
)
acDialPlanFileReplaced.setObjects(
      *(("AcBoard", "acBoardTrapGlobalsName"),
        ("AcBoard", "acBoardTrapGlobalsTextualDescription"),
        ("AcBoard", "acBoardTrapGlobalsSource"),
        ("AcBoard", "acBoardTrapGlobalsSeverity"),
        ("AcBoard", "acBoardTrapGlobalsUniqID"),
        ("AcBoard", "acBoardTrapGlobalsType"),
        ("AcBoard", "acBoardTrapGlobalsProbableCause"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo1"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo2"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo3"),
        ("AcBoard", "acBoardTrapGlobalsDateAndTime"))
)
if mibBuilder.loadTexts:
    acDialPlanFileReplaced.setStatus(
        "current"
    )

acAnalogPortSPIOutOfService = NotificationType(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 21, 2, 0, 46)
)
acAnalogPortSPIOutOfService.setObjects(
      *(("AcBoard", "acBoardTrapGlobalsName"),
        ("AcBoard", "acBoardTrapGlobalsTextualDescription"),
        ("AcBoard", "acBoardTrapGlobalsSource"),
        ("AcBoard", "acBoardTrapGlobalsSeverity"),
        ("AcBoard", "acBoardTrapGlobalsUniqID"),
        ("AcBoard", "acBoardTrapGlobalsType"),
        ("AcBoard", "acBoardTrapGlobalsProbableCause"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo1"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo2"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo3"),
        ("AcBoard", "acBoardTrapGlobalsDateAndTime"))
)
if mibBuilder.loadTexts:
    acAnalogPortSPIOutOfService.setStatus(
        "current"
    )

acAnalogPortHighTemperature = NotificationType(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 21, 2, 0, 47)
)
acAnalogPortHighTemperature.setObjects(
      *(("AcBoard", "acBoardTrapGlobalsName"),
        ("AcBoard", "acBoardTrapGlobalsTextualDescription"),
        ("AcBoard", "acBoardTrapGlobalsSource"),
        ("AcBoard", "acBoardTrapGlobalsSeverity"),
        ("AcBoard", "acBoardTrapGlobalsUniqID"),
        ("AcBoard", "acBoardTrapGlobalsType"),
        ("AcBoard", "acBoardTrapGlobalsProbableCause"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo1"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo2"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo3"),
        ("AcBoard", "acBoardTrapGlobalsDateAndTime"))
)
if mibBuilder.loadTexts:
    acAnalogPortHighTemperature.setStatus(
        "current"
    )

acHitlessUpdateStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 21, 2, 0, 48)
)
acHitlessUpdateStatus.setObjects(
      *(("AcBoard", "acBoardTrapGlobalsName"),
        ("AcBoard", "acBoardTrapGlobalsTextualDescription"),
        ("AcBoard", "acBoardTrapGlobalsSource"),
        ("AcBoard", "acBoardTrapGlobalsSeverity"),
        ("AcBoard", "acBoardTrapGlobalsUniqID"),
        ("AcBoard", "acBoardTrapGlobalsType"),
        ("AcBoard", "acBoardTrapGlobalsProbableCause"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo1"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo2"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo3"),
        ("AcBoard", "acBoardTrapGlobalsDateAndTime"))
)
if mibBuilder.loadTexts:
    acHitlessUpdateStatus.setStatus(
        "current"
    )

acTrunksAlarmNearEndLOS = NotificationType(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 21, 2, 0, 49)
)
acTrunksAlarmNearEndLOS.setObjects(
      *(("AcBoard", "acBoardTrapGlobalsName"),
        ("AcBoard", "acBoardTrapGlobalsTextualDescription"),
        ("AcBoard", "acBoardTrapGlobalsSource"),
        ("AcBoard", "acBoardTrapGlobalsSeverity"),
        ("AcBoard", "acBoardTrapGlobalsUniqID"),
        ("AcBoard", "acBoardTrapGlobalsType"),
        ("AcBoard", "acBoardTrapGlobalsProbableCause"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo1"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo2"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo3"),
        ("AcBoard", "acBoardTrapGlobalsDateAndTime"))
)
if mibBuilder.loadTexts:
    acTrunksAlarmNearEndLOS.setStatus(
        "current"
    )

acTrunksAlarmNearEndLOF = NotificationType(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 21, 2, 0, 50)
)
acTrunksAlarmNearEndLOF.setObjects(
      *(("AcBoard", "acBoardTrapGlobalsName"),
        ("AcBoard", "acBoardTrapGlobalsTextualDescription"),
        ("AcBoard", "acBoardTrapGlobalsSource"),
        ("AcBoard", "acBoardTrapGlobalsSeverity"),
        ("AcBoard", "acBoardTrapGlobalsUniqID"),
        ("AcBoard", "acBoardTrapGlobalsType"),
        ("AcBoard", "acBoardTrapGlobalsProbableCause"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo1"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo2"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo3"),
        ("AcBoard", "acBoardTrapGlobalsDateAndTime"))
)
if mibBuilder.loadTexts:
    acTrunksAlarmNearEndLOF.setStatus(
        "current"
    )

acTrunksAlarmRcvAIS = NotificationType(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 21, 2, 0, 51)
)
acTrunksAlarmRcvAIS.setObjects(
      *(("AcBoard", "acBoardTrapGlobalsName"),
        ("AcBoard", "acBoardTrapGlobalsTextualDescription"),
        ("AcBoard", "acBoardTrapGlobalsSource"),
        ("AcBoard", "acBoardTrapGlobalsSeverity"),
        ("AcBoard", "acBoardTrapGlobalsUniqID"),
        ("AcBoard", "acBoardTrapGlobalsType"),
        ("AcBoard", "acBoardTrapGlobalsProbableCause"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo1"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo2"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo3"),
        ("AcBoard", "acBoardTrapGlobalsDateAndTime"))
)
if mibBuilder.loadTexts:
    acTrunksAlarmRcvAIS.setStatus(
        "current"
    )

acTrunksAlarmFarEndLOF = NotificationType(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 21, 2, 0, 52)
)
acTrunksAlarmFarEndLOF.setObjects(
      *(("AcBoard", "acBoardTrapGlobalsName"),
        ("AcBoard", "acBoardTrapGlobalsTextualDescription"),
        ("AcBoard", "acBoardTrapGlobalsSource"),
        ("AcBoard", "acBoardTrapGlobalsSeverity"),
        ("AcBoard", "acBoardTrapGlobalsUniqID"),
        ("AcBoard", "acBoardTrapGlobalsType"),
        ("AcBoard", "acBoardTrapGlobalsProbableCause"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo1"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo2"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo3"),
        ("AcBoard", "acBoardTrapGlobalsDateAndTime"))
)
if mibBuilder.loadTexts:
    acTrunksAlarmFarEndLOF.setStatus(
        "current"
    )

acIPv6ErrorAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 21, 2, 0, 53)
)
acIPv6ErrorAlarm.setObjects(
      *(("AcBoard", "acBoardTrapGlobalsName"),
        ("AcBoard", "acBoardTrapGlobalsTextualDescription"),
        ("AcBoard", "acBoardTrapGlobalsSource"),
        ("AcBoard", "acBoardTrapGlobalsSeverity"),
        ("AcBoard", "acBoardTrapGlobalsUniqID"),
        ("AcBoard", "acBoardTrapGlobalsType"),
        ("AcBoard", "acBoardTrapGlobalsProbableCause"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo1"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo2"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo3"),
        ("AcBoard", "acBoardTrapGlobalsDateAndTime"))
)
if mibBuilder.loadTexts:
    acIPv6ErrorAlarm.setStatus(
        "current"
    )

acAMSProcedureResult = NotificationType(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 21, 2, 0, 54)
)
acAMSProcedureResult.setObjects(
      *(("AcBoard", "acBoardTrapGlobalsName"),
        ("AcBoard", "acBoardTrapGlobalsTextualDescription"),
        ("AcBoard", "acBoardTrapGlobalsSource"),
        ("AcBoard", "acBoardTrapGlobalsSeverity"),
        ("AcBoard", "acBoardTrapGlobalsUniqID"),
        ("AcBoard", "acBoardTrapGlobalsType"),
        ("AcBoard", "acBoardTrapGlobalsProbableCause"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo1"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo2"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo3"),
        ("AcBoard", "acBoardTrapGlobalsDateAndTime"))
)
if mibBuilder.loadTexts:
    acAMSProcedureResult.setStatus(
        "current"
    )

acWeakRedundancy = NotificationType(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 21, 2, 0, 55)
)
acWeakRedundancy.setObjects(
      *(("AcBoard", "acBoardTrapGlobalsName"),
        ("AcBoard", "acBoardTrapGlobalsTextualDescription"),
        ("AcBoard", "acBoardTrapGlobalsSource"),
        ("AcBoard", "acBoardTrapGlobalsSeverity"),
        ("AcBoard", "acBoardTrapGlobalsUniqID"),
        ("AcBoard", "acBoardTrapGlobalsType"),
        ("AcBoard", "acBoardTrapGlobalsProbableCause"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo1"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo2"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo3"),
        ("AcBoard", "acBoardTrapGlobalsDateAndTime"))
)
if mibBuilder.loadTexts:
    acWeakRedundancy.setStatus(
        "current"
    )

acTMInconsistentRemoteAndLocalPLLStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 21, 2, 0, 56)
)
acTMInconsistentRemoteAndLocalPLLStatus.setObjects(
      *(("AcBoard", "acBoardTrapGlobalsName"),
        ("AcBoard", "acBoardTrapGlobalsTextualDescription"),
        ("AcBoard", "acBoardTrapGlobalsSource"),
        ("AcBoard", "acBoardTrapGlobalsSeverity"),
        ("AcBoard", "acBoardTrapGlobalsUniqID"),
        ("AcBoard", "acBoardTrapGlobalsType"),
        ("AcBoard", "acBoardTrapGlobalsProbableCause"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo1"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo2"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo3"),
        ("AcBoard", "acBoardTrapGlobalsDateAndTime"))
)
if mibBuilder.loadTexts:
    acTMInconsistentRemoteAndLocalPLLStatus.setStatus(
        "current"
    )

acTMReferenceStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 21, 2, 0, 57)
)
acTMReferenceStatus.setObjects(
      *(("AcBoard", "acBoardTrapGlobalsName"),
        ("AcBoard", "acBoardTrapGlobalsTextualDescription"),
        ("AcBoard", "acBoardTrapGlobalsSource"),
        ("AcBoard", "acBoardTrapGlobalsSeverity"),
        ("AcBoard", "acBoardTrapGlobalsUniqID"),
        ("AcBoard", "acBoardTrapGlobalsType"),
        ("AcBoard", "acBoardTrapGlobalsProbableCause"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo1"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo2"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo3"),
        ("AcBoard", "acBoardTrapGlobalsDateAndTime"))
)
if mibBuilder.loadTexts:
    acTMReferenceStatus.setStatus(
        "current"
    )

acTMReferenceChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 21, 2, 0, 58)
)
acTMReferenceChange.setObjects(
      *(("AcBoard", "acBoardTrapGlobalsName"),
        ("AcBoard", "acBoardTrapGlobalsTextualDescription"),
        ("AcBoard", "acBoardTrapGlobalsSource"),
        ("AcBoard", "acBoardTrapGlobalsSeverity"),
        ("AcBoard", "acBoardTrapGlobalsUniqID"),
        ("AcBoard", "acBoardTrapGlobalsType"),
        ("AcBoard", "acBoardTrapGlobalsProbableCause"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo1"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo2"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo3"),
        ("AcBoard", "acBoardTrapGlobalsDateAndTime"))
)
if mibBuilder.loadTexts:
    acTMReferenceChange.setStatus(
        "current"
    )

acGWSASEmergencyModeAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 21, 2, 0, 59)
)
acGWSASEmergencyModeAlarm.setObjects(
      *(("AcBoard", "acBoardTrapGlobalsName"),
        ("AcBoard", "acBoardTrapGlobalsTextualDescription"),
        ("AcBoard", "acBoardTrapGlobalsSource"),
        ("AcBoard", "acBoardTrapGlobalsSeverity"),
        ("AcBoard", "acBoardTrapGlobalsUniqID"),
        ("AcBoard", "acBoardTrapGlobalsType"),
        ("AcBoard", "acBoardTrapGlobalsProbableCause"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo1"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo2"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo3"),
        ("AcBoard", "acBoardTrapGlobalsDateAndTime"))
)
if mibBuilder.loadTexts:
    acGWSASEmergencyModeAlarm.setStatus(
        "current"
    )

acV52InterfaceAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 21, 2, 0, 60)
)
acV52InterfaceAlarm.setObjects(
      *(("AcBoard", "acBoardTrapGlobalsName"),
        ("AcBoard", "acBoardTrapGlobalsTextualDescription"),
        ("AcBoard", "acBoardTrapGlobalsSource"),
        ("AcBoard", "acBoardTrapGlobalsSeverity"),
        ("AcBoard", "acBoardTrapGlobalsUniqID"),
        ("AcBoard", "acBoardTrapGlobalsType"),
        ("AcBoard", "acBoardTrapGlobalsProbableCause"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo1"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo2"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo3"),
        ("AcBoard", "acBoardTrapGlobalsDateAndTime"))
)
if mibBuilder.loadTexts:
    acV52InterfaceAlarm.setStatus(
        "current"
    )

acSonetPathSTSLOPAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 21, 2, 0, 61)
)
acSonetPathSTSLOPAlarm.setObjects(
      *(("AcBoard", "acBoardTrapGlobalsName"),
        ("AcBoard", "acBoardTrapGlobalsTextualDescription"),
        ("AcBoard", "acBoardTrapGlobalsSource"),
        ("AcBoard", "acBoardTrapGlobalsSeverity"),
        ("AcBoard", "acBoardTrapGlobalsUniqID"),
        ("AcBoard", "acBoardTrapGlobalsType"),
        ("AcBoard", "acBoardTrapGlobalsProbableCause"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo1"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo2"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo3"),
        ("AcBoard", "acBoardTrapGlobalsDateAndTime"))
)
if mibBuilder.loadTexts:
    acSonetPathSTSLOPAlarm.setStatus(
        "current"
    )

acSonetPathSTSAISAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 21, 2, 0, 62)
)
acSonetPathSTSAISAlarm.setObjects(
      *(("AcBoard", "acBoardTrapGlobalsName"),
        ("AcBoard", "acBoardTrapGlobalsTextualDescription"),
        ("AcBoard", "acBoardTrapGlobalsSource"),
        ("AcBoard", "acBoardTrapGlobalsSeverity"),
        ("AcBoard", "acBoardTrapGlobalsUniqID"),
        ("AcBoard", "acBoardTrapGlobalsType"),
        ("AcBoard", "acBoardTrapGlobalsProbableCause"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo1"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo2"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo3"),
        ("AcBoard", "acBoardTrapGlobalsDateAndTime"))
)
if mibBuilder.loadTexts:
    acSonetPathSTSAISAlarm.setStatus(
        "current"
    )

acSonetPathSTSRDIAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 21, 2, 0, 63)
)
acSonetPathSTSRDIAlarm.setObjects(
      *(("AcBoard", "acBoardTrapGlobalsName"),
        ("AcBoard", "acBoardTrapGlobalsTextualDescription"),
        ("AcBoard", "acBoardTrapGlobalsSource"),
        ("AcBoard", "acBoardTrapGlobalsSeverity"),
        ("AcBoard", "acBoardTrapGlobalsUniqID"),
        ("AcBoard", "acBoardTrapGlobalsType"),
        ("AcBoard", "acBoardTrapGlobalsProbableCause"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo1"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo2"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo3"),
        ("AcBoard", "acBoardTrapGlobalsDateAndTime"))
)
if mibBuilder.loadTexts:
    acSonetPathSTSRDIAlarm.setStatus(
        "current"
    )

acSonetPathUnequippedAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 21, 2, 0, 64)
)
acSonetPathUnequippedAlarm.setObjects(
      *(("AcBoard", "acBoardTrapGlobalsName"),
        ("AcBoard", "acBoardTrapGlobalsTextualDescription"),
        ("AcBoard", "acBoardTrapGlobalsSource"),
        ("AcBoard", "acBoardTrapGlobalsSeverity"),
        ("AcBoard", "acBoardTrapGlobalsUniqID"),
        ("AcBoard", "acBoardTrapGlobalsType"),
        ("AcBoard", "acBoardTrapGlobalsProbableCause"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo1"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo2"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo3"),
        ("AcBoard", "acBoardTrapGlobalsDateAndTime"))
)
if mibBuilder.loadTexts:
    acSonetPathUnequippedAlarm.setStatus(
        "current"
    )

acSonetPathSignalLabelMismatchAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 21, 2, 0, 65)
)
acSonetPathSignalLabelMismatchAlarm.setObjects(
      *(("AcBoard", "acBoardTrapGlobalsName"),
        ("AcBoard", "acBoardTrapGlobalsTextualDescription"),
        ("AcBoard", "acBoardTrapGlobalsSource"),
        ("AcBoard", "acBoardTrapGlobalsSeverity"),
        ("AcBoard", "acBoardTrapGlobalsUniqID"),
        ("AcBoard", "acBoardTrapGlobalsType"),
        ("AcBoard", "acBoardTrapGlobalsProbableCause"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo1"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo2"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo3"),
        ("AcBoard", "acBoardTrapGlobalsDateAndTime"))
)
if mibBuilder.loadTexts:
    acSonetPathSignalLabelMismatchAlarm.setStatus(
        "current"
    )

acDS3RAIAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 21, 2, 0, 66)
)
acDS3RAIAlarm.setObjects(
      *(("AcBoard", "acBoardTrapGlobalsName"),
        ("AcBoard", "acBoardTrapGlobalsTextualDescription"),
        ("AcBoard", "acBoardTrapGlobalsSource"),
        ("AcBoard", "acBoardTrapGlobalsSeverity"),
        ("AcBoard", "acBoardTrapGlobalsUniqID"),
        ("AcBoard", "acBoardTrapGlobalsType"),
        ("AcBoard", "acBoardTrapGlobalsProbableCause"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo1"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo2"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo3"),
        ("AcBoard", "acBoardTrapGlobalsDateAndTime"))
)
if mibBuilder.loadTexts:
    acDS3RAIAlarm.setStatus(
        "current"
    )

acDS3AISAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 21, 2, 0, 67)
)
acDS3AISAlarm.setObjects(
      *(("AcBoard", "acBoardTrapGlobalsName"),
        ("AcBoard", "acBoardTrapGlobalsTextualDescription"),
        ("AcBoard", "acBoardTrapGlobalsSource"),
        ("AcBoard", "acBoardTrapGlobalsSeverity"),
        ("AcBoard", "acBoardTrapGlobalsUniqID"),
        ("AcBoard", "acBoardTrapGlobalsType"),
        ("AcBoard", "acBoardTrapGlobalsProbableCause"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo1"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo2"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo3"),
        ("AcBoard", "acBoardTrapGlobalsDateAndTime"))
)
if mibBuilder.loadTexts:
    acDS3AISAlarm.setStatus(
        "current"
    )

acDS3LOFAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 21, 2, 0, 68)
)
acDS3LOFAlarm.setObjects(
      *(("AcBoard", "acBoardTrapGlobalsName"),
        ("AcBoard", "acBoardTrapGlobalsTextualDescription"),
        ("AcBoard", "acBoardTrapGlobalsSource"),
        ("AcBoard", "acBoardTrapGlobalsSeverity"),
        ("AcBoard", "acBoardTrapGlobalsUniqID"),
        ("AcBoard", "acBoardTrapGlobalsType"),
        ("AcBoard", "acBoardTrapGlobalsProbableCause"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo1"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo2"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo3"),
        ("AcBoard", "acBoardTrapGlobalsDateAndTime"))
)
if mibBuilder.loadTexts:
    acDS3LOFAlarm.setStatus(
        "current"
    )

acDS3LOSAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 21, 2, 0, 69)
)
acDS3LOSAlarm.setObjects(
      *(("AcBoard", "acBoardTrapGlobalsName"),
        ("AcBoard", "acBoardTrapGlobalsTextualDescription"),
        ("AcBoard", "acBoardTrapGlobalsSource"),
        ("AcBoard", "acBoardTrapGlobalsSeverity"),
        ("AcBoard", "acBoardTrapGlobalsUniqID"),
        ("AcBoard", "acBoardTrapGlobalsType"),
        ("AcBoard", "acBoardTrapGlobalsProbableCause"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo1"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo2"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo3"),
        ("AcBoard", "acBoardTrapGlobalsDateAndTime"))
)
if mibBuilder.loadTexts:
    acDS3LOSAlarm.setStatus(
        "current"
    )

acSWUpgradeAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 21, 2, 0, 70)
)
acSWUpgradeAlarm.setObjects(
      *(("AcBoard", "acBoardTrapGlobalsName"),
        ("AcBoard", "acBoardTrapGlobalsTextualDescription"),
        ("AcBoard", "acBoardTrapGlobalsSource"),
        ("AcBoard", "acBoardTrapGlobalsSeverity"),
        ("AcBoard", "acBoardTrapGlobalsUniqID"),
        ("AcBoard", "acBoardTrapGlobalsType"),
        ("AcBoard", "acBoardTrapGlobalsProbableCause"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo1"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo2"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo3"),
        ("AcBoard", "acBoardTrapGlobalsDateAndTime"))
)
if mibBuilder.loadTexts:
    acSWUpgradeAlarm.setStatus(
        "current"
    )

acNTPServerStatusAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 21, 2, 0, 71)
)
acNTPServerStatusAlarm.setObjects(
      *(("AcBoard", "acBoardTrapGlobalsName"),
        ("AcBoard", "acBoardTrapGlobalsTextualDescription"),
        ("AcBoard", "acBoardTrapGlobalsSource"),
        ("AcBoard", "acBoardTrapGlobalsSeverity"),
        ("AcBoard", "acBoardTrapGlobalsUniqID"),
        ("AcBoard", "acBoardTrapGlobalsType"),
        ("AcBoard", "acBoardTrapGlobalsProbableCause"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo1"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo2"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo3"),
        ("AcBoard", "acBoardTrapGlobalsDateAndTime"))
)
if mibBuilder.loadTexts:
    acNTPServerStatusAlarm.setStatus(
        "current"
    )

acThreeWayConferenceOutOfResources = NotificationType(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 21, 2, 0, 72)
)
acThreeWayConferenceOutOfResources.setObjects(
      *(("AcBoard", "acBoardTrapGlobalsName"),
        ("AcBoard", "acBoardTrapGlobalsTextualDescription"),
        ("AcBoard", "acBoardTrapGlobalsSource"),
        ("AcBoard", "acBoardTrapGlobalsSeverity"),
        ("AcBoard", "acBoardTrapGlobalsUniqID"),
        ("AcBoard", "acBoardTrapGlobalsType"),
        ("AcBoard", "acBoardTrapGlobalsProbableCause"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo1"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo2"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo3"),
        ("AcBoard", "acBoardTrapGlobalsDateAndTime"))
)
if mibBuilder.loadTexts:
    acThreeWayConferenceOutOfResources.setStatus(
        "current"
    )

acSS7AliasPcStateChangeAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 21, 2, 0, 73)
)
acSS7AliasPcStateChangeAlarm.setObjects(
      *(("AcBoard", "acBoardTrapGlobalsName"),
        ("AcBoard", "acBoardTrapGlobalsTextualDescription"),
        ("AcBoard", "acBoardTrapGlobalsSource"),
        ("AcBoard", "acBoardTrapGlobalsSeverity"),
        ("AcBoard", "acBoardTrapGlobalsUniqID"),
        ("AcBoard", "acBoardTrapGlobalsType"),
        ("AcBoard", "acBoardTrapGlobalsProbableCause"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo1"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo2"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo3"),
        ("AcBoard", "acBoardTrapGlobalsDateAndTime"))
)
if mibBuilder.loadTexts:
    acSS7AliasPcStateChangeAlarm.setStatus(
        "current"
    )

acSS7UalGroupStateChangeAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 21, 2, 0, 74)
)
acSS7UalGroupStateChangeAlarm.setObjects(
      *(("AcBoard", "acBoardTrapGlobalsName"),
        ("AcBoard", "acBoardTrapGlobalsTextualDescription"),
        ("AcBoard", "acBoardTrapGlobalsSource"),
        ("AcBoard", "acBoardTrapGlobalsSeverity"),
        ("AcBoard", "acBoardTrapGlobalsUniqID"),
        ("AcBoard", "acBoardTrapGlobalsType"),
        ("AcBoard", "acBoardTrapGlobalsProbableCause"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo1"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo2"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo3"),
        ("AcBoard", "acBoardTrapGlobalsDateAndTime"))
)
if mibBuilder.loadTexts:
    acSS7UalGroupStateChangeAlarm.setStatus(
        "current"
    )

acLDAPLostConnection = NotificationType(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 21, 2, 0, 75)
)
acLDAPLostConnection.setObjects(
      *(("AcBoard", "acBoardTrapGlobalsName"),
        ("AcBoard", "acBoardTrapGlobalsTextualDescription"),
        ("AcBoard", "acBoardTrapGlobalsSource"),
        ("AcBoard", "acBoardTrapGlobalsSeverity"),
        ("AcBoard", "acBoardTrapGlobalsUniqID"),
        ("AcBoard", "acBoardTrapGlobalsType"),
        ("AcBoard", "acBoardTrapGlobalsProbableCause"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo1"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo2"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo3"),
        ("AcBoard", "acBoardTrapGlobalsDateAndTime"))
)
if mibBuilder.loadTexts:
    acLDAPLostConnection.setStatus(
        "current"
    )

acAnalogPortGroundFaultOutOfService = NotificationType(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 21, 2, 0, 76)
)
acAnalogPortGroundFaultOutOfService.setObjects(
      *(("AcBoard", "acBoardTrapGlobalsName"),
        ("AcBoard", "acBoardTrapGlobalsTextualDescription"),
        ("AcBoard", "acBoardTrapGlobalsSource"),
        ("AcBoard", "acBoardTrapGlobalsSeverity"),
        ("AcBoard", "acBoardTrapGlobalsUniqID"),
        ("AcBoard", "acBoardTrapGlobalsType"),
        ("AcBoard", "acBoardTrapGlobalsProbableCause"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo1"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo2"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo3"),
        ("AcBoard", "acBoardTrapGlobalsDateAndTime"))
)
if mibBuilder.loadTexts:
    acAnalogPortGroundFaultOutOfService.setStatus(
        "current"
    )

acSSHConnectionStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 21, 2, 0, 77)
)
acSSHConnectionStatus.setObjects(
      *(("AcBoard", "acBoardTrapGlobalsName"),
        ("AcBoard", "acBoardTrapGlobalsTextualDescription"),
        ("AcBoard", "acBoardTrapGlobalsSource"),
        ("AcBoard", "acBoardTrapGlobalsSeverity"),
        ("AcBoard", "acBoardTrapGlobalsUniqID"),
        ("AcBoard", "acBoardTrapGlobalsType"),
        ("AcBoard", "acBoardTrapGlobalsProbableCause"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo1"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo2"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo3"),
        ("AcBoard", "acBoardTrapGlobalsDateAndTime"))
)
if mibBuilder.loadTexts:
    acSSHConnectionStatus.setStatus(
        "current"
    )

acOCSPServerStatusAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 1, 21, 2, 0, 78)
)
acOCSPServerStatusAlarm.setObjects(
      *(("AcBoard", "acBoardTrapGlobalsName"),
        ("AcBoard", "acBoardTrapGlobalsTextualDescription"),
        ("AcBoard", "acBoardTrapGlobalsSource"),
        ("AcBoard", "acBoardTrapGlobalsSeverity"),
        ("AcBoard", "acBoardTrapGlobalsUniqID"),
        ("AcBoard", "acBoardTrapGlobalsType"),
        ("AcBoard", "acBoardTrapGlobalsProbableCause"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo1"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo2"),
        ("AcBoard", "acBoardTrapGlobalsAdditionalInfo3"),
        ("AcBoard", "acBoardTrapGlobalsDateAndTime"))
)
if mibBuilder.loadTexts:
    acOCSPServerStatusAlarm.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AcBoard",
    **{"audioCodes": audioCodes,
       "acRegistrations": acRegistrations,
       "acGeneric": acGeneric,
       "acProducts": acProducts,
       "acBoardMibs": acBoardMibs,
       "acBoard": acBoard,
       "boardConfiguration": boardConfiguration,
       "boardTDMBusSettings": boardTDMBusSettings,
       "pCMLawSelect": pCMLawSelect,
       "tDMBusClockSource": tDMBusClockSource,
       "tDMBusEnableFallBack": tDMBusEnableFallBack,
       "tDMBusLocalReference": tDMBusLocalReference,
       "idlePCMPattern": idlePCMPattern,
       "idleABCD": idleABCD,
       "tDMBusMasterSlaveSelection": tDMBusMasterSlaveSelection,
       "tDMBusNetRefSpeed": tDMBusNetRefSpeed,
       "tDMBusOutputStartingChannel": tDMBusOutputStartingChannel,
       "boardTDMBusOutputPort": boardTDMBusOutputPort,
       "tDMBusSpeed": tDMBusSpeed,
       "tDMBusType": tDMBusType,
       "acOverrideDefaultIdlePCMPattern": acOverrideDefaultIdlePCMPattern,
       "acOverrideDefaultIdleABCDPattern": acOverrideDefaultIdleABCDPattern,
       "networkSettings": networkSettings,
       "baseUDPPort": baseUDPPort,
       "defaultGatewayAddr": defaultGatewayAddr,
       "boardIPAddr": boardIPAddr,
       "boardSubNetAddr": boardSubNetAddr,
       "acSyslogServerIP": acSyslogServerIP,
       "acMGControlProtocolType": acMGControlProtocolType,
       "acSNMPManagerIP": acSNMPManagerIP,
       "acDisableWEBConfig": acDisableWEBConfig,
       "acEnableSyslog": acEnableSyslog,
       "acContrlProtocolTransportType": acContrlProtocolTransportType,
       "acCPControlDiffServ": acCPControlDiffServ,
       "snmpManagers": snmpManagers,
       "snmpManagersTable": snmpManagersTable,
       "snmpManagersEntry": snmpManagersEntry,
       "snmpManagerIndex": snmpManagerIndex,
       "snmpManagerIsUsed": snmpManagerIsUsed,
       "snmpManagerIp": snmpManagerIp,
       "snmpManagerTrapPort": snmpManagerTrapPort,
       "snmpManagerTrapSendingEnable": snmpManagerTrapSendingEnable,
       "acNTPSettings": acNTPSettings,
       "acNTPServerIPAddress": acNTPServerIPAddress,
       "acNTPUtcOffset": acNTPUtcOffset,
       "acNTPUpdateInterval": acNTPUpdateInterval,
       "acWEBAccess": acWEBAccess,
       "acWEBAccessTable": acWEBAccessTable,
       "acWEBAccessEntry": acWEBAccessEntry,
       "acWEBAccessRowStatus": acWEBAccessRowStatus,
       "acWEBAccessAction": acWEBAccessAction,
       "acWEBAccessActionResult": acWEBAccessActionResult,
       "acWEBAccessIndex": acWEBAccessIndex,
       "acWEBAccessUserName": acWEBAccessUserName,
       "acWEBAccessUserCode": acWEBAccessUserCode,
       "auxiliarySettings": auxiliarySettings,
       "enableDiagnostics": enableDiagnostics,
       "trunkSettings": trunkSettings,
       "trunkSettingsTable": trunkSettingsTable,
       "trunkSettingsEntry": trunkSettingsEntry,
       "trunkId": trunkId,
       "clockMaster": clockMaster,
       "framingMethod": framingMethod,
       "protocolType": protocolType,
       "terminationSide": terminationSide,
       "dchConfig": dchConfig,
       "lineCode": lineCode,
       "lineBuildOutLoss": lineBuildOutLoss,
       "lineBuildOutOverwrite": lineBuildOutOverwrite,
       "lineBuildOutXPM0": lineBuildOutXPM0,
       "lineBuildOutXPM1": lineBuildOutXPM1,
       "lineBuildOutXPM2": lineBuildOutXPM2,
       "traceLevel": traceLevel,
       "acV5InterfaceTrunkGroupId": acV5InterfaceTrunkGroupId,
       "acV5LinkIdOld": acV5LinkIdOld,
       "acPMStatus": acPMStatus,
       "acLedStatusColor": acLedStatusColor,
       "acLedStatusRate": acLedStatusRate,
       "acIsdnNfasInterfaceId": acIsdnNfasInterfaceId,
       "acTrunkCasTableIndex": acTrunkCasTableIndex,
       "acTrunkAdminState": acTrunkAdminState,
       "acPSTNIuaInterfaceId": acPSTNIuaInterfaceId,
       "acIsdnQ931LayerResponseBehavior": acIsdnQ931LayerResponseBehavior,
       "acIsdnIncomingCallsBehavior": acIsdnIncomingCallsBehavior,
       "acIsdnOutgoingCallsBehavior": acIsdnOutgoingCallsBehavior,
       "acIsdnGeneralCCBehavior": acIsdnGeneralCCBehavior,
       "acIsdnNfasGroupNumber": acIsdnNfasGroupNumber,
       "mGCPSettings": mGCPSettings,
       "callAgentIP": callAgentIP,
       "callAgentPort": callAgentPort,
       "callAgentDomainName": callAgentDomainName,
       "redundantAgentIP": redundantAgentIP,
       "redundantAgentPort": redundantAgentPort,
       "redundantCallAgentDomainName": redundantCallAgentDomainName,
       "dePopulatedChannelsNumber": dePopulatedChannelsNumber,
       "gateWayName": gateWayName,
       "endPointName": endPointName,
       "mGCPCommunicationLayerTimeout": mGCPCommunicationLayerTimeout,
       "acDefaultChannelSettings": acDefaultChannelSettings,
       "acChDefaultDJBufMinDelay": acChDefaultDJBufMinDelay,
       "acChDefaultDJBufOptFactor": acChDefaultDJBufOptFactor,
       "acChDefaultCallerIDType": acChDefaultCallerIDType,
       "acChDefaultFaxModemBypassM": acChDefaultFaxModemBypassM,
       "acChDefaultFaxModemRelayVolume": acChDefaultFaxModemRelayVolume,
       "acChDefaultFaxRelayECMEnable": acChDefaultFaxRelayECMEnable,
       "acChDefaultFaxRelayMaxRate": acChDefaultFaxRelayMaxRate,
       "acChDefaultFaxTransportMode": acChDefaultFaxTransportMode,
       "acChDefaultModemRelayRedundancyDepth": acChDefaultModemRelayRedundancyDepth,
       "acChDefaultModemRelayMaxRate": acChDefaultModemRelayMaxRate,
       "acChDefaultUseT38orFRF11": acChDefaultUseT38orFRF11,
       "acChDefaultV21ModemTransportType": acChDefaultV21ModemTransportType,
       "acChDefaultV22ModemTransportType": acChDefaultV22ModemTransportType,
       "acChDefaultV23ModemTransportType": acChDefaultV23ModemTransportType,
       "acChDefaultV32ModemTransportType": acChDefaultV32ModemTransportType,
       "acChDefaultV34ModemTransportType": acChDefaultV34ModemTransportType,
       "acChDefaultFaxModemBypassCoderType": acChDefaultFaxModemBypassCoderType,
       "acChDefaultFaxRelayRedundancyDepth": acChDefaultFaxRelayRedundancyDepth,
       "acChDefaultT38ProtectionMode": acChDefaultT38ProtectionMode,
       "acChDefaultDTMFVolume": acChDefaultDTMFVolume,
       "acChDefaultDTMFTransportType": acChDefaultDTMFTransportType,
       "acChDefaultMFTransportType": acChDefaultMFTransportType,
       "acChDefaultInputGain": acChDefaultInputGain,
       "acChDefaultRTPRedundancyDepth": acChDefaultRTPRedundancyDepth,
       "acChDefaultTestMode": acChDefaultTestMode,
       "acChDefaultVoiceVolume": acChDefaultVoiceVolume,
       "acChDefaultM": acChDefaultM,
       "acChDefaultFlashHookPeriod": acChDefaultFlashHookPeriod,
       "acChDefaultDTMFDetectionPoint": acChDefaultDTMFDetectionPoint,
       "acChDefaultRtpIpTos": acChDefaultRtpIpTos,
       "acChDefaultRtpIpPrecedence": acChDefaultRtpIpPrecedence,
       "acChDefaultEchoCancler": acChDefaultEchoCancler,
       "acChDefaultSilenceSuppression": acChDefaultSilenceSuppression,
       "acChDefaultEchoCanclerHybridLoss": acChDefaultEchoCanclerHybridLoss,
       "acChDefaultPacketizationPeriod": acChDefaultPacketizationPeriod,
       "aTMSettings": aTMSettings,
       "vPMask": vPMask,
       "vCMask": vCMask,
       "externalClk": externalClk,
       "aTMLoopBack": aTMLoopBack,
       "utopiaSlave": utopiaSlave,
       "multyPhy": multyPhy,
       "slavePhyNum": slavePhyNum,
       "utopiaBus16": utopiaBus16,
       "aTMPHYType": aTMPHYType,
       "disablePayloadScrambling": disablePayloadScrambling,
       "pHYClkSource": pHYClkSource,
       "sendIdleCASUponLinkFail": sendIdleCASUponLinkFail,
       "masterSlaveMode": masterSlaveMode,
       "vccProfile": vccProfile,
       "tPNCPVPI": tPNCPVPI,
       "tPNCPVCI": tPNCPVCI,
       "sAALLink0VPI": sAALLink0VPI,
       "sAALLink0VCI": sAALLink0VCI,
       "sAALLink1VPI": sAALLink1VPI,
       "sAALLink1VCI": sAALLink1VCI,
       "acSS7Settings": acSS7Settings,
       "acSS7SettingsTable": acSS7SettingsTable,
       "acSS7SettingsEntry": acSS7SettingsEntry,
       "acSS7LinkId": acSS7LinkId,
       "acSS7traceLevel": acSS7traceLevel,
       "acConfigFiles": acConfigFiles,
       "acFxsCoefficients": acFxsCoefficients,
       "acFxoCoefficients": acFxoCoefficients,
       "acCptFile": acCptFile,
       "acVpFile": acVpFile,
       "acCasTables": acCasTables,
       "acCasTablesTable": acCasTablesTable,
       "acCasTablesEntry": acCasTablesEntry,
       "acCasTableIndex": acCasTableIndex,
       "acCasTabeName": acCasTabeName,
       "acFxs": acFxs,
       "acPolarityReversalType": acPolarityReversalType,
       "megacoSettings": megacoSettings,
       "megacoCurrentProfile": megacoCurrentProfile,
       "megacoGatewayName": megacoGatewayName,
       "megacoEndpointName": megacoEndpointName,
       "megacoTrunkName": megacoTrunkName,
       "megacoActiveCallAgentIp": megacoActiveCallAgentIp,
       "megacoActiveCallAgentPort": megacoActiveCallAgentPort,
       "megacoCallAgents": megacoCallAgents,
       "megacoCallAgentsTable": megacoCallAgentsTable,
       "megacoCallAgentsEntry": megacoCallAgentsEntry,
       "megacoCallAgentId": megacoCallAgentId,
       "megacoCallAgentIp": megacoCallAgentIp,
       "megacoCallAgentPort": megacoCallAgentPort,
       "megacoCallAgentIsUsed": megacoCallAgentIsUsed,
       "megacoCheckLegalityOfMGC": megacoCheckLegalityOfMGC,
       "acPSTNParameters": acPSTNParameters,
       "acQ931RELAYMODE": acQ931RELAYMODE,
       "acIsdnDuplicateQ931BuffMode": acIsdnDuplicateQ931BuffMode,
       "acPSTNCASTableNum": acPSTNCASTableNum,
       "aMsConfiguration": aMsConfiguration,
       "amsNumOfConferencePorts": amsNumOfConferencePorts,
       "amsNumOfTestTrunkPorts": amsNumOfTestTrunkPorts,
       "amsNumOfLawfulInterceptPorts": amsNumOfLawfulInterceptPorts,
       "amsNumOfAnnouncementPorts": amsNumOfAnnouncementPorts,
       "amsApsIpAddress": amsApsIpAddress,
       "amsApsPort": amsApsPort,
       "amsPrimaryLanguage": amsPrimaryLanguage,
       "amsSecondaryLanguage": amsSecondaryLanguage,
       "amsProfile": amsProfile,
       "amsAASPackagesProfile": amsAASPackagesProfile,
       "acFeatureKey": acFeatureKey,
       "acFeatureKeyString": acFeatureKeyString,
       "acActiveFeaturesList": acActiveFeaturesList,
       "supplementary": supplementary,
       "supplementaryField": supplementaryField,
       "boardInformation": boardInformation,
       "boardType": boardType,
       "boardName": boardName,
       "serialNum": serialNum,
       "dSPCount": dSPCount,
       "channelsCount": channelsCount,
       "cPUSpeed": cPUSpeed,
       "softwareVersion": softwareVersion,
       "trunkPackSoftwareDate": trunkPackSoftwareDate,
       "slotNumber": slotNumber,
       "iniFileVersion": iniFileVersion,
       "acDspType": acDspType,
       "acFlashVersion": acFlashVersion,
       "acBoardFxsOrFxo": acBoardFxsOrFxo,
       "acTrunkslCount": acTrunkslCount,
       "acDspVersionTemplate": acDspVersionTemplate,
       "acFirstPortDuplexMode": acFirstPortDuplexMode,
       "acFirstPortSpeed": acFirstPortSpeed,
       "acMeanFreeChannels": acMeanFreeChannels,
       "acMaxFreeChannels": acMaxFreeChannels,
       "acSysUpTime": acSysUpTime,
       "acPhysicalModCount": acPhysicalModCount,
       "acBoardTemperature": acBoardTemperature,
       "channelConfiguration": channelConfiguration,
       "voiceSettings": voiceSettings,
       "voiceSettingsTable": voiceSettingsTable,
       "voiceSettingsEntry": voiceSettingsEntry,
       "cID": cID,
       "coder": coder,
       "eCE": eCE,
       "sCE": sCE,
       "pFE": pFE,
       "hPFE": hPFE,
       "testMode": testMode,
       "voiceVolume": voiceVolume,
       "inputGain": inputGain,
       "m": m,
       "rTPRedundancyDepth": rTPRedundancyDepth,
       "eCLength": eCLength,
       "eCHybridLoss": eCHybridLoss,
       "faxModemSettings": faxModemSettings,
       "faxModemSettingsTable": faxModemSettingsTable,
       "faxModemSettingsEntry": faxModemSettingsEntry,
       "fAXTransportType": fAXTransportType,
       "acCallerIDType": acCallerIDType,
       "v21ModemTransportType": v21ModemTransportType,
       "v22ModemTransportType": v22ModemTransportType,
       "v23ModemTransportType": v23ModemTransportType,
       "v32ModemTransportType": v32ModemTransportType,
       "v34ModemTransportType": v34ModemTransportType,
       "faxRelayMaxRate": faxRelayMaxRate,
       "modemRelayMaxRate": modemRelayMaxRate,
       "faxRelayECMEnable": faxRelayECMEnable,
       "t38FaxRelayProtectionMode": t38FaxRelayProtectionMode,
       "faxRelayRedundancyDepth": faxRelayRedundancyDepth,
       "enhancedFaxRelayRedundancyDepth": enhancedFaxRelayRedundancyDepth,
       "modemRelayRedundancyDepth": modemRelayRedundancyDepth,
       "faxModemRelayVolume": faxModemRelayVolume,
       "faxModemBypassCoderType": faxModemBypassCoderType,
       "faxModemBypassM": faxModemBypassM,
       "useT38orFRF11": useT38orFRF11,
       "dJBSettings": dJBSettings,
       "dJBSettingsTable": dJBSettingsTable,
       "dJBSettingsEntry": dJBSettingsEntry,
       "dJBufMinDelay": dJBufMinDelay,
       "dJBufOptFactor": dJBufOptFactor,
       "channelTDMBusSettings": channelTDMBusSettings,
       "channelTDMBusSettingsTable": channelTDMBusSettingsTable,
       "channelTDMBusSettingsEntry": channelTDMBusSettingsEntry,
       "tDMBusInputPort": tDMBusInputPort,
       "tDMBusInputChannel": tDMBusInputChannel,
       "tDMBusOutputDisable": tDMBusOutputDisable,
       "tDMBusOutputPort": tDMBusOutputPort,
       "tDMBusOutputChannel": tDMBusOutputChannel,
       "transportSettings": transportSettings,
       "transportSettingsTable": transportSettingsTable,
       "transportSettingsEntry": transportSettingsEntry,
       "useNIorPCI": useNIorPCI,
       "disableSoftIPLoopback": disableSoftIPLoopback,
       "uniDirectionalRTP": uniDirectionalRTP,
       "rTPRTCPSettings": rTPRTCPSettings,
       "rTPRTCPSettingsTable": rTPRTCPSettingsTable,
       "rTPRTCPSettingsEntry": rTPRTCPSettingsEntry,
       "cNAME": cNAME,
       "iPPrecedence": iPPrecedence,
       "iPTOS": iPTOS,
       "localRTPPort": localRTPPort,
       "remoteRTPAddr": remoteRTPAddr,
       "remoteRTPPort": remoteRTPPort,
       "remoteT38Addr": remoteT38Addr,
       "remoteT38Port": remoteT38Port,
       "rTCPMeanTxInterval": rTCPMeanTxInterval,
       "rxRTPPayloadType": rxRTPPayloadType,
       "txRTPPayloadType": txRTPPayloadType,
       "channelStatus": channelStatus,
       "channelStatusTable": channelStatusTable,
       "channelStatusEntry": channelStatusEntry,
       "rTPActive": rTPActive,
       "bypassNIC": bypassNIC,
       "pendingIdle": pendingIdle,
       "txSilencePeriod": txSilencePeriod,
       "rxSilencePeriod": rxSilencePeriod,
       "txFaxMode": txFaxMode,
       "rxFaxMode": rxFaxMode,
       "txDTMFPeriod": txDTMFPeriod,
       "rxDTMFPeriod": rxDTMFPeriod,
       "packetsToDSPCnt": packetsToDSPCnt,
       "jitterBufErrorCnt": jitterBufErrorCnt,
       "jitterBufForcedPacketLost": jitterBufForcedPacketLost,
       "jitterBufForcedPacketAddition": jitterBufForcedPacketAddition,
       "jitterBufUnderRunCnt": jitterBufUnderRunCnt,
       "jitterBufOverRunCnt": jitterBufOverRunCnt,
       "jitterBufAccumDelay": jitterBufAccumDelay,
       "fXSorFXO": fXSorFXO,
       "channelHookState": channelHookState,
       "notifications": notifications,
       "reset": reset,
       "remoteReset": remoteReset,
       "acSetDefaults": acSetDefaults,
       "acgwAdminState": acgwAdminState,
       "acgwAdminStateLockControl": acgwAdminStateLockControl,
       "acSaveConfigToSystem": acSaveConfigToSystem,
       "acOperationalState": acOperationalState,
       "remoteResetControl": remoteResetControl,
       "acTrap": acTrap,
       "acBoardTrapGlobals": acBoardTrapGlobals,
       "acBoardTrapGlobalsName": acBoardTrapGlobalsName,
       "acBoardTrapGlobalsTextualDescription": acBoardTrapGlobalsTextualDescription,
       "acBoardTrapGlobalsSource": acBoardTrapGlobalsSource,
       "acBoardTrapGlobalsSeverity": acBoardTrapGlobalsSeverity,
       "acBoardTrapGlobalsUniqID": acBoardTrapGlobalsUniqID,
       "acBoardTrapGlobalsType": acBoardTrapGlobalsType,
       "acBoardTrapGlobalsProbableCause": acBoardTrapGlobalsProbableCause,
       "acBoardTrapGlobalsAdditionalInfo1": acBoardTrapGlobalsAdditionalInfo1,
       "acBoardTrapGlobalsAdditionalInfo2": acBoardTrapGlobalsAdditionalInfo2,
       "acBoardTrapGlobalsAdditionalInfo3": acBoardTrapGlobalsAdditionalInfo3,
       "acBoardTrapGlobalsDateAndTime": acBoardTrapGlobalsDateAndTime,
       "acBoardTrapDefinitions": acBoardTrapDefinitions,
       "acBoardFatalError": acBoardFatalError,
       "acBoardConfigurationError": acBoardConfigurationError,
       "acBoardTemperatureAlarm": acBoardTemperatureAlarm,
       "acBoardEvBoardStarted": acBoardEvBoardStarted,
       "acBoardEvResettingBoard": acBoardEvResettingBoard,
       "acFeatureKeyError": acFeatureKeyError,
       "acgwAdminStateChange": acgwAdminStateChange,
       "acBoardCallResourcesAlarm": acBoardCallResourcesAlarm,
       "acBoardControllerFailureAlarm": acBoardControllerFailureAlarm,
       "acBoardEthernetLinkAlarm": acBoardEthernetLinkAlarm,
       "acBoardOverloadAlarm": acBoardOverloadAlarm,
       "acActiveAlarmTableOverflow": acActiveAlarmTableOverflow,
       "acAtmPortAlarm": acAtmPortAlarm,
       "acAudioProvisioningAlarm": acAudioProvisioningAlarm,
       "acOperationalStateChange": acOperationalStateChange,
       "acKeepAlive": acKeepAlive,
       "acNATTraversalAlarm": acNATTraversalAlarm,
       "acEnhancedBITStatus": acEnhancedBITStatus,
       "acSS7LinkStateChangeAlarm": acSS7LinkStateChangeAlarm,
       "acSS7LinkInhibitStateChangeAlarm": acSS7LinkInhibitStateChangeAlarm,
       "acSS7LinkBlockStateChangeAlarm": acSS7LinkBlockStateChangeAlarm,
       "acSS7LinkCongestionStateChangeAlarm": acSS7LinkCongestionStateChangeAlarm,
       "acSS7LinkSetStateChangeAlarm": acSS7LinkSetStateChangeAlarm,
       "acSS7RouteSetStateChangeAlarm": acSS7RouteSetStateChangeAlarm,
       "acSS7SNSetStateChangeAlarm": acSS7SNSetStateChangeAlarm,
       "acSS7RedundancyAlarm": acSS7RedundancyAlarm,
       "acPerformanceMonitoringThresholdCrossing": acPerformanceMonitoringThresholdCrossing,
       "acHTTPDownloadResult": acHTTPDownloadResult,
       "acFanTrayAlarm": acFanTrayAlarm,
       "acPowerSupplyAlarm": acPowerSupplyAlarm,
       "acPEMAlarm": acPEMAlarm,
       "acSAMissingAlarm": acSAMissingAlarm,
       "acHASystemFaultAlarm": acHASystemFaultAlarm,
       "acHASystemConfigMismatchAlarm": acHASystemConfigMismatchAlarm,
       "acHASystemSwitchOverAlarm": acHASystemSwitchOverAlarm,
       "acUserInputAlarm": acUserInputAlarm,
       "acDChannelStatus": acDChannelStatus,
       "acSonetSectionLOFAlarm": acSonetSectionLOFAlarm,
       "acSonetSectionLOSAlarm": acSonetSectionLOSAlarm,
       "acSonetLineAISAlarm": acSonetLineAISAlarm,
       "acSonetLineRDIAlarm": acSonetLineRDIAlarm,
       "acSonetIfHwFailureAlarm": acSonetIfHwFailureAlarm,
       "acHwFailureAlarm": acHwFailureAlarm,
       "acH248LostConnectionWithCA": acH248LostConnectionWithCA,
       "acDialPlanFileReplaced": acDialPlanFileReplaced,
       "acAnalogPortSPIOutOfService": acAnalogPortSPIOutOfService,
       "acAnalogPortHighTemperature": acAnalogPortHighTemperature,
       "acHitlessUpdateStatus": acHitlessUpdateStatus,
       "acTrunksAlarmNearEndLOS": acTrunksAlarmNearEndLOS,
       "acTrunksAlarmNearEndLOF": acTrunksAlarmNearEndLOF,
       "acTrunksAlarmRcvAIS": acTrunksAlarmRcvAIS,
       "acTrunksAlarmFarEndLOF": acTrunksAlarmFarEndLOF,
       "acIPv6ErrorAlarm": acIPv6ErrorAlarm,
       "acAMSProcedureResult": acAMSProcedureResult,
       "acWeakRedundancy": acWeakRedundancy,
       "acTMInconsistentRemoteAndLocalPLLStatus": acTMInconsistentRemoteAndLocalPLLStatus,
       "acTMReferenceStatus": acTMReferenceStatus,
       "acTMReferenceChange": acTMReferenceChange,
       "acGWSASEmergencyModeAlarm": acGWSASEmergencyModeAlarm,
       "acV52InterfaceAlarm": acV52InterfaceAlarm,
       "acSonetPathSTSLOPAlarm": acSonetPathSTSLOPAlarm,
       "acSonetPathSTSAISAlarm": acSonetPathSTSAISAlarm,
       "acSonetPathSTSRDIAlarm": acSonetPathSTSRDIAlarm,
       "acSonetPathUnequippedAlarm": acSonetPathUnequippedAlarm,
       "acSonetPathSignalLabelMismatchAlarm": acSonetPathSignalLabelMismatchAlarm,
       "acDS3RAIAlarm": acDS3RAIAlarm,
       "acDS3AISAlarm": acDS3AISAlarm,
       "acDS3LOFAlarm": acDS3LOFAlarm,
       "acDS3LOSAlarm": acDS3LOSAlarm,
       "acSWUpgradeAlarm": acSWUpgradeAlarm,
       "acNTPServerStatusAlarm": acNTPServerStatusAlarm,
       "acThreeWayConferenceOutOfResources": acThreeWayConferenceOutOfResources,
       "acSS7AliasPcStateChangeAlarm": acSS7AliasPcStateChangeAlarm,
       "acSS7UalGroupStateChangeAlarm": acSS7UalGroupStateChangeAlarm,
       "acLDAPLostConnection": acLDAPLostConnection,
       "acAnalogPortGroundFaultOutOfService": acAnalogPortGroundFaultOutOfService,
       "acSSHConnectionStatus": acSSHConnectionStatus,
       "acOCSPServerStatusAlarm": acOCSPServerStatusAlarm}
)
