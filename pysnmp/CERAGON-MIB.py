# SNMP MIB module (CERAGON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CERAGON-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:54:19 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

_Ceragon_ObjectIdentity = ObjectIdentity
ceragon = _Ceragon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281)
)
_GnOID_ObjectIdentity = ObjectIdentity
gnOID = _GnOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 1)
)
_GnFirstOID_ObjectIdentity = ObjectIdentity
gnFirstOID = _GnFirstOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 1, 1)
)
_GnSystem_ObjectIdentity = ObjectIdentity
gnSystem = _GnSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 2)
)
_GnGeneral_ObjectIdentity = ObjectIdentity
gnGeneral = _GnGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1)
)


class _GnGenStandardOrg_Type(Integer32):
    """Custom type gnGenStandardOrg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("australia", 7),
          ("cmds", 6),
          ("etsi", 2),
          ("fcc", 3),
          ("japan", 4),
          ("lmds", 5),
          ("other", 8))
    )


_GnGenStandardOrg_Type.__name__ = "Integer32"
_GnGenStandardOrg_Object = MibScalar
gnGenStandardOrg = _GnGenStandardOrg_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 1),
    _GnGenStandardOrg_Type()
)
gnGenStandardOrg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnGenStandardOrg.setStatus("mandatory")


class _GnGenTxFreqRange_Type(Integer32):
    """Custom type gnGenTxFreqRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
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
        *(("from37000to37350", 2),
          ("from37058to37618", 10),
          ("from37350to37700", 3),
          ("from37618to38178", 11),
          ("from37700to38050", 4),
          ("from38050to38400", 5),
          ("from38318to38878", 12),
          ("from38600to38950", 6),
          ("from38878to39438", 13),
          ("from38950to39300", 7),
          ("from39300to39650", 8),
          ("from39650to40000", 9),
          ("notUsed", 14))
    )


_GnGenTxFreqRange_Type.__name__ = "Integer32"
_GnGenTxFreqRange_Object = MibScalar
gnGenTxFreqRange = _GnGenTxFreqRange_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 2),
    _GnGenTxFreqRange_Type()
)
gnGenTxFreqRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnGenTxFreqRange.setStatus("mandatory")


class _GnGenRemoteConnection_Type(Integer32):
    """Custom type gnGenRemoteConnection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("connected", 2),
          ("disconnected", 3))
    )


_GnGenRemoteConnection_Type.__name__ = "Integer32"
_GnGenRemoteConnection_Object = MibScalar
gnGenRemoteConnection = _GnGenRemoteConnection_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 3),
    _GnGenRemoteConnection_Type()
)
gnGenRemoteConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnGenRemoteConnection.setStatus("mandatory")


class _GnGenRemoteDistance_Type(Integer32):
    """Custom type gnGenRemoteDistance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 30000),
    )


_GnGenRemoteDistance_Type.__name__ = "Integer32"
_GnGenRemoteDistance_Object = MibScalar
gnGenRemoteDistance = _GnGenRemoteDistance_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 4),
    _GnGenRemoteDistance_Type()
)
gnGenRemoteDistance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnGenRemoteDistance.setStatus("mandatory")
_GnGenInterLenLocalRemote_Type = Integer32
_GnGenInterLenLocalRemote_Object = MibScalar
gnGenInterLenLocalRemote = _GnGenInterLenLocalRemote_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 5),
    _GnGenInterLenLocalRemote_Type()
)
gnGenInterLenLocalRemote.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnGenInterLenLocalRemote.setStatus("mandatory")


class _GnGenTxFreqLocalRemote_Type(Integer32):
    """Custom type gnGenTxFreqLocalRemote based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_GnGenTxFreqLocalRemote_Type.__name__ = "Integer32"
_GnGenTxFreqLocalRemote_Object = MibScalar
gnGenTxFreqLocalRemote = _GnGenTxFreqLocalRemote_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 6),
    _GnGenTxFreqLocalRemote_Type()
)
gnGenTxFreqLocalRemote.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnGenTxFreqLocalRemote.setStatus("mandatory")


class _GnGenRealTimeandDate_Type(OctetString):
    """Custom type gnGenRealTimeandDate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_GnGenRealTimeandDate_Type.__name__ = "OctetString"
_GnGenRealTimeandDate_Object = MibScalar
gnGenRealTimeandDate = _GnGenRealTimeandDate_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 7),
    _GnGenRealTimeandDate_Type()
)
gnGenRealTimeandDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnGenRealTimeandDate.setStatus("mandatory")
_GnGenCfgDeviceTable_Object = MibTable
gnGenCfgDeviceTable = _GnGenCfgDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 8)
)
if mibBuilder.loadTexts:
    gnGenCfgDeviceTable.setStatus("mandatory")
_GnGenCfgDeviceEntry_Object = MibTableRow
gnGenCfgDeviceEntry = _GnGenCfgDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 8, 1)
)
gnGenCfgDeviceEntry.setIndexNames(
    (0, "CERAGON-MIB", "gnGenCfgDeviceId"),
)
if mibBuilder.loadTexts:
    gnGenCfgDeviceEntry.setStatus("mandatory")


class _GnGenCfgDeviceId_Type(Integer32):
    """Custom type gnGenCfgDeviceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("remote", 2))
    )


_GnGenCfgDeviceId_Type.__name__ = "Integer32"
_GnGenCfgDeviceId_Object = MibTableColumn
gnGenCfgDeviceId = _GnGenCfgDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 8, 1, 1),
    _GnGenCfgDeviceId_Type()
)
gnGenCfgDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnGenCfgDeviceId.setStatus("mandatory")


class _GnGenCfgDeviceResetPerfMon_Type(Integer32):
    """Custom type gnGenCfgDeviceResetPerfMon based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("clearFastEthernetStatistics", 4),
          ("noAction", 3),
          ("reset", 2))
    )


_GnGenCfgDeviceResetPerfMon_Type.__name__ = "Integer32"
_GnGenCfgDeviceResetPerfMon_Object = MibTableColumn
gnGenCfgDeviceResetPerfMon = _GnGenCfgDeviceResetPerfMon_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 8, 1, 2),
    _GnGenCfgDeviceResetPerfMon_Type()
)
gnGenCfgDeviceResetPerfMon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnGenCfgDeviceResetPerfMon.setStatus("mandatory")


class _GnGenCfgDeviceOperation_Type(Integer32):
    """Custom type gnGenCfgDeviceOperation based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("clearMainManagerSoftware", 5),
          ("noOperation", 2),
          ("resetMUX", 7),
          ("resetODU", 6),
          ("resetSwOdu", 8),
          ("setDefaultConf", 4),
          ("softwareReset", 3))
    )


_GnGenCfgDeviceOperation_Type.__name__ = "Integer32"
_GnGenCfgDeviceOperation_Object = MibTableColumn
gnGenCfgDeviceOperation = _GnGenCfgDeviceOperation_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 8, 1, 3),
    _GnGenCfgDeviceOperation_Type()
)
gnGenCfgDeviceOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnGenCfgDeviceOperation.setStatus("mandatory")


class _GnGenCfgActivateLoopback_Type(Integer32):
    """Custom type gnGenCfgActivateLoopback based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              5,
              6,
              10)
        )
    )
    namedValues = NamedValues(
        *(("localODUloopback", 10),
          ("loopbackMDM", 5),
          ("loopbackOuterSPI", 6),
          ("loopbackSPI", 3),
          ("noOperation", 2))
    )


_GnGenCfgActivateLoopback_Type.__name__ = "Integer32"
_GnGenCfgActivateLoopback_Object = MibTableColumn
gnGenCfgActivateLoopback = _GnGenCfgActivateLoopback_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 8, 1, 4),
    _GnGenCfgActivateLoopback_Type()
)
gnGenCfgActivateLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnGenCfgActivateLoopback.setStatus("mandatory")


class _GnGenCfgF1DataChanConnector_Type(Integer32):
    """Custom type gnGenCfgF1DataChanConnector based on Integer32"""
    defaultValue = 2

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
        *(("noInterface", 1),
          ("rj45CoDirect", 5),
          ("rj45bridge", 6),
          ("rs232db25", 2),
          ("rs232db9", 8),
          ("rs422db25", 4),
          ("v35", 3),
          ("x21db15", 7))
    )


_GnGenCfgF1DataChanConnector_Type.__name__ = "Integer32"
_GnGenCfgF1DataChanConnector_Object = MibTableColumn
gnGenCfgF1DataChanConnector = _GnGenCfgF1DataChanConnector_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 8, 1, 5),
    _GnGenCfgF1DataChanConnector_Type()
)
gnGenCfgF1DataChanConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnGenCfgF1DataChanConnector.setStatus("mandatory")


class _GnGenCfgWaySideConnector_Type(Integer32):
    """Custom type gnGenCfgWaySideConnector based on Integer32"""
    defaultValue = 1

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
        *(("clockUnit1dot5M", 11),
          ("clockUnit2M", 10),
          ("connectorE1", 5),
          ("connectorT1", 8),
          ("lineSTM4", 9),
          ("noInterface", 1),
          ("rj45bridge", 6),
          ("rs232db25", 2),
          ("rs422db25", 4),
          ("v35", 3),
          ("x21db15", 7))
    )


_GnGenCfgWaySideConnector_Type.__name__ = "Integer32"
_GnGenCfgWaySideConnector_Object = MibTableColumn
gnGenCfgWaySideConnector = _GnGenCfgWaySideConnector_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 8, 1, 6),
    _GnGenCfgWaySideConnector_Type()
)
gnGenCfgWaySideConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnGenCfgWaySideConnector.setStatus("mandatory")


class _GnGenCfgActivateChanLoopback_Type(Integer32):
    """Custom type gnGenCfgActivateChanLoopback based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("loopbackDataChan", 3),
          ("loopbackWaySide", 4),
          ("noOperation", 2))
    )


_GnGenCfgActivateChanLoopback_Type.__name__ = "Integer32"
_GnGenCfgActivateChanLoopback_Object = MibTableColumn
gnGenCfgActivateChanLoopback = _GnGenCfgActivateChanLoopback_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 8, 1, 7),
    _GnGenCfgActivateChanLoopback_Type()
)
gnGenCfgActivateChanLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnGenCfgActivateChanLoopback.setStatus("mandatory")
_GnGenCfgInterLenLocalOnly_Type = Integer32
_GnGenCfgInterLenLocalOnly_Object = MibTableColumn
gnGenCfgInterLenLocalOnly = _GnGenCfgInterLenLocalOnly_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 8, 1, 8),
    _GnGenCfgInterLenLocalOnly_Type()
)
gnGenCfgInterLenLocalOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnGenCfgInterLenLocalOnly.setStatus("mandatory")
_GnGenCfgSlipIp_Type = IpAddress
_GnGenCfgSlipIp_Object = MibTableColumn
gnGenCfgSlipIp = _GnGenCfgSlipIp_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 8, 1, 9),
    _GnGenCfgSlipIp_Type()
)
gnGenCfgSlipIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnGenCfgSlipIp.setStatus("mandatory")
_GnGenCfgSlipModemConnection_Type = DisplayString
_GnGenCfgSlipModemConnection_Object = MibTableColumn
gnGenCfgSlipModemConnection = _GnGenCfgSlipModemConnection_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 8, 1, 10),
    _GnGenCfgSlipModemConnection_Type()
)
gnGenCfgSlipModemConnection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnGenCfgSlipModemConnection.setStatus("mandatory")


class _GnGenCfgSlipSpeed_Type(Integer32):
    """Custom type gnGenCfgSlipSpeed based on Integer32"""
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
        *(("baud115200", 5),
          ("baud19200", 2),
          ("baud38400", 3),
          ("baud57600", 4),
          ("baud9600", 1))
    )


_GnGenCfgSlipSpeed_Type.__name__ = "Integer32"
_GnGenCfgSlipSpeed_Object = MibTableColumn
gnGenCfgSlipSpeed = _GnGenCfgSlipSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 8, 1, 11),
    _GnGenCfgSlipSpeed_Type()
)
gnGenCfgSlipSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnGenCfgSlipSpeed.setStatus("mandatory")


class _GnGenCfgAlarmSeverity_Type(OctetString):
    """Custom type gnGenCfgAlarmSeverity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(15, 15),
    )


_GnGenCfgAlarmSeverity_Type.__name__ = "OctetString"
_GnGenCfgAlarmSeverity_Object = MibTableColumn
gnGenCfgAlarmSeverity = _GnGenCfgAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 8, 1, 12),
    _GnGenCfgAlarmSeverity_Type()
)
gnGenCfgAlarmSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnGenCfgAlarmSeverity.setStatus("mandatory")


class _GnGenCfgODUSerialNumber_Type(DisplayString):
    """Custom type gnGenCfgODUSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_GnGenCfgODUSerialNumber_Type.__name__ = "DisplayString"
_GnGenCfgODUSerialNumber_Object = MibTableColumn
gnGenCfgODUSerialNumber = _GnGenCfgODUSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 8, 1, 13),
    _GnGenCfgODUSerialNumber_Type()
)
gnGenCfgODUSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnGenCfgODUSerialNumber.setStatus("mandatory")


class _GnGenCfgIDUSerialNumber_Type(DisplayString):
    """Custom type gnGenCfgIDUSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_GnGenCfgIDUSerialNumber_Type.__name__ = "DisplayString"
_GnGenCfgIDUSerialNumber_Object = MibTableColumn
gnGenCfgIDUSerialNumber = _GnGenCfgIDUSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 8, 1, 14),
    _GnGenCfgIDUSerialNumber_Type()
)
gnGenCfgIDUSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnGenCfgIDUSerialNumber.setStatus("mandatory")
_GnGenCfgAlarmText_Type = DisplayString
_GnGenCfgAlarmText_Object = MibTableColumn
gnGenCfgAlarmText = _GnGenCfgAlarmText_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 8, 1, 15),
    _GnGenCfgAlarmText_Type()
)
gnGenCfgAlarmText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnGenCfgAlarmText.setStatus("mandatory")


class _GnGenCfgTrapSeverity_Type(Integer32):
    """Custom type gnGenCfgTrapSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3,
              7,
              15,
              31)
        )
    )
    namedValues = NamedValues(
        *(("clear", 0),
          ("critical", 31),
          ("event", 1),
          ("major", 15),
          ("minor", 7),
          ("warning", 3))
    )


_GnGenCfgTrapSeverity_Type.__name__ = "Integer32"
_GnGenCfgTrapSeverity_Object = MibTableColumn
gnGenCfgTrapSeverity = _GnGenCfgTrapSeverity_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 8, 1, 16),
    _GnGenCfgTrapSeverity_Type()
)
gnGenCfgTrapSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnGenCfgTrapSeverity.setStatus("mandatory")


class _GnGenCfgProductType_Type(Integer32):
    """Custom type gnGenCfgProductType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("accessMux", 2),
          ("accessMuxStm0", 5),
          ("adm", 7),
          ("narrowBandPdhRepeater", 4),
          ("plex6200", 6),
          ("sdhRegenerator", 3))
    )


_GnGenCfgProductType_Type.__name__ = "Integer32"
_GnGenCfgProductType_Object = MibTableColumn
gnGenCfgProductType = _GnGenCfgProductType_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 8, 1, 17),
    _GnGenCfgProductType_Type()
)
gnGenCfgProductType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnGenCfgProductType.setStatus("mandatory")


class _GnGenCfgLeftMediumConnector_Type(Integer32):
    """Custom type gnGenCfgLeftMediumConnector based on Integer32"""
    defaultValue = 2

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
        *(("eightE1", 12),
          ("eightT1", 13),
          ("electricalSTM1", 8),
          ("electricalSTM1Trib", 16),
          ("fiberSTM1", 7),
          ("fiberSTM1Trib", 15),
          ("hitLess", 14),
          ("hitLessWithBridge", 17),
          ("noInterface", 1),
          ("oneDS3", 3),
          ("oneE3", 5),
          ("oneFastEthernet", 6),
          ("opticalFastEthernet", 18),
          ("stpSTM1", 10),
          ("twoDS3", 2),
          ("twoE3", 4),
          ("twoSTM1", 11),
          ("utpSTM1", 9))
    )


_GnGenCfgLeftMediumConnector_Type.__name__ = "Integer32"
_GnGenCfgLeftMediumConnector_Object = MibTableColumn
gnGenCfgLeftMediumConnector = _GnGenCfgLeftMediumConnector_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 8, 1, 18),
    _GnGenCfgLeftMediumConnector_Type()
)
gnGenCfgLeftMediumConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnGenCfgLeftMediumConnector.setStatus("mandatory")


class _GnGenCfgMiddleMediumConnector_Type(Integer32):
    """Custom type gnGenCfgMiddleMediumConnector based on Integer32"""
    defaultValue = 3

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
        *(("eightE1", 12),
          ("eightT1", 13),
          ("electricalSTM1", 8),
          ("electricalSTM1Trib", 16),
          ("fiberSTM1", 7),
          ("fiberSTM1Trib", 15),
          ("hitLess", 14),
          ("hitLessWithBridge", 17),
          ("noInterface", 1),
          ("oneDS3", 3),
          ("oneE3", 5),
          ("oneFastEthernet", 6),
          ("opticalFastEthernet", 18),
          ("stpSTM1", 10),
          ("twoDS3", 2),
          ("twoE3", 4),
          ("twoSTM1", 11),
          ("utpSTM1", 9))
    )


_GnGenCfgMiddleMediumConnector_Type.__name__ = "Integer32"
_GnGenCfgMiddleMediumConnector_Object = MibTableColumn
gnGenCfgMiddleMediumConnector = _GnGenCfgMiddleMediumConnector_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 8, 1, 19),
    _GnGenCfgMiddleMediumConnector_Type()
)
gnGenCfgMiddleMediumConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnGenCfgMiddleMediumConnector.setStatus("mandatory")


class _GnGenCfgPrimaryClockSource_Type(Integer32):
    """Custom type gnGenCfgPrimaryClockSource based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
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
              24)
        )
    )
    namedValues = NamedValues(
        *(("external1AndHalfMB", 7),
          ("external2MB", 3),
          ("external2MHz", 6),
          ("fiberClock", 5),
          ("internalClock", 2),
          ("radioClock", 4),
          ("tribSTM1", 24),
          ("tributaryClock1", 8),
          ("tributaryClock10", 17),
          ("tributaryClock11", 18),
          ("tributaryClock12", 19),
          ("tributaryClock13", 20),
          ("tributaryClock14", 21),
          ("tributaryClock15", 22),
          ("tributaryClock16", 23),
          ("tributaryClock2", 9),
          ("tributaryClock3", 10),
          ("tributaryClock4", 11),
          ("tributaryClock5", 12),
          ("tributaryClock6", 13),
          ("tributaryClock7", 14),
          ("tributaryClock8", 15),
          ("tributaryClock9", 16))
    )


_GnGenCfgPrimaryClockSource_Type.__name__ = "Integer32"
_GnGenCfgPrimaryClockSource_Object = MibTableColumn
gnGenCfgPrimaryClockSource = _GnGenCfgPrimaryClockSource_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 8, 1, 20),
    _GnGenCfgPrimaryClockSource_Type()
)
gnGenCfgPrimaryClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnGenCfgPrimaryClockSource.setStatus("mandatory")


class _GnGenCfgSecondaryClockSource_Type(Integer32):
    """Custom type gnGenCfgSecondaryClockSource based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
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
              24)
        )
    )
    namedValues = NamedValues(
        *(("external1AndHalfMB", 7),
          ("external2MB", 3),
          ("external2MHz", 6),
          ("fiberClock", 5),
          ("internalClock", 2),
          ("radioClock", 4),
          ("tribSTM1", 24),
          ("tributaryClock1", 8),
          ("tributaryClock10", 17),
          ("tributaryClock11", 18),
          ("tributaryClock12", 19),
          ("tributaryClock13", 20),
          ("tributaryClock14", 21),
          ("tributaryClock15", 22),
          ("tributaryClock16", 23),
          ("tributaryClock2", 9),
          ("tributaryClock3", 10),
          ("tributaryClock4", 11),
          ("tributaryClock5", 12),
          ("tributaryClock6", 13),
          ("tributaryClock7", 14),
          ("tributaryClock8", 15),
          ("tributaryClock9", 16))
    )


_GnGenCfgSecondaryClockSource_Type.__name__ = "Integer32"
_GnGenCfgSecondaryClockSource_Object = MibTableColumn
gnGenCfgSecondaryClockSource = _GnGenCfgSecondaryClockSource_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 8, 1, 21),
    _GnGenCfgSecondaryClockSource_Type()
)
gnGenCfgSecondaryClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnGenCfgSecondaryClockSource.setStatus("mandatory")


class _GnGenCfgTrapOption_Type(Integer32):
    """Custom type gnGenCfgTrapOption based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_GnGenCfgTrapOption_Type.__name__ = "Integer32"
_GnGenCfgTrapOption_Object = MibTableColumn
gnGenCfgTrapOption = _GnGenCfgTrapOption_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 8, 1, 22),
    _GnGenCfgTrapOption_Type()
)
gnGenCfgTrapOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnGenCfgTrapOption.setStatus("mandatory")


class _GnGenCfgCLLI_Type(DisplayString):
    """Custom type gnGenCfgCLLI based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_GnGenCfgCLLI_Type.__name__ = "DisplayString"
_GnGenCfgCLLI_Object = MibTableColumn
gnGenCfgCLLI = _GnGenCfgCLLI_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 8, 1, 23),
    _GnGenCfgCLLI_Type()
)
gnGenCfgCLLI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnGenCfgCLLI.setStatus("mandatory")


class _GnGenCfgHeartbeatPeriod_Type(Integer32):
    """Custom type gnGenCfgHeartbeatPeriod based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_GnGenCfgHeartbeatPeriod_Type.__name__ = "Integer32"
_GnGenCfgHeartbeatPeriod_Object = MibTableColumn
gnGenCfgHeartbeatPeriod = _GnGenCfgHeartbeatPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 8, 1, 24),
    _GnGenCfgHeartbeatPeriod_Type()
)
gnGenCfgHeartbeatPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnGenCfgHeartbeatPeriod.setStatus("mandatory")


class _GnGenCfgGetRemoteData_Type(Integer32):
    """Custom type gnGenCfgGetRemoteData based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3))
    )


_GnGenCfgGetRemoteData_Type.__name__ = "Integer32"
_GnGenCfgGetRemoteData_Object = MibTableColumn
gnGenCfgGetRemoteData = _GnGenCfgGetRemoteData_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 8, 1, 25),
    _GnGenCfgGetRemoteData_Type()
)
gnGenCfgGetRemoteData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnGenCfgGetRemoteData.setStatus("mandatory")


class _GnGenCfgClearLoopTimeout_Type(Integer32):
    """Custom type gnGenCfgClearLoopTimeout based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_GnGenCfgClearLoopTimeout_Type.__name__ = "Integer32"
_GnGenCfgClearLoopTimeout_Object = MibTableColumn
gnGenCfgClearLoopTimeout = _GnGenCfgClearLoopTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 8, 1, 26),
    _GnGenCfgClearLoopTimeout_Type()
)
gnGenCfgClearLoopTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnGenCfgClearLoopTimeout.setStatus("mandatory")
_GnGenCfgSubProductType_Type = Integer32
_GnGenCfgSubProductType_Object = MibTableColumn
gnGenCfgSubProductType = _GnGenCfgSubProductType_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 8, 1, 27),
    _GnGenCfgSubProductType_Type()
)
gnGenCfgSubProductType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnGenCfgSubProductType.setStatus("mandatory")
_GnGenStatDeviceTable_Object = MibTable
gnGenStatDeviceTable = _GnGenStatDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 9)
)
if mibBuilder.loadTexts:
    gnGenStatDeviceTable.setStatus("mandatory")
_GnGenStatDeviceEntry_Object = MibTableRow
gnGenStatDeviceEntry = _GnGenStatDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 9, 1)
)
gnGenStatDeviceEntry.setIndexNames(
    (0, "CERAGON-MIB", "gnGenStatDeviceId"),
)
if mibBuilder.loadTexts:
    gnGenStatDeviceEntry.setStatus("mandatory")


class _GnGenStatDeviceId_Type(Integer32):
    """Custom type gnGenStatDeviceId based on Integer32"""
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
        *(("drawer1", 3),
          ("drawer2", 4),
          ("local", 1),
          ("remote", 2))
    )


_GnGenStatDeviceId_Type.__name__ = "Integer32"
_GnGenStatDeviceId_Object = MibTableColumn
gnGenStatDeviceId = _GnGenStatDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 9, 1, 1),
    _GnGenStatDeviceId_Type()
)
gnGenStatDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnGenStatDeviceId.setStatus("mandatory")


class _GnGenStatDeviceCelsiusTemp_Type(Integer32):
    """Custom type gnGenStatDeviceCelsiusTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-10, 70),
    )


_GnGenStatDeviceCelsiusTemp_Type.__name__ = "Integer32"
_GnGenStatDeviceCelsiusTemp_Object = MibTableColumn
gnGenStatDeviceCelsiusTemp = _GnGenStatDeviceCelsiusTemp_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 9, 1, 2),
    _GnGenStatDeviceCelsiusTemp_Type()
)
gnGenStatDeviceCelsiusTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnGenStatDeviceCelsiusTemp.setStatus("mandatory")


class _GnGenStatDeviceFahrenheitTemp_Type(Integer32):
    """Custom type gnGenStatDeviceFahrenheitTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(14, 158),
    )


_GnGenStatDeviceFahrenheitTemp_Type.__name__ = "Integer32"
_GnGenStatDeviceFahrenheitTemp_Object = MibTableColumn
gnGenStatDeviceFahrenheitTemp = _GnGenStatDeviceFahrenheitTemp_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 9, 1, 3),
    _GnGenStatDeviceFahrenheitTemp_Type()
)
gnGenStatDeviceFahrenheitTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnGenStatDeviceFahrenheitTemp.setStatus("mandatory")


class _GnGenStatDevicePowerSupply_Type(OctetString):
    """Custom type gnGenStatDevicePowerSupply based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_GnGenStatDevicePowerSupply_Type.__name__ = "OctetString"
_GnGenStatDevicePowerSupply_Object = MibTableColumn
gnGenStatDevicePowerSupply = _GnGenStatDevicePowerSupply_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 9, 1, 4),
    _GnGenStatDevicePowerSupply_Type()
)
gnGenStatDevicePowerSupply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnGenStatDevicePowerSupply.setStatus("mandatory")


class _GnGenStatDeviceCable_Type(Integer32):
    """Custom type gnGenStatDeviceCable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ok", 2),
          ("open", 4),
          ("short", 3))
    )


_GnGenStatDeviceCable_Type.__name__ = "Integer32"
_GnGenStatDeviceCable_Object = MibTableColumn
gnGenStatDeviceCable = _GnGenStatDeviceCable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 9, 1, 5),
    _GnGenStatDeviceCable_Type()
)
gnGenStatDeviceCable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnGenStatDeviceCable.setStatus("mandatory")


class _GnGenStatDeviceDryContact_Type(OctetString):
    """Custom type gnGenStatDeviceDryContact based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_GnGenStatDeviceDryContact_Type.__name__ = "OctetString"
_GnGenStatDeviceDryContact_Object = MibTableColumn
gnGenStatDeviceDryContact = _GnGenStatDeviceDryContact_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 9, 1, 6),
    _GnGenStatDeviceDryContact_Type()
)
gnGenStatDeviceDryContact.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnGenStatDeviceDryContact.setStatus("mandatory")


class _GnGenStatDeviceLeds_Type(OctetString):
    """Custom type gnGenStatDeviceLeds based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_GnGenStatDeviceLeds_Type.__name__ = "OctetString"
_GnGenStatDeviceLeds_Object = MibTableColumn
gnGenStatDeviceLeds = _GnGenStatDeviceLeds_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 9, 1, 7),
    _GnGenStatDeviceLeds_Type()
)
gnGenStatDeviceLeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnGenStatDeviceLeds.setStatus("mandatory")


class _GnGenStatInternalCommunication_Type(OctetString):
    """Custom type gnGenStatInternalCommunication based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_GnGenStatInternalCommunication_Type.__name__ = "OctetString"
_GnGenStatInternalCommunication_Object = MibTableColumn
gnGenStatInternalCommunication = _GnGenStatInternalCommunication_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 9, 1, 8),
    _GnGenStatInternalCommunication_Type()
)
gnGenStatInternalCommunication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnGenStatInternalCommunication.setStatus("mandatory")


class _GnGenStatDeviceFanStatus_Type(OctetString):
    """Custom type gnGenStatDeviceFanStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_GnGenStatDeviceFanStatus_Type.__name__ = "OctetString"
_GnGenStatDeviceFanStatus_Object = MibTableColumn
gnGenStatDeviceFanStatus = _GnGenStatDeviceFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 9, 1, 9),
    _GnGenStatDeviceFanStatus_Type()
)
gnGenStatDeviceFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnGenStatDeviceFanStatus.setStatus("mandatory")


class _GnGenStatDeviceODUStatus_Type(OctetString):
    """Custom type gnGenStatDeviceODUStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_GnGenStatDeviceODUStatus_Type.__name__ = "OctetString"
_GnGenStatDeviceODUStatus_Object = MibTableColumn
gnGenStatDeviceODUStatus = _GnGenStatDeviceODUStatus_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 9, 1, 10),
    _GnGenStatDeviceODUStatus_Type()
)
gnGenStatDeviceODUStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnGenStatDeviceODUStatus.setStatus("mandatory")


class _GnGenStatDeviceIDUStatus_Type(OctetString):
    """Custom type gnGenStatDeviceIDUStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_GnGenStatDeviceIDUStatus_Type.__name__ = "OctetString"
_GnGenStatDeviceIDUStatus_Object = MibTableColumn
gnGenStatDeviceIDUStatus = _GnGenStatDeviceIDUStatus_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 9, 1, 11),
    _GnGenStatDeviceIDUStatus_Type()
)
gnGenStatDeviceIDUStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnGenStatDeviceIDUStatus.setStatus("mandatory")


class _GnGenStatDeviceRSTStatus_Type(OctetString):
    """Custom type gnGenStatDeviceRSTStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_GnGenStatDeviceRSTStatus_Type.__name__ = "OctetString"
_GnGenStatDeviceRSTStatus_Object = MibTableColumn
gnGenStatDeviceRSTStatus = _GnGenStatDeviceRSTStatus_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 9, 1, 12),
    _GnGenStatDeviceRSTStatus_Type()
)
gnGenStatDeviceRSTStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnGenStatDeviceRSTStatus.setStatus("mandatory")
_GnGenChannelBandwidth_Type = Integer32
_GnGenChannelBandwidth_Object = MibScalar
gnGenChannelBandwidth = _GnGenChannelBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 10),
    _GnGenChannelBandwidth_Type()
)
gnGenChannelBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnGenChannelBandwidth.setStatus("mandatory")
_GnGenTxFreqNumLocalRemote_Type = Integer32
_GnGenTxFreqNumLocalRemote_Object = MibScalar
gnGenTxFreqNumLocalRemote = _GnGenTxFreqNumLocalRemote_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 11),
    _GnGenTxFreqNumLocalRemote_Type()
)
gnGenTxFreqNumLocalRemote.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnGenTxFreqNumLocalRemote.setStatus("mandatory")


class _GnGenProtocolType_Type(Integer32):
    """Custom type gnGenProtocolType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("gnSDH", 2),
          ("gnSDH-C", 5),
          ("gnSONET", 3),
          ("gnSONET-C", 4))
    )


_GnGenProtocolType_Type.__name__ = "Integer32"
_GnGenProtocolType_Object = MibScalar
gnGenProtocolType = _GnGenProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 12),
    _GnGenProtocolType_Type()
)
gnGenProtocolType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnGenProtocolType.setStatus("mandatory")


class _GnGenLinkId_Type(Integer32):
    """Custom type gnGenLinkId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_GnGenLinkId_Type.__name__ = "Integer32"
_GnGenLinkId_Object = MibScalar
gnGenLinkId = _GnGenLinkId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 13),
    _GnGenLinkId_Type()
)
gnGenLinkId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnGenLinkId.setStatus("mandatory")


class _GnGenMibVersion_Type(DisplayString):
    """Custom type gnGenMibVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_GnGenMibVersion_Type.__name__ = "DisplayString"
_GnGenMibVersion_Object = MibScalar
gnGenMibVersion = _GnGenMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 14),
    _GnGenMibVersion_Type()
)
gnGenMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnGenMibVersion.setStatus("mandatory")


class _GnGenModemType_Type(Integer32):
    """Custom type gnGenModemType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("gn128QAM", 4),
          ("gn16QAM", 2),
          ("gn256QAM", 5),
          ("gn32QAM", 3),
          ("gn4QAM", 7),
          ("gn64QAM", 6))
    )


_GnGenModemType_Type.__name__ = "Integer32"
_GnGenModemType_Object = MibScalar
gnGenModemType = _GnGenModemType_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 15),
    _GnGenModemType_Type()
)
gnGenModemType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnGenModemType.setStatus("mandatory")


class _GnGenRadioSide_Type(Integer32):
    """Custom type gnGenRadioSide based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("east", 2),
          ("west", 3))
    )


_GnGenRadioSide_Type.__name__ = "Integer32"
_GnGenRadioSide_Object = MibScalar
gnGenRadioSide = _GnGenRadioSide_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 16),
    _GnGenRadioSide_Type()
)
gnGenRadioSide.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnGenRadioSide.setStatus("mandatory")


class _GnGenSystemWorkTime_Type(Integer32):
    """Custom type gnGenSystemWorkTime based on Integer32"""
    defaultValue = 0


_GnGenSystemWorkTime_Object = MibScalar
gnGenSystemWorkTime = _GnGenSystemWorkTime_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 17),
    _GnGenSystemWorkTime_Type()
)
gnGenSystemWorkTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnGenSystemWorkTime.setStatus("mandatory")
_GnGenRxFreqNumLocalRemote_Type = Integer32
_GnGenRxFreqNumLocalRemote_Object = MibScalar
gnGenRxFreqNumLocalRemote = _GnGenRxFreqNumLocalRemote_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 18),
    _GnGenRxFreqNumLocalRemote_Type()
)
gnGenRxFreqNumLocalRemote.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnGenRxFreqNumLocalRemote.setStatus("mandatory")


class _GnGenLastCfgTimeandDate_Type(OctetString):
    """Custom type gnGenLastCfgTimeandDate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_GnGenLastCfgTimeandDate_Type.__name__ = "OctetString"
_GnGenLastCfgTimeandDate_Object = MibScalar
gnGenLastCfgTimeandDate = _GnGenLastCfgTimeandDate_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 19),
    _GnGenLastCfgTimeandDate_Type()
)
gnGenLastCfgTimeandDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnGenLastCfgTimeandDate.setStatus("mandatory")


class _GnGenMostSevereAlarm_Type(Integer32):
    """Custom type gnGenMostSevereAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3,
              7,
              15,
              31)
        )
    )
    namedValues = NamedValues(
        *(("clear", 0),
          ("critical", 31),
          ("event", 1),
          ("major", 15),
          ("minor", 7),
          ("warning", 3))
    )


_GnGenMostSevereAlarm_Type.__name__ = "Integer32"
_GnGenMostSevereAlarm_Object = MibScalar
gnGenMostSevereAlarm = _GnGenMostSevereAlarm_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 20),
    _GnGenMostSevereAlarm_Type()
)
gnGenMostSevereAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnGenMostSevereAlarm.setStatus("mandatory")
_GnGenIdcCfgTable_Object = MibTable
gnGenIdcCfgTable = _GnGenIdcCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 21)
)
if mibBuilder.loadTexts:
    gnGenIdcCfgTable.setStatus("mandatory")
_GnGenIdcCfgEntry_Object = MibTableRow
gnGenIdcCfgEntry = _GnGenIdcCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 21, 1)
)
gnGenIdcCfgEntry.setIndexNames(
    (0, "CERAGON-MIB", "gnGenIdcCfgId"),
)
if mibBuilder.loadTexts:
    gnGenIdcCfgEntry.setStatus("mandatory")


class _GnGenIdcCfgId_Type(Integer32):
    """Custom type gnGenIdcCfgId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("local", 1)
    )


_GnGenIdcCfgId_Type.__name__ = "Integer32"
_GnGenIdcCfgId_Object = MibTableColumn
gnGenIdcCfgId = _GnGenIdcCfgId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 21, 1, 1),
    _GnGenIdcCfgId_Type()
)
gnGenIdcCfgId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnGenIdcCfgId.setStatus("mandatory")


class _GnGenIdcCfgXpicMode_Type(Integer32):
    """Custom type gnGenIdcCfgXpicMode based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("enable", 2))
    )


_GnGenIdcCfgXpicMode_Type.__name__ = "Integer32"
_GnGenIdcCfgXpicMode_Object = MibTableColumn
gnGenIdcCfgXpicMode = _GnGenIdcCfgXpicMode_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 21, 1, 2),
    _GnGenIdcCfgXpicMode_Type()
)
gnGenIdcCfgXpicMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnGenIdcCfgXpicMode.setStatus("mandatory")


class _GnGenIdcCfgResetPerfMon_Type(Integer32):
    """Custom type gnGenIdcCfgResetPerfMon based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("clearFastEthernetStatistics", 4),
          ("noAction", 3),
          ("reset", 2))
    )


_GnGenIdcCfgResetPerfMon_Type.__name__ = "Integer32"
_GnGenIdcCfgResetPerfMon_Object = MibTableColumn
gnGenIdcCfgResetPerfMon = _GnGenIdcCfgResetPerfMon_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 21, 1, 3),
    _GnGenIdcCfgResetPerfMon_Type()
)
gnGenIdcCfgResetPerfMon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnGenIdcCfgResetPerfMon.setStatus("mandatory")


class _GnGenIdcCfgOperation_Type(Integer32):
    """Custom type gnGenIdcCfgOperation based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("hardwareColdReset", 6),
          ("hardwareSoftReset", 7),
          ("noOperation", 2),
          ("setDefaultConf", 4),
          ("setIDCDefaultConf", 5),
          ("softwareReset", 3))
    )


_GnGenIdcCfgOperation_Type.__name__ = "Integer32"
_GnGenIdcCfgOperation_Object = MibTableColumn
gnGenIdcCfgOperation = _GnGenIdcCfgOperation_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 21, 1, 4),
    _GnGenIdcCfgOperation_Type()
)
gnGenIdcCfgOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnGenIdcCfgOperation.setStatus("mandatory")


class _GnGenIdcCfgWaySideConnector_Type(Integer32):
    """Custom type gnGenIdcCfgWaySideConnector based on Integer32"""
    defaultValue = 1

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
        *(("connectorDual10baseT", 6),
          ("connectorDualE1", 4),
          ("connectorDualT1", 5),
          ("connectorE1", 2),
          ("connectorT1", 3),
          ("noInterface", 1))
    )


_GnGenIdcCfgWaySideConnector_Type.__name__ = "Integer32"
_GnGenIdcCfgWaySideConnector_Object = MibTableColumn
gnGenIdcCfgWaySideConnector = _GnGenIdcCfgWaySideConnector_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 21, 1, 5),
    _GnGenIdcCfgWaySideConnector_Type()
)
gnGenIdcCfgWaySideConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnGenIdcCfgWaySideConnector.setStatus("mandatory")


class _GnGenIdcCfgHeartbeatPeriod_Type(Integer32):
    """Custom type gnGenIdcCfgHeartbeatPeriod based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_GnGenIdcCfgHeartbeatPeriod_Type.__name__ = "Integer32"
_GnGenIdcCfgHeartbeatPeriod_Object = MibTableColumn
gnGenIdcCfgHeartbeatPeriod = _GnGenIdcCfgHeartbeatPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 21, 1, 6),
    _GnGenIdcCfgHeartbeatPeriod_Type()
)
gnGenIdcCfgHeartbeatPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnGenIdcCfgHeartbeatPeriod.setStatus("mandatory")


class _GnGenIdcCfgClearLoopTimeout_Type(Integer32):
    """Custom type gnGenIdcCfgClearLoopTimeout based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_GnGenIdcCfgClearLoopTimeout_Type.__name__ = "Integer32"
_GnGenIdcCfgClearLoopTimeout_Object = MibTableColumn
gnGenIdcCfgClearLoopTimeout = _GnGenIdcCfgClearLoopTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 21, 1, 7),
    _GnGenIdcCfgClearLoopTimeout_Type()
)
gnGenIdcCfgClearLoopTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnGenIdcCfgClearLoopTimeout.setStatus("mandatory")
_GnGenIdcCfgSlipIp_Type = IpAddress
_GnGenIdcCfgSlipIp_Object = MibTableColumn
gnGenIdcCfgSlipIp = _GnGenIdcCfgSlipIp_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 21, 1, 8),
    _GnGenIdcCfgSlipIp_Type()
)
gnGenIdcCfgSlipIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnGenIdcCfgSlipIp.setStatus("mandatory")
_GnGenIdcCfgSlipModemConnection_Type = DisplayString
_GnGenIdcCfgSlipModemConnection_Object = MibTableColumn
gnGenIdcCfgSlipModemConnection = _GnGenIdcCfgSlipModemConnection_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 21, 1, 9),
    _GnGenIdcCfgSlipModemConnection_Type()
)
gnGenIdcCfgSlipModemConnection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnGenIdcCfgSlipModemConnection.setStatus("mandatory")


class _GnGenIdcCfgSlipSpeed_Type(Integer32):
    """Custom type gnGenIdcCfgSlipSpeed based on Integer32"""
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
        *(("baud115200", 5),
          ("baud19200", 2),
          ("baud38400", 3),
          ("baud57600", 4),
          ("baud9600", 1))
    )


_GnGenIdcCfgSlipSpeed_Type.__name__ = "Integer32"
_GnGenIdcCfgSlipSpeed_Object = MibTableColumn
gnGenIdcCfgSlipSpeed = _GnGenIdcCfgSlipSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 21, 1, 10),
    _GnGenIdcCfgSlipSpeed_Type()
)
gnGenIdcCfgSlipSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnGenIdcCfgSlipSpeed.setStatus("mandatory")


class _GnGenIdcCfgAlarmSeverity_Type(OctetString):
    """Custom type gnGenIdcCfgAlarmSeverity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(15, 15),
    )


_GnGenIdcCfgAlarmSeverity_Type.__name__ = "OctetString"
_GnGenIdcCfgAlarmSeverity_Object = MibTableColumn
gnGenIdcCfgAlarmSeverity = _GnGenIdcCfgAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 21, 1, 11),
    _GnGenIdcCfgAlarmSeverity_Type()
)
gnGenIdcCfgAlarmSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnGenIdcCfgAlarmSeverity.setStatus("mandatory")


class _GnGenIdcCfgIDUSerialNumber_Type(DisplayString):
    """Custom type gnGenIdcCfgIDUSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_GnGenIdcCfgIDUSerialNumber_Type.__name__ = "DisplayString"
_GnGenIdcCfgIDUSerialNumber_Object = MibTableColumn
gnGenIdcCfgIDUSerialNumber = _GnGenIdcCfgIDUSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 21, 1, 12),
    _GnGenIdcCfgIDUSerialNumber_Type()
)
gnGenIdcCfgIDUSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnGenIdcCfgIDUSerialNumber.setStatus("mandatory")


class _GnGenIdcCfgTrapOption_Type(Integer32):
    """Custom type gnGenIdcCfgTrapOption based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_GnGenIdcCfgTrapOption_Type.__name__ = "Integer32"
_GnGenIdcCfgTrapOption_Object = MibTableColumn
gnGenIdcCfgTrapOption = _GnGenIdcCfgTrapOption_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 21, 1, 13),
    _GnGenIdcCfgTrapOption_Type()
)
gnGenIdcCfgTrapOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnGenIdcCfgTrapOption.setStatus("mandatory")


class _GnGenIdcCfgCLLI_Type(DisplayString):
    """Custom type gnGenIdcCfgCLLI based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_GnGenIdcCfgCLLI_Type.__name__ = "DisplayString"
_GnGenIdcCfgCLLI_Object = MibTableColumn
gnGenIdcCfgCLLI = _GnGenIdcCfgCLLI_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 21, 1, 14),
    _GnGenIdcCfgCLLI_Type()
)
gnGenIdcCfgCLLI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnGenIdcCfgCLLI.setStatus("mandatory")


class _GnGenIdcCfgEowCascadeStatus_Type(Integer32):
    """Custom type gnGenIdcCfgEowCascadeStatus based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("enable", 2))
    )


_GnGenIdcCfgEowCascadeStatus_Type.__name__ = "Integer32"
_GnGenIdcCfgEowCascadeStatus_Object = MibTableColumn
gnGenIdcCfgEowCascadeStatus = _GnGenIdcCfgEowCascadeStatus_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 21, 1, 15),
    _GnGenIdcCfgEowCascadeStatus_Type()
)
gnGenIdcCfgEowCascadeStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnGenIdcCfgEowCascadeStatus.setStatus("mandatory")


class _GnGenIdcCfgSerialPPPAdminStatus_Type(Integer32):
    """Custom type gnGenIdcCfgSerialPPPAdminStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("enable", 2))
    )


_GnGenIdcCfgSerialPPPAdminStatus_Type.__name__ = "Integer32"
_GnGenIdcCfgSerialPPPAdminStatus_Object = MibTableColumn
gnGenIdcCfgSerialPPPAdminStatus = _GnGenIdcCfgSerialPPPAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 21, 1, 16),
    _GnGenIdcCfgSerialPPPAdminStatus_Type()
)
gnGenIdcCfgSerialPPPAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnGenIdcCfgSerialPPPAdminStatus.setStatus("mandatory")
_GnGenIdcStatTable_Object = MibTable
gnGenIdcStatTable = _GnGenIdcStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 22)
)
if mibBuilder.loadTexts:
    gnGenIdcStatTable.setStatus("mandatory")
_GnGenIdcStatEntry_Object = MibTableRow
gnGenIdcStatEntry = _GnGenIdcStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 22, 1)
)
gnGenIdcStatEntry.setIndexNames(
    (0, "CERAGON-MIB", "gnGenIdcStatId"),
)
if mibBuilder.loadTexts:
    gnGenIdcStatEntry.setStatus("mandatory")


class _GnGenIdcStatId_Type(Integer32):
    """Custom type gnGenIdcStatId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("local", 1)
    )


_GnGenIdcStatId_Type.__name__ = "Integer32"
_GnGenIdcStatId_Object = MibTableColumn
gnGenIdcStatId = _GnGenIdcStatId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 22, 1, 1),
    _GnGenIdcStatId_Type()
)
gnGenIdcStatId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnGenIdcStatId.setStatus("mandatory")


class _GnGenIdcStatXpicSupport_Type(Integer32):
    """Custom type gnGenIdcStatXpicSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 3),
          ("yes", 2))
    )


_GnGenIdcStatXpicSupport_Type.__name__ = "Integer32"
_GnGenIdcStatXpicSupport_Object = MibTableColumn
gnGenIdcStatXpicSupport = _GnGenIdcStatXpicSupport_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 22, 1, 2),
    _GnGenIdcStatXpicSupport_Type()
)
gnGenIdcStatXpicSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnGenIdcStatXpicSupport.setStatus("mandatory")


class _GnGenIdcStatLeds_Type(OctetString):
    """Custom type gnGenIdcStatLeds based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_GnGenIdcStatLeds_Type.__name__ = "OctetString"
_GnGenIdcStatLeds_Object = MibTableColumn
gnGenIdcStatLeds = _GnGenIdcStatLeds_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 22, 1, 3),
    _GnGenIdcStatLeds_Type()
)
gnGenIdcStatLeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnGenIdcStatLeds.setStatus("mandatory")


class _GnGenIdcStatIDUStatus_Type(OctetString):
    """Custom type gnGenIdcStatIDUStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_GnGenIdcStatIDUStatus_Type.__name__ = "OctetString"
_GnGenIdcStatIDUStatus_Object = MibTableColumn
gnGenIdcStatIDUStatus = _GnGenIdcStatIDUStatus_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 22, 1, 4),
    _GnGenIdcStatIDUStatus_Type()
)
gnGenIdcStatIDUStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnGenIdcStatIDUStatus.setStatus("mandatory")


class _GnGenIdcStatMMCCardStatus_Type(OctetString):
    """Custom type gnGenIdcStatMMCCardStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_GnGenIdcStatMMCCardStatus_Type.__name__ = "OctetString"
_GnGenIdcStatMMCCardStatus_Object = MibTableColumn
gnGenIdcStatMMCCardStatus = _GnGenIdcStatMMCCardStatus_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 22, 1, 5),
    _GnGenIdcStatMMCCardStatus_Type()
)
gnGenIdcStatMMCCardStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnGenIdcStatMMCCardStatus.setStatus("mandatory")


class _GnGenIdcStatDryContact_Type(OctetString):
    """Custom type gnGenIdcStatDryContact based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_GnGenIdcStatDryContact_Type.__name__ = "OctetString"
_GnGenIdcStatDryContact_Object = MibTableColumn
gnGenIdcStatDryContact = _GnGenIdcStatDryContact_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 22, 1, 6),
    _GnGenIdcStatDryContact_Type()
)
gnGenIdcStatDryContact.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnGenIdcStatDryContact.setStatus("mandatory")


class _GnGenIdcStatFanStatus_Type(OctetString):
    """Custom type gnGenIdcStatFanStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_GnGenIdcStatFanStatus_Type.__name__ = "OctetString"
_GnGenIdcStatFanStatus_Object = MibTableColumn
gnGenIdcStatFanStatus = _GnGenIdcStatFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 22, 1, 7),
    _GnGenIdcStatFanStatus_Type()
)
gnGenIdcStatFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnGenIdcStatFanStatus.setStatus("mandatory")


class _GnGenIdcStatLeftDrawerStatus_Type(Integer32):
    """Custom type gnGenIdcStatLeftDrawerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("drawerDown", 3),
          ("drawerUp", 4),
          ("noDrawer", 2))
    )


_GnGenIdcStatLeftDrawerStatus_Type.__name__ = "Integer32"
_GnGenIdcStatLeftDrawerStatus_Object = MibTableColumn
gnGenIdcStatLeftDrawerStatus = _GnGenIdcStatLeftDrawerStatus_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 22, 1, 8),
    _GnGenIdcStatLeftDrawerStatus_Type()
)
gnGenIdcStatLeftDrawerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnGenIdcStatLeftDrawerStatus.setStatus("mandatory")


class _GnGenIdcStatRightDrawerStatus_Type(Integer32):
    """Custom type gnGenIdcStatRightDrawerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("drawerDown", 3),
          ("drawerUp", 4),
          ("noDrawer", 2))
    )


_GnGenIdcStatRightDrawerStatus_Type.__name__ = "Integer32"
_GnGenIdcStatRightDrawerStatus_Object = MibTableColumn
gnGenIdcStatRightDrawerStatus = _GnGenIdcStatRightDrawerStatus_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 22, 1, 9),
    _GnGenIdcStatRightDrawerStatus_Type()
)
gnGenIdcStatRightDrawerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnGenIdcStatRightDrawerStatus.setStatus("mandatory")


class _GnGenIdcStatHitlessSupport_Type(Integer32):
    """Custom type gnGenIdcStatHitlessSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 3),
          ("supported", 2))
    )


_GnGenIdcStatHitlessSupport_Type.__name__ = "Integer32"
_GnGenIdcStatHitlessSupport_Object = MibTableColumn
gnGenIdcStatHitlessSupport = _GnGenIdcStatHitlessSupport_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 22, 1, 10),
    _GnGenIdcStatHitlessSupport_Type()
)
gnGenIdcStatHitlessSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnGenIdcStatHitlessSupport.setStatus("mandatory")


class _GnGenIdcStatEowExistence_Type(Integer32):
    """Custom type gnGenIdcStatEowExistence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("exist", 2),
          ("notExist", 3))
    )


_GnGenIdcStatEowExistence_Type.__name__ = "Integer32"
_GnGenIdcStatEowExistence_Object = MibTableColumn
gnGenIdcStatEowExistence = _GnGenIdcStatEowExistence_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 22, 1, 11),
    _GnGenIdcStatEowExistence_Type()
)
gnGenIdcStatEowExistence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnGenIdcStatEowExistence.setStatus("mandatory")


class _GnGenIdcStatEowSupport_Type(Integer32):
    """Custom type gnGenIdcStatEowSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 3),
          ("supported", 2))
    )


_GnGenIdcStatEowSupport_Type.__name__ = "Integer32"
_GnGenIdcStatEowSupport_Object = MibTableColumn
gnGenIdcStatEowSupport = _GnGenIdcStatEowSupport_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 22, 1, 12),
    _GnGenIdcStatEowSupport_Type()
)
gnGenIdcStatEowSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnGenIdcStatEowSupport.setStatus("mandatory")


class _GnGenIdcStatIduPosition_Type(Integer32):
    """Custom type gnGenIdcStatIduPosition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("lower", 3),
          ("single", 4),
          ("upper", 2))
    )


_GnGenIdcStatIduPosition_Type.__name__ = "Integer32"
_GnGenIdcStatIduPosition_Object = MibTableColumn
gnGenIdcStatIduPosition = _GnGenIdcStatIduPosition_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 22, 1, 13),
    _GnGenIdcStatIduPosition_Type()
)
gnGenIdcStatIduPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnGenIdcStatIduPosition.setStatus("mandatory")


class _GnGenIdcStatBoardType_Type(Integer32):
    """Custom type gnGenIdcStatBoardType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("v1", 2),
          ("v2", 3))
    )


_GnGenIdcStatBoardType_Type.__name__ = "Integer32"
_GnGenIdcStatBoardType_Object = MibTableColumn
gnGenIdcStatBoardType = _GnGenIdcStatBoardType_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 22, 1, 14),
    _GnGenIdcStatBoardType_Type()
)
gnGenIdcStatBoardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnGenIdcStatBoardType.setStatus("mandatory")
_GnGenIdcStatAgentIPAddress_Type = IpAddress
_GnGenIdcStatAgentIPAddress_Object = MibTableColumn
gnGenIdcStatAgentIPAddress = _GnGenIdcStatAgentIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 22, 1, 15),
    _GnGenIdcStatAgentIPAddress_Type()
)
gnGenIdcStatAgentIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnGenIdcStatAgentIPAddress.setStatus("mandatory")


class _GnGenIdcStatInterfaceConnector_Type(Integer32):
    """Custom type gnGenIdcStatInterfaceConnector based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("notExist", 2),
          ("oneFEplus64E1", 3),
          ("twoFEplus64E1", 4))
    )


_GnGenIdcStatInterfaceConnector_Type.__name__ = "Integer32"
_GnGenIdcStatInterfaceConnector_Object = MibTableColumn
gnGenIdcStatInterfaceConnector = _GnGenIdcStatInterfaceConnector_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 22, 1, 16),
    _GnGenIdcStatInterfaceConnector_Type()
)
gnGenIdcStatInterfaceConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnGenIdcStatInterfaceConnector.setStatus("mandatory")
_GnGenIdcStatIfTableCounter_Type = Integer32
_GnGenIdcStatIfTableCounter_Object = MibTableColumn
gnGenIdcStatIfTableCounter = _GnGenIdcStatIfTableCounter_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 22, 1, 17),
    _GnGenIdcStatIfTableCounter_Type()
)
gnGenIdcStatIfTableCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnGenIdcStatIfTableCounter.setStatus("mandatory")
_GnGeneralXTable_Object = MibTable
gnGeneralXTable = _GnGeneralXTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 23)
)
if mibBuilder.loadTexts:
    gnGeneralXTable.setStatus("mandatory")
_GnGeneralXEntry_Object = MibTableRow
gnGeneralXEntry = _GnGeneralXEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 23, 1)
)
gnGeneralXEntry.setIndexNames(
    (0, "CERAGON-MIB", "gnGenXId"),
)
if mibBuilder.loadTexts:
    gnGeneralXEntry.setStatus("mandatory")


class _GnGenXId_Type(Integer32):
    """Custom type gnGenXId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("drawer1", 3),
          ("drawer2", 4))
    )


_GnGenXId_Type.__name__ = "Integer32"
_GnGenXId_Object = MibTableColumn
gnGenXId = _GnGenXId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 23, 1, 1),
    _GnGenXId_Type()
)
gnGenXId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnGenXId.setStatus("mandatory")


class _GnGenXStandardOrg_Type(Integer32):
    """Custom type gnGenXStandardOrg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("australia", 7),
          ("cmds", 6),
          ("etsi", 2),
          ("fcc", 3),
          ("japan", 4),
          ("lmds", 5),
          ("other", 8))
    )


_GnGenXStandardOrg_Type.__name__ = "Integer32"
_GnGenXStandardOrg_Object = MibTableColumn
gnGenXStandardOrg = _GnGenXStandardOrg_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 23, 1, 2),
    _GnGenXStandardOrg_Type()
)
gnGenXStandardOrg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnGenXStandardOrg.setStatus("mandatory")


class _GnGenXRemoteConnection_Type(Integer32):
    """Custom type gnGenXRemoteConnection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("connected", 2),
          ("disconnected", 3))
    )


_GnGenXRemoteConnection_Type.__name__ = "Integer32"
_GnGenXRemoteConnection_Object = MibTableColumn
gnGenXRemoteConnection = _GnGenXRemoteConnection_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 23, 1, 3),
    _GnGenXRemoteConnection_Type()
)
gnGenXRemoteConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnGenXRemoteConnection.setStatus("mandatory")


class _GnGenXLinkId_Type(Integer32):
    """Custom type gnGenXLinkId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_GnGenXLinkId_Type.__name__ = "Integer32"
_GnGenXLinkId_Object = MibTableColumn
gnGenXLinkId = _GnGenXLinkId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 23, 1, 4),
    _GnGenXLinkId_Type()
)
gnGenXLinkId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnGenXLinkId.setStatus("mandatory")


class _GnGenXModemType_Type(Integer32):
    """Custom type gnGenXModemType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("gn128QAM", 4),
          ("gn16QAM", 2),
          ("gn256QAM", 5),
          ("gn32QAM", 3),
          ("gn4QAM", 7),
          ("gn64QAM", 6))
    )


_GnGenXModemType_Type.__name__ = "Integer32"
_GnGenXModemType_Object = MibTableColumn
gnGenXModemType = _GnGenXModemType_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 23, 1, 5),
    _GnGenXModemType_Type()
)
gnGenXModemType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnGenXModemType.setStatus("mandatory")


class _GnGenXRadioSide_Type(Integer32):
    """Custom type gnGenXRadioSide based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("east", 2),
          ("west", 3))
    )


_GnGenXRadioSide_Type.__name__ = "Integer32"
_GnGenXRadioSide_Object = MibTableColumn
gnGenXRadioSide = _GnGenXRadioSide_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 23, 1, 6),
    _GnGenXRadioSide_Type()
)
gnGenXRadioSide.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnGenXRadioSide.setStatus("mandatory")


class _GnGenXSystemWorkTime_Type(Integer32):
    """Custom type gnGenXSystemWorkTime based on Integer32"""
    defaultValue = 0


_GnGenXSystemWorkTime_Object = MibTableColumn
gnGenXSystemWorkTime = _GnGenXSystemWorkTime_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 23, 1, 7),
    _GnGenXSystemWorkTime_Type()
)
gnGenXSystemWorkTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnGenXSystemWorkTime.setStatus("mandatory")


class _GnGenXOperation_Type(Integer32):
    """Custom type gnGenXOperation based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("hardwareColdReset", 4),
          ("hardwareODCReset", 7),
          ("hardwareWarmReset", 5),
          ("noOperation", 2),
          ("resetAllDrawers", 8),
          ("setMuxDefaultConf", 3),
          ("softwareODCReset", 6))
    )


_GnGenXOperation_Type.__name__ = "Integer32"
_GnGenXOperation_Object = MibTableColumn
gnGenXOperation = _GnGenXOperation_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 23, 1, 8),
    _GnGenXOperation_Type()
)
gnGenXOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnGenXOperation.setStatus("mandatory")


class _GnGenXResetPerfMon_Type(Integer32):
    """Custom type gnGenXResetPerfMon based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("clearFastEthernetStatistics", 4),
          ("noAction", 3),
          ("reset", 2))
    )


_GnGenXResetPerfMon_Type.__name__ = "Integer32"
_GnGenXResetPerfMon_Object = MibTableColumn
gnGenXResetPerfMon = _GnGenXResetPerfMon_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 23, 1, 9),
    _GnGenXResetPerfMon_Type()
)
gnGenXResetPerfMon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnGenXResetPerfMon.setStatus("mandatory")


class _GnGenXAlarmSeverity_Type(OctetString):
    """Custom type gnGenXAlarmSeverity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(15, 15),
    )


_GnGenXAlarmSeverity_Type.__name__ = "OctetString"
_GnGenXAlarmSeverity_Object = MibTableColumn
gnGenXAlarmSeverity = _GnGenXAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 23, 1, 10),
    _GnGenXAlarmSeverity_Type()
)
gnGenXAlarmSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnGenXAlarmSeverity.setStatus("mandatory")


class _GnGenXCarrierSerialNumber_Type(DisplayString):
    """Custom type gnGenXCarrierSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_GnGenXCarrierSerialNumber_Type.__name__ = "DisplayString"
_GnGenXCarrierSerialNumber_Object = MibTableColumn
gnGenXCarrierSerialNumber = _GnGenXCarrierSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 23, 1, 11),
    _GnGenXCarrierSerialNumber_Type()
)
gnGenXCarrierSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnGenXCarrierSerialNumber.setStatus("mandatory")


class _GnGenXMUXSerialNumber_Type(DisplayString):
    """Custom type gnGenXMUXSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_GnGenXMUXSerialNumber_Type.__name__ = "DisplayString"
_GnGenXMUXSerialNumber_Object = MibTableColumn
gnGenXMUXSerialNumber = _GnGenXMUXSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 23, 1, 12),
    _GnGenXMUXSerialNumber_Type()
)
gnGenXMUXSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnGenXMUXSerialNumber.setStatus("mandatory")


class _GnGenXProductType_Type(Integer32):
    """Custom type gnGenXProductType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("accessMux", 2),
          ("accessMuxStm0", 5),
          ("adm", 7),
          ("narrowBandPdhRepeater", 4),
          ("plex6200", 6),
          ("sdhRegenerator", 3))
    )


_GnGenXProductType_Type.__name__ = "Integer32"
_GnGenXProductType_Object = MibTableColumn
gnGenXProductType = _GnGenXProductType_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 23, 1, 13),
    _GnGenXProductType_Type()
)
gnGenXProductType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnGenXProductType.setStatus("mandatory")


class _GnGenXCarrierConnector_Type(Integer32):
    """Custom type gnGenXCarrierConnector based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
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
        *(("eightE1Only", 31),
          ("eightT1Only", 32),
          ("noInterface", 2),
          ("oneDS3", 19),
          ("oneE3", 21),
          ("oneElectricalGBEOnly", 26),
          ("oneElectricalGBEPlus8E1", 27),
          ("oneElectricalGBEPlus8T1", 28),
          ("oneElectricalSTM1", 3),
          ("oneFEOnly", 9),
          ("oneFEplus4E1", 10),
          ("oneFEplus4T1", 12),
          ("oneFEplus64E1", 29),
          ("oneFEplus64T1", 30),
          ("oneFEplus8E1", 11),
          ("oneFEplus8T1", 13),
          ("oneFiberSTM1MultiMode", 5),
          ("oneFiberSTM1SingleMode", 4),
          ("oneOpticalGBEOnly", 23),
          ("oneOpticalGBEPlus8E1", 24),
          ("oneOpticalGBEPlus8T1", 25),
          ("oneStm1XC", 33),
          ("threeDS3", 20),
          ("threeE3", 22),
          ("twoElectricalSTM1", 6),
          ("twoFEOnly", 14),
          ("twoFEplus4E1", 15),
          ("twoFEplus4T1", 17),
          ("twoFEplus8E1", 16),
          ("twoFEplus8T1", 18),
          ("twoFiberSTM1MultiMode", 8),
          ("twoFiberSTM1SingleMode", 7),
          ("twoStm1XC", 34))
    )


_GnGenXCarrierConnector_Type.__name__ = "Integer32"
_GnGenXCarrierConnector_Object = MibTableColumn
gnGenXCarrierConnector = _GnGenXCarrierConnector_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 23, 1, 14),
    _GnGenXCarrierConnector_Type()
)
gnGenXCarrierConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnGenXCarrierConnector.setStatus("mandatory")


class _GnGenXInterfacesLeds_Type(OctetString):
    """Custom type gnGenXInterfacesLeds based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_GnGenXInterfacesLeds_Type.__name__ = "OctetString"
_GnGenXInterfacesLeds_Object = MibTableColumn
gnGenXInterfacesLeds = _GnGenXInterfacesLeds_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 23, 1, 15),
    _GnGenXInterfacesLeds_Type()
)
gnGenXInterfacesLeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnGenXInterfacesLeds.setStatus("mandatory")


class _GnGenXMultiRateMultiConsConf_Type(Integer32):
    """Custom type gnGenXMultiRateMultiConsConf based on Integer32"""
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
              18,
              24,
              25,
              26)
        )
    )
    namedValues = NamedValues(
        *(("acm28", 26),
          ("acm50", 25),
          ("acm56", 24),
          ("mrmc1125", 10),
          ("mrmc1228", 5),
          ("mrmc1340", 13),
          ("mrmc1528", 1),
          ("mrmc1540", 6),
          ("mrmc1550", 2),
          ("mrmc2030", 12),
          ("mrmc2050", 11),
          ("mrmc3150", 4),
          ("mrmc3156", 3),
          ("mrmc3756", 18),
          ("mrmc4410", 7),
          ("mrmc4420", 8),
          ("mrmc4440", 9))
    )


_GnGenXMultiRateMultiConsConf_Type.__name__ = "Integer32"
_GnGenXMultiRateMultiConsConf_Object = MibTableColumn
gnGenXMultiRateMultiConsConf = _GnGenXMultiRateMultiConsConf_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 23, 1, 16),
    _GnGenXMultiRateMultiConsConf_Type()
)
gnGenXMultiRateMultiConsConf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnGenXMultiRateMultiConsConf.setStatus("mandatory")


class _GnGenXMultiRateMultiConsSupport_Type(OctetString):
    """Custom type gnGenXMultiRateMultiConsSupport based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_GnGenXMultiRateMultiConsSupport_Type.__name__ = "OctetString"
_GnGenXMultiRateMultiConsSupport_Object = MibTableColumn
gnGenXMultiRateMultiConsSupport = _GnGenXMultiRateMultiConsSupport_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 23, 1, 17),
    _GnGenXMultiRateMultiConsSupport_Type()
)
gnGenXMultiRateMultiConsSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnGenXMultiRateMultiConsSupport.setStatus("mandatory")


class _GnGenXWaysideChannel_Type(Integer32):
    """Custom type gnGenXWaysideChannel based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("enable", 2))
    )


_GnGenXWaysideChannel_Type.__name__ = "Integer32"
_GnGenXWaysideChannel_Object = MibTableColumn
gnGenXWaysideChannel = _GnGenXWaysideChannel_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 23, 1, 18),
    _GnGenXWaysideChannel_Type()
)
gnGenXWaysideChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnGenXWaysideChannel.setStatus("mandatory")


class _GnGenXWaySideLoopback_Type(Integer32):
    """Custom type gnGenXWaySideLoopback based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noloopback", 2),
          ("waySideLoop", 3))
    )


_GnGenXWaySideLoopback_Type.__name__ = "Integer32"
_GnGenXWaySideLoopback_Object = MibTableColumn
gnGenXWaySideLoopback = _GnGenXWaySideLoopback_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 23, 1, 19),
    _GnGenXWaySideLoopback_Type()
)
gnGenXWaySideLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnGenXWaySideLoopback.setStatus("mandatory")


class _GnGenXSyncIdcDataBase_Type(Integer32):
    """Custom type gnGenXSyncIdcDataBase based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("drawerToIdc", 4),
          ("idcToDrawer", 3),
          ("noOperation", 2))
    )


_GnGenXSyncIdcDataBase_Type.__name__ = "Integer32"
_GnGenXSyncIdcDataBase_Object = MibTableColumn
gnGenXSyncIdcDataBase = _GnGenXSyncIdcDataBase_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 23, 1, 20),
    _GnGenXSyncIdcDataBase_Type()
)
gnGenXSyncIdcDataBase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnGenXSyncIdcDataBase.setStatus("mandatory")


class _GnGenXAesEnable_Type(Integer32):
    """Custom type gnGenXAesEnable based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("enable", 2),
          ("notSupport", 4),
          ("systemFailure", 5))
    )


_GnGenXAesEnable_Type.__name__ = "Integer32"
_GnGenXAesEnable_Object = MibTableColumn
gnGenXAesEnable = _GnGenXAesEnable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 23, 1, 21),
    _GnGenXAesEnable_Type()
)
gnGenXAesEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnGenXAesEnable.setStatus("mandatory")


class _GnGenXAesMkeyMode_Type(Integer32):
    """Custom type gnGenXAesMkeyMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 2),
          ("manual", 3))
    )


_GnGenXAesMkeyMode_Type.__name__ = "Integer32"
_GnGenXAesMkeyMode_Object = MibTableColumn
gnGenXAesMkeyMode = _GnGenXAesMkeyMode_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 23, 1, 22),
    _GnGenXAesMkeyMode_Type()
)
gnGenXAesMkeyMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnGenXAesMkeyMode.setStatus("mandatory")


class _GnGenXActNumOfInterfaceOnClass1_Type(Integer32):
    """Custom type gnGenXActNumOfInterfaceOnClass1 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_GnGenXActNumOfInterfaceOnClass1_Type.__name__ = "Integer32"
_GnGenXActNumOfInterfaceOnClass1_Object = MibTableColumn
gnGenXActNumOfInterfaceOnClass1 = _GnGenXActNumOfInterfaceOnClass1_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 23, 1, 23),
    _GnGenXActNumOfInterfaceOnClass1_Type()
)
gnGenXActNumOfInterfaceOnClass1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnGenXActNumOfInterfaceOnClass1.setStatus("mandatory")


class _GnGenXActNumOfInterfaceOnClass2_Type(Integer32):
    """Custom type gnGenXActNumOfInterfaceOnClass2 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_GnGenXActNumOfInterfaceOnClass2_Type.__name__ = "Integer32"
_GnGenXActNumOfInterfaceOnClass2_Object = MibTableColumn
gnGenXActNumOfInterfaceOnClass2 = _GnGenXActNumOfInterfaceOnClass2_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 23, 1, 24),
    _GnGenXActNumOfInterfaceOnClass2_Type()
)
gnGenXActNumOfInterfaceOnClass2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnGenXActNumOfInterfaceOnClass2.setStatus("mandatory")


class _GnGenXActNumOfInterfaceOnClass3_Type(Integer32):
    """Custom type gnGenXActNumOfInterfaceOnClass3 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_GnGenXActNumOfInterfaceOnClass3_Type.__name__ = "Integer32"
_GnGenXActNumOfInterfaceOnClass3_Object = MibTableColumn
gnGenXActNumOfInterfaceOnClass3 = _GnGenXActNumOfInterfaceOnClass3_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 23, 1, 25),
    _GnGenXActNumOfInterfaceOnClass3_Type()
)
gnGenXActNumOfInterfaceOnClass3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnGenXActNumOfInterfaceOnClass3.setStatus("mandatory")


class _GnGenXEowStatus_Type(Integer32):
    """Custom type gnGenXEowStatus based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("enable", 2))
    )


_GnGenXEowStatus_Type.__name__ = "Integer32"
_GnGenXEowStatus_Object = MibTableColumn
gnGenXEowStatus = _GnGenXEowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 23, 1, 26),
    _GnGenXEowStatus_Type()
)
gnGenXEowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnGenXEowStatus.setStatus("mandatory")


class _GnGenXTempLicenseEnable_Type(Integer32):
    """Custom type gnGenXTempLicenseEnable based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("enable", 2),
          ("notSupported", 4))
    )


_GnGenXTempLicenseEnable_Type.__name__ = "Integer32"
_GnGenXTempLicenseEnable_Object = MibTableColumn
gnGenXTempLicenseEnable = _GnGenXTempLicenseEnable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 23, 1, 27),
    _GnGenXTempLicenseEnable_Type()
)
gnGenXTempLicenseEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnGenXTempLicenseEnable.setStatus("mandatory")


class _GnGenXTempLicenseTimer_Type(Integer32):
    """Custom type gnGenXTempLicenseTimer based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_GnGenXTempLicenseTimer_Type.__name__ = "Integer32"
_GnGenXTempLicenseTimer_Object = MibTableColumn
gnGenXTempLicenseTimer = _GnGenXTempLicenseTimer_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 23, 1, 28),
    _GnGenXTempLicenseTimer_Type()
)
gnGenXTempLicenseTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnGenXTempLicenseTimer.setStatus("mandatory")
_GnGenXDefectBlocks_Type = Integer32
_GnGenXDefectBlocks_Object = MibTableColumn
gnGenXDefectBlocks = _GnGenXDefectBlocks_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 23, 1, 29),
    _GnGenXDefectBlocks_Type()
)
gnGenXDefectBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnGenXDefectBlocks.setStatus("mandatory")
_GnGenXBytesCorrected_Type = Integer32
_GnGenXBytesCorrected_Object = MibTableColumn
gnGenXBytesCorrected = _GnGenXBytesCorrected_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 23, 1, 30),
    _GnGenXBytesCorrected_Type()
)
gnGenXBytesCorrected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnGenXBytesCorrected.setStatus("mandatory")


class _GnGenXPrbsTest_Type(Integer32):
    """Custom type gnGenXPrbsTest based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 3),
          ("notActive", 2))
    )


_GnGenXPrbsTest_Type.__name__ = "Integer32"
_GnGenXPrbsTest_Object = MibTableColumn
gnGenXPrbsTest = _GnGenXPrbsTest_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 23, 1, 31),
    _GnGenXPrbsTest_Type()
)
gnGenXPrbsTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnGenXPrbsTest.setStatus("mandatory")


class _GnGenXClearCounters_Type(Integer32):
    """Custom type gnGenXClearCounters based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clearCounters", 3),
          ("noAction", 2))
    )


_GnGenXClearCounters_Type.__name__ = "Integer32"
_GnGenXClearCounters_Object = MibTableColumn
gnGenXClearCounters = _GnGenXClearCounters_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 23, 1, 32),
    _GnGenXClearCounters_Type()
)
gnGenXClearCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnGenXClearCounters.setStatus("mandatory")


class _GnGenXMuxLicense_Type(OctetString):
    """Custom type gnGenXMuxLicense based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_GnGenXMuxLicense_Type.__name__ = "OctetString"
_GnGenXMuxLicense_Object = MibTableColumn
gnGenXMuxLicense = _GnGenXMuxLicense_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 23, 1, 33),
    _GnGenXMuxLicense_Type()
)
gnGenXMuxLicense.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnGenXMuxLicense.setStatus("mandatory")


class _GnGenAddAlarmExtToTraps_Type(Integer32):
    """Custom type gnGenAddAlarmExtToTraps based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 3))
    )


_GnGenAddAlarmExtToTraps_Type.__name__ = "Integer32"
_GnGenAddAlarmExtToTraps_Object = MibScalar
gnGenAddAlarmExtToTraps = _GnGenAddAlarmExtToTraps_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 24),
    _GnGenAddAlarmExtToTraps_Type()
)
gnGenAddAlarmExtToTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnGenAddAlarmExtToTraps.setStatus("mandatory")


class _GnGenFeatureSupport_Type(OctetString):
    """Custom type gnGenFeatureSupport based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_GnGenFeatureSupport_Type.__name__ = "OctetString"
_GnGenFeatureSupport_Object = MibScalar
gnGenFeatureSupport = _GnGenFeatureSupport_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 25),
    _GnGenFeatureSupport_Type()
)
gnGenFeatureSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnGenFeatureSupport.setStatus("mandatory")
_GnGeneralMrmcXTable_Object = MibTable
gnGeneralMrmcXTable = _GnGeneralMrmcXTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 26)
)
if mibBuilder.loadTexts:
    gnGeneralMrmcXTable.setStatus("mandatory")
_GnGeneralMrmcXEntry_Object = MibTableRow
gnGeneralMrmcXEntry = _GnGeneralMrmcXEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 26, 1)
)
gnGeneralMrmcXEntry.setIndexNames(
    (0, "CERAGON-MIB", "gnGenMrmcXId"),
    (0, "CERAGON-MIB", "gnGenMrmcXMrmcVal"),
)
if mibBuilder.loadTexts:
    gnGeneralMrmcXEntry.setStatus("mandatory")


class _GnGenMrmcXId_Type(Integer32):
    """Custom type gnGenMrmcXId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("drawer1", 3),
          ("drawer2", 4))
    )


_GnGenMrmcXId_Type.__name__ = "Integer32"
_GnGenMrmcXId_Object = MibTableColumn
gnGenMrmcXId = _GnGenMrmcXId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 26, 1, 1),
    _GnGenMrmcXId_Type()
)
gnGenMrmcXId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnGenMrmcXId.setStatus("mandatory")
_GnGenMrmcXMrmcVal_Type = Integer32
_GnGenMrmcXMrmcVal_Object = MibTableColumn
gnGenMrmcXMrmcVal = _GnGenMrmcXMrmcVal_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 26, 1, 2),
    _GnGenMrmcXMrmcVal_Type()
)
gnGenMrmcXMrmcVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnGenMrmcXMrmcVal.setStatus("mandatory")
_GnGenMrmcXBitRate_Type = Integer32
_GnGenMrmcXBitRate_Object = MibTableColumn
gnGenMrmcXBitRate = _GnGenMrmcXBitRate_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 26, 1, 3),
    _GnGenMrmcXBitRate_Type()
)
gnGenMrmcXBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnGenMrmcXBitRate.setStatus("mandatory")
_GnGenMrmcXBandWidth_Type = Integer32
_GnGenMrmcXBandWidth_Object = MibTableColumn
gnGenMrmcXBandWidth = _GnGenMrmcXBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 26, 1, 4),
    _GnGenMrmcXBandWidth_Type()
)
gnGenMrmcXBandWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnGenMrmcXBandWidth.setStatus("mandatory")
_GnGenMrmcXQam_Type = Integer32
_GnGenMrmcXQam_Object = MibTableColumn
gnGenMrmcXQam = _GnGenMrmcXQam_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 26, 1, 5),
    _GnGenMrmcXQam_Type()
)
gnGenMrmcXQam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnGenMrmcXQam.setStatus("mandatory")


class _GnGenMrmcXScriptType_Type(Integer32):
    """Custom type gnGenMrmcXScriptType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("v1", 2),
          ("v2", 3))
    )


_GnGenMrmcXScriptType_Type.__name__ = "Integer32"
_GnGenMrmcXScriptType_Object = MibTableColumn
gnGenMrmcXScriptType = _GnGenMrmcXScriptType_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 26, 1, 6),
    _GnGenMrmcXScriptType_Type()
)
gnGenMrmcXScriptType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnGenMrmcXScriptType.setStatus("mandatory")
_GnGenDrawerXTable_Object = MibTable
gnGenDrawerXTable = _GnGenDrawerXTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 27)
)
if mibBuilder.loadTexts:
    gnGenDrawerXTable.setStatus("mandatory")
_GnGenDrawerXEntry_Object = MibTableRow
gnGenDrawerXEntry = _GnGenDrawerXEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 27, 1)
)
gnGenDrawerXEntry.setIndexNames(
    (0, "CERAGON-MIB", "gnGenDrawerXId"),
)
if mibBuilder.loadTexts:
    gnGenDrawerXEntry.setStatus("mandatory")


class _GnGenDrawerXId_Type(Integer32):
    """Custom type gnGenDrawerXId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("drawer1", 3),
          ("drawer2", 4))
    )


_GnGenDrawerXId_Type.__name__ = "Integer32"
_GnGenDrawerXId_Object = MibTableColumn
gnGenDrawerXId = _GnGenDrawerXId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 27, 1, 1),
    _GnGenDrawerXId_Type()
)
gnGenDrawerXId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnGenDrawerXId.setStatus("mandatory")


class _GnGenDrawerXName_Type(DisplayString):
    """Custom type gnGenDrawerXName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_GnGenDrawerXName_Type.__name__ = "DisplayString"
_GnGenDrawerXName_Object = MibTableColumn
gnGenDrawerXName = _GnGenDrawerXName_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 27, 1, 2),
    _GnGenDrawerXName_Type()
)
gnGenDrawerXName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnGenDrawerXName.setStatus("mandatory")


class _GnGenDrawerXSlot1Status_Type(Integer32):
    """Custom type gnGenDrawerXSlot1Status based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("dbReady", 5),
          ("notExist", 2),
          ("powerOff", 3),
          ("powerOn", 4))
    )


_GnGenDrawerXSlot1Status_Type.__name__ = "Integer32"
_GnGenDrawerXSlot1Status_Object = MibTableColumn
gnGenDrawerXSlot1Status = _GnGenDrawerXSlot1Status_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 27, 1, 3),
    _GnGenDrawerXSlot1Status_Type()
)
gnGenDrawerXSlot1Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnGenDrawerXSlot1Status.setStatus("mandatory")


class _GnGenDrawerXSlot2Status_Type(Integer32):
    """Custom type gnGenDrawerXSlot2Status based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("dbReady", 5),
          ("notExist", 2),
          ("powerOff", 3),
          ("powerOn", 4))
    )


_GnGenDrawerXSlot2Status_Type.__name__ = "Integer32"
_GnGenDrawerXSlot2Status_Object = MibTableColumn
gnGenDrawerXSlot2Status = _GnGenDrawerXSlot2Status_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 27, 1, 4),
    _GnGenDrawerXSlot2Status_Type()
)
gnGenDrawerXSlot2Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnGenDrawerXSlot2Status.setStatus("mandatory")


class _GnGenDrawerXDeviceLeds_Type(OctetString):
    """Custom type gnGenDrawerXDeviceLeds based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_GnGenDrawerXDeviceLeds_Type.__name__ = "OctetString"
_GnGenDrawerXDeviceLeds_Object = MibTableColumn
gnGenDrawerXDeviceLeds = _GnGenDrawerXDeviceLeds_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 27, 1, 5),
    _GnGenDrawerXDeviceLeds_Type()
)
gnGenDrawerXDeviceLeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnGenDrawerXDeviceLeds.setStatus("mandatory")


class _GnGenDrawerXInternalCommunication_Type(OctetString):
    """Custom type gnGenDrawerXInternalCommunication based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_GnGenDrawerXInternalCommunication_Type.__name__ = "OctetString"
_GnGenDrawerXInternalCommunication_Object = MibTableColumn
gnGenDrawerXInternalCommunication = _GnGenDrawerXInternalCommunication_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 27, 1, 6),
    _GnGenDrawerXInternalCommunication_Type()
)
gnGenDrawerXInternalCommunication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnGenDrawerXInternalCommunication.setStatus("mandatory")


class _GnGenDrawerXDeviceIDUStatus_Type(OctetString):
    """Custom type gnGenDrawerXDeviceIDUStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_GnGenDrawerXDeviceIDUStatus_Type.__name__ = "OctetString"
_GnGenDrawerXDeviceIDUStatus_Object = MibTableColumn
gnGenDrawerXDeviceIDUStatus = _GnGenDrawerXDeviceIDUStatus_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 27, 1, 7),
    _GnGenDrawerXDeviceIDUStatus_Type()
)
gnGenDrawerXDeviceIDUStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnGenDrawerXDeviceIDUStatus.setStatus("mandatory")
_GnCluster_ObjectIdentity = ObjectIdentity
gnCluster = _GnCluster_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 28)
)
_Cluster_ObjectIdentity = ObjectIdentity
cluster = _Cluster_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 28, 1)
)


class _ClusterSystemType_Type(Integer32):
    """Custom type clusterSystemType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("p1500", 3),
          ("t3200", 4),
          ("unknown", 2))
    )


_ClusterSystemType_Type.__name__ = "Integer32"
_ClusterSystemType_Object = MibScalar
clusterSystemType = _ClusterSystemType_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 28, 1, 1),
    _ClusterSystemType_Type()
)
clusterSystemType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterSystemType.setStatus("mandatory")


class _ClusterNumOfSubRacks_Type(Integer32):
    """Custom type clusterNumOfSubRacks based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_ClusterNumOfSubRacks_Type.__name__ = "Integer32"
_ClusterNumOfSubRacks_Object = MibScalar
clusterNumOfSubRacks = _ClusterNumOfSubRacks_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 28, 1, 3),
    _ClusterNumOfSubRacks_Type()
)
clusterNumOfSubRacks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterNumOfSubRacks.setStatus("mandatory")


class _ClusterSubRackNum_Type(Integer32):
    """Custom type clusterSubRackNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_ClusterSubRackNum_Type.__name__ = "Integer32"
_ClusterSubRackNum_Object = MibScalar
clusterSubRackNum = _ClusterSubRackNum_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 28, 1, 4),
    _ClusterSubRackNum_Type()
)
clusterSubRackNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterSubRackNum.setStatus("mandatory")


class _ClusterFloorNum_Type(Integer32):
    """Custom type clusterFloorNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_ClusterFloorNum_Type.__name__ = "Integer32"
_ClusterFloorNum_Object = MibScalar
clusterFloorNum = _ClusterFloorNum_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 28, 1, 5),
    _ClusterFloorNum_Type()
)
clusterFloorNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterFloorNum.setStatus("mandatory")
_ClusterIPBase_Type = IpAddress
_ClusterIPBase_Object = MibScalar
clusterIPBase = _ClusterIPBase_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 28, 1, 6),
    _ClusterIPBase_Type()
)
clusterIPBase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterIPBase.setStatus("mandatory")


class _ClusterIDCRole_Type(Integer32):
    """Custom type clusterIDCRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("clusterPrime", 2),
          ("member", 3),
          ("subrackManager", 4))
    )


_ClusterIDCRole_Type.__name__ = "Integer32"
_ClusterIDCRole_Object = MibScalar
clusterIDCRole = _ClusterIDCRole_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 28, 1, 7),
    _ClusterIDCRole_Type()
)
clusterIDCRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterIDCRole.setStatus("mandatory")
_ClusterPrimeIPAddress_Type = IpAddress
_ClusterPrimeIPAddress_Object = MibScalar
clusterPrimeIPAddress = _ClusterPrimeIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 28, 1, 8),
    _ClusterPrimeIPAddress_Type()
)
clusterPrimeIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterPrimeIPAddress.setStatus("mandatory")
_ClusterPeerIPLastChangeTime_Type = Integer32
_ClusterPeerIPLastChangeTime_Object = MibScalar
clusterPeerIPLastChangeTime = _ClusterPeerIPLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 28, 1, 9),
    _ClusterPeerIPLastChangeTime_Type()
)
clusterPeerIPLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterPeerIPLastChangeTime.setStatus("mandatory")
_AddressesTable_Object = MibTable
addressesTable = _AddressesTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 28, 2)
)
if mibBuilder.loadTexts:
    addressesTable.setStatus("mandatory")
_AddressesEntry_Object = MibTableRow
addressesEntry = _AddressesEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 28, 2, 1)
)
addressesEntry.setIndexNames(
    (0, "CERAGON-MIB", "addressesPeerIPId"),
)
if mibBuilder.loadTexts:
    addressesEntry.setStatus("mandatory")


class _AddressesPeerIPId_Type(Integer32):
    """Custom type addressesPeerIPId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_AddressesPeerIPId_Type.__name__ = "Integer32"
_AddressesPeerIPId_Object = MibTableColumn
addressesPeerIPId = _AddressesPeerIPId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 28, 2, 1, 1),
    _AddressesPeerIPId_Type()
)
addressesPeerIPId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    addressesPeerIPId.setStatus("mandatory")
_AddressesPeerIPAddress_Type = IpAddress
_AddressesPeerIPAddress_Object = MibTableColumn
addressesPeerIPAddress = _AddressesPeerIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 28, 2, 1, 2),
    _AddressesPeerIPAddress_Type()
)
addressesPeerIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    addressesPeerIPAddress.setStatus("mandatory")
_PrimeIDC_ObjectIdentity = ObjectIdentity
primeIDC = _PrimeIDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 28, 3)
)


class _PrimeIDCAutoInternalClockDistribution_Type(Integer32):
    """Custom type primeIDCAutoInternalClockDistribution based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("enable", 2))
    )


_PrimeIDCAutoInternalClockDistribution_Type.__name__ = "Integer32"
_PrimeIDCAutoInternalClockDistribution_Object = MibScalar
primeIDCAutoInternalClockDistribution = _PrimeIDCAutoInternalClockDistribution_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 28, 3, 1),
    _PrimeIDCAutoInternalClockDistribution_Type()
)
primeIDCAutoInternalClockDistribution.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    primeIDCAutoInternalClockDistribution.setStatus("mandatory")


class _PrimeIDCSynchronizeClockInCluster_Type(Integer32):
    """Custom type primeIDCSynchronizeClockInCluster based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noaction", 2),
          ("synchronize", 3))
    )


_PrimeIDCSynchronizeClockInCluster_Type.__name__ = "Integer32"
_PrimeIDCSynchronizeClockInCluster_Object = MibScalar
primeIDCSynchronizeClockInCluster = _PrimeIDCSynchronizeClockInCluster_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 28, 3, 2),
    _PrimeIDCSynchronizeClockInCluster_Type()
)
primeIDCSynchronizeClockInCluster.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    primeIDCSynchronizeClockInCluster.setStatus("mandatory")
_BackplaneSlotMappingTable_Object = MibTable
backplaneSlotMappingTable = _BackplaneSlotMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 28, 4)
)
if mibBuilder.loadTexts:
    backplaneSlotMappingTable.setStatus("mandatory")
_BackplaneSlotMappingEntry_Object = MibTableRow
backplaneSlotMappingEntry = _BackplaneSlotMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 28, 4, 1)
)
backplaneSlotMappingEntry.setIndexNames(
    (0, "CERAGON-MIB", "backplaneSlotMappingSubrackId"),
    (0, "CERAGON-MIB", "backplaneSlotMappingFloorId"),
    (0, "CERAGON-MIB", "backplaneSlotMappingDrawerId"),
    (0, "CERAGON-MIB", "backplaneSlotMappingSubDrawerId"),
)
if mibBuilder.loadTexts:
    backplaneSlotMappingEntry.setStatus("mandatory")


class _BackplaneSlotMappingSubrackId_Type(Integer32):
    """Custom type backplaneSlotMappingSubrackId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_BackplaneSlotMappingSubrackId_Type.__name__ = "Integer32"
_BackplaneSlotMappingSubrackId_Object = MibTableColumn
backplaneSlotMappingSubrackId = _BackplaneSlotMappingSubrackId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 28, 4, 1, 1),
    _BackplaneSlotMappingSubrackId_Type()
)
backplaneSlotMappingSubrackId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    backplaneSlotMappingSubrackId.setStatus("mandatory")


class _BackplaneSlotMappingFloorId_Type(Integer32):
    """Custom type backplaneSlotMappingFloorId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_BackplaneSlotMappingFloorId_Type.__name__ = "Integer32"
_BackplaneSlotMappingFloorId_Object = MibTableColumn
backplaneSlotMappingFloorId = _BackplaneSlotMappingFloorId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 28, 4, 1, 2),
    _BackplaneSlotMappingFloorId_Type()
)
backplaneSlotMappingFloorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    backplaneSlotMappingFloorId.setStatus("mandatory")


class _BackplaneSlotMappingDrawerId_Type(Integer32):
    """Custom type backplaneSlotMappingDrawerId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_BackplaneSlotMappingDrawerId_Type.__name__ = "Integer32"
_BackplaneSlotMappingDrawerId_Object = MibTableColumn
backplaneSlotMappingDrawerId = _BackplaneSlotMappingDrawerId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 28, 4, 1, 3),
    _BackplaneSlotMappingDrawerId_Type()
)
backplaneSlotMappingDrawerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    backplaneSlotMappingDrawerId.setStatus("mandatory")


class _BackplaneSlotMappingSubDrawerId_Type(Integer32):
    """Custom type backplaneSlotMappingSubDrawerId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_BackplaneSlotMappingSubDrawerId_Type.__name__ = "Integer32"
_BackplaneSlotMappingSubDrawerId_Object = MibTableColumn
backplaneSlotMappingSubDrawerId = _BackplaneSlotMappingSubDrawerId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 28, 4, 1, 4),
    _BackplaneSlotMappingSubDrawerId_Type()
)
backplaneSlotMappingSubDrawerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    backplaneSlotMappingSubDrawerId.setStatus("mandatory")


class _BackplaneSlotMappingUnitType_Type(Integer32):
    """Custom type backplaneSlotMappingUnitType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
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
        *(("auxInterface", 10),
          ("drawer", 6),
          ("idc", 2),
          ("modem", 5),
          ("mux", 4),
          ("none", 8),
          ("odu", 3),
          ("power", 11),
          ("unknown", 7),
          ("xc", 9))
    )


_BackplaneSlotMappingUnitType_Type.__name__ = "Integer32"
_BackplaneSlotMappingUnitType_Object = MibTableColumn
backplaneSlotMappingUnitType = _BackplaneSlotMappingUnitType_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 28, 4, 1, 5),
    _BackplaneSlotMappingUnitType_Type()
)
backplaneSlotMappingUnitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    backplaneSlotMappingUnitType.setStatus("mandatory")


class _BackplaneSlotMappingUnitNumber_Type(Integer32):
    """Custom type backplaneSlotMappingUnitNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_BackplaneSlotMappingUnitNumber_Type.__name__ = "Integer32"
_BackplaneSlotMappingUnitNumber_Object = MibTableColumn
backplaneSlotMappingUnitNumber = _BackplaneSlotMappingUnitNumber_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 28, 4, 1, 6),
    _BackplaneSlotMappingUnitNumber_Type()
)
backplaneSlotMappingUnitNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    backplaneSlotMappingUnitNumber.setStatus("mandatory")
_BackplaneSlotMappingUnitIndex_Type = Integer32
_BackplaneSlotMappingUnitIndex_Object = MibTableColumn
backplaneSlotMappingUnitIndex = _BackplaneSlotMappingUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 28, 4, 1, 7),
    _BackplaneSlotMappingUnitIndex_Type()
)
backplaneSlotMappingUnitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    backplaneSlotMappingUnitIndex.setStatus("mandatory")
_GnSubrack_ObjectIdentity = ObjectIdentity
gnSubrack = _GnSubrack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 29)
)
_PowerInputTable_Object = MibTable
powerInputTable = _PowerInputTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 29, 1)
)
if mibBuilder.loadTexts:
    powerInputTable.setStatus("mandatory")
_PowerInputEntry_Object = MibTableRow
powerInputEntry = _PowerInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 29, 1, 1)
)
powerInputEntry.setIndexNames(
    (0, "CERAGON-MIB", "powerInputId"),
)
if mibBuilder.loadTexts:
    powerInputEntry.setStatus("mandatory")


class _PowerInputId_Type(Integer32):
    """Custom type powerInputId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_PowerInputId_Type.__name__ = "Integer32"
_PowerInputId_Object = MibTableColumn
powerInputId = _PowerInputId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 29, 1, 1, 1),
    _PowerInputId_Type()
)
powerInputId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerInputId.setStatus("mandatory")


class _PowerInputAdmin_Type(Integer32):
    """Custom type powerInputAdmin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("enable", 2))
    )


_PowerInputAdmin_Type.__name__ = "Integer32"
_PowerInputAdmin_Object = MibTableColumn
powerInputAdmin = _PowerInputAdmin_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 29, 1, 1, 2),
    _PowerInputAdmin_Type()
)
powerInputAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    powerInputAdmin.setStatus("mandatory")


class _PowerInputStatus_Type(Integer32):
    """Custom type powerInputStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("down", 4),
          ("notexist", 2),
          ("unknown", 3),
          ("up", 5))
    )


_PowerInputStatus_Type.__name__ = "Integer32"
_PowerInputStatus_Object = MibTableColumn
powerInputStatus = _PowerInputStatus_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 29, 1, 1, 3),
    _PowerInputStatus_Type()
)
powerInputStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerInputStatus.setStatus("mandatory")


class _PowerInputLedStatus_Type(OctetString):
    """Custom type powerInputLedStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_PowerInputLedStatus_Type.__name__ = "OctetString"
_PowerInputLedStatus_Object = MibTableColumn
powerInputLedStatus = _PowerInputLedStatus_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 29, 1, 1, 4),
    _PowerInputLedStatus_Type()
)
powerInputLedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerInputLedStatus.setStatus("mandatory")
_AuxiliaryDrawer_ObjectIdentity = ObjectIdentity
auxiliaryDrawer = _AuxiliaryDrawer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 29, 2)
)


class _AuxiliaryDrawerAuxCardType_Type(Integer32):
    """Custom type auxiliaryDrawerAuxCardType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("na", 2),
          ("v1", 3))
    )


_AuxiliaryDrawerAuxCardType_Type.__name__ = "Integer32"
_AuxiliaryDrawerAuxCardType_Object = MibScalar
auxiliaryDrawerAuxCardType = _AuxiliaryDrawerAuxCardType_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 29, 2, 1),
    _AuxiliaryDrawerAuxCardType_Type()
)
auxiliaryDrawerAuxCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxiliaryDrawerAuxCardType.setStatus("mandatory")


class _AuxiliaryDrawerLedsStatus_Type(OctetString):
    """Custom type auxiliaryDrawerLedsStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_AuxiliaryDrawerLedsStatus_Type.__name__ = "OctetString"
_AuxiliaryDrawerLedsStatus_Object = MibScalar
auxiliaryDrawerLedsStatus = _AuxiliaryDrawerLedsStatus_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 29, 2, 2),
    _AuxiliaryDrawerLedsStatus_Type()
)
auxiliaryDrawerLedsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxiliaryDrawerLedsStatus.setStatus("mandatory")
_AuxiliaryDrawerBoardHWVersion_Type = Integer32
_AuxiliaryDrawerBoardHWVersion_Object = MibScalar
auxiliaryDrawerBoardHWVersion = _AuxiliaryDrawerBoardHWVersion_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 29, 2, 3),
    _AuxiliaryDrawerBoardHWVersion_Type()
)
auxiliaryDrawerBoardHWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxiliaryDrawerBoardHWVersion.setStatus("mandatory")


class _AuxiliaryDrawerBoardFWVersion_Type(DisplayString):
    """Custom type auxiliaryDrawerBoardFWVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_AuxiliaryDrawerBoardFWVersion_Type.__name__ = "DisplayString"
_AuxiliaryDrawerBoardFWVersion_Object = MibScalar
auxiliaryDrawerBoardFWVersion = _AuxiliaryDrawerBoardFWVersion_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 29, 2, 4),
    _AuxiliaryDrawerBoardFWVersion_Type()
)
auxiliaryDrawerBoardFWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxiliaryDrawerBoardFWVersion.setStatus("mandatory")


class _AuxiliaryDrawerBoardPostResetFWVersion_Type(DisplayString):
    """Custom type auxiliaryDrawerBoardPostResetFWVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_AuxiliaryDrawerBoardPostResetFWVersion_Type.__name__ = "DisplayString"
_AuxiliaryDrawerBoardPostResetFWVersion_Object = MibScalar
auxiliaryDrawerBoardPostResetFWVersion = _AuxiliaryDrawerBoardPostResetFWVersion_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 29, 2, 5),
    _AuxiliaryDrawerBoardPostResetFWVersion_Type()
)
auxiliaryDrawerBoardPostResetFWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxiliaryDrawerBoardPostResetFWVersion.setStatus("mandatory")


class _AuxiliaryDrawerSerialNumber_Type(DisplayString):
    """Custom type auxiliaryDrawerSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_AuxiliaryDrawerSerialNumber_Type.__name__ = "DisplayString"
_AuxiliaryDrawerSerialNumber_Object = MibScalar
auxiliaryDrawerSerialNumber = _AuxiliaryDrawerSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 29, 2, 6),
    _AuxiliaryDrawerSerialNumber_Type()
)
auxiliaryDrawerSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxiliaryDrawerSerialNumber.setStatus("mandatory")


class _AuxiliaryDrawerBoardReset_Type(Integer32):
    """Custom type auxiliaryDrawerBoardReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noaction", 2),
          ("reset", 3))
    )


_AuxiliaryDrawerBoardReset_Type.__name__ = "Integer32"
_AuxiliaryDrawerBoardReset_Object = MibScalar
auxiliaryDrawerBoardReset = _AuxiliaryDrawerBoardReset_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 29, 2, 7),
    _AuxiliaryDrawerBoardReset_Type()
)
auxiliaryDrawerBoardReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    auxiliaryDrawerBoardReset.setStatus("mandatory")


class _AuxiliaryDrawerOrderWireCascading_Type(Integer32):
    """Custom type auxiliaryDrawerOrderWireCascading based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("enable", 2))
    )


_AuxiliaryDrawerOrderWireCascading_Type.__name__ = "Integer32"
_AuxiliaryDrawerOrderWireCascading_Object = MibScalar
auxiliaryDrawerOrderWireCascading = _AuxiliaryDrawerOrderWireCascading_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 29, 2, 8),
    _AuxiliaryDrawerOrderWireCascading_Type()
)
auxiliaryDrawerOrderWireCascading.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    auxiliaryDrawerOrderWireCascading.setStatus("mandatory")
_XcDrawerTable_Object = MibTable
xcDrawerTable = _XcDrawerTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 29, 3)
)
if mibBuilder.loadTexts:
    xcDrawerTable.setStatus("mandatory")
_XcDrawerEntry_Object = MibTableRow
xcDrawerEntry = _XcDrawerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 29, 3, 1)
)
xcDrawerEntry.setIndexNames(
    (0, "CERAGON-MIB", "xcDrawerXCId"),
)
if mibBuilder.loadTexts:
    xcDrawerEntry.setStatus("mandatory")


class _XcDrawerXCId_Type(Integer32):
    """Custom type xcDrawerXCId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_XcDrawerXCId_Type.__name__ = "Integer32"
_XcDrawerXCId_Object = MibTableColumn
xcDrawerXCId = _XcDrawerXCId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 29, 3, 1, 1),
    _XcDrawerXCId_Type()
)
xcDrawerXCId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcDrawerXCId.setStatus("mandatory")


class _XcDrawerLedsStatus_Type(OctetString):
    """Custom type xcDrawerLedsStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_XcDrawerLedsStatus_Type.__name__ = "OctetString"
_XcDrawerLedsStatus_Object = MibTableColumn
xcDrawerLedsStatus = _XcDrawerLedsStatus_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 29, 3, 1, 2),
    _XcDrawerLedsStatus_Type()
)
xcDrawerLedsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcDrawerLedsStatus.setStatus("mandatory")
_XcDrawerBoardHWVersion_Type = Integer32
_XcDrawerBoardHWVersion_Object = MibTableColumn
xcDrawerBoardHWVersion = _XcDrawerBoardHWVersion_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 29, 3, 1, 3),
    _XcDrawerBoardHWVersion_Type()
)
xcDrawerBoardHWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcDrawerBoardHWVersion.setStatus("mandatory")


class _XcDrawerBoardFWVersion_Type(DisplayString):
    """Custom type xcDrawerBoardFWVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_XcDrawerBoardFWVersion_Type.__name__ = "DisplayString"
_XcDrawerBoardFWVersion_Object = MibTableColumn
xcDrawerBoardFWVersion = _XcDrawerBoardFWVersion_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 29, 3, 1, 4),
    _XcDrawerBoardFWVersion_Type()
)
xcDrawerBoardFWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcDrawerBoardFWVersion.setStatus("mandatory")


class _XcDrawerBoardPostResetFWVersion_Type(DisplayString):
    """Custom type xcDrawerBoardPostResetFWVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_XcDrawerBoardPostResetFWVersion_Type.__name__ = "DisplayString"
_XcDrawerBoardPostResetFWVersion_Object = MibTableColumn
xcDrawerBoardPostResetFWVersion = _XcDrawerBoardPostResetFWVersion_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 29, 3, 1, 5),
    _XcDrawerBoardPostResetFWVersion_Type()
)
xcDrawerBoardPostResetFWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcDrawerBoardPostResetFWVersion.setStatus("mandatory")


class _XcDrawerSerialNumber_Type(DisplayString):
    """Custom type xcDrawerSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_XcDrawerSerialNumber_Type.__name__ = "DisplayString"
_XcDrawerSerialNumber_Object = MibTableColumn
xcDrawerSerialNumber = _XcDrawerSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 29, 3, 1, 6),
    _XcDrawerSerialNumber_Type()
)
xcDrawerSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcDrawerSerialNumber.setStatus("mandatory")


class _XcDrawerResetXCBoard_Type(Integer32):
    """Custom type xcDrawerResetXCBoard based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noaction", 2),
          ("reset", 3))
    )


_XcDrawerResetXCBoard_Type.__name__ = "Integer32"
_XcDrawerResetXCBoard_Object = MibTableColumn
xcDrawerResetXCBoard = _XcDrawerResetXCBoard_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 29, 3, 1, 7),
    _XcDrawerResetXCBoard_Type()
)
xcDrawerResetXCBoard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xcDrawerResetXCBoard.setStatus("mandatory")


class _XcDrawerXCSelfTestResult_Type(Integer32):
    """Custom type xcDrawerXCSelfTestResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failed", 3),
          ("passed", 2))
    )


_XcDrawerXCSelfTestResult_Type.__name__ = "Integer32"
_XcDrawerXCSelfTestResult_Object = MibTableColumn
xcDrawerXCSelfTestResult = _XcDrawerXCSelfTestResult_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 29, 3, 1, 8),
    _XcDrawerXCSelfTestResult_Type()
)
xcDrawerXCSelfTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcDrawerXCSelfTestResult.setStatus("mandatory")


class _XcDrawerXCActivityRole_Type(Integer32):
    """Custom type xcDrawerXCActivityRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("standby", 3))
    )


_XcDrawerXCActivityRole_Type.__name__ = "Integer32"
_XcDrawerXCActivityRole_Object = MibTableColumn
xcDrawerXCActivityRole = _XcDrawerXCActivityRole_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 29, 3, 1, 9),
    _XcDrawerXCActivityRole_Type()
)
xcDrawerXCActivityRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcDrawerXCActivityRole.setStatus("mandatory")


class _XcDrawerSyncIdcDataBase_Type(Integer32):
    """Custom type xcDrawerSyncIdcDataBase based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("idcToXC", 3),
          ("noOperation", 2),
          ("xcToIdc", 4))
    )


_XcDrawerSyncIdcDataBase_Type.__name__ = "Integer32"
_XcDrawerSyncIdcDataBase_Object = MibTableColumn
xcDrawerSyncIdcDataBase = _XcDrawerSyncIdcDataBase_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 29, 3, 1, 10),
    _XcDrawerSyncIdcDataBase_Type()
)
xcDrawerSyncIdcDataBase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xcDrawerSyncIdcDataBase.setStatus("mandatory")


class _XcDrawerXCConnector_Type(Integer32):
    """Custom type xcDrawerXCConnector based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            2
        )
    )
    namedValues = NamedValues(
        ("oneStm1XC", 2)
    )


_XcDrawerXCConnector_Type.__name__ = "Integer32"
_XcDrawerXCConnector_Object = MibTableColumn
xcDrawerXCConnector = _XcDrawerXCConnector_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 29, 3, 1, 11),
    _XcDrawerXCConnector_Type()
)
xcDrawerXCConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xcDrawerXCConnector.setStatus("mandatory")
_GnGenCarrierXTable_Object = MibTable
gnGenCarrierXTable = _GnGenCarrierXTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 30)
)
if mibBuilder.loadTexts:
    gnGenCarrierXTable.setStatus("mandatory")
_GnGenCarrierXEntry_Object = MibTableRow
gnGenCarrierXEntry = _GnGenCarrierXEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 30, 1)
)
gnGenCarrierXEntry.setIndexNames(
    (0, "CERAGON-MIB", "gnGenCarrierXId"),
)
if mibBuilder.loadTexts:
    gnGenCarrierXEntry.setStatus("mandatory")


class _GnGenCarrierXId_Type(Integer32):
    """Custom type gnGenCarrierXId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("carrier1", 3),
          ("carrier2", 4))
    )


_GnGenCarrierXId_Type.__name__ = "Integer32"
_GnGenCarrierXId_Object = MibTableColumn
gnGenCarrierXId = _GnGenCarrierXId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 30, 1, 1),
    _GnGenCarrierXId_Type()
)
gnGenCarrierXId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnGenCarrierXId.setStatus("mandatory")


class _GnGenCarrierXResetPerfMon_Type(Integer32):
    """Custom type gnGenCarrierXResetPerfMon based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 3),
          ("reset", 2))
    )


_GnGenCarrierXResetPerfMon_Type.__name__ = "Integer32"
_GnGenCarrierXResetPerfMon_Object = MibTableColumn
gnGenCarrierXResetPerfMon = _GnGenCarrierXResetPerfMon_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 30, 1, 2),
    _GnGenCarrierXResetPerfMon_Type()
)
gnGenCarrierXResetPerfMon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnGenCarrierXResetPerfMon.setStatus("mandatory")


class _GnGenCarrierXSyncIdcDataBase_Type(Integer32):
    """Custom type gnGenCarrierXSyncIdcDataBase based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("drawerToIdc", 4),
          ("idcToAllDrawers", 5),
          ("idcToDrawer", 3),
          ("noOperation", 2))
    )


_GnGenCarrierXSyncIdcDataBase_Type.__name__ = "Integer32"
_GnGenCarrierXSyncIdcDataBase_Object = MibTableColumn
gnGenCarrierXSyncIdcDataBase = _GnGenCarrierXSyncIdcDataBase_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 1, 30, 1, 3),
    _GnGenCarrierXSyncIdcDataBase_Type()
)
gnGenCarrierXSyncIdcDataBase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnGenCarrierXSyncIdcDataBase.setStatus("mandatory")
_GnAgn_ObjectIdentity = ObjectIdentity
gnAgn = _GnAgn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2)
)
_GnAgnMgrTable_Object = MibTable
gnAgnMgrTable = _GnAgnMgrTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 1)
)
if mibBuilder.loadTexts:
    gnAgnMgrTable.setStatus("mandatory")
_GnAgnMgrEntry_Object = MibTableRow
gnAgnMgrEntry = _GnAgnMgrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 1, 1)
)
gnAgnMgrEntry.setIndexNames(
    (0, "CERAGON-MIB", "gnAgnMgrId"),
)
if mibBuilder.loadTexts:
    gnAgnMgrEntry.setStatus("mandatory")
_GnAgnMgrId_Type = Integer32
_GnAgnMgrId_Object = MibTableColumn
gnAgnMgrId = _GnAgnMgrId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 1, 1, 1),
    _GnAgnMgrId_Type()
)
gnAgnMgrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnAgnMgrId.setStatus("mandatory")
_GnAgnMgrIP_Type = IpAddress
_GnAgnMgrIP_Object = MibTableColumn
gnAgnMgrIP = _GnAgnMgrIP_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 1, 1, 2),
    _GnAgnMgrIP_Type()
)
gnAgnMgrIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnAgnMgrIP.setStatus("mandatory")


class _GnAgnMgrAlarmGroupMask_Type(OctetString):
    """Custom type gnAgnMgrAlarmGroupMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_GnAgnMgrAlarmGroupMask_Type.__name__ = "OctetString"
_GnAgnMgrAlarmGroupMask_Object = MibTableColumn
gnAgnMgrAlarmGroupMask = _GnAgnMgrAlarmGroupMask_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 1, 1, 3),
    _GnAgnMgrAlarmGroupMask_Type()
)
gnAgnMgrAlarmGroupMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnAgnMgrAlarmGroupMask.setStatus("mandatory")


class _GnAgnMgrSeverityFilter_Type(OctetString):
    """Custom type gnAgnMgrSeverityFilter based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_GnAgnMgrSeverityFilter_Type.__name__ = "OctetString"
_GnAgnMgrSeverityFilter_Object = MibTableColumn
gnAgnMgrSeverityFilter = _GnAgnMgrSeverityFilter_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 1, 1, 4),
    _GnAgnMgrSeverityFilter_Type()
)
gnAgnMgrSeverityFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnAgnMgrSeverityFilter.setStatus("mandatory")


class _GnAgnMgrTrapPort_Type(Integer32):
    """Custom type gnAgnMgrTrapPort based on Integer32"""
    defaultValue = 162

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(70, 65535),
    )


_GnAgnMgrTrapPort_Type.__name__ = "Integer32"
_GnAgnMgrTrapPort_Object = MibTableColumn
gnAgnMgrTrapPort = _GnAgnMgrTrapPort_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 1, 1, 5),
    _GnAgnMgrTrapPort_Type()
)
gnAgnMgrTrapPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnAgnMgrTrapPort.setStatus("mandatory")
_GnAgnLogFileData_ObjectIdentity = ObjectIdentity
gnAgnLogFileData = _GnAgnLogFileData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 2)
)
_GnAgnLogFileMaxEntries_Type = Integer32
_GnAgnLogFileMaxEntries_Object = MibScalar
gnAgnLogFileMaxEntries = _GnAgnLogFileMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 2, 1),
    _GnAgnLogFileMaxEntries_Type()
)
gnAgnLogFileMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnAgnLogFileMaxEntries.setStatus("mandatory")
_GnAgnLogFileValidEntries_Type = Integer32
_GnAgnLogFileValidEntries_Object = MibScalar
gnAgnLogFileValidEntries = _GnAgnLogFileValidEntries_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 2, 2),
    _GnAgnLogFileValidEntries_Type()
)
gnAgnLogFileValidEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnAgnLogFileValidEntries.setStatus("mandatory")


class _GnAgnLogFileAction_Type(Integer32):
    """Custom type gnAgnLogFileAction based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("noAction", 5),
          ("save", 3),
          ("saveAndClear", 4))
    )


_GnAgnLogFileAction_Type.__name__ = "Integer32"
_GnAgnLogFileAction_Object = MibScalar
gnAgnLogFileAction = _GnAgnLogFileAction_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 2, 3),
    _GnAgnLogFileAction_Type()
)
gnAgnLogFileAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnAgnLogFileAction.setStatus("mandatory")
_GnAgnLogFileTable_Object = MibTable
gnAgnLogFileTable = _GnAgnLogFileTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 2, 4)
)
if mibBuilder.loadTexts:
    gnAgnLogFileTable.setStatus("mandatory")
_GnAgnLogFileEntry_Object = MibTableRow
gnAgnLogFileEntry = _GnAgnLogFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 2, 4, 1)
)
gnAgnLogFileEntry.setIndexNames(
    (0, "CERAGON-MIB", "gnAgnLogFileId"),
)
if mibBuilder.loadTexts:
    gnAgnLogFileEntry.setStatus("mandatory")
_GnAgnLogFileId_Type = Integer32
_GnAgnLogFileId_Object = MibTableColumn
gnAgnLogFileId = _GnAgnLogFileId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 2, 4, 1, 1),
    _GnAgnLogFileId_Type()
)
gnAgnLogFileId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnAgnLogFileId.setStatus("mandatory")


class _GnAgnLogFileValid_Type(Integer32):
    """Custom type gnAgnLogFileValid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notvalid", 3),
          ("valid", 2))
    )


_GnAgnLogFileValid_Type.__name__ = "Integer32"
_GnAgnLogFileValid_Object = MibTableColumn
gnAgnLogFileValid = _GnAgnLogFileValid_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 2, 4, 1, 2),
    _GnAgnLogFileValid_Type()
)
gnAgnLogFileValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnAgnLogFileValid.setStatus("mandatory")
_GnAgnLogFileDate_Type = DisplayString
_GnAgnLogFileDate_Object = MibTableColumn
gnAgnLogFileDate = _GnAgnLogFileDate_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 2, 4, 1, 3),
    _GnAgnLogFileDate_Type()
)
gnAgnLogFileDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnAgnLogFileDate.setStatus("mandatory")
_GnAgnLogFileTime_Type = DisplayString
_GnAgnLogFileTime_Object = MibTableColumn
gnAgnLogFileTime = _GnAgnLogFileTime_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 2, 4, 1, 4),
    _GnAgnLogFileTime_Type()
)
gnAgnLogFileTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnAgnLogFileTime.setStatus("mandatory")


class _GnAgnLogFileSeverity_Type(Integer32):
    """Custom type gnAgnLogFileSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              7,
              15,
              31)
        )
    )
    namedValues = NamedValues(
        *(("critical", 31),
          ("event", 1),
          ("major", 15),
          ("minor", 7),
          ("warning", 3))
    )


_GnAgnLogFileSeverity_Type.__name__ = "Integer32"
_GnAgnLogFileSeverity_Object = MibTableColumn
gnAgnLogFileSeverity = _GnAgnLogFileSeverity_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 2, 4, 1, 5),
    _GnAgnLogFileSeverity_Type()
)
gnAgnLogFileSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnAgnLogFileSeverity.setStatus("mandatory")
_GnAgnLogFileText_Type = DisplayString
_GnAgnLogFileText_Object = MibTableColumn
gnAgnLogFileText = _GnAgnLogFileText_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 2, 4, 1, 6),
    _GnAgnLogFileText_Type()
)
gnAgnLogFileText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnAgnLogFileText.setStatus("mandatory")
_GnAgnLogFileDeviceCelsiusTemp_Type = Integer32
_GnAgnLogFileDeviceCelsiusTemp_Object = MibTableColumn
gnAgnLogFileDeviceCelsiusTemp = _GnAgnLogFileDeviceCelsiusTemp_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 2, 4, 1, 7),
    _GnAgnLogFileDeviceCelsiusTemp_Type()
)
gnAgnLogFileDeviceCelsiusTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnAgnLogFileDeviceCelsiusTemp.setStatus("mandatory")


class _GnAgnLogFileDevicePowerSupply_Type(OctetString):
    """Custom type gnAgnLogFileDevicePowerSupply based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_GnAgnLogFileDevicePowerSupply_Type.__name__ = "OctetString"
_GnAgnLogFileDevicePowerSupply_Object = MibTableColumn
gnAgnLogFileDevicePowerSupply = _GnAgnLogFileDevicePowerSupply_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 2, 4, 1, 8),
    _GnAgnLogFileDevicePowerSupply_Type()
)
gnAgnLogFileDevicePowerSupply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnAgnLogFileDevicePowerSupply.setStatus("mandatory")


class _GnAgnLogFileInternalCommunication_Type(OctetString):
    """Custom type gnAgnLogFileInternalCommunication based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_GnAgnLogFileInternalCommunication_Type.__name__ = "OctetString"
_GnAgnLogFileInternalCommunication_Object = MibTableColumn
gnAgnLogFileInternalCommunication = _GnAgnLogFileInternalCommunication_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 2, 4, 1, 9),
    _GnAgnLogFileInternalCommunication_Type()
)
gnAgnLogFileInternalCommunication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnAgnLogFileInternalCommunication.setStatus("mandatory")


class _GnAgnLogFileDeviceFanStatus_Type(OctetString):
    """Custom type gnAgnLogFileDeviceFanStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_GnAgnLogFileDeviceFanStatus_Type.__name__ = "OctetString"
_GnAgnLogFileDeviceFanStatus_Object = MibTableColumn
gnAgnLogFileDeviceFanStatus = _GnAgnLogFileDeviceFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 2, 4, 1, 10),
    _GnAgnLogFileDeviceFanStatus_Type()
)
gnAgnLogFileDeviceFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnAgnLogFileDeviceFanStatus.setStatus("mandatory")


class _GnAgnLogFileDeviceODUStatus_Type(OctetString):
    """Custom type gnAgnLogFileDeviceODUStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_GnAgnLogFileDeviceODUStatus_Type.__name__ = "OctetString"
_GnAgnLogFileDeviceODUStatus_Object = MibTableColumn
gnAgnLogFileDeviceODUStatus = _GnAgnLogFileDeviceODUStatus_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 2, 4, 1, 11),
    _GnAgnLogFileDeviceODUStatus_Type()
)
gnAgnLogFileDeviceODUStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnAgnLogFileDeviceODUStatus.setStatus("mandatory")


class _GnAgnLogFileDeviceIDUStatus_Type(OctetString):
    """Custom type gnAgnLogFileDeviceIDUStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_GnAgnLogFileDeviceIDUStatus_Type.__name__ = "OctetString"
_GnAgnLogFileDeviceIDUStatus_Object = MibTableColumn
gnAgnLogFileDeviceIDUStatus = _GnAgnLogFileDeviceIDUStatus_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 2, 4, 1, 12),
    _GnAgnLogFileDeviceIDUStatus_Type()
)
gnAgnLogFileDeviceIDUStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnAgnLogFileDeviceIDUStatus.setStatus("mandatory")
_GnAgnLogFileOduCelsiusTemp_Type = Integer32
_GnAgnLogFileOduCelsiusTemp_Object = MibTableColumn
gnAgnLogFileOduCelsiusTemp = _GnAgnLogFileOduCelsiusTemp_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 2, 4, 1, 13),
    _GnAgnLogFileOduCelsiusTemp_Type()
)
gnAgnLogFileOduCelsiusTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnAgnLogFileOduCelsiusTemp.setStatus("mandatory")
_GnAgnLogFileOduReceiveLevel_Type = Integer32
_GnAgnLogFileOduReceiveLevel_Object = MibTableColumn
gnAgnLogFileOduReceiveLevel = _GnAgnLogFileOduReceiveLevel_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 2, 4, 1, 14),
    _GnAgnLogFileOduReceiveLevel_Type()
)
gnAgnLogFileOduReceiveLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnAgnLogFileOduReceiveLevel.setStatus("mandatory")


class _GnAgnLogFileOduSynthesizerVCOLock_Type(OctetString):
    """Custom type gnAgnLogFileOduSynthesizerVCOLock based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_GnAgnLogFileOduSynthesizerVCOLock_Type.__name__ = "OctetString"
_GnAgnLogFileOduSynthesizerVCOLock_Object = MibTableColumn
gnAgnLogFileOduSynthesizerVCOLock = _GnAgnLogFileOduSynthesizerVCOLock_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 2, 4, 1, 15),
    _GnAgnLogFileOduSynthesizerVCOLock_Type()
)
gnAgnLogFileOduSynthesizerVCOLock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnAgnLogFileOduSynthesizerVCOLock.setStatus("mandatory")


class _GnAgnLogFileOduPowerSupply_Type(OctetString):
    """Custom type gnAgnLogFileOduPowerSupply based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_GnAgnLogFileOduPowerSupply_Type.__name__ = "OctetString"
_GnAgnLogFileOduPowerSupply_Object = MibTableColumn
gnAgnLogFileOduPowerSupply = _GnAgnLogFileOduPowerSupply_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 2, 4, 1, 16),
    _GnAgnLogFileOduPowerSupply_Type()
)
gnAgnLogFileOduPowerSupply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnAgnLogFileOduPowerSupply.setStatus("mandatory")
_GnAgnLogFileLineBERCur_Type = Integer32
_GnAgnLogFileLineBERCur_Object = MibTableColumn
gnAgnLogFileLineBERCur = _GnAgnLogFileLineBERCur_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 2, 4, 1, 17),
    _GnAgnLogFileLineBERCur_Type()
)
gnAgnLogFileLineBERCur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnAgnLogFileLineBERCur.setStatus("mandatory")
_GnAgnLogFileRadioBERCur_Type = Integer32
_GnAgnLogFileRadioBERCur_Object = MibTableColumn
gnAgnLogFileRadioBERCur = _GnAgnLogFileRadioBERCur_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 2, 4, 1, 18),
    _GnAgnLogFileRadioBERCur_Type()
)
gnAgnLogFileRadioBERCur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnAgnLogFileRadioBERCur.setStatus("mandatory")
_GnAgnLogFileModStatus_Type = Integer32
_GnAgnLogFileModStatus_Object = MibTableColumn
gnAgnLogFileModStatus = _GnAgnLogFileModStatus_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 2, 4, 1, 19),
    _GnAgnLogFileModStatus_Type()
)
gnAgnLogFileModStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnAgnLogFileModStatus.setStatus("mandatory")
_GnAgnLogFileDemodStatus_Type = Integer32
_GnAgnLogFileDemodStatus_Object = MibTableColumn
gnAgnLogFileDemodStatus = _GnAgnLogFileDemodStatus_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 2, 4, 1, 20),
    _GnAgnLogFileDemodStatus_Type()
)
gnAgnLogFileDemodStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnAgnLogFileDemodStatus.setStatus("mandatory")
_GnAgnLogFileLastDemodDefectBlocks_Type = Integer32
_GnAgnLogFileLastDemodDefectBlocks_Object = MibTableColumn
gnAgnLogFileLastDemodDefectBlocks = _GnAgnLogFileLastDemodDefectBlocks_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 2, 4, 1, 21),
    _GnAgnLogFileLastDemodDefectBlocks_Type()
)
gnAgnLogFileLastDemodDefectBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnAgnLogFileLastDemodDefectBlocks.setStatus("mandatory")
_GnAgnLogFileLastDemodBytesCorrected_Type = Integer32
_GnAgnLogFileLastDemodBytesCorrected_Object = MibTableColumn
gnAgnLogFileLastDemodBytesCorrected = _GnAgnLogFileLastDemodBytesCorrected_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 2, 4, 1, 22),
    _GnAgnLogFileLastDemodBytesCorrected_Type()
)
gnAgnLogFileLastDemodBytesCorrected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnAgnLogFileLastDemodBytesCorrected.setStatus("mandatory")
_GnAgnLogFileLastDemodBlocksCorrected_Type = Integer32
_GnAgnLogFileLastDemodBlocksCorrected_Object = MibTableColumn
gnAgnLogFileLastDemodBlocksCorrected = _GnAgnLogFileLastDemodBlocksCorrected_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 2, 4, 1, 23),
    _GnAgnLogFileLastDemodBlocksCorrected_Type()
)
gnAgnLogFileLastDemodBlocksCorrected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnAgnLogFileLastDemodBlocksCorrected.setStatus("mandatory")
_GnAgnLogFileUniqueId_Type = Integer32
_GnAgnLogFileUniqueId_Object = MibTableColumn
gnAgnLogFileUniqueId = _GnAgnLogFileUniqueId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 2, 4, 1, 24),
    _GnAgnLogFileUniqueId_Type()
)
gnAgnLogFileUniqueId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnAgnLogFileUniqueId.setStatus("mandatory")


class _GnAgnLogFileSource_Type(Integer32):
    """Custom type gnAgnLogFileSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              257,
              258,
              259,
              260,
              261,
              262,
              263,
              264,
              265,
              513,
              514,
              515,
              516,
              517,
              518,
              519,
              520,
              521,
              522,
              523,
              524,
              525,
              526,
              527,
              769,
              770,
              771,
              772,
              773,
              774)
        )
    )
    namedValues = NamedValues(
        *(("drawer1", 3),
          ("drawer2", 4),
          ("idc", 2),
          ("interfaces", 1),
          ("tDrawer1", 513),
          ("tDrawer10", 522),
          ("tDrawer11", 523),
          ("tDrawer12", 524),
          ("tDrawer13", 525),
          ("tDrawer14", 526),
          ("tDrawer15", 527),
          ("tDrawer2", 514),
          ("tDrawer3", 515),
          ("tDrawer4", 516),
          ("tDrawer5", 517),
          ("tDrawer6", 518),
          ("tDrawer7", 519),
          ("tDrawer8", 520),
          ("tDrawer9", 521),
          ("tIdc1", 257),
          ("tIdc2", 258),
          ("tIdc3", 259),
          ("tIdc4", 260),
          ("tIdc5", 261),
          ("tIdc6", 262),
          ("tIdc7", 263),
          ("tIdc8", 264),
          ("tIdc9", 265),
          ("tXC1", 769),
          ("tXC2", 770),
          ("tXC3", 771),
          ("tXC4", 772),
          ("tXC5", 773),
          ("tXC6", 774))
    )


_GnAgnLogFileSource_Type.__name__ = "Integer32"
_GnAgnLogFileSource_Object = MibTableColumn
gnAgnLogFileSource = _GnAgnLogFileSource_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 2, 4, 1, 25),
    _GnAgnLogFileSource_Type()
)
gnAgnLogFileSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnAgnLogFileSource.setStatus("mandatory")
_GnAgnLogFileTimeT_Type = Integer32
_GnAgnLogFileTimeT_Object = MibTableColumn
gnAgnLogFileTimeT = _GnAgnLogFileTimeT_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 2, 4, 1, 26),
    _GnAgnLogFileTimeT_Type()
)
gnAgnLogFileTimeT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnAgnLogFileTimeT.setStatus("mandatory")


class _GnAgnLogFileHitlessSwitchLogAdmin_Type(Integer32):
    """Custom type gnAgnLogFileHitlessSwitchLogAdmin based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("enable", 2))
    )


_GnAgnLogFileHitlessSwitchLogAdmin_Type.__name__ = "Integer32"
_GnAgnLogFileHitlessSwitchLogAdmin_Object = MibScalar
gnAgnLogFileHitlessSwitchLogAdmin = _GnAgnLogFileHitlessSwitchLogAdmin_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 2, 5),
    _GnAgnLogFileHitlessSwitchLogAdmin_Type()
)
gnAgnLogFileHitlessSwitchLogAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnAgnLogFileHitlessSwitchLogAdmin.setStatus("mandatory")


class _GnAgnLogFileXCSwitchLogAdmin_Type(Integer32):
    """Custom type gnAgnLogFileXCSwitchLogAdmin based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("enable", 2))
    )


_GnAgnLogFileXCSwitchLogAdmin_Type.__name__ = "Integer32"
_GnAgnLogFileXCSwitchLogAdmin_Object = MibScalar
gnAgnLogFileXCSwitchLogAdmin = _GnAgnLogFileXCSwitchLogAdmin_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 2, 6),
    _GnAgnLogFileXCSwitchLogAdmin_Type()
)
gnAgnLogFileXCSwitchLogAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnAgnLogFileXCSwitchLogAdmin.setStatus("mandatory")
_GnAgnExternAlarm_ObjectIdentity = ObjectIdentity
gnAgnExternAlarm = _GnAgnExternAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 3)
)
_GnAgnInExternAlarmTable_Object = MibTable
gnAgnInExternAlarmTable = _GnAgnInExternAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 3, 1)
)
if mibBuilder.loadTexts:
    gnAgnInExternAlarmTable.setStatus("mandatory")
_GnAgnInExternAlarmEntry_Object = MibTableRow
gnAgnInExternAlarmEntry = _GnAgnInExternAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 3, 1, 1)
)
gnAgnInExternAlarmEntry.setIndexNames(
    (0, "CERAGON-MIB", "gnAgnInExternAlarmDevId"),
    (0, "CERAGON-MIB", "gnAgnInExternAlarmIndex"),
)
if mibBuilder.loadTexts:
    gnAgnInExternAlarmEntry.setStatus("mandatory")


class _GnAgnInExternAlarmDevId_Type(Integer32):
    """Custom type gnAgnInExternAlarmDevId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("remote", 2))
    )


_GnAgnInExternAlarmDevId_Type.__name__ = "Integer32"
_GnAgnInExternAlarmDevId_Object = MibTableColumn
gnAgnInExternAlarmDevId = _GnAgnInExternAlarmDevId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 3, 1, 1, 1),
    _GnAgnInExternAlarmDevId_Type()
)
gnAgnInExternAlarmDevId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnAgnInExternAlarmDevId.setStatus("mandatory")


class _GnAgnInExternAlarmIndex_Type(Integer32):
    """Custom type gnAgnInExternAlarmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_GnAgnInExternAlarmIndex_Type.__name__ = "Integer32"
_GnAgnInExternAlarmIndex_Object = MibTableColumn
gnAgnInExternAlarmIndex = _GnAgnInExternAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 3, 1, 1, 2),
    _GnAgnInExternAlarmIndex_Type()
)
gnAgnInExternAlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnAgnInExternAlarmIndex.setStatus("mandatory")


class _GnAgnInExternAlarmEnable_Type(Integer32):
    """Custom type gnAgnInExternAlarmEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3))
    )


_GnAgnInExternAlarmEnable_Type.__name__ = "Integer32"
_GnAgnInExternAlarmEnable_Object = MibTableColumn
gnAgnInExternAlarmEnable = _GnAgnInExternAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 3, 1, 1, 3),
    _GnAgnInExternAlarmEnable_Type()
)
gnAgnInExternAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnAgnInExternAlarmEnable.setStatus("mandatory")


class _GnAgnInExternAlarmText_Type(DisplayString):
    """Custom type gnAgnInExternAlarmText based on DisplayString"""
    defaultValue = OctetString("Alarm Description")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_GnAgnInExternAlarmText_Type.__name__ = "DisplayString"
_GnAgnInExternAlarmText_Object = MibTableColumn
gnAgnInExternAlarmText = _GnAgnInExternAlarmText_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 3, 1, 1, 4),
    _GnAgnInExternAlarmText_Type()
)
gnAgnInExternAlarmText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnAgnInExternAlarmText.setStatus("mandatory")


class _GnAgnInExternAlarmSeverity_Type(Integer32):
    """Custom type gnAgnInExternAlarmSeverity based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              7,
              15,
              31)
        )
    )
    namedValues = NamedValues(
        *(("critical", 31),
          ("event", 1),
          ("major", 15),
          ("minor", 7),
          ("warning", 3))
    )


_GnAgnInExternAlarmSeverity_Type.__name__ = "Integer32"
_GnAgnInExternAlarmSeverity_Object = MibTableColumn
gnAgnInExternAlarmSeverity = _GnAgnInExternAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 3, 1, 1, 5),
    _GnAgnInExternAlarmSeverity_Type()
)
gnAgnInExternAlarmSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnAgnInExternAlarmSeverity.setStatus("mandatory")
_GnAgnOutRelayAlarmTable_Object = MibTable
gnAgnOutRelayAlarmTable = _GnAgnOutRelayAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 3, 2)
)
if mibBuilder.loadTexts:
    gnAgnOutRelayAlarmTable.setStatus("mandatory")
_GnAgnOutRelayAlarmEntry_Object = MibTableRow
gnAgnOutRelayAlarmEntry = _GnAgnOutRelayAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 3, 2, 1)
)
gnAgnOutRelayAlarmEntry.setIndexNames(
    (0, "CERAGON-MIB", "gnAgnOutRelayAlarmDevId"),
    (0, "CERAGON-MIB", "gnAgnOutRelayAlarmIndex"),
)
if mibBuilder.loadTexts:
    gnAgnOutRelayAlarmEntry.setStatus("mandatory")


class _GnAgnOutRelayAlarmDevId_Type(Integer32):
    """Custom type gnAgnOutRelayAlarmDevId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("remote", 2))
    )


_GnAgnOutRelayAlarmDevId_Type.__name__ = "Integer32"
_GnAgnOutRelayAlarmDevId_Object = MibTableColumn
gnAgnOutRelayAlarmDevId = _GnAgnOutRelayAlarmDevId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 3, 2, 1, 1),
    _GnAgnOutRelayAlarmDevId_Type()
)
gnAgnOutRelayAlarmDevId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnAgnOutRelayAlarmDevId.setStatus("mandatory")


class _GnAgnOutRelayAlarmIndex_Type(Integer32):
    """Custom type gnAgnOutRelayAlarmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_GnAgnOutRelayAlarmIndex_Type.__name__ = "Integer32"
_GnAgnOutRelayAlarmIndex_Object = MibTableColumn
gnAgnOutRelayAlarmIndex = _GnAgnOutRelayAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 3, 2, 1, 2),
    _GnAgnOutRelayAlarmIndex_Type()
)
gnAgnOutRelayAlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnAgnOutRelayAlarmIndex.setStatus("mandatory")


class _GnAgnOutRelayAlarmType_Type(Integer32):
    """Custom type gnAgnOutRelayAlarmType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
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
        *(("ber", 7),
          ("cable", 13),
          ("critical", 15),
          ("external", 5),
          ("idu", 11),
          ("line", 8),
          ("lof", 10),
          ("loopback", 9),
          ("major", 2),
          ("minor", 3),
          ("odu", 12),
          ("off", 17),
          ("power", 6),
          ("remote", 14),
          ("testOn", 16),
          ("warning", 4),
          ("xc", 18))
    )


_GnAgnOutRelayAlarmType_Type.__name__ = "Integer32"
_GnAgnOutRelayAlarmType_Object = MibTableColumn
gnAgnOutRelayAlarmType = _GnAgnOutRelayAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 3, 2, 1, 3),
    _GnAgnOutRelayAlarmType_Type()
)
gnAgnOutRelayAlarmType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnAgnOutRelayAlarmType.setStatus("mandatory")
_GnAgnFileTransfer_ObjectIdentity = ObjectIdentity
gnAgnFileTransfer = _GnAgnFileTransfer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 4)
)


class _GnAgnFileTransferDestination_Type(Integer32):
    """Custom type gnAgnFileTransferDestination based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("gnLocal", 1)
    )


_GnAgnFileTransferDestination_Type.__name__ = "Integer32"
_GnAgnFileTransferDestination_Object = MibScalar
gnAgnFileTransferDestination = _GnAgnFileTransferDestination_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 4, 1),
    _GnAgnFileTransferDestination_Type()
)
gnAgnFileTransferDestination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnAgnFileTransferDestination.setStatus("mandatory")
_GnAgnFileTransferServerIP_Type = IpAddress
_GnAgnFileTransferServerIP_Object = MibScalar
gnAgnFileTransferServerIP = _GnAgnFileTransferServerIP_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 4, 2),
    _GnAgnFileTransferServerIP_Type()
)
gnAgnFileTransferServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnAgnFileTransferServerIP.setStatus("mandatory")
_GnAgnFileTransferFileName_Type = DisplayString
_GnAgnFileTransferFileName_Object = MibScalar
gnAgnFileTransferFileName = _GnAgnFileTransferFileName_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 4, 3),
    _GnAgnFileTransferFileName_Type()
)
gnAgnFileTransferFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnAgnFileTransferFileName.setStatus("mandatory")
_GnAgnFileTransferTftpTotalTimeOut_Type = Integer32
_GnAgnFileTransferTftpTotalTimeOut_Object = MibScalar
gnAgnFileTransferTftpTotalTimeOut = _GnAgnFileTransferTftpTotalTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 4, 4),
    _GnAgnFileTransferTftpTotalTimeOut_Type()
)
gnAgnFileTransferTftpTotalTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnAgnFileTransferTftpTotalTimeOut.setStatus("mandatory")


class _GnAgnFileTransferTransCmd_Type(Integer32):
    """Custom type gnAgnFileTransferTransCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              255)
        )
    )
    namedValues = NamedValues(
        *(("gnCancel", 4),
          ("gnNoOperation", 255),
          ("gnStartMUXSoftwareDownLoad", 1),
          ("gnStartMainManagerSoftwareDownLoad", 3),
          ("gnStartODUSoftwareDownLoad", 2))
    )


_GnAgnFileTransferTransCmd_Type.__name__ = "Integer32"
_GnAgnFileTransferTransCmd_Object = MibScalar
gnAgnFileTransferTransCmd = _GnAgnFileTransferTransCmd_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 4, 5),
    _GnAgnFileTransferTransCmd_Type()
)
gnAgnFileTransferTransCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnAgnFileTransferTransCmd.setStatus("mandatory")


class _GnAgnFileTransfertFtpStatus_Type(Integer32):
    """Custom type gnAgnFileTransfertFtpStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              255)
        )
    )
    namedValues = NamedValues(
        *(("gnNoTftpSession", 255),
          ("gnTftpSessionDone", 6),
          ("gnTftpSessionFileError", 2),
          ("gnTftpSessionPreStartSession", 1),
          ("gnTftpSessionRcvBlock", 3),
          ("gnTftpSessionRcvError", 5),
          ("gnTftpSessionRcvtimeout", 4))
    )


_GnAgnFileTransfertFtpStatus_Type.__name__ = "Integer32"
_GnAgnFileTransfertFtpStatus_Object = MibScalar
gnAgnFileTransfertFtpStatus = _GnAgnFileTransfertFtpStatus_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 4, 6),
    _GnAgnFileTransfertFtpStatus_Type()
)
gnAgnFileTransfertFtpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnAgnFileTransfertFtpStatus.setStatus("mandatory")
_GnAgnFileTransfertftpBlockCount_Type = Integer32
_GnAgnFileTransfertftpBlockCount_Object = MibScalar
gnAgnFileTransfertftpBlockCount = _GnAgnFileTransfertftpBlockCount_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 4, 7),
    _GnAgnFileTransfertftpBlockCount_Type()
)
gnAgnFileTransfertftpBlockCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnAgnFileTransfertftpBlockCount.setStatus("mandatory")


class _GnAgnFileTransferProtocol_Type(Integer32):
    """Custom type gnAgnFileTransferProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ftp", 3),
          ("tftp", 2))
    )


_GnAgnFileTransferProtocol_Type.__name__ = "Integer32"
_GnAgnFileTransferProtocol_Object = MibScalar
gnAgnFileTransferProtocol = _GnAgnFileTransferProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 4, 8),
    _GnAgnFileTransferProtocol_Type()
)
gnAgnFileTransferProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnAgnFileTransferProtocol.setStatus("mandatory")


class _GnAgnFileTransferUserName_Type(DisplayString):
    """Custom type gnAgnFileTransferUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_GnAgnFileTransferUserName_Type.__name__ = "DisplayString"
_GnAgnFileTransferUserName_Object = MibScalar
gnAgnFileTransferUserName = _GnAgnFileTransferUserName_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 4, 9),
    _GnAgnFileTransferUserName_Type()
)
gnAgnFileTransferUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnAgnFileTransferUserName.setStatus("mandatory")


class _GnAgnFileTransferPassword_Type(DisplayString):
    """Custom type gnAgnFileTransferPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_GnAgnFileTransferPassword_Type.__name__ = "DisplayString"
_GnAgnFileTransferPassword_Object = MibScalar
gnAgnFileTransferPassword = _GnAgnFileTransferPassword_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 4, 10),
    _GnAgnFileTransferPassword_Type()
)
gnAgnFileTransferPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnAgnFileTransferPassword.setStatus("mandatory")


class _GnAgnFileTransferIDCVersionControl_Type(Integer32):
    """Custom type gnAgnFileTransferIDCVersionControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("version1", 1),
          ("version2", 2))
    )


_GnAgnFileTransferIDCVersionControl_Type.__name__ = "Integer32"
_GnAgnFileTransferIDCVersionControl_Object = MibScalar
gnAgnFileTransferIDCVersionControl = _GnAgnFileTransferIDCVersionControl_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 4, 11),
    _GnAgnFileTransferIDCVersionControl_Type()
)
gnAgnFileTransferIDCVersionControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnAgnFileTransferIDCVersionControl.setStatus("mandatory")


class _GnAgnFileTransferODCVersionControl_Type(Integer32):
    """Custom type gnAgnFileTransferODCVersionControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("version1", 1),
          ("version2", 2))
    )


_GnAgnFileTransferODCVersionControl_Type.__name__ = "Integer32"
_GnAgnFileTransferODCVersionControl_Object = MibScalar
gnAgnFileTransferODCVersionControl = _GnAgnFileTransferODCVersionControl_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 4, 12),
    _GnAgnFileTransferODCVersionControl_Type()
)
gnAgnFileTransferODCVersionControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnAgnFileTransferODCVersionControl.setStatus("mandatory")
_GnAgnInternalDownloadTable_Object = MibTable
gnAgnInternalDownloadTable = _GnAgnInternalDownloadTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 5)
)
if mibBuilder.loadTexts:
    gnAgnInternalDownloadTable.setStatus("mandatory")
_GnAgnInternalDownloadEntry_Object = MibTableRow
gnAgnInternalDownloadEntry = _GnAgnInternalDownloadEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 5, 1)
)
gnAgnInternalDownloadEntry.setIndexNames(
    (0, "CERAGON-MIB", "gnAgnInternalDownloadId"),
)
if mibBuilder.loadTexts:
    gnAgnInternalDownloadEntry.setStatus("mandatory")
_GnAgnInternalDownloadId_Type = Integer32
_GnAgnInternalDownloadId_Object = MibTableColumn
gnAgnInternalDownloadId = _GnAgnInternalDownloadId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 5, 1, 1),
    _GnAgnInternalDownloadId_Type()
)
gnAgnInternalDownloadId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnAgnInternalDownloadId.setStatus("mandatory")


class _GnAgnInternalDownloadOperation_Type(Integer32):
    """Custom type gnAgnInternalDownloadOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("leftShelfODU", 6),
          ("localMUX", 2),
          ("localODU", 3),
          ("remoteMUX", 4),
          ("remoteODU", 5),
          ("rightShelfODU", 7))
    )


_GnAgnInternalDownloadOperation_Type.__name__ = "Integer32"
_GnAgnInternalDownloadOperation_Object = MibTableColumn
gnAgnInternalDownloadOperation = _GnAgnInternalDownloadOperation_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 5, 1, 2),
    _GnAgnInternalDownloadOperation_Type()
)
gnAgnInternalDownloadOperation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnAgnInternalDownloadOperation.setStatus("mandatory")


class _GnAgnInternalDownloadAction_Type(Integer32):
    """Custom type gnAgnInternalDownloadAction based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("cancel", 3),
          ("clear", 4),
          ("noAction", 5),
          ("start", 2),
          ("upLoadFpga", 6))
    )


_GnAgnInternalDownloadAction_Type.__name__ = "Integer32"
_GnAgnInternalDownloadAction_Object = MibTableColumn
gnAgnInternalDownloadAction = _GnAgnInternalDownloadAction_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 5, 1, 3),
    _GnAgnInternalDownloadAction_Type()
)
gnAgnInternalDownloadAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnAgnInternalDownloadAction.setStatus("mandatory")


class _GnAgnInternalDownloadStatus_Type(Integer32):
    """Custom type gnAgnInternalDownloadStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              255)
        )
    )
    namedValues = NamedValues(
        *(("gnInternalDownloadSessionClearing", 2),
          ("gnInternalDownloadSessionDone", 5),
          ("gnInternalDownloadSessionError", 1),
          ("gnInternalDownloadSessionSendBlock", 3),
          ("gnInternalDownloadSessionWaitForRetransmit", 6),
          ("gnInternalDownloadSessiontimeout", 4),
          ("gnNoInternalDownloadSession", 255))
    )


_GnAgnInternalDownloadStatus_Type.__name__ = "Integer32"
_GnAgnInternalDownloadStatus_Object = MibTableColumn
gnAgnInternalDownloadStatus = _GnAgnInternalDownloadStatus_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 5, 1, 4),
    _GnAgnInternalDownloadStatus_Type()
)
gnAgnInternalDownloadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnAgnInternalDownloadStatus.setStatus("mandatory")
_GnAgnInternalDownloadBlockCount_Type = Integer32
_GnAgnInternalDownloadBlockCount_Object = MibTableColumn
gnAgnInternalDownloadBlockCount = _GnAgnInternalDownloadBlockCount_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 5, 1, 5),
    _GnAgnInternalDownloadBlockCount_Type()
)
gnAgnInternalDownloadBlockCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnAgnInternalDownloadBlockCount.setStatus("mandatory")


class _GnAgnInternalDownloadVersionControl_Type(Integer32):
    """Custom type gnAgnInternalDownloadVersionControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("version1", 1),
          ("version2", 2))
    )


_GnAgnInternalDownloadVersionControl_Type.__name__ = "Integer32"
_GnAgnInternalDownloadVersionControl_Object = MibTableColumn
gnAgnInternalDownloadVersionControl = _GnAgnInternalDownloadVersionControl_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 5, 1, 6),
    _GnAgnInternalDownloadVersionControl_Type()
)
gnAgnInternalDownloadVersionControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnAgnInternalDownloadVersionControl.setStatus("mandatory")
_GnAgnInternalDownloadFileSizeInBytes_Type = Integer32
_GnAgnInternalDownloadFileSizeInBytes_Object = MibTableColumn
gnAgnInternalDownloadFileSizeInBytes = _GnAgnInternalDownloadFileSizeInBytes_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 5, 1, 7),
    _GnAgnInternalDownloadFileSizeInBytes_Type()
)
gnAgnInternalDownloadFileSizeInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnAgnInternalDownloadFileSizeInBytes.setStatus("mandatory")
_GnAgnInternalDownloadBytesCount_Type = Integer32
_GnAgnInternalDownloadBytesCount_Object = MibTableColumn
gnAgnInternalDownloadBytesCount = _GnAgnInternalDownloadBytesCount_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 5, 1, 8),
    _GnAgnInternalDownloadBytesCount_Type()
)
gnAgnInternalDownloadBytesCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnAgnInternalDownloadBytesCount.setStatus("mandatory")
_GnAgnInterLinkTable_Object = MibTable
gnAgnInterLinkTable = _GnAgnInterLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 6)
)
if mibBuilder.loadTexts:
    gnAgnInterLinkTable.setStatus("mandatory")
_GnAgnInterLinkEntry_Object = MibTableRow
gnAgnInterLinkEntry = _GnAgnInterLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 6, 1)
)
gnAgnInterLinkEntry.setIndexNames(
    (0, "CERAGON-MIB", "gnAgnInterLinkId"),
)
if mibBuilder.loadTexts:
    gnAgnInterLinkEntry.setStatus("mandatory")
_GnAgnInterLinkId_Type = Integer32
_GnAgnInterLinkId_Object = MibTableColumn
gnAgnInterLinkId = _GnAgnInterLinkId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 6, 1, 1),
    _GnAgnInterLinkId_Type()
)
gnAgnInterLinkId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnAgnInterLinkId.setStatus("mandatory")


class _GnAgnInterLinkSide_Type(Integer32):
    """Custom type gnAgnInterLinkSide based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("local", 2),
          ("remote", 3))
    )


_GnAgnInterLinkSide_Type.__name__ = "Integer32"
_GnAgnInterLinkSide_Object = MibTableColumn
gnAgnInterLinkSide = _GnAgnInterLinkSide_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 6, 1, 2),
    _GnAgnInterLinkSide_Type()
)
gnAgnInterLinkSide.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnAgnInterLinkSide.setStatus("mandatory")


class _GnAgnInterLinkSource_Type(Integer32):
    """Custom type gnAgnInterLinkSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mate", 3),
          ("me", 2))
    )


_GnAgnInterLinkSource_Type.__name__ = "Integer32"
_GnAgnInterLinkSource_Object = MibTableColumn
gnAgnInterLinkSource = _GnAgnInterLinkSource_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 6, 1, 3),
    _GnAgnInterLinkSource_Type()
)
gnAgnInterLinkSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnAgnInterLinkSource.setStatus("mandatory")


class _GnAgnInterLinkDestination_Type(Integer32):
    """Custom type gnAgnInterLinkDestination based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("mate", 3),
          ("me", 2),
          ("remote", 4))
    )


_GnAgnInterLinkDestination_Type.__name__ = "Integer32"
_GnAgnInterLinkDestination_Object = MibTableColumn
gnAgnInterLinkDestination = _GnAgnInterLinkDestination_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 6, 1, 4),
    _GnAgnInterLinkDestination_Type()
)
gnAgnInterLinkDestination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnAgnInterLinkDestination.setStatus("mandatory")


class _GnAgnInterLinkSoftware_Type(Integer32):
    """Custom type gnAgnInterLinkSoftware based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("manager", 2),
          ("mux", 3),
          ("odu", 4))
    )


_GnAgnInterLinkSoftware_Type.__name__ = "Integer32"
_GnAgnInterLinkSoftware_Object = MibTableColumn
gnAgnInterLinkSoftware = _GnAgnInterLinkSoftware_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 6, 1, 5),
    _GnAgnInterLinkSoftware_Type()
)
gnAgnInterLinkSoftware.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnAgnInterLinkSoftware.setStatus("mandatory")


class _GnAgnInterLinkAction_Type(Integer32):
    """Custom type gnAgnInterLinkAction based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("cancel", 3),
          ("noAction", 4),
          ("start", 2))
    )


_GnAgnInterLinkAction_Type.__name__ = "Integer32"
_GnAgnInterLinkAction_Object = MibTableColumn
gnAgnInterLinkAction = _GnAgnInterLinkAction_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 6, 1, 6),
    _GnAgnInterLinkAction_Type()
)
gnAgnInterLinkAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnAgnInterLinkAction.setStatus("mandatory")


class _GnAgnInterLinkStatus_Type(Integer32):
    """Custom type gnAgnInterLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              255)
        )
    )
    namedValues = NamedValues(
        *(("gnInterLinkSessionClearing", 2),
          ("gnInterLinkSessionDone", 5),
          ("gnInterLinkSessionError", 1),
          ("gnInterLinkSessionSendBlock", 3),
          ("gnInterLinkSessiontimeout", 4),
          ("gnNoInterLinkSession", 255))
    )


_GnAgnInterLinkStatus_Type.__name__ = "Integer32"
_GnAgnInterLinkStatus_Object = MibTableColumn
gnAgnInterLinkStatus = _GnAgnInterLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 6, 1, 7),
    _GnAgnInterLinkStatus_Type()
)
gnAgnInterLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnAgnInterLinkStatus.setStatus("mandatory")
_GnAgnInterLinkBlockCount_Type = Integer32
_GnAgnInterLinkBlockCount_Object = MibTableColumn
gnAgnInterLinkBlockCount = _GnAgnInterLinkBlockCount_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 6, 1, 8),
    _GnAgnInterLinkBlockCount_Type()
)
gnAgnInterLinkBlockCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnAgnInterLinkBlockCount.setStatus("mandatory")
_GnSoftwareVersionTable_Object = MibTable
gnSoftwareVersionTable = _GnSoftwareVersionTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 7)
)
if mibBuilder.loadTexts:
    gnSoftwareVersionTable.setStatus("mandatory")
_GnSoftwareVersionEntry_Object = MibTableRow
gnSoftwareVersionEntry = _GnSoftwareVersionEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 7, 1)
)
gnSoftwareVersionEntry.setIndexNames(
    (0, "CERAGON-MIB", "gnSoftwareVersionId"),
)
if mibBuilder.loadTexts:
    gnSoftwareVersionEntry.setStatus("mandatory")


class _GnSoftwareVersionId_Type(Integer32):
    """Custom type gnSoftwareVersionId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("remote", 2))
    )


_GnSoftwareVersionId_Type.__name__ = "Integer32"
_GnSoftwareVersionId_Object = MibTableColumn
gnSoftwareVersionId = _GnSoftwareVersionId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 7, 1, 1),
    _GnSoftwareVersionId_Type()
)
gnSoftwareVersionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnSoftwareVersionId.setStatus("mandatory")


class _GnSoftwareVersionIDU_Type(DisplayString):
    """Custom type gnSoftwareVersionIDU based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_GnSoftwareVersionIDU_Type.__name__ = "DisplayString"
_GnSoftwareVersionIDU_Object = MibTableColumn
gnSoftwareVersionIDU = _GnSoftwareVersionIDU_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 7, 1, 2),
    _GnSoftwareVersionIDU_Type()
)
gnSoftwareVersionIDU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnSoftwareVersionIDU.setStatus("mandatory")


class _GnSoftwareVersionMUX_Type(DisplayString):
    """Custom type gnSoftwareVersionMUX based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_GnSoftwareVersionMUX_Type.__name__ = "DisplayString"
_GnSoftwareVersionMUX_Object = MibTableColumn
gnSoftwareVersionMUX = _GnSoftwareVersionMUX_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 7, 1, 3),
    _GnSoftwareVersionMUX_Type()
)
gnSoftwareVersionMUX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnSoftwareVersionMUX.setStatus("mandatory")


class _GnSoftwareVersionODU_Type(DisplayString):
    """Custom type gnSoftwareVersionODU based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_GnSoftwareVersionODU_Type.__name__ = "DisplayString"
_GnSoftwareVersionODU_Object = MibTableColumn
gnSoftwareVersionODU = _GnSoftwareVersionODU_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 7, 1, 4),
    _GnSoftwareVersionODU_Type()
)
gnSoftwareVersionODU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnSoftwareVersionODU.setStatus("mandatory")


class _GnSoftwareVersionIDUPostResetVersion_Type(DisplayString):
    """Custom type gnSoftwareVersionIDUPostResetVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_GnSoftwareVersionIDUPostResetVersion_Type.__name__ = "DisplayString"
_GnSoftwareVersionIDUPostResetVersion_Object = MibTableColumn
gnSoftwareVersionIDUPostResetVersion = _GnSoftwareVersionIDUPostResetVersion_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 7, 1, 5),
    _GnSoftwareVersionIDUPostResetVersion_Type()
)
gnSoftwareVersionIDUPostResetVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnSoftwareVersionIDUPostResetVersion.setStatus("mandatory")


class _GnSoftwareVersionMUXPostResetVersion_Type(DisplayString):
    """Custom type gnSoftwareVersionMUXPostResetVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_GnSoftwareVersionMUXPostResetVersion_Type.__name__ = "DisplayString"
_GnSoftwareVersionMUXPostResetVersion_Object = MibTableColumn
gnSoftwareVersionMUXPostResetVersion = _GnSoftwareVersionMUXPostResetVersion_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 7, 1, 6),
    _GnSoftwareVersionMUXPostResetVersion_Type()
)
gnSoftwareVersionMUXPostResetVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnSoftwareVersionMUXPostResetVersion.setStatus("mandatory")


class _GnSoftwareVersionODUPostResetVersion_Type(DisplayString):
    """Custom type gnSoftwareVersionODUPostResetVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_GnSoftwareVersionODUPostResetVersion_Type.__name__ = "DisplayString"
_GnSoftwareVersionODUPostResetVersion_Object = MibTableColumn
gnSoftwareVersionODUPostResetVersion = _GnSoftwareVersionODUPostResetVersion_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 7, 1, 7),
    _GnSoftwareVersionODUPostResetVersion_Type()
)
gnSoftwareVersionODUPostResetVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnSoftwareVersionODUPostResetVersion.setStatus("mandatory")


class _GnSoftwareVersionMuxAlteraVer_Type(DisplayString):
    """Custom type gnSoftwareVersionMuxAlteraVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_GnSoftwareVersionMuxAlteraVer_Type.__name__ = "DisplayString"
_GnSoftwareVersionMuxAlteraVer_Object = MibTableColumn
gnSoftwareVersionMuxAlteraVer = _GnSoftwareVersionMuxAlteraVer_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 7, 1, 8),
    _GnSoftwareVersionMuxAlteraVer_Type()
)
gnSoftwareVersionMuxAlteraVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnSoftwareVersionMuxAlteraVer.setStatus("mandatory")


class _GnSoftwareIDCVersionControl_Type(Integer32):
    """Custom type gnSoftwareIDCVersionControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("version1", 1),
          ("version2", 2))
    )


_GnSoftwareIDCVersionControl_Type.__name__ = "Integer32"
_GnSoftwareIDCVersionControl_Object = MibTableColumn
gnSoftwareIDCVersionControl = _GnSoftwareIDCVersionControl_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 7, 1, 9),
    _GnSoftwareIDCVersionControl_Type()
)
gnSoftwareIDCVersionControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnSoftwareIDCVersionControl.setStatus("mandatory")


class _GnSoftwareVersionWSAlteraVer_Type(DisplayString):
    """Custom type gnSoftwareVersionWSAlteraVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_GnSoftwareVersionWSAlteraVer_Type.__name__ = "DisplayString"
_GnSoftwareVersionWSAlteraVer_Object = MibTableColumn
gnSoftwareVersionWSAlteraVer = _GnSoftwareVersionWSAlteraVer_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 7, 1, 10),
    _GnSoftwareVersionWSAlteraVer_Type()
)
gnSoftwareVersionWSAlteraVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnSoftwareVersionWSAlteraVer.setStatus("mandatory")


class _GnSoftwareVersionWSPostResetVersion_Type(DisplayString):
    """Custom type gnSoftwareVersionWSPostResetVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_GnSoftwareVersionWSPostResetVersion_Type.__name__ = "DisplayString"
_GnSoftwareVersionWSPostResetVersion_Object = MibTableColumn
gnSoftwareVersionWSPostResetVersion = _GnSoftwareVersionWSPostResetVersion_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 7, 1, 11),
    _GnSoftwareVersionWSPostResetVersion_Type()
)
gnSoftwareVersionWSPostResetVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnSoftwareVersionWSPostResetVersion.setStatus("mandatory")


class _GnSoftwareVersionMrmcVer_Type(DisplayString):
    """Custom type gnSoftwareVersionMrmcVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_GnSoftwareVersionMrmcVer_Type.__name__ = "DisplayString"
_GnSoftwareVersionMrmcVer_Object = MibTableColumn
gnSoftwareVersionMrmcVer = _GnSoftwareVersionMrmcVer_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 7, 1, 12),
    _GnSoftwareVersionMrmcVer_Type()
)
gnSoftwareVersionMrmcVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnSoftwareVersionMrmcVer.setStatus("mandatory")


class _GnSoftwareVersionMrmcPostResetVer_Type(DisplayString):
    """Custom type gnSoftwareVersionMrmcPostResetVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_GnSoftwareVersionMrmcPostResetVer_Type.__name__ = "DisplayString"
_GnSoftwareVersionMrmcPostResetVer_Object = MibTableColumn
gnSoftwareVersionMrmcPostResetVer = _GnSoftwareVersionMrmcPostResetVer_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 7, 1, 13),
    _GnSoftwareVersionMrmcPostResetVer_Type()
)
gnSoftwareVersionMrmcPostResetVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnSoftwareVersionMrmcPostResetVer.setStatus("mandatory")


class _GnSoftwareVersionBootSoftVer_Type(DisplayString):
    """Custom type gnSoftwareVersionBootSoftVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_GnSoftwareVersionBootSoftVer_Type.__name__ = "DisplayString"
_GnSoftwareVersionBootSoftVer_Object = MibTableColumn
gnSoftwareVersionBootSoftVer = _GnSoftwareVersionBootSoftVer_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 7, 1, 14),
    _GnSoftwareVersionBootSoftVer_Type()
)
gnSoftwareVersionBootSoftVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnSoftwareVersionBootSoftVer.setStatus("mandatory")


class _GnSoftwareVersionBootFlashVer_Type(DisplayString):
    """Custom type gnSoftwareVersionBootFlashVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_GnSoftwareVersionBootFlashVer_Type.__name__ = "DisplayString"
_GnSoftwareVersionBootFlashVer_Object = MibTableColumn
gnSoftwareVersionBootFlashVer = _GnSoftwareVersionBootFlashVer_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 7, 1, 15),
    _GnSoftwareVersionBootFlashVer_Type()
)
gnSoftwareVersionBootFlashVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnSoftwareVersionBootFlashVer.setStatus("mandatory")


class _GnSoftwareVersionAcmLutVer_Type(DisplayString):
    """Custom type gnSoftwareVersionAcmLutVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_GnSoftwareVersionAcmLutVer_Type.__name__ = "DisplayString"
_GnSoftwareVersionAcmLutVer_Object = MibTableColumn
gnSoftwareVersionAcmLutVer = _GnSoftwareVersionAcmLutVer_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 7, 1, 16),
    _GnSoftwareVersionAcmLutVer_Type()
)
gnSoftwareVersionAcmLutVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnSoftwareVersionAcmLutVer.setStatus("mandatory")


class _GnSoftwareVersionAcmLutVerPostResetVer_Type(DisplayString):
    """Custom type gnSoftwareVersionAcmLutVerPostResetVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_GnSoftwareVersionAcmLutVerPostResetVer_Type.__name__ = "DisplayString"
_GnSoftwareVersionAcmLutVerPostResetVer_Object = MibTableColumn
gnSoftwareVersionAcmLutVerPostResetVer = _GnSoftwareVersionAcmLutVerPostResetVer_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 7, 1, 17),
    _GnSoftwareVersionAcmLutVerPostResetVer_Type()
)
gnSoftwareVersionAcmLutVerPostResetVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnSoftwareVersionAcmLutVerPostResetVer.setStatus("mandatory")


class _GnSoftwareVersionSfdVer_Type(DisplayString):
    """Custom type gnSoftwareVersionSfdVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_GnSoftwareVersionSfdVer_Type.__name__ = "DisplayString"
_GnSoftwareVersionSfdVer_Object = MibTableColumn
gnSoftwareVersionSfdVer = _GnSoftwareVersionSfdVer_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 7, 1, 18),
    _GnSoftwareVersionSfdVer_Type()
)
gnSoftwareVersionSfdVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnSoftwareVersionSfdVer.setStatus("mandatory")
_GnAgnNTPCfg_ObjectIdentity = ObjectIdentity
gnAgnNTPCfg = _GnAgnNTPCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 8)
)
_GnAgnNTPCfgServerIP_Type = IpAddress
_GnAgnNTPCfgServerIP_Object = MibScalar
gnAgnNTPCfgServerIP = _GnAgnNTPCfgServerIP_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 8, 1),
    _GnAgnNTPCfgServerIP_Type()
)
gnAgnNTPCfgServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnAgnNTPCfgServerIP.setStatus("mandatory")


class _GnAgnNTPCfgOffsetFromUTC_Type(Integer32):
    """Custom type gnAgnNTPCfgOffsetFromUTC based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1439, 1439),
    )


_GnAgnNTPCfgOffsetFromUTC_Type.__name__ = "Integer32"
_GnAgnNTPCfgOffsetFromUTC_Object = MibScalar
gnAgnNTPCfgOffsetFromUTC = _GnAgnNTPCfgOffsetFromUTC_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 8, 2),
    _GnAgnNTPCfgOffsetFromUTC_Type()
)
gnAgnNTPCfgOffsetFromUTC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnAgnNTPCfgOffsetFromUTC.setStatus("mandatory")


class _GnAgnNTPCfgSummerAdjOffset_Type(Integer32):
    """Custom type gnAgnNTPCfgSummerAdjOffset based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1439, 1439),
    )


_GnAgnNTPCfgSummerAdjOffset_Type.__name__ = "Integer32"
_GnAgnNTPCfgSummerAdjOffset_Object = MibScalar
gnAgnNTPCfgSummerAdjOffset = _GnAgnNTPCfgSummerAdjOffset_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 8, 3),
    _GnAgnNTPCfgSummerAdjOffset_Type()
)
gnAgnNTPCfgSummerAdjOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnAgnNTPCfgSummerAdjOffset.setStatus("mandatory")
_GnAgnNTPCfgSummerAdjStart_Type = Integer32
_GnAgnNTPCfgSummerAdjStart_Object = MibScalar
gnAgnNTPCfgSummerAdjStart = _GnAgnNTPCfgSummerAdjStart_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 8, 4),
    _GnAgnNTPCfgSummerAdjStart_Type()
)
gnAgnNTPCfgSummerAdjStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnAgnNTPCfgSummerAdjStart.setStatus("mandatory")
_GnAgnNTPCfgSummerAdjEnd_Type = Integer32
_GnAgnNTPCfgSummerAdjEnd_Object = MibScalar
gnAgnNTPCfgSummerAdjEnd = _GnAgnNTPCfgSummerAdjEnd_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 8, 5),
    _GnAgnNTPCfgSummerAdjEnd_Type()
)
gnAgnNTPCfgSummerAdjEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnAgnNTPCfgSummerAdjEnd.setStatus("mandatory")


class _GnAgnNTPCfgEnableAuth_Type(Integer32):
    """Custom type gnAgnNTPCfgEnableAuth based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("des", 3),
          ("disabled", 2))
    )


_GnAgnNTPCfgEnableAuth_Type.__name__ = "Integer32"
_GnAgnNTPCfgEnableAuth_Object = MibScalar
gnAgnNTPCfgEnableAuth = _GnAgnNTPCfgEnableAuth_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 8, 6),
    _GnAgnNTPCfgEnableAuth_Type()
)
gnAgnNTPCfgEnableAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnAgnNTPCfgEnableAuth.setStatus("mandatory")


class _GnAgnNTPCfgAuthSecretKey_Type(OctetString):
    """Custom type gnAgnNTPCfgAuthSecretKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_GnAgnNTPCfgAuthSecretKey_Type.__name__ = "OctetString"
_GnAgnNTPCfgAuthSecretKey_Object = MibScalar
gnAgnNTPCfgAuthSecretKey = _GnAgnNTPCfgAuthSecretKey_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 8, 7),
    _GnAgnNTPCfgAuthSecretKey_Type()
)
gnAgnNTPCfgAuthSecretKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnAgnNTPCfgAuthSecretKey.setStatus("mandatory")
_GnAgnNTPCfgAuthPublicKey_Type = Gauge32
_GnAgnNTPCfgAuthPublicKey_Object = MibScalar
gnAgnNTPCfgAuthPublicKey = _GnAgnNTPCfgAuthPublicKey_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 8, 8),
    _GnAgnNTPCfgAuthPublicKey_Type()
)
gnAgnNTPCfgAuthPublicKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnAgnNTPCfgAuthPublicKey.setStatus("mandatory")


class _GnAgnNTPCfgUpdateInterval_Type(Integer32):
    """Custom type gnAgnNTPCfgUpdateInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_GnAgnNTPCfgUpdateInterval_Type.__name__ = "Integer32"
_GnAgnNTPCfgUpdateInterval_Object = MibScalar
gnAgnNTPCfgUpdateInterval = _GnAgnNTPCfgUpdateInterval_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 8, 9),
    _GnAgnNTPCfgUpdateInterval_Type()
)
gnAgnNTPCfgUpdateInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnAgnNTPCfgUpdateInterval.setStatus("mandatory")


class _GnAgnNTPCfgProtocolType_Type(Integer32):
    """Custom type gnAgnNTPCfgProtocolType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ntp", 2),
          ("sntp", 3))
    )


_GnAgnNTPCfgProtocolType_Type.__name__ = "Integer32"
_GnAgnNTPCfgProtocolType_Object = MibScalar
gnAgnNTPCfgProtocolType = _GnAgnNTPCfgProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 8, 10),
    _GnAgnNTPCfgProtocolType_Type()
)
gnAgnNTPCfgProtocolType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnAgnNTPCfgProtocolType.setStatus("mandatory")
_GnAgnInBandMng_ObjectIdentity = ObjectIdentity
gnAgnInBandMng = _GnAgnInBandMng_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 9)
)
_GnAgnInBandMngEthernetIp_Type = IpAddress
_GnAgnInBandMngEthernetIp_Object = MibScalar
gnAgnInBandMngEthernetIp = _GnAgnInBandMngEthernetIp_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 9, 1),
    _GnAgnInBandMngEthernetIp_Type()
)
gnAgnInBandMngEthernetIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnAgnInBandMngEthernetIp.setStatus("mandatory")
_GnAgnInBandMngEthernetMask_Type = IpAddress
_GnAgnInBandMngEthernetMask_Object = MibScalar
gnAgnInBandMngEthernetMask = _GnAgnInBandMngEthernetMask_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 9, 2),
    _GnAgnInBandMngEthernetMask_Type()
)
gnAgnInBandMngEthernetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnAgnInBandMngEthernetMask.setStatus("mandatory")
_GnAgnInBandMngPppIp_Type = IpAddress
_GnAgnInBandMngPppIp_Object = MibScalar
gnAgnInBandMngPppIp = _GnAgnInBandMngPppIp_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 9, 3),
    _GnAgnInBandMngPppIp_Type()
)
gnAgnInBandMngPppIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnAgnInBandMngPppIp.setStatus("mandatory")
_GnAgnInBandMngPppMask_Type = IpAddress
_GnAgnInBandMngPppMask_Object = MibScalar
gnAgnInBandMngPppMask = _GnAgnInBandMngPppMask_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 9, 4),
    _GnAgnInBandMngPppMask_Type()
)
gnAgnInBandMngPppMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnAgnInBandMngPppMask.setStatus("mandatory")
_GnAgnInBandMngDefRoute_Type = IpAddress
_GnAgnInBandMngDefRoute_Object = MibScalar
gnAgnInBandMngDefRoute = _GnAgnInBandMngDefRoute_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 9, 5),
    _GnAgnInBandMngDefRoute_Type()
)
gnAgnInBandMngDefRoute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnAgnInBandMngDefRoute.setStatus("mandatory")


class _GnAgnInBandMngEnable_Type(Integer32):
    """Custom type gnAgnInBandMngEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("enable", 2))
    )


_GnAgnInBandMngEnable_Type.__name__ = "Integer32"
_GnAgnInBandMngEnable_Object = MibScalar
gnAgnInBandMngEnable = _GnAgnInBandMngEnable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 9, 6),
    _GnAgnInBandMngEnable_Type()
)
gnAgnInBandMngEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnAgnInBandMngEnable.setStatus("mandatory")


class _GnAgnInBandMngNetworkElementType_Type(Integer32):
    """Custom type gnAgnInBandMngNetworkElementType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("gateway", 3),
          ("networkElement", 2))
    )


_GnAgnInBandMngNetworkElementType_Type.__name__ = "Integer32"
_GnAgnInBandMngNetworkElementType_Object = MibScalar
gnAgnInBandMngNetworkElementType = _GnAgnInBandMngNetworkElementType_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 9, 7),
    _GnAgnInBandMngNetworkElementType_Type()
)
gnAgnInBandMngNetworkElementType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnAgnInBandMngNetworkElementType.setStatus("mandatory")


class _GnAgnInBandMngRadioChannel_Type(Integer32):
    """Custom type gnAgnInBandMngRadioChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("dccm", 3),
          ("dccr", 2),
          ("mediaSpecific128k", 4),
          ("proprietary", 5),
          ("userChannel", 6))
    )


_GnAgnInBandMngRadioChannel_Type.__name__ = "Integer32"
_GnAgnInBandMngRadioChannel_Object = MibScalar
gnAgnInBandMngRadioChannel = _GnAgnInBandMngRadioChannel_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 9, 8),
    _GnAgnInBandMngRadioChannel_Type()
)
gnAgnInBandMngRadioChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnAgnInBandMngRadioChannel.setStatus("mandatory")


class _GnAgnInBandMngUnknownPackets_Type(Integer32):
    """Custom type gnAgnInBandMngUnknownPackets based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("discard", 3),
          ("transparent", 2))
    )


_GnAgnInBandMngUnknownPackets_Type.__name__ = "Integer32"
_GnAgnInBandMngUnknownPackets_Object = MibScalar
gnAgnInBandMngUnknownPackets = _GnAgnInBandMngUnknownPackets_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 9, 9),
    _GnAgnInBandMngUnknownPackets_Type()
)
gnAgnInBandMngUnknownPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnAgnInBandMngUnknownPackets.setStatus("mandatory")


class _GnAgnInBandMngTTL_Type(Integer32):
    """Custom type gnAgnInBandMngTTL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 64),
    )


_GnAgnInBandMngTTL_Type.__name__ = "Integer32"
_GnAgnInBandMngTTL_Object = MibScalar
gnAgnInBandMngTTL = _GnAgnInBandMngTTL_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 9, 10),
    _GnAgnInBandMngTTL_Type()
)
gnAgnInBandMngTTL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnAgnInBandMngTTL.setStatus("mandatory")
_GnAgnInBandMngRingIpSubnet_Type = IpAddress
_GnAgnInBandMngRingIpSubnet_Object = MibScalar
gnAgnInBandMngRingIpSubnet = _GnAgnInBandMngRingIpSubnet_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 9, 11),
    _GnAgnInBandMngRingIpSubnet_Type()
)
gnAgnInBandMngRingIpSubnet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnAgnInBandMngRingIpSubnet.setStatus("mandatory")
_GnAgnInBandMngRingIpMask_Type = IpAddress
_GnAgnInBandMngRingIpMask_Object = MibScalar
gnAgnInBandMngRingIpMask = _GnAgnInBandMngRingIpMask_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 9, 12),
    _GnAgnInBandMngRingIpMask_Type()
)
gnAgnInBandMngRingIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnAgnInBandMngRingIpMask.setStatus("mandatory")


class _GnAgnInBandMngNetworkId_Type(Integer32):
    """Custom type gnAgnInBandMngNetworkId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_GnAgnInBandMngNetworkId_Type.__name__ = "Integer32"
_GnAgnInBandMngNetworkId_Object = MibScalar
gnAgnInBandMngNetworkId = _GnAgnInBandMngNetworkId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 9, 13),
    _GnAgnInBandMngNetworkId_Type()
)
gnAgnInBandMngNetworkId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnAgnInBandMngNetworkId.setStatus("mandatory")


class _GnAgnInBandMngLineMode_Type(Integer32):
    """Custom type gnAgnInBandMngLineMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("forcePPPoE", 3),
          ("inbandFiber", 2))
    )


_GnAgnInBandMngLineMode_Type.__name__ = "Integer32"
_GnAgnInBandMngLineMode_Object = MibScalar
gnAgnInBandMngLineMode = _GnAgnInBandMngLineMode_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 9, 14),
    _GnAgnInBandMngLineMode_Type()
)
gnAgnInBandMngLineMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnAgnInBandMngLineMode.setStatus("mandatory")


class _GnAgnInBandMngFiberChannel_Type(Integer32):
    """Custom type gnAgnInBandMngFiberChannel based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              5)
        )
    )
    namedValues = NamedValues(
        *(("dccm", 3),
          ("dccr", 2),
          ("userChannel", 5))
    )


_GnAgnInBandMngFiberChannel_Type.__name__ = "Integer32"
_GnAgnInBandMngFiberChannel_Object = MibScalar
gnAgnInBandMngFiberChannel = _GnAgnInBandMngFiberChannel_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 9, 15),
    _GnAgnInBandMngFiberChannel_Type()
)
gnAgnInBandMngFiberChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnAgnInBandMngFiberChannel.setStatus("mandatory")


class _GnAgnInBandMngTribChannel_Type(Integer32):
    """Custom type gnAgnInBandMngTribChannel based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("dccm", 4),
          ("dccr", 3),
          ("disable", 2))
    )


_GnAgnInBandMngTribChannel_Type.__name__ = "Integer32"
_GnAgnInBandMngTribChannel_Object = MibScalar
gnAgnInBandMngTribChannel = _GnAgnInBandMngTribChannel_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 9, 16),
    _GnAgnInBandMngTribChannel_Type()
)
gnAgnInBandMngTribChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnAgnInBandMngTribChannel.setStatus("mandatory")
_GnAgnInBandMngXChannelTable_Object = MibTable
gnAgnInBandMngXChannelTable = _GnAgnInBandMngXChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 9, 17)
)
if mibBuilder.loadTexts:
    gnAgnInBandMngXChannelTable.setStatus("mandatory")
_GnAgnInBandMngXChannelEntry_Object = MibTableRow
gnAgnInBandMngXChannelEntry = _GnAgnInBandMngXChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 9, 17, 1)
)
gnAgnInBandMngXChannelEntry.setIndexNames(
    (0, "CERAGON-MIB", "gnAgnInBandMngXChannelId"),
)
if mibBuilder.loadTexts:
    gnAgnInBandMngXChannelEntry.setStatus("mandatory")


class _GnAgnInBandMngXChannelId_Type(Integer32):
    """Custom type gnAgnInBandMngXChannelId based on Integer32"""
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
        *(("channel1", 1),
          ("channel2", 2),
          ("channel3", 3),
          ("channel4", 4))
    )


_GnAgnInBandMngXChannelId_Type.__name__ = "Integer32"
_GnAgnInBandMngXChannelId_Object = MibTableColumn
gnAgnInBandMngXChannelId = _GnAgnInBandMngXChannelId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 9, 17, 1, 1),
    _GnAgnInBandMngXChannelId_Type()
)
gnAgnInBandMngXChannelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnAgnInBandMngXChannelId.setStatus("mandatory")
_GnAgnInBandMngXChannelIfIndex_Type = Integer32
_GnAgnInBandMngXChannelIfIndex_Object = MibTableColumn
gnAgnInBandMngXChannelIfIndex = _GnAgnInBandMngXChannelIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 9, 17, 1, 2),
    _GnAgnInBandMngXChannelIfIndex_Type()
)
gnAgnInBandMngXChannelIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnAgnInBandMngXChannelIfIndex.setStatus("mandatory")


class _GnAgnInBandMngXChannelType_Type(Integer32):
    """Custom type gnAgnInBandMngXChannelType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("dccm", 4),
          ("dccr", 3),
          ("mediaspecific", 5),
          ("pppoe", 6),
          ("proprietary", 2))
    )


_GnAgnInBandMngXChannelType_Type.__name__ = "Integer32"
_GnAgnInBandMngXChannelType_Object = MibTableColumn
gnAgnInBandMngXChannelType = _GnAgnInBandMngXChannelType_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 9, 17, 1, 3),
    _GnAgnInBandMngXChannelType_Type()
)
gnAgnInBandMngXChannelType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnAgnInBandMngXChannelType.setStatus("mandatory")


class _GnAgnInBandMngXChannelState_Type(Integer32):
    """Custom type gnAgnInBandMngXChannelState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("enable", 2))
    )


_GnAgnInBandMngXChannelState_Type.__name__ = "Integer32"
_GnAgnInBandMngXChannelState_Object = MibTableColumn
gnAgnInBandMngXChannelState = _GnAgnInBandMngXChannelState_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 9, 17, 1, 4),
    _GnAgnInBandMngXChannelState_Type()
)
gnAgnInBandMngXChannelState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnAgnInBandMngXChannelState.setStatus("mandatory")
_GnAgnInBandMngXChannelNeighborIP_Type = IpAddress
_GnAgnInBandMngXChannelNeighborIP_Object = MibTableColumn
gnAgnInBandMngXChannelNeighborIP = _GnAgnInBandMngXChannelNeighborIP_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 9, 17, 1, 5),
    _GnAgnInBandMngXChannelNeighborIP_Type()
)
gnAgnInBandMngXChannelNeighborIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnAgnInBandMngXChannelNeighborIP.setStatus("mandatory")


class _GnAgnInBandMngXChannelStatus_Type(Integer32):
    """Custom type gnAgnInBandMngXChannelStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("closed", 4),
          ("down", 3),
          ("up", 2))
    )


_GnAgnInBandMngXChannelStatus_Type.__name__ = "Integer32"
_GnAgnInBandMngXChannelStatus_Object = MibTableColumn
gnAgnInBandMngXChannelStatus = _GnAgnInBandMngXChannelStatus_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 9, 17, 1, 6),
    _GnAgnInBandMngXChannelStatus_Type()
)
gnAgnInBandMngXChannelStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnAgnInBandMngXChannelStatus.setStatus("mandatory")


class _GnAgnInBandMngXEnableInbandChannels_Type(Integer32):
    """Custom type gnAgnInBandMngXEnableInbandChannels based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_GnAgnInBandMngXEnableInbandChannels_Type.__name__ = "Integer32"
_GnAgnInBandMngXEnableInbandChannels_Object = MibScalar
gnAgnInBandMngXEnableInbandChannels = _GnAgnInBandMngXEnableInbandChannels_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 9, 18),
    _GnAgnInBandMngXEnableInbandChannels_Type()
)
gnAgnInBandMngXEnableInbandChannels.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnAgnInBandMngXEnableInbandChannels.setStatus("mandatory")


class _GnAgnInBandMngMainGNEInterface_Type(Integer32):
    """Custom type gnAgnInBandMngMainGNEInterface based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("channel1", 3),
          ("channel2", 4),
          ("channel3", 5),
          ("channel4", 6),
          ("default", 2))
    )


_GnAgnInBandMngMainGNEInterface_Type.__name__ = "Integer32"
_GnAgnInBandMngMainGNEInterface_Object = MibScalar
gnAgnInBandMngMainGNEInterface = _GnAgnInBandMngMainGNEInterface_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 9, 19),
    _GnAgnInBandMngMainGNEInterface_Type()
)
gnAgnInBandMngMainGNEInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnAgnInBandMngMainGNEInterface.setStatus("mandatory")
_GnNeighborIP_ObjectIdentity = ObjectIdentity
gnNeighborIP = _GnNeighborIP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 10)
)
_GnNeighborInBandTable_Object = MibTable
gnNeighborInBandTable = _GnNeighborInBandTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 10, 1)
)
if mibBuilder.loadTexts:
    gnNeighborInBandTable.setStatus("mandatory")
_GnNeighborInBandEntry_Object = MibTableRow
gnNeighborInBandEntry = _GnNeighborInBandEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 10, 1, 1)
)
gnNeighborInBandEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    gnNeighborInBandEntry.setStatus("mandatory")
_GnNeighborInBandIP_Type = IpAddress
_GnNeighborInBandIP_Object = MibTableColumn
gnNeighborInBandIP = _GnNeighborInBandIP_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 10, 1, 1, 1),
    _GnNeighborInBandIP_Type()
)
gnNeighborInBandIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnNeighborInBandIP.setStatus("mandatory")


class _GnNeighborInBandStatus_Type(Integer32):
    """Custom type gnNeighborInBandStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("closed", 4),
          ("down", 3),
          ("up", 2))
    )


_GnNeighborInBandStatus_Type.__name__ = "Integer32"
_GnNeighborInBandStatus_Object = MibTableColumn
gnNeighborInBandStatus = _GnNeighborInBandStatus_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 10, 1, 1, 2),
    _GnNeighborInBandStatus_Type()
)
gnNeighborInBandStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnNeighborInBandStatus.setStatus("mandatory")
_GnNeighborMateIP_Type = IpAddress
_GnNeighborMateIP_Object = MibScalar
gnNeighborMateIP = _GnNeighborMateIP_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 10, 2),
    _GnNeighborMateIP_Type()
)
gnNeighborMateIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnNeighborMateIP.setStatus("mandatory")
_GnNeighborRemoteRadioIP_Type = IpAddress
_GnNeighborRemoteRadioIP_Object = MibScalar
gnNeighborRemoteRadioIP = _GnNeighborRemoteRadioIP_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 10, 3),
    _GnNeighborRemoteRadioIP_Type()
)
gnNeighborRemoteRadioIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnNeighborRemoteRadioIP.setStatus("mandatory")
_GnNeighborInBandXTable_Object = MibTable
gnNeighborInBandXTable = _GnNeighborInBandXTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 10, 4)
)
if mibBuilder.loadTexts:
    gnNeighborInBandXTable.setStatus("mandatory")
_GnNeighborInBandXEntry_Object = MibTableRow
gnNeighborInBandXEntry = _GnNeighborInBandXEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 10, 4, 1)
)
gnNeighborInBandXEntry.setIndexNames(
    (0, "CERAGON-MIB", "gnNeighborInBandXId"),
)
if mibBuilder.loadTexts:
    gnNeighborInBandXEntry.setStatus("mandatory")


class _GnNeighborInBandXId_Type(Integer32):
    """Custom type gnNeighborInBandXId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("drawer1", 3),
          ("drawer2", 4))
    )


_GnNeighborInBandXId_Type.__name__ = "Integer32"
_GnNeighborInBandXId_Object = MibTableColumn
gnNeighborInBandXId = _GnNeighborInBandXId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 10, 4, 1, 1),
    _GnNeighborInBandXId_Type()
)
gnNeighborInBandXId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnNeighborInBandXId.setStatus("mandatory")
_GnNeighborInBandXIP_Type = IpAddress
_GnNeighborInBandXIP_Object = MibTableColumn
gnNeighborInBandXIP = _GnNeighborInBandXIP_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 10, 4, 1, 2),
    _GnNeighborInBandXIP_Type()
)
gnNeighborInBandXIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnNeighborInBandXIP.setStatus("mandatory")
_GnNeighborIpTable_Object = MibTable
gnNeighborIpTable = _GnNeighborIpTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 10, 5)
)
if mibBuilder.loadTexts:
    gnNeighborIpTable.setStatus("mandatory")
_GnNeighborIpEntry_Object = MibTableRow
gnNeighborIpEntry = _GnNeighborIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 10, 5, 1)
)
gnNeighborIpEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    gnNeighborIpEntry.setStatus("mandatory")


class _GnNeighborIpDetectMode_Type(Integer32):
    """Custom type gnNeighborIpDetectMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("auto", 4),
          ("disable", 2),
          ("manual", 3))
    )


_GnNeighborIpDetectMode_Type.__name__ = "Integer32"
_GnNeighborIpDetectMode_Object = MibTableColumn
gnNeighborIpDetectMode = _GnNeighborIpDetectMode_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 10, 5, 1, 1),
    _GnNeighborIpDetectMode_Type()
)
gnNeighborIpDetectMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnNeighborIpDetectMode.setStatus("mandatory")
_GnNeighborIpAddress_Type = IpAddress
_GnNeighborIpAddress_Object = MibTableColumn
gnNeighborIpAddress = _GnNeighborIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 10, 5, 1, 2),
    _GnNeighborIpAddress_Type()
)
gnNeighborIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnNeighborIpAddress.setStatus("mandatory")
_GnNeighborIpRemoteIfIndex_Type = Integer32
_GnNeighborIpRemoteIfIndex_Object = MibTableColumn
gnNeighborIpRemoteIfIndex = _GnNeighborIpRemoteIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 10, 5, 1, 3),
    _GnNeighborIpRemoteIfIndex_Type()
)
gnNeighborIpRemoteIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnNeighborIpRemoteIfIndex.setStatus("mandatory")


class _GnNeighborIpRemoteType_Type(Integer32):
    """Custom type gnNeighborIpRemoteType based on Integer32"""
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
        *(("access", 2),
          ("adm", 3),
          ("admline2line", 5),
          ("regenerator", 1),
          ("unit1500p", 4))
    )


_GnNeighborIpRemoteType_Type.__name__ = "Integer32"
_GnNeighborIpRemoteType_Object = MibTableColumn
gnNeighborIpRemoteType = _GnNeighborIpRemoteType_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 10, 5, 1, 4),
    _GnNeighborIpRemoteType_Type()
)
gnNeighborIpRemoteType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnNeighborIpRemoteType.setStatus("mandatory")
_GnAgnSNMPCfg_ObjectIdentity = ObjectIdentity
gnAgnSNMPCfg = _GnAgnSNMPCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 11)
)


class _GnAgnSNMPCfgTrapCommunity_Type(OctetString):
    """Custom type gnAgnSNMPCfgTrapCommunity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )


_GnAgnSNMPCfgTrapCommunity_Type.__name__ = "OctetString"
_GnAgnSNMPCfgTrapCommunity_Object = MibScalar
gnAgnSNMPCfgTrapCommunity = _GnAgnSNMPCfgTrapCommunity_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 11, 1),
    _GnAgnSNMPCfgTrapCommunity_Type()
)
gnAgnSNMPCfgTrapCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnAgnSNMPCfgTrapCommunity.setStatus("mandatory")


class _GnAgnSNMPCfgReadCommunity_Type(OctetString):
    """Custom type gnAgnSNMPCfgReadCommunity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )


_GnAgnSNMPCfgReadCommunity_Type.__name__ = "OctetString"
_GnAgnSNMPCfgReadCommunity_Object = MibScalar
gnAgnSNMPCfgReadCommunity = _GnAgnSNMPCfgReadCommunity_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 11, 2),
    _GnAgnSNMPCfgReadCommunity_Type()
)
gnAgnSNMPCfgReadCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnAgnSNMPCfgReadCommunity.setStatus("mandatory")


class _GnAgnSNMPCfgWriteCommunity_Type(OctetString):
    """Custom type gnAgnSNMPCfgWriteCommunity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )


_GnAgnSNMPCfgWriteCommunity_Type.__name__ = "OctetString"
_GnAgnSNMPCfgWriteCommunity_Object = MibScalar
gnAgnSNMPCfgWriteCommunity = _GnAgnSNMPCfgWriteCommunity_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 11, 3),
    _GnAgnSNMPCfgWriteCommunity_Type()
)
gnAgnSNMPCfgWriteCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnAgnSNMPCfgWriteCommunity.setStatus("mandatory")
_GnAgnPrvt_ObjectIdentity = ObjectIdentity
gnAgnPrvt = _GnAgnPrvt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 12)
)


class _GnAgnPrvtCmd_Type(Integer32):
    """Custom type gnAgnPrvtCmd based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("cNV", 3),
          ("cNVBtr", 4),
          ("noOperation", 2))
    )


_GnAgnPrvtCmd_Type.__name__ = "Integer32"
_GnAgnPrvtCmd_Object = MibScalar
gnAgnPrvtCmd = _GnAgnPrvtCmd_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 12, 1),
    _GnAgnPrvtCmd_Type()
)
gnAgnPrvtCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnAgnPrvtCmd.setStatus("mandatory")


class _GnAgnPrvtCmdStat_Type(Integer32):
    """Custom type gnAgnPrvtCmdStat based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("cNVBtrFail", 6),
          ("cNVBtrPass", 5),
          ("cNVFail", 4),
          ("cNVPass", 3),
          ("ready", 2))
    )


_GnAgnPrvtCmdStat_Type.__name__ = "Integer32"
_GnAgnPrvtCmdStat_Object = MibScalar
gnAgnPrvtCmdStat = _GnAgnPrvtCmdStat_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 12, 2),
    _GnAgnPrvtCmdStat_Type()
)
gnAgnPrvtCmdStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnAgnPrvtCmdStat.setStatus("mandatory")
_GnSoftwareDrawerVersionTable_Object = MibTable
gnSoftwareDrawerVersionTable = _GnSoftwareDrawerVersionTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 13)
)
if mibBuilder.loadTexts:
    gnSoftwareDrawerVersionTable.setStatus("mandatory")
_GnSoftwareDrawerVersionEntry_Object = MibTableRow
gnSoftwareDrawerVersionEntry = _GnSoftwareDrawerVersionEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 13, 1)
)
gnSoftwareDrawerVersionEntry.setIndexNames(
    (0, "CERAGON-MIB", "gnSoftwareDrawerId"),
)
if mibBuilder.loadTexts:
    gnSoftwareDrawerVersionEntry.setStatus("mandatory")


class _GnSoftwareDrawerId_Type(Integer32):
    """Custom type gnSoftwareDrawerId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("drawer1", 3),
          ("drawer2", 4))
    )


_GnSoftwareDrawerId_Type.__name__ = "Integer32"
_GnSoftwareDrawerId_Object = MibTableColumn
gnSoftwareDrawerId = _GnSoftwareDrawerId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 13, 1, 1),
    _GnSoftwareDrawerId_Type()
)
gnSoftwareDrawerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnSoftwareDrawerId.setStatus("mandatory")


class _GnSoftwareDrawerVersionMUX_Type(DisplayString):
    """Custom type gnSoftwareDrawerVersionMUX based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_GnSoftwareDrawerVersionMUX_Type.__name__ = "DisplayString"
_GnSoftwareDrawerVersionMUX_Object = MibTableColumn
gnSoftwareDrawerVersionMUX = _GnSoftwareDrawerVersionMUX_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 13, 1, 2),
    _GnSoftwareDrawerVersionMUX_Type()
)
gnSoftwareDrawerVersionMUX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnSoftwareDrawerVersionMUX.setStatus("mandatory")


class _GnSoftwareDrawerVersionMUXPostResetVersion_Type(DisplayString):
    """Custom type gnSoftwareDrawerVersionMUXPostResetVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_GnSoftwareDrawerVersionMUXPostResetVersion_Type.__name__ = "DisplayString"
_GnSoftwareDrawerVersionMUXPostResetVersion_Object = MibTableColumn
gnSoftwareDrawerVersionMUXPostResetVersion = _GnSoftwareDrawerVersionMUXPostResetVersion_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 13, 1, 3),
    _GnSoftwareDrawerVersionMUXPostResetVersion_Type()
)
gnSoftwareDrawerVersionMUXPostResetVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnSoftwareDrawerVersionMUXPostResetVersion.setStatus("mandatory")


class _GnSoftwareDrawerVersionODU_Type(DisplayString):
    """Custom type gnSoftwareDrawerVersionODU based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_GnSoftwareDrawerVersionODU_Type.__name__ = "DisplayString"
_GnSoftwareDrawerVersionODU_Object = MibTableColumn
gnSoftwareDrawerVersionODU = _GnSoftwareDrawerVersionODU_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 13, 1, 4),
    _GnSoftwareDrawerVersionODU_Type()
)
gnSoftwareDrawerVersionODU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnSoftwareDrawerVersionODU.setStatus("mandatory")


class _GnSoftwareDrawerVersionODUPostResetVersion_Type(DisplayString):
    """Custom type gnSoftwareDrawerVersionODUPostResetVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_GnSoftwareDrawerVersionODUPostResetVersion_Type.__name__ = "DisplayString"
_GnSoftwareDrawerVersionODUPostResetVersion_Object = MibTableColumn
gnSoftwareDrawerVersionODUPostResetVersion = _GnSoftwareDrawerVersionODUPostResetVersion_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 13, 1, 5),
    _GnSoftwareDrawerVersionODUPostResetVersion_Type()
)
gnSoftwareDrawerVersionODUPostResetVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnSoftwareDrawerVersionODUPostResetVersion.setStatus("mandatory")


class _GnSoftwareDrawerVersionModemFile_Type(DisplayString):
    """Custom type gnSoftwareDrawerVersionModemFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_GnSoftwareDrawerVersionModemFile_Type.__name__ = "DisplayString"
_GnSoftwareDrawerVersionModemFile_Object = MibTableColumn
gnSoftwareDrawerVersionModemFile = _GnSoftwareDrawerVersionModemFile_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 13, 1, 6),
    _GnSoftwareDrawerVersionModemFile_Type()
)
gnSoftwareDrawerVersionModemFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnSoftwareDrawerVersionModemFile.setStatus("mandatory")


class _GnSoftwareDrawerVersionModemFilePostResetVersion_Type(DisplayString):
    """Custom type gnSoftwareDrawerVersionModemFilePostResetVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_GnSoftwareDrawerVersionModemFilePostResetVersion_Type.__name__ = "DisplayString"
_GnSoftwareDrawerVersionModemFilePostResetVersion_Object = MibTableColumn
gnSoftwareDrawerVersionModemFilePostResetVersion = _GnSoftwareDrawerVersionModemFilePostResetVersion_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 13, 1, 7),
    _GnSoftwareDrawerVersionModemFilePostResetVersion_Type()
)
gnSoftwareDrawerVersionModemFilePostResetVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnSoftwareDrawerVersionModemFilePostResetVersion.setStatus("mandatory")


class _GnSoftwareDrawerVersionModemScript_Type(DisplayString):
    """Custom type gnSoftwareDrawerVersionModemScript based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_GnSoftwareDrawerVersionModemScript_Type.__name__ = "DisplayString"
_GnSoftwareDrawerVersionModemScript_Object = MibTableColumn
gnSoftwareDrawerVersionModemScript = _GnSoftwareDrawerVersionModemScript_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 13, 1, 8),
    _GnSoftwareDrawerVersionModemScript_Type()
)
gnSoftwareDrawerVersionModemScript.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnSoftwareDrawerVersionModemScript.setStatus("mandatory")


class _GnSoftwareDrawerVersionModemScriptPostResetVersion_Type(DisplayString):
    """Custom type gnSoftwareDrawerVersionModemScriptPostResetVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_GnSoftwareDrawerVersionModemScriptPostResetVersion_Type.__name__ = "DisplayString"
_GnSoftwareDrawerVersionModemScriptPostResetVersion_Object = MibTableColumn
gnSoftwareDrawerVersionModemScriptPostResetVersion = _GnSoftwareDrawerVersionModemScriptPostResetVersion_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 13, 1, 9),
    _GnSoftwareDrawerVersionModemScriptPostResetVersion_Type()
)
gnSoftwareDrawerVersionModemScriptPostResetVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnSoftwareDrawerVersionModemScriptPostResetVersion.setStatus("mandatory")


class _GnSoftwareDrawerVersionRfuFpgaVersion_Type(DisplayString):
    """Custom type gnSoftwareDrawerVersionRfuFpgaVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_GnSoftwareDrawerVersionRfuFpgaVersion_Type.__name__ = "DisplayString"
_GnSoftwareDrawerVersionRfuFpgaVersion_Object = MibTableColumn
gnSoftwareDrawerVersionRfuFpgaVersion = _GnSoftwareDrawerVersionRfuFpgaVersion_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 13, 1, 10),
    _GnSoftwareDrawerVersionRfuFpgaVersion_Type()
)
gnSoftwareDrawerVersionRfuFpgaVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnSoftwareDrawerVersionRfuFpgaVersion.setStatus("mandatory")
_GnAgnCurrentAlarm_ObjectIdentity = ObjectIdentity
gnAgnCurrentAlarm = _GnAgnCurrentAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 14)
)
_GnAgnCurrentAlarmLastChange_Type = Integer32
_GnAgnCurrentAlarmLastChange_Object = MibScalar
gnAgnCurrentAlarmLastChange = _GnAgnCurrentAlarmLastChange_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 14, 1),
    _GnAgnCurrentAlarmLastChange_Type()
)
gnAgnCurrentAlarmLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnAgnCurrentAlarmLastChange.setStatus("mandatory")
_GnAgnCurrentAlarmTable_Object = MibTable
gnAgnCurrentAlarmTable = _GnAgnCurrentAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 14, 2)
)
if mibBuilder.loadTexts:
    gnAgnCurrentAlarmTable.setStatus("mandatory")
_GnAgnCurrentAlarmEntry_Object = MibTableRow
gnAgnCurrentAlarmEntry = _GnAgnCurrentAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 14, 2, 1)
)
gnAgnCurrentAlarmEntry.setIndexNames(
    (0, "CERAGON-MIB", "gnAgnCurrentAlarmCounter"),
)
if mibBuilder.loadTexts:
    gnAgnCurrentAlarmEntry.setStatus("mandatory")
_GnAgnCurrentAlarmCounter_Type = Integer32
_GnAgnCurrentAlarmCounter_Object = MibTableColumn
gnAgnCurrentAlarmCounter = _GnAgnCurrentAlarmCounter_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 14, 2, 1, 1),
    _GnAgnCurrentAlarmCounter_Type()
)
gnAgnCurrentAlarmCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnAgnCurrentAlarmCounter.setStatus("mandatory")


class _GnAgnCurrentAlarmSeverity_Type(Integer32):
    """Custom type gnAgnCurrentAlarmSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              7,
              15,
              31)
        )
    )
    namedValues = NamedValues(
        *(("critical", 31),
          ("event", 1),
          ("major", 15),
          ("minor", 7),
          ("warning", 3))
    )


_GnAgnCurrentAlarmSeverity_Type.__name__ = "Integer32"
_GnAgnCurrentAlarmSeverity_Object = MibTableColumn
gnAgnCurrentAlarmSeverity = _GnAgnCurrentAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 14, 2, 1, 2),
    _GnAgnCurrentAlarmSeverity_Type()
)
gnAgnCurrentAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnAgnCurrentAlarmSeverity.setStatus("mandatory")
_GnAgnCurrentAlarmId_Type = Integer32
_GnAgnCurrentAlarmId_Object = MibTableColumn
gnAgnCurrentAlarmId = _GnAgnCurrentAlarmId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 14, 2, 1, 3),
    _GnAgnCurrentAlarmId_Type()
)
gnAgnCurrentAlarmId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnAgnCurrentAlarmId.setStatus("mandatory")
_GnAgnCurrentAlarmIfIndex_Type = Integer32
_GnAgnCurrentAlarmIfIndex_Object = MibTableColumn
gnAgnCurrentAlarmIfIndex = _GnAgnCurrentAlarmIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 14, 2, 1, 4),
    _GnAgnCurrentAlarmIfIndex_Type()
)
gnAgnCurrentAlarmIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnAgnCurrentAlarmIfIndex.setStatus("mandatory")


class _GnAgnCurrentAlarmOrigin_Type(Integer32):
    """Custom type gnAgnCurrentAlarmOrigin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              257,
              258,
              259,
              260,
              261,
              262,
              263,
              264,
              265,
              513,
              514,
              515,
              516,
              517,
              518,
              519,
              520,
              521,
              522,
              523,
              524,
              525,
              526,
              527,
              769,
              770,
              771,
              772,
              773,
              774)
        )
    )
    namedValues = NamedValues(
        *(("drawer1", 3),
          ("drawer2", 4),
          ("idc", 2),
          ("interfaces", 1),
          ("tDrawer1", 513),
          ("tDrawer10", 522),
          ("tDrawer11", 523),
          ("tDrawer12", 524),
          ("tDrawer13", 525),
          ("tDrawer14", 526),
          ("tDrawer15", 527),
          ("tDrawer2", 514),
          ("tDrawer3", 515),
          ("tDrawer4", 516),
          ("tDrawer5", 517),
          ("tDrawer6", 518),
          ("tDrawer7", 519),
          ("tDrawer8", 520),
          ("tDrawer9", 521),
          ("tIdc1", 257),
          ("tIdc2", 258),
          ("tIdc3", 259),
          ("tIdc4", 260),
          ("tIdc5", 261),
          ("tIdc6", 262),
          ("tIdc7", 263),
          ("tIdc8", 264),
          ("tIdc9", 265),
          ("tXC1", 769),
          ("tXC2", 770),
          ("tXC3", 771),
          ("tXC4", 772),
          ("tXC5", 773),
          ("tXC6", 774),
          ("unKnown", 5))
    )


_GnAgnCurrentAlarmOrigin_Type.__name__ = "Integer32"
_GnAgnCurrentAlarmOrigin_Object = MibTableColumn
gnAgnCurrentAlarmOrigin = _GnAgnCurrentAlarmOrigin_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 14, 2, 1, 5),
    _GnAgnCurrentAlarmOrigin_Type()
)
gnAgnCurrentAlarmOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnAgnCurrentAlarmOrigin.setStatus("mandatory")


class _GnAgnCurrentAlarmUnit_Type(Integer32):
    """Custom type gnAgnCurrentAlarmUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6,
              7,
              9)
        )
    )
    namedValues = NamedValues(
        *(("drawer", 6),
          ("idc", 2),
          ("modem", 5),
          ("mux", 4),
          ("odu", 3),
          ("unKnown", 7),
          ("xc", 9))
    )


_GnAgnCurrentAlarmUnit_Type.__name__ = "Integer32"
_GnAgnCurrentAlarmUnit_Object = MibTableColumn
gnAgnCurrentAlarmUnit = _GnAgnCurrentAlarmUnit_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 14, 2, 1, 6),
    _GnAgnCurrentAlarmUnit_Type()
)
gnAgnCurrentAlarmUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnAgnCurrentAlarmUnit.setStatus("mandatory")
_GnAgnCurrentAlarmTrapID_Type = Integer32
_GnAgnCurrentAlarmTrapID_Object = MibTableColumn
gnAgnCurrentAlarmTrapID = _GnAgnCurrentAlarmTrapID_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 14, 2, 1, 7),
    _GnAgnCurrentAlarmTrapID_Type()
)
gnAgnCurrentAlarmTrapID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnAgnCurrentAlarmTrapID.setStatus("mandatory")
_GnAgnCurrentAlarmTimeT_Type = Integer32
_GnAgnCurrentAlarmTimeT_Object = MibTableColumn
gnAgnCurrentAlarmTimeT = _GnAgnCurrentAlarmTimeT_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 14, 2, 1, 8),
    _GnAgnCurrentAlarmTimeT_Type()
)
gnAgnCurrentAlarmTimeT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnAgnCurrentAlarmTimeT.setStatus("mandatory")
_GnAgnCurrentAlarmText_Type = DisplayString
_GnAgnCurrentAlarmText_Object = MibTableColumn
gnAgnCurrentAlarmText = _GnAgnCurrentAlarmText_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 14, 2, 1, 9),
    _GnAgnCurrentAlarmText_Type()
)
gnAgnCurrentAlarmText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnAgnCurrentAlarmText.setStatus("mandatory")
_GnNMS_ObjectIdentity = ObjectIdentity
gnNMS = _GnNMS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 15)
)
_GnApplicFileTable_Object = MibTable
gnApplicFileTable = _GnApplicFileTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 16)
)
if mibBuilder.loadTexts:
    gnApplicFileTable.setStatus("mandatory")
_GnApplicFileEntry_Object = MibTableRow
gnApplicFileEntry = _GnApplicFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 16, 1)
)
gnApplicFileEntry.setIndexNames(
    (0, "CERAGON-MIB", "gnApplicFileId"),
)
if mibBuilder.loadTexts:
    gnApplicFileEntry.setStatus("mandatory")
_GnApplicFileId_Type = Integer32
_GnApplicFileId_Object = MibTableColumn
gnApplicFileId = _GnApplicFileId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 16, 1, 1),
    _GnApplicFileId_Type()
)
gnApplicFileId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnApplicFileId.setStatus("mandatory")


class _GnApplicFileName_Type(DisplayString):
    """Custom type gnApplicFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_GnApplicFileName_Type.__name__ = "DisplayString"
_GnApplicFileName_Object = MibTableColumn
gnApplicFileName = _GnApplicFileName_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 16, 1, 2),
    _GnApplicFileName_Type()
)
gnApplicFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnApplicFileName.setStatus("mandatory")


class _GnApplicFileVersion_Type(DisplayString):
    """Custom type gnApplicFileVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_GnApplicFileVersion_Type.__name__ = "DisplayString"
_GnApplicFileVersion_Object = MibTableColumn
gnApplicFileVersion = _GnApplicFileVersion_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 16, 1, 3),
    _GnApplicFileVersion_Type()
)
gnApplicFileVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnApplicFileVersion.setStatus("mandatory")


class _GnApplicFileCreateDate_Type(OctetString):
    """Custom type gnApplicFileCreateDate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_GnApplicFileCreateDate_Type.__name__ = "OctetString"
_GnApplicFileCreateDate_Object = MibTableColumn
gnApplicFileCreateDate = _GnApplicFileCreateDate_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 16, 1, 4),
    _GnApplicFileCreateDate_Type()
)
gnApplicFileCreateDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnApplicFileCreateDate.setStatus("mandatory")


class _GnApplicFileDownloadDate_Type(OctetString):
    """Custom type gnApplicFileDownloadDate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_GnApplicFileDownloadDate_Type.__name__ = "OctetString"
_GnApplicFileDownloadDate_Object = MibTableColumn
gnApplicFileDownloadDate = _GnApplicFileDownloadDate_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 16, 1, 5),
    _GnApplicFileDownloadDate_Type()
)
gnApplicFileDownloadDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnApplicFileDownloadDate.setStatus("mandatory")


class _GnApplicFileType_Type(Integer32):
    """Custom type gnApplicFileType based on Integer32"""
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("aAux", 14),
          ("boot", 5),
          ("bootRom", 8),
          ("frameConfigTable", 16),
          ("idc", 1),
          ("license", 15),
          ("modem", 4),
          ("modemConfig", 6),
          ("mrmcTable", 11),
          ("mux", 2),
          ("odu", 3),
          ("rfuConfig", 10),
          ("rfuFpga", 9),
          ("wayside", 7),
          ("xc", 12),
          ("xcErrorgen", 13))
    )


_GnApplicFileType_Type.__name__ = "Integer32"
_GnApplicFileType_Object = MibTableColumn
gnApplicFileType = _GnApplicFileType_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 16, 1, 6),
    _GnApplicFileType_Type()
)
gnApplicFileType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnApplicFileType.setStatus("mandatory")


class _GnApplicFileSubType_Type(DisplayString):
    """Custom type gnApplicFileSubType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_GnApplicFileSubType_Type.__name__ = "DisplayString"
_GnApplicFileSubType_Object = MibTableColumn
gnApplicFileSubType = _GnApplicFileSubType_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 16, 1, 7),
    _GnApplicFileSubType_Type()
)
gnApplicFileSubType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnApplicFileSubType.setStatus("mandatory")
_GnApplicFileFirmware_Type = Integer32
_GnApplicFileFirmware_Object = MibTableColumn
gnApplicFileFirmware = _GnApplicFileFirmware_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 16, 1, 8),
    _GnApplicFileFirmware_Type()
)
gnApplicFileFirmware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnApplicFileFirmware.setStatus("mandatory")
_GnApplicFileGeneralPurpose_Type = Integer32
_GnApplicFileGeneralPurpose_Object = MibTableColumn
gnApplicFileGeneralPurpose = _GnApplicFileGeneralPurpose_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 16, 1, 9),
    _GnApplicFileGeneralPurpose_Type()
)
gnApplicFileGeneralPurpose.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnApplicFileGeneralPurpose.setStatus("mandatory")
_GnApplicFileSize_Type = Integer32
_GnApplicFileSize_Object = MibTableColumn
gnApplicFileSize = _GnApplicFileSize_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 16, 1, 10),
    _GnApplicFileSize_Type()
)
gnApplicFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnApplicFileSize.setStatus("mandatory")


class _GnApplicFileCompressed_Type(Integer32):
    """Custom type gnApplicFileCompressed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 3),
          ("yes", 2))
    )


_GnApplicFileCompressed_Type.__name__ = "Integer32"
_GnApplicFileCompressed_Object = MibTableColumn
gnApplicFileCompressed = _GnApplicFileCompressed_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 16, 1, 11),
    _GnApplicFileCompressed_Type()
)
gnApplicFileCompressed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnApplicFileCompressed.setStatus("mandatory")


class _GnApplicFileDssSupport_Type(Integer32):
    """Custom type gnApplicFileDssSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 3),
          ("yes", 2))
    )


_GnApplicFileDssSupport_Type.__name__ = "Integer32"
_GnApplicFileDssSupport_Object = MibTableColumn
gnApplicFileDssSupport = _GnApplicFileDssSupport_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 16, 1, 12),
    _GnApplicFileDssSupport_Type()
)
gnApplicFileDssSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnApplicFileDssSupport.setStatus("mandatory")


class _GnApplicFileCrcSupport_Type(Integer32):
    """Custom type gnApplicFileCrcSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 3),
          ("yes", 2))
    )


_GnApplicFileCrcSupport_Type.__name__ = "Integer32"
_GnApplicFileCrcSupport_Object = MibTableColumn
gnApplicFileCrcSupport = _GnApplicFileCrcSupport_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 16, 1, 13),
    _GnApplicFileCrcSupport_Type()
)
gnApplicFileCrcSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnApplicFileCrcSupport.setStatus("mandatory")
_GnDiskCapacityData_ObjectIdentity = ObjectIdentity
gnDiskCapacityData = _GnDiskCapacityData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 17)
)
_GnDiskUsedspace_Type = Integer32
_GnDiskUsedspace_Object = MibScalar
gnDiskUsedspace = _GnDiskUsedspace_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 17, 1),
    _GnDiskUsedspace_Type()
)
gnDiskUsedspace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnDiskUsedspace.setStatus("mandatory")
_GnDiskFreespace_Type = Integer32
_GnDiskFreespace_Object = MibScalar
gnDiskFreespace = _GnDiskFreespace_Object(
    (1, 3, 6, 1, 4, 1, 2281, 2, 2, 17, 2),
    _GnDiskFreespace_Type()
)
gnDiskFreespace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnDiskFreespace.setStatus("mandatory")
_GnUnits_ObjectIdentity = ObjectIdentity
gnUnits = _GnUnits_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 3)
)
_GnODU_ObjectIdentity = ObjectIdentity
gnODU = _GnODU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1)
)
_GnOduCfgTable_Object = MibTable
gnOduCfgTable = _GnOduCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 1)
)
if mibBuilder.loadTexts:
    gnOduCfgTable.setStatus("mandatory")
_GnOduCfgEntry_Object = MibTableRow
gnOduCfgEntry = _GnOduCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 1, 1)
)
gnOduCfgEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    gnOduCfgEntry.setStatus("mandatory")


class _GnOduCfgTransmitterFrequency_Type(Integer32):
    """Custom type gnOduCfgTransmitterFrequency based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_GnOduCfgTransmitterFrequency_Type.__name__ = "Integer32"
_GnOduCfgTransmitterFrequency_Object = MibTableColumn
gnOduCfgTransmitterFrequency = _GnOduCfgTransmitterFrequency_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 1, 1, 1),
    _GnOduCfgTransmitterFrequency_Type()
)
gnOduCfgTransmitterFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnOduCfgTransmitterFrequency.setStatus("mandatory")


class _GnOduCfgRLPerfMonThresh1_Type(Integer32):
    """Custom type gnOduCfgRLPerfMonThresh1 based on Integer32"""
    defaultValue = -50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-75, -15),
    )


_GnOduCfgRLPerfMonThresh1_Type.__name__ = "Integer32"
_GnOduCfgRLPerfMonThresh1_Object = MibTableColumn
gnOduCfgRLPerfMonThresh1 = _GnOduCfgRLPerfMonThresh1_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 1, 1, 2),
    _GnOduCfgRLPerfMonThresh1_Type()
)
gnOduCfgRLPerfMonThresh1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnOduCfgRLPerfMonThresh1.setStatus("mandatory")


class _GnOduCfgRLPerfMonThresh2_Type(Integer32):
    """Custom type gnOduCfgRLPerfMonThresh2 based on Integer32"""
    defaultValue = -70

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-75, -15),
    )


_GnOduCfgRLPerfMonThresh2_Type.__name__ = "Integer32"
_GnOduCfgRLPerfMonThresh2_Object = MibTableColumn
gnOduCfgRLPerfMonThresh2 = _GnOduCfgRLPerfMonThresh2_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 1, 1, 3),
    _GnOduCfgRLPerfMonThresh2_Type()
)
gnOduCfgRLPerfMonThresh2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnOduCfgRLPerfMonThresh2.setStatus("mandatory")


class _GnOduCfgATPCStatus_Type(Integer32):
    """Custom type gnOduCfgATPCStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 3),
          ("on", 2))
    )


_GnOduCfgATPCStatus_Type.__name__ = "Integer32"
_GnOduCfgATPCStatus_Object = MibTableColumn
gnOduCfgATPCStatus = _GnOduCfgATPCStatus_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 1, 1, 4),
    _GnOduCfgATPCStatus_Type()
)
gnOduCfgATPCStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnOduCfgATPCStatus.setStatus("mandatory")


class _GnOduCfgMUTEStatus_Type(Integer32):
    """Custom type gnOduCfgMUTEStatus based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 3),
          ("on", 2))
    )


_GnOduCfgMUTEStatus_Type.__name__ = "Integer32"
_GnOduCfgMUTEStatus_Object = MibTableColumn
gnOduCfgMUTEStatus = _GnOduCfgMUTEStatus_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 1, 1, 5),
    _GnOduCfgMUTEStatus_Type()
)
gnOduCfgMUTEStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnOduCfgMUTEStatus.setStatus("mandatory")


class _GnOduCfgAntennaType_Type(Integer32):
    """Custom type gnOduCfgAntennaType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("fourFeet", 5),
          ("oneFoot", 2),
          ("sixFeet", 6),
          ("threeFeet", 4),
          ("twoFeet", 3))
    )


_GnOduCfgAntennaType_Type.__name__ = "Integer32"
_GnOduCfgAntennaType_Object = MibTableColumn
gnOduCfgAntennaType = _GnOduCfgAntennaType_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 1, 1, 6),
    _GnOduCfgAntennaType_Type()
)
gnOduCfgAntennaType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnOduCfgAntennaType.setStatus("mandatory")


class _GnOduCfgTransmitLevel_Type(Integer32):
    """Custom type gnOduCfgTransmitLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-50, 30),
    )


_GnOduCfgTransmitLevel_Type.__name__ = "Integer32"
_GnOduCfgTransmitLevel_Object = MibTableColumn
gnOduCfgTransmitLevel = _GnOduCfgTransmitLevel_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 1, 1, 7),
    _GnOduCfgTransmitLevel_Type()
)
gnOduCfgTransmitLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnOduCfgTransmitLevel.setStatus("mandatory")
_GnOduCfgRealTxFreqNumber_Type = Integer32
_GnOduCfgRealTxFreqNumber_Object = MibTableColumn
gnOduCfgRealTxFreqNumber = _GnOduCfgRealTxFreqNumber_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 1, 1, 8),
    _GnOduCfgRealTxFreqNumber_Type()
)
gnOduCfgRealTxFreqNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnOduCfgRealTxFreqNumber.setStatus("mandatory")
_GnOduCfgRealRxFreqNumber_Type = Integer32
_GnOduCfgRealRxFreqNumber_Object = MibTableColumn
gnOduCfgRealRxFreqNumber = _GnOduCfgRealRxFreqNumber_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 1, 1, 9),
    _GnOduCfgRealRxFreqNumber_Type()
)
gnOduCfgRealRxFreqNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnOduCfgRealRxFreqNumber.setStatus("mandatory")


class _GnOduCfgMinTxFreqNumber_Type(Integer32):
    """Custom type gnOduCfgMinTxFreqNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_GnOduCfgMinTxFreqNumber_Type.__name__ = "Integer32"
_GnOduCfgMinTxFreqNumber_Object = MibTableColumn
gnOduCfgMinTxFreqNumber = _GnOduCfgMinTxFreqNumber_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 1, 1, 10),
    _GnOduCfgMinTxFreqNumber_Type()
)
gnOduCfgMinTxFreqNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduCfgMinTxFreqNumber.setStatus("mandatory")


class _GnOduCfgMaxTxFreqNumber_Type(Integer32):
    """Custom type gnOduCfgMaxTxFreqNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_GnOduCfgMaxTxFreqNumber_Type.__name__ = "Integer32"
_GnOduCfgMaxTxFreqNumber_Object = MibTableColumn
gnOduCfgMaxTxFreqNumber = _GnOduCfgMaxTxFreqNumber_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 1, 1, 11),
    _GnOduCfgMaxTxFreqNumber_Type()
)
gnOduCfgMaxTxFreqNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduCfgMaxTxFreqNumber.setStatus("mandatory")


class _GnOduCfgMaxTxLevel_Type(Integer32):
    """Custom type gnOduCfgMaxTxLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_GnOduCfgMaxTxLevel_Type.__name__ = "Integer32"
_GnOduCfgMaxTxLevel_Object = MibTableColumn
gnOduCfgMaxTxLevel = _GnOduCfgMaxTxLevel_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 1, 1, 12),
    _GnOduCfgMaxTxLevel_Type()
)
gnOduCfgMaxTxLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduCfgMaxTxLevel.setStatus("mandatory")


class _GnOduCfgRefRsl_Type(Integer32):
    """Custom type gnOduCfgRefRsl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-70, -30),
    )


_GnOduCfgRefRsl_Type.__name__ = "Integer32"
_GnOduCfgRefRsl_Object = MibTableColumn
gnOduCfgRefRsl = _GnOduCfgRefRsl_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 1, 1, 13),
    _GnOduCfgRefRsl_Type()
)
gnOduCfgRefRsl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnOduCfgRefRsl.setStatus("mandatory")


class _GnOduCfgForceRmtMuteTx_Type(Integer32):
    """Custom type gnOduCfgForceRmtMuteTx based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 3),
          ("on", 2))
    )


_GnOduCfgForceRmtMuteTx_Type.__name__ = "Integer32"
_GnOduCfgForceRmtMuteTx_Object = MibTableColumn
gnOduCfgForceRmtMuteTx = _GnOduCfgForceRmtMuteTx_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 1, 1, 14),
    _GnOduCfgForceRmtMuteTx_Type()
)
gnOduCfgForceRmtMuteTx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnOduCfgForceRmtMuteTx.setStatus("mandatory")


class _GnOduCfgForceRmtMaxTx_Type(Integer32):
    """Custom type gnOduCfgForceRmtMaxTx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-50, 30),
    )


_GnOduCfgForceRmtMaxTx_Type.__name__ = "Integer32"
_GnOduCfgForceRmtMaxTx_Object = MibTableColumn
gnOduCfgForceRmtMaxTx = _GnOduCfgForceRmtMaxTx_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 1, 1, 15),
    _GnOduCfgForceRmtMaxTx_Type()
)
gnOduCfgForceRmtMaxTx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnOduCfgForceRmtMaxTx.setStatus("mandatory")


class _GnOduCfgTLPerfMonThresh1_Type(Integer32):
    """Custom type gnOduCfgTLPerfMonThresh1 based on Integer32"""
    defaultValue = 25

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-10, 25),
    )


_GnOduCfgTLPerfMonThresh1_Type.__name__ = "Integer32"
_GnOduCfgTLPerfMonThresh1_Object = MibTableColumn
gnOduCfgTLPerfMonThresh1 = _GnOduCfgTLPerfMonThresh1_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 1, 1, 16),
    _GnOduCfgTLPerfMonThresh1_Type()
)
gnOduCfgTLPerfMonThresh1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnOduCfgTLPerfMonThresh1.setStatus("mandatory")
_GnOduCfgMinRxFreqNumber_Type = Integer32
_GnOduCfgMinRxFreqNumber_Object = MibTableColumn
gnOduCfgMinRxFreqNumber = _GnOduCfgMinRxFreqNumber_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 1, 1, 17),
    _GnOduCfgMinRxFreqNumber_Type()
)
gnOduCfgMinRxFreqNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduCfgMinRxFreqNumber.setStatus("mandatory")
_GnOduCfgMaxRxFreqNumber_Type = Integer32
_GnOduCfgMaxRxFreqNumber_Object = MibTableColumn
gnOduCfgMaxRxFreqNumber = _GnOduCfgMaxRxFreqNumber_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 1, 1, 18),
    _GnOduCfgMaxRxFreqNumber_Type()
)
gnOduCfgMaxRxFreqNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduCfgMaxRxFreqNumber.setStatus("mandatory")


class _GnOduCfgOduLoopSupport_Type(Integer32):
    """Custom type gnOduCfgOduLoopSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 2),
          ("supported", 3))
    )


_GnOduCfgOduLoopSupport_Type.__name__ = "Integer32"
_GnOduCfgOduLoopSupport_Object = MibTableColumn
gnOduCfgOduLoopSupport = _GnOduCfgOduLoopSupport_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 1, 1, 19),
    _GnOduCfgOduLoopSupport_Type()
)
gnOduCfgOduLoopSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduCfgOduLoopSupport.setStatus("mandatory")


class _GnOduCfgOduModel_Type(Integer32):
    """Custom type gnOduCfgOduModel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 2),
          ("v1", 4),
          ("v2", 3))
    )


_GnOduCfgOduModel_Type.__name__ = "Integer32"
_GnOduCfgOduModel_Object = MibTableColumn
gnOduCfgOduModel = _GnOduCfgOduModel_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 1, 1, 20),
    _GnOduCfgOduModel_Type()
)
gnOduCfgOduModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduCfgOduModel.setStatus("mandatory")


class _GnOduCfgFreqPlanStandard_Type(DisplayString):
    """Custom type gnOduCfgFreqPlanStandard based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 45),
    )


_GnOduCfgFreqPlanStandard_Type.__name__ = "DisplayString"
_GnOduCfgFreqPlanStandard_Object = MibTableColumn
gnOduCfgFreqPlanStandard = _GnOduCfgFreqPlanStandard_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 1, 1, 21),
    _GnOduCfgFreqPlanStandard_Type()
)
gnOduCfgFreqPlanStandard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnOduCfgFreqPlanStandard.setStatus("mandatory")
_GnOduCfgFreqDevider_Type = Integer32
_GnOduCfgFreqDevider_Object = MibTableColumn
gnOduCfgFreqDevider = _GnOduCfgFreqDevider_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 1, 1, 22),
    _GnOduCfgFreqDevider_Type()
)
gnOduCfgFreqDevider.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduCfgFreqDevider.setStatus("mandatory")
_GnOduStatusTable_Object = MibTable
gnOduStatusTable = _GnOduStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 2)
)
if mibBuilder.loadTexts:
    gnOduStatusTable.setStatus("mandatory")
_GnOduStatusEntry_Object = MibTableRow
gnOduStatusEntry = _GnOduStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 2, 1)
)
gnOduStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    gnOduStatusEntry.setStatus("mandatory")


class _GnOduStatusCelsiusTemp_Type(Integer32):
    """Custom type gnOduStatusCelsiusTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-50, 80),
    )


_GnOduStatusCelsiusTemp_Type.__name__ = "Integer32"
_GnOduStatusCelsiusTemp_Object = MibTableColumn
gnOduStatusCelsiusTemp = _GnOduStatusCelsiusTemp_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 2, 1, 1),
    _GnOduStatusCelsiusTemp_Type()
)
gnOduStatusCelsiusTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduStatusCelsiusTemp.setStatus("mandatory")


class _GnOduStatusFahrenheitTemp_Type(Integer32):
    """Custom type gnOduStatusFahrenheitTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-58, 176),
    )


_GnOduStatusFahrenheitTemp_Type.__name__ = "Integer32"
_GnOduStatusFahrenheitTemp_Object = MibTableColumn
gnOduStatusFahrenheitTemp = _GnOduStatusFahrenheitTemp_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 2, 1, 2),
    _GnOduStatusFahrenheitTemp_Type()
)
gnOduStatusFahrenheitTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduStatusFahrenheitTemp.setStatus("mandatory")


class _GnOduStatusTransmitLevel_Type(Integer32):
    """Custom type gnOduStatusTransmitLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-99, 30),
    )


_GnOduStatusTransmitLevel_Type.__name__ = "Integer32"
_GnOduStatusTransmitLevel_Object = MibTableColumn
gnOduStatusTransmitLevel = _GnOduStatusTransmitLevel_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 2, 1, 3),
    _GnOduStatusTransmitLevel_Type()
)
gnOduStatusTransmitLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduStatusTransmitLevel.setStatus("mandatory")


class _GnOduStatusReceiveLevel_Type(Integer32):
    """Custom type gnOduStatusReceiveLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-99, -15),
    )


_GnOduStatusReceiveLevel_Type.__name__ = "Integer32"
_GnOduStatusReceiveLevel_Object = MibTableColumn
gnOduStatusReceiveLevel = _GnOduStatusReceiveLevel_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 2, 1, 4),
    _GnOduStatusReceiveLevel_Type()
)
gnOduStatusReceiveLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduStatusReceiveLevel.setStatus("mandatory")


class _GnOduStatusSynthesizerVCOLock_Type(OctetString):
    """Custom type gnOduStatusSynthesizerVCOLock based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_GnOduStatusSynthesizerVCOLock_Type.__name__ = "OctetString"
_GnOduStatusSynthesizerVCOLock_Object = MibTableColumn
gnOduStatusSynthesizerVCOLock = _GnOduStatusSynthesizerVCOLock_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 2, 1, 5),
    _GnOduStatusSynthesizerVCOLock_Type()
)
gnOduStatusSynthesizerVCOLock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduStatusSynthesizerVCOLock.setStatus("mandatory")


class _GnOduStatusPowerSupply_Type(OctetString):
    """Custom type gnOduStatusPowerSupply based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_GnOduStatusPowerSupply_Type.__name__ = "OctetString"
_GnOduStatusPowerSupply_Object = MibTableColumn
gnOduStatusPowerSupply = _GnOduStatusPowerSupply_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 2, 1, 6),
    _GnOduStatusPowerSupply_Type()
)
gnOduStatusPowerSupply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduStatusPowerSupply.setStatus("mandatory")


class _GnOduStatusClearLoopTimer_Type(Integer32):
    """Custom type gnOduStatusClearLoopTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_GnOduStatusClearLoopTimer_Type.__name__ = "Integer32"
_GnOduStatusClearLoopTimer_Object = MibTableColumn
gnOduStatusClearLoopTimer = _GnOduStatusClearLoopTimer_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 2, 1, 7),
    _GnOduStatusClearLoopTimer_Type()
)
gnOduStatusClearLoopTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduStatusClearLoopTimer.setStatus("mandatory")
_GnOduMonitor_ObjectIdentity = ObjectIdentity
gnOduMonitor = _GnOduMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 3)
)
_GnOduMonCurrTable_Object = MibTable
gnOduMonCurrTable = _GnOduMonCurrTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 3, 1)
)
if mibBuilder.loadTexts:
    gnOduMonCurrTable.setStatus("mandatory")
_GnOduMonCurrEntry_Object = MibTableRow
gnOduMonCurrEntry = _GnOduMonCurrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 3, 1, 1)
)
gnOduMonCurrEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    gnOduMonCurrEntry.setStatus("mandatory")
_GnOduMonCurrMinRL_Type = Integer32
_GnOduMonCurrMinRL_Object = MibTableColumn
gnOduMonCurrMinRL = _GnOduMonCurrMinRL_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 3, 1, 1, 1),
    _GnOduMonCurrMinRL_Type()
)
gnOduMonCurrMinRL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonCurrMinRL.setStatus("mandatory")
_GnOduMonCurrMaxRL_Type = Integer32
_GnOduMonCurrMaxRL_Object = MibTableColumn
gnOduMonCurrMaxRL = _GnOduMonCurrMaxRL_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 3, 1, 1, 2),
    _GnOduMonCurrMaxRL_Type()
)
gnOduMonCurrMaxRL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonCurrMaxRL.setStatus("mandatory")
_GnOduMonCurrTLThresh1Exceed_Type = Counter32
_GnOduMonCurrTLThresh1Exceed_Object = MibTableColumn
gnOduMonCurrTLThresh1Exceed = _GnOduMonCurrTLThresh1Exceed_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 3, 1, 1, 3),
    _GnOduMonCurrTLThresh1Exceed_Type()
)
gnOduMonCurrTLThresh1Exceed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonCurrTLThresh1Exceed.setStatus("mandatory")
_GnOduMonCurrRLThresh1Exceed_Type = Counter32
_GnOduMonCurrRLThresh1Exceed_Object = MibTableColumn
gnOduMonCurrRLThresh1Exceed = _GnOduMonCurrRLThresh1Exceed_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 3, 1, 1, 4),
    _GnOduMonCurrRLThresh1Exceed_Type()
)
gnOduMonCurrRLThresh1Exceed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonCurrRLThresh1Exceed.setStatus("mandatory")
_GnOduMonCurrRLThresh2Exceed_Type = Counter32
_GnOduMonCurrRLThresh2Exceed_Object = MibTableColumn
gnOduMonCurrRLThresh2Exceed = _GnOduMonCurrRLThresh2Exceed_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 3, 1, 1, 5),
    _GnOduMonCurrRLThresh2Exceed_Type()
)
gnOduMonCurrRLThresh2Exceed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonCurrRLThresh2Exceed.setStatus("mandatory")
_GnOduMonCurrDayMinRL_Type = Integer32
_GnOduMonCurrDayMinRL_Object = MibTableColumn
gnOduMonCurrDayMinRL = _GnOduMonCurrDayMinRL_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 3, 1, 1, 6),
    _GnOduMonCurrDayMinRL_Type()
)
gnOduMonCurrDayMinRL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonCurrDayMinRL.setStatus("mandatory")
_GnOduMonCurrDayMaxRL_Type = Integer32
_GnOduMonCurrDayMaxRL_Object = MibTableColumn
gnOduMonCurrDayMaxRL = _GnOduMonCurrDayMaxRL_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 3, 1, 1, 7),
    _GnOduMonCurrDayMaxRL_Type()
)
gnOduMonCurrDayMaxRL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonCurrDayMaxRL.setStatus("mandatory")
_GnOduMonCurrDayTLThresh1Exceed_Type = Counter32
_GnOduMonCurrDayTLThresh1Exceed_Object = MibTableColumn
gnOduMonCurrDayTLThresh1Exceed = _GnOduMonCurrDayTLThresh1Exceed_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 3, 1, 1, 8),
    _GnOduMonCurrDayTLThresh1Exceed_Type()
)
gnOduMonCurrDayTLThresh1Exceed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonCurrDayTLThresh1Exceed.setStatus("mandatory")
_GnOduMonCurrDayRLThresh1Exceed_Type = Counter32
_GnOduMonCurrDayRLThresh1Exceed_Object = MibTableColumn
gnOduMonCurrDayRLThresh1Exceed = _GnOduMonCurrDayRLThresh1Exceed_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 3, 1, 1, 9),
    _GnOduMonCurrDayRLThresh1Exceed_Type()
)
gnOduMonCurrDayRLThresh1Exceed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonCurrDayRLThresh1Exceed.setStatus("mandatory")
_GnOduMonCurrDayRLThresh2Exceed_Type = Counter32
_GnOduMonCurrDayRLThresh2Exceed_Object = MibTableColumn
gnOduMonCurrDayRLThresh2Exceed = _GnOduMonCurrDayRLThresh2Exceed_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 3, 1, 1, 10),
    _GnOduMonCurrDayRLThresh2Exceed_Type()
)
gnOduMonCurrDayRLThresh2Exceed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonCurrDayRLThresh2Exceed.setStatus("mandatory")
_GnOduMonCurrMinTL_Type = Integer32
_GnOduMonCurrMinTL_Object = MibTableColumn
gnOduMonCurrMinTL = _GnOduMonCurrMinTL_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 3, 1, 1, 11),
    _GnOduMonCurrMinTL_Type()
)
gnOduMonCurrMinTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonCurrMinTL.setStatus("mandatory")
_GnOduMonCurrMaxTL_Type = Integer32
_GnOduMonCurrMaxTL_Object = MibTableColumn
gnOduMonCurrMaxTL = _GnOduMonCurrMaxTL_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 3, 1, 1, 12),
    _GnOduMonCurrMaxTL_Type()
)
gnOduMonCurrMaxTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonCurrMaxTL.setStatus("mandatory")
_GnOduMonCurrDayMinTL_Type = Integer32
_GnOduMonCurrDayMinTL_Object = MibTableColumn
gnOduMonCurrDayMinTL = _GnOduMonCurrDayMinTL_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 3, 1, 1, 13),
    _GnOduMonCurrDayMinTL_Type()
)
gnOduMonCurrDayMinTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonCurrDayMinTL.setStatus("mandatory")
_GnOduMonCurrDayMaxTL_Type = Integer32
_GnOduMonCurrDayMaxTL_Object = MibTableColumn
gnOduMonCurrDayMaxTL = _GnOduMonCurrDayMaxTL_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 3, 1, 1, 14),
    _GnOduMonCurrDayMaxTL_Type()
)
gnOduMonCurrDayMaxTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonCurrDayMaxTL.setStatus("mandatory")
_GnOduMonIntervalTable_Object = MibTable
gnOduMonIntervalTable = _GnOduMonIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 3, 2)
)
if mibBuilder.loadTexts:
    gnOduMonIntervalTable.setStatus("mandatory")
_GnOduMonIntervalEntry_Object = MibTableRow
gnOduMonIntervalEntry = _GnOduMonIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 3, 2, 1)
)
gnOduMonIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CERAGON-MIB", "gnOduMonIntervalIdx"),
)
if mibBuilder.loadTexts:
    gnOduMonIntervalEntry.setStatus("mandatory")


class _GnOduMonIntervalIdx_Type(Integer32):
    """Custom type gnOduMonIntervalIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_GnOduMonIntervalIdx_Type.__name__ = "Integer32"
_GnOduMonIntervalIdx_Object = MibTableColumn
gnOduMonIntervalIdx = _GnOduMonIntervalIdx_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 3, 2, 1, 1),
    _GnOduMonIntervalIdx_Type()
)
gnOduMonIntervalIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonIntervalIdx.setStatus("mandatory")
_GnOduMonIntervalMinRL_Type = Integer32
_GnOduMonIntervalMinRL_Object = MibTableColumn
gnOduMonIntervalMinRL = _GnOduMonIntervalMinRL_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 3, 2, 1, 2),
    _GnOduMonIntervalMinRL_Type()
)
gnOduMonIntervalMinRL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonIntervalMinRL.setStatus("mandatory")
_GnOduMonIntervalMaxRL_Type = Integer32
_GnOduMonIntervalMaxRL_Object = MibTableColumn
gnOduMonIntervalMaxRL = _GnOduMonIntervalMaxRL_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 3, 2, 1, 3),
    _GnOduMonIntervalMaxRL_Type()
)
gnOduMonIntervalMaxRL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonIntervalMaxRL.setStatus("mandatory")
_GnOduMonIntervalTLThresh1Exceed_Type = Counter32
_GnOduMonIntervalTLThresh1Exceed_Object = MibTableColumn
gnOduMonIntervalTLThresh1Exceed = _GnOduMonIntervalTLThresh1Exceed_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 3, 2, 1, 4),
    _GnOduMonIntervalTLThresh1Exceed_Type()
)
gnOduMonIntervalTLThresh1Exceed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonIntervalTLThresh1Exceed.setStatus("mandatory")


class _GnOduMonIntervalEvent_Type(OctetString):
    """Custom type gnOduMonIntervalEvent based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_GnOduMonIntervalEvent_Type.__name__ = "OctetString"
_GnOduMonIntervalEvent_Object = MibTableColumn
gnOduMonIntervalEvent = _GnOduMonIntervalEvent_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 3, 2, 1, 5),
    _GnOduMonIntervalEvent_Type()
)
gnOduMonIntervalEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonIntervalEvent.setStatus("mandatory")
_GnOduMonIntervalRLThresh1Exceed_Type = Counter32
_GnOduMonIntervalRLThresh1Exceed_Object = MibTableColumn
gnOduMonIntervalRLThresh1Exceed = _GnOduMonIntervalRLThresh1Exceed_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 3, 2, 1, 6),
    _GnOduMonIntervalRLThresh1Exceed_Type()
)
gnOduMonIntervalRLThresh1Exceed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonIntervalRLThresh1Exceed.setStatus("mandatory")
_GnOduMonIntervalRLThresh2Exceed_Type = Counter32
_GnOduMonIntervalRLThresh2Exceed_Object = MibTableColumn
gnOduMonIntervalRLThresh2Exceed = _GnOduMonIntervalRLThresh2Exceed_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 3, 2, 1, 7),
    _GnOduMonIntervalRLThresh2Exceed_Type()
)
gnOduMonIntervalRLThresh2Exceed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonIntervalRLThresh2Exceed.setStatus("mandatory")
_GnOduMonIntervalMinTL_Type = Integer32
_GnOduMonIntervalMinTL_Object = MibTableColumn
gnOduMonIntervalMinTL = _GnOduMonIntervalMinTL_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 3, 2, 1, 8),
    _GnOduMonIntervalMinTL_Type()
)
gnOduMonIntervalMinTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonIntervalMinTL.setStatus("mandatory")
_GnOduMonIntervalMaxTL_Type = Integer32
_GnOduMonIntervalMaxTL_Object = MibTableColumn
gnOduMonIntervalMaxTL = _GnOduMonIntervalMaxTL_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 3, 2, 1, 9),
    _GnOduMonIntervalMaxTL_Type()
)
gnOduMonIntervalMaxTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonIntervalMaxTL.setStatus("mandatory")
_GnOduMonDayTable_Object = MibTable
gnOduMonDayTable = _GnOduMonDayTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 3, 3)
)
if mibBuilder.loadTexts:
    gnOduMonDayTable.setStatus("mandatory")
_GnOduMonDayEntry_Object = MibTableRow
gnOduMonDayEntry = _GnOduMonDayEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 3, 3, 1)
)
gnOduMonDayEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CERAGON-MIB", "gnOduMonDayIdx"),
)
if mibBuilder.loadTexts:
    gnOduMonDayEntry.setStatus("mandatory")


class _GnOduMonDayIdx_Type(Integer32):
    """Custom type gnOduMonDayIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_GnOduMonDayIdx_Type.__name__ = "Integer32"
_GnOduMonDayIdx_Object = MibTableColumn
gnOduMonDayIdx = _GnOduMonDayIdx_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 3, 3, 1, 1),
    _GnOduMonDayIdx_Type()
)
gnOduMonDayIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonDayIdx.setStatus("mandatory")
_GnOduMonDayMinRL_Type = Integer32
_GnOduMonDayMinRL_Object = MibTableColumn
gnOduMonDayMinRL = _GnOduMonDayMinRL_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 3, 3, 1, 2),
    _GnOduMonDayMinRL_Type()
)
gnOduMonDayMinRL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonDayMinRL.setStatus("mandatory")
_GnOduMonDayMaxRL_Type = Integer32
_GnOduMonDayMaxRL_Object = MibTableColumn
gnOduMonDayMaxRL = _GnOduMonDayMaxRL_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 3, 3, 1, 3),
    _GnOduMonDayMaxRL_Type()
)
gnOduMonDayMaxRL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonDayMaxRL.setStatus("mandatory")
_GnOduMonDayTLThresh1Exceed_Type = Counter32
_GnOduMonDayTLThresh1Exceed_Object = MibTableColumn
gnOduMonDayTLThresh1Exceed = _GnOduMonDayTLThresh1Exceed_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 3, 3, 1, 4),
    _GnOduMonDayTLThresh1Exceed_Type()
)
gnOduMonDayTLThresh1Exceed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonDayTLThresh1Exceed.setStatus("mandatory")
_GnOduMonDayRLThresh1Exceed_Type = Counter32
_GnOduMonDayRLThresh1Exceed_Object = MibTableColumn
gnOduMonDayRLThresh1Exceed = _GnOduMonDayRLThresh1Exceed_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 3, 3, 1, 5),
    _GnOduMonDayRLThresh1Exceed_Type()
)
gnOduMonDayRLThresh1Exceed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonDayRLThresh1Exceed.setStatus("mandatory")
_GnOduMonDayRLThresh2Exceed_Type = Counter32
_GnOduMonDayRLThresh2Exceed_Object = MibTableColumn
gnOduMonDayRLThresh2Exceed = _GnOduMonDayRLThresh2Exceed_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 3, 3, 1, 6),
    _GnOduMonDayRLThresh2Exceed_Type()
)
gnOduMonDayRLThresh2Exceed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonDayRLThresh2Exceed.setStatus("mandatory")
_GnOduMonDayMinTL_Type = Integer32
_GnOduMonDayMinTL_Object = MibTableColumn
gnOduMonDayMinTL = _GnOduMonDayMinTL_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 3, 3, 1, 7),
    _GnOduMonDayMinTL_Type()
)
gnOduMonDayMinTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonDayMinTL.setStatus("mandatory")
_GnOduMonDayMaxTL_Type = Integer32
_GnOduMonDayMaxTL_Object = MibTableColumn
gnOduMonDayMaxTL = _GnOduMonDayMaxTL_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 3, 3, 1, 8),
    _GnOduMonDayMaxTL_Type()
)
gnOduMonDayMaxTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonDayMaxTL.setStatus("mandatory")
_GnOduCfgXTable_Object = MibTable
gnOduCfgXTable = _GnOduCfgXTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 4)
)
if mibBuilder.loadTexts:
    gnOduCfgXTable.setStatus("mandatory")
_GnOduCfgXEntry_Object = MibTableRow
gnOduCfgXEntry = _GnOduCfgXEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 4, 1)
)
gnOduCfgXEntry.setIndexNames(
    (0, "CERAGON-MIB", "gnOduCfgXId"),
)
if mibBuilder.loadTexts:
    gnOduCfgXEntry.setStatus("mandatory")


class _GnOduCfgXId_Type(Integer32):
    """Custom type gnOduCfgXId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("drawer1", 3),
          ("drawer2", 4))
    )


_GnOduCfgXId_Type.__name__ = "Integer32"
_GnOduCfgXId_Object = MibTableColumn
gnOduCfgXId = _GnOduCfgXId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 4, 1, 1),
    _GnOduCfgXId_Type()
)
gnOduCfgXId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduCfgXId.setStatus("mandatory")
_GnOduCfgXTxFreqNumLocalRemote_Type = Integer32
_GnOduCfgXTxFreqNumLocalRemote_Object = MibTableColumn
gnOduCfgXTxFreqNumLocalRemote = _GnOduCfgXTxFreqNumLocalRemote_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 4, 1, 2),
    _GnOduCfgXTxFreqNumLocalRemote_Type()
)
gnOduCfgXTxFreqNumLocalRemote.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnOduCfgXTxFreqNumLocalRemote.setStatus("mandatory")


class _GnOduCfgXRLPerfMonThresh1_Type(Integer32):
    """Custom type gnOduCfgXRLPerfMonThresh1 based on Integer32"""
    defaultValue = -50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-75, -15),
    )


_GnOduCfgXRLPerfMonThresh1_Type.__name__ = "Integer32"
_GnOduCfgXRLPerfMonThresh1_Object = MibTableColumn
gnOduCfgXRLPerfMonThresh1 = _GnOduCfgXRLPerfMonThresh1_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 4, 1, 3),
    _GnOduCfgXRLPerfMonThresh1_Type()
)
gnOduCfgXRLPerfMonThresh1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnOduCfgXRLPerfMonThresh1.setStatus("mandatory")


class _GnOduCfgXRLPerfMonThresh2_Type(Integer32):
    """Custom type gnOduCfgXRLPerfMonThresh2 based on Integer32"""
    defaultValue = -70

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-75, -15),
    )


_GnOduCfgXRLPerfMonThresh2_Type.__name__ = "Integer32"
_GnOduCfgXRLPerfMonThresh2_Object = MibTableColumn
gnOduCfgXRLPerfMonThresh2 = _GnOduCfgXRLPerfMonThresh2_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 4, 1, 4),
    _GnOduCfgXRLPerfMonThresh2_Type()
)
gnOduCfgXRLPerfMonThresh2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnOduCfgXRLPerfMonThresh2.setStatus("mandatory")


class _GnOduCfgXATPCStatus_Type(Integer32):
    """Custom type gnOduCfgXATPCStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 3),
          ("on", 2))
    )


_GnOduCfgXATPCStatus_Type.__name__ = "Integer32"
_GnOduCfgXATPCStatus_Object = MibTableColumn
gnOduCfgXATPCStatus = _GnOduCfgXATPCStatus_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 4, 1, 5),
    _GnOduCfgXATPCStatus_Type()
)
gnOduCfgXATPCStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnOduCfgXATPCStatus.setStatus("mandatory")


class _GnOduCfgXMUTEStatus_Type(Integer32):
    """Custom type gnOduCfgXMUTEStatus based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 3),
          ("on", 2))
    )


_GnOduCfgXMUTEStatus_Type.__name__ = "Integer32"
_GnOduCfgXMUTEStatus_Object = MibTableColumn
gnOduCfgXMUTEStatus = _GnOduCfgXMUTEStatus_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 4, 1, 6),
    _GnOduCfgXMUTEStatus_Type()
)
gnOduCfgXMUTEStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnOduCfgXMUTEStatus.setStatus("mandatory")


class _GnOduCfgXAntennaType_Type(Integer32):
    """Custom type gnOduCfgXAntennaType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("fourFeet", 5),
          ("oneFoot", 2),
          ("sixFeet", 6),
          ("threeFeet", 4),
          ("twoFeet", 3))
    )


_GnOduCfgXAntennaType_Type.__name__ = "Integer32"
_GnOduCfgXAntennaType_Object = MibTableColumn
gnOduCfgXAntennaType = _GnOduCfgXAntennaType_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 4, 1, 7),
    _GnOduCfgXAntennaType_Type()
)
gnOduCfgXAntennaType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnOduCfgXAntennaType.setStatus("mandatory")


class _GnOduCfgXTransmitLevel_Type(Integer32):
    """Custom type gnOduCfgXTransmitLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-50, 34),
    )


_GnOduCfgXTransmitLevel_Type.__name__ = "Integer32"
_GnOduCfgXTransmitLevel_Object = MibTableColumn
gnOduCfgXTransmitLevel = _GnOduCfgXTransmitLevel_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 4, 1, 8),
    _GnOduCfgXTransmitLevel_Type()
)
gnOduCfgXTransmitLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnOduCfgXTransmitLevel.setStatus("mandatory")
_GnOduCfgXRealTxFreqNumber_Type = Integer32
_GnOduCfgXRealTxFreqNumber_Object = MibTableColumn
gnOduCfgXRealTxFreqNumber = _GnOduCfgXRealTxFreqNumber_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 4, 1, 9),
    _GnOduCfgXRealTxFreqNumber_Type()
)
gnOduCfgXRealTxFreqNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnOduCfgXRealTxFreqNumber.setStatus("mandatory")
_GnOduCfgXRealRxFreqNumber_Type = Integer32
_GnOduCfgXRealRxFreqNumber_Object = MibTableColumn
gnOduCfgXRealRxFreqNumber = _GnOduCfgXRealRxFreqNumber_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 4, 1, 10),
    _GnOduCfgXRealRxFreqNumber_Type()
)
gnOduCfgXRealRxFreqNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnOduCfgXRealRxFreqNumber.setStatus("mandatory")


class _GnOduCfgXMinTxFreqNumber_Type(Integer32):
    """Custom type gnOduCfgXMinTxFreqNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_GnOduCfgXMinTxFreqNumber_Type.__name__ = "Integer32"
_GnOduCfgXMinTxFreqNumber_Object = MibTableColumn
gnOduCfgXMinTxFreqNumber = _GnOduCfgXMinTxFreqNumber_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 4, 1, 11),
    _GnOduCfgXMinTxFreqNumber_Type()
)
gnOduCfgXMinTxFreqNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduCfgXMinTxFreqNumber.setStatus("mandatory")


class _GnOduCfgXMaxTxFreqNumber_Type(Integer32):
    """Custom type gnOduCfgXMaxTxFreqNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_GnOduCfgXMaxTxFreqNumber_Type.__name__ = "Integer32"
_GnOduCfgXMaxTxFreqNumber_Object = MibTableColumn
gnOduCfgXMaxTxFreqNumber = _GnOduCfgXMaxTxFreqNumber_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 4, 1, 12),
    _GnOduCfgXMaxTxFreqNumber_Type()
)
gnOduCfgXMaxTxFreqNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduCfgXMaxTxFreqNumber.setStatus("mandatory")


class _GnOduCfgXMaxTxLevel_Type(Integer32):
    """Custom type gnOduCfgXMaxTxLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_GnOduCfgXMaxTxLevel_Type.__name__ = "Integer32"
_GnOduCfgXMaxTxLevel_Object = MibTableColumn
gnOduCfgXMaxTxLevel = _GnOduCfgXMaxTxLevel_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 4, 1, 13),
    _GnOduCfgXMaxTxLevel_Type()
)
gnOduCfgXMaxTxLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduCfgXMaxTxLevel.setStatus("mandatory")


class _GnOduCfgXRefRsl_Type(Integer32):
    """Custom type gnOduCfgXRefRsl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-70, -30),
    )


_GnOduCfgXRefRsl_Type.__name__ = "Integer32"
_GnOduCfgXRefRsl_Object = MibTableColumn
gnOduCfgXRefRsl = _GnOduCfgXRefRsl_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 4, 1, 14),
    _GnOduCfgXRefRsl_Type()
)
gnOduCfgXRefRsl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnOduCfgXRefRsl.setStatus("mandatory")


class _GnOduCfgXForceRmtMuteTx_Type(Integer32):
    """Custom type gnOduCfgXForceRmtMuteTx based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 3),
          ("on", 2))
    )


_GnOduCfgXForceRmtMuteTx_Type.__name__ = "Integer32"
_GnOduCfgXForceRmtMuteTx_Object = MibTableColumn
gnOduCfgXForceRmtMuteTx = _GnOduCfgXForceRmtMuteTx_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 4, 1, 15),
    _GnOduCfgXForceRmtMuteTx_Type()
)
gnOduCfgXForceRmtMuteTx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnOduCfgXForceRmtMuteTx.setStatus("mandatory")


class _GnOduCfgXForceRmtMaxTx_Type(Integer32):
    """Custom type gnOduCfgXForceRmtMaxTx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-50, 30),
    )


_GnOduCfgXForceRmtMaxTx_Type.__name__ = "Integer32"
_GnOduCfgXForceRmtMaxTx_Object = MibTableColumn
gnOduCfgXForceRmtMaxTx = _GnOduCfgXForceRmtMaxTx_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 4, 1, 16),
    _GnOduCfgXForceRmtMaxTx_Type()
)
gnOduCfgXForceRmtMaxTx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnOduCfgXForceRmtMaxTx.setStatus("mandatory")


class _GnOduCfgXTLPerfMonThresh1_Type(Integer32):
    """Custom type gnOduCfgXTLPerfMonThresh1 based on Integer32"""
    defaultValue = 25

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-10, 25),
    )


_GnOduCfgXTLPerfMonThresh1_Type.__name__ = "Integer32"
_GnOduCfgXTLPerfMonThresh1_Object = MibTableColumn
gnOduCfgXTLPerfMonThresh1 = _GnOduCfgXTLPerfMonThresh1_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 4, 1, 17),
    _GnOduCfgXTLPerfMonThresh1_Type()
)
gnOduCfgXTLPerfMonThresh1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnOduCfgXTLPerfMonThresh1.setStatus("mandatory")


class _GnOduCfgXOperation_Type(Integer32):
    """Custom type gnOduCfgXOperation based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("noOperation", 2),
          ("resetODU", 4),
          ("setOduDefaultConf", 3),
          ("swResetODU", 5))
    )


_GnOduCfgXOperation_Type.__name__ = "Integer32"
_GnOduCfgXOperation_Object = MibTableColumn
gnOduCfgXOperation = _GnOduCfgXOperation_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 4, 1, 18),
    _GnOduCfgXOperation_Type()
)
gnOduCfgXOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnOduCfgXOperation.setStatus("mandatory")


class _GnOduCfgXODUSerialNumber_Type(DisplayString):
    """Custom type gnOduCfgXODUSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_GnOduCfgXODUSerialNumber_Type.__name__ = "DisplayString"
_GnOduCfgXODUSerialNumber_Object = MibTableColumn
gnOduCfgXODUSerialNumber = _GnOduCfgXODUSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 4, 1, 19),
    _GnOduCfgXODUSerialNumber_Type()
)
gnOduCfgXODUSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduCfgXODUSerialNumber.setStatus("mandatory")
_GnOduCfgXChannelBandwidth_Type = Integer32
_GnOduCfgXChannelBandwidth_Object = MibTableColumn
gnOduCfgXChannelBandwidth = _GnOduCfgXChannelBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 4, 1, 20),
    _GnOduCfgXChannelBandwidth_Type()
)
gnOduCfgXChannelBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduCfgXChannelBandwidth.setStatus("mandatory")
_GnOduCfgXMinRxFreqNumber_Type = Integer32
_GnOduCfgXMinRxFreqNumber_Object = MibTableColumn
gnOduCfgXMinRxFreqNumber = _GnOduCfgXMinRxFreqNumber_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 4, 1, 21),
    _GnOduCfgXMinRxFreqNumber_Type()
)
gnOduCfgXMinRxFreqNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduCfgXMinRxFreqNumber.setStatus("mandatory")
_GnOduCfgXMaxRxFreqNumber_Type = Integer32
_GnOduCfgXMaxRxFreqNumber_Object = MibTableColumn
gnOduCfgXMaxRxFreqNumber = _GnOduCfgXMaxRxFreqNumber_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 4, 1, 22),
    _GnOduCfgXMaxRxFreqNumber_Type()
)
gnOduCfgXMaxRxFreqNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduCfgXMaxRxFreqNumber.setStatus("mandatory")
_GnOduCfgXRxFreqNumLocalRemote_Type = Integer32
_GnOduCfgXRxFreqNumLocalRemote_Object = MibTableColumn
gnOduCfgXRxFreqNumLocalRemote = _GnOduCfgXRxFreqNumLocalRemote_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 4, 1, 23),
    _GnOduCfgXRxFreqNumLocalRemote_Type()
)
gnOduCfgXRxFreqNumLocalRemote.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnOduCfgXRxFreqNumLocalRemote.setStatus("mandatory")


class _GnOduCfgXOduLoopSupport_Type(Integer32):
    """Custom type gnOduCfgXOduLoopSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 2),
          ("supported", 3))
    )


_GnOduCfgXOduLoopSupport_Type.__name__ = "Integer32"
_GnOduCfgXOduLoopSupport_Object = MibTableColumn
gnOduCfgXOduLoopSupport = _GnOduCfgXOduLoopSupport_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 4, 1, 24),
    _GnOduCfgXOduLoopSupport_Type()
)
gnOduCfgXOduLoopSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduCfgXOduLoopSupport.setStatus("mandatory")


class _GnOduCfgXOduModel_Type(Integer32):
    """Custom type gnOduCfgXOduModel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
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
        *(("unknown", 2),
          ("v1", 4),
          ("v2", 3),
          ("v3", 5),
          ("v4", 6),
          ("v5", 7),
          ("v6", 8),
          ("v7", 9),
          ("v8", 10),
          ("v9", 11))
    )


_GnOduCfgXOduModel_Type.__name__ = "Integer32"
_GnOduCfgXOduModel_Object = MibTableColumn
gnOduCfgXOduModel = _GnOduCfgXOduModel_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 4, 1, 25),
    _GnOduCfgXOduModel_Type()
)
gnOduCfgXOduModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduCfgXOduModel.setStatus("mandatory")
_GnOduCfgXFreqPlanStandard_Type = DisplayString
_GnOduCfgXFreqPlanStandard_Object = MibTableColumn
gnOduCfgXFreqPlanStandard = _GnOduCfgXFreqPlanStandard_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 4, 1, 26),
    _GnOduCfgXFreqPlanStandard_Type()
)
gnOduCfgXFreqPlanStandard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnOduCfgXFreqPlanStandard.setStatus("mandatory")
_GnOduCfgXFreqDevider_Type = Integer32
_GnOduCfgXFreqDevider_Object = MibTableColumn
gnOduCfgXFreqDevider = _GnOduCfgXFreqDevider_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 4, 1, 27),
    _GnOduCfgXFreqDevider_Type()
)
gnOduCfgXFreqDevider.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduCfgXFreqDevider.setStatus("mandatory")


class _GnOduCfgXLoopbackOption_Type(Integer32):
    """Custom type gnOduCfgXLoopbackOption based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("interfaceInterLoop", 3),
          ("noloopback", 2))
    )


_GnOduCfgXLoopbackOption_Type.__name__ = "Integer32"
_GnOduCfgXLoopbackOption_Object = MibTableColumn
gnOduCfgXLoopbackOption = _GnOduCfgXLoopbackOption_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 4, 1, 28),
    _GnOduCfgXLoopbackOption_Type()
)
gnOduCfgXLoopbackOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnOduCfgXLoopbackOption.setStatus("mandatory")


class _GnOduCfgXxpicClockMode_Type(Integer32):
    """Custom type gnOduCfgXxpicClockMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("masterClock", 3),
          ("slaveClock", 4),
          ("standAlone", 2))
    )


_GnOduCfgXxpicClockMode_Type.__name__ = "Integer32"
_GnOduCfgXxpicClockMode_Object = MibTableColumn
gnOduCfgXxpicClockMode = _GnOduCfgXxpicClockMode_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 4, 1, 29),
    _GnOduCfgXxpicClockMode_Type()
)
gnOduCfgXxpicClockMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduCfgXxpicClockMode.setStatus("mandatory")


class _GnOduCfgXUnfadedReferenceRsl_Type(Integer32):
    """Custom type gnOduCfgXUnfadedReferenceRsl based on Integer32"""
    defaultValue = -70

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-70, -15),
    )


_GnOduCfgXUnfadedReferenceRsl_Type.__name__ = "Integer32"
_GnOduCfgXUnfadedReferenceRsl_Object = MibTableColumn
gnOduCfgXUnfadedReferenceRsl = _GnOduCfgXUnfadedReferenceRsl_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 4, 1, 30),
    _GnOduCfgXUnfadedReferenceRsl_Type()
)
gnOduCfgXUnfadedReferenceRsl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnOduCfgXUnfadedReferenceRsl.setStatus("mandatory")


class _GnOduCfgXRfuMode_Type(Integer32):
    """Custom type gnOduCfgXRfuMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("combined", 4),
          ("diversity", 3),
          ("main", 2))
    )


_GnOduCfgXRfuMode_Type.__name__ = "Integer32"
_GnOduCfgXRfuMode_Object = MibTableColumn
gnOduCfgXRfuMode = _GnOduCfgXRfuMode_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 4, 1, 31),
    _GnOduCfgXRfuMode_Type()
)
gnOduCfgXRfuMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnOduCfgXRfuMode.setStatus("mandatory")


class _GnOduCfgXRslRouteToConnector_Type(Integer32):
    """Custom type gnOduCfgXRslRouteToConnector based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("diversity", 3),
          ("main", 2))
    )


_GnOduCfgXRslRouteToConnector_Type.__name__ = "Integer32"
_GnOduCfgXRslRouteToConnector_Object = MibTableColumn
gnOduCfgXRslRouteToConnector = _GnOduCfgXRslRouteToConnector_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 4, 1, 32),
    _GnOduCfgXRslRouteToConnector_Type()
)
gnOduCfgXRslRouteToConnector.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnOduCfgXRslRouteToConnector.setStatus("mandatory")


class _GnOduCfgXDelayCalibrationOperation_Type(Integer32):
    """Custom type gnOduCfgXDelayCalibrationOperation based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("activate", 3),
          ("error", 4),
          ("noAction", 2))
    )


_GnOduCfgXDelayCalibrationOperation_Type.__name__ = "Integer32"
_GnOduCfgXDelayCalibrationOperation_Object = MibTableColumn
gnOduCfgXDelayCalibrationOperation = _GnOduCfgXDelayCalibrationOperation_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 4, 1, 33),
    _GnOduCfgXDelayCalibrationOperation_Type()
)
gnOduCfgXDelayCalibrationOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnOduCfgXDelayCalibrationOperation.setStatus("mandatory")


class _GnOduCfgXDelayCalibrationValue_Type(Integer32):
    """Custom type gnOduCfgXDelayCalibrationValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-130, 130),
    )


_GnOduCfgXDelayCalibrationValue_Type.__name__ = "Integer32"
_GnOduCfgXDelayCalibrationValue_Object = MibTableColumn
gnOduCfgXDelayCalibrationValue = _GnOduCfgXDelayCalibrationValue_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 4, 1, 34),
    _GnOduCfgXDelayCalibrationValue_Type()
)
gnOduCfgXDelayCalibrationValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnOduCfgXDelayCalibrationValue.setStatus("mandatory")


class _GnOduCfgXDelayCalibrationWgType_Type(DisplayString):
    """Custom type gnOduCfgXDelayCalibrationWgType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 45),
    )


_GnOduCfgXDelayCalibrationWgType_Type.__name__ = "DisplayString"
_GnOduCfgXDelayCalibrationWgType_Object = MibTableColumn
gnOduCfgXDelayCalibrationWgType = _GnOduCfgXDelayCalibrationWgType_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 4, 1, 35),
    _GnOduCfgXDelayCalibrationWgType_Type()
)
gnOduCfgXDelayCalibrationWgType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnOduCfgXDelayCalibrationWgType.setStatus("mandatory")


class _GnOduCfgXOduLog_Type(Integer32):
    """Custom type gnOduCfgXOduLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("enable", 2))
    )


_GnOduCfgXOduLog_Type.__name__ = "Integer32"
_GnOduCfgXOduLog_Object = MibTableColumn
gnOduCfgXOduLog = _GnOduCfgXOduLog_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 4, 1, 36),
    _GnOduCfgXOduLog_Type()
)
gnOduCfgXOduLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnOduCfgXOduLog.setStatus("mandatory")


class _GnOduCfgXOduLogPeriod_Type(Integer32):
    """Custom type gnOduCfgXOduLogPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_GnOduCfgXOduLogPeriod_Type.__name__ = "Integer32"
_GnOduCfgXOduLogPeriod_Object = MibTableColumn
gnOduCfgXOduLogPeriod = _GnOduCfgXOduLogPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 4, 1, 37),
    _GnOduCfgXOduLogPeriod_Type()
)
gnOduCfgXOduLogPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnOduCfgXOduLogPeriod.setStatus("mandatory")


class _GnOduCfgXXpiPerfMonThresh_Type(Integer32):
    """Custom type gnOduCfgXXpiPerfMonThresh based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 30),
    )


_GnOduCfgXXpiPerfMonThresh_Type.__name__ = "Integer32"
_GnOduCfgXXpiPerfMonThresh_Object = MibTableColumn
gnOduCfgXXpiPerfMonThresh = _GnOduCfgXXpiPerfMonThresh_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 4, 1, 38),
    _GnOduCfgXXpiPerfMonThresh_Type()
)
gnOduCfgXXpiPerfMonThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnOduCfgXXpiPerfMonThresh.setStatus("mandatory")
_GnOduStatusXTable_Object = MibTable
gnOduStatusXTable = _GnOduStatusXTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 5)
)
if mibBuilder.loadTexts:
    gnOduStatusXTable.setStatus("mandatory")
_GnOduStatusXEntry_Object = MibTableRow
gnOduStatusXEntry = _GnOduStatusXEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 5, 1)
)
gnOduStatusXEntry.setIndexNames(
    (0, "CERAGON-MIB", "gnOduStatusXId"),
)
if mibBuilder.loadTexts:
    gnOduStatusXEntry.setStatus("mandatory")


class _GnOduStatusXId_Type(Integer32):
    """Custom type gnOduStatusXId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("drawer1", 3),
          ("drawer2", 4))
    )


_GnOduStatusXId_Type.__name__ = "Integer32"
_GnOduStatusXId_Object = MibTableColumn
gnOduStatusXId = _GnOduStatusXId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 5, 1, 1),
    _GnOduStatusXId_Type()
)
gnOduStatusXId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduStatusXId.setStatus("mandatory")


class _GnOduStatusXCelsiusTemp_Type(Integer32):
    """Custom type gnOduStatusXCelsiusTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-70, 80),
    )


_GnOduStatusXCelsiusTemp_Type.__name__ = "Integer32"
_GnOduStatusXCelsiusTemp_Object = MibTableColumn
gnOduStatusXCelsiusTemp = _GnOduStatusXCelsiusTemp_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 5, 1, 2),
    _GnOduStatusXCelsiusTemp_Type()
)
gnOduStatusXCelsiusTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduStatusXCelsiusTemp.setStatus("mandatory")


class _GnOduStatusXFahrenheitTemp_Type(Integer32):
    """Custom type gnOduStatusXFahrenheitTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-58, 176),
    )


_GnOduStatusXFahrenheitTemp_Type.__name__ = "Integer32"
_GnOduStatusXFahrenheitTemp_Object = MibTableColumn
gnOduStatusXFahrenheitTemp = _GnOduStatusXFahrenheitTemp_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 5, 1, 3),
    _GnOduStatusXFahrenheitTemp_Type()
)
gnOduStatusXFahrenheitTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduStatusXFahrenheitTemp.setStatus("mandatory")


class _GnOduStatusXTransmitLevel_Type(Integer32):
    """Custom type gnOduStatusXTransmitLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-99, 34),
    )


_GnOduStatusXTransmitLevel_Type.__name__ = "Integer32"
_GnOduStatusXTransmitLevel_Object = MibTableColumn
gnOduStatusXTransmitLevel = _GnOduStatusXTransmitLevel_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 5, 1, 4),
    _GnOduStatusXTransmitLevel_Type()
)
gnOduStatusXTransmitLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduStatusXTransmitLevel.setStatus("mandatory")


class _GnOduStatusXReceiveLevel_Type(Integer32):
    """Custom type gnOduStatusXReceiveLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-99, -15),
    )


_GnOduStatusXReceiveLevel_Type.__name__ = "Integer32"
_GnOduStatusXReceiveLevel_Object = MibTableColumn
gnOduStatusXReceiveLevel = _GnOduStatusXReceiveLevel_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 5, 1, 5),
    _GnOduStatusXReceiveLevel_Type()
)
gnOduStatusXReceiveLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduStatusXReceiveLevel.setStatus("mandatory")


class _GnOduStatusXSynthesizerVCOLock_Type(OctetString):
    """Custom type gnOduStatusXSynthesizerVCOLock based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_GnOduStatusXSynthesizerVCOLock_Type.__name__ = "OctetString"
_GnOduStatusXSynthesizerVCOLock_Object = MibTableColumn
gnOduStatusXSynthesizerVCOLock = _GnOduStatusXSynthesizerVCOLock_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 5, 1, 6),
    _GnOduStatusXSynthesizerVCOLock_Type()
)
gnOduStatusXSynthesizerVCOLock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduStatusXSynthesizerVCOLock.setStatus("mandatory")


class _GnOduStatusXPowerSupply_Type(OctetString):
    """Custom type gnOduStatusXPowerSupply based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_GnOduStatusXPowerSupply_Type.__name__ = "OctetString"
_GnOduStatusXPowerSupply_Object = MibTableColumn
gnOduStatusXPowerSupply = _GnOduStatusXPowerSupply_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 5, 1, 7),
    _GnOduStatusXPowerSupply_Type()
)
gnOduStatusXPowerSupply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduStatusXPowerSupply.setStatus("mandatory")


class _GnOduStatusXIfcSupported_Type(Integer32):
    """Custom type gnOduStatusXIfcSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 3),
          ("yes", 2))
    )


_GnOduStatusXIfcSupported_Type.__name__ = "Integer32"
_GnOduStatusXIfcSupported_Object = MibTableColumn
gnOduStatusXIfcSupported = _GnOduStatusXIfcSupported_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 5, 1, 8),
    _GnOduStatusXIfcSupported_Type()
)
gnOduStatusXIfcSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduStatusXIfcSupported.setStatus("mandatory")


class _GnOduStatusXRslDiversity_Type(Integer32):
    """Custom type gnOduStatusXRslDiversity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-99, 0),
    )


_GnOduStatusXRslDiversity_Type.__name__ = "Integer32"
_GnOduStatusXRslDiversity_Object = MibTableColumn
gnOduStatusXRslDiversity = _GnOduStatusXRslDiversity_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 5, 1, 9),
    _GnOduStatusXRslDiversity_Type()
)
gnOduStatusXRslDiversity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduStatusXRslDiversity.setStatus("mandatory")


class _GnOduStatusXRslCombined_Type(Integer32):
    """Custom type gnOduStatusXRslCombined based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-99, 0),
    )


_GnOduStatusXRslCombined_Type.__name__ = "Integer32"
_GnOduStatusXRslCombined_Object = MibTableColumn
gnOduStatusXRslCombined = _GnOduStatusXRslCombined_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 5, 1, 10),
    _GnOduStatusXRslCombined_Type()
)
gnOduStatusXRslCombined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduStatusXRslCombined.setStatus("mandatory")


class _GnOduStatusXRfuAddress_Type(Integer32):
    """Custom type gnOduStatusXRfuAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_GnOduStatusXRfuAddress_Type.__name__ = "Integer32"
_GnOduStatusXRfuAddress_Object = MibTableColumn
gnOduStatusXRfuAddress = _GnOduStatusXRfuAddress_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 5, 1, 11),
    _GnOduStatusXRfuAddress_Type()
)
gnOduStatusXRfuAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduStatusXRfuAddress.setStatus("mandatory")


class _GnOduStatusXMinTransmitLevel_Type(Integer32):
    """Custom type gnOduStatusXMinTransmitLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-50, 34),
    )


_GnOduStatusXMinTransmitLevel_Type.__name__ = "Integer32"
_GnOduStatusXMinTransmitLevel_Object = MibTableColumn
gnOduStatusXMinTransmitLevel = _GnOduStatusXMinTransmitLevel_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 5, 1, 12),
    _GnOduStatusXMinTransmitLevel_Type()
)
gnOduStatusXMinTransmitLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduStatusXMinTransmitLevel.setStatus("mandatory")


class _GnOduStatusXOduSWVer_Type(DisplayString):
    """Custom type gnOduStatusXOduSWVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_GnOduStatusXOduSWVer_Type.__name__ = "DisplayString"
_GnOduStatusXOduSWVer_Object = MibTableColumn
gnOduStatusXOduSWVer = _GnOduStatusXOduSWVer_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 5, 1, 13),
    _GnOduStatusXOduSWVer_Type()
)
gnOduStatusXOduSWVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduStatusXOduSWVer.setStatus("mandatory")


class _GnOduStatusXOduSWPostVer_Type(DisplayString):
    """Custom type gnOduStatusXOduSWPostVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_GnOduStatusXOduSWPostVer_Type.__name__ = "DisplayString"
_GnOduStatusXOduSWPostVer_Object = MibTableColumn
gnOduStatusXOduSWPostVer = _GnOduStatusXOduSWPostVer_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 5, 1, 14),
    _GnOduStatusXOduSWPostVer_Type()
)
gnOduStatusXOduSWPostVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduStatusXOduSWPostVer.setStatus("mandatory")


class _GnOduStatusXRfuFwVer_Type(DisplayString):
    """Custom type gnOduStatusXRfuFwVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_GnOduStatusXRfuFwVer_Type.__name__ = "DisplayString"
_GnOduStatusXRfuFwVer_Object = MibTableColumn
gnOduStatusXRfuFwVer = _GnOduStatusXRfuFwVer_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 5, 1, 15),
    _GnOduStatusXRfuFwVer_Type()
)
gnOduStatusXRfuFwVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduStatusXRfuFwVer.setStatus("mandatory")


class _GnOduStatusXValidIntervals_Type(Integer32):
    """Custom type gnOduStatusXValidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_GnOduStatusXValidIntervals_Type.__name__ = "Integer32"
_GnOduStatusXValidIntervals_Object = MibTableColumn
gnOduStatusXValidIntervals = _GnOduStatusXValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 5, 1, 16),
    _GnOduStatusXValidIntervals_Type()
)
gnOduStatusXValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduStatusXValidIntervals.setStatus("mandatory")
_GnOduMonitorX_ObjectIdentity = ObjectIdentity
gnOduMonitorX = _GnOduMonitorX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 6)
)
_GnOduMonCurrXTable_Object = MibTable
gnOduMonCurrXTable = _GnOduMonCurrXTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 6, 1)
)
if mibBuilder.loadTexts:
    gnOduMonCurrXTable.setStatus("mandatory")
_GnOduMonCurrXEntry_Object = MibTableRow
gnOduMonCurrXEntry = _GnOduMonCurrXEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 6, 1, 1)
)
gnOduMonCurrXEntry.setIndexNames(
    (0, "CERAGON-MIB", "gnOduMonCurrXId"),
)
if mibBuilder.loadTexts:
    gnOduMonCurrXEntry.setStatus("mandatory")


class _GnOduMonCurrXId_Type(Integer32):
    """Custom type gnOduMonCurrXId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("drawer1", 3),
          ("drawer2", 4))
    )


_GnOduMonCurrXId_Type.__name__ = "Integer32"
_GnOduMonCurrXId_Object = MibTableColumn
gnOduMonCurrXId = _GnOduMonCurrXId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 6, 1, 1, 1),
    _GnOduMonCurrXId_Type()
)
gnOduMonCurrXId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonCurrXId.setStatus("mandatory")
_GnOduMonCurrXMinRL_Type = Integer32
_GnOduMonCurrXMinRL_Object = MibTableColumn
gnOduMonCurrXMinRL = _GnOduMonCurrXMinRL_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 6, 1, 1, 2),
    _GnOduMonCurrXMinRL_Type()
)
gnOduMonCurrXMinRL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonCurrXMinRL.setStatus("mandatory")
_GnOduMonCurrXMaxRL_Type = Integer32
_GnOduMonCurrXMaxRL_Object = MibTableColumn
gnOduMonCurrXMaxRL = _GnOduMonCurrXMaxRL_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 6, 1, 1, 3),
    _GnOduMonCurrXMaxRL_Type()
)
gnOduMonCurrXMaxRL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonCurrXMaxRL.setStatus("mandatory")
_GnOduMonCurrXTLThresh1Exceed_Type = Counter32
_GnOduMonCurrXTLThresh1Exceed_Object = MibTableColumn
gnOduMonCurrXTLThresh1Exceed = _GnOduMonCurrXTLThresh1Exceed_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 6, 1, 1, 4),
    _GnOduMonCurrXTLThresh1Exceed_Type()
)
gnOduMonCurrXTLThresh1Exceed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonCurrXTLThresh1Exceed.setStatus("mandatory")
_GnOduMonCurrXRLThresh1Exceed_Type = Counter32
_GnOduMonCurrXRLThresh1Exceed_Object = MibTableColumn
gnOduMonCurrXRLThresh1Exceed = _GnOduMonCurrXRLThresh1Exceed_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 6, 1, 1, 5),
    _GnOduMonCurrXRLThresh1Exceed_Type()
)
gnOduMonCurrXRLThresh1Exceed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonCurrXRLThresh1Exceed.setStatus("mandatory")
_GnOduMonCurrXRLThresh2Exceed_Type = Counter32
_GnOduMonCurrXRLThresh2Exceed_Object = MibTableColumn
gnOduMonCurrXRLThresh2Exceed = _GnOduMonCurrXRLThresh2Exceed_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 6, 1, 1, 6),
    _GnOduMonCurrXRLThresh2Exceed_Type()
)
gnOduMonCurrXRLThresh2Exceed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonCurrXRLThresh2Exceed.setStatus("mandatory")
_GnOduMonCurrXDayMinRL_Type = Integer32
_GnOduMonCurrXDayMinRL_Object = MibTableColumn
gnOduMonCurrXDayMinRL = _GnOduMonCurrXDayMinRL_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 6, 1, 1, 7),
    _GnOduMonCurrXDayMinRL_Type()
)
gnOduMonCurrXDayMinRL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonCurrXDayMinRL.setStatus("mandatory")
_GnOduMonCurrXDayMaxRL_Type = Integer32
_GnOduMonCurrXDayMaxRL_Object = MibTableColumn
gnOduMonCurrXDayMaxRL = _GnOduMonCurrXDayMaxRL_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 6, 1, 1, 8),
    _GnOduMonCurrXDayMaxRL_Type()
)
gnOduMonCurrXDayMaxRL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonCurrXDayMaxRL.setStatus("mandatory")
_GnOduMonCurrXDayTLThresh1Exceed_Type = Counter32
_GnOduMonCurrXDayTLThresh1Exceed_Object = MibTableColumn
gnOduMonCurrXDayTLThresh1Exceed = _GnOduMonCurrXDayTLThresh1Exceed_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 6, 1, 1, 9),
    _GnOduMonCurrXDayTLThresh1Exceed_Type()
)
gnOduMonCurrXDayTLThresh1Exceed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonCurrXDayTLThresh1Exceed.setStatus("mandatory")
_GnOduMonCurrXDayRLThresh1Exceed_Type = Counter32
_GnOduMonCurrXDayRLThresh1Exceed_Object = MibTableColumn
gnOduMonCurrXDayRLThresh1Exceed = _GnOduMonCurrXDayRLThresh1Exceed_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 6, 1, 1, 10),
    _GnOduMonCurrXDayRLThresh1Exceed_Type()
)
gnOduMonCurrXDayRLThresh1Exceed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonCurrXDayRLThresh1Exceed.setStatus("mandatory")
_GnOduMonCurrXDayRLThresh2Exceed_Type = Counter32
_GnOduMonCurrXDayRLThresh2Exceed_Object = MibTableColumn
gnOduMonCurrXDayRLThresh2Exceed = _GnOduMonCurrXDayRLThresh2Exceed_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 6, 1, 1, 11),
    _GnOduMonCurrXDayRLThresh2Exceed_Type()
)
gnOduMonCurrXDayRLThresh2Exceed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonCurrXDayRLThresh2Exceed.setStatus("mandatory")
_GnOduMonCurrXMinTL_Type = Integer32
_GnOduMonCurrXMinTL_Object = MibTableColumn
gnOduMonCurrXMinTL = _GnOduMonCurrXMinTL_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 6, 1, 1, 12),
    _GnOduMonCurrXMinTL_Type()
)
gnOduMonCurrXMinTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonCurrXMinTL.setStatus("mandatory")
_GnOduMonCurrXMaxTL_Type = Integer32
_GnOduMonCurrXMaxTL_Object = MibTableColumn
gnOduMonCurrXMaxTL = _GnOduMonCurrXMaxTL_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 6, 1, 1, 13),
    _GnOduMonCurrXMaxTL_Type()
)
gnOduMonCurrXMaxTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonCurrXMaxTL.setStatus("mandatory")
_GnOduMonCurrXDayMinTL_Type = Integer32
_GnOduMonCurrXDayMinTL_Object = MibTableColumn
gnOduMonCurrXDayMinTL = _GnOduMonCurrXDayMinTL_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 6, 1, 1, 14),
    _GnOduMonCurrXDayMinTL_Type()
)
gnOduMonCurrXDayMinTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonCurrXDayMinTL.setStatus("mandatory")
_GnOduMonCurrXDayMaxTL_Type = Integer32
_GnOduMonCurrXDayMaxTL_Object = MibTableColumn
gnOduMonCurrXDayMaxTL = _GnOduMonCurrXDayMaxTL_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 6, 1, 1, 15),
    _GnOduMonCurrXDayMaxTL_Type()
)
gnOduMonCurrXDayMaxTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonCurrXDayMaxTL.setStatus("mandatory")
_GnOduMonCurrXXpi_Type = Integer32
_GnOduMonCurrXXpi_Object = MibTableColumn
gnOduMonCurrXXpi = _GnOduMonCurrXXpi_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 6, 1, 1, 16),
    _GnOduMonCurrXXpi_Type()
)
gnOduMonCurrXXpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonCurrXXpi.setStatus("mandatory")
_GnOduMonCurrXMinXpi_Type = Integer32
_GnOduMonCurrXMinXpi_Object = MibTableColumn
gnOduMonCurrXMinXpi = _GnOduMonCurrXMinXpi_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 6, 1, 1, 17),
    _GnOduMonCurrXMinXpi_Type()
)
gnOduMonCurrXMinXpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonCurrXMinXpi.setStatus("mandatory")
_GnOduMonCurrXMaxXpi_Type = Integer32
_GnOduMonCurrXMaxXpi_Object = MibTableColumn
gnOduMonCurrXMaxXpi = _GnOduMonCurrXMaxXpi_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 6, 1, 1, 18),
    _GnOduMonCurrXMaxXpi_Type()
)
gnOduMonCurrXMaxXpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonCurrXMaxXpi.setStatus("mandatory")
_GnOduMonCurrXDayMinXpi_Type = Integer32
_GnOduMonCurrXDayMinXpi_Object = MibTableColumn
gnOduMonCurrXDayMinXpi = _GnOduMonCurrXDayMinXpi_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 6, 1, 1, 19),
    _GnOduMonCurrXDayMinXpi_Type()
)
gnOduMonCurrXDayMinXpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonCurrXDayMinXpi.setStatus("mandatory")
_GnOduMonCurrXDayMaxXpi_Type = Integer32
_GnOduMonCurrXDayMaxXpi_Object = MibTableColumn
gnOduMonCurrXDayMaxXpi = _GnOduMonCurrXDayMaxXpi_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 6, 1, 1, 20),
    _GnOduMonCurrXDayMaxXpi_Type()
)
gnOduMonCurrXDayMaxXpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonCurrXDayMaxXpi.setStatus("mandatory")
_GnOduMonCurrXXpiThreshExceed_Type = Counter32
_GnOduMonCurrXXpiThreshExceed_Object = MibTableColumn
gnOduMonCurrXXpiThreshExceed = _GnOduMonCurrXXpiThreshExceed_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 6, 1, 1, 21),
    _GnOduMonCurrXXpiThreshExceed_Type()
)
gnOduMonCurrXXpiThreshExceed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonCurrXXpiThreshExceed.setStatus("mandatory")
_GnOduMonCurrXDayXpiThreshExceed_Type = Counter32
_GnOduMonCurrXDayXpiThreshExceed_Object = MibTableColumn
gnOduMonCurrXDayXpiThreshExceed = _GnOduMonCurrXDayXpiThreshExceed_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 6, 1, 1, 22),
    _GnOduMonCurrXDayXpiThreshExceed_Type()
)
gnOduMonCurrXDayXpiThreshExceed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonCurrXDayXpiThreshExceed.setStatus("mandatory")
_GnOduMonCurrXMse_Type = Integer32
_GnOduMonCurrXMse_Object = MibTableColumn
gnOduMonCurrXMse = _GnOduMonCurrXMse_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 6, 1, 1, 23),
    _GnOduMonCurrXMse_Type()
)
gnOduMonCurrXMse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonCurrXMse.setStatus("mandatory")


class _GnOduMonCurrXLastDayIDF_Type(Integer32):
    """Custom type gnOduMonCurrXLastDayIDF based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3))
    )


_GnOduMonCurrXLastDayIDF_Type.__name__ = "Integer32"
_GnOduMonCurrXLastDayIDF_Object = MibTableColumn
gnOduMonCurrXLastDayIDF = _GnOduMonCurrXLastDayIDF_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 6, 1, 1, 24),
    _GnOduMonCurrXLastDayIDF_Type()
)
gnOduMonCurrXLastDayIDF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonCurrXLastDayIDF.setStatus("mandatory")
_GnOduMonIntervalXTable_Object = MibTable
gnOduMonIntervalXTable = _GnOduMonIntervalXTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 6, 2)
)
if mibBuilder.loadTexts:
    gnOduMonIntervalXTable.setStatus("mandatory")
_GnOduMonIntervalXEntry_Object = MibTableRow
gnOduMonIntervalXEntry = _GnOduMonIntervalXEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 6, 2, 1)
)
gnOduMonIntervalXEntry.setIndexNames(
    (0, "CERAGON-MIB", "gnOduMonIntervalXId"),
    (0, "CERAGON-MIB", "gnOduMonIntervalXIdx"),
)
if mibBuilder.loadTexts:
    gnOduMonIntervalXEntry.setStatus("mandatory")


class _GnOduMonIntervalXId_Type(Integer32):
    """Custom type gnOduMonIntervalXId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("drawer1", 3),
          ("drawer2", 4))
    )


_GnOduMonIntervalXId_Type.__name__ = "Integer32"
_GnOduMonIntervalXId_Object = MibTableColumn
gnOduMonIntervalXId = _GnOduMonIntervalXId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 6, 2, 1, 1),
    _GnOduMonIntervalXId_Type()
)
gnOduMonIntervalXId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonIntervalXId.setStatus("mandatory")


class _GnOduMonIntervalXIdx_Type(Integer32):
    """Custom type gnOduMonIntervalXIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_GnOduMonIntervalXIdx_Type.__name__ = "Integer32"
_GnOduMonIntervalXIdx_Object = MibTableColumn
gnOduMonIntervalXIdx = _GnOduMonIntervalXIdx_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 6, 2, 1, 2),
    _GnOduMonIntervalXIdx_Type()
)
gnOduMonIntervalXIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonIntervalXIdx.setStatus("mandatory")
_GnOduMonIntervalXMinRL_Type = Integer32
_GnOduMonIntervalXMinRL_Object = MibTableColumn
gnOduMonIntervalXMinRL = _GnOduMonIntervalXMinRL_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 6, 2, 1, 3),
    _GnOduMonIntervalXMinRL_Type()
)
gnOduMonIntervalXMinRL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonIntervalXMinRL.setStatus("mandatory")
_GnOduMonIntervalXMaxRL_Type = Integer32
_GnOduMonIntervalXMaxRL_Object = MibTableColumn
gnOduMonIntervalXMaxRL = _GnOduMonIntervalXMaxRL_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 6, 2, 1, 4),
    _GnOduMonIntervalXMaxRL_Type()
)
gnOduMonIntervalXMaxRL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonIntervalXMaxRL.setStatus("mandatory")
_GnOduMonIntervalXTLThresh1Exceed_Type = Counter32
_GnOduMonIntervalXTLThresh1Exceed_Object = MibTableColumn
gnOduMonIntervalXTLThresh1Exceed = _GnOduMonIntervalXTLThresh1Exceed_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 6, 2, 1, 5),
    _GnOduMonIntervalXTLThresh1Exceed_Type()
)
gnOduMonIntervalXTLThresh1Exceed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonIntervalXTLThresh1Exceed.setStatus("mandatory")


class _GnOduMonIntervalXEvent_Type(OctetString):
    """Custom type gnOduMonIntervalXEvent based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_GnOduMonIntervalXEvent_Type.__name__ = "OctetString"
_GnOduMonIntervalXEvent_Object = MibTableColumn
gnOduMonIntervalXEvent = _GnOduMonIntervalXEvent_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 6, 2, 1, 6),
    _GnOduMonIntervalXEvent_Type()
)
gnOduMonIntervalXEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonIntervalXEvent.setStatus("mandatory")
_GnOduMonIntervalXRLThresh1Exceed_Type = Counter32
_GnOduMonIntervalXRLThresh1Exceed_Object = MibTableColumn
gnOduMonIntervalXRLThresh1Exceed = _GnOduMonIntervalXRLThresh1Exceed_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 6, 2, 1, 7),
    _GnOduMonIntervalXRLThresh1Exceed_Type()
)
gnOduMonIntervalXRLThresh1Exceed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonIntervalXRLThresh1Exceed.setStatus("mandatory")
_GnOduMonIntervalXRLThresh2Exceed_Type = Counter32
_GnOduMonIntervalXRLThresh2Exceed_Object = MibTableColumn
gnOduMonIntervalXRLThresh2Exceed = _GnOduMonIntervalXRLThresh2Exceed_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 6, 2, 1, 8),
    _GnOduMonIntervalXRLThresh2Exceed_Type()
)
gnOduMonIntervalXRLThresh2Exceed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonIntervalXRLThresh2Exceed.setStatus("mandatory")
_GnOduMonIntervalXMinTL_Type = Integer32
_GnOduMonIntervalXMinTL_Object = MibTableColumn
gnOduMonIntervalXMinTL = _GnOduMonIntervalXMinTL_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 6, 2, 1, 9),
    _GnOduMonIntervalXMinTL_Type()
)
gnOduMonIntervalXMinTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonIntervalXMinTL.setStatus("mandatory")
_GnOduMonIntervalXMaxTL_Type = Integer32
_GnOduMonIntervalXMaxTL_Object = MibTableColumn
gnOduMonIntervalXMaxTL = _GnOduMonIntervalXMaxTL_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 6, 2, 1, 10),
    _GnOduMonIntervalXMaxTL_Type()
)
gnOduMonIntervalXMaxTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonIntervalXMaxTL.setStatus("mandatory")
_GnOduMonIntervalXMinXpi_Type = Integer32
_GnOduMonIntervalXMinXpi_Object = MibTableColumn
gnOduMonIntervalXMinXpi = _GnOduMonIntervalXMinXpi_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 6, 2, 1, 11),
    _GnOduMonIntervalXMinXpi_Type()
)
gnOduMonIntervalXMinXpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonIntervalXMinXpi.setStatus("mandatory")
_GnOduMonIntervalXMaxXpi_Type = Integer32
_GnOduMonIntervalXMaxXpi_Object = MibTableColumn
gnOduMonIntervalXMaxXpi = _GnOduMonIntervalXMaxXpi_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 6, 2, 1, 12),
    _GnOduMonIntervalXMaxXpi_Type()
)
gnOduMonIntervalXMaxXpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonIntervalXMaxXpi.setStatus("mandatory")
_GnOduMonIntervalXXpiThreshExceed_Type = Counter32
_GnOduMonIntervalXXpiThreshExceed_Object = MibTableColumn
gnOduMonIntervalXXpiThreshExceed = _GnOduMonIntervalXXpiThreshExceed_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 6, 2, 1, 13),
    _GnOduMonIntervalXXpiThreshExceed_Type()
)
gnOduMonIntervalXXpiThreshExceed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonIntervalXXpiThreshExceed.setStatus("mandatory")


class _GnOduMonIntervalXIDF_Type(Integer32):
    """Custom type gnOduMonIntervalXIDF based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3))
    )


_GnOduMonIntervalXIDF_Type.__name__ = "Integer32"
_GnOduMonIntervalXIDF_Object = MibTableColumn
gnOduMonIntervalXIDF = _GnOduMonIntervalXIDF_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 6, 2, 1, 14),
    _GnOduMonIntervalXIDF_Type()
)
gnOduMonIntervalXIDF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonIntervalXIDF.setStatus("mandatory")
_GnOduMonDayXTable_Object = MibTable
gnOduMonDayXTable = _GnOduMonDayXTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 6, 3)
)
if mibBuilder.loadTexts:
    gnOduMonDayXTable.setStatus("mandatory")
_GnOduMonDayXEntry_Object = MibTableRow
gnOduMonDayXEntry = _GnOduMonDayXEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 6, 3, 1)
)
gnOduMonDayXEntry.setIndexNames(
    (0, "CERAGON-MIB", "gnOduMonDayXId"),
    (0, "CERAGON-MIB", "gnOduMonDayXIdx"),
)
if mibBuilder.loadTexts:
    gnOduMonDayXEntry.setStatus("mandatory")


class _GnOduMonDayXId_Type(Integer32):
    """Custom type gnOduMonDayXId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("drawer1", 3),
          ("drawer2", 4))
    )


_GnOduMonDayXId_Type.__name__ = "Integer32"
_GnOduMonDayXId_Object = MibTableColumn
gnOduMonDayXId = _GnOduMonDayXId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 6, 3, 1, 1),
    _GnOduMonDayXId_Type()
)
gnOduMonDayXId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonDayXId.setStatus("mandatory")


class _GnOduMonDayXIdx_Type(Integer32):
    """Custom type gnOduMonDayXIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_GnOduMonDayXIdx_Type.__name__ = "Integer32"
_GnOduMonDayXIdx_Object = MibTableColumn
gnOduMonDayXIdx = _GnOduMonDayXIdx_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 6, 3, 1, 2),
    _GnOduMonDayXIdx_Type()
)
gnOduMonDayXIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonDayXIdx.setStatus("mandatory")
_GnOduMonDayXMinRL_Type = Integer32
_GnOduMonDayXMinRL_Object = MibTableColumn
gnOduMonDayXMinRL = _GnOduMonDayXMinRL_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 6, 3, 1, 3),
    _GnOduMonDayXMinRL_Type()
)
gnOduMonDayXMinRL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonDayXMinRL.setStatus("mandatory")
_GnOduMonDayXMaxRL_Type = Integer32
_GnOduMonDayXMaxRL_Object = MibTableColumn
gnOduMonDayXMaxRL = _GnOduMonDayXMaxRL_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 6, 3, 1, 4),
    _GnOduMonDayXMaxRL_Type()
)
gnOduMonDayXMaxRL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonDayXMaxRL.setStatus("mandatory")
_GnOduMonDayXTLThresh1Exceed_Type = Counter32
_GnOduMonDayXTLThresh1Exceed_Object = MibTableColumn
gnOduMonDayXTLThresh1Exceed = _GnOduMonDayXTLThresh1Exceed_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 6, 3, 1, 5),
    _GnOduMonDayXTLThresh1Exceed_Type()
)
gnOduMonDayXTLThresh1Exceed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonDayXTLThresh1Exceed.setStatus("mandatory")
_GnOduMonDayXRLThresh1Exceed_Type = Counter32
_GnOduMonDayXRLThresh1Exceed_Object = MibTableColumn
gnOduMonDayXRLThresh1Exceed = _GnOduMonDayXRLThresh1Exceed_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 6, 3, 1, 6),
    _GnOduMonDayXRLThresh1Exceed_Type()
)
gnOduMonDayXRLThresh1Exceed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonDayXRLThresh1Exceed.setStatus("mandatory")
_GnOduMonDayXRLThresh2Exceed_Type = Counter32
_GnOduMonDayXRLThresh2Exceed_Object = MibTableColumn
gnOduMonDayXRLThresh2Exceed = _GnOduMonDayXRLThresh2Exceed_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 6, 3, 1, 7),
    _GnOduMonDayXRLThresh2Exceed_Type()
)
gnOduMonDayXRLThresh2Exceed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonDayXRLThresh2Exceed.setStatus("mandatory")
_GnOduMonDayXMinTL_Type = Integer32
_GnOduMonDayXMinTL_Object = MibTableColumn
gnOduMonDayXMinTL = _GnOduMonDayXMinTL_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 6, 3, 1, 8),
    _GnOduMonDayXMinTL_Type()
)
gnOduMonDayXMinTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonDayXMinTL.setStatus("mandatory")
_GnOduMonDayXMaxTL_Type = Integer32
_GnOduMonDayXMaxTL_Object = MibTableColumn
gnOduMonDayXMaxTL = _GnOduMonDayXMaxTL_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 6, 3, 1, 9),
    _GnOduMonDayXMaxTL_Type()
)
gnOduMonDayXMaxTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonDayXMaxTL.setStatus("mandatory")
_GnOduMonDayXMinXpi_Type = Integer32
_GnOduMonDayXMinXpi_Object = MibTableColumn
gnOduMonDayXMinXpi = _GnOduMonDayXMinXpi_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 6, 3, 1, 10),
    _GnOduMonDayXMinXpi_Type()
)
gnOduMonDayXMinXpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonDayXMinXpi.setStatus("mandatory")
_GnOduMonDayXMaxXpi_Type = Integer32
_GnOduMonDayXMaxXpi_Object = MibTableColumn
gnOduMonDayXMaxXpi = _GnOduMonDayXMaxXpi_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 6, 3, 1, 11),
    _GnOduMonDayXMaxXpi_Type()
)
gnOduMonDayXMaxXpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonDayXMaxXpi.setStatus("mandatory")
_GnOduMonDayXXpiThreshExceed_Type = Counter32
_GnOduMonDayXXpiThreshExceed_Object = MibTableColumn
gnOduMonDayXXpiThreshExceed = _GnOduMonDayXXpiThreshExceed_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 6, 3, 1, 12),
    _GnOduMonDayXXpiThreshExceed_Type()
)
gnOduMonDayXXpiThreshExceed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonDayXXpiThreshExceed.setStatus("mandatory")


class _GnOduMonDayXIDF_Type(Integer32):
    """Custom type gnOduMonDayXIDF based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3))
    )


_GnOduMonDayXIDF_Type.__name__ = "Integer32"
_GnOduMonDayXIDF_Object = MibTableColumn
gnOduMonDayXIDF = _GnOduMonDayXIDF_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 6, 3, 1, 13),
    _GnOduMonDayXIDF_Type()
)
gnOduMonDayXIDF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonDayXIDF.setStatus("mandatory")
_GnOduMonCurrDiversityXTable_Object = MibTable
gnOduMonCurrDiversityXTable = _GnOduMonCurrDiversityXTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 6, 4)
)
if mibBuilder.loadTexts:
    gnOduMonCurrDiversityXTable.setStatus("mandatory")
_GnOduMonCurrDiversityXEntry_Object = MibTableRow
gnOduMonCurrDiversityXEntry = _GnOduMonCurrDiversityXEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 6, 4, 1)
)
gnOduMonCurrDiversityXEntry.setIndexNames(
    (0, "CERAGON-MIB", "gnOduMonCurrDiversityXId"),
)
if mibBuilder.loadTexts:
    gnOduMonCurrDiversityXEntry.setStatus("mandatory")


class _GnOduMonCurrDiversityXId_Type(Integer32):
    """Custom type gnOduMonCurrDiversityXId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("drawer1", 3),
          ("drawer2", 4))
    )


_GnOduMonCurrDiversityXId_Type.__name__ = "Integer32"
_GnOduMonCurrDiversityXId_Object = MibTableColumn
gnOduMonCurrDiversityXId = _GnOduMonCurrDiversityXId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 6, 4, 1, 1),
    _GnOduMonCurrDiversityXId_Type()
)
gnOduMonCurrDiversityXId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonCurrDiversityXId.setStatus("mandatory")
_GnOduMonCurrDiversityXMinRL_Type = Integer32
_GnOduMonCurrDiversityXMinRL_Object = MibTableColumn
gnOduMonCurrDiversityXMinRL = _GnOduMonCurrDiversityXMinRL_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 6, 4, 1, 2),
    _GnOduMonCurrDiversityXMinRL_Type()
)
gnOduMonCurrDiversityXMinRL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonCurrDiversityXMinRL.setStatus("mandatory")
_GnOduMonCurrDiversityXMaxRL_Type = Integer32
_GnOduMonCurrDiversityXMaxRL_Object = MibTableColumn
gnOduMonCurrDiversityXMaxRL = _GnOduMonCurrDiversityXMaxRL_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 6, 4, 1, 3),
    _GnOduMonCurrDiversityXMaxRL_Type()
)
gnOduMonCurrDiversityXMaxRL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonCurrDiversityXMaxRL.setStatus("mandatory")
_GnOduMonCurrDiversityXRLThresh1Exceed_Type = Counter32
_GnOduMonCurrDiversityXRLThresh1Exceed_Object = MibTableColumn
gnOduMonCurrDiversityXRLThresh1Exceed = _GnOduMonCurrDiversityXRLThresh1Exceed_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 6, 4, 1, 4),
    _GnOduMonCurrDiversityXRLThresh1Exceed_Type()
)
gnOduMonCurrDiversityXRLThresh1Exceed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonCurrDiversityXRLThresh1Exceed.setStatus("mandatory")
_GnOduMonCurrDiversityXRLThresh2Exceed_Type = Counter32
_GnOduMonCurrDiversityXRLThresh2Exceed_Object = MibTableColumn
gnOduMonCurrDiversityXRLThresh2Exceed = _GnOduMonCurrDiversityXRLThresh2Exceed_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 6, 4, 1, 5),
    _GnOduMonCurrDiversityXRLThresh2Exceed_Type()
)
gnOduMonCurrDiversityXRLThresh2Exceed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonCurrDiversityXRLThresh2Exceed.setStatus("mandatory")
_GnOduMonCurrDiversityXDayMinRL_Type = Integer32
_GnOduMonCurrDiversityXDayMinRL_Object = MibTableColumn
gnOduMonCurrDiversityXDayMinRL = _GnOduMonCurrDiversityXDayMinRL_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 6, 4, 1, 6),
    _GnOduMonCurrDiversityXDayMinRL_Type()
)
gnOduMonCurrDiversityXDayMinRL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonCurrDiversityXDayMinRL.setStatus("mandatory")
_GnOduMonCurrDiversityXDayMaxRL_Type = Integer32
_GnOduMonCurrDiversityXDayMaxRL_Object = MibTableColumn
gnOduMonCurrDiversityXDayMaxRL = _GnOduMonCurrDiversityXDayMaxRL_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 6, 4, 1, 7),
    _GnOduMonCurrDiversityXDayMaxRL_Type()
)
gnOduMonCurrDiversityXDayMaxRL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonCurrDiversityXDayMaxRL.setStatus("mandatory")
_GnOduMonCurrDiversityXDayRLThresh1Exceed_Type = Integer32
_GnOduMonCurrDiversityXDayRLThresh1Exceed_Object = MibTableColumn
gnOduMonCurrDiversityXDayRLThresh1Exceed = _GnOduMonCurrDiversityXDayRLThresh1Exceed_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 6, 4, 1, 8),
    _GnOduMonCurrDiversityXDayRLThresh1Exceed_Type()
)
gnOduMonCurrDiversityXDayRLThresh1Exceed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonCurrDiversityXDayRLThresh1Exceed.setStatus("mandatory")
_GnOduMonCurrDiversityXDayRLThresh2Exceed_Type = Integer32
_GnOduMonCurrDiversityXDayRLThresh2Exceed_Object = MibTableColumn
gnOduMonCurrDiversityXDayRLThresh2Exceed = _GnOduMonCurrDiversityXDayRLThresh2Exceed_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 6, 4, 1, 9),
    _GnOduMonCurrDiversityXDayRLThresh2Exceed_Type()
)
gnOduMonCurrDiversityXDayRLThresh2Exceed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonCurrDiversityXDayRLThresh2Exceed.setStatus("mandatory")
_GnOduMonIntervalDiversityXTable_Object = MibTable
gnOduMonIntervalDiversityXTable = _GnOduMonIntervalDiversityXTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 6, 5)
)
if mibBuilder.loadTexts:
    gnOduMonIntervalDiversityXTable.setStatus("mandatory")
_GnOduMonIntervalDiversityXEntry_Object = MibTableRow
gnOduMonIntervalDiversityXEntry = _GnOduMonIntervalDiversityXEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 6, 5, 1)
)
gnOduMonIntervalDiversityXEntry.setIndexNames(
    (0, "CERAGON-MIB", "gnOduMonIntervalDiversityXId"),
    (0, "CERAGON-MIB", "gnOduMonIntervalDiversityXIdx"),
)
if mibBuilder.loadTexts:
    gnOduMonIntervalDiversityXEntry.setStatus("mandatory")


class _GnOduMonIntervalDiversityXId_Type(Integer32):
    """Custom type gnOduMonIntervalDiversityXId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("drawer1", 3),
          ("drawer2", 4))
    )


_GnOduMonIntervalDiversityXId_Type.__name__ = "Integer32"
_GnOduMonIntervalDiversityXId_Object = MibTableColumn
gnOduMonIntervalDiversityXId = _GnOduMonIntervalDiversityXId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 6, 5, 1, 1),
    _GnOduMonIntervalDiversityXId_Type()
)
gnOduMonIntervalDiversityXId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonIntervalDiversityXId.setStatus("mandatory")


class _GnOduMonIntervalDiversityXIdx_Type(Integer32):
    """Custom type gnOduMonIntervalDiversityXIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_GnOduMonIntervalDiversityXIdx_Type.__name__ = "Integer32"
_GnOduMonIntervalDiversityXIdx_Object = MibTableColumn
gnOduMonIntervalDiversityXIdx = _GnOduMonIntervalDiversityXIdx_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 6, 5, 1, 2),
    _GnOduMonIntervalDiversityXIdx_Type()
)
gnOduMonIntervalDiversityXIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonIntervalDiversityXIdx.setStatus("mandatory")
_GnOduMonIntervalDiversityXMinRL_Type = Integer32
_GnOduMonIntervalDiversityXMinRL_Object = MibTableColumn
gnOduMonIntervalDiversityXMinRL = _GnOduMonIntervalDiversityXMinRL_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 6, 5, 1, 3),
    _GnOduMonIntervalDiversityXMinRL_Type()
)
gnOduMonIntervalDiversityXMinRL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonIntervalDiversityXMinRL.setStatus("mandatory")
_GnOduMonIntervalDiversityXMaxRL_Type = Integer32
_GnOduMonIntervalDiversityXMaxRL_Object = MibTableColumn
gnOduMonIntervalDiversityXMaxRL = _GnOduMonIntervalDiversityXMaxRL_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 6, 5, 1, 4),
    _GnOduMonIntervalDiversityXMaxRL_Type()
)
gnOduMonIntervalDiversityXMaxRL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonIntervalDiversityXMaxRL.setStatus("mandatory")
_GnOduMonIntervalDiversityXRLThresh1Exceed_Type = Counter32
_GnOduMonIntervalDiversityXRLThresh1Exceed_Object = MibTableColumn
gnOduMonIntervalDiversityXRLThresh1Exceed = _GnOduMonIntervalDiversityXRLThresh1Exceed_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 6, 5, 1, 5),
    _GnOduMonIntervalDiversityXRLThresh1Exceed_Type()
)
gnOduMonIntervalDiversityXRLThresh1Exceed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonIntervalDiversityXRLThresh1Exceed.setStatus("mandatory")
_GnOduMonIntervalDiversityXRLThresh2Exceed_Type = Counter32
_GnOduMonIntervalDiversityXRLThresh2Exceed_Object = MibTableColumn
gnOduMonIntervalDiversityXRLThresh2Exceed = _GnOduMonIntervalDiversityXRLThresh2Exceed_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 6, 5, 1, 6),
    _GnOduMonIntervalDiversityXRLThresh2Exceed_Type()
)
gnOduMonIntervalDiversityXRLThresh2Exceed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonIntervalDiversityXRLThresh2Exceed.setStatus("mandatory")
_GnOduMonDayDiversityXTable_Object = MibTable
gnOduMonDayDiversityXTable = _GnOduMonDayDiversityXTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 6, 6)
)
if mibBuilder.loadTexts:
    gnOduMonDayDiversityXTable.setStatus("mandatory")
_GnOduMonDayDiversityXEntry_Object = MibTableRow
gnOduMonDayDiversityXEntry = _GnOduMonDayDiversityXEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 6, 6, 1)
)
gnOduMonDayDiversityXEntry.setIndexNames(
    (0, "CERAGON-MIB", "gnOduMonDayDiversityXId"),
    (0, "CERAGON-MIB", "gnOduMonDayDiversityXIdx"),
)
if mibBuilder.loadTexts:
    gnOduMonDayDiversityXEntry.setStatus("mandatory")


class _GnOduMonDayDiversityXId_Type(Integer32):
    """Custom type gnOduMonDayDiversityXId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("drawer1", 3),
          ("drawer2", 4))
    )


_GnOduMonDayDiversityXId_Type.__name__ = "Integer32"
_GnOduMonDayDiversityXId_Object = MibTableColumn
gnOduMonDayDiversityXId = _GnOduMonDayDiversityXId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 6, 6, 1, 1),
    _GnOduMonDayDiversityXId_Type()
)
gnOduMonDayDiversityXId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonDayDiversityXId.setStatus("mandatory")


class _GnOduMonDayDiversityXIdx_Type(Integer32):
    """Custom type gnOduMonDayDiversityXIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_GnOduMonDayDiversityXIdx_Type.__name__ = "Integer32"
_GnOduMonDayDiversityXIdx_Object = MibTableColumn
gnOduMonDayDiversityXIdx = _GnOduMonDayDiversityXIdx_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 6, 6, 1, 2),
    _GnOduMonDayDiversityXIdx_Type()
)
gnOduMonDayDiversityXIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonDayDiversityXIdx.setStatus("mandatory")
_GnOduMonDayDiversityXMinRL_Type = Integer32
_GnOduMonDayDiversityXMinRL_Object = MibTableColumn
gnOduMonDayDiversityXMinRL = _GnOduMonDayDiversityXMinRL_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 6, 6, 1, 3),
    _GnOduMonDayDiversityXMinRL_Type()
)
gnOduMonDayDiversityXMinRL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonDayDiversityXMinRL.setStatus("mandatory")
_GnOduMonDayDiversityXMaxRL_Type = Integer32
_GnOduMonDayDiversityXMaxRL_Object = MibTableColumn
gnOduMonDayDiversityXMaxRL = _GnOduMonDayDiversityXMaxRL_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 6, 6, 1, 4),
    _GnOduMonDayDiversityXMaxRL_Type()
)
gnOduMonDayDiversityXMaxRL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonDayDiversityXMaxRL.setStatus("mandatory")
_GnOduMonDayDiversityXRLThresh1Exceed_Type = Counter32
_GnOduMonDayDiversityXRLThresh1Exceed_Object = MibTableColumn
gnOduMonDayDiversityXRLThresh1Exceed = _GnOduMonDayDiversityXRLThresh1Exceed_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 6, 6, 1, 5),
    _GnOduMonDayDiversityXRLThresh1Exceed_Type()
)
gnOduMonDayDiversityXRLThresh1Exceed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonDayDiversityXRLThresh1Exceed.setStatus("mandatory")
_GnOduMonDayDiversityXRLThresh2Exceed_Type = Counter32
_GnOduMonDayDiversityXRLThresh2Exceed_Object = MibTableColumn
gnOduMonDayDiversityXRLThresh2Exceed = _GnOduMonDayDiversityXRLThresh2Exceed_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 6, 6, 1, 6),
    _GnOduMonDayDiversityXRLThresh2Exceed_Type()
)
gnOduMonDayDiversityXRLThresh2Exceed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonDayDiversityXRLThresh2Exceed.setStatus("mandatory")
_GnOduMonCurrCombinedXTable_Object = MibTable
gnOduMonCurrCombinedXTable = _GnOduMonCurrCombinedXTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 6, 7)
)
if mibBuilder.loadTexts:
    gnOduMonCurrCombinedXTable.setStatus("mandatory")
_GnOduMonCurrCombinedXEntry_Object = MibTableRow
gnOduMonCurrCombinedXEntry = _GnOduMonCurrCombinedXEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 6, 7, 1)
)
gnOduMonCurrCombinedXEntry.setIndexNames(
    (0, "CERAGON-MIB", "gnOduMonCurrCombinedXId"),
)
if mibBuilder.loadTexts:
    gnOduMonCurrCombinedXEntry.setStatus("mandatory")


class _GnOduMonCurrCombinedXId_Type(Integer32):
    """Custom type gnOduMonCurrCombinedXId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("drawer1", 3),
          ("drawer2", 4))
    )


_GnOduMonCurrCombinedXId_Type.__name__ = "Integer32"
_GnOduMonCurrCombinedXId_Object = MibTableColumn
gnOduMonCurrCombinedXId = _GnOduMonCurrCombinedXId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 6, 7, 1, 1),
    _GnOduMonCurrCombinedXId_Type()
)
gnOduMonCurrCombinedXId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonCurrCombinedXId.setStatus("mandatory")
_GnOduMonCurrCombinedXMinRL_Type = Integer32
_GnOduMonCurrCombinedXMinRL_Object = MibTableColumn
gnOduMonCurrCombinedXMinRL = _GnOduMonCurrCombinedXMinRL_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 6, 7, 1, 2),
    _GnOduMonCurrCombinedXMinRL_Type()
)
gnOduMonCurrCombinedXMinRL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonCurrCombinedXMinRL.setStatus("mandatory")
_GnOduMonCurrCombinedXMaxRL_Type = Integer32
_GnOduMonCurrCombinedXMaxRL_Object = MibTableColumn
gnOduMonCurrCombinedXMaxRL = _GnOduMonCurrCombinedXMaxRL_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 6, 7, 1, 3),
    _GnOduMonCurrCombinedXMaxRL_Type()
)
gnOduMonCurrCombinedXMaxRL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonCurrCombinedXMaxRL.setStatus("mandatory")
_GnOduMonCurrCombinedXRLThresh1Exceed_Type = Counter32
_GnOduMonCurrCombinedXRLThresh1Exceed_Object = MibTableColumn
gnOduMonCurrCombinedXRLThresh1Exceed = _GnOduMonCurrCombinedXRLThresh1Exceed_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 6, 7, 1, 4),
    _GnOduMonCurrCombinedXRLThresh1Exceed_Type()
)
gnOduMonCurrCombinedXRLThresh1Exceed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonCurrCombinedXRLThresh1Exceed.setStatus("mandatory")
_GnOduMonCurrCombinedXRLThresh2Exceed_Type = Counter32
_GnOduMonCurrCombinedXRLThresh2Exceed_Object = MibTableColumn
gnOduMonCurrCombinedXRLThresh2Exceed = _GnOduMonCurrCombinedXRLThresh2Exceed_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 6, 7, 1, 5),
    _GnOduMonCurrCombinedXRLThresh2Exceed_Type()
)
gnOduMonCurrCombinedXRLThresh2Exceed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonCurrCombinedXRLThresh2Exceed.setStatus("mandatory")
_GnOduMonCurrCombinedXDayMinRL_Type = Integer32
_GnOduMonCurrCombinedXDayMinRL_Object = MibTableColumn
gnOduMonCurrCombinedXDayMinRL = _GnOduMonCurrCombinedXDayMinRL_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 6, 7, 1, 6),
    _GnOduMonCurrCombinedXDayMinRL_Type()
)
gnOduMonCurrCombinedXDayMinRL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonCurrCombinedXDayMinRL.setStatus("mandatory")
_GnOduMonCurrCombinedXDayMaxRL_Type = Integer32
_GnOduMonCurrCombinedXDayMaxRL_Object = MibTableColumn
gnOduMonCurrCombinedXDayMaxRL = _GnOduMonCurrCombinedXDayMaxRL_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 6, 7, 1, 7),
    _GnOduMonCurrCombinedXDayMaxRL_Type()
)
gnOduMonCurrCombinedXDayMaxRL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonCurrCombinedXDayMaxRL.setStatus("mandatory")
_GnOduMonCurrCombinedXDayRLThresh1Exceed_Type = Integer32
_GnOduMonCurrCombinedXDayRLThresh1Exceed_Object = MibTableColumn
gnOduMonCurrCombinedXDayRLThresh1Exceed = _GnOduMonCurrCombinedXDayRLThresh1Exceed_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 6, 7, 1, 8),
    _GnOduMonCurrCombinedXDayRLThresh1Exceed_Type()
)
gnOduMonCurrCombinedXDayRLThresh1Exceed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonCurrCombinedXDayRLThresh1Exceed.setStatus("mandatory")
_GnOduMonCurrCombinedXDayRLThresh2Exceed_Type = Integer32
_GnOduMonCurrCombinedXDayRLThresh2Exceed_Object = MibTableColumn
gnOduMonCurrCombinedXDayRLThresh2Exceed = _GnOduMonCurrCombinedXDayRLThresh2Exceed_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 6, 7, 1, 9),
    _GnOduMonCurrCombinedXDayRLThresh2Exceed_Type()
)
gnOduMonCurrCombinedXDayRLThresh2Exceed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonCurrCombinedXDayRLThresh2Exceed.setStatus("mandatory")
_GnOduMonIntervalCombinedXTable_Object = MibTable
gnOduMonIntervalCombinedXTable = _GnOduMonIntervalCombinedXTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 6, 8)
)
if mibBuilder.loadTexts:
    gnOduMonIntervalCombinedXTable.setStatus("mandatory")
_GnOduMonIntervalCombinedXEntry_Object = MibTableRow
gnOduMonIntervalCombinedXEntry = _GnOduMonIntervalCombinedXEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 6, 8, 1)
)
gnOduMonIntervalCombinedXEntry.setIndexNames(
    (0, "CERAGON-MIB", "gnOduMonIntervalCombinedXId"),
    (0, "CERAGON-MIB", "gnOduMonIntervalCombinedXIdx"),
)
if mibBuilder.loadTexts:
    gnOduMonIntervalCombinedXEntry.setStatus("mandatory")


class _GnOduMonIntervalCombinedXId_Type(Integer32):
    """Custom type gnOduMonIntervalCombinedXId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("drawer1", 3),
          ("drawer2", 4))
    )


_GnOduMonIntervalCombinedXId_Type.__name__ = "Integer32"
_GnOduMonIntervalCombinedXId_Object = MibTableColumn
gnOduMonIntervalCombinedXId = _GnOduMonIntervalCombinedXId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 6, 8, 1, 1),
    _GnOduMonIntervalCombinedXId_Type()
)
gnOduMonIntervalCombinedXId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonIntervalCombinedXId.setStatus("mandatory")


class _GnOduMonIntervalCombinedXIdx_Type(Integer32):
    """Custom type gnOduMonIntervalCombinedXIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_GnOduMonIntervalCombinedXIdx_Type.__name__ = "Integer32"
_GnOduMonIntervalCombinedXIdx_Object = MibTableColumn
gnOduMonIntervalCombinedXIdx = _GnOduMonIntervalCombinedXIdx_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 6, 8, 1, 2),
    _GnOduMonIntervalCombinedXIdx_Type()
)
gnOduMonIntervalCombinedXIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonIntervalCombinedXIdx.setStatus("mandatory")
_GnOduMonIntervalCombinedXMinRL_Type = Integer32
_GnOduMonIntervalCombinedXMinRL_Object = MibTableColumn
gnOduMonIntervalCombinedXMinRL = _GnOduMonIntervalCombinedXMinRL_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 6, 8, 1, 3),
    _GnOduMonIntervalCombinedXMinRL_Type()
)
gnOduMonIntervalCombinedXMinRL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonIntervalCombinedXMinRL.setStatus("mandatory")
_GnOduMonIntervalCombinedXMaxRL_Type = Integer32
_GnOduMonIntervalCombinedXMaxRL_Object = MibTableColumn
gnOduMonIntervalCombinedXMaxRL = _GnOduMonIntervalCombinedXMaxRL_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 6, 8, 1, 4),
    _GnOduMonIntervalCombinedXMaxRL_Type()
)
gnOduMonIntervalCombinedXMaxRL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonIntervalCombinedXMaxRL.setStatus("mandatory")
_GnOduMonIntervalCombinedXRLThresh1Exceed_Type = Counter32
_GnOduMonIntervalCombinedXRLThresh1Exceed_Object = MibTableColumn
gnOduMonIntervalCombinedXRLThresh1Exceed = _GnOduMonIntervalCombinedXRLThresh1Exceed_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 6, 8, 1, 5),
    _GnOduMonIntervalCombinedXRLThresh1Exceed_Type()
)
gnOduMonIntervalCombinedXRLThresh1Exceed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonIntervalCombinedXRLThresh1Exceed.setStatus("mandatory")
_GnOduMonIntervalCombinedXRLThresh2Exceed_Type = Counter32
_GnOduMonIntervalCombinedXRLThresh2Exceed_Object = MibTableColumn
gnOduMonIntervalCombinedXRLThresh2Exceed = _GnOduMonIntervalCombinedXRLThresh2Exceed_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 6, 8, 1, 6),
    _GnOduMonIntervalCombinedXRLThresh2Exceed_Type()
)
gnOduMonIntervalCombinedXRLThresh2Exceed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonIntervalCombinedXRLThresh2Exceed.setStatus("mandatory")
_GnOduMonDayCombinedXTable_Object = MibTable
gnOduMonDayCombinedXTable = _GnOduMonDayCombinedXTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 6, 9)
)
if mibBuilder.loadTexts:
    gnOduMonDayCombinedXTable.setStatus("mandatory")
_GnOduMonDayCombinedXEntry_Object = MibTableRow
gnOduMonDayCombinedXEntry = _GnOduMonDayCombinedXEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 6, 9, 1)
)
gnOduMonDayCombinedXEntry.setIndexNames(
    (0, "CERAGON-MIB", "gnOduMonDayCombinedXId"),
    (0, "CERAGON-MIB", "gnOduMonDayCombinedXIdx"),
)
if mibBuilder.loadTexts:
    gnOduMonDayCombinedXEntry.setStatus("mandatory")


class _GnOduMonDayCombinedXId_Type(Integer32):
    """Custom type gnOduMonDayCombinedXId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("drawer1", 3),
          ("drawer2", 4))
    )


_GnOduMonDayCombinedXId_Type.__name__ = "Integer32"
_GnOduMonDayCombinedXId_Object = MibTableColumn
gnOduMonDayCombinedXId = _GnOduMonDayCombinedXId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 6, 9, 1, 1),
    _GnOduMonDayCombinedXId_Type()
)
gnOduMonDayCombinedXId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonDayCombinedXId.setStatus("mandatory")


class _GnOduMonDayCombinedXIdx_Type(Integer32):
    """Custom type gnOduMonDayCombinedXIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_GnOduMonDayCombinedXIdx_Type.__name__ = "Integer32"
_GnOduMonDayCombinedXIdx_Object = MibTableColumn
gnOduMonDayCombinedXIdx = _GnOduMonDayCombinedXIdx_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 6, 9, 1, 2),
    _GnOduMonDayCombinedXIdx_Type()
)
gnOduMonDayCombinedXIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonDayCombinedXIdx.setStatus("mandatory")
_GnOduMonDayCombinedXMinRL_Type = Integer32
_GnOduMonDayCombinedXMinRL_Object = MibTableColumn
gnOduMonDayCombinedXMinRL = _GnOduMonDayCombinedXMinRL_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 6, 9, 1, 3),
    _GnOduMonDayCombinedXMinRL_Type()
)
gnOduMonDayCombinedXMinRL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonDayCombinedXMinRL.setStatus("mandatory")
_GnOduMonDayCombinedXMaxRL_Type = Integer32
_GnOduMonDayCombinedXMaxRL_Object = MibTableColumn
gnOduMonDayCombinedXMaxRL = _GnOduMonDayCombinedXMaxRL_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 6, 9, 1, 4),
    _GnOduMonDayCombinedXMaxRL_Type()
)
gnOduMonDayCombinedXMaxRL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonDayCombinedXMaxRL.setStatus("mandatory")
_GnOduMonDayCombinedXRLThresh1Exceed_Type = Counter32
_GnOduMonDayCombinedXRLThresh1Exceed_Object = MibTableColumn
gnOduMonDayCombinedXRLThresh1Exceed = _GnOduMonDayCombinedXRLThresh1Exceed_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 6, 9, 1, 5),
    _GnOduMonDayCombinedXRLThresh1Exceed_Type()
)
gnOduMonDayCombinedXRLThresh1Exceed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonDayCombinedXRLThresh1Exceed.setStatus("mandatory")
_GnOduMonDayCombinedXRLThresh2Exceed_Type = Counter32
_GnOduMonDayCombinedXRLThresh2Exceed_Object = MibTableColumn
gnOduMonDayCombinedXRLThresh2Exceed = _GnOduMonDayCombinedXRLThresh2Exceed_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 1, 6, 9, 1, 6),
    _GnOduMonDayCombinedXRLThresh2Exceed_Type()
)
gnOduMonDayCombinedXRLThresh2Exceed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnOduMonDayCombinedXRLThresh2Exceed.setStatus("mandatory")
_GnIDU_ObjectIdentity = ObjectIdentity
gnIDU = _GnIDU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2)
)
_GnMdm_ObjectIdentity = ObjectIdentity
gnMdm = _GnMdm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 1)
)
_GnMdmStatTable_Object = MibTable
gnMdmStatTable = _GnMdmStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 1, 2)
)
if mibBuilder.loadTexts:
    gnMdmStatTable.setStatus("mandatory")
_GnMdmStatEntry_Object = MibTableRow
gnMdmStatEntry = _GnMdmStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 1, 2, 1)
)
gnMdmStatEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    gnMdmStatEntry.setStatus("mandatory")


class _GnMdmModStatus_Type(Integer32):
    """Custom type gnMdmModStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("modulatorFault", 3),
          ("ok", 2))
    )


_GnMdmModStatus_Type.__name__ = "Integer32"
_GnMdmModStatus_Object = MibTableColumn
gnMdmModStatus = _GnMdmModStatus_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 1, 2, 1, 1),
    _GnMdmModStatus_Type()
)
gnMdmModStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnMdmModStatus.setStatus("mandatory")
_GnMdmDemodStatus_Type = Integer32
_GnMdmDemodStatus_Object = MibTableColumn
gnMdmDemodStatus = _GnMdmDemodStatus_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 1, 2, 1, 2),
    _GnMdmDemodStatus_Type()
)
gnMdmDemodStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnMdmDemodStatus.setStatus("mandatory")
_GnMdmDefectBlocks_Type = Integer32
_GnMdmDefectBlocks_Object = MibTableColumn
gnMdmDefectBlocks = _GnMdmDefectBlocks_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 1, 2, 1, 3),
    _GnMdmDefectBlocks_Type()
)
gnMdmDefectBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnMdmDefectBlocks.setStatus("mandatory")
_GnMdmBytesCorrected_Type = Integer32
_GnMdmBytesCorrected_Object = MibTableColumn
gnMdmBytesCorrected = _GnMdmBytesCorrected_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 1, 2, 1, 4),
    _GnMdmBytesCorrected_Type()
)
gnMdmBytesCorrected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnMdmBytesCorrected.setStatus("mandatory")


class _GnMdmClearBC_Type(Integer32):
    """Custom type gnMdmClearBC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clear", 3),
          ("noAction", 2))
    )


_GnMdmClearBC_Type.__name__ = "Integer32"
_GnMdmClearBC_Object = MibTableColumn
gnMdmClearBC = _GnMdmClearBC_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 1, 2, 1, 5),
    _GnMdmClearBC_Type()
)
gnMdmClearBC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnMdmClearBC.setStatus("mandatory")
_GnMdmStatXTable_Object = MibTable
gnMdmStatXTable = _GnMdmStatXTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 1, 3)
)
if mibBuilder.loadTexts:
    gnMdmStatXTable.setStatus("mandatory")
_GnMdmStatXEntry_Object = MibTableRow
gnMdmStatXEntry = _GnMdmStatXEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 1, 3, 1)
)
gnMdmStatXEntry.setIndexNames(
    (0, "CERAGON-MIB", "gnMdmStatXId"),
)
if mibBuilder.loadTexts:
    gnMdmStatXEntry.setStatus("mandatory")


class _GnMdmStatXId_Type(Integer32):
    """Custom type gnMdmStatXId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("modem1", 3),
          ("modem2", 4))
    )


_GnMdmStatXId_Type.__name__ = "Integer32"
_GnMdmStatXId_Object = MibTableColumn
gnMdmStatXId = _GnMdmStatXId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 1, 3, 1, 1),
    _GnMdmStatXId_Type()
)
gnMdmStatXId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnMdmStatXId.setStatus("mandatory")


class _GnMdmStatXStandardOrg_Type(Integer32):
    """Custom type gnMdmStatXStandardOrg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("australia", 7),
          ("cmds", 6),
          ("etsi", 2),
          ("fcc", 3),
          ("japan", 4),
          ("lmds", 5),
          ("other", 8))
    )


_GnMdmStatXStandardOrg_Type.__name__ = "Integer32"
_GnMdmStatXStandardOrg_Object = MibTableColumn
gnMdmStatXStandardOrg = _GnMdmStatXStandardOrg_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 1, 3, 1, 2),
    _GnMdmStatXStandardOrg_Type()
)
gnMdmStatXStandardOrg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnMdmStatXStandardOrg.setStatus("mandatory")


class _GnMdmStatXRemoteConnection_Type(Integer32):
    """Custom type gnMdmStatXRemoteConnection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("connected", 2),
          ("disconnected", 3))
    )


_GnMdmStatXRemoteConnection_Type.__name__ = "Integer32"
_GnMdmStatXRemoteConnection_Object = MibTableColumn
gnMdmStatXRemoteConnection = _GnMdmStatXRemoteConnection_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 1, 3, 1, 3),
    _GnMdmStatXRemoteConnection_Type()
)
gnMdmStatXRemoteConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnMdmStatXRemoteConnection.setStatus("mandatory")


class _GnMdmStatXModemType_Type(Integer32):
    """Custom type gnMdmStatXModemType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_GnMdmStatXModemType_Type.__name__ = "Integer32"
_GnMdmStatXModemType_Object = MibTableColumn
gnMdmStatXModemType = _GnMdmStatXModemType_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 1, 3, 1, 4),
    _GnMdmStatXModemType_Type()
)
gnMdmStatXModemType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnMdmStatXModemType.setStatus("mandatory")


class _GnMdmStatXModemWorkTime_Type(Integer32):
    """Custom type gnMdmStatXModemWorkTime based on Integer32"""
    defaultValue = 0


_GnMdmStatXModemWorkTime_Object = MibTableColumn
gnMdmStatXModemWorkTime = _GnMdmStatXModemWorkTime_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 1, 3, 1, 5),
    _GnMdmStatXModemWorkTime_Type()
)
gnMdmStatXModemWorkTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnMdmStatXModemWorkTime.setStatus("mandatory")


class _GnMdmStatXModemSerialNumber_Type(DisplayString):
    """Custom type gnMdmStatXModemSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_GnMdmStatXModemSerialNumber_Type.__name__ = "DisplayString"
_GnMdmStatXModemSerialNumber_Object = MibTableColumn
gnMdmStatXModemSerialNumber = _GnMdmStatXModemSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 1, 3, 1, 6),
    _GnMdmStatXModemSerialNumber_Type()
)
gnMdmStatXModemSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnMdmStatXModemSerialNumber.setStatus("mandatory")


class _GnMdmStatXModemFWVer_Type(DisplayString):
    """Custom type gnMdmStatXModemFWVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_GnMdmStatXModemFWVer_Type.__name__ = "DisplayString"
_GnMdmStatXModemFWVer_Object = MibTableColumn
gnMdmStatXModemFWVer = _GnMdmStatXModemFWVer_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 1, 3, 1, 7),
    _GnMdmStatXModemFWVer_Type()
)
gnMdmStatXModemFWVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnMdmStatXModemFWVer.setStatus("mandatory")


class _GnMdmStatXModemFWPostVer_Type(DisplayString):
    """Custom type gnMdmStatXModemFWPostVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_GnMdmStatXModemFWPostVer_Type.__name__ = "DisplayString"
_GnMdmStatXModemFWPostVer_Object = MibTableColumn
gnMdmStatXModemFWPostVer = _GnMdmStatXModemFWPostVer_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 1, 3, 1, 8),
    _GnMdmStatXModemFWPostVer_Type()
)
gnMdmStatXModemFWPostVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnMdmStatXModemFWPostVer.setStatus("mandatory")


class _GnMdmStatXModemScriptVer_Type(DisplayString):
    """Custom type gnMdmStatXModemScriptVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_GnMdmStatXModemScriptVer_Type.__name__ = "DisplayString"
_GnMdmStatXModemScriptVer_Object = MibTableColumn
gnMdmStatXModemScriptVer = _GnMdmStatXModemScriptVer_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 1, 3, 1, 9),
    _GnMdmStatXModemScriptVer_Type()
)
gnMdmStatXModemScriptVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnMdmStatXModemScriptVer.setStatus("mandatory")


class _GnMdmStatXModemScriptPostVer_Type(DisplayString):
    """Custom type gnMdmStatXModemScriptPostVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_GnMdmStatXModemScriptPostVer_Type.__name__ = "DisplayString"
_GnMdmStatXModemScriptPostVer_Object = MibTableColumn
gnMdmStatXModemScriptPostVer = _GnMdmStatXModemScriptPostVer_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 1, 3, 1, 10),
    _GnMdmStatXModemScriptPostVer_Type()
)
gnMdmStatXModemScriptPostVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnMdmStatXModemScriptPostVer.setStatus("mandatory")


class _GnMdmStatXIfLoopbackTimeOut_Type(Integer32):
    """Custom type gnMdmStatXIfLoopbackTimeOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_GnMdmStatXIfLoopbackTimeOut_Type.__name__ = "Integer32"
_GnMdmStatXIfLoopbackTimeOut_Object = MibTableColumn
gnMdmStatXIfLoopbackTimeOut = _GnMdmStatXIfLoopbackTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 1, 3, 1, 11),
    _GnMdmStatXIfLoopbackTimeOut_Type()
)
gnMdmStatXIfLoopbackTimeOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnMdmStatXIfLoopbackTimeOut.setStatus("mandatory")


class _GnMdmStatXBoardType_Type(Integer32):
    """Custom type gnMdmStatXBoardType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("v1", 2),
          ("v2", 3),
          ("v3", 4))
    )


_GnMdmStatXBoardType_Type.__name__ = "Integer32"
_GnMdmStatXBoardType_Object = MibTableColumn
gnMdmStatXBoardType = _GnMdmStatXBoardType_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 1, 3, 1, 12),
    _GnMdmStatXBoardType_Type()
)
gnMdmStatXBoardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnMdmStatXBoardType.setStatus("mandatory")
_GnMdmStatXDefectedBlocks_Type = Integer32
_GnMdmStatXDefectedBlocks_Object = MibTableColumn
gnMdmStatXDefectedBlocks = _GnMdmStatXDefectedBlocks_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 1, 3, 1, 13),
    _GnMdmStatXDefectedBlocks_Type()
)
gnMdmStatXDefectedBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnMdmStatXDefectedBlocks.setStatus("mandatory")


class _GnMdmStatXScriptType_Type(Integer32):
    """Custom type gnMdmStatXScriptType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("v1", 2),
          ("v2", 3))
    )


_GnMdmStatXScriptType_Type.__name__ = "Integer32"
_GnMdmStatXScriptType_Object = MibTableColumn
gnMdmStatXScriptType = _GnMdmStatXScriptType_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 1, 3, 1, 14),
    _GnMdmStatXScriptType_Type()
)
gnMdmStatXScriptType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnMdmStatXScriptType.setStatus("mandatory")


class _GnMdmStatXAcmValidIntervals_Type(Integer32):
    """Custom type gnMdmStatXAcmValidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_GnMdmStatXAcmValidIntervals_Type.__name__ = "Integer32"
_GnMdmStatXAcmValidIntervals_Object = MibTableColumn
gnMdmStatXAcmValidIntervals = _GnMdmStatXAcmValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 1, 3, 1, 15),
    _GnMdmStatXAcmValidIntervals_Type()
)
gnMdmStatXAcmValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnMdmStatXAcmValidIntervals.setStatus("mandatory")


class _GnMdmStatXAcmSignalValid_Type(Integer32):
    """Custom type gnMdmStatXAcmSignalValid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notValid", 3),
          ("valid", 2))
    )


_GnMdmStatXAcmSignalValid_Type.__name__ = "Integer32"
_GnMdmStatXAcmSignalValid_Object = MibTableColumn
gnMdmStatXAcmSignalValid = _GnMdmStatXAcmSignalValid_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 1, 3, 1, 16),
    _GnMdmStatXAcmSignalValid_Type()
)
gnMdmStatXAcmSignalValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnMdmStatXAcmSignalValid.setStatus("mandatory")


class _GnMdmStatXTxConstellation_Type(Integer32):
    """Custom type gnMdmStatXTxConstellation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_GnMdmStatXTxConstellation_Type.__name__ = "Integer32"
_GnMdmStatXTxConstellation_Object = MibTableColumn
gnMdmStatXTxConstellation = _GnMdmStatXTxConstellation_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 1, 3, 1, 17),
    _GnMdmStatXTxConstellation_Type()
)
gnMdmStatXTxConstellation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnMdmStatXTxConstellation.setStatus("mandatory")


class _GnMdmStatXRxConstellation_Type(Integer32):
    """Custom type gnMdmStatXRxConstellation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_GnMdmStatXRxConstellation_Type.__name__ = "Integer32"
_GnMdmStatXRxConstellation_Object = MibTableColumn
gnMdmStatXRxConstellation = _GnMdmStatXRxConstellation_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 1, 3, 1, 18),
    _GnMdmStatXRxConstellation_Type()
)
gnMdmStatXRxConstellation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnMdmStatXRxConstellation.setStatus("mandatory")
_GnMdmCfgTable_Object = MibTable
gnMdmCfgTable = _GnMdmCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 1, 4)
)
if mibBuilder.loadTexts:
    gnMdmCfgTable.setStatus("mandatory")
_GnMdmCfgEntry_Object = MibTableRow
gnMdmCfgEntry = _GnMdmCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 1, 4, 1)
)
gnMdmCfgEntry.setIndexNames(
    (0, "CERAGON-MIB", "gnMdmCfgId"),
)
if mibBuilder.loadTexts:
    gnMdmCfgEntry.setStatus("mandatory")


class _GnMdmCfgId_Type(Integer32):
    """Custom type gnMdmCfgId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("drawer1", 3),
          ("drawer2", 4))
    )


_GnMdmCfgId_Type.__name__ = "Integer32"
_GnMdmCfgId_Object = MibTableColumn
gnMdmCfgId = _GnMdmCfgId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 1, 4, 1, 1),
    _GnMdmCfgId_Type()
)
gnMdmCfgId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnMdmCfgId.setStatus("mandatory")


class _GnMdmCfgDiversityMode_Type(Integer32):
    """Custom type gnMdmCfgDiversityMode based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("enable", 2))
    )


_GnMdmCfgDiversityMode_Type.__name__ = "Integer32"
_GnMdmCfgDiversityMode_Object = MibTableColumn
gnMdmCfgDiversityMode = _GnMdmCfgDiversityMode_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 1, 4, 1, 2),
    _GnMdmCfgDiversityMode_Type()
)
gnMdmCfgDiversityMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnMdmCfgDiversityMode.setStatus("mandatory")
_GnMdmCfgXTable_Object = MibTable
gnMdmCfgXTable = _GnMdmCfgXTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 1, 5)
)
if mibBuilder.loadTexts:
    gnMdmCfgXTable.setStatus("mandatory")
_GnMdmCfgXEntry_Object = MibTableRow
gnMdmCfgXEntry = _GnMdmCfgXEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 1, 5, 1)
)
gnMdmCfgXEntry.setIndexNames(
    (0, "CERAGON-MIB", "gnMdmCfgXId"),
)
if mibBuilder.loadTexts:
    gnMdmCfgXEntry.setStatus("mandatory")


class _GnMdmCfgXId_Type(Integer32):
    """Custom type gnMdmCfgXId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("modem1", 3),
          ("modem2", 4))
    )


_GnMdmCfgXId_Type.__name__ = "Integer32"
_GnMdmCfgXId_Object = MibTableColumn
gnMdmCfgXId = _GnMdmCfgXId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 1, 5, 1, 1),
    _GnMdmCfgXId_Type()
)
gnMdmCfgXId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnMdmCfgXId.setStatus("mandatory")


class _GnMdmCfgXLatencyType_Type(Integer32):
    """Custom type gnMdmCfgXLatencyType based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("high", 3),
          ("low", 2))
    )


_GnMdmCfgXLatencyType_Type.__name__ = "Integer32"
_GnMdmCfgXLatencyType_Object = MibTableColumn
gnMdmCfgXLatencyType = _GnMdmCfgXLatencyType_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 1, 5, 1, 2),
    _GnMdmCfgXLatencyType_Type()
)
gnMdmCfgXLatencyType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnMdmCfgXLatencyType.setStatus("mandatory")


class _GnMdmCfgXLinkId_Type(Integer32):
    """Custom type gnMdmCfgXLinkId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_GnMdmCfgXLinkId_Type.__name__ = "Integer32"
_GnMdmCfgXLinkId_Object = MibTableColumn
gnMdmCfgXLinkId = _GnMdmCfgXLinkId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 1, 5, 1, 3),
    _GnMdmCfgXLinkId_Type()
)
gnMdmCfgXLinkId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnMdmCfgXLinkId.setStatus("mandatory")


class _GnMdmCfgXRadioSide_Type(Integer32):
    """Custom type gnMdmCfgXRadioSide based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("east", 2),
          ("west", 3))
    )


_GnMdmCfgXRadioSide_Type.__name__ = "Integer32"
_GnMdmCfgXRadioSide_Object = MibTableColumn
gnMdmCfgXRadioSide = _GnMdmCfgXRadioSide_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 1, 5, 1, 4),
    _GnMdmCfgXRadioSide_Type()
)
gnMdmCfgXRadioSide.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnMdmCfgXRadioSide.setStatus("mandatory")


class _GnMdmCfgXMrmcConf_Type(Integer32):
    """Custom type gnMdmCfgXMrmcConf based on Integer32"""
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
              18,
              24,
              25,
              26)
        )
    )
    namedValues = NamedValues(
        *(("acm28", 26),
          ("acm50", 25),
          ("acm56", 24),
          ("mrmc1125", 10),
          ("mrmc1228", 5),
          ("mrmc1340", 13),
          ("mrmc1528", 1),
          ("mrmc1540", 6),
          ("mrmc1550", 2),
          ("mrmc2030", 12),
          ("mrmc2050", 11),
          ("mrmc3150", 4),
          ("mrmc3156", 3),
          ("mrmc3756", 18),
          ("mrmc4410", 7),
          ("mrmc4420", 8),
          ("mrmc4440", 9))
    )


_GnMdmCfgXMrmcConf_Type.__name__ = "Integer32"
_GnMdmCfgXMrmcConf_Object = MibTableColumn
gnMdmCfgXMrmcConf = _GnMdmCfgXMrmcConf_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 1, 5, 1, 5),
    _GnMdmCfgXMrmcConf_Type()
)
gnMdmCfgXMrmcConf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnMdmCfgXMrmcConf.setStatus("mandatory")


class _GnMdmCfgXIfLoopback_Type(Integer32):
    """Custom type gnMdmCfgXIfLoopback based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 3),
          ("none", 2))
    )


_GnMdmCfgXIfLoopback_Type.__name__ = "Integer32"
_GnMdmCfgXIfLoopback_Object = MibTableColumn
gnMdmCfgXIfLoopback = _GnMdmCfgXIfLoopback_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 1, 5, 1, 6),
    _GnMdmCfgXIfLoopback_Type()
)
gnMdmCfgXIfLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnMdmCfgXIfLoopback.setStatus("mandatory")


class _GnMdmCfgXHwReset_Type(Integer32):
    """Custom type gnMdmCfgXHwReset based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hwReset", 3),
          ("noOperation", 2))
    )


_GnMdmCfgXHwReset_Type.__name__ = "Integer32"
_GnMdmCfgXHwReset_Object = MibTableColumn
gnMdmCfgXHwReset = _GnMdmCfgXHwReset_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 1, 5, 1, 7),
    _GnMdmCfgXHwReset_Type()
)
gnMdmCfgXHwReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnMdmCfgXHwReset.setStatus("mandatory")


class _GnMdmCfgXPrbsTest_Type(Integer32):
    """Custom type gnMdmCfgXPrbsTest based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 3),
          ("notActive", 2))
    )


_GnMdmCfgXPrbsTest_Type.__name__ = "Integer32"
_GnMdmCfgXPrbsTest_Object = MibTableColumn
gnMdmCfgXPrbsTest = _GnMdmCfgXPrbsTest_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 1, 5, 1, 8),
    _GnMdmCfgXPrbsTest_Type()
)
gnMdmCfgXPrbsTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnMdmCfgXPrbsTest.setStatus("mandatory")


class _GnMdmCfgXClearCounters_Type(Integer32):
    """Custom type gnMdmCfgXClearCounters based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clearCounters", 3),
          ("noAction", 2))
    )


_GnMdmCfgXClearCounters_Type.__name__ = "Integer32"
_GnMdmCfgXClearCounters_Object = MibTableColumn
gnMdmCfgXClearCounters = _GnMdmCfgXClearCounters_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 1, 5, 1, 9),
    _GnMdmCfgXClearCounters_Type()
)
gnMdmCfgXClearCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnMdmCfgXClearCounters.setStatus("mandatory")


class _GnMdmCfgXAcmOperationMode_Type(Integer32):
    """Custom type gnMdmCfgXAcmOperationMode based on Integer32"""
    defaultValue = 2

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
        *(("acm128QAM", 7),
          ("acm16QAM", 4),
          ("acm256QAM", 8),
          ("acm32QAM", 5),
          ("acm4QAM", 2),
          ("acm64QAM", 6),
          ("acm8QAM", 3),
          ("adaptive", 1))
    )


_GnMdmCfgXAcmOperationMode_Type.__name__ = "Integer32"
_GnMdmCfgXAcmOperationMode_Object = MibTableColumn
gnMdmCfgXAcmOperationMode = _GnMdmCfgXAcmOperationMode_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 1, 5, 1, 10),
    _GnMdmCfgXAcmOperationMode_Type()
)
gnMdmCfgXAcmOperationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnMdmCfgXAcmOperationMode.setStatus("mandatory")


class _GnMdmCfgXAcmMaximumConstellation_Type(Integer32):
    """Custom type gnMdmCfgXAcmMaximumConstellation based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("acm128QAM", 7),
          ("acm16QAM", 4),
          ("acm256QAM", 8),
          ("acm32QAM", 5),
          ("acm4QAM", 2),
          ("acm64QAM", 6),
          ("acm8QAM", 3))
    )


_GnMdmCfgXAcmMaximumConstellation_Type.__name__ = "Integer32"
_GnMdmCfgXAcmMaximumConstellation_Object = MibTableColumn
gnMdmCfgXAcmMaximumConstellation = _GnMdmCfgXAcmMaximumConstellation_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 1, 5, 1, 11),
    _GnMdmCfgXAcmMaximumConstellation_Type()
)
gnMdmCfgXAcmMaximumConstellation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnMdmCfgXAcmMaximumConstellation.setStatus("mandatory")
_GnMdmAcmStatXTable_Object = MibTable
gnMdmAcmStatXTable = _GnMdmAcmStatXTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 1, 6)
)
if mibBuilder.loadTexts:
    gnMdmAcmStatXTable.setStatus("mandatory")
_GnMdmAcmStatXEntry_Object = MibTableRow
gnMdmAcmStatXEntry = _GnMdmAcmStatXEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 1, 6, 1)
)
gnMdmAcmStatXEntry.setIndexNames(
    (0, "CERAGON-MIB", "gnMdmAcmStatXId"),
    (0, "CERAGON-MIB", "gnMdmAcmStatXQamId"),
)
if mibBuilder.loadTexts:
    gnMdmAcmStatXEntry.setStatus("mandatory")


class _GnMdmAcmStatXId_Type(Integer32):
    """Custom type gnMdmAcmStatXId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("modem1", 3),
          ("modem2", 4))
    )


_GnMdmAcmStatXId_Type.__name__ = "Integer32"
_GnMdmAcmStatXId_Object = MibTableColumn
gnMdmAcmStatXId = _GnMdmAcmStatXId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 1, 6, 1, 1),
    _GnMdmAcmStatXId_Type()
)
gnMdmAcmStatXId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnMdmAcmStatXId.setStatus("mandatory")


class _GnMdmAcmStatXQamId_Type(Integer32):
    """Custom type gnMdmAcmStatXQamId based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("acm128QAM", 7),
          ("acm16QAM", 4),
          ("acm256QAM", 8),
          ("acm32QAM", 5),
          ("acm4QAM", 2),
          ("acm64QAM", 6),
          ("acm8QAM", 3))
    )


_GnMdmAcmStatXQamId_Type.__name__ = "Integer32"
_GnMdmAcmStatXQamId_Object = MibTableColumn
gnMdmAcmStatXQamId = _GnMdmAcmStatXQamId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 1, 6, 1, 2),
    _GnMdmAcmStatXQamId_Type()
)
gnMdmAcmStatXQamId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnMdmAcmStatXQamId.setStatus("mandatory")


class _GnMdmAcmStatXRoundedThroughput_Type(Integer32):
    """Custom type gnMdmAcmStatXRoundedThroughput based on Integer32"""
    defaultValue = 155

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_GnMdmAcmStatXRoundedThroughput_Type.__name__ = "Integer32"
_GnMdmAcmStatXRoundedThroughput_Object = MibTableColumn
gnMdmAcmStatXRoundedThroughput = _GnMdmAcmStatXRoundedThroughput_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 1, 6, 1, 3),
    _GnMdmAcmStatXRoundedThroughput_Type()
)
gnMdmAcmStatXRoundedThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnMdmAcmStatXRoundedThroughput.setStatus("mandatory")


class _GnMdmAcmStatXSupportedThroughput_Type(Integer32):
    """Custom type gnMdmAcmStatXSupportedThroughput based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notSupport", 2),
          ("support", 3))
    )


_GnMdmAcmStatXSupportedThroughput_Type.__name__ = "Integer32"
_GnMdmAcmStatXSupportedThroughput_Object = MibTableColumn
gnMdmAcmStatXSupportedThroughput = _GnMdmAcmStatXSupportedThroughput_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 1, 6, 1, 4),
    _GnMdmAcmStatXSupportedThroughput_Type()
)
gnMdmAcmStatXSupportedThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnMdmAcmStatXSupportedThroughput.setStatus("mandatory")
_GnMdmMonitorX_ObjectIdentity = ObjectIdentity
gnMdmMonitorX = _GnMdmMonitorX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 1, 7)
)
_GnMdmAcmMonitorX_ObjectIdentity = ObjectIdentity
gnMdmAcmMonitorX = _GnMdmAcmMonitorX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 1, 7, 1)
)
_GnMdmAcmMonCurrXTable_Object = MibTable
gnMdmAcmMonCurrXTable = _GnMdmAcmMonCurrXTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 1, 7, 1, 1)
)
if mibBuilder.loadTexts:
    gnMdmAcmMonCurrXTable.setStatus("mandatory")
_GnMdmAcmMonCurrXEntry_Object = MibTableRow
gnMdmAcmMonCurrXEntry = _GnMdmAcmMonCurrXEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 1, 7, 1, 1, 1)
)
gnMdmAcmMonCurrXEntry.setIndexNames(
    (0, "CERAGON-MIB", "gnMdmAcmMonCurrXId"),
)
if mibBuilder.loadTexts:
    gnMdmAcmMonCurrXEntry.setStatus("mandatory")


class _GnMdmAcmMonCurrXId_Type(Integer32):
    """Custom type gnMdmAcmMonCurrXId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("modem1", 3),
          ("modem2", 4))
    )


_GnMdmAcmMonCurrXId_Type.__name__ = "Integer32"
_GnMdmAcmMonCurrXId_Object = MibTableColumn
gnMdmAcmMonCurrXId = _GnMdmAcmMonCurrXId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 1, 7, 1, 1, 1, 1),
    _GnMdmAcmMonCurrXId_Type()
)
gnMdmAcmMonCurrXId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnMdmAcmMonCurrXId.setStatus("mandatory")
_GnMdmAcmMonCurrXMinConstellation_Type = Integer32
_GnMdmAcmMonCurrXMinConstellation_Object = MibTableColumn
gnMdmAcmMonCurrXMinConstellation = _GnMdmAcmMonCurrXMinConstellation_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 1, 7, 1, 1, 1, 2),
    _GnMdmAcmMonCurrXMinConstellation_Type()
)
gnMdmAcmMonCurrXMinConstellation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnMdmAcmMonCurrXMinConstellation.setStatus("mandatory")
_GnMdmAcmMonCurrXMaxConstellation_Type = Integer32
_GnMdmAcmMonCurrXMaxConstellation_Object = MibTableColumn
gnMdmAcmMonCurrXMaxConstellation = _GnMdmAcmMonCurrXMaxConstellation_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 1, 7, 1, 1, 1, 3),
    _GnMdmAcmMonCurrXMaxConstellation_Type()
)
gnMdmAcmMonCurrXMaxConstellation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnMdmAcmMonCurrXMaxConstellation.setStatus("mandatory")


class _GnMdmAcmMonCurrXIDF_Type(Integer32):
    """Custom type gnMdmAcmMonCurrXIDF based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3))
    )


_GnMdmAcmMonCurrXIDF_Type.__name__ = "Integer32"
_GnMdmAcmMonCurrXIDF_Object = MibTableColumn
gnMdmAcmMonCurrXIDF = _GnMdmAcmMonCurrXIDF_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 1, 7, 1, 1, 1, 4),
    _GnMdmAcmMonCurrXIDF_Type()
)
gnMdmAcmMonCurrXIDF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnMdmAcmMonCurrXIDF.setStatus("mandatory")
_GnMdmAcmMonCurrXDayMinConstellation_Type = Integer32
_GnMdmAcmMonCurrXDayMinConstellation_Object = MibTableColumn
gnMdmAcmMonCurrXDayMinConstellation = _GnMdmAcmMonCurrXDayMinConstellation_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 1, 7, 1, 1, 1, 5),
    _GnMdmAcmMonCurrXDayMinConstellation_Type()
)
gnMdmAcmMonCurrXDayMinConstellation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnMdmAcmMonCurrXDayMinConstellation.setStatus("mandatory")
_GnMdmAcmMonCurrXDayMaxConstellation_Type = Integer32
_GnMdmAcmMonCurrXDayMaxConstellation_Object = MibTableColumn
gnMdmAcmMonCurrXDayMaxConstellation = _GnMdmAcmMonCurrXDayMaxConstellation_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 1, 7, 1, 1, 1, 6),
    _GnMdmAcmMonCurrXDayMaxConstellation_Type()
)
gnMdmAcmMonCurrXDayMaxConstellation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnMdmAcmMonCurrXDayMaxConstellation.setStatus("mandatory")


class _GnMdmAcmMonCurrXDayIDF_Type(Integer32):
    """Custom type gnMdmAcmMonCurrXDayIDF based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3))
    )


_GnMdmAcmMonCurrXDayIDF_Type.__name__ = "Integer32"
_GnMdmAcmMonCurrXDayIDF_Object = MibTableColumn
gnMdmAcmMonCurrXDayIDF = _GnMdmAcmMonCurrXDayIDF_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 1, 7, 1, 1, 1, 7),
    _GnMdmAcmMonCurrXDayIDF_Type()
)
gnMdmAcmMonCurrXDayIDF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnMdmAcmMonCurrXDayIDF.setStatus("mandatory")
_GnMdmAcmMonIntervalXTable_Object = MibTable
gnMdmAcmMonIntervalXTable = _GnMdmAcmMonIntervalXTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 1, 7, 1, 2)
)
if mibBuilder.loadTexts:
    gnMdmAcmMonIntervalXTable.setStatus("mandatory")
_GnMdmAcmMonIntervalXEntry_Object = MibTableRow
gnMdmAcmMonIntervalXEntry = _GnMdmAcmMonIntervalXEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 1, 7, 1, 2, 1)
)
gnMdmAcmMonIntervalXEntry.setIndexNames(
    (0, "CERAGON-MIB", "gnMdmAcmMonIntervalXId"),
    (0, "CERAGON-MIB", "gnMdmAcmMonIntervalXIdx"),
)
if mibBuilder.loadTexts:
    gnMdmAcmMonIntervalXEntry.setStatus("mandatory")


class _GnMdmAcmMonIntervalXId_Type(Integer32):
    """Custom type gnMdmAcmMonIntervalXId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("modem1", 3),
          ("modem2", 4))
    )


_GnMdmAcmMonIntervalXId_Type.__name__ = "Integer32"
_GnMdmAcmMonIntervalXId_Object = MibTableColumn
gnMdmAcmMonIntervalXId = _GnMdmAcmMonIntervalXId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 1, 7, 1, 2, 1, 1),
    _GnMdmAcmMonIntervalXId_Type()
)
gnMdmAcmMonIntervalXId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnMdmAcmMonIntervalXId.setStatus("mandatory")


class _GnMdmAcmMonIntervalXIdx_Type(Integer32):
    """Custom type gnMdmAcmMonIntervalXIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_GnMdmAcmMonIntervalXIdx_Type.__name__ = "Integer32"
_GnMdmAcmMonIntervalXIdx_Object = MibTableColumn
gnMdmAcmMonIntervalXIdx = _GnMdmAcmMonIntervalXIdx_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 1, 7, 1, 2, 1, 2),
    _GnMdmAcmMonIntervalXIdx_Type()
)
gnMdmAcmMonIntervalXIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnMdmAcmMonIntervalXIdx.setStatus("mandatory")
_GnMdmAcmMonIntervalXMinConstellation_Type = Integer32
_GnMdmAcmMonIntervalXMinConstellation_Object = MibTableColumn
gnMdmAcmMonIntervalXMinConstellation = _GnMdmAcmMonIntervalXMinConstellation_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 1, 7, 1, 2, 1, 3),
    _GnMdmAcmMonIntervalXMinConstellation_Type()
)
gnMdmAcmMonIntervalXMinConstellation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnMdmAcmMonIntervalXMinConstellation.setStatus("mandatory")
_GnMdmAcmMonIntervalXMaxConstellation_Type = Integer32
_GnMdmAcmMonIntervalXMaxConstellation_Object = MibTableColumn
gnMdmAcmMonIntervalXMaxConstellation = _GnMdmAcmMonIntervalXMaxConstellation_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 1, 7, 1, 2, 1, 4),
    _GnMdmAcmMonIntervalXMaxConstellation_Type()
)
gnMdmAcmMonIntervalXMaxConstellation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnMdmAcmMonIntervalXMaxConstellation.setStatus("mandatory")


class _GnMdmAcmMonIntervalXIDF_Type(Integer32):
    """Custom type gnMdmAcmMonIntervalXIDF based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3))
    )


_GnMdmAcmMonIntervalXIDF_Type.__name__ = "Integer32"
_GnMdmAcmMonIntervalXIDF_Object = MibTableColumn
gnMdmAcmMonIntervalXIDF = _GnMdmAcmMonIntervalXIDF_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 1, 7, 1, 2, 1, 5),
    _GnMdmAcmMonIntervalXIDF_Type()
)
gnMdmAcmMonIntervalXIDF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnMdmAcmMonIntervalXIDF.setStatus("mandatory")
_GnMdmAcmMonDayXTable_Object = MibTable
gnMdmAcmMonDayXTable = _GnMdmAcmMonDayXTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 1, 7, 1, 3)
)
if mibBuilder.loadTexts:
    gnMdmAcmMonDayXTable.setStatus("mandatory")
_GnMdmAcmMonDayXEntry_Object = MibTableRow
gnMdmAcmMonDayXEntry = _GnMdmAcmMonDayXEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 1, 7, 1, 3, 1)
)
gnMdmAcmMonDayXEntry.setIndexNames(
    (0, "CERAGON-MIB", "gnMdmAcmMonDayXId"),
    (0, "CERAGON-MIB", "gnMdmAcmMonDayXIdx"),
)
if mibBuilder.loadTexts:
    gnMdmAcmMonDayXEntry.setStatus("mandatory")


class _GnMdmAcmMonDayXId_Type(Integer32):
    """Custom type gnMdmAcmMonDayXId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("modem1", 3),
          ("modem2", 4))
    )


_GnMdmAcmMonDayXId_Type.__name__ = "Integer32"
_GnMdmAcmMonDayXId_Object = MibTableColumn
gnMdmAcmMonDayXId = _GnMdmAcmMonDayXId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 1, 7, 1, 3, 1, 1),
    _GnMdmAcmMonDayXId_Type()
)
gnMdmAcmMonDayXId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnMdmAcmMonDayXId.setStatus("mandatory")


class _GnMdmAcmMonDayXIdx_Type(Integer32):
    """Custom type gnMdmAcmMonDayXIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_GnMdmAcmMonDayXIdx_Type.__name__ = "Integer32"
_GnMdmAcmMonDayXIdx_Object = MibTableColumn
gnMdmAcmMonDayXIdx = _GnMdmAcmMonDayXIdx_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 1, 7, 1, 3, 1, 2),
    _GnMdmAcmMonDayXIdx_Type()
)
gnMdmAcmMonDayXIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnMdmAcmMonDayXIdx.setStatus("mandatory")
_GnMdmAcmMonDayXMinConstellation_Type = Integer32
_GnMdmAcmMonDayXMinConstellation_Object = MibTableColumn
gnMdmAcmMonDayXMinConstellation = _GnMdmAcmMonDayXMinConstellation_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 1, 7, 1, 3, 1, 3),
    _GnMdmAcmMonDayXMinConstellation_Type()
)
gnMdmAcmMonDayXMinConstellation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnMdmAcmMonDayXMinConstellation.setStatus("mandatory")
_GnMdmAcmMonDayXMaxConstellation_Type = Integer32
_GnMdmAcmMonDayXMaxConstellation_Object = MibTableColumn
gnMdmAcmMonDayXMaxConstellation = _GnMdmAcmMonDayXMaxConstellation_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 1, 7, 1, 3, 1, 4),
    _GnMdmAcmMonDayXMaxConstellation_Type()
)
gnMdmAcmMonDayXMaxConstellation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnMdmAcmMonDayXMaxConstellation.setStatus("mandatory")


class _GnMdmAcmMonDayXIDF_Type(Integer32):
    """Custom type gnMdmAcmMonDayXIDF based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3))
    )


_GnMdmAcmMonDayXIDF_Type.__name__ = "Integer32"
_GnMdmAcmMonDayXIDF_Object = MibTableColumn
gnMdmAcmMonDayXIDF = _GnMdmAcmMonDayXIDF_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 1, 7, 1, 3, 1, 5),
    _GnMdmAcmMonDayXIDF_Type()
)
gnMdmAcmMonDayXIDF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnMdmAcmMonDayXIDF.setStatus("mandatory")
_GnSpi_ObjectIdentity = ObjectIdentity
gnSpi = _GnSpi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 2)
)
_GnSpiCfgTable_Object = MibTable
gnSpiCfgTable = _GnSpiCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 2, 1)
)
if mibBuilder.loadTexts:
    gnSpiCfgTable.setStatus("mandatory")
_GnSpiCfgEntry_Object = MibTableRow
gnSpiCfgEntry = _GnSpiCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 2, 1, 1)
)
gnSpiCfgEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    gnSpiCfgEntry.setStatus("mandatory")


class _GnSpiCfgConnector_Type(Integer32):
    """Custom type gnSpiCfgConnector based on Integer32"""
    defaultValue = 2

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
        *(("electrical", 3),
          ("fiber", 2),
          ("nointerface", 1),
          ("stp", 5),
          ("utp", 4))
    )


_GnSpiCfgConnector_Type.__name__ = "Integer32"
_GnSpiCfgConnector_Object = MibTableColumn
gnSpiCfgConnector = _GnSpiCfgConnector_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 2, 1, 1, 1),
    _GnSpiCfgConnector_Type()
)
gnSpiCfgConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnSpiCfgConnector.setStatus("mandatory")
_GnMux_ObjectIdentity = ObjectIdentity
gnMux = _GnMux_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3)
)
_GnRstCfgTable_Object = MibTable
gnRstCfgTable = _GnRstCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 1)
)
if mibBuilder.loadTexts:
    gnRstCfgTable.setStatus("mandatory")
_GnRstCfgEntry_Object = MibTableRow
gnRstCfgEntry = _GnRstCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 1, 1)
)
gnRstCfgEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    gnRstCfgEntry.setStatus("mandatory")


class _GnRstCfgTransmittedJ0_Type(DisplayString):
    """Custom type gnRstCfgTransmittedJ0 based on DisplayString"""
    defaultValue = OctetString("J0 J0 J0 J0 J0 ")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_GnRstCfgTransmittedJ0_Type.__name__ = "DisplayString"
_GnRstCfgTransmittedJ0_Object = MibTableColumn
gnRstCfgTransmittedJ0 = _GnRstCfgTransmittedJ0_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 1, 1, 1),
    _GnRstCfgTransmittedJ0_Type()
)
gnRstCfgTransmittedJ0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnRstCfgTransmittedJ0.setStatus("mandatory")


class _GnRstCfgExpectedJ0_Type(DisplayString):
    """Custom type gnRstCfgExpectedJ0 based on DisplayString"""
    defaultValue = OctetString("J0 J0 J0 J0 J0 ")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_GnRstCfgExpectedJ0_Type.__name__ = "DisplayString"
_GnRstCfgExpectedJ0_Object = MibTableColumn
gnRstCfgExpectedJ0 = _GnRstCfgExpectedJ0_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 1, 1, 2),
    _GnRstCfgExpectedJ0_Type()
)
gnRstCfgExpectedJ0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnRstCfgExpectedJ0.setStatus("mandatory")


class _GnRstCfgTransparencyJ0_Type(Integer32):
    """Custom type gnRstCfgTransparencyJ0 based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("notActive", 4),
          ("passthrough", 3))
    )


_GnRstCfgTransparencyJ0_Type.__name__ = "Integer32"
_GnRstCfgTransparencyJ0_Object = MibTableColumn
gnRstCfgTransparencyJ0 = _GnRstCfgTransparencyJ0_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 1, 1, 3),
    _GnRstCfgTransparencyJ0_Type()
)
gnRstCfgTransparencyJ0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnRstCfgTransparencyJ0.setStatus("mandatory")


class _GnRstCfgRSTAISMode_Type(Integer32):
    """Custom type gnRstCfgRSTAISMode based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("doNotSendAIS", 3),
          ("sendAIS", 2))
    )


_GnRstCfgRSTAISMode_Type.__name__ = "Integer32"
_GnRstCfgRSTAISMode_Object = MibTableColumn
gnRstCfgRSTAISMode = _GnRstCfgRSTAISMode_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 1, 1, 4),
    _GnRstCfgRSTAISMode_Type()
)
gnRstCfgRSTAISMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnRstCfgRSTAISMode.setStatus("mandatory")


class _GnRstCfgRstEXCThresh_Type(Integer32):
    """Custom type gnRstCfgRstEXCThresh based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("tenExpMinus3", 2),
          ("tenExpMinus4", 3),
          ("tenExpMinus5", 4))
    )


_GnRstCfgRstEXCThresh_Type.__name__ = "Integer32"
_GnRstCfgRstEXCThresh_Object = MibTableColumn
gnRstCfgRstEXCThresh = _GnRstCfgRstEXCThresh_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 1, 1, 5),
    _GnRstCfgRstEXCThresh_Type()
)
gnRstCfgRstEXCThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnRstCfgRstEXCThresh.setStatus("mandatory")


class _GnRstCfgRstSDThresh_Type(Integer32):
    """Custom type gnRstCfgRstSDThresh based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("tenExpMinus6", 3),
          ("tenExpMinus7", 4),
          ("tenExpMinus8", 5),
          ("tenExpMinus9", 6))
    )


_GnRstCfgRstSDThresh_Type.__name__ = "Integer32"
_GnRstCfgRstSDThresh_Object = MibTableColumn
gnRstCfgRstSDThresh = _GnRstCfgRstSDThresh_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 1, 1, 6),
    _GnRstCfgRstSDThresh_Type()
)
gnRstCfgRstSDThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnRstCfgRstSDThresh.setStatus("mandatory")


class _GnRstCfgTransparencyE1_Type(Integer32):
    """Custom type gnRstCfgTransparencyE1 based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("disable", 4),
          ("passthrough", 3))
    )


_GnRstCfgTransparencyE1_Type.__name__ = "Integer32"
_GnRstCfgTransparencyE1_Object = MibTableColumn
gnRstCfgTransparencyE1 = _GnRstCfgTransparencyE1_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 1, 1, 7),
    _GnRstCfgTransparencyE1_Type()
)
gnRstCfgTransparencyE1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnRstCfgTransparencyE1.setStatus("mandatory")


class _GnRstCfgTransparencyF1_Type(Integer32):
    """Custom type gnRstCfgTransparencyF1 based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("disable", 4),
          ("passthrough", 3))
    )


_GnRstCfgTransparencyF1_Type.__name__ = "Integer32"
_GnRstCfgTransparencyF1_Object = MibTableColumn
gnRstCfgTransparencyF1 = _GnRstCfgTransparencyF1_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 1, 1, 8),
    _GnRstCfgTransparencyF1_Type()
)
gnRstCfgTransparencyF1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnRstCfgTransparencyF1.setStatus("mandatory")


class _GnRstCfgTransparencyUnscrambled_Type(Integer32):
    """Custom type gnRstCfgTransparencyUnscrambled based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("passthrough", 3))
    )


_GnRstCfgTransparencyUnscrambled_Type.__name__ = "Integer32"
_GnRstCfgTransparencyUnscrambled_Object = MibTableColumn
gnRstCfgTransparencyUnscrambled = _GnRstCfgTransparencyUnscrambled_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 1, 1, 9),
    _GnRstCfgTransparencyUnscrambled_Type()
)
gnRstCfgTransparencyUnscrambled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnRstCfgTransparencyUnscrambled.setStatus("mandatory")


class _GnRstCfgMngByteLocation_Type(Integer32):
    """Custom type gnRstCfgMngByteLocation based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
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
        *(("dccm", 7),
          ("dccr", 6),
          ("e1Byets", 4),
          ("mediaSpecificBytes", 2),
          ("noMngBytes", 5),
          ("spareA1A0Bytes", 3),
          ("userChannel", 8),
          ("waysideChannel", 9))
    )


_GnRstCfgMngByteLocation_Type.__name__ = "Integer32"
_GnRstCfgMngByteLocation_Object = MibTableColumn
gnRstCfgMngByteLocation = _GnRstCfgMngByteLocation_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 1, 1, 10),
    _GnRstCfgMngByteLocation_Type()
)
gnRstCfgMngByteLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnRstCfgMngByteLocation.setStatus("mandatory")


class _GnRstCfgE1waysideChannel_Type(Integer32):
    """Custom type gnRstCfgE1waysideChannel based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2))
    )


_GnRstCfgE1waysideChannel_Type.__name__ = "Integer32"
_GnRstCfgE1waysideChannel_Object = MibTableColumn
gnRstCfgE1waysideChannel = _GnRstCfgE1waysideChannel_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 1, 1, 11),
    _GnRstCfgE1waysideChannel_Type()
)
gnRstCfgE1waysideChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnRstCfgE1waysideChannel.setStatus("mandatory")


class _GnRstCfgTransparencyDCCR_Type(Integer32):
    """Custom type gnRstCfgTransparencyDCCR based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("passthrough", 3))
    )


_GnRstCfgTransparencyDCCR_Type.__name__ = "Integer32"
_GnRstCfgTransparencyDCCR_Object = MibTableColumn
gnRstCfgTransparencyDCCR = _GnRstCfgTransparencyDCCR_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 1, 1, 12),
    _GnRstCfgTransparencyDCCR_Type()
)
gnRstCfgTransparencyDCCR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnRstCfgTransparencyDCCR.setStatus("mandatory")


class _GnRstCfgTransparencyB1Chan_Type(Integer32):
    """Custom type gnRstCfgTransparencyB1Chan based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("passthrough", 3))
    )


_GnRstCfgTransparencyB1Chan_Type.__name__ = "Integer32"
_GnRstCfgTransparencyB1Chan_Object = MibTableColumn
gnRstCfgTransparencyB1Chan = _GnRstCfgTransparencyB1Chan_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 1, 1, 13),
    _GnRstCfgTransparencyB1Chan_Type()
)
gnRstCfgTransparencyB1Chan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnRstCfgTransparencyB1Chan.setStatus("mandatory")


class _GnRstCfgTestActivate_Type(OctetString):
    """Custom type gnRstCfgTestActivate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_GnRstCfgTestActivate_Type.__name__ = "OctetString"
_GnRstCfgTestActivate_Object = MibTableColumn
gnRstCfgTestActivate = _GnRstCfgTestActivate_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 1, 1, 14),
    _GnRstCfgTestActivate_Type()
)
gnRstCfgTestActivate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnRstCfgTestActivate.setStatus("mandatory")


class _GnRstCfgLoopbackOption_Type(Integer32):
    """Custom type gnRstCfgLoopbackOption based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("interfaceExterLoop", 4),
          ("interfaceInterLoop", 3),
          ("noloopback", 2))
    )


_GnRstCfgLoopbackOption_Type.__name__ = "Integer32"
_GnRstCfgLoopbackOption_Object = MibTableColumn
gnRstCfgLoopbackOption = _GnRstCfgLoopbackOption_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 1, 1, 15),
    _GnRstCfgLoopbackOption_Type()
)
gnRstCfgLoopbackOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnRstCfgLoopbackOption.setStatus("mandatory")
_GnRstStatTable_Object = MibTable
gnRstStatTable = _GnRstStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 2)
)
if mibBuilder.loadTexts:
    gnRstStatTable.setStatus("mandatory")
_GnRstStatEntry_Object = MibTableRow
gnRstStatEntry = _GnRstStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 2, 1)
)
gnRstStatEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    gnRstStatEntry.setStatus("mandatory")


class _GnRstStatReceivedJ0_Type(DisplayString):
    """Custom type gnRstStatReceivedJ0 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_GnRstStatReceivedJ0_Type.__name__ = "DisplayString"
_GnRstStatReceivedJ0_Object = MibTableColumn
gnRstStatReceivedJ0 = _GnRstStatReceivedJ0_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 2, 1, 1),
    _GnRstStatReceivedJ0_Type()
)
gnRstStatReceivedJ0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnRstStatReceivedJ0.setStatus("mandatory")


class _GnRstStatBERCur_Type(Integer32):
    """Custom type gnRstStatBERCur based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
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
        *(("tenExpMinus10", 9),
          ("tenExpMinus11", 10),
          ("tenExpMinus12", 11),
          ("tenExpMinus13", 12),
          ("tenExpMinus14", 13),
          ("tenExpMinus3", 2),
          ("tenExpMinus4", 3),
          ("tenExpMinus5", 4),
          ("tenExpMinus6", 5),
          ("tenExpMinus7", 6),
          ("tenExpMinus8", 7),
          ("tenExpMinus9", 8))
    )


_GnRstStatBERCur_Type.__name__ = "Integer32"
_GnRstStatBERCur_Object = MibTableColumn
gnRstStatBERCur = _GnRstStatBERCur_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 2, 1, 2),
    _GnRstStatBERCur_Type()
)
gnRstStatBERCur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnRstStatBERCur.setStatus("mandatory")


class _GnRstStatStatus_Type(OctetString):
    """Custom type gnRstStatStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_GnRstStatStatus_Type.__name__ = "OctetString"
_GnRstStatStatus_Object = MibTableColumn
gnRstStatStatus = _GnRstStatStatus_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 2, 1, 3),
    _GnRstStatStatus_Type()
)
gnRstStatStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnRstStatStatus.setStatus("mandatory")


class _GnRstStatClearLoopTimer_Type(Integer32):
    """Custom type gnRstStatClearLoopTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_GnRstStatClearLoopTimer_Type.__name__ = "Integer32"
_GnRstStatClearLoopTimer_Object = MibTableColumn
gnRstStatClearLoopTimer = _GnRstStatClearLoopTimer_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 2, 1, 4),
    _GnRstStatClearLoopTimer_Type()
)
gnRstStatClearLoopTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnRstStatClearLoopTimer.setStatus("mandatory")
_GnRstMon_ObjectIdentity = ObjectIdentity
gnRstMon = _GnRstMon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 3)
)
_GnRstMonCurrTable_Object = MibTable
gnRstMonCurrTable = _GnRstMonCurrTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 3, 1)
)
if mibBuilder.loadTexts:
    gnRstMonCurrTable.setStatus("mandatory")
_GnRstMonCurrEntry_Object = MibTableRow
gnRstMonCurrEntry = _GnRstMonCurrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 3, 1, 1)
)
gnRstMonCurrEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    gnRstMonCurrEntry.setStatus("mandatory")
_GnRstMonCurrBBE_Type = Gauge32
_GnRstMonCurrBBE_Object = MibTableColumn
gnRstMonCurrBBE = _GnRstMonCurrBBE_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 3, 1, 1, 1),
    _GnRstMonCurrBBE_Type()
)
gnRstMonCurrBBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnRstMonCurrBBE.setStatus("mandatory")
_GnRstMonCurrUAS_Type = Gauge32
_GnRstMonCurrUAS_Object = MibTableColumn
gnRstMonCurrUAS = _GnRstMonCurrUAS_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 3, 1, 1, 2),
    _GnRstMonCurrUAS_Type()
)
gnRstMonCurrUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnRstMonCurrUAS.setStatus("mandatory")
_GnRstMonCurrLastDayES_Type = Gauge32
_GnRstMonCurrLastDayES_Object = MibTableColumn
gnRstMonCurrLastDayES = _GnRstMonCurrLastDayES_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 3, 1, 1, 3),
    _GnRstMonCurrLastDayES_Type()
)
gnRstMonCurrLastDayES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnRstMonCurrLastDayES.setStatus("mandatory")
_GnRstMonCurrLastDaySES_Type = Gauge32
_GnRstMonCurrLastDaySES_Object = MibTableColumn
gnRstMonCurrLastDaySES = _GnRstMonCurrLastDaySES_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 3, 1, 1, 4),
    _GnRstMonCurrLastDaySES_Type()
)
gnRstMonCurrLastDaySES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnRstMonCurrLastDaySES.setStatus("mandatory")
_GnRstMonCurrLastDayBBE_Type = Gauge32
_GnRstMonCurrLastDayBBE_Object = MibTableColumn
gnRstMonCurrLastDayBBE = _GnRstMonCurrLastDayBBE_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 3, 1, 1, 5),
    _GnRstMonCurrLastDayBBE_Type()
)
gnRstMonCurrLastDayBBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnRstMonCurrLastDayBBE.setStatus("mandatory")
_GnRstMonCurrLastDayUAS_Type = Gauge32
_GnRstMonCurrLastDayUAS_Object = MibTableColumn
gnRstMonCurrLastDayUAS = _GnRstMonCurrLastDayUAS_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 3, 1, 1, 6),
    _GnRstMonCurrLastDayUAS_Type()
)
gnRstMonCurrLastDayUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnRstMonCurrLastDayUAS.setStatus("mandatory")
_GnRstMonCurrLastDayOFS_Type = Gauge32
_GnRstMonCurrLastDayOFS_Object = MibTableColumn
gnRstMonCurrLastDayOFS = _GnRstMonCurrLastDayOFS_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 3, 1, 1, 7),
    _GnRstMonCurrLastDayOFS_Type()
)
gnRstMonCurrLastDayOFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnRstMonCurrLastDayOFS.setStatus("mandatory")


class _GnRstMonCurrLastDayIDF_Type(Integer32):
    """Custom type gnRstMonCurrLastDayIDF based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3))
    )


_GnRstMonCurrLastDayIDF_Type.__name__ = "Integer32"
_GnRstMonCurrLastDayIDF_Object = MibTableColumn
gnRstMonCurrLastDayIDF = _GnRstMonCurrLastDayIDF_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 3, 1, 1, 8),
    _GnRstMonCurrLastDayIDF_Type()
)
gnRstMonCurrLastDayIDF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnRstMonCurrLastDayIDF.setStatus("mandatory")
_GnRstMonIntervalTable_Object = MibTable
gnRstMonIntervalTable = _GnRstMonIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 3, 2)
)
if mibBuilder.loadTexts:
    gnRstMonIntervalTable.setStatus("mandatory")
_GnRstMonIntervalEntry_Object = MibTableRow
gnRstMonIntervalEntry = _GnRstMonIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 3, 2, 1)
)
gnRstMonIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CERAGON-MIB", "gnRstMonIntervalIdx"),
)
if mibBuilder.loadTexts:
    gnRstMonIntervalEntry.setStatus("mandatory")


class _GnRstMonIntervalIdx_Type(Integer32):
    """Custom type gnRstMonIntervalIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_GnRstMonIntervalIdx_Type.__name__ = "Integer32"
_GnRstMonIntervalIdx_Object = MibTableColumn
gnRstMonIntervalIdx = _GnRstMonIntervalIdx_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 3, 2, 1, 1),
    _GnRstMonIntervalIdx_Type()
)
gnRstMonIntervalIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnRstMonIntervalIdx.setStatus("mandatory")
_GnRstMonIntervalBBE_Type = Gauge32
_GnRstMonIntervalBBE_Object = MibTableColumn
gnRstMonIntervalBBE = _GnRstMonIntervalBBE_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 3, 2, 1, 2),
    _GnRstMonIntervalBBE_Type()
)
gnRstMonIntervalBBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnRstMonIntervalBBE.setStatus("mandatory")
_GnRstMonIntervalUAS_Type = Gauge32
_GnRstMonIntervalUAS_Object = MibTableColumn
gnRstMonIntervalUAS = _GnRstMonIntervalUAS_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 3, 2, 1, 3),
    _GnRstMonIntervalUAS_Type()
)
gnRstMonIntervalUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnRstMonIntervalUAS.setStatus("mandatory")


class _GnRstMonIntervalIDF_Type(Integer32):
    """Custom type gnRstMonIntervalIDF based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3))
    )


_GnRstMonIntervalIDF_Type.__name__ = "Integer32"
_GnRstMonIntervalIDF_Object = MibTableColumn
gnRstMonIntervalIDF = _GnRstMonIntervalIDF_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 3, 2, 1, 4),
    _GnRstMonIntervalIDF_Type()
)
gnRstMonIntervalIDF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnRstMonIntervalIDF.setStatus("mandatory")
_GnRstMonDayTable_Object = MibTable
gnRstMonDayTable = _GnRstMonDayTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 3, 3)
)
if mibBuilder.loadTexts:
    gnRstMonDayTable.setStatus("mandatory")
_GnRstMonDayEntry_Object = MibTableRow
gnRstMonDayEntry = _GnRstMonDayEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 3, 3, 1)
)
gnRstMonDayEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CERAGON-MIB", "gnRstMonDayIdx"),
)
if mibBuilder.loadTexts:
    gnRstMonDayEntry.setStatus("mandatory")


class _GnRstMonDayIdx_Type(Integer32):
    """Custom type gnRstMonDayIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_GnRstMonDayIdx_Type.__name__ = "Integer32"
_GnRstMonDayIdx_Object = MibTableColumn
gnRstMonDayIdx = _GnRstMonDayIdx_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 3, 3, 1, 1),
    _GnRstMonDayIdx_Type()
)
gnRstMonDayIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnRstMonDayIdx.setStatus("mandatory")
_GnRstMonDayES_Type = Gauge32
_GnRstMonDayES_Object = MibTableColumn
gnRstMonDayES = _GnRstMonDayES_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 3, 3, 1, 2),
    _GnRstMonDayES_Type()
)
gnRstMonDayES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnRstMonDayES.setStatus("mandatory")
_GnRstMonDaySES_Type = Gauge32
_GnRstMonDaySES_Object = MibTableColumn
gnRstMonDaySES = _GnRstMonDaySES_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 3, 3, 1, 3),
    _GnRstMonDaySES_Type()
)
gnRstMonDaySES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnRstMonDaySES.setStatus("mandatory")
_GnRstMonDayBBE_Type = Gauge32
_GnRstMonDayBBE_Object = MibTableColumn
gnRstMonDayBBE = _GnRstMonDayBBE_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 3, 3, 1, 4),
    _GnRstMonDayBBE_Type()
)
gnRstMonDayBBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnRstMonDayBBE.setStatus("mandatory")
_GnRstMonDayUAS_Type = Gauge32
_GnRstMonDayUAS_Object = MibTableColumn
gnRstMonDayUAS = _GnRstMonDayUAS_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 3, 3, 1, 5),
    _GnRstMonDayUAS_Type()
)
gnRstMonDayUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnRstMonDayUAS.setStatus("mandatory")
_GnRstMonDayOFS_Type = Gauge32
_GnRstMonDayOFS_Object = MibTableColumn
gnRstMonDayOFS = _GnRstMonDayOFS_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 3, 3, 1, 6),
    _GnRstMonDayOFS_Type()
)
gnRstMonDayOFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnRstMonDayOFS.setStatus("mandatory")


class _GnRstMonDayIDF_Type(Integer32):
    """Custom type gnRstMonDayIDF based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3))
    )


_GnRstMonDayIDF_Type.__name__ = "Integer32"
_GnRstMonDayIDF_Object = MibTableColumn
gnRstMonDayIDF = _GnRstMonDayIDF_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 3, 3, 1, 7),
    _GnRstMonDayIDF_Type()
)
gnRstMonDayIDF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnRstMonDayIDF.setStatus("mandatory")
_GnMstCfgTable_Object = MibTable
gnMstCfgTable = _GnMstCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 4)
)
if mibBuilder.loadTexts:
    gnMstCfgTable.setStatus("mandatory")
_GnMstCfgEntry_Object = MibTableRow
gnMstCfgEntry = _GnMstCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 4, 1)
)
gnMstCfgEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    gnMstCfgEntry.setStatus("mandatory")


class _GnMstCfgEXCThresh_Type(Integer32):
    """Custom type gnMstCfgEXCThresh based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("tenExpMinus3", 2),
          ("tenExpMinus4", 3),
          ("tenExpMinus5", 4))
    )


_GnMstCfgEXCThresh_Type.__name__ = "Integer32"
_GnMstCfgEXCThresh_Object = MibTableColumn
gnMstCfgEXCThresh = _GnMstCfgEXCThresh_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 4, 1, 1),
    _GnMstCfgEXCThresh_Type()
)
gnMstCfgEXCThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnMstCfgEXCThresh.setStatus("mandatory")


class _GnMstCfgSDThresh_Type(Integer32):
    """Custom type gnMstCfgSDThresh based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("tenExpMinus6", 3),
          ("tenExpMinus7", 4),
          ("tenExpMinus8", 5),
          ("tenExpMinus9", 6))
    )


_GnMstCfgSDThresh_Type.__name__ = "Integer32"
_GnMstCfgSDThresh_Object = MibTableColumn
gnMstCfgSDThresh = _GnMstCfgSDThresh_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 4, 1, 2),
    _GnMstCfgSDThresh_Type()
)
gnMstCfgSDThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnMstCfgSDThresh.setStatus("mandatory")
_GnMstStatTable_Object = MibTable
gnMstStatTable = _GnMstStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 5)
)
if mibBuilder.loadTexts:
    gnMstStatTable.setStatus("mandatory")
_GnMstStatEntry_Object = MibTableRow
gnMstStatEntry = _GnMstStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 5, 1)
)
gnMstStatEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    gnMstStatEntry.setStatus("mandatory")


class _GnMstStatReceivedS1_Type(Integer32):
    """Custom type gnMstStatReceivedS1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_GnMstStatReceivedS1_Type.__name__ = "Integer32"
_GnMstStatReceivedS1_Object = MibTableColumn
gnMstStatReceivedS1 = _GnMstStatReceivedS1_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 5, 1, 1),
    _GnMstStatReceivedS1_Type()
)
gnMstStatReceivedS1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnMstStatReceivedS1.setStatus("mandatory")


class _GnMstStatStatus_Type(OctetString):
    """Custom type gnMstStatStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_GnMstStatStatus_Type.__name__ = "OctetString"
_GnMstStatStatus_Object = MibTableColumn
gnMstStatStatus = _GnMstStatStatus_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 5, 1, 2),
    _GnMstStatStatus_Type()
)
gnMstStatStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnMstStatStatus.setStatus("mandatory")


class _GnMstStatTransmitS1_Type(Integer32):
    """Custom type gnMstStatTransmitS1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_GnMstStatTransmitS1_Type.__name__ = "Integer32"
_GnMstStatTransmitS1_Object = MibTableColumn
gnMstStatTransmitS1 = _GnMstStatTransmitS1_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 5, 1, 3),
    _GnMstStatTransmitS1_Type()
)
gnMstStatTransmitS1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnMstStatTransmitS1.setStatus("mandatory")


class _GnMstStatCurrentBer_Type(Integer32):
    """Custom type gnMstStatCurrentBer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
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
        *(("tenExpMinus10", 9),
          ("tenExpMinus11", 10),
          ("tenExpMinus12", 11),
          ("tenExpMinus13", 12),
          ("tenExpMinus14", 13),
          ("tenExpMinus3", 2),
          ("tenExpMinus4", 3),
          ("tenExpMinus5", 4),
          ("tenExpMinus6", 5),
          ("tenExpMinus7", 6),
          ("tenExpMinus8", 7),
          ("tenExpMinus9", 8))
    )


_GnMstStatCurrentBer_Type.__name__ = "Integer32"
_GnMstStatCurrentBer_Object = MibTableColumn
gnMstStatCurrentBer = _GnMstStatCurrentBer_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 5, 1, 4),
    _GnMstStatCurrentBer_Type()
)
gnMstStatCurrentBer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnMstStatCurrentBer.setStatus("mandatory")


class _GnMstStatReceivedK1_Type(Integer32):
    """Custom type gnMstStatReceivedK1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_GnMstStatReceivedK1_Type.__name__ = "Integer32"
_GnMstStatReceivedK1_Object = MibTableColumn
gnMstStatReceivedK1 = _GnMstStatReceivedK1_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 5, 1, 5),
    _GnMstStatReceivedK1_Type()
)
gnMstStatReceivedK1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnMstStatReceivedK1.setStatus("mandatory")


class _GnMstStatReceivedK2_Type(Integer32):
    """Custom type gnMstStatReceivedK2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_GnMstStatReceivedK2_Type.__name__ = "Integer32"
_GnMstStatReceivedK2_Object = MibTableColumn
gnMstStatReceivedK2 = _GnMstStatReceivedK2_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 5, 1, 6),
    _GnMstStatReceivedK2_Type()
)
gnMstStatReceivedK2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnMstStatReceivedK2.setStatus("mandatory")


class _GnMstStatTransmitK1_Type(Integer32):
    """Custom type gnMstStatTransmitK1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_GnMstStatTransmitK1_Type.__name__ = "Integer32"
_GnMstStatTransmitK1_Object = MibTableColumn
gnMstStatTransmitK1 = _GnMstStatTransmitK1_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 5, 1, 7),
    _GnMstStatTransmitK1_Type()
)
gnMstStatTransmitK1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnMstStatTransmitK1.setStatus("mandatory")


class _GnMstStatTransmitK2_Type(Integer32):
    """Custom type gnMstStatTransmitK2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_GnMstStatTransmitK2_Type.__name__ = "Integer32"
_GnMstStatTransmitK2_Object = MibTableColumn
gnMstStatTransmitK2 = _GnMstStatTransmitK2_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 5, 1, 8),
    _GnMstStatTransmitK2_Type()
)
gnMstStatTransmitK2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnMstStatTransmitK2.setStatus("mandatory")
_GnMstMon_ObjectIdentity = ObjectIdentity
gnMstMon = _GnMstMon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 6)
)
_GnMstMonCurrTable_Object = MibTable
gnMstMonCurrTable = _GnMstMonCurrTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 6, 1)
)
if mibBuilder.loadTexts:
    gnMstMonCurrTable.setStatus("mandatory")
_GnMstMonCurrEntry_Object = MibTableRow
gnMstMonCurrEntry = _GnMstMonCurrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 6, 1, 1)
)
gnMstMonCurrEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    gnMstMonCurrEntry.setStatus("mandatory")
_GnMstMonCurrBBE_Type = Gauge32
_GnMstMonCurrBBE_Object = MibTableColumn
gnMstMonCurrBBE = _GnMstMonCurrBBE_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 6, 1, 1, 1),
    _GnMstMonCurrBBE_Type()
)
gnMstMonCurrBBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnMstMonCurrBBE.setStatus("mandatory")
_GnMstMonCurrUAS_Type = Gauge32
_GnMstMonCurrUAS_Object = MibTableColumn
gnMstMonCurrUAS = _GnMstMonCurrUAS_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 6, 1, 1, 2),
    _GnMstMonCurrUAS_Type()
)
gnMstMonCurrUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnMstMonCurrUAS.setStatus("mandatory")
_GnMstMonCurrLastDayES_Type = Gauge32
_GnMstMonCurrLastDayES_Object = MibTableColumn
gnMstMonCurrLastDayES = _GnMstMonCurrLastDayES_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 6, 1, 1, 3),
    _GnMstMonCurrLastDayES_Type()
)
gnMstMonCurrLastDayES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnMstMonCurrLastDayES.setStatus("mandatory")
_GnMstMonCurrLastDaySES_Type = Gauge32
_GnMstMonCurrLastDaySES_Object = MibTableColumn
gnMstMonCurrLastDaySES = _GnMstMonCurrLastDaySES_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 6, 1, 1, 4),
    _GnMstMonCurrLastDaySES_Type()
)
gnMstMonCurrLastDaySES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnMstMonCurrLastDaySES.setStatus("mandatory")
_GnMstMonCurrLastDayBBE_Type = Gauge32
_GnMstMonCurrLastDayBBE_Object = MibTableColumn
gnMstMonCurrLastDayBBE = _GnMstMonCurrLastDayBBE_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 6, 1, 1, 5),
    _GnMstMonCurrLastDayBBE_Type()
)
gnMstMonCurrLastDayBBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnMstMonCurrLastDayBBE.setStatus("mandatory")
_GnMstMonCurrLastDayUAS_Type = Gauge32
_GnMstMonCurrLastDayUAS_Object = MibTableColumn
gnMstMonCurrLastDayUAS = _GnMstMonCurrLastDayUAS_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 6, 1, 1, 6),
    _GnMstMonCurrLastDayUAS_Type()
)
gnMstMonCurrLastDayUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnMstMonCurrLastDayUAS.setStatus("mandatory")
_GnMstMonIntervalTable_Object = MibTable
gnMstMonIntervalTable = _GnMstMonIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 6, 2)
)
if mibBuilder.loadTexts:
    gnMstMonIntervalTable.setStatus("mandatory")
_GnMstMonIntervalEntry_Object = MibTableRow
gnMstMonIntervalEntry = _GnMstMonIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 6, 2, 1)
)
gnMstMonIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CERAGON-MIB", "gnMstMonIntervalIdx"),
)
if mibBuilder.loadTexts:
    gnMstMonIntervalEntry.setStatus("mandatory")


class _GnMstMonIntervalIdx_Type(Integer32):
    """Custom type gnMstMonIntervalIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_GnMstMonIntervalIdx_Type.__name__ = "Integer32"
_GnMstMonIntervalIdx_Object = MibTableColumn
gnMstMonIntervalIdx = _GnMstMonIntervalIdx_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 6, 2, 1, 1),
    _GnMstMonIntervalIdx_Type()
)
gnMstMonIntervalIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnMstMonIntervalIdx.setStatus("mandatory")
_GnMstMonIntervalBBE_Type = Gauge32
_GnMstMonIntervalBBE_Object = MibTableColumn
gnMstMonIntervalBBE = _GnMstMonIntervalBBE_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 6, 2, 1, 2),
    _GnMstMonIntervalBBE_Type()
)
gnMstMonIntervalBBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnMstMonIntervalBBE.setStatus("mandatory")
_GnMstMonIntervalUAS_Type = Gauge32
_GnMstMonIntervalUAS_Object = MibTableColumn
gnMstMonIntervalUAS = _GnMstMonIntervalUAS_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 6, 2, 1, 3),
    _GnMstMonIntervalUAS_Type()
)
gnMstMonIntervalUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnMstMonIntervalUAS.setStatus("mandatory")
_GnMstMonDayTable_Object = MibTable
gnMstMonDayTable = _GnMstMonDayTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 6, 3)
)
if mibBuilder.loadTexts:
    gnMstMonDayTable.setStatus("mandatory")
_GnMstMonDayEntry_Object = MibTableRow
gnMstMonDayEntry = _GnMstMonDayEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 6, 3, 1)
)
gnMstMonDayEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CERAGON-MIB", "gnMstMonDayIdx"),
)
if mibBuilder.loadTexts:
    gnMstMonDayEntry.setStatus("mandatory")


class _GnMstMonDayIdx_Type(Integer32):
    """Custom type gnMstMonDayIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_GnMstMonDayIdx_Type.__name__ = "Integer32"
_GnMstMonDayIdx_Object = MibTableColumn
gnMstMonDayIdx = _GnMstMonDayIdx_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 6, 3, 1, 1),
    _GnMstMonDayIdx_Type()
)
gnMstMonDayIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnMstMonDayIdx.setStatus("mandatory")
_GnMstMonDayES_Type = Gauge32
_GnMstMonDayES_Object = MibTableColumn
gnMstMonDayES = _GnMstMonDayES_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 6, 3, 1, 2),
    _GnMstMonDayES_Type()
)
gnMstMonDayES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnMstMonDayES.setStatus("mandatory")
_GnMstMonDaySES_Type = Gauge32
_GnMstMonDaySES_Object = MibTableColumn
gnMstMonDaySES = _GnMstMonDaySES_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 6, 3, 1, 3),
    _GnMstMonDaySES_Type()
)
gnMstMonDaySES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnMstMonDaySES.setStatus("mandatory")
_GnMstMonDayBBE_Type = Gauge32
_GnMstMonDayBBE_Object = MibTableColumn
gnMstMonDayBBE = _GnMstMonDayBBE_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 6, 3, 1, 4),
    _GnMstMonDayBBE_Type()
)
gnMstMonDayBBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnMstMonDayBBE.setStatus("mandatory")
_GnMstMonDayUAS_Type = Gauge32
_GnMstMonDayUAS_Object = MibTableColumn
gnMstMonDayUAS = _GnMstMonDayUAS_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 6, 3, 1, 5),
    _GnMstMonDayUAS_Type()
)
gnMstMonDayUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnMstMonDayUAS.setStatus("mandatory")
_GnMstFarEndMonCurrTable_Object = MibTable
gnMstFarEndMonCurrTable = _GnMstFarEndMonCurrTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 6, 4)
)
if mibBuilder.loadTexts:
    gnMstFarEndMonCurrTable.setStatus("mandatory")
_GnMstFarEndMonCurrEntry_Object = MibTableRow
gnMstFarEndMonCurrEntry = _GnMstFarEndMonCurrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 6, 4, 1)
)
gnMstFarEndMonCurrEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    gnMstFarEndMonCurrEntry.setStatus("mandatory")
_GnMstFarEndMonCurrBBE_Type = Gauge32
_GnMstFarEndMonCurrBBE_Object = MibTableColumn
gnMstFarEndMonCurrBBE = _GnMstFarEndMonCurrBBE_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 6, 4, 1, 1),
    _GnMstFarEndMonCurrBBE_Type()
)
gnMstFarEndMonCurrBBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnMstFarEndMonCurrBBE.setStatus("mandatory")
_GnMstFarEndMonCurrUAS_Type = Gauge32
_GnMstFarEndMonCurrUAS_Object = MibTableColumn
gnMstFarEndMonCurrUAS = _GnMstFarEndMonCurrUAS_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 6, 4, 1, 2),
    _GnMstFarEndMonCurrUAS_Type()
)
gnMstFarEndMonCurrUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnMstFarEndMonCurrUAS.setStatus("mandatory")
_GnMstFarEndMonCurrLastDayES_Type = Gauge32
_GnMstFarEndMonCurrLastDayES_Object = MibTableColumn
gnMstFarEndMonCurrLastDayES = _GnMstFarEndMonCurrLastDayES_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 6, 4, 1, 3),
    _GnMstFarEndMonCurrLastDayES_Type()
)
gnMstFarEndMonCurrLastDayES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnMstFarEndMonCurrLastDayES.setStatus("mandatory")
_GnMstFarEndMonCurrLastDaySES_Type = Gauge32
_GnMstFarEndMonCurrLastDaySES_Object = MibTableColumn
gnMstFarEndMonCurrLastDaySES = _GnMstFarEndMonCurrLastDaySES_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 6, 4, 1, 4),
    _GnMstFarEndMonCurrLastDaySES_Type()
)
gnMstFarEndMonCurrLastDaySES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnMstFarEndMonCurrLastDaySES.setStatus("mandatory")
_GnMstFarEndMonCurrLastDayBBE_Type = Gauge32
_GnMstFarEndMonCurrLastDayBBE_Object = MibTableColumn
gnMstFarEndMonCurrLastDayBBE = _GnMstFarEndMonCurrLastDayBBE_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 6, 4, 1, 5),
    _GnMstFarEndMonCurrLastDayBBE_Type()
)
gnMstFarEndMonCurrLastDayBBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnMstFarEndMonCurrLastDayBBE.setStatus("mandatory")
_GnMstFarEndMonCurrLastDayUAS_Type = Gauge32
_GnMstFarEndMonCurrLastDayUAS_Object = MibTableColumn
gnMstFarEndMonCurrLastDayUAS = _GnMstFarEndMonCurrLastDayUAS_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 6, 4, 1, 6),
    _GnMstFarEndMonCurrLastDayUAS_Type()
)
gnMstFarEndMonCurrLastDayUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnMstFarEndMonCurrLastDayUAS.setStatus("mandatory")
_GnMstFarEndMonIntervalTable_Object = MibTable
gnMstFarEndMonIntervalTable = _GnMstFarEndMonIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 6, 5)
)
if mibBuilder.loadTexts:
    gnMstFarEndMonIntervalTable.setStatus("mandatory")
_GnMstFarEndMonIntervalEntry_Object = MibTableRow
gnMstFarEndMonIntervalEntry = _GnMstFarEndMonIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 6, 5, 1)
)
gnMstFarEndMonIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CERAGON-MIB", "gnMstFarEndMonIntervalIdx"),
)
if mibBuilder.loadTexts:
    gnMstFarEndMonIntervalEntry.setStatus("mandatory")


class _GnMstFarEndMonIntervalIdx_Type(Integer32):
    """Custom type gnMstFarEndMonIntervalIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_GnMstFarEndMonIntervalIdx_Type.__name__ = "Integer32"
_GnMstFarEndMonIntervalIdx_Object = MibTableColumn
gnMstFarEndMonIntervalIdx = _GnMstFarEndMonIntervalIdx_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 6, 5, 1, 1),
    _GnMstFarEndMonIntervalIdx_Type()
)
gnMstFarEndMonIntervalIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnMstFarEndMonIntervalIdx.setStatus("mandatory")
_GnMstFarEndMonIntervalBBE_Type = Gauge32
_GnMstFarEndMonIntervalBBE_Object = MibTableColumn
gnMstFarEndMonIntervalBBE = _GnMstFarEndMonIntervalBBE_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 6, 5, 1, 2),
    _GnMstFarEndMonIntervalBBE_Type()
)
gnMstFarEndMonIntervalBBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnMstFarEndMonIntervalBBE.setStatus("mandatory")
_GnMstFarEndMonIntervalUAS_Type = Gauge32
_GnMstFarEndMonIntervalUAS_Object = MibTableColumn
gnMstFarEndMonIntervalUAS = _GnMstFarEndMonIntervalUAS_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 6, 5, 1, 3),
    _GnMstFarEndMonIntervalUAS_Type()
)
gnMstFarEndMonIntervalUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnMstFarEndMonIntervalUAS.setStatus("mandatory")
_GnMstFarEndMonDayTable_Object = MibTable
gnMstFarEndMonDayTable = _GnMstFarEndMonDayTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 6, 6)
)
if mibBuilder.loadTexts:
    gnMstFarEndMonDayTable.setStatus("mandatory")
_GnMstFarEndMonDayEntry_Object = MibTableRow
gnMstFarEndMonDayEntry = _GnMstFarEndMonDayEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 6, 6, 1)
)
gnMstFarEndMonDayEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CERAGON-MIB", "gnMstFarEndMonDayIdx"),
)
if mibBuilder.loadTexts:
    gnMstFarEndMonDayEntry.setStatus("mandatory")


class _GnMstFarEndMonDayIdx_Type(Integer32):
    """Custom type gnMstFarEndMonDayIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_GnMstFarEndMonDayIdx_Type.__name__ = "Integer32"
_GnMstFarEndMonDayIdx_Object = MibTableColumn
gnMstFarEndMonDayIdx = _GnMstFarEndMonDayIdx_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 6, 6, 1, 1),
    _GnMstFarEndMonDayIdx_Type()
)
gnMstFarEndMonDayIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnMstFarEndMonDayIdx.setStatus("mandatory")
_GnMstFarEndMonDayES_Type = Gauge32
_GnMstFarEndMonDayES_Object = MibTableColumn
gnMstFarEndMonDayES = _GnMstFarEndMonDayES_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 6, 6, 1, 2),
    _GnMstFarEndMonDayES_Type()
)
gnMstFarEndMonDayES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnMstFarEndMonDayES.setStatus("mandatory")
_GnMstFarEndMonDaySES_Type = Gauge32
_GnMstFarEndMonDaySES_Object = MibTableColumn
gnMstFarEndMonDaySES = _GnMstFarEndMonDaySES_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 6, 6, 1, 3),
    _GnMstFarEndMonDaySES_Type()
)
gnMstFarEndMonDaySES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnMstFarEndMonDaySES.setStatus("mandatory")
_GnMstFarEndMonDayBBE_Type = Gauge32
_GnMstFarEndMonDayBBE_Object = MibTableColumn
gnMstFarEndMonDayBBE = _GnMstFarEndMonDayBBE_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 6, 6, 1, 4),
    _GnMstFarEndMonDayBBE_Type()
)
gnMstFarEndMonDayBBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnMstFarEndMonDayBBE.setStatus("mandatory")
_GnMstFarEndMonDayUAS_Type = Gauge32
_GnMstFarEndMonDayUAS_Object = MibTableColumn
gnMstFarEndMonDayUAS = _GnMstFarEndMonDayUAS_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 6, 6, 1, 5),
    _GnMstFarEndMonDayUAS_Type()
)
gnMstFarEndMonDayUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnMstFarEndMonDayUAS.setStatus("mandatory")
_GnHptCfgTable_Object = MibTable
gnHptCfgTable = _GnHptCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 7)
)
if mibBuilder.loadTexts:
    gnHptCfgTable.setStatus("mandatory")
_GnHptCfgEntry_Object = MibTableRow
gnHptCfgEntry = _GnHptCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 7, 1)
)
gnHptCfgEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    gnHptCfgEntry.setStatus("mandatory")


class _GnHptCfgTransmittedJ1_Type(DisplayString):
    """Custom type gnHptCfgTransmittedJ1 based on DisplayString"""
    defaultValue = OctetString("  ACCESS MUX   ")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_GnHptCfgTransmittedJ1_Type.__name__ = "DisplayString"
_GnHptCfgTransmittedJ1_Object = MibTableColumn
gnHptCfgTransmittedJ1 = _GnHptCfgTransmittedJ1_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 7, 1, 1),
    _GnHptCfgTransmittedJ1_Type()
)
gnHptCfgTransmittedJ1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnHptCfgTransmittedJ1.setStatus("mandatory")


class _GnHptCfgExpectedJ1_Type(DisplayString):
    """Custom type gnHptCfgExpectedJ1 based on DisplayString"""
    defaultValue = OctetString("  ACCESS MUX   ")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_GnHptCfgExpectedJ1_Type.__name__ = "DisplayString"
_GnHptCfgExpectedJ1_Object = MibTableColumn
gnHptCfgExpectedJ1 = _GnHptCfgExpectedJ1_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 7, 1, 2),
    _GnHptCfgExpectedJ1_Type()
)
gnHptCfgExpectedJ1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnHptCfgExpectedJ1.setStatus("mandatory")


class _GnHptCfgMismatchJ1_Type(Integer32):
    """Custom type gnHptCfgMismatchJ1 based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("sendAIS", 3),
          ("sendAlarm", 2))
    )


_GnHptCfgMismatchJ1_Type.__name__ = "Integer32"
_GnHptCfgMismatchJ1_Object = MibTableColumn
gnHptCfgMismatchJ1 = _GnHptCfgMismatchJ1_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 7, 1, 3),
    _GnHptCfgMismatchJ1_Type()
)
gnHptCfgMismatchJ1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnHptCfgMismatchJ1.setStatus("mandatory")


class _GnHptCfgTransparencyJ1_Type(Integer32):
    """Custom type gnHptCfgTransparencyJ1 based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("notActive", 4),
          ("passthrough", 3))
    )


_GnHptCfgTransparencyJ1_Type.__name__ = "Integer32"
_GnHptCfgTransparencyJ1_Object = MibTableColumn
gnHptCfgTransparencyJ1 = _GnHptCfgTransparencyJ1_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 7, 1, 4),
    _GnHptCfgTransparencyJ1_Type()
)
gnHptCfgTransparencyJ1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnHptCfgTransparencyJ1.setStatus("mandatory")


class _GnHptCfgEXCThresh_Type(Integer32):
    """Custom type gnHptCfgEXCThresh based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("tenExpMinus3", 2),
          ("tenExpMinus4", 3),
          ("tenExpMinus5", 4))
    )


_GnHptCfgEXCThresh_Type.__name__ = "Integer32"
_GnHptCfgEXCThresh_Object = MibTableColumn
gnHptCfgEXCThresh = _GnHptCfgEXCThresh_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 7, 1, 5),
    _GnHptCfgEXCThresh_Type()
)
gnHptCfgEXCThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnHptCfgEXCThresh.setStatus("mandatory")


class _GnHptCfgSDThresh_Type(Integer32):
    """Custom type gnHptCfgSDThresh based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("tenExpMinus6", 3),
          ("tenExpMinus7", 4),
          ("tenExpMinus8", 5),
          ("tenExpMinus9", 6))
    )


_GnHptCfgSDThresh_Type.__name__ = "Integer32"
_GnHptCfgSDThresh_Object = MibTableColumn
gnHptCfgSDThresh = _GnHptCfgSDThresh_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 7, 1, 6),
    _GnHptCfgSDThresh_Type()
)
gnHptCfgSDThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnHptCfgSDThresh.setStatus("mandatory")


class _GnHptCfgTug3Structure1_Type(OctetString):
    """Custom type gnHptCfgTug3Structure1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_GnHptCfgTug3Structure1_Type.__name__ = "OctetString"
_GnHptCfgTug3Structure1_Object = MibTableColumn
gnHptCfgTug3Structure1 = _GnHptCfgTug3Structure1_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 7, 1, 7),
    _GnHptCfgTug3Structure1_Type()
)
gnHptCfgTug3Structure1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnHptCfgTug3Structure1.setStatus("mandatory")


class _GnHptCfgTug3Structure2_Type(OctetString):
    """Custom type gnHptCfgTug3Structure2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_GnHptCfgTug3Structure2_Type.__name__ = "OctetString"
_GnHptCfgTug3Structure2_Object = MibTableColumn
gnHptCfgTug3Structure2 = _GnHptCfgTug3Structure2_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 7, 1, 8),
    _GnHptCfgTug3Structure2_Type()
)
gnHptCfgTug3Structure2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnHptCfgTug3Structure2.setStatus("mandatory")


class _GnHptCfgTug3Structure3_Type(OctetString):
    """Custom type gnHptCfgTug3Structure3 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_GnHptCfgTug3Structure3_Type.__name__ = "OctetString"
_GnHptCfgTug3Structure3_Object = MibTableColumn
gnHptCfgTug3Structure3 = _GnHptCfgTug3Structure3_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 7, 1, 9),
    _GnHptCfgTug3Structure3_Type()
)
gnHptCfgTug3Structure3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnHptCfgTug3Structure3.setStatus("mandatory")


class _GnHptCfgSignalLabelMismatch_Type(Integer32):
    """Custom type gnHptCfgSignalLabelMismatch based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("sendAIS", 3),
          ("sendAlarm", 2))
    )


_GnHptCfgSignalLabelMismatch_Type.__name__ = "Integer32"
_GnHptCfgSignalLabelMismatch_Object = MibTableColumn
gnHptCfgSignalLabelMismatch = _GnHptCfgSignalLabelMismatch_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 7, 1, 10),
    _GnHptCfgSignalLabelMismatch_Type()
)
gnHptCfgSignalLabelMismatch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnHptCfgSignalLabelMismatch.setStatus("mandatory")


class _GnHptCfgTrailPT1_Type(OctetString):
    """Custom type gnHptCfgTrailPT1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_GnHptCfgTrailPT1_Type.__name__ = "OctetString"
_GnHptCfgTrailPT1_Object = MibTableColumn
gnHptCfgTrailPT1 = _GnHptCfgTrailPT1_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 7, 1, 11),
    _GnHptCfgTrailPT1_Type()
)
gnHptCfgTrailPT1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnHptCfgTrailPT1.setStatus("mandatory")


class _GnHptCfgTrailPT2_Type(OctetString):
    """Custom type gnHptCfgTrailPT2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_GnHptCfgTrailPT2_Type.__name__ = "OctetString"
_GnHptCfgTrailPT2_Object = MibTableColumn
gnHptCfgTrailPT2 = _GnHptCfgTrailPT2_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 7, 1, 12),
    _GnHptCfgTrailPT2_Type()
)
gnHptCfgTrailPT2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnHptCfgTrailPT2.setStatus("mandatory")


class _GnHptCfgTrailPT3_Type(OctetString):
    """Custom type gnHptCfgTrailPT3 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_GnHptCfgTrailPT3_Type.__name__ = "OctetString"
_GnHptCfgTrailPT3_Object = MibTableColumn
gnHptCfgTrailPT3 = _GnHptCfgTrailPT3_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 7, 1, 13),
    _GnHptCfgTrailPT3_Type()
)
gnHptCfgTrailPT3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnHptCfgTrailPT3.setStatus("mandatory")
_GnHptStatTable_Object = MibTable
gnHptStatTable = _GnHptStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 8)
)
if mibBuilder.loadTexts:
    gnHptStatTable.setStatus("mandatory")
_GnHptStatEntry_Object = MibTableRow
gnHptStatEntry = _GnHptStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 8, 1)
)
gnHptStatEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    gnHptStatEntry.setStatus("mandatory")


class _GnHptStatReceivedJ1_Type(DisplayString):
    """Custom type gnHptStatReceivedJ1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_GnHptStatReceivedJ1_Type.__name__ = "DisplayString"
_GnHptStatReceivedJ1_Object = MibTableColumn
gnHptStatReceivedJ1 = _GnHptStatReceivedJ1_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 8, 1, 1),
    _GnHptStatReceivedJ1_Type()
)
gnHptStatReceivedJ1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnHptStatReceivedJ1.setStatus("mandatory")


class _GnHptStatStatus_Type(OctetString):
    """Custom type gnHptStatStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_GnHptStatStatus_Type.__name__ = "OctetString"
_GnHptStatStatus_Object = MibTableColumn
gnHptStatStatus = _GnHptStatStatus_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 8, 1, 2),
    _GnHptStatStatus_Type()
)
gnHptStatStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnHptStatStatus.setStatus("mandatory")


class _GnHptStatCurrentBer_Type(Integer32):
    """Custom type gnHptStatCurrentBer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
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
        *(("tenExpMinus10", 9),
          ("tenExpMinus11", 10),
          ("tenExpMinus12", 11),
          ("tenExpMinus13", 12),
          ("tenExpMinus14", 13),
          ("tenExpMinus3", 2),
          ("tenExpMinus4", 3),
          ("tenExpMinus5", 4),
          ("tenExpMinus6", 5),
          ("tenExpMinus7", 6),
          ("tenExpMinus8", 7),
          ("tenExpMinus9", 8))
    )


_GnHptStatCurrentBer_Type.__name__ = "Integer32"
_GnHptStatCurrentBer_Object = MibTableColumn
gnHptStatCurrentBer = _GnHptStatCurrentBer_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 8, 1, 3),
    _GnHptStatCurrentBer_Type()
)
gnHptStatCurrentBer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnHptStatCurrentBer.setStatus("mandatory")


class _GnHptStatFarEndCurrentBer_Type(Integer32):
    """Custom type gnHptStatFarEndCurrentBer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
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
        *(("tenExpMinus10", 9),
          ("tenExpMinus11", 10),
          ("tenExpMinus12", 11),
          ("tenExpMinus13", 12),
          ("tenExpMinus14", 13),
          ("tenExpMinus3", 2),
          ("tenExpMinus4", 3),
          ("tenExpMinus5", 4),
          ("tenExpMinus6", 5),
          ("tenExpMinus7", 6),
          ("tenExpMinus8", 7),
          ("tenExpMinus9", 8))
    )


_GnHptStatFarEndCurrentBer_Type.__name__ = "Integer32"
_GnHptStatFarEndCurrentBer_Object = MibTableColumn
gnHptStatFarEndCurrentBer = _GnHptStatFarEndCurrentBer_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 8, 1, 4),
    _GnHptStatFarEndCurrentBer_Type()
)
gnHptStatFarEndCurrentBer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnHptStatFarEndCurrentBer.setStatus("mandatory")


class _GnHptStatReceivedSignalLabel_Type(OctetString):
    """Custom type gnHptStatReceivedSignalLabel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_GnHptStatReceivedSignalLabel_Type.__name__ = "OctetString"
_GnHptStatReceivedSignalLabel_Object = MibTableColumn
gnHptStatReceivedSignalLabel = _GnHptStatReceivedSignalLabel_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 8, 1, 5),
    _GnHptStatReceivedSignalLabel_Type()
)
gnHptStatReceivedSignalLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnHptStatReceivedSignalLabel.setStatus("mandatory")
_GnHptMon_ObjectIdentity = ObjectIdentity
gnHptMon = _GnHptMon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 9)
)
_GnHptMonCurrTable_Object = MibTable
gnHptMonCurrTable = _GnHptMonCurrTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 9, 1)
)
if mibBuilder.loadTexts:
    gnHptMonCurrTable.setStatus("mandatory")
_GnHptMonCurrEntry_Object = MibTableRow
gnHptMonCurrEntry = _GnHptMonCurrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 9, 1, 1)
)
gnHptMonCurrEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    gnHptMonCurrEntry.setStatus("mandatory")
_GnHptMonCurrBBE_Type = Gauge32
_GnHptMonCurrBBE_Object = MibTableColumn
gnHptMonCurrBBE = _GnHptMonCurrBBE_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 9, 1, 1, 1),
    _GnHptMonCurrBBE_Type()
)
gnHptMonCurrBBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnHptMonCurrBBE.setStatus("mandatory")
_GnHptMonCurrUAS_Type = Gauge32
_GnHptMonCurrUAS_Object = MibTableColumn
gnHptMonCurrUAS = _GnHptMonCurrUAS_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 9, 1, 1, 2),
    _GnHptMonCurrUAS_Type()
)
gnHptMonCurrUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnHptMonCurrUAS.setStatus("mandatory")
_GnHptMonCurrLastDayES_Type = Gauge32
_GnHptMonCurrLastDayES_Object = MibTableColumn
gnHptMonCurrLastDayES = _GnHptMonCurrLastDayES_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 9, 1, 1, 3),
    _GnHptMonCurrLastDayES_Type()
)
gnHptMonCurrLastDayES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnHptMonCurrLastDayES.setStatus("mandatory")
_GnHptMonCurrLastDaySES_Type = Gauge32
_GnHptMonCurrLastDaySES_Object = MibTableColumn
gnHptMonCurrLastDaySES = _GnHptMonCurrLastDaySES_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 9, 1, 1, 4),
    _GnHptMonCurrLastDaySES_Type()
)
gnHptMonCurrLastDaySES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnHptMonCurrLastDaySES.setStatus("mandatory")
_GnHptMonCurrLastDayBBE_Type = Gauge32
_GnHptMonCurrLastDayBBE_Object = MibTableColumn
gnHptMonCurrLastDayBBE = _GnHptMonCurrLastDayBBE_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 9, 1, 1, 5),
    _GnHptMonCurrLastDayBBE_Type()
)
gnHptMonCurrLastDayBBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnHptMonCurrLastDayBBE.setStatus("mandatory")
_GnHptMonCurrLastDayUAS_Type = Gauge32
_GnHptMonCurrLastDayUAS_Object = MibTableColumn
gnHptMonCurrLastDayUAS = _GnHptMonCurrLastDayUAS_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 9, 1, 1, 6),
    _GnHptMonCurrLastDayUAS_Type()
)
gnHptMonCurrLastDayUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnHptMonCurrLastDayUAS.setStatus("mandatory")
_GnHptMonIntervalTable_Object = MibTable
gnHptMonIntervalTable = _GnHptMonIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 9, 2)
)
if mibBuilder.loadTexts:
    gnHptMonIntervalTable.setStatus("mandatory")
_GnHptMonIntervalEntry_Object = MibTableRow
gnHptMonIntervalEntry = _GnHptMonIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 9, 2, 1)
)
gnHptMonIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CERAGON-MIB", "gnHptMonIntervalIdx"),
)
if mibBuilder.loadTexts:
    gnHptMonIntervalEntry.setStatus("mandatory")


class _GnHptMonIntervalIdx_Type(Integer32):
    """Custom type gnHptMonIntervalIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_GnHptMonIntervalIdx_Type.__name__ = "Integer32"
_GnHptMonIntervalIdx_Object = MibTableColumn
gnHptMonIntervalIdx = _GnHptMonIntervalIdx_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 9, 2, 1, 1),
    _GnHptMonIntervalIdx_Type()
)
gnHptMonIntervalIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnHptMonIntervalIdx.setStatus("mandatory")
_GnHptMonIntervalBBE_Type = Gauge32
_GnHptMonIntervalBBE_Object = MibTableColumn
gnHptMonIntervalBBE = _GnHptMonIntervalBBE_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 9, 2, 1, 2),
    _GnHptMonIntervalBBE_Type()
)
gnHptMonIntervalBBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnHptMonIntervalBBE.setStatus("mandatory")
_GnHptMonIntervalUAS_Type = Gauge32
_GnHptMonIntervalUAS_Object = MibTableColumn
gnHptMonIntervalUAS = _GnHptMonIntervalUAS_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 9, 2, 1, 3),
    _GnHptMonIntervalUAS_Type()
)
gnHptMonIntervalUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnHptMonIntervalUAS.setStatus("mandatory")
_GnHptMonDayTable_Object = MibTable
gnHptMonDayTable = _GnHptMonDayTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 9, 3)
)
if mibBuilder.loadTexts:
    gnHptMonDayTable.setStatus("mandatory")
_GnHptMonDayEntry_Object = MibTableRow
gnHptMonDayEntry = _GnHptMonDayEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 9, 3, 1)
)
gnHptMonDayEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CERAGON-MIB", "gnHptMonDayIdx"),
)
if mibBuilder.loadTexts:
    gnHptMonDayEntry.setStatus("mandatory")


class _GnHptMonDayIdx_Type(Integer32):
    """Custom type gnHptMonDayIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_GnHptMonDayIdx_Type.__name__ = "Integer32"
_GnHptMonDayIdx_Object = MibTableColumn
gnHptMonDayIdx = _GnHptMonDayIdx_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 9, 3, 1, 1),
    _GnHptMonDayIdx_Type()
)
gnHptMonDayIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnHptMonDayIdx.setStatus("mandatory")
_GnHptMonDayES_Type = Gauge32
_GnHptMonDayES_Object = MibTableColumn
gnHptMonDayES = _GnHptMonDayES_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 9, 3, 1, 2),
    _GnHptMonDayES_Type()
)
gnHptMonDayES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnHptMonDayES.setStatus("mandatory")
_GnHptMonDaySES_Type = Gauge32
_GnHptMonDaySES_Object = MibTableColumn
gnHptMonDaySES = _GnHptMonDaySES_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 9, 3, 1, 3),
    _GnHptMonDaySES_Type()
)
gnHptMonDaySES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnHptMonDaySES.setStatus("mandatory")
_GnHptMonDayBBE_Type = Gauge32
_GnHptMonDayBBE_Object = MibTableColumn
gnHptMonDayBBE = _GnHptMonDayBBE_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 9, 3, 1, 4),
    _GnHptMonDayBBE_Type()
)
gnHptMonDayBBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnHptMonDayBBE.setStatus("mandatory")
_GnHptMonDayUAS_Type = Gauge32
_GnHptMonDayUAS_Object = MibTableColumn
gnHptMonDayUAS = _GnHptMonDayUAS_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 9, 3, 1, 5),
    _GnHptMonDayUAS_Type()
)
gnHptMonDayUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnHptMonDayUAS.setStatus("mandatory")
_GnHptFarEndMonCurrTable_Object = MibTable
gnHptFarEndMonCurrTable = _GnHptFarEndMonCurrTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 9, 4)
)
if mibBuilder.loadTexts:
    gnHptFarEndMonCurrTable.setStatus("mandatory")
_GnHptFarEndMonCurrEntry_Object = MibTableRow
gnHptFarEndMonCurrEntry = _GnHptFarEndMonCurrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 9, 4, 1)
)
gnHptFarEndMonCurrEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    gnHptFarEndMonCurrEntry.setStatus("mandatory")
_GnHptFarEndMonCurrBBE_Type = Gauge32
_GnHptFarEndMonCurrBBE_Object = MibTableColumn
gnHptFarEndMonCurrBBE = _GnHptFarEndMonCurrBBE_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 9, 4, 1, 1),
    _GnHptFarEndMonCurrBBE_Type()
)
gnHptFarEndMonCurrBBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnHptFarEndMonCurrBBE.setStatus("mandatory")
_GnHptFarEndMonCurrUAS_Type = Gauge32
_GnHptFarEndMonCurrUAS_Object = MibTableColumn
gnHptFarEndMonCurrUAS = _GnHptFarEndMonCurrUAS_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 9, 4, 1, 2),
    _GnHptFarEndMonCurrUAS_Type()
)
gnHptFarEndMonCurrUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnHptFarEndMonCurrUAS.setStatus("mandatory")
_GnHptFarEndMonCurrLastDayES_Type = Gauge32
_GnHptFarEndMonCurrLastDayES_Object = MibTableColumn
gnHptFarEndMonCurrLastDayES = _GnHptFarEndMonCurrLastDayES_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 9, 4, 1, 3),
    _GnHptFarEndMonCurrLastDayES_Type()
)
gnHptFarEndMonCurrLastDayES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnHptFarEndMonCurrLastDayES.setStatus("mandatory")
_GnHptFarEndMonCurrLastDaySES_Type = Gauge32
_GnHptFarEndMonCurrLastDaySES_Object = MibTableColumn
gnHptFarEndMonCurrLastDaySES = _GnHptFarEndMonCurrLastDaySES_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 9, 4, 1, 4),
    _GnHptFarEndMonCurrLastDaySES_Type()
)
gnHptFarEndMonCurrLastDaySES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnHptFarEndMonCurrLastDaySES.setStatus("mandatory")
_GnHptFarEndMonCurrLastDayBBE_Type = Gauge32
_GnHptFarEndMonCurrLastDayBBE_Object = MibTableColumn
gnHptFarEndMonCurrLastDayBBE = _GnHptFarEndMonCurrLastDayBBE_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 9, 4, 1, 5),
    _GnHptFarEndMonCurrLastDayBBE_Type()
)
gnHptFarEndMonCurrLastDayBBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnHptFarEndMonCurrLastDayBBE.setStatus("mandatory")
_GnHptFarEndMonCurrLastDayUAS_Type = Gauge32
_GnHptFarEndMonCurrLastDayUAS_Object = MibTableColumn
gnHptFarEndMonCurrLastDayUAS = _GnHptFarEndMonCurrLastDayUAS_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 9, 4, 1, 6),
    _GnHptFarEndMonCurrLastDayUAS_Type()
)
gnHptFarEndMonCurrLastDayUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnHptFarEndMonCurrLastDayUAS.setStatus("mandatory")
_GnHptFarEndMonIntervalTable_Object = MibTable
gnHptFarEndMonIntervalTable = _GnHptFarEndMonIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 9, 5)
)
if mibBuilder.loadTexts:
    gnHptFarEndMonIntervalTable.setStatus("mandatory")
_GnHptFarEndMonIntervalEntry_Object = MibTableRow
gnHptFarEndMonIntervalEntry = _GnHptFarEndMonIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 9, 5, 1)
)
gnHptFarEndMonIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CERAGON-MIB", "gnHptFarEndMonIntervalIdx"),
)
if mibBuilder.loadTexts:
    gnHptFarEndMonIntervalEntry.setStatus("mandatory")


class _GnHptFarEndMonIntervalIdx_Type(Integer32):
    """Custom type gnHptFarEndMonIntervalIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_GnHptFarEndMonIntervalIdx_Type.__name__ = "Integer32"
_GnHptFarEndMonIntervalIdx_Object = MibTableColumn
gnHptFarEndMonIntervalIdx = _GnHptFarEndMonIntervalIdx_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 9, 5, 1, 1),
    _GnHptFarEndMonIntervalIdx_Type()
)
gnHptFarEndMonIntervalIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnHptFarEndMonIntervalIdx.setStatus("mandatory")
_GnHptFarEndMonIntervalBBE_Type = Gauge32
_GnHptFarEndMonIntervalBBE_Object = MibTableColumn
gnHptFarEndMonIntervalBBE = _GnHptFarEndMonIntervalBBE_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 9, 5, 1, 2),
    _GnHptFarEndMonIntervalBBE_Type()
)
gnHptFarEndMonIntervalBBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnHptFarEndMonIntervalBBE.setStatus("mandatory")
_GnHptFarEndMonIntervalUAS_Type = Gauge32
_GnHptFarEndMonIntervalUAS_Object = MibTableColumn
gnHptFarEndMonIntervalUAS = _GnHptFarEndMonIntervalUAS_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 9, 5, 1, 3),
    _GnHptFarEndMonIntervalUAS_Type()
)
gnHptFarEndMonIntervalUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnHptFarEndMonIntervalUAS.setStatus("mandatory")
_GnHptFarEndMonDayTable_Object = MibTable
gnHptFarEndMonDayTable = _GnHptFarEndMonDayTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 9, 6)
)
if mibBuilder.loadTexts:
    gnHptFarEndMonDayTable.setStatus("mandatory")
_GnHptFarEndMonDayEntry_Object = MibTableRow
gnHptFarEndMonDayEntry = _GnHptFarEndMonDayEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 9, 6, 1)
)
gnHptFarEndMonDayEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CERAGON-MIB", "gnHptFarEndMonDayIdx"),
)
if mibBuilder.loadTexts:
    gnHptFarEndMonDayEntry.setStatus("mandatory")


class _GnHptFarEndMonDayIdx_Type(Integer32):
    """Custom type gnHptFarEndMonDayIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_GnHptFarEndMonDayIdx_Type.__name__ = "Integer32"
_GnHptFarEndMonDayIdx_Object = MibTableColumn
gnHptFarEndMonDayIdx = _GnHptFarEndMonDayIdx_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 9, 6, 1, 1),
    _GnHptFarEndMonDayIdx_Type()
)
gnHptFarEndMonDayIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnHptFarEndMonDayIdx.setStatus("mandatory")
_GnHptFarEndMonDayES_Type = Gauge32
_GnHptFarEndMonDayES_Object = MibTableColumn
gnHptFarEndMonDayES = _GnHptFarEndMonDayES_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 9, 6, 1, 2),
    _GnHptFarEndMonDayES_Type()
)
gnHptFarEndMonDayES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnHptFarEndMonDayES.setStatus("mandatory")
_GnHptFarEndMonDaySES_Type = Gauge32
_GnHptFarEndMonDaySES_Object = MibTableColumn
gnHptFarEndMonDaySES = _GnHptFarEndMonDaySES_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 9, 6, 1, 3),
    _GnHptFarEndMonDaySES_Type()
)
gnHptFarEndMonDaySES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnHptFarEndMonDaySES.setStatus("mandatory")
_GnHptFarEndMonDayBBE_Type = Gauge32
_GnHptFarEndMonDayBBE_Object = MibTableColumn
gnHptFarEndMonDayBBE = _GnHptFarEndMonDayBBE_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 9, 6, 1, 4),
    _GnHptFarEndMonDayBBE_Type()
)
gnHptFarEndMonDayBBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnHptFarEndMonDayBBE.setStatus("mandatory")
_GnHptFarEndMonDayUAS_Type = Gauge32
_GnHptFarEndMonDayUAS_Object = MibTableColumn
gnHptFarEndMonDayUAS = _GnHptFarEndMonDayUAS_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 9, 6, 1, 5),
    _GnHptFarEndMonDayUAS_Type()
)
gnHptFarEndMonDayUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnHptFarEndMonDayUAS.setStatus("mandatory")
_GnLptCfgTable_Object = MibTable
gnLptCfgTable = _GnLptCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 10)
)
if mibBuilder.loadTexts:
    gnLptCfgTable.setStatus("mandatory")
_GnLptCfgEntry_Object = MibTableRow
gnLptCfgEntry = _GnLptCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 10, 1)
)
gnLptCfgEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    gnLptCfgEntry.setStatus("mandatory")


class _GnLptCfgEXCThresh_Type(Integer32):
    """Custom type gnLptCfgEXCThresh based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("tenExpMinus3", 2),
          ("tenExpMinus4", 3),
          ("tenExpMinus5", 4))
    )


_GnLptCfgEXCThresh_Type.__name__ = "Integer32"
_GnLptCfgEXCThresh_Object = MibTableColumn
gnLptCfgEXCThresh = _GnLptCfgEXCThresh_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 10, 1, 1),
    _GnLptCfgEXCThresh_Type()
)
gnLptCfgEXCThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnLptCfgEXCThresh.setStatus("mandatory")


class _GnLptCfgSDThresh_Type(Integer32):
    """Custom type gnLptCfgSDThresh based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5,
              6,
              15)
        )
    )
    namedValues = NamedValues(
        *(("notActive", 15),
          ("tenExpMinus6", 3),
          ("tenExpMinus7", 4),
          ("tenExpMinus8", 5),
          ("tenExpMinus9", 6))
    )


_GnLptCfgSDThresh_Type.__name__ = "Integer32"
_GnLptCfgSDThresh_Object = MibTableColumn
gnLptCfgSDThresh = _GnLptCfgSDThresh_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 10, 1, 2),
    _GnLptCfgSDThresh_Type()
)
gnLptCfgSDThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnLptCfgSDThresh.setStatus("mandatory")
_GnLptStatTable_Object = MibTable
gnLptStatTable = _GnLptStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 11)
)
if mibBuilder.loadTexts:
    gnLptStatTable.setStatus("mandatory")
_GnLptStatEntry_Object = MibTableRow
gnLptStatEntry = _GnLptStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 11, 1)
)
gnLptStatEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    gnLptStatEntry.setStatus("mandatory")


class _GnLptStatReceivedJ2_Type(DisplayString):
    """Custom type gnLptStatReceivedJ2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_GnLptStatReceivedJ2_Type.__name__ = "DisplayString"
_GnLptStatReceivedJ2_Object = MibTableColumn
gnLptStatReceivedJ2 = _GnLptStatReceivedJ2_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 11, 1, 1),
    _GnLptStatReceivedJ2_Type()
)
gnLptStatReceivedJ2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnLptStatReceivedJ2.setStatus("mandatory")


class _GnLptStatStatus_Type(OctetString):
    """Custom type gnLptStatStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_GnLptStatStatus_Type.__name__ = "OctetString"
_GnLptStatStatus_Object = MibTableColumn
gnLptStatStatus = _GnLptStatStatus_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 11, 1, 2),
    _GnLptStatStatus_Type()
)
gnLptStatStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnLptStatStatus.setStatus("mandatory")


class _GnLptStatProtectionMode_Type(Integer32):
    """Custom type gnLptStatProtectionMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("notActive", 5),
          ("passthrough", 4),
          ("protect", 3),
          ("working", 2))
    )


_GnLptStatProtectionMode_Type.__name__ = "Integer32"
_GnLptStatProtectionMode_Object = MibTableColumn
gnLptStatProtectionMode = _GnLptStatProtectionMode_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 11, 1, 3),
    _GnLptStatProtectionMode_Type()
)
gnLptStatProtectionMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnLptStatProtectionMode.setStatus("mandatory")


class _GnLptStatCurrentBer_Type(Integer32):
    """Custom type gnLptStatCurrentBer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
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
        *(("tenExpMinus10", 9),
          ("tenExpMinus11", 10),
          ("tenExpMinus12", 11),
          ("tenExpMinus13", 12),
          ("tenExpMinus14", 13),
          ("tenExpMinus3", 2),
          ("tenExpMinus4", 3),
          ("tenExpMinus5", 4),
          ("tenExpMinus6", 5),
          ("tenExpMinus7", 6),
          ("tenExpMinus8", 7),
          ("tenExpMinus9", 8))
    )


_GnLptStatCurrentBer_Type.__name__ = "Integer32"
_GnLptStatCurrentBer_Object = MibTableColumn
gnLptStatCurrentBer = _GnLptStatCurrentBer_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 11, 1, 4),
    _GnLptStatCurrentBer_Type()
)
gnLptStatCurrentBer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnLptStatCurrentBer.setStatus("mandatory")


class _GnLptStatFarEndCurrentBer_Type(Integer32):
    """Custom type gnLptStatFarEndCurrentBer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
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
        *(("tenExpMinus10", 9),
          ("tenExpMinus11", 10),
          ("tenExpMinus12", 11),
          ("tenExpMinus13", 12),
          ("tenExpMinus14", 13),
          ("tenExpMinus3", 2),
          ("tenExpMinus4", 3),
          ("tenExpMinus5", 4),
          ("tenExpMinus6", 5),
          ("tenExpMinus7", 6),
          ("tenExpMinus8", 7),
          ("tenExpMinus9", 8))
    )


_GnLptStatFarEndCurrentBer_Type.__name__ = "Integer32"
_GnLptStatFarEndCurrentBer_Object = MibTableColumn
gnLptStatFarEndCurrentBer = _GnLptStatFarEndCurrentBer_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 11, 1, 5),
    _GnLptStatFarEndCurrentBer_Type()
)
gnLptStatFarEndCurrentBer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnLptStatFarEndCurrentBer.setStatus("mandatory")


class _GnLptStatReceivedSignalLabel_Type(OctetString):
    """Custom type gnLptStatReceivedSignalLabel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_GnLptStatReceivedSignalLabel_Type.__name__ = "OctetString"
_GnLptStatReceivedSignalLabel_Object = MibTableColumn
gnLptStatReceivedSignalLabel = _GnLptStatReceivedSignalLabel_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 11, 1, 6),
    _GnLptStatReceivedSignalLabel_Type()
)
gnLptStatReceivedSignalLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnLptStatReceivedSignalLabel.setStatus("mandatory")
_GnLptStatKLM_Type = Integer32
_GnLptStatKLM_Object = MibTableColumn
gnLptStatKLM = _GnLptStatKLM_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 11, 1, 7),
    _GnLptStatKLM_Type()
)
gnLptStatKLM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnLptStatKLM.setStatus("mandatory")
_GnLptMon_ObjectIdentity = ObjectIdentity
gnLptMon = _GnLptMon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 12)
)
_GnLptMonCurrTable_Object = MibTable
gnLptMonCurrTable = _GnLptMonCurrTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 12, 1)
)
if mibBuilder.loadTexts:
    gnLptMonCurrTable.setStatus("mandatory")
_GnLptMonCurrEntry_Object = MibTableRow
gnLptMonCurrEntry = _GnLptMonCurrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 12, 1, 1)
)
gnLptMonCurrEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    gnLptMonCurrEntry.setStatus("mandatory")
_GnLptMonCurrBBE_Type = Gauge32
_GnLptMonCurrBBE_Object = MibTableColumn
gnLptMonCurrBBE = _GnLptMonCurrBBE_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 12, 1, 1, 1),
    _GnLptMonCurrBBE_Type()
)
gnLptMonCurrBBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnLptMonCurrBBE.setStatus("mandatory")
_GnLptMonCurrUAS_Type = Gauge32
_GnLptMonCurrUAS_Object = MibTableColumn
gnLptMonCurrUAS = _GnLptMonCurrUAS_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 12, 1, 1, 2),
    _GnLptMonCurrUAS_Type()
)
gnLptMonCurrUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnLptMonCurrUAS.setStatus("mandatory")
_GnLptMonCurrLastDayES_Type = Gauge32
_GnLptMonCurrLastDayES_Object = MibTableColumn
gnLptMonCurrLastDayES = _GnLptMonCurrLastDayES_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 12, 1, 1, 3),
    _GnLptMonCurrLastDayES_Type()
)
gnLptMonCurrLastDayES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnLptMonCurrLastDayES.setStatus("mandatory")
_GnLptMonCurrLastDaySES_Type = Gauge32
_GnLptMonCurrLastDaySES_Object = MibTableColumn
gnLptMonCurrLastDaySES = _GnLptMonCurrLastDaySES_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 12, 1, 1, 4),
    _GnLptMonCurrLastDaySES_Type()
)
gnLptMonCurrLastDaySES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnLptMonCurrLastDaySES.setStatus("mandatory")
_GnLptMonCurrLastDayBBE_Type = Gauge32
_GnLptMonCurrLastDayBBE_Object = MibTableColumn
gnLptMonCurrLastDayBBE = _GnLptMonCurrLastDayBBE_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 12, 1, 1, 5),
    _GnLptMonCurrLastDayBBE_Type()
)
gnLptMonCurrLastDayBBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnLptMonCurrLastDayBBE.setStatus("mandatory")
_GnLptMonCurrLastDayUAS_Type = Gauge32
_GnLptMonCurrLastDayUAS_Object = MibTableColumn
gnLptMonCurrLastDayUAS = _GnLptMonCurrLastDayUAS_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 12, 1, 1, 6),
    _GnLptMonCurrLastDayUAS_Type()
)
gnLptMonCurrLastDayUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnLptMonCurrLastDayUAS.setStatus("mandatory")
_GnLptMonIntervalTable_Object = MibTable
gnLptMonIntervalTable = _GnLptMonIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 12, 2)
)
if mibBuilder.loadTexts:
    gnLptMonIntervalTable.setStatus("mandatory")
_GnLptMonIntervalEntry_Object = MibTableRow
gnLptMonIntervalEntry = _GnLptMonIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 12, 2, 1)
)
gnLptMonIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CERAGON-MIB", "gnLptMonIntervalIdx"),
)
if mibBuilder.loadTexts:
    gnLptMonIntervalEntry.setStatus("mandatory")


class _GnLptMonIntervalIdx_Type(Integer32):
    """Custom type gnLptMonIntervalIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_GnLptMonIntervalIdx_Type.__name__ = "Integer32"
_GnLptMonIntervalIdx_Object = MibTableColumn
gnLptMonIntervalIdx = _GnLptMonIntervalIdx_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 12, 2, 1, 1),
    _GnLptMonIntervalIdx_Type()
)
gnLptMonIntervalIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnLptMonIntervalIdx.setStatus("mandatory")
_GnLptMonIntervalBBE_Type = Gauge32
_GnLptMonIntervalBBE_Object = MibTableColumn
gnLptMonIntervalBBE = _GnLptMonIntervalBBE_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 12, 2, 1, 2),
    _GnLptMonIntervalBBE_Type()
)
gnLptMonIntervalBBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnLptMonIntervalBBE.setStatus("mandatory")
_GnLptMonIntervalUAS_Type = Gauge32
_GnLptMonIntervalUAS_Object = MibTableColumn
gnLptMonIntervalUAS = _GnLptMonIntervalUAS_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 12, 2, 1, 3),
    _GnLptMonIntervalUAS_Type()
)
gnLptMonIntervalUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnLptMonIntervalUAS.setStatus("mandatory")
_GnLptMonDayTable_Object = MibTable
gnLptMonDayTable = _GnLptMonDayTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 12, 3)
)
if mibBuilder.loadTexts:
    gnLptMonDayTable.setStatus("mandatory")
_GnLptMonDayEntry_Object = MibTableRow
gnLptMonDayEntry = _GnLptMonDayEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 12, 3, 1)
)
gnLptMonDayEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CERAGON-MIB", "gnLptMonDayIdx"),
)
if mibBuilder.loadTexts:
    gnLptMonDayEntry.setStatus("mandatory")


class _GnLptMonDayIdx_Type(Integer32):
    """Custom type gnLptMonDayIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_GnLptMonDayIdx_Type.__name__ = "Integer32"
_GnLptMonDayIdx_Object = MibTableColumn
gnLptMonDayIdx = _GnLptMonDayIdx_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 12, 3, 1, 1),
    _GnLptMonDayIdx_Type()
)
gnLptMonDayIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnLptMonDayIdx.setStatus("mandatory")
_GnLptMonDayES_Type = Gauge32
_GnLptMonDayES_Object = MibTableColumn
gnLptMonDayES = _GnLptMonDayES_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 12, 3, 1, 2),
    _GnLptMonDayES_Type()
)
gnLptMonDayES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnLptMonDayES.setStatus("mandatory")
_GnLptMonDaySES_Type = Gauge32
_GnLptMonDaySES_Object = MibTableColumn
gnLptMonDaySES = _GnLptMonDaySES_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 12, 3, 1, 3),
    _GnLptMonDaySES_Type()
)
gnLptMonDaySES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnLptMonDaySES.setStatus("mandatory")
_GnLptMonDayBBE_Type = Gauge32
_GnLptMonDayBBE_Object = MibTableColumn
gnLptMonDayBBE = _GnLptMonDayBBE_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 12, 3, 1, 4),
    _GnLptMonDayBBE_Type()
)
gnLptMonDayBBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnLptMonDayBBE.setStatus("mandatory")
_GnLptMonDayUAS_Type = Gauge32
_GnLptMonDayUAS_Object = MibTableColumn
gnLptMonDayUAS = _GnLptMonDayUAS_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 12, 3, 1, 5),
    _GnLptMonDayUAS_Type()
)
gnLptMonDayUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnLptMonDayUAS.setStatus("mandatory")
_GnLptFarEndMonCurrTable_Object = MibTable
gnLptFarEndMonCurrTable = _GnLptFarEndMonCurrTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 12, 4)
)
if mibBuilder.loadTexts:
    gnLptFarEndMonCurrTable.setStatus("mandatory")
_GnLptFarEndMonCurrEntry_Object = MibTableRow
gnLptFarEndMonCurrEntry = _GnLptFarEndMonCurrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 12, 4, 1)
)
gnLptFarEndMonCurrEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    gnLptFarEndMonCurrEntry.setStatus("mandatory")
_GnLptFarEndMonCurrBBE_Type = Gauge32
_GnLptFarEndMonCurrBBE_Object = MibTableColumn
gnLptFarEndMonCurrBBE = _GnLptFarEndMonCurrBBE_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 12, 4, 1, 1),
    _GnLptFarEndMonCurrBBE_Type()
)
gnLptFarEndMonCurrBBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnLptFarEndMonCurrBBE.setStatus("mandatory")
_GnLptFarEndMonCurrUAS_Type = Gauge32
_GnLptFarEndMonCurrUAS_Object = MibTableColumn
gnLptFarEndMonCurrUAS = _GnLptFarEndMonCurrUAS_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 12, 4, 1, 2),
    _GnLptFarEndMonCurrUAS_Type()
)
gnLptFarEndMonCurrUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnLptFarEndMonCurrUAS.setStatus("mandatory")
_GnLptFarEndMonCurrLastDayES_Type = Gauge32
_GnLptFarEndMonCurrLastDayES_Object = MibTableColumn
gnLptFarEndMonCurrLastDayES = _GnLptFarEndMonCurrLastDayES_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 12, 4, 1, 3),
    _GnLptFarEndMonCurrLastDayES_Type()
)
gnLptFarEndMonCurrLastDayES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnLptFarEndMonCurrLastDayES.setStatus("mandatory")
_GnLptFarEndMonCurrLastDaySES_Type = Gauge32
_GnLptFarEndMonCurrLastDaySES_Object = MibTableColumn
gnLptFarEndMonCurrLastDaySES = _GnLptFarEndMonCurrLastDaySES_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 12, 4, 1, 4),
    _GnLptFarEndMonCurrLastDaySES_Type()
)
gnLptFarEndMonCurrLastDaySES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnLptFarEndMonCurrLastDaySES.setStatus("mandatory")
_GnLptFarEndMonCurrLastDayBBE_Type = Gauge32
_GnLptFarEndMonCurrLastDayBBE_Object = MibTableColumn
gnLptFarEndMonCurrLastDayBBE = _GnLptFarEndMonCurrLastDayBBE_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 12, 4, 1, 5),
    _GnLptFarEndMonCurrLastDayBBE_Type()
)
gnLptFarEndMonCurrLastDayBBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnLptFarEndMonCurrLastDayBBE.setStatus("mandatory")
_GnLptFarEndMonCurrLastDayUAS_Type = Gauge32
_GnLptFarEndMonCurrLastDayUAS_Object = MibTableColumn
gnLptFarEndMonCurrLastDayUAS = _GnLptFarEndMonCurrLastDayUAS_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 12, 4, 1, 6),
    _GnLptFarEndMonCurrLastDayUAS_Type()
)
gnLptFarEndMonCurrLastDayUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnLptFarEndMonCurrLastDayUAS.setStatus("mandatory")
_GnLptFarEndMonIntervalTable_Object = MibTable
gnLptFarEndMonIntervalTable = _GnLptFarEndMonIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 12, 5)
)
if mibBuilder.loadTexts:
    gnLptFarEndMonIntervalTable.setStatus("mandatory")
_GnLptFarEndMonIntervalEntry_Object = MibTableRow
gnLptFarEndMonIntervalEntry = _GnLptFarEndMonIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 12, 5, 1)
)
gnLptFarEndMonIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CERAGON-MIB", "gnLptFarEndMonIntervalIdx"),
)
if mibBuilder.loadTexts:
    gnLptFarEndMonIntervalEntry.setStatus("mandatory")


class _GnLptFarEndMonIntervalIdx_Type(Integer32):
    """Custom type gnLptFarEndMonIntervalIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_GnLptFarEndMonIntervalIdx_Type.__name__ = "Integer32"
_GnLptFarEndMonIntervalIdx_Object = MibTableColumn
gnLptFarEndMonIntervalIdx = _GnLptFarEndMonIntervalIdx_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 12, 5, 1, 1),
    _GnLptFarEndMonIntervalIdx_Type()
)
gnLptFarEndMonIntervalIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnLptFarEndMonIntervalIdx.setStatus("mandatory")
_GnLptFarEndMonIntervalBBE_Type = Gauge32
_GnLptFarEndMonIntervalBBE_Object = MibTableColumn
gnLptFarEndMonIntervalBBE = _GnLptFarEndMonIntervalBBE_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 12, 5, 1, 2),
    _GnLptFarEndMonIntervalBBE_Type()
)
gnLptFarEndMonIntervalBBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnLptFarEndMonIntervalBBE.setStatus("mandatory")
_GnLptFarEndMonIntervalUAS_Type = Gauge32
_GnLptFarEndMonIntervalUAS_Object = MibTableColumn
gnLptFarEndMonIntervalUAS = _GnLptFarEndMonIntervalUAS_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 12, 5, 1, 3),
    _GnLptFarEndMonIntervalUAS_Type()
)
gnLptFarEndMonIntervalUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnLptFarEndMonIntervalUAS.setStatus("mandatory")
_GnLptFarEndMonDayTable_Object = MibTable
gnLptFarEndMonDayTable = _GnLptFarEndMonDayTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 12, 6)
)
if mibBuilder.loadTexts:
    gnLptFarEndMonDayTable.setStatus("mandatory")
_GnLptFarEndMonDayEntry_Object = MibTableRow
gnLptFarEndMonDayEntry = _GnLptFarEndMonDayEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 12, 6, 1)
)
gnLptFarEndMonDayEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CERAGON-MIB", "gnLptFarEndMonDayIdx"),
)
if mibBuilder.loadTexts:
    gnLptFarEndMonDayEntry.setStatus("mandatory")


class _GnLptFarEndMonDayIdx_Type(Integer32):
    """Custom type gnLptFarEndMonDayIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_GnLptFarEndMonDayIdx_Type.__name__ = "Integer32"
_GnLptFarEndMonDayIdx_Object = MibTableColumn
gnLptFarEndMonDayIdx = _GnLptFarEndMonDayIdx_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 12, 6, 1, 1),
    _GnLptFarEndMonDayIdx_Type()
)
gnLptFarEndMonDayIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnLptFarEndMonDayIdx.setStatus("mandatory")
_GnLptFarEndMonDayES_Type = Gauge32
_GnLptFarEndMonDayES_Object = MibTableColumn
gnLptFarEndMonDayES = _GnLptFarEndMonDayES_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 12, 6, 1, 2),
    _GnLptFarEndMonDayES_Type()
)
gnLptFarEndMonDayES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnLptFarEndMonDayES.setStatus("mandatory")
_GnLptFarEndMonDaySES_Type = Gauge32
_GnLptFarEndMonDaySES_Object = MibTableColumn
gnLptFarEndMonDaySES = _GnLptFarEndMonDaySES_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 12, 6, 1, 3),
    _GnLptFarEndMonDaySES_Type()
)
gnLptFarEndMonDaySES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnLptFarEndMonDaySES.setStatus("mandatory")
_GnLptFarEndMonDayBBE_Type = Gauge32
_GnLptFarEndMonDayBBE_Object = MibTableColumn
gnLptFarEndMonDayBBE = _GnLptFarEndMonDayBBE_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 12, 6, 1, 4),
    _GnLptFarEndMonDayBBE_Type()
)
gnLptFarEndMonDayBBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnLptFarEndMonDayBBE.setStatus("mandatory")
_GnLptFarEndMonDayUAS_Type = Gauge32
_GnLptFarEndMonDayUAS_Object = MibTableColumn
gnLptFarEndMonDayUAS = _GnLptFarEndMonDayUAS_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 12, 6, 1, 5),
    _GnLptFarEndMonDayUAS_Type()
)
gnLptFarEndMonDayUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnLptFarEndMonDayUAS.setStatus("mandatory")
_GnMuxCfgXTable_Object = MibTable
gnMuxCfgXTable = _GnMuxCfgXTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 13)
)
if mibBuilder.loadTexts:
    gnMuxCfgXTable.setStatus("mandatory")
_GnMuxCfgXEntry_Object = MibTableRow
gnMuxCfgXEntry = _GnMuxCfgXEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 13, 1)
)
gnMuxCfgXEntry.setIndexNames(
    (0, "CERAGON-MIB", "gnMuxCfgXId"),
)
if mibBuilder.loadTexts:
    gnMuxCfgXEntry.setStatus("mandatory")


class _GnMuxCfgXId_Type(Integer32):
    """Custom type gnMuxCfgXId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("mux1", 3),
          ("mux2", 4))
    )


_GnMuxCfgXId_Type.__name__ = "Integer32"
_GnMuxCfgXId_Object = MibTableColumn
gnMuxCfgXId = _GnMuxCfgXId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 13, 1, 1),
    _GnMuxCfgXId_Type()
)
gnMuxCfgXId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnMuxCfgXId.setStatus("mandatory")


class _GnMuxCfgXWsAdmin_Type(Integer32):
    """Custom type gnMuxCfgXWsAdmin based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("enable", 2))
    )


_GnMuxCfgXWsAdmin_Type.__name__ = "Integer32"
_GnMuxCfgXWsAdmin_Object = MibTableColumn
gnMuxCfgXWsAdmin = _GnMuxCfgXWsAdmin_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 13, 1, 2),
    _GnMuxCfgXWsAdmin_Type()
)
gnMuxCfgXWsAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnMuxCfgXWsAdmin.setStatus("mandatory")


class _GnMuxCfgXWsLoopback_Type(Integer32):
    """Custom type gnMuxCfgXWsLoopback based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noloopback", 2),
          ("waySideLoop", 3))
    )


_GnMuxCfgXWsLoopback_Type.__name__ = "Integer32"
_GnMuxCfgXWsLoopback_Object = MibTableColumn
gnMuxCfgXWsLoopback = _GnMuxCfgXWsLoopback_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 13, 1, 3),
    _GnMuxCfgXWsLoopback_Type()
)
gnMuxCfgXWsLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnMuxCfgXWsLoopback.setStatus("mandatory")


class _GnMuxCfgXHwReset_Type(Integer32):
    """Custom type gnMuxCfgXHwReset based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hwReset", 3),
          ("noOperation", 2))
    )


_GnMuxCfgXHwReset_Type.__name__ = "Integer32"
_GnMuxCfgXHwReset_Object = MibTableColumn
gnMuxCfgXHwReset = _GnMuxCfgXHwReset_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 13, 1, 4),
    _GnMuxCfgXHwReset_Type()
)
gnMuxCfgXHwReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnMuxCfgXHwReset.setStatus("mandatory")


class _GnMUXCfgXTempLicenseEnable_Type(Integer32):
    """Custom type gnMUXCfgXTempLicenseEnable based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("enable", 2),
          ("notSupported", 4))
    )


_GnMUXCfgXTempLicenseEnable_Type.__name__ = "Integer32"
_GnMUXCfgXTempLicenseEnable_Object = MibTableColumn
gnMUXCfgXTempLicenseEnable = _GnMUXCfgXTempLicenseEnable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 13, 1, 5),
    _GnMUXCfgXTempLicenseEnable_Type()
)
gnMUXCfgXTempLicenseEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnMUXCfgXTempLicenseEnable.setStatus("mandatory")


class _GnMUXCfgXTempLicenseTimer_Type(Integer32):
    """Custom type gnMUXCfgXTempLicenseTimer based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_GnMUXCfgXTempLicenseTimer_Type.__name__ = "Integer32"
_GnMUXCfgXTempLicenseTimer_Object = MibTableColumn
gnMUXCfgXTempLicenseTimer = _GnMUXCfgXTempLicenseTimer_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 13, 1, 6),
    _GnMUXCfgXTempLicenseTimer_Type()
)
gnMUXCfgXTempLicenseTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnMUXCfgXTempLicenseTimer.setStatus("mandatory")
_GnMuxStatXTable_Object = MibTable
gnMuxStatXTable = _GnMuxStatXTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 14)
)
if mibBuilder.loadTexts:
    gnMuxStatXTable.setStatus("mandatory")
_GnMuxStatXEntry_Object = MibTableRow
gnMuxStatXEntry = _GnMuxStatXEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 14, 1)
)
gnMuxStatXEntry.setIndexNames(
    (0, "CERAGON-MIB", "gnMuxStatXId"),
)
if mibBuilder.loadTexts:
    gnMuxStatXEntry.setStatus("mandatory")


class _GnMuxStatXId_Type(Integer32):
    """Custom type gnMuxStatXId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("mux1", 3),
          ("mux2", 4))
    )


_GnMuxStatXId_Type.__name__ = "Integer32"
_GnMuxStatXId_Object = MibTableColumn
gnMuxStatXId = _GnMuxStatXId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 14, 1, 1),
    _GnMuxStatXId_Type()
)
gnMuxStatXId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnMuxStatXId.setStatus("mandatory")


class _GnMuxStatXMuxSerialNumber_Type(DisplayString):
    """Custom type gnMuxStatXMuxSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_GnMuxStatXMuxSerialNumber_Type.__name__ = "DisplayString"
_GnMuxStatXMuxSerialNumber_Object = MibTableColumn
gnMuxStatXMuxSerialNumber = _GnMuxStatXMuxSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 14, 1, 2),
    _GnMuxStatXMuxSerialNumber_Type()
)
gnMuxStatXMuxSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnMuxStatXMuxSerialNumber.setStatus("mandatory")


class _GnMuxStatXIfLeds_Type(OctetString):
    """Custom type gnMuxStatXIfLeds based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_GnMuxStatXIfLeds_Type.__name__ = "OctetString"
_GnMuxStatXIfLeds_Object = MibTableColumn
gnMuxStatXIfLeds = _GnMuxStatXIfLeds_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 14, 1, 3),
    _GnMuxStatXIfLeds_Type()
)
gnMuxStatXIfLeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnMuxStatXIfLeds.setStatus("mandatory")


class _GnMuxStatXNumOfIfOnClass1_Type(Integer32):
    """Custom type gnMuxStatXNumOfIfOnClass1 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_GnMuxStatXNumOfIfOnClass1_Type.__name__ = "Integer32"
_GnMuxStatXNumOfIfOnClass1_Object = MibTableColumn
gnMuxStatXNumOfIfOnClass1 = _GnMuxStatXNumOfIfOnClass1_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 14, 1, 4),
    _GnMuxStatXNumOfIfOnClass1_Type()
)
gnMuxStatXNumOfIfOnClass1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnMuxStatXNumOfIfOnClass1.setStatus("mandatory")


class _GnMuxStatXNumOfIfOnClass2_Type(Integer32):
    """Custom type gnMuxStatXNumOfIfOnClass2 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_GnMuxStatXNumOfIfOnClass2_Type.__name__ = "Integer32"
_GnMuxStatXNumOfIfOnClass2_Object = MibTableColumn
gnMuxStatXNumOfIfOnClass2 = _GnMuxStatXNumOfIfOnClass2_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 14, 1, 5),
    _GnMuxStatXNumOfIfOnClass2_Type()
)
gnMuxStatXNumOfIfOnClass2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnMuxStatXNumOfIfOnClass2.setStatus("mandatory")


class _GnMuxStatXNumOfIfOnClass3_Type(Integer32):
    """Custom type gnMuxStatXNumOfIfOnClass3 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_GnMuxStatXNumOfIfOnClass3_Type.__name__ = "Integer32"
_GnMuxStatXNumOfIfOnClass3_Object = MibTableColumn
gnMuxStatXNumOfIfOnClass3 = _GnMuxStatXNumOfIfOnClass3_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 14, 1, 6),
    _GnMuxStatXNumOfIfOnClass3_Type()
)
gnMuxStatXNumOfIfOnClass3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnMuxStatXNumOfIfOnClass3.setStatus("mandatory")


class _GnMuxStatXAesAdmin_Type(Integer32):
    """Custom type gnMuxStatXAesAdmin based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("enable", 2),
          ("notSupport", 4),
          ("systemFailure", 5))
    )


_GnMuxStatXAesAdmin_Type.__name__ = "Integer32"
_GnMuxStatXAesAdmin_Object = MibTableColumn
gnMuxStatXAesAdmin = _GnMuxStatXAesAdmin_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 14, 1, 7),
    _GnMuxStatXAesAdmin_Type()
)
gnMuxStatXAesAdmin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnMuxStatXAesAdmin.setStatus("mandatory")


class _GnMuxStatXMuxFWVer_Type(DisplayString):
    """Custom type gnMuxStatXMuxFWVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_GnMuxStatXMuxFWVer_Type.__name__ = "DisplayString"
_GnMuxStatXMuxFWVer_Object = MibTableColumn
gnMuxStatXMuxFWVer = _GnMuxStatXMuxFWVer_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 14, 1, 8),
    _GnMuxStatXMuxFWVer_Type()
)
gnMuxStatXMuxFWVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnMuxStatXMuxFWVer.setStatus("mandatory")


class _GnMuxStatXMuxFWPostVer_Type(DisplayString):
    """Custom type gnMuxStatXMuxFWPostVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_GnMuxStatXMuxFWPostVer_Type.__name__ = "DisplayString"
_GnMuxStatXMuxFWPostVer_Object = MibTableColumn
gnMuxStatXMuxFWPostVer = _GnMuxStatXMuxFWPostVer_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 14, 1, 9),
    _GnMuxStatXMuxFWPostVer_Type()
)
gnMuxStatXMuxFWPostVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnMuxStatXMuxFWPostVer.setStatus("mandatory")


class _GnMuxStatXBoardConnector_Type(Integer32):
    """Custom type gnMuxStatXBoardConnector based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
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
        *(("eightE1Only", 31),
          ("eightT1Only", 32),
          ("noInterface", 2),
          ("oneDS3", 19),
          ("oneE3", 21),
          ("oneElectricalGBEOnly", 26),
          ("oneElectricalGBEPlus8E1", 27),
          ("oneElectricalGBEPlus8T1", 28),
          ("oneElectricalSTM1", 3),
          ("oneFEOnly", 9),
          ("oneFEplus4E1", 10),
          ("oneFEplus4T1", 12),
          ("oneFEplus64E1", 29),
          ("oneFEplus64T1", 30),
          ("oneFEplus8E1", 11),
          ("oneFEplus8T1", 13),
          ("oneFiberSTM1MultiMode", 5),
          ("oneFiberSTM1SingleMode", 4),
          ("oneOpticalGBEOnly", 23),
          ("oneOpticalGBEPlus8E1", 24),
          ("oneOpticalGBEPlus8T1", 25),
          ("oneStm1XC", 33),
          ("threeDS3", 20),
          ("threeE3", 22),
          ("twoElectricalSTM1", 6),
          ("twoFEOnly", 14),
          ("twoFEplus4E1", 15),
          ("twoFEplus4T1", 17),
          ("twoFEplus8E1", 16),
          ("twoFEplus8T1", 18),
          ("twoFiberSTM1MultiMode", 8),
          ("twoFiberSTM1SingleMode", 7),
          ("twoStm1XC", 34))
    )


_GnMuxStatXBoardConnector_Type.__name__ = "Integer32"
_GnMuxStatXBoardConnector_Object = MibTableColumn
gnMuxStatXBoardConnector = _GnMuxStatXBoardConnector_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 14, 1, 10),
    _GnMuxStatXBoardConnector_Type()
)
gnMuxStatXBoardConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnMuxStatXBoardConnector.setStatus("mandatory")


class _GnMuxStatXBoardType_Type(Integer32):
    """Custom type gnMuxStatXBoardType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("v1", 2),
          ("v2", 3),
          ("v3", 4),
          ("v4", 5),
          ("v5", 6),
          ("v6", 7))
    )


_GnMuxStatXBoardType_Type.__name__ = "Integer32"
_GnMuxStatXBoardType_Object = MibTableColumn
gnMuxStatXBoardType = _GnMuxStatXBoardType_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 3, 14, 1, 11),
    _GnMuxStatXBoardType_Type()
)
gnMuxStatXBoardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnMuxStatXBoardType.setStatus("mandatory")
_GnAux_ObjectIdentity = ObjectIdentity
gnAux = _GnAux_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 4)
)
_GnAuxGeneral_ObjectIdentity = ObjectIdentity
gnAuxGeneral = _GnAuxGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 4, 1)
)
_GnAuxGeneralTable_Object = MibTable
gnAuxGeneralTable = _GnAuxGeneralTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 4, 1, 1)
)
if mibBuilder.loadTexts:
    gnAuxGeneralTable.setStatus("mandatory")
_GnAuxGeneralEntry_Object = MibTableRow
gnAuxGeneralEntry = _GnAuxGeneralEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 4, 1, 1, 1)
)
gnAuxGeneralEntry.setIndexNames(
    (0, "CERAGON-MIB", "gnAuxGeneralId"),
)
if mibBuilder.loadTexts:
    gnAuxGeneralEntry.setStatus("mandatory")


class _GnAuxGeneralId_Type(Integer32):
    """Custom type gnAuxGeneralId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("local", 1)
    )


_GnAuxGeneralId_Type.__name__ = "Integer32"
_GnAuxGeneralId_Object = MibTableColumn
gnAuxGeneralId = _GnAuxGeneralId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 4, 1, 1, 1, 1),
    _GnAuxGeneralId_Type()
)
gnAuxGeneralId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnAuxGeneralId.setStatus("mandatory")


class _GnAuxGeneralSyncIdcDataBase_Type(Integer32):
    """Custom type gnAuxGeneralSyncIdcDataBase based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("auxToIdc", 3),
          ("idcToAux", 4),
          ("noOperation", 2))
    )


_GnAuxGeneralSyncIdcDataBase_Type.__name__ = "Integer32"
_GnAuxGeneralSyncIdcDataBase_Object = MibTableColumn
gnAuxGeneralSyncIdcDataBase = _GnAuxGeneralSyncIdcDataBase_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 4, 1, 1, 1, 2),
    _GnAuxGeneralSyncIdcDataBase_Type()
)
gnAuxGeneralSyncIdcDataBase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnAuxGeneralSyncIdcDataBase.setStatus("mandatory")
_GnWsc_ObjectIdentity = ObjectIdentity
gnWsc = _GnWsc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 4, 2)
)
_GnWscCfgTable_Object = MibTable
gnWscCfgTable = _GnWscCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 4, 2, 1)
)
if mibBuilder.loadTexts:
    gnWscCfgTable.setStatus("mandatory")
_GnWscCfgEntry_Object = MibTableRow
gnWscCfgEntry = _GnWscCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 4, 2, 1, 1)
)
gnWscCfgEntry.setIndexNames(
    (0, "CERAGON-MIB", "gnWscCfgId"),
    (0, "CERAGON-MIB", "gnWscCfgChNumber"),
)
if mibBuilder.loadTexts:
    gnWscCfgEntry.setStatus("mandatory")


class _GnWscCfgId_Type(Integer32):
    """Custom type gnWscCfgId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("local", 1)
    )


_GnWscCfgId_Type.__name__ = "Integer32"
_GnWscCfgId_Object = MibTableColumn
gnWscCfgId = _GnWscCfgId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 4, 2, 1, 1, 1),
    _GnWscCfgId_Type()
)
gnWscCfgId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnWscCfgId.setStatus("mandatory")


class _GnWscCfgChNumber_Type(Integer32):
    """Custom type gnWscCfgChNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("channel1", 1),
          ("channel2", 2))
    )


_GnWscCfgChNumber_Type.__name__ = "Integer32"
_GnWscCfgChNumber_Object = MibTableColumn
gnWscCfgChNumber = _GnWscCfgChNumber_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 4, 2, 1, 1, 2),
    _GnWscCfgChNumber_Type()
)
gnWscCfgChNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnWscCfgChNumber.setStatus("mandatory")


class _GnWscCfgRouting_Type(Integer32):
    """Custom type gnWscCfgRouting based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("drawer1", 2),
          ("drawer2", 3))
    )


_GnWscCfgRouting_Type.__name__ = "Integer32"
_GnWscCfgRouting_Object = MibTableColumn
gnWscCfgRouting = _GnWscCfgRouting_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 4, 2, 1, 1, 3),
    _GnWscCfgRouting_Type()
)
gnWscCfgRouting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnWscCfgRouting.setStatus("mandatory")


class _GnWscCfgEnable_Type(Integer32):
    """Custom type gnWscCfgEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("enable", 2))
    )


_GnWscCfgEnable_Type.__name__ = "Integer32"
_GnWscCfgEnable_Object = MibTableColumn
gnWscCfgEnable = _GnWscCfgEnable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 4, 2, 1, 1, 4),
    _GnWscCfgEnable_Type()
)
gnWscCfgEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnWscCfgEnable.setStatus("mandatory")


class _GnWscCfgBitRate_Type(Integer32):
    """Custom type gnWscCfgBitRate based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("high", 3),
          ("low", 2))
    )


_GnWscCfgBitRate_Type.__name__ = "Integer32"
_GnWscCfgBitRate_Object = MibTableColumn
gnWscCfgBitRate = _GnWscCfgBitRate_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 4, 2, 1, 1, 5),
    _GnWscCfgBitRate_Type()
)
gnWscCfgBitRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnWscCfgBitRate.setStatus("mandatory")


class _GnWscCfgType_Type(Integer32):
    """Custom type gnWscCfgType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("e1", 2),
          ("fastEthernet", 4),
          ("t1", 3))
    )


_GnWscCfgType_Type.__name__ = "Integer32"
_GnWscCfgType_Object = MibTableColumn
gnWscCfgType = _GnWscCfgType_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 4, 2, 1, 1, 6),
    _GnWscCfgType_Type()
)
gnWscCfgType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnWscCfgType.setStatus("mandatory")
_GnWscStatTable_Object = MibTable
gnWscStatTable = _GnWscStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 4, 2, 2)
)
if mibBuilder.loadTexts:
    gnWscStatTable.setStatus("mandatory")
_GnWscStatEntry_Object = MibTableRow
gnWscStatEntry = _GnWscStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 4, 2, 2, 1)
)
gnWscStatEntry.setIndexNames(
    (0, "CERAGON-MIB", "gnWscStatId"),
    (0, "CERAGON-MIB", "gnWscStatChNumber"),
)
if mibBuilder.loadTexts:
    gnWscStatEntry.setStatus("mandatory")


class _GnWscStatId_Type(Integer32):
    """Custom type gnWscStatId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("local", 1)
    )


_GnWscStatId_Type.__name__ = "Integer32"
_GnWscStatId_Object = MibTableColumn
gnWscStatId = _GnWscStatId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 4, 2, 2, 1, 1),
    _GnWscStatId_Type()
)
gnWscStatId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnWscStatId.setStatus("mandatory")


class _GnWscStatChNumber_Type(Integer32):
    """Custom type gnWscStatChNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("channel1", 1),
          ("channel2", 2))
    )


_GnWscStatChNumber_Type.__name__ = "Integer32"
_GnWscStatChNumber_Object = MibTableColumn
gnWscStatChNumber = _GnWscStatChNumber_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 4, 2, 2, 1, 2),
    _GnWscStatChNumber_Type()
)
gnWscStatChNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnWscStatChNumber.setStatus("mandatory")


class _GnWscStatBitRateSupport_Type(Integer32):
    """Custom type gnWscStatBitRateSupport based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 3),
          ("supported", 2))
    )


_GnWscStatBitRateSupport_Type.__name__ = "Integer32"
_GnWscStatBitRateSupport_Object = MibTableColumn
gnWscStatBitRateSupport = _GnWscStatBitRateSupport_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 4, 2, 2, 1, 3),
    _GnWscStatBitRateSupport_Type()
)
gnWscStatBitRateSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnWscStatBitRateSupport.setStatus("mandatory")
_GnEow_ObjectIdentity = ObjectIdentity
gnEow = _GnEow_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 4, 3)
)
_GnEowCfgTable_Object = MibTable
gnEowCfgTable = _GnEowCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 4, 3, 1)
)
if mibBuilder.loadTexts:
    gnEowCfgTable.setStatus("mandatory")
_GnEowCfgEntry_Object = MibTableRow
gnEowCfgEntry = _GnEowCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 4, 3, 1, 1)
)
gnEowCfgEntry.setIndexNames(
    (0, "CERAGON-MIB", "gnEowCfgId"),
)
if mibBuilder.loadTexts:
    gnEowCfgEntry.setStatus("mandatory")


class _GnEowCfgId_Type(Integer32):
    """Custom type gnEowCfgId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("local", 1)
    )


_GnEowCfgId_Type.__name__ = "Integer32"
_GnEowCfgId_Object = MibTableColumn
gnEowCfgId = _GnEowCfgId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 4, 3, 1, 1, 1),
    _GnEowCfgId_Type()
)
gnEowCfgId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnEowCfgId.setStatus("mandatory")


class _GnEowCfgEowLeftEnable_Type(Integer32):
    """Custom type gnEowCfgEowLeftEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("enable", 2))
    )


_GnEowCfgEowLeftEnable_Type.__name__ = "Integer32"
_GnEowCfgEowLeftEnable_Object = MibTableColumn
gnEowCfgEowLeftEnable = _GnEowCfgEowLeftEnable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 4, 3, 1, 1, 2),
    _GnEowCfgEowLeftEnable_Type()
)
gnEowCfgEowLeftEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnEowCfgEowLeftEnable.setStatus("mandatory")


class _GnEowCfgEowRightEnable_Type(Integer32):
    """Custom type gnEowCfgEowRightEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("enable", 2))
    )


_GnEowCfgEowRightEnable_Type.__name__ = "Integer32"
_GnEowCfgEowRightEnable_Object = MibTableColumn
gnEowCfgEowRightEnable = _GnEowCfgEowRightEnable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 4, 3, 1, 1, 3),
    _GnEowCfgEowRightEnable_Type()
)
gnEowCfgEowRightEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnEowCfgEowRightEnable.setStatus("mandatory")


class _GnEowCfgEowCascadeEnable_Type(Integer32):
    """Custom type gnEowCfgEowCascadeEnable based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("enable", 2))
    )


_GnEowCfgEowCascadeEnable_Type.__name__ = "Integer32"
_GnEowCfgEowCascadeEnable_Object = MibTableColumn
gnEowCfgEowCascadeEnable = _GnEowCfgEowCascadeEnable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 4, 3, 1, 1, 4),
    _GnEowCfgEowCascadeEnable_Type()
)
gnEowCfgEowCascadeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnEowCfgEowCascadeEnable.setStatus("mandatory")
_GnEowStatTable_Object = MibTable
gnEowStatTable = _GnEowStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 4, 3, 2)
)
if mibBuilder.loadTexts:
    gnEowStatTable.setStatus("mandatory")
_GnEowStatEntry_Object = MibTableRow
gnEowStatEntry = _GnEowStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 4, 3, 2, 1)
)
gnEowStatEntry.setIndexNames(
    (0, "CERAGON-MIB", "gnEowStatId"),
)
if mibBuilder.loadTexts:
    gnEowStatEntry.setStatus("mandatory")


class _GnEowStatId_Type(Integer32):
    """Custom type gnEowStatId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("local", 1)
    )


_GnEowStatId_Type.__name__ = "Integer32"
_GnEowStatId_Object = MibTableColumn
gnEowStatId = _GnEowStatId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 4, 3, 2, 1, 1),
    _GnEowStatId_Type()
)
gnEowStatId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnEowStatId.setStatus("mandatory")


class _GnEowStatEowLeftSupport_Type(Integer32):
    """Custom type gnEowStatEowLeftSupport based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 3),
          ("supported", 2))
    )


_GnEowStatEowLeftSupport_Type.__name__ = "Integer32"
_GnEowStatEowLeftSupport_Object = MibTableColumn
gnEowStatEowLeftSupport = _GnEowStatEowLeftSupport_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 4, 3, 2, 1, 2),
    _GnEowStatEowLeftSupport_Type()
)
gnEowStatEowLeftSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnEowStatEowLeftSupport.setStatus("mandatory")


class _GnEowStatEowRightSupport_Type(Integer32):
    """Custom type gnEowStatEowRightSupport based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 3),
          ("supported", 2))
    )


_GnEowStatEowRightSupport_Type.__name__ = "Integer32"
_GnEowStatEowRightSupport_Object = MibTableColumn
gnEowStatEowRightSupport = _GnEowStatEowRightSupport_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 4, 3, 2, 1, 3),
    _GnEowStatEowRightSupport_Type()
)
gnEowStatEowRightSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnEowStatEowRightSupport.setStatus("mandatory")
_GnUc_ObjectIdentity = ObjectIdentity
gnUc = _GnUc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 4, 4)
)
_GnUcCfgTable_Object = MibTable
gnUcCfgTable = _GnUcCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 4, 4, 1)
)
if mibBuilder.loadTexts:
    gnUcCfgTable.setStatus("mandatory")
_GnUcCfgEntry_Object = MibTableRow
gnUcCfgEntry = _GnUcCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 4, 4, 1, 1)
)
gnUcCfgEntry.setIndexNames(
    (0, "CERAGON-MIB", "gnUcCfgId"),
    (0, "CERAGON-MIB", "gnUcCfgChNumber"),
)
if mibBuilder.loadTexts:
    gnUcCfgEntry.setStatus("mandatory")


class _GnUcCfgId_Type(Integer32):
    """Custom type gnUcCfgId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("local", 1)
    )


_GnUcCfgId_Type.__name__ = "Integer32"
_GnUcCfgId_Object = MibTableColumn
gnUcCfgId = _GnUcCfgId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 4, 4, 1, 1, 1),
    _GnUcCfgId_Type()
)
gnUcCfgId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnUcCfgId.setStatus("mandatory")


class _GnUcCfgChNumber_Type(Integer32):
    """Custom type gnUcCfgChNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("channel1", 1),
          ("channel2", 2))
    )


_GnUcCfgChNumber_Type.__name__ = "Integer32"
_GnUcCfgChNumber_Object = MibTableColumn
gnUcCfgChNumber = _GnUcCfgChNumber_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 4, 4, 1, 1, 2),
    _GnUcCfgChNumber_Type()
)
gnUcCfgChNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnUcCfgChNumber.setStatus("mandatory")


class _GnUcCfgRouting_Type(Integer32):
    """Custom type gnUcCfgRouting based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("drawer1", 2),
          ("drawer2", 3))
    )


_GnUcCfgRouting_Type.__name__ = "Integer32"
_GnUcCfgRouting_Object = MibTableColumn
gnUcCfgRouting = _GnUcCfgRouting_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 4, 4, 1, 1, 3),
    _GnUcCfgRouting_Type()
)
gnUcCfgRouting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnUcCfgRouting.setStatus("mandatory")


class _GnUcCfgEnable_Type(Integer32):
    """Custom type gnUcCfgEnable based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("enable", 2))
    )


_GnUcCfgEnable_Type.__name__ = "Integer32"
_GnUcCfgEnable_Object = MibTableColumn
gnUcCfgEnable = _GnUcCfgEnable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 4, 4, 1, 1, 4),
    _GnUcCfgEnable_Type()
)
gnUcCfgEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnUcCfgEnable.setStatus("mandatory")


class _GnUcCfgType_Type(Integer32):
    """Custom type gnUcCfgType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 6),
          ("rs232", 3),
          ("v11Asyn", 2),
          ("v11SynCoDirectional", 4),
          ("v11SynContraDirectional", 5))
    )


_GnUcCfgType_Type.__name__ = "Integer32"
_GnUcCfgType_Object = MibTableColumn
gnUcCfgType = _GnUcCfgType_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 4, 4, 1, 1, 5),
    _GnUcCfgType_Type()
)
gnUcCfgType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnUcCfgType.setStatus("mandatory")


class _GnUcCfgLoopback_Type(Integer32):
    """Custom type gnUcCfgLoopback based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("line", 3),
          ("none", 2))
    )


_GnUcCfgLoopback_Type.__name__ = "Integer32"
_GnUcCfgLoopback_Object = MibTableColumn
gnUcCfgLoopback = _GnUcCfgLoopback_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 4, 4, 1, 1, 6),
    _GnUcCfgLoopback_Type()
)
gnUcCfgLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnUcCfgLoopback.setStatus("mandatory")
_GnUcStatTable_Object = MibTable
gnUcStatTable = _GnUcStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 4, 4, 2)
)
if mibBuilder.loadTexts:
    gnUcStatTable.setStatus("mandatory")
_GnUcStatEntry_Object = MibTableRow
gnUcStatEntry = _GnUcStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 4, 4, 2, 1)
)
gnUcStatEntry.setIndexNames(
    (0, "CERAGON-MIB", "gnUcStatId"),
)
if mibBuilder.loadTexts:
    gnUcStatEntry.setStatus("mandatory")


class _GnUcStatId_Type(Integer32):
    """Custom type gnUcStatId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("local", 1)
    )


_GnUcStatId_Type.__name__ = "Integer32"
_GnUcStatId_Object = MibTableColumn
gnUcStatId = _GnUcStatId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 4, 4, 2, 1, 1),
    _GnUcStatId_Type()
)
gnUcStatId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnUcStatId.setStatus("mandatory")


class _GnUcStatLeftMaxRouteChannel_Type(Integer32):
    """Custom type gnUcStatLeftMaxRouteChannel based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_GnUcStatLeftMaxRouteChannel_Type.__name__ = "Integer32"
_GnUcStatLeftMaxRouteChannel_Object = MibTableColumn
gnUcStatLeftMaxRouteChannel = _GnUcStatLeftMaxRouteChannel_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 4, 4, 2, 1, 2),
    _GnUcStatLeftMaxRouteChannel_Type()
)
gnUcStatLeftMaxRouteChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnUcStatLeftMaxRouteChannel.setStatus("mandatory")


class _GnUcStatRightMaxRouteChannel_Type(Integer32):
    """Custom type gnUcStatRightMaxRouteChannel based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_GnUcStatRightMaxRouteChannel_Type.__name__ = "Integer32"
_GnUcStatRightMaxRouteChannel_Object = MibTableColumn
gnUcStatRightMaxRouteChannel = _GnUcStatRightMaxRouteChannel_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 2, 4, 4, 2, 1, 3),
    _GnUcStatRightMaxRouteChannel_Type()
)
gnUcStatRightMaxRouteChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnUcStatRightMaxRouteChannel.setStatus("mandatory")
_GnProtect_ObjectIdentity = ObjectIdentity
gnProtect = _GnProtect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3)
)
_GnProtectCfgTable_Object = MibTable
gnProtectCfgTable = _GnProtectCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 1)
)
if mibBuilder.loadTexts:
    gnProtectCfgTable.setStatus("mandatory")
_GnProtectCfgEntry_Object = MibTableRow
gnProtectCfgEntry = _GnProtectCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 1, 1)
)
gnProtectCfgEntry.setIndexNames(
    (0, "CERAGON-MIB", "gnProtectCfgId"),
)
if mibBuilder.loadTexts:
    gnProtectCfgEntry.setStatus("mandatory")


class _GnProtectCfgId_Type(Integer32):
    """Custom type gnProtectCfgId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("remote", 2))
    )


_GnProtectCfgId_Type.__name__ = "Integer32"
_GnProtectCfgId_Object = MibTableColumn
gnProtectCfgId = _GnProtectCfgId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 1, 1, 1),
    _GnProtectCfgId_Type()
)
gnProtectCfgId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnProtectCfgId.setStatus("mandatory")


class _GnProtectCfgSwitchRequest_Type(Integer32):
    """Custom type gnProtectCfgSwitchRequest based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 2),
          ("userForceSwitch", 4),
          ("userSwitchRequest", 3))
    )


_GnProtectCfgSwitchRequest_Type.__name__ = "Integer32"
_GnProtectCfgSwitchRequest_Object = MibTableColumn
gnProtectCfgSwitchRequest = _GnProtectCfgSwitchRequest_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 1, 1, 2),
    _GnProtectCfgSwitchRequest_Type()
)
gnProtectCfgSwitchRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnProtectCfgSwitchRequest.setStatus("mandatory")


class _GnProtectCfgBERSwitch_Type(Integer32):
    """Custom type gnProtectCfgBERSwitch based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("enable", 2))
    )


_GnProtectCfgBERSwitch_Type.__name__ = "Integer32"
_GnProtectCfgBERSwitch_Object = MibTableColumn
gnProtectCfgBERSwitch = _GnProtectCfgBERSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 1, 1, 3),
    _GnProtectCfgBERSwitch_Type()
)
gnProtectCfgBERSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnProtectCfgBERSwitch.setStatus("mandatory")


class _GnProtectCfgExtInSwitch_Type(Integer32):
    """Custom type gnProtectCfgExtInSwitch based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("enable", 2))
    )


_GnProtectCfgExtInSwitch_Type.__name__ = "Integer32"
_GnProtectCfgExtInSwitch_Object = MibTableColumn
gnProtectCfgExtInSwitch = _GnProtectCfgExtInSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 1, 1, 4),
    _GnProtectCfgExtInSwitch_Type()
)
gnProtectCfgExtInSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnProtectCfgExtInSwitch.setStatus("mandatory")


class _GnProtectCfgOption_Type(OctetString):
    """Custom type gnProtectCfgOption based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_GnProtectCfgOption_Type.__name__ = "OctetString"
_GnProtectCfgOption_Object = MibTableColumn
gnProtectCfgOption = _GnProtectCfgOption_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 1, 1, 5),
    _GnProtectCfgOption_Type()
)
gnProtectCfgOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnProtectCfgOption.setStatus("mandatory")


class _GnProtectCfgUserCommand_Type(Integer32):
    """Custom type gnProtectCfgUserCommand based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("copyConfToMate", 3),
          ("copyLeftConfToRight", 4),
          ("copyRightConfToLeft", 5),
          ("noAction", 2))
    )


_GnProtectCfgUserCommand_Type.__name__ = "Integer32"
_GnProtectCfgUserCommand_Object = MibTableColumn
gnProtectCfgUserCommand = _GnProtectCfgUserCommand_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 1, 1, 6),
    _GnProtectCfgUserCommand_Type()
)
gnProtectCfgUserCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnProtectCfgUserCommand.setStatus("mandatory")


class _GnProtectCfgType_Type(Integer32):
    """Custom type gnProtectCfgType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("external", 4),
          ("externalInternal", 5),
          ("internal", 3),
          ("multiRadioWithLineProtection", 7),
          ("multiRadioWithoutLineProtection", 6),
          ("none", 2))
    )


_GnProtectCfgType_Type.__name__ = "Integer32"
_GnProtectCfgType_Object = MibTableColumn
gnProtectCfgType = _GnProtectCfgType_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 1, 1, 7),
    _GnProtectCfgType_Type()
)
gnProtectCfgType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnProtectCfgType.setStatus("mandatory")


class _GnProtectCfgProtectionLockout_Type(Integer32):
    """Custom type gnProtectCfgProtectionLockout based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 3),
          ("on", 2))
    )


_GnProtectCfgProtectionLockout_Type.__name__ = "Integer32"
_GnProtectCfgProtectionLockout_Object = MibTableColumn
gnProtectCfgProtectionLockout = _GnProtectCfgProtectionLockout_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 1, 1, 8),
    _GnProtectCfgProtectionLockout_Type()
)
gnProtectCfgProtectionLockout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnProtectCfgProtectionLockout.setStatus("mandatory")


class _GnProtectCfgSdBERSwitch_Type(Integer32):
    """Custom type gnProtectCfgSdBERSwitch based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("enable", 2))
    )


_GnProtectCfgSdBERSwitch_Type.__name__ = "Integer32"
_GnProtectCfgSdBERSwitch_Object = MibTableColumn
gnProtectCfgSdBERSwitch = _GnProtectCfgSdBERSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 1, 1, 9),
    _GnProtectCfgSdBERSwitch_Type()
)
gnProtectCfgSdBERSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnProtectCfgSdBERSwitch.setStatus("mandatory")


class _GnProtectCfgMultiRadioBlock_Type(Integer32):
    """Custom type gnProtectCfgMultiRadioBlock based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("blockBoth", 5),
          ("blockLeft", 3),
          ("blockRight", 4),
          ("unblock", 2))
    )


_GnProtectCfgMultiRadioBlock_Type.__name__ = "Integer32"
_GnProtectCfgMultiRadioBlock_Object = MibTableColumn
gnProtectCfgMultiRadioBlock = _GnProtectCfgMultiRadioBlock_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 1, 1, 10),
    _GnProtectCfgMultiRadioBlock_Type()
)
gnProtectCfgMultiRadioBlock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnProtectCfgMultiRadioBlock.setStatus("mandatory")


class _GnProtectUnitMode_Type(Integer32):
    """Custom type gnProtectUnitMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("master", 3),
          ("slave", 2))
    )


_GnProtectUnitMode_Type.__name__ = "Integer32"
_GnProtectUnitMode_Object = MibScalar
gnProtectUnitMode = _GnProtectUnitMode_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 2),
    _GnProtectUnitMode_Type()
)
gnProtectUnitMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnProtectUnitMode.setStatus("mandatory")
_GnHitLessCfgTable_Object = MibTable
gnHitLessCfgTable = _GnHitLessCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 3)
)
if mibBuilder.loadTexts:
    gnHitLessCfgTable.setStatus("mandatory")
_GnHitLessCfgEntry_Object = MibTableRow
gnHitLessCfgEntry = _GnHitLessCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 3, 1)
)
gnHitLessCfgEntry.setIndexNames(
    (0, "CERAGON-MIB", "gnHitLessCfgId"),
)
if mibBuilder.loadTexts:
    gnHitLessCfgEntry.setStatus("mandatory")


class _GnHitLessCfgId_Type(Integer32):
    """Custom type gnHitLessCfgId based on Integer32"""
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
        *(("drawer1", 3),
          ("drawer2", 4),
          ("local", 1),
          ("remote", 2))
    )


_GnHitLessCfgId_Type.__name__ = "Integer32"
_GnHitLessCfgId_Object = MibTableColumn
gnHitLessCfgId = _GnHitLessCfgId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 3, 1, 1),
    _GnHitLessCfgId_Type()
)
gnHitLessCfgId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnHitLessCfgId.setStatus("mandatory")


class _GnHitLessCfgSwitchEnable_Type(Integer32):
    """Custom type gnHitLessCfgSwitchEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("enable", 2))
    )


_GnHitLessCfgSwitchEnable_Type.__name__ = "Integer32"
_GnHitLessCfgSwitchEnable_Object = MibTableColumn
gnHitLessCfgSwitchEnable = _GnHitLessCfgSwitchEnable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 3, 1, 2),
    _GnHitLessCfgSwitchEnable_Type()
)
gnHitLessCfgSwitchEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnHitLessCfgSwitchEnable.setStatus("mandatory")


class _GnHitLessCfgDiversityType_Type(Integer32):
    """Custom type gnHitLessCfgDiversityType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("frequency", 3),
          ("none", 4),
          ("space", 2))
    )


_GnHitLessCfgDiversityType_Type.__name__ = "Integer32"
_GnHitLessCfgDiversityType_Object = MibTableColumn
gnHitLessCfgDiversityType = _GnHitLessCfgDiversityType_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 3, 1, 3),
    _GnHitLessCfgDiversityType_Type()
)
gnHitLessCfgDiversityType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnHitLessCfgDiversityType.setStatus("mandatory")


class _GnHitLessCfgSwitchingMode_Type(Integer32):
    """Custom type gnHitLessCfgSwitchingMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nonRevertive", 3),
          ("revertive", 2))
    )


_GnHitLessCfgSwitchingMode_Type.__name__ = "Integer32"
_GnHitLessCfgSwitchingMode_Object = MibTableColumn
gnHitLessCfgSwitchingMode = _GnHitLessCfgSwitchingMode_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 3, 1, 4),
    _GnHitLessCfgSwitchingMode_Type()
)
gnHitLessCfgSwitchingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnHitLessCfgSwitchingMode.setStatus("mandatory")


class _GnHitLessCfgRevertTime_Type(Integer32):
    """Custom type gnHitLessCfgRevertTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_GnHitLessCfgRevertTime_Type.__name__ = "Integer32"
_GnHitLessCfgRevertTime_Object = MibTableColumn
gnHitLessCfgRevertTime = _GnHitLessCfgRevertTime_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 3, 1, 5),
    _GnHitLessCfgRevertTime_Type()
)
gnHitLessCfgRevertTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnHitLessCfgRevertTime.setStatus("mandatory")


class _GnHitLessCfgManualSwitch_Type(Integer32):
    """Custom type gnHitLessCfgManualSwitch based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("activate", 3),
          ("noAction", 2))
    )


_GnHitLessCfgManualSwitch_Type.__name__ = "Integer32"
_GnHitLessCfgManualSwitch_Object = MibTableColumn
gnHitLessCfgManualSwitch = _GnHitLessCfgManualSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 3, 1, 6),
    _GnHitLessCfgManualSwitch_Type()
)
gnHitLessCfgManualSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnHitLessCfgManualSwitch.setStatus("mandatory")


class _GnHitLessCfgEventCounterCommand_Type(Integer32):
    """Custom type gnHitLessCfgEventCounterCommand based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clearCounter", 3),
          ("noAction", 2))
    )


_GnHitLessCfgEventCounterCommand_Type.__name__ = "Integer32"
_GnHitLessCfgEventCounterCommand_Object = MibTableColumn
gnHitLessCfgEventCounterCommand = _GnHitLessCfgEventCounterCommand_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 3, 1, 7),
    _GnHitLessCfgEventCounterCommand_Type()
)
gnHitLessCfgEventCounterCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnHitLessCfgEventCounterCommand.setStatus("mandatory")


class _GnHitLessCfgSwitchLock_Type(Integer32):
    """Custom type gnHitLessCfgSwitchLock based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("left", 3),
          ("mate", 6),
          ("off", 2),
          ("right", 4),
          ("self", 5))
    )


_GnHitLessCfgSwitchLock_Type.__name__ = "Integer32"
_GnHitLessCfgSwitchLock_Object = MibTableColumn
gnHitLessCfgSwitchLock = _GnHitLessCfgSwitchLock_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 3, 1, 8),
    _GnHitLessCfgSwitchLock_Type()
)
gnHitLessCfgSwitchLock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnHitLessCfgSwitchLock.setStatus("mandatory")
_GnHitLessStatTable_Object = MibTable
gnHitLessStatTable = _GnHitLessStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 4)
)
if mibBuilder.loadTexts:
    gnHitLessStatTable.setStatus("mandatory")
_GnHitLessStatEntry_Object = MibTableRow
gnHitLessStatEntry = _GnHitLessStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 4, 1)
)
gnHitLessStatEntry.setIndexNames(
    (0, "CERAGON-MIB", "gnHitLessStatId"),
)
if mibBuilder.loadTexts:
    gnHitLessStatEntry.setStatus("mandatory")


class _GnHitLessStatId_Type(Integer32):
    """Custom type gnHitLessStatId based on Integer32"""
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
        *(("drawer1", 3),
          ("drawer2", 4),
          ("local", 1),
          ("remote", 2))
    )


_GnHitLessStatId_Type.__name__ = "Integer32"
_GnHitLessStatId_Object = MibTableColumn
gnHitLessStatId = _GnHitLessStatId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 4, 1, 1),
    _GnHitLessStatId_Type()
)
gnHitLessStatId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnHitLessStatId.setStatus("mandatory")


class _GnHitLessStatReceiverStatus_Type(Integer32):
    """Custom type gnHitLessStatReceiverStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("leftRadio", 4),
          ("local", 2),
          ("mate", 3),
          ("rightRadio", 5))
    )


_GnHitLessStatReceiverStatus_Type.__name__ = "Integer32"
_GnHitLessStatReceiverStatus_Object = MibTableColumn
gnHitLessStatReceiverStatus = _GnHitLessStatReceiverStatus_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 4, 1, 2),
    _GnHitLessStatReceiverStatus_Type()
)
gnHitLessStatReceiverStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnHitLessStatReceiverStatus.setStatus("mandatory")


class _GnHitLessStatModeStatus_Type(Integer32):
    """Custom type gnHitLessStatModeStatus based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hitlessFailure", 3),
          ("hitlessOK", 2))
    )


_GnHitLessStatModeStatus_Type.__name__ = "Integer32"
_GnHitLessStatModeStatus_Object = MibTableColumn
gnHitLessStatModeStatus = _GnHitLessStatModeStatus_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 4, 1, 3),
    _GnHitLessStatModeStatus_Type()
)
gnHitLessStatModeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnHitLessStatModeStatus.setStatus("mandatory")


class _GnHitLessStatEventCounter_Type(Integer32):
    """Custom type gnHitLessStatEventCounter based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_GnHitLessStatEventCounter_Type.__name__ = "Integer32"
_GnHitLessStatEventCounter_Object = MibTableColumn
gnHitLessStatEventCounter = _GnHitLessStatEventCounter_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 4, 1, 4),
    _GnHitLessStatEventCounter_Type()
)
gnHitLessStatEventCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnHitLessStatEventCounter.setStatus("mandatory")


class _GnHitLessStatAlarmStatus_Type(OctetString):
    """Custom type gnHitLessStatAlarmStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_GnHitLessStatAlarmStatus_Type.__name__ = "OctetString"
_GnHitLessStatAlarmStatus_Object = MibTableColumn
gnHitLessStatAlarmStatus = _GnHitLessStatAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 4, 1, 5),
    _GnHitLessStatAlarmStatus_Type()
)
gnHitLessStatAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnHitLessStatAlarmStatus.setStatus("mandatory")
_GnTribStmProtectCfg_ObjectIdentity = ObjectIdentity
gnTribStmProtectCfg = _GnTribStmProtectCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 5)
)


class _GnTribStmProtectType_Type(Integer32):
    """Custom type gnTribStmProtectType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("msp", 3),
          ("none", 2),
          ("sncp", 4))
    )


_GnTribStmProtectType_Type.__name__ = "Integer32"
_GnTribStmProtectType_Object = MibScalar
gnTribStmProtectType = _GnTribStmProtectType_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 5, 1),
    _GnTribStmProtectType_Type()
)
gnTribStmProtectType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnTribStmProtectType.setStatus("mandatory")


class _GnTribStmMspConnect_Type(Integer32):
    """Custom type gnTribStmMspConnect based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dualTribConnect", 2),
          ("singleTribConnect", 3))
    )


_GnTribStmMspConnect_Type.__name__ = "Integer32"
_GnTribStmMspConnect_Object = MibScalar
gnTribStmMspConnect = _GnTribStmMspConnect_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 5, 2),
    _GnTribStmMspConnect_Type()
)
gnTribStmMspConnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnTribStmMspConnect.setStatus("mandatory")


class _GnTribStmMspType_Type(Integer32):
    """Custom type gnTribStmMspType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("biDirectional", 3),
          ("uniDirectional", 2))
    )


_GnTribStmMspType_Type.__name__ = "Integer32"
_GnTribStmMspType_Object = MibScalar
gnTribStmMspType = _GnTribStmMspType_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 5, 3),
    _GnTribStmMspType_Type()
)
gnTribStmMspType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnTribStmMspType.setStatus("mandatory")


class _GnTribStmMspRevertiveMode_Type(Integer32):
    """Custom type gnTribStmMspRevertiveMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nonRevertive", 2),
          ("revertive", 3))
    )


_GnTribStmMspRevertiveMode_Type.__name__ = "Integer32"
_GnTribStmMspRevertiveMode_Object = MibScalar
gnTribStmMspRevertiveMode = _GnTribStmMspRevertiveMode_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 5, 4),
    _GnTribStmMspRevertiveMode_Type()
)
gnTribStmMspRevertiveMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnTribStmMspRevertiveMode.setStatus("mandatory")


class _GnTribStmMspProtectRole_Type(Integer32):
    """Custom type gnTribStmMspProtectRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("main", 2),
          ("standBy", 3))
    )


_GnTribStmMspProtectRole_Type.__name__ = "Integer32"
_GnTribStmMspProtectRole_Object = MibScalar
gnTribStmMspProtectRole = _GnTribStmMspProtectRole_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 5, 5),
    _GnTribStmMspProtectRole_Type()
)
gnTribStmMspProtectRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnTribStmMspProtectRole.setStatus("mandatory")


class _GnTribStmMspWaitToRestoreTime_Type(Integer32):
    """Custom type gnTribStmMspWaitToRestoreTime based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 12),
    )


_GnTribStmMspWaitToRestoreTime_Type.__name__ = "Integer32"
_GnTribStmMspWaitToRestoreTime_Object = MibScalar
gnTribStmMspWaitToRestoreTime = _GnTribStmMspWaitToRestoreTime_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 5, 6),
    _GnTribStmMspWaitToRestoreTime_Type()
)
gnTribStmMspWaitToRestoreTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnTribStmMspWaitToRestoreTime.setStatus("mandatory")


class _GnTribStmMspUserCommand_Type(Integer32):
    """Custom type gnTribStmMspUserCommand based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("exercise", 6),
          ("forceSwitch", 4),
          ("lockOut", 3),
          ("manualSwitch", 5))
    )


_GnTribStmMspUserCommand_Type.__name__ = "Integer32"
_GnTribStmMspUserCommand_Object = MibScalar
gnTribStmMspUserCommand = _GnTribStmMspUserCommand_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 5, 7),
    _GnTribStmMspUserCommand_Type()
)
gnTribStmMspUserCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnTribStmMspUserCommand.setStatus("mandatory")
_GnTribStmProtectStat_ObjectIdentity = ObjectIdentity
gnTribStmProtectStat = _GnTribStmProtectStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 6)
)


class _GnTribStmProtectCurrentState_Type(Integer32):
    """Custom type gnTribStmProtectCurrentState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("protecting", 3),
          ("working", 2))
    )


_GnTribStmProtectCurrentState_Type.__name__ = "Integer32"
_GnTribStmProtectCurrentState_Object = MibScalar
gnTribStmProtectCurrentState = _GnTribStmProtectCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 6, 1),
    _GnTribStmProtectCurrentState_Type()
)
gnTribStmProtectCurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnTribStmProtectCurrentState.setStatus("mandatory")


class _GnTribStmProtectCableStatus_Type(Integer32):
    """Custom type gnTribStmProtectCableStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fault", 3),
          ("ok", 2))
    )


_GnTribStmProtectCableStatus_Type.__name__ = "Integer32"
_GnTribStmProtectCableStatus_Object = MibScalar
gnTribStmProtectCableStatus = _GnTribStmProtectCableStatus_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 6, 2),
    _GnTribStmProtectCableStatus_Type()
)
gnTribStmProtectCableStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnTribStmProtectCableStatus.setStatus("mandatory")
_GnProtectXTable_Object = MibTable
gnProtectXTable = _GnProtectXTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 7)
)
if mibBuilder.loadTexts:
    gnProtectXTable.setStatus("mandatory")
_GnProtectXEntry_Object = MibTableRow
gnProtectXEntry = _GnProtectXEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 7, 1)
)
gnProtectXEntry.setIndexNames(
    (0, "CERAGON-MIB", "gnProtectXId"),
)
if mibBuilder.loadTexts:
    gnProtectXEntry.setStatus("mandatory")


class _GnProtectXId_Type(Integer32):
    """Custom type gnProtectXId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("drawer1", 3),
          ("drawer2", 4))
    )


_GnProtectXId_Type.__name__ = "Integer32"
_GnProtectXId_Object = MibTableColumn
gnProtectXId = _GnProtectXId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 7, 1, 1),
    _GnProtectXId_Type()
)
gnProtectXId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnProtectXId.setStatus("mandatory")


class _GnProtectXProtectUnitMode_Type(Integer32):
    """Custom type gnProtectXProtectUnitMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("master", 3),
          ("slave", 2))
    )


_GnProtectXProtectUnitMode_Type.__name__ = "Integer32"
_GnProtectXProtectUnitMode_Object = MibTableColumn
gnProtectXProtectUnitMode = _GnProtectXProtectUnitMode_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 7, 1, 2),
    _GnProtectXProtectUnitMode_Type()
)
gnProtectXProtectUnitMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnProtectXProtectUnitMode.setStatus("mandatory")


class _GnProtectXMultiRadioOhRadioSource_Type(Integer32):
    """Custom type gnProtectXMultiRadioOhRadioSource based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("drawer1", 3),
          ("drawer2", 4))
    )


_GnProtectXMultiRadioOhRadioSource_Type.__name__ = "Integer32"
_GnProtectXMultiRadioOhRadioSource_Object = MibTableColumn
gnProtectXMultiRadioOhRadioSource = _GnProtectXMultiRadioOhRadioSource_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 7, 1, 3),
    _GnProtectXMultiRadioOhRadioSource_Type()
)
gnProtectXMultiRadioOhRadioSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnProtectXMultiRadioOhRadioSource.setStatus("mandatory")
_GnLinkGroups_ObjectIdentity = ObjectIdentity
gnLinkGroups = _GnLinkGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 8)
)
_TopologiesOptionsTable_Object = MibTable
topologiesOptionsTable = _TopologiesOptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 8, 1)
)
if mibBuilder.loadTexts:
    topologiesOptionsTable.setStatus("mandatory")
_TopologiesOptionsEntry_Object = MibTableRow
topologiesOptionsEntry = _TopologiesOptionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 8, 1, 1)
)
topologiesOptionsEntry.setIndexNames(
    (0, "CERAGON-MIB", "topologiesOptionsGroupTopology"),
)
if mibBuilder.loadTexts:
    topologiesOptionsEntry.setStatus("mandatory")


class _TopologiesOptionsGroupTopology_Type(Integer32):
    """Custom type topologiesOptionsGroupTopology based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_TopologiesOptionsGroupTopology_Type.__name__ = "Integer32"
_TopologiesOptionsGroupTopology_Object = MibTableColumn
topologiesOptionsGroupTopology = _TopologiesOptionsGroupTopology_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 8, 1, 1, 1),
    _TopologiesOptionsGroupTopology_Type()
)
topologiesOptionsGroupTopology.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    topologiesOptionsGroupTopology.setStatus("mandatory")


class _TopologiesOptionsMembersCarriers_Type(Integer32):
    """Custom type topologiesOptionsMembersCarriers based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_TopologiesOptionsMembersCarriers_Type.__name__ = "Integer32"
_TopologiesOptionsMembersCarriers_Object = MibTableColumn
topologiesOptionsMembersCarriers = _TopologiesOptionsMembersCarriers_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 8, 1, 1, 2),
    _TopologiesOptionsMembersCarriers_Type()
)
topologiesOptionsMembersCarriers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    topologiesOptionsMembersCarriers.setStatus("mandatory")


class _TopologiesOptionsProtectingCarriers_Type(Integer32):
    """Custom type topologiesOptionsProtectingCarriers based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_TopologiesOptionsProtectingCarriers_Type.__name__ = "Integer32"
_TopologiesOptionsProtectingCarriers_Object = MibTableColumn
topologiesOptionsProtectingCarriers = _TopologiesOptionsProtectingCarriers_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 8, 1, 1, 3),
    _TopologiesOptionsProtectingCarriers_Type()
)
topologiesOptionsProtectingCarriers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    topologiesOptionsProtectingCarriers.setStatus("mandatory")


class _TopologiesOptionsName_Type(DisplayString):
    """Custom type topologiesOptionsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_TopologiesOptionsName_Type.__name__ = "DisplayString"
_TopologiesOptionsName_Object = MibTableColumn
topologiesOptionsName = _TopologiesOptionsName_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 8, 1, 1, 4),
    _TopologiesOptionsName_Type()
)
topologiesOptionsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    topologiesOptionsName.setStatus("mandatory")
_LinkGroupingTable_Object = MibTable
linkGroupingTable = _LinkGroupingTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 8, 2)
)
if mibBuilder.loadTexts:
    linkGroupingTable.setStatus("mandatory")
_LinkGroupingEntry_Object = MibTableRow
linkGroupingEntry = _LinkGroupingEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 8, 2, 1)
)
linkGroupingEntry.setIndexNames(
    (0, "CERAGON-MIB", "linkGroupingGroupId"),
)
if mibBuilder.loadTexts:
    linkGroupingEntry.setStatus("mandatory")


class _LinkGroupingGroupId_Type(Integer32):
    """Custom type linkGroupingGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_LinkGroupingGroupId_Type.__name__ = "Integer32"
_LinkGroupingGroupId_Object = MibTableColumn
linkGroupingGroupId = _LinkGroupingGroupId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 8, 2, 1, 1),
    _LinkGroupingGroupId_Type()
)
linkGroupingGroupId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    linkGroupingGroupId.setStatus("mandatory")


class _LinkGroupingGroupAdmin_Type(Integer32):
    """Custom type linkGroupingGroupAdmin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("enable", 2))
    )


_LinkGroupingGroupAdmin_Type.__name__ = "Integer32"
_LinkGroupingGroupAdmin_Object = MibTableColumn
linkGroupingGroupAdmin = _LinkGroupingGroupAdmin_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 8, 2, 1, 2),
    _LinkGroupingGroupAdmin_Type()
)
linkGroupingGroupAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    linkGroupingGroupAdmin.setStatus("mandatory")


class _LinkGroupingGroupTopology_Type(Integer32):
    """Custom type linkGroupingGroupTopology based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              256,
              513,
              514,
              515,
              516,
              517,
              518,
              519,
              520,
              521)
        )
    )
    namedValues = NamedValues(
        *(("topology1plus1", 513),
          ("topology2plus1", 514),
          ("topology3plus1", 515),
          ("topology4plus1", 516),
          ("topology5plus1", 517),
          ("topology6plus1", 518),
          ("topology7plus1", 519),
          ("topology8plus1", 520),
          ("topology9plus1", 521),
          ("topologyhsb1-1", 1),
          ("topologystandalone", 256))
    )


_LinkGroupingGroupTopology_Type.__name__ = "Integer32"
_LinkGroupingGroupTopology_Object = MibTableColumn
linkGroupingGroupTopology = _LinkGroupingGroupTopology_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 8, 2, 1, 3),
    _LinkGroupingGroupTopology_Type()
)
linkGroupingGroupTopology.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    linkGroupingGroupTopology.setStatus("mandatory")


class _LinkGroupingExtraTrafficAdmin_Type(Integer32):
    """Custom type linkGroupingExtraTrafficAdmin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("enable", 2))
    )


_LinkGroupingExtraTrafficAdmin_Type.__name__ = "Integer32"
_LinkGroupingExtraTrafficAdmin_Object = MibTableColumn
linkGroupingExtraTrafficAdmin = _LinkGroupingExtraTrafficAdmin_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 8, 2, 1, 4),
    _LinkGroupingExtraTrafficAdmin_Type()
)
linkGroupingExtraTrafficAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    linkGroupingExtraTrafficAdmin.setStatus("mandatory")


class _LinkGroupingGroupName_Type(DisplayString):
    """Custom type linkGroupingGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_LinkGroupingGroupName_Type.__name__ = "DisplayString"
_LinkGroupingGroupName_Object = MibTableColumn
linkGroupingGroupName = _LinkGroupingGroupName_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 8, 2, 1, 5),
    _LinkGroupingGroupName_Type()
)
linkGroupingGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    linkGroupingGroupName.setStatus("mandatory")
_ProtectionTable_Object = MibTable
protectionTable = _ProtectionTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 8, 3)
)
if mibBuilder.loadTexts:
    protectionTable.setStatus("mandatory")
_ProtectionEntry_Object = MibTableRow
protectionEntry = _ProtectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 8, 3, 1)
)
protectionEntry.setIndexNames(
    (0, "CERAGON-MIB", "protectionGroupId"),
)
if mibBuilder.loadTexts:
    protectionEntry.setStatus("mandatory")


class _ProtectionGroupId_Type(Integer32):
    """Custom type protectionGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_ProtectionGroupId_Type.__name__ = "Integer32"
_ProtectionGroupId_Object = MibTableColumn
protectionGroupId = _ProtectionGroupId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 8, 3, 1, 1),
    _ProtectionGroupId_Type()
)
protectionGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    protectionGroupId.setStatus("mandatory")


class _ProtectionGroupsProtectionAdmin_Type(Integer32):
    """Custom type protectionGroupsProtectionAdmin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("enable", 2))
    )


_ProtectionGroupsProtectionAdmin_Type.__name__ = "Integer32"
_ProtectionGroupsProtectionAdmin_Object = MibTableColumn
protectionGroupsProtectionAdmin = _ProtectionGroupsProtectionAdmin_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 8, 3, 1, 2),
    _ProtectionGroupsProtectionAdmin_Type()
)
protectionGroupsProtectionAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    protectionGroupsProtectionAdmin.setStatus("mandatory")


class _ProtectionNplus1ProtectionMethod_Type(Integer32):
    """Custom type protectionNplus1ProtectionMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("advanced", 3),
          ("standard", 2))
    )


_ProtectionNplus1ProtectionMethod_Type.__name__ = "Integer32"
_ProtectionNplus1ProtectionMethod_Object = MibTableColumn
protectionNplus1ProtectionMethod = _ProtectionNplus1ProtectionMethod_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 8, 3, 1, 3),
    _ProtectionNplus1ProtectionMethod_Type()
)
protectionNplus1ProtectionMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    protectionNplus1ProtectionMethod.setStatus("mandatory")


class _ProtectionProtectingCarrierId_Type(Integer32):
    """Custom type protectionProtectingCarrierId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_ProtectionProtectingCarrierId_Type.__name__ = "Integer32"
_ProtectionProtectingCarrierId_Object = MibTableColumn
protectionProtectingCarrierId = _ProtectionProtectingCarrierId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 8, 3, 1, 4),
    _ProtectionProtectingCarrierId_Type()
)
protectionProtectingCarrierId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    protectionProtectingCarrierId.setStatus("mandatory")
_StandardProtectionTable_Object = MibTable
standardProtectionTable = _StandardProtectionTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 8, 4)
)
if mibBuilder.loadTexts:
    standardProtectionTable.setStatus("mandatory")
_StandardProtectionEntry_Object = MibTableRow
standardProtectionEntry = _StandardProtectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 8, 4, 1)
)
standardProtectionEntry.setIndexNames(
    (0, "CERAGON-MIB", "standardProtectionGroupId"),
)
if mibBuilder.loadTexts:
    standardProtectionEntry.setStatus("mandatory")


class _StandardProtectionGroupId_Type(Integer32):
    """Custom type standardProtectionGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_StandardProtectionGroupId_Type.__name__ = "Integer32"
_StandardProtectionGroupId_Object = MibTableColumn
standardProtectionGroupId = _StandardProtectionGroupId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 8, 4, 1, 1),
    _StandardProtectionGroupId_Type()
)
standardProtectionGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    standardProtectionGroupId.setStatus("mandatory")


class _StandardProtectionSwitchOnEarlyWarning_Type(Integer32):
    """Custom type standardProtectionSwitchOnEarlyWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("enable", 2))
    )


_StandardProtectionSwitchOnEarlyWarning_Type.__name__ = "Integer32"
_StandardProtectionSwitchOnEarlyWarning_Object = MibTableColumn
standardProtectionSwitchOnEarlyWarning = _StandardProtectionSwitchOnEarlyWarning_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 8, 4, 1, 2),
    _StandardProtectionSwitchOnEarlyWarning_Type()
)
standardProtectionSwitchOnEarlyWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    standardProtectionSwitchOnEarlyWarning.setStatus("mandatory")


class _StandardProtectionHighPrioProtectionTh_Type(Integer32):
    """Custom type standardProtectionHighPrioProtectionTh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("bbexb", 5),
          ("bblof", 4),
          ("bbsd", 6),
          ("ew", 7))
    )


_StandardProtectionHighPrioProtectionTh_Type.__name__ = "Integer32"
_StandardProtectionHighPrioProtectionTh_Object = MibTableColumn
standardProtectionHighPrioProtectionTh = _StandardProtectionHighPrioProtectionTh_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 8, 4, 1, 3),
    _StandardProtectionHighPrioProtectionTh_Type()
)
standardProtectionHighPrioProtectionTh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    standardProtectionHighPrioProtectionTh.setStatus("mandatory")


class _StandardProtectionRevertiveLink_Type(Integer32):
    """Custom type standardProtectionRevertiveLink based on Integer32"""
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
              256,
              257)
        )
    )
    namedValues = NamedValues(
        *(("carrier1", 1),
          ("carrier10", 10),
          ("carrier11", 11),
          ("carrier12", 12),
          ("carrier13", 13),
          ("carrier14", 14),
          ("carrier15", 15),
          ("carrier2", 2),
          ("carrier3", 3),
          ("carrier4", 4),
          ("carrier5", 5),
          ("carrier6", 6),
          ("carrier7", 7),
          ("carrier8", 8),
          ("carrier9", 9),
          ("extraTraffic", 256),
          ("none", 257))
    )


_StandardProtectionRevertiveLink_Type.__name__ = "Integer32"
_StandardProtectionRevertiveLink_Object = MibTableColumn
standardProtectionRevertiveLink = _StandardProtectionRevertiveLink_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 8, 4, 1, 4),
    _StandardProtectionRevertiveLink_Type()
)
standardProtectionRevertiveLink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    standardProtectionRevertiveLink.setStatus("mandatory")


class _StandardProtectionRevertiveSwitchTimeOut_Type(Integer32):
    """Custom type standardProtectionRevertiveSwitchTimeOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_StandardProtectionRevertiveSwitchTimeOut_Type.__name__ = "Integer32"
_StandardProtectionRevertiveSwitchTimeOut_Object = MibTableColumn
standardProtectionRevertiveSwitchTimeOut = _StandardProtectionRevertiveSwitchTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 8, 4, 1, 5),
    _StandardProtectionRevertiveSwitchTimeOut_Type()
)
standardProtectionRevertiveSwitchTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    standardProtectionRevertiveSwitchTimeOut.setStatus("mandatory")
_MembersTable_Object = MibTable
membersTable = _MembersTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 8, 5)
)
if mibBuilder.loadTexts:
    membersTable.setStatus("mandatory")
_MembersEntry_Object = MibTableRow
membersEntry = _MembersEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 8, 5, 1)
)
membersEntry.setIndexNames(
    (0, "CERAGON-MIB", "membersGroupId"),
    (0, "CERAGON-MIB", "membersCarrierId"),
)
if mibBuilder.loadTexts:
    membersEntry.setStatus("mandatory")


class _MembersGroupId_Type(Integer32):
    """Custom type membersGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_MembersGroupId_Type.__name__ = "Integer32"
_MembersGroupId_Object = MibTableColumn
membersGroupId = _MembersGroupId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 8, 5, 1, 1),
    _MembersGroupId_Type()
)
membersGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    membersGroupId.setStatus("mandatory")


class _MembersCarrierId_Type(Integer32):
    """Custom type membersCarrierId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_MembersCarrierId_Type.__name__ = "Integer32"
_MembersCarrierId_Object = MibTableColumn
membersCarrierId = _MembersCarrierId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 8, 5, 1, 2),
    _MembersCarrierId_Type()
)
membersCarrierId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    membersCarrierId.setStatus("mandatory")


class _MembersProtectionPriorityLevel_Type(Integer32):
    """Custom type membersProtectionPriorityLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("high", 4),
          ("normal", 3),
          ("void", 2))
    )


_MembersProtectionPriorityLevel_Type.__name__ = "Integer32"
_MembersProtectionPriorityLevel_Object = MibTableColumn
membersProtectionPriorityLevel = _MembersProtectionPriorityLevel_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 8, 5, 1, 3),
    _MembersProtectionPriorityLevel_Type()
)
membersProtectionPriorityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    membersProtectionPriorityLevel.setStatus("mandatory")
_Nplus1ProtectingTable_Object = MibTable
nplus1ProtectingTable = _Nplus1ProtectingTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 8, 6)
)
if mibBuilder.loadTexts:
    nplus1ProtectingTable.setStatus("mandatory")
_Nplus1ProtectingEntry_Object = MibTableRow
nplus1ProtectingEntry = _Nplus1ProtectingEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 8, 6, 1)
)
nplus1ProtectingEntry.setIndexNames(
    (0, "CERAGON-MIB", "nplus1ProtectingGroupId"),
)
if mibBuilder.loadTexts:
    nplus1ProtectingEntry.setStatus("mandatory")


class _Nplus1ProtectingGroupId_Type(Integer32):
    """Custom type nplus1ProtectingGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_Nplus1ProtectingGroupId_Type.__name__ = "Integer32"
_Nplus1ProtectingGroupId_Object = MibTableColumn
nplus1ProtectingGroupId = _Nplus1ProtectingGroupId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 8, 6, 1, 1),
    _Nplus1ProtectingGroupId_Type()
)
nplus1ProtectingGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nplus1ProtectingGroupId.setStatus("mandatory")


class _Nplus1ProtectingXCProtectionFraming_Type(Integer32):
    """Custom type nplus1ProtectingXCProtectionFraming based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("clear", 5),
          ("lof", 3),
          ("na", 2),
          ("noPeer", 4))
    )


_Nplus1ProtectingXCProtectionFraming_Type.__name__ = "Integer32"
_Nplus1ProtectingXCProtectionFraming_Object = MibTableColumn
nplus1ProtectingXCProtectionFraming = _Nplus1ProtectingXCProtectionFraming_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 8, 6, 1, 2),
    _Nplus1ProtectingXCProtectionFraming_Type()
)
nplus1ProtectingXCProtectionFraming.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nplus1ProtectingXCProtectionFraming.setStatus("mandatory")


class _Nplus1ProtectingProtectedLinkTx_Type(Integer32):
    """Custom type nplus1ProtectingProtectedLinkTx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Nplus1ProtectingProtectedLinkTx_Type.__name__ = "Integer32"
_Nplus1ProtectingProtectedLinkTx_Object = MibTableColumn
nplus1ProtectingProtectedLinkTx = _Nplus1ProtectingProtectedLinkTx_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 8, 6, 1, 3),
    _Nplus1ProtectingProtectedLinkTx_Type()
)
nplus1ProtectingProtectedLinkTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nplus1ProtectingProtectedLinkTx.setStatus("mandatory")


class _Nplus1ProtectingProtectedLinkRx_Type(Integer32):
    """Custom type nplus1ProtectingProtectedLinkRx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Nplus1ProtectingProtectedLinkRx_Type.__name__ = "Integer32"
_Nplus1ProtectingProtectedLinkRx_Object = MibTableColumn
nplus1ProtectingProtectedLinkRx = _Nplus1ProtectingProtectedLinkRx_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 8, 6, 1, 4),
    _Nplus1ProtectingProtectedLinkRx_Type()
)
nplus1ProtectingProtectedLinkRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nplus1ProtectingProtectedLinkRx.setStatus("mandatory")


class _Nplus1ProtectingRequestedLinkTx_Type(Integer32):
    """Custom type nplus1ProtectingRequestedLinkTx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Nplus1ProtectingRequestedLinkTx_Type.__name__ = "Integer32"
_Nplus1ProtectingRequestedLinkTx_Object = MibTableColumn
nplus1ProtectingRequestedLinkTx = _Nplus1ProtectingRequestedLinkTx_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 8, 6, 1, 5),
    _Nplus1ProtectingRequestedLinkTx_Type()
)
nplus1ProtectingRequestedLinkTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nplus1ProtectingRequestedLinkTx.setStatus("mandatory")


class _Nplus1ProtectingRequestedLinkRx_Type(Integer32):
    """Custom type nplus1ProtectingRequestedLinkRx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Nplus1ProtectingRequestedLinkRx_Type.__name__ = "Integer32"
_Nplus1ProtectingRequestedLinkRx_Object = MibTableColumn
nplus1ProtectingRequestedLinkRx = _Nplus1ProtectingRequestedLinkRx_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 8, 6, 1, 6),
    _Nplus1ProtectingRequestedLinkRx_Type()
)
nplus1ProtectingRequestedLinkRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nplus1ProtectingRequestedLinkRx.setStatus("mandatory")


class _Nplus1ProtectingSwitchToProtectingCommand_Type(Integer32):
    """Custom type nplus1ProtectingSwitchToProtectingCommand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(256,
              512,
              769,
              770,
              771,
              772,
              773,
              774,
              775,
              776,
              777,
              778,
              779,
              780,
              781,
              782,
              783,
              1025,
              1026,
              1027,
              1028,
              1029,
              1030,
              1031,
              1032,
              1033,
              1034,
              1035,
              1036,
              1037,
              1038,
              1039)
        )
    )
    namedValues = NamedValues(
        *(("force1", 769),
          ("force10", 778),
          ("force11", 779),
          ("force12", 780),
          ("force13", 781),
          ("force14", 782),
          ("force15", 783),
          ("force2", 770),
          ("force3", 771),
          ("force4", 772),
          ("force5", 773),
          ("force6", 774),
          ("force7", 775),
          ("force8", 776),
          ("force9", 777),
          ("lockout", 512),
          ("noaction", 256),
          ("request1", 1025),
          ("request10", 1034),
          ("request11", 1035),
          ("request12", 1036),
          ("request13", 1037),
          ("request14", 1038),
          ("request15", 1039),
          ("request2", 1026),
          ("request3", 1027),
          ("request4", 1028),
          ("request5", 1029),
          ("request6", 1030),
          ("request7", 1031),
          ("request8", 1032),
          ("request9", 1033))
    )


_Nplus1ProtectingSwitchToProtectingCommand_Type.__name__ = "Integer32"
_Nplus1ProtectingSwitchToProtectingCommand_Object = MibTableColumn
nplus1ProtectingSwitchToProtectingCommand = _Nplus1ProtectingSwitchToProtectingCommand_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 8, 6, 1, 7),
    _Nplus1ProtectingSwitchToProtectingCommand_Type()
)
nplus1ProtectingSwitchToProtectingCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nplus1ProtectingSwitchToProtectingCommand.setStatus("mandatory")
_CarrierProtectionTable_Object = MibTable
carrierProtectionTable = _CarrierProtectionTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 8, 7)
)
if mibBuilder.loadTexts:
    carrierProtectionTable.setStatus("mandatory")
_CarrierProtectionEntry_Object = MibTableRow
carrierProtectionEntry = _CarrierProtectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 8, 7, 1)
)
carrierProtectionEntry.setIndexNames(
    (0, "CERAGON-MIB", "carrierProtectionXCId"),
    (0, "CERAGON-MIB", "carrierProtectionCarrierId"),
)
if mibBuilder.loadTexts:
    carrierProtectionEntry.setStatus("mandatory")


class _CarrierProtectionXCId_Type(Integer32):
    """Custom type carrierProtectionXCId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_CarrierProtectionXCId_Type.__name__ = "Integer32"
_CarrierProtectionXCId_Object = MibTableColumn
carrierProtectionXCId = _CarrierProtectionXCId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 8, 7, 1, 1),
    _CarrierProtectionXCId_Type()
)
carrierProtectionXCId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carrierProtectionXCId.setStatus("mandatory")


class _CarrierProtectionCarrierId_Type(Integer32):
    """Custom type carrierProtectionCarrierId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_CarrierProtectionCarrierId_Type.__name__ = "Integer32"
_CarrierProtectionCarrierId_Object = MibTableColumn
carrierProtectionCarrierId = _CarrierProtectionCarrierId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 8, 7, 1, 2),
    _CarrierProtectionCarrierId_Type()
)
carrierProtectionCarrierId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carrierProtectionCarrierId.setStatus("mandatory")


class _CarrierProtectionLinkGroupNum_Type(Integer32):
    """Custom type carrierProtectionLinkGroupNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("group1", 3),
          ("group2", 4),
          ("group3", 5),
          ("group4", 6),
          ("standalone", 2))
    )


_CarrierProtectionLinkGroupNum_Type.__name__ = "Integer32"
_CarrierProtectionLinkGroupNum_Object = MibTableColumn
carrierProtectionLinkGroupNum = _CarrierProtectionLinkGroupNum_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 8, 7, 1, 3),
    _CarrierProtectionLinkGroupNum_Type()
)
carrierProtectionLinkGroupNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carrierProtectionLinkGroupNum.setStatus("mandatory")


class _CarrierProtectionServedByRemoteXC_Type(Integer32):
    """Custom type carrierProtectionServedByRemoteXC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("na", 2),
          ("no", 4),
          ("yes", 3))
    )


_CarrierProtectionServedByRemoteXC_Type.__name__ = "Integer32"
_CarrierProtectionServedByRemoteXC_Object = MibTableColumn
carrierProtectionServedByRemoteXC = _CarrierProtectionServedByRemoteXC_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 8, 7, 1, 4),
    _CarrierProtectionServedByRemoteXC_Type()
)
carrierProtectionServedByRemoteXC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carrierProtectionServedByRemoteXC.setStatus("mandatory")


class _CarrierProtectionRadioStatus_Type(Integer32):
    """Custom type carrierProtectionRadioStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("bbexb", 5),
          ("bblof", 4),
          ("bbsd", 6),
          ("clear", 8),
          ("ew", 7),
          ("na", 2),
          ("off", 3))
    )


_CarrierProtectionRadioStatus_Type.__name__ = "Integer32"
_CarrierProtectionRadioStatus_Object = MibTableColumn
carrierProtectionRadioStatus = _CarrierProtectionRadioStatus_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 8, 7, 1, 5),
    _CarrierProtectionRadioStatus_Type()
)
carrierProtectionRadioStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carrierProtectionRadioStatus.setStatus("mandatory")


class _CarrierProtectionLineFraming_Type(Integer32):
    """Custom type carrierProtectionLineFraming based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("clear", 4),
          ("lof", 3),
          ("na", 2))
    )


_CarrierProtectionLineFraming_Type.__name__ = "Integer32"
_CarrierProtectionLineFraming_Object = MibTableColumn
carrierProtectionLineFraming = _CarrierProtectionLineFraming_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 8, 7, 1, 6),
    _CarrierProtectionLineFraming_Type()
)
carrierProtectionLineFraming.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carrierProtectionLineFraming.setStatus("mandatory")


class _CarrierProtectionLoopback_Type(Integer32):
    """Custom type carrierProtectionLoopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("external", 4),
          ("none", 3))
    )


_CarrierProtectionLoopback_Type.__name__ = "Integer32"
_CarrierProtectionLoopback_Object = MibTableColumn
carrierProtectionLoopback = _CarrierProtectionLoopback_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 8, 7, 1, 7),
    _CarrierProtectionLoopback_Type()
)
carrierProtectionLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    carrierProtectionLoopback.setStatus("mandatory")


class _CarrierProtectionLoopbackTimer_Type(Integer32):
    """Custom type carrierProtectionLoopbackTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_CarrierProtectionLoopbackTimer_Type.__name__ = "Integer32"
_CarrierProtectionLoopbackTimer_Object = MibTableColumn
carrierProtectionLoopbackTimer = _CarrierProtectionLoopbackTimer_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 8, 7, 1, 8),
    _CarrierProtectionLoopbackTimer_Type()
)
carrierProtectionLoopbackTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carrierProtectionLoopbackTimer.setStatus("mandatory")
_Nplus1StandardPMCurrTable_Object = MibTable
nplus1StandardPMCurrTable = _Nplus1StandardPMCurrTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 8, 8)
)
if mibBuilder.loadTexts:
    nplus1StandardPMCurrTable.setStatus("mandatory")
_Nplus1StandardPMCurrEntry_Object = MibTableRow
nplus1StandardPMCurrEntry = _Nplus1StandardPMCurrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 8, 8, 1)
)
nplus1StandardPMCurrEntry.setIndexNames(
    (0, "CERAGON-MIB", "nplus1StandardPMCurrCarrierId"),
)
if mibBuilder.loadTexts:
    nplus1StandardPMCurrEntry.setStatus("mandatory")


class _Nplus1StandardPMCurrCarrierId_Type(Integer32):
    """Custom type nplus1StandardPMCurrCarrierId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Nplus1StandardPMCurrCarrierId_Type.__name__ = "Integer32"
_Nplus1StandardPMCurrCarrierId_Object = MibTableColumn
nplus1StandardPMCurrCarrierId = _Nplus1StandardPMCurrCarrierId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 8, 8, 1, 1),
    _Nplus1StandardPMCurrCarrierId_Type()
)
nplus1StandardPMCurrCarrierId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nplus1StandardPMCurrCarrierId.setStatus("mandatory")


class _Nplus1StandardPMCurrTimeElapsed_Type(Integer32):
    """Custom type nplus1StandardPMCurrTimeElapsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 900),
    )


_Nplus1StandardPMCurrTimeElapsed_Type.__name__ = "Integer32"
_Nplus1StandardPMCurrTimeElapsed_Object = MibTableColumn
nplus1StandardPMCurrTimeElapsed = _Nplus1StandardPMCurrTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 8, 8, 1, 2),
    _Nplus1StandardPMCurrTimeElapsed_Type()
)
nplus1StandardPMCurrTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nplus1StandardPMCurrTimeElapsed.setStatus("mandatory")


class _Nplus1StandardPMCurrValidIntervals_Type(Integer32):
    """Custom type nplus1StandardPMCurrValidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_Nplus1StandardPMCurrValidIntervals_Type.__name__ = "Integer32"
_Nplus1StandardPMCurrValidIntervals_Object = MibTableColumn
nplus1StandardPMCurrValidIntervals = _Nplus1StandardPMCurrValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 8, 8, 1, 3),
    _Nplus1StandardPMCurrValidIntervals_Type()
)
nplus1StandardPMCurrValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nplus1StandardPMCurrValidIntervals.setStatus("mandatory")


class _Nplus1StandardPMCurrLastDayIDF_Type(Integer32):
    """Custom type nplus1StandardPMCurrLastDayIDF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3))
    )


_Nplus1StandardPMCurrLastDayIDF_Type.__name__ = "Integer32"
_Nplus1StandardPMCurrLastDayIDF_Object = MibTableColumn
nplus1StandardPMCurrLastDayIDF = _Nplus1StandardPMCurrLastDayIDF_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 8, 8, 1, 4),
    _Nplus1StandardPMCurrLastDayIDF_Type()
)
nplus1StandardPMCurrLastDayIDF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nplus1StandardPMCurrLastDayIDF.setStatus("mandatory")


class _Nplus1StandardPMCurrLastDayGroupNum_Type(Integer32):
    """Custom type nplus1StandardPMCurrLastDayGroupNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 4),
    )


_Nplus1StandardPMCurrLastDayGroupNum_Type.__name__ = "Integer32"
_Nplus1StandardPMCurrLastDayGroupNum_Object = MibTableColumn
nplus1StandardPMCurrLastDayGroupNum = _Nplus1StandardPMCurrLastDayGroupNum_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 8, 8, 1, 5),
    _Nplus1StandardPMCurrLastDayGroupNum_Type()
)
nplus1StandardPMCurrLastDayGroupNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nplus1StandardPMCurrLastDayGroupNum.setStatus("mandatory")
_Nplus1StandardPMCurrPSAC_Type = Gauge32
_Nplus1StandardPMCurrPSAC_Object = MibTableColumn
nplus1StandardPMCurrPSAC = _Nplus1StandardPMCurrPSAC_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 8, 8, 1, 6),
    _Nplus1StandardPMCurrPSAC_Type()
)
nplus1StandardPMCurrPSAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nplus1StandardPMCurrPSAC.setStatus("mandatory")
_Nplus1StandardPMCurrFSRC_Type = Gauge32
_Nplus1StandardPMCurrFSRC_Object = MibTableColumn
nplus1StandardPMCurrFSRC = _Nplus1StandardPMCurrFSRC_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 8, 8, 1, 7),
    _Nplus1StandardPMCurrFSRC_Type()
)
nplus1StandardPMCurrFSRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nplus1StandardPMCurrFSRC.setStatus("mandatory")
_Nplus1StandardPMCurrPSAD_Type = Gauge32
_Nplus1StandardPMCurrPSAD_Object = MibTableColumn
nplus1StandardPMCurrPSAD = _Nplus1StandardPMCurrPSAD_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 8, 8, 1, 8),
    _Nplus1StandardPMCurrPSAD_Type()
)
nplus1StandardPMCurrPSAD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nplus1StandardPMCurrPSAD.setStatus("mandatory")
_Nplus1StandardPMCurrFSRD_Type = Gauge32
_Nplus1StandardPMCurrFSRD_Object = MibTableColumn
nplus1StandardPMCurrFSRD = _Nplus1StandardPMCurrFSRD_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 8, 8, 1, 9),
    _Nplus1StandardPMCurrFSRD_Type()
)
nplus1StandardPMCurrFSRD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nplus1StandardPMCurrFSRD.setStatus("mandatory")
_Nplus1StandardPMCurrLastDayPSAC_Type = Gauge32
_Nplus1StandardPMCurrLastDayPSAC_Object = MibTableColumn
nplus1StandardPMCurrLastDayPSAC = _Nplus1StandardPMCurrLastDayPSAC_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 8, 8, 1, 10),
    _Nplus1StandardPMCurrLastDayPSAC_Type()
)
nplus1StandardPMCurrLastDayPSAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nplus1StandardPMCurrLastDayPSAC.setStatus("mandatory")
_Nplus1StandardPMCurrLastDayFSRC_Type = Gauge32
_Nplus1StandardPMCurrLastDayFSRC_Object = MibTableColumn
nplus1StandardPMCurrLastDayFSRC = _Nplus1StandardPMCurrLastDayFSRC_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 8, 8, 1, 11),
    _Nplus1StandardPMCurrLastDayFSRC_Type()
)
nplus1StandardPMCurrLastDayFSRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nplus1StandardPMCurrLastDayFSRC.setStatus("mandatory")
_Nplus1StandardPMCurrLastDayPSAD_Type = Gauge32
_Nplus1StandardPMCurrLastDayPSAD_Object = MibTableColumn
nplus1StandardPMCurrLastDayPSAD = _Nplus1StandardPMCurrLastDayPSAD_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 8, 8, 1, 12),
    _Nplus1StandardPMCurrLastDayPSAD_Type()
)
nplus1StandardPMCurrLastDayPSAD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nplus1StandardPMCurrLastDayPSAD.setStatus("mandatory")
_Nplus1StandardPMCurrLastDayFSRD_Type = Gauge32
_Nplus1StandardPMCurrLastDayFSRD_Object = MibTableColumn
nplus1StandardPMCurrLastDayFSRD = _Nplus1StandardPMCurrLastDayFSRD_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 8, 8, 1, 13),
    _Nplus1StandardPMCurrLastDayFSRD_Type()
)
nplus1StandardPMCurrLastDayFSRD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nplus1StandardPMCurrLastDayFSRD.setStatus("mandatory")
_Nplus1StandardPMIntervalTable_Object = MibTable
nplus1StandardPMIntervalTable = _Nplus1StandardPMIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 8, 9)
)
if mibBuilder.loadTexts:
    nplus1StandardPMIntervalTable.setStatus("mandatory")
_Nplus1StandardPMIntervalEntry_Object = MibTableRow
nplus1StandardPMIntervalEntry = _Nplus1StandardPMIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 8, 9, 1)
)
nplus1StandardPMIntervalEntry.setIndexNames(
    (0, "CERAGON-MIB", "nplus1StandardPMIntervalCarrierId"),
    (0, "CERAGON-MIB", "nplus1StandardPMIntervalIdx"),
)
if mibBuilder.loadTexts:
    nplus1StandardPMIntervalEntry.setStatus("mandatory")


class _Nplus1StandardPMIntervalCarrierId_Type(Integer32):
    """Custom type nplus1StandardPMIntervalCarrierId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Nplus1StandardPMIntervalCarrierId_Type.__name__ = "Integer32"
_Nplus1StandardPMIntervalCarrierId_Object = MibTableColumn
nplus1StandardPMIntervalCarrierId = _Nplus1StandardPMIntervalCarrierId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 8, 9, 1, 1),
    _Nplus1StandardPMIntervalCarrierId_Type()
)
nplus1StandardPMIntervalCarrierId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nplus1StandardPMIntervalCarrierId.setStatus("mandatory")


class _Nplus1StandardPMIntervalIdx_Type(Integer32):
    """Custom type nplus1StandardPMIntervalIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_Nplus1StandardPMIntervalIdx_Type.__name__ = "Integer32"
_Nplus1StandardPMIntervalIdx_Object = MibTableColumn
nplus1StandardPMIntervalIdx = _Nplus1StandardPMIntervalIdx_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 8, 9, 1, 2),
    _Nplus1StandardPMIntervalIdx_Type()
)
nplus1StandardPMIntervalIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nplus1StandardPMIntervalIdx.setStatus("mandatory")


class _Nplus1StandardPMIntervalIDF_Type(Integer32):
    """Custom type nplus1StandardPMIntervalIDF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3))
    )


_Nplus1StandardPMIntervalIDF_Type.__name__ = "Integer32"
_Nplus1StandardPMIntervalIDF_Object = MibTableColumn
nplus1StandardPMIntervalIDF = _Nplus1StandardPMIntervalIDF_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 8, 9, 1, 3),
    _Nplus1StandardPMIntervalIDF_Type()
)
nplus1StandardPMIntervalIDF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nplus1StandardPMIntervalIDF.setStatus("mandatory")


class _Nplus1StandardPMIntervalGroupNum_Type(Integer32):
    """Custom type nplus1StandardPMIntervalGroupNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 4),
    )


_Nplus1StandardPMIntervalGroupNum_Type.__name__ = "Integer32"
_Nplus1StandardPMIntervalGroupNum_Object = MibTableColumn
nplus1StandardPMIntervalGroupNum = _Nplus1StandardPMIntervalGroupNum_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 8, 9, 1, 4),
    _Nplus1StandardPMIntervalGroupNum_Type()
)
nplus1StandardPMIntervalGroupNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nplus1StandardPMIntervalGroupNum.setStatus("mandatory")
_Nplus1StandardPMIntervalPSAC_Type = Gauge32
_Nplus1StandardPMIntervalPSAC_Object = MibTableColumn
nplus1StandardPMIntervalPSAC = _Nplus1StandardPMIntervalPSAC_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 8, 9, 1, 5),
    _Nplus1StandardPMIntervalPSAC_Type()
)
nplus1StandardPMIntervalPSAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nplus1StandardPMIntervalPSAC.setStatus("mandatory")
_Nplus1StandardPMIntervalFSRC_Type = Gauge32
_Nplus1StandardPMIntervalFSRC_Object = MibTableColumn
nplus1StandardPMIntervalFSRC = _Nplus1StandardPMIntervalFSRC_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 8, 9, 1, 6),
    _Nplus1StandardPMIntervalFSRC_Type()
)
nplus1StandardPMIntervalFSRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nplus1StandardPMIntervalFSRC.setStatus("mandatory")
_Nplus1StandardPMIntervalPSAD_Type = Gauge32
_Nplus1StandardPMIntervalPSAD_Object = MibTableColumn
nplus1StandardPMIntervalPSAD = _Nplus1StandardPMIntervalPSAD_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 8, 9, 1, 7),
    _Nplus1StandardPMIntervalPSAD_Type()
)
nplus1StandardPMIntervalPSAD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nplus1StandardPMIntervalPSAD.setStatus("mandatory")
_Nplus1StandardPMIntervalFSRD_Type = Gauge32
_Nplus1StandardPMIntervalFSRD_Object = MibTableColumn
nplus1StandardPMIntervalFSRD = _Nplus1StandardPMIntervalFSRD_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 8, 9, 1, 8),
    _Nplus1StandardPMIntervalFSRD_Type()
)
nplus1StandardPMIntervalFSRD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nplus1StandardPMIntervalFSRD.setStatus("mandatory")
_Nplus1StandardPMDayTable_Object = MibTable
nplus1StandardPMDayTable = _Nplus1StandardPMDayTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 8, 10)
)
if mibBuilder.loadTexts:
    nplus1StandardPMDayTable.setStatus("mandatory")
_Nplus1StandardPMDayEntry_Object = MibTableRow
nplus1StandardPMDayEntry = _Nplus1StandardPMDayEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 8, 10, 1)
)
nplus1StandardPMDayEntry.setIndexNames(
    (0, "CERAGON-MIB", "nplus1StandardPMDayCarrierId"),
    (0, "CERAGON-MIB", "nplus1StandardPMDayIdx"),
)
if mibBuilder.loadTexts:
    nplus1StandardPMDayEntry.setStatus("mandatory")


class _Nplus1StandardPMDayCarrierId_Type(Integer32):
    """Custom type nplus1StandardPMDayCarrierId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Nplus1StandardPMDayCarrierId_Type.__name__ = "Integer32"
_Nplus1StandardPMDayCarrierId_Object = MibTableColumn
nplus1StandardPMDayCarrierId = _Nplus1StandardPMDayCarrierId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 8, 10, 1, 1),
    _Nplus1StandardPMDayCarrierId_Type()
)
nplus1StandardPMDayCarrierId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nplus1StandardPMDayCarrierId.setStatus("mandatory")


class _Nplus1StandardPMDayIdx_Type(Integer32):
    """Custom type nplus1StandardPMDayIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_Nplus1StandardPMDayIdx_Type.__name__ = "Integer32"
_Nplus1StandardPMDayIdx_Object = MibTableColumn
nplus1StandardPMDayIdx = _Nplus1StandardPMDayIdx_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 8, 10, 1, 2),
    _Nplus1StandardPMDayIdx_Type()
)
nplus1StandardPMDayIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nplus1StandardPMDayIdx.setStatus("mandatory")


class _Nplus1StandardPMDayIDF_Type(Integer32):
    """Custom type nplus1StandardPMDayIDF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3))
    )


_Nplus1StandardPMDayIDF_Type.__name__ = "Integer32"
_Nplus1StandardPMDayIDF_Object = MibTableColumn
nplus1StandardPMDayIDF = _Nplus1StandardPMDayIDF_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 8, 10, 1, 3),
    _Nplus1StandardPMDayIDF_Type()
)
nplus1StandardPMDayIDF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nplus1StandardPMDayIDF.setStatus("mandatory")


class _Nplus1StandardPMDayGroupNum_Type(Integer32):
    """Custom type nplus1StandardPMDayGroupNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 4),
    )


_Nplus1StandardPMDayGroupNum_Type.__name__ = "Integer32"
_Nplus1StandardPMDayGroupNum_Object = MibTableColumn
nplus1StandardPMDayGroupNum = _Nplus1StandardPMDayGroupNum_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 8, 10, 1, 4),
    _Nplus1StandardPMDayGroupNum_Type()
)
nplus1StandardPMDayGroupNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nplus1StandardPMDayGroupNum.setStatus("mandatory")
_Nplus1StandardPMDayPSAC_Type = Gauge32
_Nplus1StandardPMDayPSAC_Object = MibTableColumn
nplus1StandardPMDayPSAC = _Nplus1StandardPMDayPSAC_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 8, 10, 1, 5),
    _Nplus1StandardPMDayPSAC_Type()
)
nplus1StandardPMDayPSAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nplus1StandardPMDayPSAC.setStatus("mandatory")
_Nplus1StandardPMDayFSRC_Type = Gauge32
_Nplus1StandardPMDayFSRC_Object = MibTableColumn
nplus1StandardPMDayFSRC = _Nplus1StandardPMDayFSRC_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 8, 10, 1, 6),
    _Nplus1StandardPMDayFSRC_Type()
)
nplus1StandardPMDayFSRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nplus1StandardPMDayFSRC.setStatus("mandatory")
_Nplus1StandardPMDayPSAD_Type = Gauge32
_Nplus1StandardPMDayPSAD_Object = MibTableColumn
nplus1StandardPMDayPSAD = _Nplus1StandardPMDayPSAD_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 8, 10, 1, 7),
    _Nplus1StandardPMDayPSAD_Type()
)
nplus1StandardPMDayPSAD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nplus1StandardPMDayPSAD.setStatus("mandatory")
_Nplus1StandardPMDayFSRD_Type = Gauge32
_Nplus1StandardPMDayFSRD_Object = MibTableColumn
nplus1StandardPMDayFSRD = _Nplus1StandardPMDayFSRD_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 3, 8, 10, 1, 8),
    _Nplus1StandardPMDayFSRD_Type()
)
nplus1StandardPMDayFSRD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nplus1StandardPMDayFSRD.setStatus("mandatory")
_GnSSM_ObjectIdentity = ObjectIdentity
gnSSM = _GnSSM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 3, 4)
)
_GnSSMCfg_ObjectIdentity = ObjectIdentity
gnSSMCfg = _GnSSMCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 3, 4, 1)
)


class _GnSSMCfgSSMMode_Type(Integer32):
    """Custom type gnSSMCfgSSMMode based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2))
    )


_GnSSMCfgSSMMode_Type.__name__ = "Integer32"
_GnSSMCfgSSMMode_Object = MibScalar
gnSSMCfgSSMMode = _GnSSMCfgSSMMode_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 4, 1, 1),
    _GnSSMCfgSSMMode_Type()
)
gnSSMCfgSSMMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnSSMCfgSSMMode.setStatus("mandatory")


class _GnSSMCfgPrimaryClockSource_Type(Integer32):
    """Custom type gnSSMCfgPrimaryClockSource based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
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
              24)
        )
    )
    namedValues = NamedValues(
        *(("external1AndHalfMB", 7),
          ("external2MB", 3),
          ("external2MHz", 6),
          ("fiberClock", 5),
          ("internalClock", 2),
          ("radioClock", 4),
          ("tribSTM1", 24),
          ("tributaryClock1", 8),
          ("tributaryClock10", 17),
          ("tributaryClock11", 18),
          ("tributaryClock12", 19),
          ("tributaryClock13", 20),
          ("tributaryClock14", 21),
          ("tributaryClock15", 22),
          ("tributaryClock16", 23),
          ("tributaryClock2", 9),
          ("tributaryClock3", 10),
          ("tributaryClock4", 11),
          ("tributaryClock5", 12),
          ("tributaryClock6", 13),
          ("tributaryClock7", 14),
          ("tributaryClock8", 15),
          ("tributaryClock9", 16))
    )


_GnSSMCfgPrimaryClockSource_Type.__name__ = "Integer32"
_GnSSMCfgPrimaryClockSource_Object = MibScalar
gnSSMCfgPrimaryClockSource = _GnSSMCfgPrimaryClockSource_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 4, 1, 2),
    _GnSSMCfgPrimaryClockSource_Type()
)
gnSSMCfgPrimaryClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnSSMCfgPrimaryClockSource.setStatus("mandatory")


class _GnSSMCfgPrimaryClockQuality_Type(Integer32):
    """Custom type gnSSMCfgPrimaryClockQuality based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_GnSSMCfgPrimaryClockQuality_Type.__name__ = "Integer32"
_GnSSMCfgPrimaryClockQuality_Object = MibScalar
gnSSMCfgPrimaryClockQuality = _GnSSMCfgPrimaryClockQuality_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 4, 1, 3),
    _GnSSMCfgPrimaryClockQuality_Type()
)
gnSSMCfgPrimaryClockQuality.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnSSMCfgPrimaryClockQuality.setStatus("mandatory")


class _GnSSMCfgSecondaryClockSource_Type(Integer32):
    """Custom type gnSSMCfgSecondaryClockSource based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
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
              24)
        )
    )
    namedValues = NamedValues(
        *(("external1AndHalfMB", 7),
          ("external2MB", 3),
          ("external2MHz", 6),
          ("fiberClock", 5),
          ("internalClock", 2),
          ("radioClock", 4),
          ("tribSTM1", 24),
          ("tributaryClock1", 8),
          ("tributaryClock10", 17),
          ("tributaryClock11", 18),
          ("tributaryClock12", 19),
          ("tributaryClock13", 20),
          ("tributaryClock14", 21),
          ("tributaryClock15", 22),
          ("tributaryClock16", 23),
          ("tributaryClock2", 9),
          ("tributaryClock3", 10),
          ("tributaryClock4", 11),
          ("tributaryClock5", 12),
          ("tributaryClock6", 13),
          ("tributaryClock7", 14),
          ("tributaryClock8", 15),
          ("tributaryClock9", 16))
    )


_GnSSMCfgSecondaryClockSource_Type.__name__ = "Integer32"
_GnSSMCfgSecondaryClockSource_Object = MibScalar
gnSSMCfgSecondaryClockSource = _GnSSMCfgSecondaryClockSource_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 4, 1, 4),
    _GnSSMCfgSecondaryClockSource_Type()
)
gnSSMCfgSecondaryClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnSSMCfgSecondaryClockSource.setStatus("mandatory")


class _GnSSMCfgSecondaryClockQuality_Type(Integer32):
    """Custom type gnSSMCfgSecondaryClockQuality based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_GnSSMCfgSecondaryClockQuality_Type.__name__ = "Integer32"
_GnSSMCfgSecondaryClockQuality_Object = MibScalar
gnSSMCfgSecondaryClockQuality = _GnSSMCfgSecondaryClockQuality_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 4, 1, 5),
    _GnSSMCfgSecondaryClockQuality_Type()
)
gnSSMCfgSecondaryClockQuality.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnSSMCfgSecondaryClockQuality.setStatus("mandatory")


class _GnSSMCfgClockUserCommand_Type(Integer32):
    """Custom type gnSSMCfgClockUserCommand based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 2),
          ("switchToInternalClock", 5),
          ("switchToPrimaryClock", 3),
          ("switchToSecondaryClock", 4))
    )


_GnSSMCfgClockUserCommand_Type.__name__ = "Integer32"
_GnSSMCfgClockUserCommand_Object = MibScalar
gnSSMCfgClockUserCommand = _GnSSMCfgClockUserCommand_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 4, 1, 6),
    _GnSSMCfgClockUserCommand_Type()
)
gnSSMCfgClockUserCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnSSMCfgClockUserCommand.setStatus("mandatory")


class _GnSSMCfgClockOutputMute_Type(Integer32):
    """Custom type gnSSMCfgClockOutputMute based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 3),
          ("on", 2))
    )


_GnSSMCfgClockOutputMute_Type.__name__ = "Integer32"
_GnSSMCfgClockOutputMute_Object = MibScalar
gnSSMCfgClockOutputMute = _GnSSMCfgClockOutputMute_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 4, 1, 7),
    _GnSSMCfgClockOutputMute_Type()
)
gnSSMCfgClockOutputMute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnSSMCfgClockOutputMute.setStatus("mandatory")
_GnSSMStat_ObjectIdentity = ObjectIdentity
gnSSMStat = _GnSSMStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 3, 4, 2)
)


class _GnSSMStatStatus_Type(OctetString):
    """Custom type gnSSMStatStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_GnSSMStatStatus_Type.__name__ = "OctetString"
_GnSSMStatStatus_Object = MibScalar
gnSSMStatStatus = _GnSSMStatStatus_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 4, 2, 1),
    _GnSSMStatStatus_Type()
)
gnSSMStatStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnSSMStatStatus.setStatus("mandatory")


class _GnSSMStatCurrentClock_Type(Integer32):
    """Custom type gnSSMStatCurrentClock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("holdOver", 5),
          ("internal", 4),
          ("primary", 2),
          ("secondary", 3))
    )


_GnSSMStatCurrentClock_Type.__name__ = "Integer32"
_GnSSMStatCurrentClock_Object = MibScalar
gnSSMStatCurrentClock = _GnSSMStatCurrentClock_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 4, 2, 2),
    _GnSSMStatCurrentClock_Type()
)
gnSSMStatCurrentClock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnSSMStatCurrentClock.setStatus("mandatory")


class _GnSSMStatCurrentClockQuality_Type(Integer32):
    """Custom type gnSSMStatCurrentClockQuality based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_GnSSMStatCurrentClockQuality_Type.__name__ = "Integer32"
_GnSSMStatCurrentClockQuality_Object = MibScalar
gnSSMStatCurrentClockQuality = _GnSSMStatCurrentClockQuality_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 4, 2, 3),
    _GnSSMStatCurrentClockQuality_Type()
)
gnSSMStatCurrentClockQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnSSMStatCurrentClockQuality.setStatus("mandatory")


class _GnSSMStatClockUnitType_Type(Integer32):
    """Custom type gnSSMStatClockUnitType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("noClockUnit", 2),
          ("sec", 4),
          ("smc", 3),
          ("st3", 5),
          ("st3e", 6))
    )


_GnSSMStatClockUnitType_Type.__name__ = "Integer32"
_GnSSMStatClockUnitType_Object = MibScalar
gnSSMStatClockUnitType = _GnSSMStatClockUnitType_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 4, 2, 4),
    _GnSSMStatClockUnitType_Type()
)
gnSSMStatClockUnitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnSSMStatClockUnitType.setStatus("mandatory")


class _GnSSMStatHoldoverPeriod_Type(Integer32):
    """Custom type gnSSMStatHoldoverPeriod based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2880),
    )


_GnSSMStatHoldoverPeriod_Type.__name__ = "Integer32"
_GnSSMStatHoldoverPeriod_Object = MibScalar
gnSSMStatHoldoverPeriod = _GnSSMStatHoldoverPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2281, 3, 4, 2, 5),
    _GnSSMStatHoldoverPeriod_Type()
)
gnSSMStatHoldoverPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnSSMStatHoldoverPeriod.setStatus("mandatory")
_GnAccess_ObjectIdentity = ObjectIdentity
gnAccess = _GnAccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 4)
)
_GnAccessCfg_ObjectIdentity = ObjectIdentity
gnAccessCfg = _GnAccessCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 4, 1)
)
_GnAccessCfgTable_Object = MibTable
gnAccessCfgTable = _GnAccessCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 1, 1)
)
if mibBuilder.loadTexts:
    gnAccessCfgTable.setStatus("mandatory")
_GnAccessCfgEntry_Object = MibTableRow
gnAccessCfgEntry = _GnAccessCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 1, 1, 1)
)
gnAccessCfgEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    gnAccessCfgEntry.setStatus("mandatory")


class _GnAccessCfgLongCableOption_Type(Integer32):
    """Custom type gnAccessCfgLongCableOption based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
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
        *(("anyLength", 9),
          ("ds3LongCable", 3),
          ("ds3ShortCable", 2),
          ("t1FA640From0to110ft", 10),
          ("t1FA640From110to220ft", 11),
          ("t1FA640From220to330ft", 12),
          ("t1FA640From330to440ft", 13),
          ("t1FA640From440to550ft", 14),
          ("t1From0to133ft", 4),
          ("t1From133to266ft", 5),
          ("t1From266to399ft", 6),
          ("t1From399to533ft", 7),
          ("t1From533to655ft", 8))
    )


_GnAccessCfgLongCableOption_Type.__name__ = "Integer32"
_GnAccessCfgLongCableOption_Object = MibTableColumn
gnAccessCfgLongCableOption = _GnAccessCfgLongCableOption_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 1, 1, 1, 1),
    _GnAccessCfgLongCableOption_Type()
)
gnAccessCfgLongCableOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnAccessCfgLongCableOption.setStatus("mandatory")


class _GnAccessCfgLoopbackOption_Type(Integer32):
    """Custom type gnAccessCfgLoopbackOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("interfaceExterLoop", 4),
          ("interfaceInterLoop", 3),
          ("noloopback", 2))
    )


_GnAccessCfgLoopbackOption_Type.__name__ = "Integer32"
_GnAccessCfgLoopbackOption_Object = MibTableColumn
gnAccessCfgLoopbackOption = _GnAccessCfgLoopbackOption_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 1, 1, 1, 2),
    _GnAccessCfgLoopbackOption_Type()
)
gnAccessCfgLoopbackOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnAccessCfgLoopbackOption.setStatus("mandatory")


class _GnAccessCfgRunPrbs_Type(Integer32):
    """Custom type gnAccessCfgRunPrbs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
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
        *(("lineOffRadioOffRcvLine", 9),
          ("lineOffRadioOffRcvRadio", 10),
          ("lineOffRadioOnRcvLine", 7),
          ("lineOffRadioOnRcvOff", 12),
          ("lineOffRadioOnRcvRadio", 8),
          ("lineOnRadioOffRcvLine", 5),
          ("lineOnRadioOffRcvOff", 13),
          ("lineOnRadioOffRcvRadio", 6),
          ("lineOnRadioOnRcvLine", 3),
          ("lineOnRadioOnRcvOff", 11),
          ("lineOnRadioOnRcvRadio", 4),
          ("noOperation", 2))
    )


_GnAccessCfgRunPrbs_Type.__name__ = "Integer32"
_GnAccessCfgRunPrbs_Object = MibTableColumn
gnAccessCfgRunPrbs = _GnAccessCfgRunPrbs_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 1, 1, 1, 3),
    _GnAccessCfgRunPrbs_Type()
)
gnAccessCfgRunPrbs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnAccessCfgRunPrbs.setStatus("mandatory")


class _GnAccessCfgEXCThresh_Type(Integer32):
    """Custom type gnAccessCfgEXCThresh based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("tenExpMinus3", 2),
          ("tenExpMinus4", 3),
          ("tenExpMinus5", 4))
    )


_GnAccessCfgEXCThresh_Type.__name__ = "Integer32"
_GnAccessCfgEXCThresh_Object = MibTableColumn
gnAccessCfgEXCThresh = _GnAccessCfgEXCThresh_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 1, 1, 1, 4),
    _GnAccessCfgEXCThresh_Type()
)
gnAccessCfgEXCThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnAccessCfgEXCThresh.setStatus("mandatory")


class _GnAccessCfgSDThresh_Type(Integer32):
    """Custom type gnAccessCfgSDThresh based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("tenExpMinus6", 3),
          ("tenExpMinus7", 4),
          ("tenExpMinus8", 5),
          ("tenExpMinus9", 6))
    )


_GnAccessCfgSDThresh_Type.__name__ = "Integer32"
_GnAccessCfgSDThresh_Object = MibTableColumn
gnAccessCfgSDThresh = _GnAccessCfgSDThresh_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 1, 1, 1, 5),
    _GnAccessCfgSDThresh_Type()
)
gnAccessCfgSDThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnAccessCfgSDThresh.setStatus("mandatory")


class _GnAccessCfgTest_Type(Integer32):
    """Custom type gnAccessCfgTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 2),
          ("sendAIS", 3))
    )


_GnAccessCfgTest_Type.__name__ = "Integer32"
_GnAccessCfgTest_Object = MibTableColumn
gnAccessCfgTest = _GnAccessCfgTest_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 1, 1, 1, 6),
    _GnAccessCfgTest_Type()
)
gnAccessCfgTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnAccessCfgTest.setStatus("mandatory")


class _GnAccessCfgLineCoding_Type(Integer32):
    """Custom type gnAccessCfgLineCoding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ami", 2),
          ("b3zs", 5),
          ("b8zs", 3),
          ("hdb3", 4))
    )


_GnAccessCfgLineCoding_Type.__name__ = "Integer32"
_GnAccessCfgLineCoding_Object = MibTableColumn
gnAccessCfgLineCoding = _GnAccessCfgLineCoding_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 1, 1, 1, 7),
    _GnAccessCfgLineCoding_Type()
)
gnAccessCfgLineCoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnAccessCfgLineCoding.setStatus("mandatory")
_GnAccessStat_ObjectIdentity = ObjectIdentity
gnAccessStat = _GnAccessStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 4, 2)
)
_GnAccessStatTable_Object = MibTable
gnAccessStatTable = _GnAccessStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 2, 1)
)
if mibBuilder.loadTexts:
    gnAccessStatTable.setStatus("mandatory")
_GnAccessStatEntry_Object = MibTableRow
gnAccessStatEntry = _GnAccessStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 2, 1, 1)
)
gnAccessStatEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    gnAccessStatEntry.setStatus("mandatory")


class _GnAccessStatInterfaceBer_Type(Integer32):
    """Custom type gnAccessStatInterfaceBer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
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
        *(("tenExpMinus10", 9),
          ("tenExpMinus11", 10),
          ("tenExpMinus12", 11),
          ("tenExpMinus13", 12),
          ("tenExpMinus14", 13),
          ("tenExpMinus3", 2),
          ("tenExpMinus4", 3),
          ("tenExpMinus5", 4),
          ("tenExpMinus6", 5),
          ("tenExpMinus7", 6),
          ("tenExpMinus8", 7),
          ("tenExpMinus9", 8))
    )


_GnAccessStatInterfaceBer_Type.__name__ = "Integer32"
_GnAccessStatInterfaceBer_Object = MibTableColumn
gnAccessStatInterfaceBer = _GnAccessStatInterfaceBer_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 2, 1, 1, 1),
    _GnAccessStatInterfaceBer_Type()
)
gnAccessStatInterfaceBer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnAccessStatInterfaceBer.setStatus("mandatory")


class _GnAccessStatStatus_Type(OctetString):
    """Custom type gnAccessStatStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_GnAccessStatStatus_Type.__name__ = "OctetString"
_GnAccessStatStatus_Object = MibTableColumn
gnAccessStatStatus = _GnAccessStatStatus_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 2, 1, 1, 2),
    _GnAccessStatStatus_Type()
)
gnAccessStatStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnAccessStatStatus.setStatus("mandatory")


class _GnAccessStatPrbsBer_Type(Integer32):
    """Custom type gnAccessStatPrbsBer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
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
        *(("tenExpMinus10", 9),
          ("tenExpMinus11", 10),
          ("tenExpMinus12", 11),
          ("tenExpMinus13", 12),
          ("tenExpMinus14", 13),
          ("tenExpMinus3", 2),
          ("tenExpMinus4", 3),
          ("tenExpMinus5", 4),
          ("tenExpMinus6", 5),
          ("tenExpMinus7", 6),
          ("tenExpMinus8", 7),
          ("tenExpMinus9", 8))
    )


_GnAccessStatPrbsBer_Type.__name__ = "Integer32"
_GnAccessStatPrbsBer_Object = MibTableColumn
gnAccessStatPrbsBer = _GnAccessStatPrbsBer_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 2, 1, 1, 3),
    _GnAccessStatPrbsBer_Type()
)
gnAccessStatPrbsBer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnAccessStatPrbsBer.setStatus("mandatory")


class _GnAccessStatValidIntervals_Type(Integer32):
    """Custom type gnAccessStatValidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_GnAccessStatValidIntervals_Type.__name__ = "Integer32"
_GnAccessStatValidIntervals_Object = MibTableColumn
gnAccessStatValidIntervals = _GnAccessStatValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 2, 1, 1, 4),
    _GnAccessStatValidIntervals_Type()
)
gnAccessStatValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnAccessStatValidIntervals.setStatus("mandatory")
_GnFastEthernetCfg_ObjectIdentity = ObjectIdentity
gnFastEthernetCfg = _GnFastEthernetCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 4, 3)
)
_GnFastEthernetCfgTable_Object = MibTable
gnFastEthernetCfgTable = _GnFastEthernetCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 3, 1)
)
if mibBuilder.loadTexts:
    gnFastEthernetCfgTable.setStatus("mandatory")
_GnFastEthernetCfgEntry_Object = MibTableRow
gnFastEthernetCfgEntry = _GnFastEthernetCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 3, 1, 1)
)
gnFastEthernetCfgEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    gnFastEthernetCfgEntry.setStatus("mandatory")


class _GnFastEthernetCfgAutoNegotiation_Type(Integer32):
    """Custom type gnFastEthernetCfgAutoNegotiation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 3),
          ("on", 2))
    )


_GnFastEthernetCfgAutoNegotiation_Type.__name__ = "Integer32"
_GnFastEthernetCfgAutoNegotiation_Object = MibTableColumn
gnFastEthernetCfgAutoNegotiation = _GnFastEthernetCfgAutoNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 3, 1, 1, 1),
    _GnFastEthernetCfgAutoNegotiation_Type()
)
gnFastEthernetCfgAutoNegotiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnFastEthernetCfgAutoNegotiation.setStatus("mandatory")


class _GnFastEthernetCfgForceSpeed_Type(Integer32):
    """Custom type gnFastEthernetCfgForceSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hundredBased", 3),
          ("tenBased", 2))
    )


_GnFastEthernetCfgForceSpeed_Type.__name__ = "Integer32"
_GnFastEthernetCfgForceSpeed_Object = MibTableColumn
gnFastEthernetCfgForceSpeed = _GnFastEthernetCfgForceSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 3, 1, 1, 2),
    _GnFastEthernetCfgForceSpeed_Type()
)
gnFastEthernetCfgForceSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnFastEthernetCfgForceSpeed.setStatus("mandatory")


class _GnFastEthernetCfgDynamicBand_Type(Integer32):
    """Custom type gnFastEthernetCfgDynamicBand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 3),
          ("ipPriority", 6),
          ("leftPreferred", 4),
          ("notActive", 2),
          ("vlanPriority", 5))
    )


_GnFastEthernetCfgDynamicBand_Type.__name__ = "Integer32"
_GnFastEthernetCfgDynamicBand_Object = MibTableColumn
gnFastEthernetCfgDynamicBand = _GnFastEthernetCfgDynamicBand_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 3, 1, 1, 3),
    _GnFastEthernetCfgDynamicBand_Type()
)
gnFastEthernetCfgDynamicBand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnFastEthernetCfgDynamicBand.setStatus("mandatory")


class _GnFastEthernetCfgGigabitEthernet_Type(Integer32):
    """Custom type gnFastEthernetCfgGigabitEthernet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 3))
    )


_GnFastEthernetCfgGigabitEthernet_Type.__name__ = "Integer32"
_GnFastEthernetCfgGigabitEthernet_Object = MibTableColumn
gnFastEthernetCfgGigabitEthernet = _GnFastEthernetCfgGigabitEthernet_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 3, 1, 1, 4),
    _GnFastEthernetCfgGigabitEthernet_Type()
)
gnFastEthernetCfgGigabitEthernet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnFastEthernetCfgGigabitEthernet.setStatus("mandatory")


class _GnFastEthernetCfgDuplexMode_Type(Integer32):
    """Custom type gnFastEthernetCfgDuplexMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fullDuplex", 3),
          ("halfDuplex", 2))
    )


_GnFastEthernetCfgDuplexMode_Type.__name__ = "Integer32"
_GnFastEthernetCfgDuplexMode_Object = MibTableColumn
gnFastEthernetCfgDuplexMode = _GnFastEthernetCfgDuplexMode_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 3, 1, 1, 5),
    _GnFastEthernetCfgDuplexMode_Type()
)
gnFastEthernetCfgDuplexMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnFastEthernetCfgDuplexMode.setStatus("mandatory")


class _GnFastEthernetCfgQueuingScheme_Type(Integer32):
    """Custom type gnFastEthernetCfgQueuingScheme based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fixedPriority", 2),
          ("weightedFair", 3))
    )


_GnFastEthernetCfgQueuingScheme_Type.__name__ = "Integer32"
_GnFastEthernetCfgQueuingScheme_Object = MibTableColumn
gnFastEthernetCfgQueuingScheme = _GnFastEthernetCfgQueuingScheme_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 3, 1, 1, 6),
    _GnFastEthernetCfgQueuingScheme_Type()
)
gnFastEthernetCfgQueuingScheme.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnFastEthernetCfgQueuingScheme.setStatus("mandatory")
_GnFastEthernetStat_ObjectIdentity = ObjectIdentity
gnFastEthernetStat = _GnFastEthernetStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 4, 4)
)
_GnFastEthernetStatTable_Object = MibTable
gnFastEthernetStatTable = _GnFastEthernetStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 4, 1)
)
if mibBuilder.loadTexts:
    gnFastEthernetStatTable.setStatus("mandatory")
_GnFastEthernetStatEntry_Object = MibTableRow
gnFastEthernetStatEntry = _GnFastEthernetStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 4, 1, 1)
)
gnFastEthernetStatEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    gnFastEthernetStatEntry.setStatus("mandatory")


class _GnFastEthernetStatStatus_Type(OctetString):
    """Custom type gnFastEthernetStatStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_GnFastEthernetStatStatus_Type.__name__ = "OctetString"
_GnFastEthernetStatStatus_Object = MibTableColumn
gnFastEthernetStatStatus = _GnFastEthernetStatStatus_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 4, 1, 1, 1),
    _GnFastEthernetStatStatus_Type()
)
gnFastEthernetStatStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnFastEthernetStatStatus.setStatus("mandatory")
_GnPdhMon_ObjectIdentity = ObjectIdentity
gnPdhMon = _GnPdhMon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 4, 5)
)
_GnPdhMonCurrTable_Object = MibTable
gnPdhMonCurrTable = _GnPdhMonCurrTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 5, 1)
)
if mibBuilder.loadTexts:
    gnPdhMonCurrTable.setStatus("mandatory")
_GnPdhMonCurrEntry_Object = MibTableRow
gnPdhMonCurrEntry = _GnPdhMonCurrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 5, 1, 1)
)
gnPdhMonCurrEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    gnPdhMonCurrEntry.setStatus("mandatory")
_GnPdhMonCurrES_Type = Gauge32
_GnPdhMonCurrES_Object = MibTableColumn
gnPdhMonCurrES = _GnPdhMonCurrES_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 5, 1, 1, 1),
    _GnPdhMonCurrES_Type()
)
gnPdhMonCurrES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnPdhMonCurrES.setStatus("mandatory")
_GnPdhMonCurrSES_Type = Gauge32
_GnPdhMonCurrSES_Object = MibTableColumn
gnPdhMonCurrSES = _GnPdhMonCurrSES_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 5, 1, 1, 2),
    _GnPdhMonCurrSES_Type()
)
gnPdhMonCurrSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnPdhMonCurrSES.setStatus("mandatory")
_GnPdhMonCurrBBE_Type = Gauge32
_GnPdhMonCurrBBE_Object = MibTableColumn
gnPdhMonCurrBBE = _GnPdhMonCurrBBE_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 5, 1, 1, 3),
    _GnPdhMonCurrBBE_Type()
)
gnPdhMonCurrBBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnPdhMonCurrBBE.setStatus("mandatory")
_GnPdhMonCurrUAS_Type = Gauge32
_GnPdhMonCurrUAS_Object = MibTableColumn
gnPdhMonCurrUAS = _GnPdhMonCurrUAS_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 5, 1, 1, 4),
    _GnPdhMonCurrUAS_Type()
)
gnPdhMonCurrUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnPdhMonCurrUAS.setStatus("mandatory")
_GnPdhMonCurrCV_Type = Gauge32
_GnPdhMonCurrCV_Object = MibTableColumn
gnPdhMonCurrCV = _GnPdhMonCurrCV_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 5, 1, 1, 5),
    _GnPdhMonCurrCV_Type()
)
gnPdhMonCurrCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnPdhMonCurrCV.setStatus("mandatory")
_GnPdhMonCurrLastDayES_Type = Gauge32
_GnPdhMonCurrLastDayES_Object = MibTableColumn
gnPdhMonCurrLastDayES = _GnPdhMonCurrLastDayES_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 5, 1, 1, 6),
    _GnPdhMonCurrLastDayES_Type()
)
gnPdhMonCurrLastDayES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnPdhMonCurrLastDayES.setStatus("mandatory")
_GnPdhMonCurrLastDaySES_Type = Gauge32
_GnPdhMonCurrLastDaySES_Object = MibTableColumn
gnPdhMonCurrLastDaySES = _GnPdhMonCurrLastDaySES_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 5, 1, 1, 7),
    _GnPdhMonCurrLastDaySES_Type()
)
gnPdhMonCurrLastDaySES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnPdhMonCurrLastDaySES.setStatus("mandatory")
_GnPdhMonCurrLastDayBBE_Type = Gauge32
_GnPdhMonCurrLastDayBBE_Object = MibTableColumn
gnPdhMonCurrLastDayBBE = _GnPdhMonCurrLastDayBBE_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 5, 1, 1, 8),
    _GnPdhMonCurrLastDayBBE_Type()
)
gnPdhMonCurrLastDayBBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnPdhMonCurrLastDayBBE.setStatus("mandatory")
_GnPdhMonCurrLastDayUAS_Type = Gauge32
_GnPdhMonCurrLastDayUAS_Object = MibTableColumn
gnPdhMonCurrLastDayUAS = _GnPdhMonCurrLastDayUAS_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 5, 1, 1, 9),
    _GnPdhMonCurrLastDayUAS_Type()
)
gnPdhMonCurrLastDayUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnPdhMonCurrLastDayUAS.setStatus("mandatory")
_GnPdhMonCurrLastDayCV_Type = Gauge32
_GnPdhMonCurrLastDayCV_Object = MibTableColumn
gnPdhMonCurrLastDayCV = _GnPdhMonCurrLastDayCV_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 5, 1, 1, 10),
    _GnPdhMonCurrLastDayCV_Type()
)
gnPdhMonCurrLastDayCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnPdhMonCurrLastDayCV.setStatus("mandatory")


class _GnPdhMonCurrLastDayIDF_Type(Integer32):
    """Custom type gnPdhMonCurrLastDayIDF based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3))
    )


_GnPdhMonCurrLastDayIDF_Type.__name__ = "Integer32"
_GnPdhMonCurrLastDayIDF_Object = MibTableColumn
gnPdhMonCurrLastDayIDF = _GnPdhMonCurrLastDayIDF_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 5, 1, 1, 11),
    _GnPdhMonCurrLastDayIDF_Type()
)
gnPdhMonCurrLastDayIDF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnPdhMonCurrLastDayIDF.setStatus("mandatory")
_GnPdhMonIntervalTable_Object = MibTable
gnPdhMonIntervalTable = _GnPdhMonIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 5, 2)
)
if mibBuilder.loadTexts:
    gnPdhMonIntervalTable.setStatus("mandatory")
_GnPdhMonIntervalEntry_Object = MibTableRow
gnPdhMonIntervalEntry = _GnPdhMonIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 5, 2, 1)
)
gnPdhMonIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CERAGON-MIB", "gnPdhMonIntervalIdx"),
)
if mibBuilder.loadTexts:
    gnPdhMonIntervalEntry.setStatus("mandatory")


class _GnPdhMonIntervalIdx_Type(Integer32):
    """Custom type gnPdhMonIntervalIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_GnPdhMonIntervalIdx_Type.__name__ = "Integer32"
_GnPdhMonIntervalIdx_Object = MibTableColumn
gnPdhMonIntervalIdx = _GnPdhMonIntervalIdx_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 5, 2, 1, 1),
    _GnPdhMonIntervalIdx_Type()
)
gnPdhMonIntervalIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnPdhMonIntervalIdx.setStatus("mandatory")
_GnPdhMonIntervalES_Type = Gauge32
_GnPdhMonIntervalES_Object = MibTableColumn
gnPdhMonIntervalES = _GnPdhMonIntervalES_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 5, 2, 1, 2),
    _GnPdhMonIntervalES_Type()
)
gnPdhMonIntervalES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnPdhMonIntervalES.setStatus("mandatory")
_GnPdhMonIntervalSES_Type = Gauge32
_GnPdhMonIntervalSES_Object = MibTableColumn
gnPdhMonIntervalSES = _GnPdhMonIntervalSES_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 5, 2, 1, 3),
    _GnPdhMonIntervalSES_Type()
)
gnPdhMonIntervalSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnPdhMonIntervalSES.setStatus("mandatory")
_GnPdhMonIntervalBBE_Type = Gauge32
_GnPdhMonIntervalBBE_Object = MibTableColumn
gnPdhMonIntervalBBE = _GnPdhMonIntervalBBE_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 5, 2, 1, 4),
    _GnPdhMonIntervalBBE_Type()
)
gnPdhMonIntervalBBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnPdhMonIntervalBBE.setStatus("mandatory")
_GnPdhMonIntervalUAS_Type = Gauge32
_GnPdhMonIntervalUAS_Object = MibTableColumn
gnPdhMonIntervalUAS = _GnPdhMonIntervalUAS_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 5, 2, 1, 5),
    _GnPdhMonIntervalUAS_Type()
)
gnPdhMonIntervalUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnPdhMonIntervalUAS.setStatus("mandatory")
_GnPdhMonIntervalCV_Type = Gauge32
_GnPdhMonIntervalCV_Object = MibTableColumn
gnPdhMonIntervalCV = _GnPdhMonIntervalCV_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 5, 2, 1, 6),
    _GnPdhMonIntervalCV_Type()
)
gnPdhMonIntervalCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnPdhMonIntervalCV.setStatus("mandatory")


class _GnPdhMonIntervalIDF_Type(Integer32):
    """Custom type gnPdhMonIntervalIDF based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3))
    )


_GnPdhMonIntervalIDF_Type.__name__ = "Integer32"
_GnPdhMonIntervalIDF_Object = MibTableColumn
gnPdhMonIntervalIDF = _GnPdhMonIntervalIDF_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 5, 2, 1, 7),
    _GnPdhMonIntervalIDF_Type()
)
gnPdhMonIntervalIDF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnPdhMonIntervalIDF.setStatus("mandatory")
_GnPdhMonDayTable_Object = MibTable
gnPdhMonDayTable = _GnPdhMonDayTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 5, 3)
)
if mibBuilder.loadTexts:
    gnPdhMonDayTable.setStatus("mandatory")
_GnPdhMonDayEntry_Object = MibTableRow
gnPdhMonDayEntry = _GnPdhMonDayEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 5, 3, 1)
)
gnPdhMonDayEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CERAGON-MIB", "gnPdhMonDayIdx"),
)
if mibBuilder.loadTexts:
    gnPdhMonDayEntry.setStatus("mandatory")


class _GnPdhMonDayIdx_Type(Integer32):
    """Custom type gnPdhMonDayIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_GnPdhMonDayIdx_Type.__name__ = "Integer32"
_GnPdhMonDayIdx_Object = MibTableColumn
gnPdhMonDayIdx = _GnPdhMonDayIdx_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 5, 3, 1, 1),
    _GnPdhMonDayIdx_Type()
)
gnPdhMonDayIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnPdhMonDayIdx.setStatus("mandatory")
_GnPdhMonDayES_Type = Gauge32
_GnPdhMonDayES_Object = MibTableColumn
gnPdhMonDayES = _GnPdhMonDayES_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 5, 3, 1, 2),
    _GnPdhMonDayES_Type()
)
gnPdhMonDayES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnPdhMonDayES.setStatus("mandatory")
_GnPdhMonDaySES_Type = Gauge32
_GnPdhMonDaySES_Object = MibTableColumn
gnPdhMonDaySES = _GnPdhMonDaySES_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 5, 3, 1, 3),
    _GnPdhMonDaySES_Type()
)
gnPdhMonDaySES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnPdhMonDaySES.setStatus("mandatory")
_GnPdhMonDayBBE_Type = Gauge32
_GnPdhMonDayBBE_Object = MibTableColumn
gnPdhMonDayBBE = _GnPdhMonDayBBE_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 5, 3, 1, 4),
    _GnPdhMonDayBBE_Type()
)
gnPdhMonDayBBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnPdhMonDayBBE.setStatus("mandatory")
_GnPdhMonDayUAS_Type = Gauge32
_GnPdhMonDayUAS_Object = MibTableColumn
gnPdhMonDayUAS = _GnPdhMonDayUAS_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 5, 3, 1, 5),
    _GnPdhMonDayUAS_Type()
)
gnPdhMonDayUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnPdhMonDayUAS.setStatus("mandatory")
_GnPdhMonDayCV_Type = Gauge32
_GnPdhMonDayCV_Object = MibTableColumn
gnPdhMonDayCV = _GnPdhMonDayCV_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 5, 3, 1, 6),
    _GnPdhMonDayCV_Type()
)
gnPdhMonDayCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnPdhMonDayCV.setStatus("mandatory")


class _GnPdhMonDayIDF_Type(Integer32):
    """Custom type gnPdhMonDayIDF based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3))
    )


_GnPdhMonDayIDF_Type.__name__ = "Integer32"
_GnPdhMonDayIDF_Object = MibTableColumn
gnPdhMonDayIDF = _GnPdhMonDayIDF_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 5, 3, 1, 7),
    _GnPdhMonDayIDF_Type()
)
gnPdhMonDayIDF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnPdhMonDayIDF.setStatus("mandatory")
_GnFastEthernetMon_ObjectIdentity = ObjectIdentity
gnFastEthernetMon = _GnFastEthernetMon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 4, 6)
)
_GnFastEthernetMonPrivateTable_Object = MibTable
gnFastEthernetMonPrivateTable = _GnFastEthernetMonPrivateTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 6, 1)
)
if mibBuilder.loadTexts:
    gnFastEthernetMonPrivateTable.setStatus("mandatory")
_GnFastEthernetMonPrivateEntry_Object = MibTableRow
gnFastEthernetMonPrivateEntry = _GnFastEthernetMonPrivateEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 6, 1, 1)
)
gnFastEthernetMonPrivateEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    gnFastEthernetMonPrivateEntry.setStatus("mandatory")
_GnFastEthernetMonPrivateAlignmentErrors_Type = Counter32
_GnFastEthernetMonPrivateAlignmentErrors_Object = MibTableColumn
gnFastEthernetMonPrivateAlignmentErrors = _GnFastEthernetMonPrivateAlignmentErrors_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 6, 1, 1, 1),
    _GnFastEthernetMonPrivateAlignmentErrors_Type()
)
gnFastEthernetMonPrivateAlignmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnFastEthernetMonPrivateAlignmentErrors.setStatus("mandatory")
_GnFastEthernetMonPrivateFcsErrors_Type = Counter32
_GnFastEthernetMonPrivateFcsErrors_Object = MibTableColumn
gnFastEthernetMonPrivateFcsErrors = _GnFastEthernetMonPrivateFcsErrors_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 6, 1, 1, 2),
    _GnFastEthernetMonPrivateFcsErrors_Type()
)
gnFastEthernetMonPrivateFcsErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnFastEthernetMonPrivateFcsErrors.setStatus("mandatory")
_GnFastEthernetMonPrivateFrameTooLongs_Type = Counter32
_GnFastEthernetMonPrivateFrameTooLongs_Object = MibTableColumn
gnFastEthernetMonPrivateFrameTooLongs = _GnFastEthernetMonPrivateFrameTooLongs_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 6, 1, 1, 3),
    _GnFastEthernetMonPrivateFrameTooLongs_Type()
)
gnFastEthernetMonPrivateFrameTooLongs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnFastEthernetMonPrivateFrameTooLongs.setStatus("mandatory")
_GnFastEthernetMonStdHiTable_Object = MibTable
gnFastEthernetMonStdHiTable = _GnFastEthernetMonStdHiTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 6, 2)
)
if mibBuilder.loadTexts:
    gnFastEthernetMonStdHiTable.setStatus("mandatory")
_GnFastEthernetMonStdHiEntry_Object = MibTableRow
gnFastEthernetMonStdHiEntry = _GnFastEthernetMonStdHiEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 6, 2, 1)
)
gnFastEthernetMonStdHiEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    gnFastEthernetMonStdHiEntry.setStatus("mandatory")
_GnFastEthernetMonStdHiInOctetsHC_Type = Counter32
_GnFastEthernetMonStdHiInOctetsHC_Object = MibTableColumn
gnFastEthernetMonStdHiInOctetsHC = _GnFastEthernetMonStdHiInOctetsHC_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 6, 2, 1, 1),
    _GnFastEthernetMonStdHiInOctetsHC_Type()
)
gnFastEthernetMonStdHiInOctetsHC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnFastEthernetMonStdHiInOctetsHC.setStatus("mandatory")
_GnFastEthernetMonStdHiInUcastPktsHC_Type = Counter32
_GnFastEthernetMonStdHiInUcastPktsHC_Object = MibTableColumn
gnFastEthernetMonStdHiInUcastPktsHC = _GnFastEthernetMonStdHiInUcastPktsHC_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 6, 2, 1, 2),
    _GnFastEthernetMonStdHiInUcastPktsHC_Type()
)
gnFastEthernetMonStdHiInUcastPktsHC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnFastEthernetMonStdHiInUcastPktsHC.setStatus("mandatory")
_GnFastEthernetMonStdHiInNUcastPktsHC_Type = Counter32
_GnFastEthernetMonStdHiInNUcastPktsHC_Object = MibTableColumn
gnFastEthernetMonStdHiInNUcastPktsHC = _GnFastEthernetMonStdHiInNUcastPktsHC_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 6, 2, 1, 3),
    _GnFastEthernetMonStdHiInNUcastPktsHC_Type()
)
gnFastEthernetMonStdHiInNUcastPktsHC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnFastEthernetMonStdHiInNUcastPktsHC.setStatus("mandatory")
_GnFastEthernetMonStdHiOutOctetsHC_Type = Counter32
_GnFastEthernetMonStdHiOutOctetsHC_Object = MibTableColumn
gnFastEthernetMonStdHiOutOctetsHC = _GnFastEthernetMonStdHiOutOctetsHC_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 6, 2, 1, 4),
    _GnFastEthernetMonStdHiOutOctetsHC_Type()
)
gnFastEthernetMonStdHiOutOctetsHC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnFastEthernetMonStdHiOutOctetsHC.setStatus("mandatory")
_GnFastEthernetMonStdHiOutUcastPktsHC_Type = Counter32
_GnFastEthernetMonStdHiOutUcastPktsHC_Object = MibTableColumn
gnFastEthernetMonStdHiOutUcastPktsHC = _GnFastEthernetMonStdHiOutUcastPktsHC_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 6, 2, 1, 5),
    _GnFastEthernetMonStdHiOutUcastPktsHC_Type()
)
gnFastEthernetMonStdHiOutUcastPktsHC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnFastEthernetMonStdHiOutUcastPktsHC.setStatus("mandatory")
_GnFastEthernetMonStdHiOutNUcastPktsHC_Type = Counter32
_GnFastEthernetMonStdHiOutNUcastPktsHC_Object = MibTableColumn
gnFastEthernetMonStdHiOutNUcastPktsHC = _GnFastEthernetMonStdHiOutNUcastPktsHC_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 6, 2, 1, 6),
    _GnFastEthernetMonStdHiOutNUcastPktsHC_Type()
)
gnFastEthernetMonStdHiOutNUcastPktsHC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnFastEthernetMonStdHiOutNUcastPktsHC.setStatus("mandatory")
_GnTrailCfg_ObjectIdentity = ObjectIdentity
gnTrailCfg = _GnTrailCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 4, 7)
)
_GnTrailCfgTable_Object = MibTable
gnTrailCfgTable = _GnTrailCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 7, 1)
)
if mibBuilder.loadTexts:
    gnTrailCfgTable.setStatus("mandatory")
_GnTrailCfgEntry_Object = MibTableRow
gnTrailCfgEntry = _GnTrailCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 7, 1, 1)
)
gnTrailCfgEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    gnTrailCfgEntry.setStatus("mandatory")


class _GnTrailCfgTrailName_Type(DisplayString):
    """Custom type gnTrailCfgTrailName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_GnTrailCfgTrailName_Type.__name__ = "DisplayString"
_GnTrailCfgTrailName_Object = MibTableColumn
gnTrailCfgTrailName = _GnTrailCfgTrailName_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 7, 1, 1, 1),
    _GnTrailCfgTrailName_Type()
)
gnTrailCfgTrailName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnTrailCfgTrailName.setStatus("mandatory")


class _GnTrailCfgProtection_Type(Integer32):
    """Custom type gnTrailCfgProtection based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("protected", 2),
          ("unprotected", 3))
    )


_GnTrailCfgProtection_Type.__name__ = "Integer32"
_GnTrailCfgProtection_Object = MibTableColumn
gnTrailCfgProtection = _GnTrailCfgProtection_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 7, 1, 1, 2),
    _GnTrailCfgProtection_Type()
)
gnTrailCfgProtection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnTrailCfgProtection.setStatus("mandatory")
_GnTrailCfgLowPathIndex_Type = Integer32
_GnTrailCfgLowPathIndex_Object = MibTableColumn
gnTrailCfgLowPathIndex = _GnTrailCfgLowPathIndex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 7, 1, 1, 3),
    _GnTrailCfgLowPathIndex_Type()
)
gnTrailCfgLowPathIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnTrailCfgLowPathIndex.setStatus("mandatory")


class _GnTrailCfgLowPathSide_Type(Integer32):
    """Custom type gnTrailCfgLowPathSide based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("east", 2),
          ("west", 3))
    )


_GnTrailCfgLowPathSide_Type.__name__ = "Integer32"
_GnTrailCfgLowPathSide_Object = MibTableColumn
gnTrailCfgLowPathSide = _GnTrailCfgLowPathSide_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 7, 1, 1, 4),
    _GnTrailCfgLowPathSide_Type()
)
gnTrailCfgLowPathSide.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnTrailCfgLowPathSide.setStatus("mandatory")


class _GnTrailCfgProtectionOptions_Type(Integer32):
    """Custom type gnTrailCfgProtectionOptions based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 3),
          ("inhibit", 2))
    )


_GnTrailCfgProtectionOptions_Type.__name__ = "Integer32"
_GnTrailCfgProtectionOptions_Object = MibTableColumn
gnTrailCfgProtectionOptions = _GnTrailCfgProtectionOptions_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 7, 1, 1, 5),
    _GnTrailCfgProtectionOptions_Type()
)
gnTrailCfgProtectionOptions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnTrailCfgProtectionOptions.setStatus("mandatory")


class _GnTrailCfgMismatchJ2_Type(Integer32):
    """Custom type gnTrailCfgMismatchJ2 based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ignoreAlarm", 4),
          ("sendAIS", 3),
          ("sendAlarm", 2))
    )


_GnTrailCfgMismatchJ2_Type.__name__ = "Integer32"
_GnTrailCfgMismatchJ2_Object = MibTableColumn
gnTrailCfgMismatchJ2 = _GnTrailCfgMismatchJ2_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 7, 1, 1, 6),
    _GnTrailCfgMismatchJ2_Type()
)
gnTrailCfgMismatchJ2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnTrailCfgMismatchJ2.setStatus("mandatory")


class _GnTrailCfgTransmittedJ2_Type(DisplayString):
    """Custom type gnTrailCfgTransmittedJ2 based on DisplayString"""
    defaultValue = OctetString("J2 J2 J2 J2 J2 ")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_GnTrailCfgTransmittedJ2_Type.__name__ = "DisplayString"
_GnTrailCfgTransmittedJ2_Object = MibTableColumn
gnTrailCfgTransmittedJ2 = _GnTrailCfgTransmittedJ2_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 7, 1, 1, 7),
    _GnTrailCfgTransmittedJ2_Type()
)
gnTrailCfgTransmittedJ2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnTrailCfgTransmittedJ2.setStatus("mandatory")


class _GnTrailCfgExpectedJ2_Type(DisplayString):
    """Custom type gnTrailCfgExpectedJ2 based on DisplayString"""
    defaultValue = OctetString("J2 J2 J2 J2 J2 ")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_GnTrailCfgExpectedJ2_Type.__name__ = "DisplayString"
_GnTrailCfgExpectedJ2_Object = MibTableColumn
gnTrailCfgExpectedJ2 = _GnTrailCfgExpectedJ2_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 7, 1, 1, 8),
    _GnTrailCfgExpectedJ2_Type()
)
gnTrailCfgExpectedJ2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnTrailCfgExpectedJ2.setStatus("mandatory")


class _GnTrailCfgReversionMode_Type(Integer32):
    """Custom type gnTrailCfgReversionMode based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nonRevertive", 3),
          ("revertive", 2))
    )


_GnTrailCfgReversionMode_Type.__name__ = "Integer32"
_GnTrailCfgReversionMode_Object = MibTableColumn
gnTrailCfgReversionMode = _GnTrailCfgReversionMode_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 7, 1, 1, 9),
    _GnTrailCfgReversionMode_Type()
)
gnTrailCfgReversionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnTrailCfgReversionMode.setStatus("mandatory")


class _GnTrailCfgProtectionUserCommand_Type(Integer32):
    """Custom type gnTrailCfgProtectionUserCommand based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 2),
          ("switchToProtection", 3),
          ("switchToWorking", 4))
    )


_GnTrailCfgProtectionUserCommand_Type.__name__ = "Integer32"
_GnTrailCfgProtectionUserCommand_Object = MibTableColumn
gnTrailCfgProtectionUserCommand = _GnTrailCfgProtectionUserCommand_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 7, 1, 1, 10),
    _GnTrailCfgProtectionUserCommand_Type()
)
gnTrailCfgProtectionUserCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnTrailCfgProtectionUserCommand.setStatus("mandatory")


class _GnTrailCfgHoldOffTime_Type(Integer32):
    """Custom type gnTrailCfgHoldOffTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20000),
    )


_GnTrailCfgHoldOffTime_Type.__name__ = "Integer32"
_GnTrailCfgHoldOffTime_Object = MibTableColumn
gnTrailCfgHoldOffTime = _GnTrailCfgHoldOffTime_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 7, 1, 1, 11),
    _GnTrailCfgHoldOffTime_Type()
)
gnTrailCfgHoldOffTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnTrailCfgHoldOffTime.setStatus("mandatory")


class _GnTrailCfgOscillationGuardTime_Type(Integer32):
    """Custom type gnTrailCfgOscillationGuardTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_GnTrailCfgOscillationGuardTime_Type.__name__ = "Integer32"
_GnTrailCfgOscillationGuardTime_Object = MibTableColumn
gnTrailCfgOscillationGuardTime = _GnTrailCfgOscillationGuardTime_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 7, 1, 1, 12),
    _GnTrailCfgOscillationGuardTime_Type()
)
gnTrailCfgOscillationGuardTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnTrailCfgOscillationGuardTime.setStatus("mandatory")


class _GnTrailCfgWaitToRestoreTime_Type(Integer32):
    """Custom type gnTrailCfgWaitToRestoreTime based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 12),
    )


_GnTrailCfgWaitToRestoreTime_Type.__name__ = "Integer32"
_GnTrailCfgWaitToRestoreTime_Object = MibTableColumn
gnTrailCfgWaitToRestoreTime = _GnTrailCfgWaitToRestoreTime_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 7, 1, 1, 13),
    _GnTrailCfgWaitToRestoreTime_Type()
)
gnTrailCfgWaitToRestoreTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnTrailCfgWaitToRestoreTime.setStatus("mandatory")


class _GnTrailCfgSignalLabelMismatch_Type(Integer32):
    """Custom type gnTrailCfgSignalLabelMismatch based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("sendAIS", 3),
          ("sendAlarm", 2))
    )


_GnTrailCfgSignalLabelMismatch_Type.__name__ = "Integer32"
_GnTrailCfgSignalLabelMismatch_Object = MibTableColumn
gnTrailCfgSignalLabelMismatch = _GnTrailCfgSignalLabelMismatch_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 7, 1, 1, 14),
    _GnTrailCfgSignalLabelMismatch_Type()
)
gnTrailCfgSignalLabelMismatch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnTrailCfgSignalLabelMismatch.setStatus("mandatory")


class _GnTrailCfgBERConsAction_Type(Integer32):
    """Custom type gnTrailCfgBERConsAction based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("doPathProtection", 4),
          ("sendAISDoPathProtection", 3),
          ("sendAlarm", 2))
    )


_GnTrailCfgBERConsAction_Type.__name__ = "Integer32"
_GnTrailCfgBERConsAction_Object = MibTableColumn
gnTrailCfgBERConsAction = _GnTrailCfgBERConsAction_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 7, 1, 1, 15),
    _GnTrailCfgBERConsAction_Type()
)
gnTrailCfgBERConsAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnTrailCfgBERConsAction.setStatus("mandatory")
_GnTribCfg_ObjectIdentity = ObjectIdentity
gnTribCfg = _GnTribCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 4, 8)
)
_GnTribCfgTable_Object = MibTable
gnTribCfgTable = _GnTribCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 8, 1)
)
if mibBuilder.loadTexts:
    gnTribCfgTable.setStatus("mandatory")
_GnTribCfgEntry_Object = MibTableRow
gnTribCfgEntry = _GnTribCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 8, 1, 1)
)
gnTribCfgEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    gnTribCfgEntry.setStatus("mandatory")
_GnTribCfgLowPathIndex_Type = Integer32
_GnTribCfgLowPathIndex_Object = MibTableColumn
gnTribCfgLowPathIndex = _GnTribCfgLowPathIndex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 8, 1, 1, 1),
    _GnTribCfgLowPathIndex_Type()
)
gnTribCfgLowPathIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnTribCfgLowPathIndex.setStatus("mandatory")


class _GnTribCfgLowPathSide_Type(Integer32):
    """Custom type gnTribCfgLowPathSide based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("east", 2),
          ("west", 3))
    )


_GnTribCfgLowPathSide_Type.__name__ = "Integer32"
_GnTribCfgLowPathSide_Object = MibTableColumn
gnTribCfgLowPathSide = _GnTribCfgLowPathSide_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 8, 1, 1, 2),
    _GnTribCfgLowPathSide_Type()
)
gnTribCfgLowPathSide.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnTribCfgLowPathSide.setStatus("mandatory")


class _GnTribCfgProtection_Type(Integer32):
    """Custom type gnTribCfgProtection based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("protected", 2),
          ("unprotected", 3))
    )


_GnTribCfgProtection_Type.__name__ = "Integer32"
_GnTribCfgProtection_Object = MibTableColumn
gnTribCfgProtection = _GnTribCfgProtection_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 8, 1, 1, 3),
    _GnTribCfgProtection_Type()
)
gnTribCfgProtection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnTribCfgProtection.setStatus("mandatory")


class _GnTribCfgProtectionOptions_Type(Integer32):
    """Custom type gnTribCfgProtectionOptions based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 3),
          ("inhibit", 2))
    )


_GnTribCfgProtectionOptions_Type.__name__ = "Integer32"
_GnTribCfgProtectionOptions_Object = MibTableColumn
gnTribCfgProtectionOptions = _GnTribCfgProtectionOptions_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 8, 1, 1, 4),
    _GnTribCfgProtectionOptions_Type()
)
gnTribCfgProtectionOptions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnTribCfgProtectionOptions.setStatus("mandatory")


class _GnTribCfgReversionMode_Type(Integer32):
    """Custom type gnTribCfgReversionMode based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nonRevertive", 3),
          ("revertive", 2))
    )


_GnTribCfgReversionMode_Type.__name__ = "Integer32"
_GnTribCfgReversionMode_Object = MibTableColumn
gnTribCfgReversionMode = _GnTribCfgReversionMode_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 8, 1, 1, 5),
    _GnTribCfgReversionMode_Type()
)
gnTribCfgReversionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnTribCfgReversionMode.setStatus("mandatory")


class _GnTribCfgProtectionUserCommand_Type(Integer32):
    """Custom type gnTribCfgProtectionUserCommand based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 2),
          ("switchToProtection", 3),
          ("switchToWorking", 4))
    )


_GnTribCfgProtectionUserCommand_Type.__name__ = "Integer32"
_GnTribCfgProtectionUserCommand_Object = MibTableColumn
gnTribCfgProtectionUserCommand = _GnTribCfgProtectionUserCommand_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 8, 1, 1, 6),
    _GnTribCfgProtectionUserCommand_Type()
)
gnTribCfgProtectionUserCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnTribCfgProtectionUserCommand.setStatus("mandatory")


class _GnTribCfgHoldOffTime_Type(Integer32):
    """Custom type gnTribCfgHoldOffTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20000),
    )


_GnTribCfgHoldOffTime_Type.__name__ = "Integer32"
_GnTribCfgHoldOffTime_Object = MibTableColumn
gnTribCfgHoldOffTime = _GnTribCfgHoldOffTime_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 8, 1, 1, 7),
    _GnTribCfgHoldOffTime_Type()
)
gnTribCfgHoldOffTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnTribCfgHoldOffTime.setStatus("mandatory")


class _GnTribCfgOscillationGuardTime_Type(Integer32):
    """Custom type gnTribCfgOscillationGuardTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_GnTribCfgOscillationGuardTime_Type.__name__ = "Integer32"
_GnTribCfgOscillationGuardTime_Object = MibTableColumn
gnTribCfgOscillationGuardTime = _GnTribCfgOscillationGuardTime_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 8, 1, 1, 8),
    _GnTribCfgOscillationGuardTime_Type()
)
gnTribCfgOscillationGuardTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnTribCfgOscillationGuardTime.setStatus("mandatory")


class _GnTribCfgWaitToRestoreTime_Type(Integer32):
    """Custom type gnTribCfgWaitToRestoreTime based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 12),
    )


_GnTribCfgWaitToRestoreTime_Type.__name__ = "Integer32"
_GnTribCfgWaitToRestoreTime_Object = MibTableColumn
gnTribCfgWaitToRestoreTime = _GnTribCfgWaitToRestoreTime_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 8, 1, 1, 9),
    _GnTribCfgWaitToRestoreTime_Type()
)
gnTribCfgWaitToRestoreTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnTribCfgWaitToRestoreTime.setStatus("mandatory")
_GnTribCfgKLM_Type = Integer32
_GnTribCfgKLM_Object = MibTableColumn
gnTribCfgKLM = _GnTribCfgKLM_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 8, 1, 1, 10),
    _GnTribCfgKLM_Type()
)
gnTribCfgKLM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnTribCfgKLM.setStatus("mandatory")
_GnTrailPassThrough_ObjectIdentity = ObjectIdentity
gnTrailPassThrough = _GnTrailPassThrough_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 4, 9)
)
_GnTrailPassThroughTable_Object = MibTable
gnTrailPassThroughTable = _GnTrailPassThroughTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 9, 1)
)
if mibBuilder.loadTexts:
    gnTrailPassThroughTable.setStatus("mandatory")
_GnTrailPassThroughEntry_Object = MibTableRow
gnTrailPassThroughEntry = _GnTrailPassThroughEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 9, 1, 1)
)
gnTrailPassThroughEntry.setIndexNames(
    (0, "CERAGON-MIB", "gnTrailPassThroughIndex"),
)
if mibBuilder.loadTexts:
    gnTrailPassThroughEntry.setStatus("mandatory")


class _GnTrailPassThroughIndex_Type(Integer32):
    """Custom type gnTrailPassThroughIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 84),
    )


_GnTrailPassThroughIndex_Type.__name__ = "Integer32"
_GnTrailPassThroughIndex_Object = MibTableColumn
gnTrailPassThroughIndex = _GnTrailPassThroughIndex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 9, 1, 1, 1),
    _GnTrailPassThroughIndex_Type()
)
gnTrailPassThroughIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnTrailPassThroughIndex.setStatus("mandatory")


class _GnTrailPassThroughName_Type(DisplayString):
    """Custom type gnTrailPassThroughName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_GnTrailPassThroughName_Type.__name__ = "DisplayString"
_GnTrailPassThroughName_Object = MibTableColumn
gnTrailPassThroughName = _GnTrailPassThroughName_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 9, 1, 1, 2),
    _GnTrailPassThroughName_Type()
)
gnTrailPassThroughName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnTrailPassThroughName.setStatus("mandatory")
_GnGigabitEthernetCfg_ObjectIdentity = ObjectIdentity
gnGigabitEthernetCfg = _GnGigabitEthernetCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 4, 10)
)
_GnGigabitEthernetCfgTable_Object = MibTable
gnGigabitEthernetCfgTable = _GnGigabitEthernetCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 10, 1)
)
if mibBuilder.loadTexts:
    gnGigabitEthernetCfgTable.setStatus("mandatory")
_GnGigabitEthernetCfgEntry_Object = MibTableRow
gnGigabitEthernetCfgEntry = _GnGigabitEthernetCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 10, 1, 1)
)
gnGigabitEthernetCfgEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    gnGigabitEthernetCfgEntry.setStatus("mandatory")


class _GnGigabitEthernetCfgPauseFrameGenerating_Type(Integer32):
    """Custom type gnGigabitEthernetCfgPauseFrameGenerating based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("enable", 2))
    )


_GnGigabitEthernetCfgPauseFrameGenerating_Type.__name__ = "Integer32"
_GnGigabitEthernetCfgPauseFrameGenerating_Object = MibTableColumn
gnGigabitEthernetCfgPauseFrameGenerating = _GnGigabitEthernetCfgPauseFrameGenerating_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 10, 1, 1, 1),
    _GnGigabitEthernetCfgPauseFrameGenerating_Type()
)
gnGigabitEthernetCfgPauseFrameGenerating.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnGigabitEthernetCfgPauseFrameGenerating.setStatus("mandatory")


class _GnGigabitEthernetCfgMuteOnExcError_Type(Integer32):
    """Custom type gnGigabitEthernetCfgMuteOnExcError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("enable", 2))
    )


_GnGigabitEthernetCfgMuteOnExcError_Type.__name__ = "Integer32"
_GnGigabitEthernetCfgMuteOnExcError_Object = MibTableColumn
gnGigabitEthernetCfgMuteOnExcError = _GnGigabitEthernetCfgMuteOnExcError_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 10, 1, 1, 2),
    _GnGigabitEthernetCfgMuteOnExcError_Type()
)
gnGigabitEthernetCfgMuteOnExcError.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnGigabitEthernetCfgMuteOnExcError.setStatus("mandatory")


class _GnGigabitEthernetCfgMuteOnSd_Type(Integer32):
    """Custom type gnGigabitEthernetCfgMuteOnSd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("enable", 2))
    )


_GnGigabitEthernetCfgMuteOnSd_Type.__name__ = "Integer32"
_GnGigabitEthernetCfgMuteOnSd_Object = MibTableColumn
gnGigabitEthernetCfgMuteOnSd = _GnGigabitEthernetCfgMuteOnSd_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 10, 1, 1, 3),
    _GnGigabitEthernetCfgMuteOnSd_Type()
)
gnGigabitEthernetCfgMuteOnSd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnGigabitEthernetCfgMuteOnSd.setStatus("mandatory")


class _GnGigabitEthernetCfgMuteOnRemoteRadioFault_Type(Integer32):
    """Custom type gnGigabitEthernetCfgMuteOnRemoteRadioFault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("enable", 2))
    )


_GnGigabitEthernetCfgMuteOnRemoteRadioFault_Type.__name__ = "Integer32"
_GnGigabitEthernetCfgMuteOnRemoteRadioFault_Object = MibTableColumn
gnGigabitEthernetCfgMuteOnRemoteRadioFault = _GnGigabitEthernetCfgMuteOnRemoteRadioFault_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 10, 1, 1, 4),
    _GnGigabitEthernetCfgMuteOnRemoteRadioFault_Type()
)
gnGigabitEthernetCfgMuteOnRemoteRadioFault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnGigabitEthernetCfgMuteOnRemoteRadioFault.setStatus("mandatory")


class _GnGigabitEthernetCfgSpeedAndDuplex_Type(Integer32):
    """Custom type gnGigabitEthernetCfgSpeedAndDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("autoNegotiation", 2),
          ("hundredBasedFullDuplex", 5),
          ("hundredBasedHalfDuplex", 6),
          ("tenBasedFullDuplex", 7),
          ("tenBasedHalfDuplex", 8),
          ("thousandBasedFullDuplex", 3),
          ("thousandBasedHalfDuplex", 4))
    )


_GnGigabitEthernetCfgSpeedAndDuplex_Type.__name__ = "Integer32"
_GnGigabitEthernetCfgSpeedAndDuplex_Object = MibTableColumn
gnGigabitEthernetCfgSpeedAndDuplex = _GnGigabitEthernetCfgSpeedAndDuplex_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 10, 1, 1, 5),
    _GnGigabitEthernetCfgSpeedAndDuplex_Type()
)
gnGigabitEthernetCfgSpeedAndDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnGigabitEthernetCfgSpeedAndDuplex.setStatus("mandatory")


class _GnGigabitEthernetCfgSchedulerPriorityOption_Type(Integer32):
    """Custom type gnGigabitEthernetCfgSchedulerPriorityOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hrr", 3),
          ("strict", 2))
    )


_GnGigabitEthernetCfgSchedulerPriorityOption_Type.__name__ = "Integer32"
_GnGigabitEthernetCfgSchedulerPriorityOption_Object = MibTableColumn
gnGigabitEthernetCfgSchedulerPriorityOption = _GnGigabitEthernetCfgSchedulerPriorityOption_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 10, 1, 1, 6),
    _GnGigabitEthernetCfgSchedulerPriorityOption_Type()
)
gnGigabitEthernetCfgSchedulerPriorityOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnGigabitEthernetCfgSchedulerPriorityOption.setStatus("mandatory")


class _GnGigabitEthernetCfgSchedulerQueue1Weight_Type(Integer32):
    """Custom type gnGigabitEthernetCfgSchedulerQueue1Weight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            17
        )
    )
    namedValues = NamedValues(
        ("strict", 17)
    )


_GnGigabitEthernetCfgSchedulerQueue1Weight_Type.__name__ = "Integer32"
_GnGigabitEthernetCfgSchedulerQueue1Weight_Object = MibTableColumn
gnGigabitEthernetCfgSchedulerQueue1Weight = _GnGigabitEthernetCfgSchedulerQueue1Weight_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 10, 1, 1, 7),
    _GnGigabitEthernetCfgSchedulerQueue1Weight_Type()
)
gnGigabitEthernetCfgSchedulerQueue1Weight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnGigabitEthernetCfgSchedulerQueue1Weight.setStatus("mandatory")


class _GnGigabitEthernetCfgSchedulerQueue2Weight_Type(Integer32):
    """Custom type gnGigabitEthernetCfgSchedulerQueue2Weight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_GnGigabitEthernetCfgSchedulerQueue2Weight_Type.__name__ = "Integer32"
_GnGigabitEthernetCfgSchedulerQueue2Weight_Object = MibTableColumn
gnGigabitEthernetCfgSchedulerQueue2Weight = _GnGigabitEthernetCfgSchedulerQueue2Weight_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 10, 1, 1, 8),
    _GnGigabitEthernetCfgSchedulerQueue2Weight_Type()
)
gnGigabitEthernetCfgSchedulerQueue2Weight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnGigabitEthernetCfgSchedulerQueue2Weight.setStatus("mandatory")


class _GnGigabitEthernetCfgSchedulerQueue3Weight_Type(Integer32):
    """Custom type gnGigabitEthernetCfgSchedulerQueue3Weight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_GnGigabitEthernetCfgSchedulerQueue3Weight_Type.__name__ = "Integer32"
_GnGigabitEthernetCfgSchedulerQueue3Weight_Object = MibTableColumn
gnGigabitEthernetCfgSchedulerQueue3Weight = _GnGigabitEthernetCfgSchedulerQueue3Weight_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 10, 1, 1, 9),
    _GnGigabitEthernetCfgSchedulerQueue3Weight_Type()
)
gnGigabitEthernetCfgSchedulerQueue3Weight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnGigabitEthernetCfgSchedulerQueue3Weight.setStatus("mandatory")


class _GnGigabitEthernetCfgSchedulerQueue4Weight_Type(Integer32):
    """Custom type gnGigabitEthernetCfgSchedulerQueue4Weight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_GnGigabitEthernetCfgSchedulerQueue4Weight_Type.__name__ = "Integer32"
_GnGigabitEthernetCfgSchedulerQueue4Weight_Object = MibTableColumn
gnGigabitEthernetCfgSchedulerQueue4Weight = _GnGigabitEthernetCfgSchedulerQueue4Weight_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 10, 1, 1, 10),
    _GnGigabitEthernetCfgSchedulerQueue4Weight_Type()
)
gnGigabitEthernetCfgSchedulerQueue4Weight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnGigabitEthernetCfgSchedulerQueue4Weight.setStatus("mandatory")


class _GnGigabitEthernetCfgClassifierFirstPrioUDP_Type(Integer32):
    """Custom type gnGigabitEthernetCfgClassifierFirstPrioUDP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("enable", 2))
    )


_GnGigabitEthernetCfgClassifierFirstPrioUDP_Type.__name__ = "Integer32"
_GnGigabitEthernetCfgClassifierFirstPrioUDP_Object = MibTableColumn
gnGigabitEthernetCfgClassifierFirstPrioUDP = _GnGigabitEthernetCfgClassifierFirstPrioUDP_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 10, 1, 1, 11),
    _GnGigabitEthernetCfgClassifierFirstPrioUDP_Type()
)
gnGigabitEthernetCfgClassifierFirstPrioUDP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnGigabitEthernetCfgClassifierFirstPrioUDP.setStatus("mandatory")


class _GnGigabitEthernetCfgClassifierPrioBitSource_Type(Integer32):
    """Custom type gnGigabitEthernetCfgClassifierPrioBitSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("externalOverhead", 3),
          ("ip", 5),
          ("mpls", 6),
          ("none", 2),
          ("vlan", 4))
    )


_GnGigabitEthernetCfgClassifierPrioBitSource_Type.__name__ = "Integer32"
_GnGigabitEthernetCfgClassifierPrioBitSource_Object = MibTableColumn
gnGigabitEthernetCfgClassifierPrioBitSource = _GnGigabitEthernetCfgClassifierPrioBitSource_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 10, 1, 1, 12),
    _GnGigabitEthernetCfgClassifierPrioBitSource_Type()
)
gnGigabitEthernetCfgClassifierPrioBitSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnGigabitEthernetCfgClassifierPrioBitSource.setStatus("mandatory")


class _GnGigabitEthernetCfgClassifierGroupMinVlanId_Type(Integer32):
    """Custom type gnGigabitEthernetCfgClassifierGroupMinVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_GnGigabitEthernetCfgClassifierGroupMinVlanId_Type.__name__ = "Integer32"
_GnGigabitEthernetCfgClassifierGroupMinVlanId_Object = MibTableColumn
gnGigabitEthernetCfgClassifierGroupMinVlanId = _GnGigabitEthernetCfgClassifierGroupMinVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 10, 1, 1, 13),
    _GnGigabitEthernetCfgClassifierGroupMinVlanId_Type()
)
gnGigabitEthernetCfgClassifierGroupMinVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnGigabitEthernetCfgClassifierGroupMinVlanId.setStatus("mandatory")


class _GnGigabitEthernetCfgClassifierGroupMaxVlanId_Type(Integer32):
    """Custom type gnGigabitEthernetCfgClassifierGroupMaxVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_GnGigabitEthernetCfgClassifierGroupMaxVlanId_Type.__name__ = "Integer32"
_GnGigabitEthernetCfgClassifierGroupMaxVlanId_Object = MibTableColumn
gnGigabitEthernetCfgClassifierGroupMaxVlanId = _GnGigabitEthernetCfgClassifierGroupMaxVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 10, 1, 1, 14),
    _GnGigabitEthernetCfgClassifierGroupMaxVlanId_Type()
)
gnGigabitEthernetCfgClassifierGroupMaxVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnGigabitEthernetCfgClassifierGroupMaxVlanId.setStatus("mandatory")


class _GnGigabitEthernetCfgClassifierGroupVlanPriority_Type(Integer32):
    """Custom type gnGigabitEthernetCfgClassifierGroupVlanPriority based on Integer32"""
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
        *(("clear", 0),
          ("queue1", 1),
          ("queue2", 2),
          ("queue3", 3),
          ("queue4", 4))
    )


_GnGigabitEthernetCfgClassifierGroupVlanPriority_Type.__name__ = "Integer32"
_GnGigabitEthernetCfgClassifierGroupVlanPriority_Object = MibTableColumn
gnGigabitEthernetCfgClassifierGroupVlanPriority = _GnGigabitEthernetCfgClassifierGroupVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 10, 1, 1, 15),
    _GnGigabitEthernetCfgClassifierGroupVlanPriority_Type()
)
gnGigabitEthernetCfgClassifierGroupVlanPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnGigabitEthernetCfgClassifierGroupVlanPriority.setStatus("mandatory")


class _GnGigabitEthernetCfgClassifierGroupVlanSet_Type(Integer32):
    """Custom type gnGigabitEthernetCfgClassifierGroupVlanSet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("notActive", 3))
    )


_GnGigabitEthernetCfgClassifierGroupVlanSet_Type.__name__ = "Integer32"
_GnGigabitEthernetCfgClassifierGroupVlanSet_Object = MibTableColumn
gnGigabitEthernetCfgClassifierGroupVlanSet = _GnGigabitEthernetCfgClassifierGroupVlanSet_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 10, 1, 1, 16),
    _GnGigabitEthernetCfgClassifierGroupVlanSet_Type()
)
gnGigabitEthernetCfgClassifierGroupVlanSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnGigabitEthernetCfgClassifierGroupVlanSet.setStatus("mandatory")


class _GnGigabitEthernetCfgAcmMuteOnMinConstellation_Type(Integer32):
    """Custom type gnGigabitEthernetCfgAcmMuteOnMinConstellation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("acm128QAM", 7),
          ("acm16QAM", 4),
          ("acm256QAM", 8),
          ("acm32QAM", 5),
          ("acm4QAM", 2),
          ("acm64QAM", 6),
          ("acm8QAM", 3))
    )


_GnGigabitEthernetCfgAcmMuteOnMinConstellation_Type.__name__ = "Integer32"
_GnGigabitEthernetCfgAcmMuteOnMinConstellation_Object = MibTableColumn
gnGigabitEthernetCfgAcmMuteOnMinConstellation = _GnGigabitEthernetCfgAcmMuteOnMinConstellation_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 10, 1, 1, 17),
    _GnGigabitEthernetCfgAcmMuteOnMinConstellation_Type()
)
gnGigabitEthernetCfgAcmMuteOnMinConstellation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnGigabitEthernetCfgAcmMuteOnMinConstellation.setStatus("mandatory")


class _GnGigabitEthernetCfgEnableAutomaticTxMute_Type(Integer32):
    """Custom type gnGigabitEthernetCfgEnableAutomaticTxMute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("enable", 2))
    )


_GnGigabitEthernetCfgEnableAutomaticTxMute_Type.__name__ = "Integer32"
_GnGigabitEthernetCfgEnableAutomaticTxMute_Object = MibTableColumn
gnGigabitEthernetCfgEnableAutomaticTxMute = _GnGigabitEthernetCfgEnableAutomaticTxMute_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 10, 1, 1, 18),
    _GnGigabitEthernetCfgEnableAutomaticTxMute_Type()
)
gnGigabitEthernetCfgEnableAutomaticTxMute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnGigabitEthernetCfgEnableAutomaticTxMute.setStatus("mandatory")


class _GnGigabitEthernetCfgTrafficBISTAdmin_Type(Integer32):
    """Custom type gnGigabitEthernetCfgTrafficBISTAdmin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("notActive", 3))
    )


_GnGigabitEthernetCfgTrafficBISTAdmin_Type.__name__ = "Integer32"
_GnGigabitEthernetCfgTrafficBISTAdmin_Object = MibTableColumn
gnGigabitEthernetCfgTrafficBISTAdmin = _GnGigabitEthernetCfgTrafficBISTAdmin_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 10, 1, 1, 19),
    _GnGigabitEthernetCfgTrafficBISTAdmin_Type()
)
gnGigabitEthernetCfgTrafficBISTAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnGigabitEthernetCfgTrafficBISTAdmin.setStatus("mandatory")


class _GnGigabitEthernetCfgClearStatistics_Type(Integer32):
    """Custom type gnGigabitEthernetCfgClearStatistics based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clear", 3),
          ("noAction", 2))
    )


_GnGigabitEthernetCfgClearStatistics_Type.__name__ = "Integer32"
_GnGigabitEthernetCfgClearStatistics_Object = MibTableColumn
gnGigabitEthernetCfgClearStatistics = _GnGigabitEthernetCfgClearStatistics_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 10, 1, 1, 20),
    _GnGigabitEthernetCfgClearStatistics_Type()
)
gnGigabitEthernetCfgClearStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnGigabitEthernetCfgClearStatistics.setStatus("mandatory")


class _GnGigabitEthernetCfgPauseFrameForwarding_Type(Integer32):
    """Custom type gnGigabitEthernetCfgPauseFrameForwarding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("enable", 2))
    )


_GnGigabitEthernetCfgPauseFrameForwarding_Type.__name__ = "Integer32"
_GnGigabitEthernetCfgPauseFrameForwarding_Object = MibTableColumn
gnGigabitEthernetCfgPauseFrameForwarding = _GnGigabitEthernetCfgPauseFrameForwarding_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 10, 1, 1, 21),
    _GnGigabitEthernetCfgPauseFrameForwarding_Type()
)
gnGigabitEthernetCfgPauseFrameForwarding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnGigabitEthernetCfgPauseFrameForwarding.setStatus("mandatory")


class _GnGigabitEthernetCfgPhyLoopback_Type(Integer32):
    """Custom type gnGigabitEthernetCfgPhyLoopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("interfaceInterLoop", 3),
          ("noloopback", 2))
    )


_GnGigabitEthernetCfgPhyLoopback_Type.__name__ = "Integer32"
_GnGigabitEthernetCfgPhyLoopback_Object = MibTableColumn
gnGigabitEthernetCfgPhyLoopback = _GnGigabitEthernetCfgPhyLoopback_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 10, 1, 1, 22),
    _GnGigabitEthernetCfgPhyLoopback_Type()
)
gnGigabitEthernetCfgPhyLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gnGigabitEthernetCfgPhyLoopback.setStatus("mandatory")
_GnVlanEthernetStat_ObjectIdentity = ObjectIdentity
gnVlanEthernetStat = _GnVlanEthernetStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 4, 11)
)
_GnVlanEthernetStatTable_Object = MibTable
gnVlanEthernetStatTable = _GnVlanEthernetStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 11, 1)
)
if mibBuilder.loadTexts:
    gnVlanEthernetStatTable.setStatus("mandatory")
_GnVlanEthernetStatEntry_Object = MibTableRow
gnVlanEthernetStatEntry = _GnVlanEthernetStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 11, 1, 1)
)
gnVlanEthernetStatEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CERAGON-MIB", "gnVlanEthernetStatGroupId"),
)
if mibBuilder.loadTexts:
    gnVlanEthernetStatEntry.setStatus("mandatory")


class _GnVlanEthernetStatGroupId_Type(Integer32):
    """Custom type gnVlanEthernetStatGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_GnVlanEthernetStatGroupId_Type.__name__ = "Integer32"
_GnVlanEthernetStatGroupId_Object = MibTableColumn
gnVlanEthernetStatGroupId = _GnVlanEthernetStatGroupId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 11, 1, 1, 1),
    _GnVlanEthernetStatGroupId_Type()
)
gnVlanEthernetStatGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnVlanEthernetStatGroupId.setStatus("mandatory")


class _GnVlanEthernetStatMinVlanId_Type(Integer32):
    """Custom type gnVlanEthernetStatMinVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_GnVlanEthernetStatMinVlanId_Type.__name__ = "Integer32"
_GnVlanEthernetStatMinVlanId_Object = MibTableColumn
gnVlanEthernetStatMinVlanId = _GnVlanEthernetStatMinVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 11, 1, 1, 2),
    _GnVlanEthernetStatMinVlanId_Type()
)
gnVlanEthernetStatMinVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnVlanEthernetStatMinVlanId.setStatus("mandatory")


class _GnVlanEthernetStatMaxVlanId_Type(Integer32):
    """Custom type gnVlanEthernetStatMaxVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_GnVlanEthernetStatMaxVlanId_Type.__name__ = "Integer32"
_GnVlanEthernetStatMaxVlanId_Object = MibTableColumn
gnVlanEthernetStatMaxVlanId = _GnVlanEthernetStatMaxVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 11, 1, 1, 3),
    _GnVlanEthernetStatMaxVlanId_Type()
)
gnVlanEthernetStatMaxVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnVlanEthernetStatMaxVlanId.setStatus("mandatory")


class _GnVlanEthernetStatVlanPriority_Type(Integer32):
    """Custom type gnVlanEthernetStatVlanPriority based on Integer32"""
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
        *(("queue1", 1),
          ("queue2", 2),
          ("queue3", 3),
          ("queue4", 4))
    )


_GnVlanEthernetStatVlanPriority_Type.__name__ = "Integer32"
_GnVlanEthernetStatVlanPriority_Object = MibTableColumn
gnVlanEthernetStatVlanPriority = _GnVlanEthernetStatVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 11, 1, 1, 4),
    _GnVlanEthernetStatVlanPriority_Type()
)
gnVlanEthernetStatVlanPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnVlanEthernetStatVlanPriority.setStatus("mandatory")
_GnGigabitEthernetStat_ObjectIdentity = ObjectIdentity
gnGigabitEthernetStat = _GnGigabitEthernetStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 4, 12)
)
_GnGigabitEthernetStatTable_Object = MibTable
gnGigabitEthernetStatTable = _GnGigabitEthernetStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 12, 1)
)
if mibBuilder.loadTexts:
    gnGigabitEthernetStatTable.setStatus("mandatory")
_GnGigabitEthernetStatEntry_Object = MibTableRow
gnGigabitEthernetStatEntry = _GnGigabitEthernetStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 12, 1, 1)
)
gnGigabitEthernetStatEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    gnGigabitEthernetStatEntry.setStatus("mandatory")
_GnGigabitEthernetStatBistErrorSeconds_Type = Integer32
_GnGigabitEthernetStatBistErrorSeconds_Object = MibTableColumn
gnGigabitEthernetStatBistErrorSeconds = _GnGigabitEthernetStatBistErrorSeconds_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 12, 1, 1, 1),
    _GnGigabitEthernetStatBistErrorSeconds_Type()
)
gnGigabitEthernetStatBistErrorSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnGigabitEthernetStatBistErrorSeconds.setStatus("mandatory")


class _GnGigabitEthernetStatSpeedAndDuplexSupport_Type(OctetString):
    """Custom type gnGigabitEthernetStatSpeedAndDuplexSupport based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_GnGigabitEthernetStatSpeedAndDuplexSupport_Type.__name__ = "OctetString"
_GnGigabitEthernetStatSpeedAndDuplexSupport_Object = MibTableColumn
gnGigabitEthernetStatSpeedAndDuplexSupport = _GnGigabitEthernetStatSpeedAndDuplexSupport_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 12, 1, 1, 2),
    _GnGigabitEthernetStatSpeedAndDuplexSupport_Type()
)
gnGigabitEthernetStatSpeedAndDuplexSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnGigabitEthernetStatSpeedAndDuplexSupport.setStatus("mandatory")


class _GnGigabitEthernetStatValidIntervals_Type(Integer32):
    """Custom type gnGigabitEthernetStatValidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_GnGigabitEthernetStatValidIntervals_Type.__name__ = "Integer32"
_GnGigabitEthernetStatValidIntervals_Object = MibTableColumn
gnGigabitEthernetStatValidIntervals = _GnGigabitEthernetStatValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 12, 1, 1, 3),
    _GnGigabitEthernetStatValidIntervals_Type()
)
gnGigabitEthernetStatValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnGigabitEthernetStatValidIntervals.setStatus("mandatory")


class _GnGigabitEthernetStatSpeedAndDuplexMode_Type(Integer32):
    """Custom type gnGigabitEthernetStatSpeedAndDuplexMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("hundredBasedFullDuplex", 5),
          ("hundredBasedHalfDuplex", 6),
          ("tenBasedFullDuplex", 7),
          ("tenBasedHalfDuplex", 8),
          ("thousandBasedFullDuplex", 3),
          ("thousandBasedHalfDuplex", 4))
    )


_GnGigabitEthernetStatSpeedAndDuplexMode_Type.__name__ = "Integer32"
_GnGigabitEthernetStatSpeedAndDuplexMode_Object = MibTableColumn
gnGigabitEthernetStatSpeedAndDuplexMode = _GnGigabitEthernetStatSpeedAndDuplexMode_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 12, 1, 1, 4),
    _GnGigabitEthernetStatSpeedAndDuplexMode_Type()
)
gnGigabitEthernetStatSpeedAndDuplexMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnGigabitEthernetStatSpeedAndDuplexMode.setStatus("mandatory")
_GnGigabitEthernetMon_ObjectIdentity = ObjectIdentity
gnGigabitEthernetMon = _GnGigabitEthernetMon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 4, 13)
)
_GnGigabitEthernetMonCurrTable_Object = MibTable
gnGigabitEthernetMonCurrTable = _GnGigabitEthernetMonCurrTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 13, 1)
)
if mibBuilder.loadTexts:
    gnGigabitEthernetMonCurrTable.setStatus("mandatory")
_GnGigabitEthernetMonCurrEntry_Object = MibTableRow
gnGigabitEthernetMonCurrEntry = _GnGigabitEthernetMonCurrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 13, 1, 1)
)
gnGigabitEthernetMonCurrEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    gnGigabitEthernetMonCurrEntry.setStatus("mandatory")


class _GnGigabitEthernetMonCurrPacketErrorRate_Type(Integer32):
    """Custom type gnGigabitEthernetMonCurrPacketErrorRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_GnGigabitEthernetMonCurrPacketErrorRate_Type.__name__ = "Integer32"
_GnGigabitEthernetMonCurrPacketErrorRate_Object = MibTableColumn
gnGigabitEthernetMonCurrPacketErrorRate = _GnGigabitEthernetMonCurrPacketErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 13, 1, 1, 1),
    _GnGigabitEthernetMonCurrPacketErrorRate_Type()
)
gnGigabitEthernetMonCurrPacketErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnGigabitEthernetMonCurrPacketErrorRate.setStatus("mandatory")


class _GnGigabitEthernetMonCurrIDF_Type(Integer32):
    """Custom type gnGigabitEthernetMonCurrIDF based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3))
    )


_GnGigabitEthernetMonCurrIDF_Type.__name__ = "Integer32"
_GnGigabitEthernetMonCurrIDF_Object = MibTableColumn
gnGigabitEthernetMonCurrIDF = _GnGigabitEthernetMonCurrIDF_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 13, 1, 1, 2),
    _GnGigabitEthernetMonCurrIDF_Type()
)
gnGigabitEthernetMonCurrIDF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnGigabitEthernetMonCurrIDF.setStatus("mandatory")


class _GnGigabitEthernetMonCurrDayPacketErrorRate_Type(Integer32):
    """Custom type gnGigabitEthernetMonCurrDayPacketErrorRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_GnGigabitEthernetMonCurrDayPacketErrorRate_Type.__name__ = "Integer32"
_GnGigabitEthernetMonCurrDayPacketErrorRate_Object = MibTableColumn
gnGigabitEthernetMonCurrDayPacketErrorRate = _GnGigabitEthernetMonCurrDayPacketErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 13, 1, 1, 3),
    _GnGigabitEthernetMonCurrDayPacketErrorRate_Type()
)
gnGigabitEthernetMonCurrDayPacketErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnGigabitEthernetMonCurrDayPacketErrorRate.setStatus("mandatory")


class _GnGigabitEthernetMonCurrDayIDF_Type(Integer32):
    """Custom type gnGigabitEthernetMonCurrDayIDF based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3))
    )


_GnGigabitEthernetMonCurrDayIDF_Type.__name__ = "Integer32"
_GnGigabitEthernetMonCurrDayIDF_Object = MibTableColumn
gnGigabitEthernetMonCurrDayIDF = _GnGigabitEthernetMonCurrDayIDF_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 13, 1, 1, 4),
    _GnGigabitEthernetMonCurrDayIDF_Type()
)
gnGigabitEthernetMonCurrDayIDF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnGigabitEthernetMonCurrDayIDF.setStatus("mandatory")
_GnGigabitEthernetMonIntervalTable_Object = MibTable
gnGigabitEthernetMonIntervalTable = _GnGigabitEthernetMonIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 13, 2)
)
if mibBuilder.loadTexts:
    gnGigabitEthernetMonIntervalTable.setStatus("mandatory")
_GnGigabitEthernetMonIntervalEntry_Object = MibTableRow
gnGigabitEthernetMonIntervalEntry = _GnGigabitEthernetMonIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 13, 2, 1)
)
gnGigabitEthernetMonIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CERAGON-MIB", "gnGigabitEthernetMonIntervalIdx"),
)
if mibBuilder.loadTexts:
    gnGigabitEthernetMonIntervalEntry.setStatus("mandatory")


class _GnGigabitEthernetMonIntervalIdx_Type(Integer32):
    """Custom type gnGigabitEthernetMonIntervalIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_GnGigabitEthernetMonIntervalIdx_Type.__name__ = "Integer32"
_GnGigabitEthernetMonIntervalIdx_Object = MibTableColumn
gnGigabitEthernetMonIntervalIdx = _GnGigabitEthernetMonIntervalIdx_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 13, 2, 1, 1),
    _GnGigabitEthernetMonIntervalIdx_Type()
)
gnGigabitEthernetMonIntervalIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnGigabitEthernetMonIntervalIdx.setStatus("mandatory")


class _GnGigabitEthernetMonIntervalPacketErrorRate_Type(Integer32):
    """Custom type gnGigabitEthernetMonIntervalPacketErrorRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_GnGigabitEthernetMonIntervalPacketErrorRate_Type.__name__ = "Integer32"
_GnGigabitEthernetMonIntervalPacketErrorRate_Object = MibTableColumn
gnGigabitEthernetMonIntervalPacketErrorRate = _GnGigabitEthernetMonIntervalPacketErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 13, 2, 1, 2),
    _GnGigabitEthernetMonIntervalPacketErrorRate_Type()
)
gnGigabitEthernetMonIntervalPacketErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnGigabitEthernetMonIntervalPacketErrorRate.setStatus("mandatory")


class _GnGigabitEthernetMonIntervalIDF_Type(Integer32):
    """Custom type gnGigabitEthernetMonIntervalIDF based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3))
    )


_GnGigabitEthernetMonIntervalIDF_Type.__name__ = "Integer32"
_GnGigabitEthernetMonIntervalIDF_Object = MibTableColumn
gnGigabitEthernetMonIntervalIDF = _GnGigabitEthernetMonIntervalIDF_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 13, 2, 1, 3),
    _GnGigabitEthernetMonIntervalIDF_Type()
)
gnGigabitEthernetMonIntervalIDF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnGigabitEthernetMonIntervalIDF.setStatus("mandatory")
_GnGigabitEthernetMonDayTable_Object = MibTable
gnGigabitEthernetMonDayTable = _GnGigabitEthernetMonDayTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 13, 3)
)
if mibBuilder.loadTexts:
    gnGigabitEthernetMonDayTable.setStatus("mandatory")
_GnGigabitEthernetMonDayEntry_Object = MibTableRow
gnGigabitEthernetMonDayEntry = _GnGigabitEthernetMonDayEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 13, 3, 1)
)
gnGigabitEthernetMonDayEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CERAGON-MIB", "gnGigabitEthernetMonDayIdx"),
)
if mibBuilder.loadTexts:
    gnGigabitEthernetMonDayEntry.setStatus("mandatory")


class _GnGigabitEthernetMonDayIdx_Type(Integer32):
    """Custom type gnGigabitEthernetMonDayIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_GnGigabitEthernetMonDayIdx_Type.__name__ = "Integer32"
_GnGigabitEthernetMonDayIdx_Object = MibTableColumn
gnGigabitEthernetMonDayIdx = _GnGigabitEthernetMonDayIdx_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 13, 3, 1, 1),
    _GnGigabitEthernetMonDayIdx_Type()
)
gnGigabitEthernetMonDayIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnGigabitEthernetMonDayIdx.setStatus("mandatory")


class _GnGigabitEthernetMonDayPacketErrorRate_Type(Integer32):
    """Custom type gnGigabitEthernetMonDayPacketErrorRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_GnGigabitEthernetMonDayPacketErrorRate_Type.__name__ = "Integer32"
_GnGigabitEthernetMonDayPacketErrorRate_Object = MibTableColumn
gnGigabitEthernetMonDayPacketErrorRate = _GnGigabitEthernetMonDayPacketErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 13, 3, 1, 2),
    _GnGigabitEthernetMonDayPacketErrorRate_Type()
)
gnGigabitEthernetMonDayPacketErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnGigabitEthernetMonDayPacketErrorRate.setStatus("mandatory")


class _GnGigabitEthernetMonDayIDF_Type(Integer32):
    """Custom type gnGigabitEthernetMonDayIDF based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3))
    )


_GnGigabitEthernetMonDayIDF_Type.__name__ = "Integer32"
_GnGigabitEthernetMonDayIDF_Object = MibTableColumn
gnGigabitEthernetMonDayIDF = _GnGigabitEthernetMonDayIDF_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 13, 3, 1, 3),
    _GnGigabitEthernetMonDayIDF_Type()
)
gnGigabitEthernetMonDayIDF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnGigabitEthernetMonDayIDF.setStatus("mandatory")
_GnEthStatistic_ObjectIdentity = ObjectIdentity
gnEthStatistic = _GnEthStatistic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 4, 14)
)
_GnEthStatisticTable_Object = MibTable
gnEthStatisticTable = _GnEthStatisticTable_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 14, 1)
)
if mibBuilder.loadTexts:
    gnEthStatisticTable.setStatus("mandatory")
_GnEthStatisticEntry_Object = MibTableRow
gnEthStatisticEntry = _GnEthStatisticEntry_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 14, 1, 1)
)
gnEthStatisticEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    gnEthStatisticEntry.setStatus("mandatory")
_GnEthStatisticIfInOctetsMsb_Type = Counter32
_GnEthStatisticIfInOctetsMsb_Object = MibTableColumn
gnEthStatisticIfInOctetsMsb = _GnEthStatisticIfInOctetsMsb_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 14, 1, 1, 1),
    _GnEthStatisticIfInOctetsMsb_Type()
)
gnEthStatisticIfInOctetsMsb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnEthStatisticIfInOctetsMsb.setStatus("mandatory")
_GnEthStatisticAFrameReceivedOkLsb_Type = Counter32
_GnEthStatisticAFrameReceivedOkLsb_Object = MibTableColumn
gnEthStatisticAFrameReceivedOkLsb = _GnEthStatisticAFrameReceivedOkLsb_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 14, 1, 1, 2),
    _GnEthStatisticAFrameReceivedOkLsb_Type()
)
gnEthStatisticAFrameReceivedOkLsb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnEthStatisticAFrameReceivedOkLsb.setStatus("mandatory")
_GnEthStatisticAFrameReceivedOkMsb_Type = Counter32
_GnEthStatisticAFrameReceivedOkMsb_Object = MibTableColumn
gnEthStatisticAFrameReceivedOkMsb = _GnEthStatisticAFrameReceivedOkMsb_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 14, 1, 1, 3),
    _GnEthStatisticAFrameReceivedOkMsb_Type()
)
gnEthStatisticAFrameReceivedOkMsb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnEthStatisticAFrameReceivedOkMsb.setStatus("mandatory")
_GnEthStatisticCRCAlignErrorsMsb_Type = Counter32
_GnEthStatisticCRCAlignErrorsMsb_Object = MibTableColumn
gnEthStatisticCRCAlignErrorsMsb = _GnEthStatisticCRCAlignErrorsMsb_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 14, 1, 1, 4),
    _GnEthStatisticCRCAlignErrorsMsb_Type()
)
gnEthStatisticCRCAlignErrorsMsb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnEthStatisticCRCAlignErrorsMsb.setStatus("mandatory")
_GnEthStatisticIfInUcastPktsMsb_Type = Counter32
_GnEthStatisticIfInUcastPktsMsb_Object = MibTableColumn
gnEthStatisticIfInUcastPktsMsb = _GnEthStatisticIfInUcastPktsMsb_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 14, 1, 1, 5),
    _GnEthStatisticIfInUcastPktsMsb_Type()
)
gnEthStatisticIfInUcastPktsMsb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnEthStatisticIfInUcastPktsMsb.setStatus("mandatory")
_GnEthStatisticBroadcastPktsMsb_Type = Counter32
_GnEthStatisticBroadcastPktsMsb_Object = MibTableColumn
gnEthStatisticBroadcastPktsMsb = _GnEthStatisticBroadcastPktsMsb_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 14, 1, 1, 6),
    _GnEthStatisticBroadcastPktsMsb_Type()
)
gnEthStatisticBroadcastPktsMsb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnEthStatisticBroadcastPktsMsb.setStatus("mandatory")
_GnEthStatisticMulticastPktsMsb_Type = Counter32
_GnEthStatisticMulticastPktsMsb_Object = MibTableColumn
gnEthStatisticMulticastPktsMsb = _GnEthStatisticMulticastPktsMsb_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 14, 1, 1, 7),
    _GnEthStatisticMulticastPktsMsb_Type()
)
gnEthStatisticMulticastPktsMsb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnEthStatisticMulticastPktsMsb.setStatus("mandatory")
_GnEthStatisticUndersizePktsMsb_Type = Counter32
_GnEthStatisticUndersizePktsMsb_Object = MibTableColumn
gnEthStatisticUndersizePktsMsb = _GnEthStatisticUndersizePktsMsb_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 14, 1, 1, 8),
    _GnEthStatisticUndersizePktsMsb_Type()
)
gnEthStatisticUndersizePktsMsb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnEthStatisticUndersizePktsMsb.setStatus("mandatory")
_GnEthStatisticOversizePktsMsb_Type = Counter32
_GnEthStatisticOversizePktsMsb_Object = MibTableColumn
gnEthStatisticOversizePktsMsb = _GnEthStatisticOversizePktsMsb_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 14, 1, 1, 9),
    _GnEthStatisticOversizePktsMsb_Type()
)
gnEthStatisticOversizePktsMsb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnEthStatisticOversizePktsMsb.setStatus("mandatory")
_GnEthStatisticPkts64OctetMsb_Type = Counter32
_GnEthStatisticPkts64OctetMsb_Object = MibTableColumn
gnEthStatisticPkts64OctetMsb = _GnEthStatisticPkts64OctetMsb_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 14, 1, 1, 10),
    _GnEthStatisticPkts64OctetMsb_Type()
)
gnEthStatisticPkts64OctetMsb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnEthStatisticPkts64OctetMsb.setStatus("mandatory")
_GnEthStatisticPkts65to127OctetMsb_Type = Counter32
_GnEthStatisticPkts65to127OctetMsb_Object = MibTableColumn
gnEthStatisticPkts65to127OctetMsb = _GnEthStatisticPkts65to127OctetMsb_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 14, 1, 1, 11),
    _GnEthStatisticPkts65to127OctetMsb_Type()
)
gnEthStatisticPkts65to127OctetMsb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnEthStatisticPkts65to127OctetMsb.setStatus("mandatory")
_GnEthStatisticPkts128to255OctetMsb_Type = Counter32
_GnEthStatisticPkts128to255OctetMsb_Object = MibTableColumn
gnEthStatisticPkts128to255OctetMsb = _GnEthStatisticPkts128to255OctetMsb_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 14, 1, 1, 12),
    _GnEthStatisticPkts128to255OctetMsb_Type()
)
gnEthStatisticPkts128to255OctetMsb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnEthStatisticPkts128to255OctetMsb.setStatus("mandatory")
_GnEthStatisticPkts256to511OctetMsb_Type = Counter32
_GnEthStatisticPkts256to511OctetMsb_Object = MibTableColumn
gnEthStatisticPkts256to511OctetMsb = _GnEthStatisticPkts256to511OctetMsb_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 14, 1, 1, 13),
    _GnEthStatisticPkts256to511OctetMsb_Type()
)
gnEthStatisticPkts256to511OctetMsb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnEthStatisticPkts256to511OctetMsb.setStatus("mandatory")
_GnEthStatisticPkts512to1023OctetMsb_Type = Counter32
_GnEthStatisticPkts512to1023OctetMsb_Object = MibTableColumn
gnEthStatisticPkts512to1023OctetMsb = _GnEthStatisticPkts512to1023OctetMsb_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 14, 1, 1, 14),
    _GnEthStatisticPkts512to1023OctetMsb_Type()
)
gnEthStatisticPkts512to1023OctetMsb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnEthStatisticPkts512to1023OctetMsb.setStatus("mandatory")
_GnEthStatisticPkts1024to1518OctetMsb_Type = Counter32
_GnEthStatisticPkts1024to1518OctetMsb_Object = MibTableColumn
gnEthStatisticPkts1024to1518OctetMsb = _GnEthStatisticPkts1024to1518OctetMsb_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 14, 1, 1, 15),
    _GnEthStatisticPkts1024to1518OctetMsb_Type()
)
gnEthStatisticPkts1024to1518OctetMsb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnEthStatisticPkts1024to1518OctetMsb.setStatus("mandatory")
_GnEthStatisticRadioTransmitFramesLsb_Type = Counter32
_GnEthStatisticRadioTransmitFramesLsb_Object = MibTableColumn
gnEthStatisticRadioTransmitFramesLsb = _GnEthStatisticRadioTransmitFramesLsb_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 14, 1, 1, 16),
    _GnEthStatisticRadioTransmitFramesLsb_Type()
)
gnEthStatisticRadioTransmitFramesLsb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnEthStatisticRadioTransmitFramesLsb.setStatus("mandatory")
_GnEthStatisticRadioTransmitFramesMsb_Type = Counter32
_GnEthStatisticRadioTransmitFramesMsb_Object = MibTableColumn
gnEthStatisticRadioTransmitFramesMsb = _GnEthStatisticRadioTransmitFramesMsb_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 14, 1, 1, 17),
    _GnEthStatisticRadioTransmitFramesMsb_Type()
)
gnEthStatisticRadioTransmitFramesMsb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnEthStatisticRadioTransmitFramesMsb.setStatus("mandatory")
_GnEthStatisticDroppedPacketsLsb_Type = Counter32
_GnEthStatisticDroppedPacketsLsb_Object = MibTableColumn
gnEthStatisticDroppedPacketsLsb = _GnEthStatisticDroppedPacketsLsb_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 14, 1, 1, 18),
    _GnEthStatisticDroppedPacketsLsb_Type()
)
gnEthStatisticDroppedPacketsLsb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnEthStatisticDroppedPacketsLsb.setStatus("mandatory")
_GnEthStatisticDroppedPacketsMsb_Type = Counter32
_GnEthStatisticDroppedPacketsMsb_Object = MibTableColumn
gnEthStatisticDroppedPacketsMsb = _GnEthStatisticDroppedPacketsMsb_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 14, 1, 1, 19),
    _GnEthStatisticDroppedPacketsMsb_Type()
)
gnEthStatisticDroppedPacketsMsb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnEthStatisticDroppedPacketsMsb.setStatus("mandatory")
_GnEthStatisticRadioReceivedFramesLsb_Type = Counter32
_GnEthStatisticRadioReceivedFramesLsb_Object = MibTableColumn
gnEthStatisticRadioReceivedFramesLsb = _GnEthStatisticRadioReceivedFramesLsb_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 14, 1, 1, 20),
    _GnEthStatisticRadioReceivedFramesLsb_Type()
)
gnEthStatisticRadioReceivedFramesLsb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnEthStatisticRadioReceivedFramesLsb.setStatus("mandatory")
_GnEthStatisticRadioReceivedFramesMsb_Type = Counter32
_GnEthStatisticRadioReceivedFramesMsb_Object = MibTableColumn
gnEthStatisticRadioReceivedFramesMsb = _GnEthStatisticRadioReceivedFramesMsb_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 14, 1, 1, 21),
    _GnEthStatisticRadioReceivedFramesMsb_Type()
)
gnEthStatisticRadioReceivedFramesMsb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnEthStatisticRadioReceivedFramesMsb.setStatus("mandatory")
_GnEthStatisticRadioReceivedCrcFramesLsb_Type = Counter32
_GnEthStatisticRadioReceivedCrcFramesLsb_Object = MibTableColumn
gnEthStatisticRadioReceivedCrcFramesLsb = _GnEthStatisticRadioReceivedCrcFramesLsb_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 14, 1, 1, 22),
    _GnEthStatisticRadioReceivedCrcFramesLsb_Type()
)
gnEthStatisticRadioReceivedCrcFramesLsb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnEthStatisticRadioReceivedCrcFramesLsb.setStatus("mandatory")
_GnEthStatisticRadioReceivedCrcFramesMsb_Type = Counter32
_GnEthStatisticRadioReceivedCrcFramesMsb_Object = MibTableColumn
gnEthStatisticRadioReceivedCrcFramesMsb = _GnEthStatisticRadioReceivedCrcFramesMsb_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 14, 1, 1, 23),
    _GnEthStatisticRadioReceivedCrcFramesMsb_Type()
)
gnEthStatisticRadioReceivedCrcFramesMsb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnEthStatisticRadioReceivedCrcFramesMsb.setStatus("mandatory")
_GnEthStatisticRadioSyncUnlockEventsLsb_Type = Counter32
_GnEthStatisticRadioSyncUnlockEventsLsb_Object = MibTableColumn
gnEthStatisticRadioSyncUnlockEventsLsb = _GnEthStatisticRadioSyncUnlockEventsLsb_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 14, 1, 1, 24),
    _GnEthStatisticRadioSyncUnlockEventsLsb_Type()
)
gnEthStatisticRadioSyncUnlockEventsLsb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnEthStatisticRadioSyncUnlockEventsLsb.setStatus("mandatory")
_GnEthStatisticRadioSyncUnlockEventsMsb_Type = Counter32
_GnEthStatisticRadioSyncUnlockEventsMsb_Object = MibTableColumn
gnEthStatisticRadioSyncUnlockEventsMsb = _GnEthStatisticRadioSyncUnlockEventsMsb_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 14, 1, 1, 25),
    _GnEthStatisticRadioSyncUnlockEventsMsb_Type()
)
gnEthStatisticRadioSyncUnlockEventsMsb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnEthStatisticRadioSyncUnlockEventsMsb.setStatus("mandatory")
_GnEthStatisticAFrameTransmittedOkLsb_Type = Counter32
_GnEthStatisticAFrameTransmittedOkLsb_Object = MibTableColumn
gnEthStatisticAFrameTransmittedOkLsb = _GnEthStatisticAFrameTransmittedOkLsb_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 14, 1, 1, 26),
    _GnEthStatisticAFrameTransmittedOkLsb_Type()
)
gnEthStatisticAFrameTransmittedOkLsb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnEthStatisticAFrameTransmittedOkLsb.setStatus("mandatory")
_GnEthStatisticAFrameTransmittedOkMsb_Type = Counter32
_GnEthStatisticAFrameTransmittedOkMsb_Object = MibTableColumn
gnEthStatisticAFrameTransmittedOkMsb = _GnEthStatisticAFrameTransmittedOkMsb_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 14, 1, 1, 27),
    _GnEthStatisticAFrameTransmittedOkMsb_Type()
)
gnEthStatisticAFrameTransmittedOkMsb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnEthStatisticAFrameTransmittedOkMsb.setStatus("mandatory")
_GnEthStatisticIfOutOctetsMsb_Type = Counter32
_GnEthStatisticIfOutOctetsMsb_Object = MibTableColumn
gnEthStatisticIfOutOctetsMsb = _GnEthStatisticIfOutOctetsMsb_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 14, 1, 1, 28),
    _GnEthStatisticIfOutOctetsMsb_Type()
)
gnEthStatisticIfOutOctetsMsb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnEthStatisticIfOutOctetsMsb.setStatus("mandatory")
_GnEthStatisticEtherStatsPktsMsb_Type = Counter32
_GnEthStatisticEtherStatsPktsMsb_Object = MibTableColumn
gnEthStatisticEtherStatsPktsMsb = _GnEthStatisticEtherStatsPktsMsb_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 14, 1, 1, 29),
    _GnEthStatisticEtherStatsPktsMsb_Type()
)
gnEthStatisticEtherStatsPktsMsb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnEthStatisticEtherStatsPktsMsb.setStatus("mandatory")
_GnEthStatisticEtherStatsOctetsMsb_Type = Counter32
_GnEthStatisticEtherStatsOctetsMsb_Object = MibTableColumn
gnEthStatisticEtherStatsOctetsMsb = _GnEthStatisticEtherStatsOctetsMsb_Object(
    (1, 3, 6, 1, 4, 1, 2281, 4, 14, 1, 1, 30),
    _GnEthStatisticEtherStatsOctetsMsb_Type()
)
gnEthStatisticEtherStatsOctetsMsb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnEthStatisticEtherStatsOctetsMsb.setStatus("mandatory")
_GnLastDummy_ObjectIdentity = ObjectIdentity
gnLastDummy = _GnLastDummy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2281, 9)
)
_GnLastDummyParam_Type = Integer32
_GnLastDummyParam_Object = MibScalar
gnLastDummyParam = _GnLastDummyParam_Object(
    (1, 3, 6, 1, 4, 1, 2281, 9, 1),
    _GnLastDummyParam_Type()
)
gnLastDummyParam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gnLastDummyParam.setStatus("mandatory")

# Managed Objects groups


# Notification objects

gnODUTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 1)
)
gnODUTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenStatDeviceODUStatus"),
        ("CERAGON-MIB", "gnGenCfgIDUSerialNumber"))
)
if mibBuilder.loadTexts:
    gnODUTrap.setStatus(
        ""
    )

gnIDUTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 2)
)
gnIDUTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenDrawerXDeviceIDUStatus"),
        ("CERAGON-MIB", "gnGenCfgIDUSerialNumber"))
)
if mibBuilder.loadTexts:
    gnIDUTrap.setStatus(
        ""
    )

gnSDHTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 3)
)
gnSDHTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenStatDeviceRSTStatus"),
        ("CERAGON-MIB", "gnGenCfgIDUSerialNumber"))
)
if mibBuilder.loadTexts:
    gnSDHTrap.setStatus(
        ""
    )

gnACCESSTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 4)
)
gnACCESSTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgIDUSerialNumber"))
)
if mibBuilder.loadTexts:
    gnACCESSTrap.setStatus(
        ""
    )

gnODUTrapCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 5)
)
gnODUTrapCleared.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenStatDeviceODUStatus"),
        ("CERAGON-MIB", "gnGenCfgIDUSerialNumber"))
)
if mibBuilder.loadTexts:
    gnODUTrapCleared.setStatus(
        ""
    )

gnIDUTrapCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 6)
)
gnIDUTrapCleared.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenDrawerXDeviceIDUStatus"),
        ("CERAGON-MIB", "gnGenCfgIDUSerialNumber"))
)
if mibBuilder.loadTexts:
    gnIDUTrapCleared.setStatus(
        ""
    )

gnSDHTrapCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 7)
)
gnSDHTrapCleared.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenStatDeviceRSTStatus"),
        ("CERAGON-MIB", "gnGenCfgIDUSerialNumber"))
)
if mibBuilder.loadTexts:
    gnSDHTrapCleared.setStatus(
        ""
    )

gnAccessTrapCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 8)
)
gnAccessTrapCleared.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgIDUSerialNumber"))
)
if mibBuilder.loadTexts:
    gnAccessTrapCleared.setStatus(
        ""
    )

gnLODUPowerFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 10)
)
gnLODUPowerFailTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnOduStatusPowerSupply"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnLODUPowerFailTrap.setStatus(
        ""
    )

gnLODUSynthUnLockTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 11)
)
gnLODUSynthUnLockTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnOduStatusSynthesizerVCOLock"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnLODUSynthUnLockTrap.setStatus(
        ""
    )

gnLODUTxLevelOutOfRangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 12)
)
gnLODUTxLevelOutOfRangeTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnOduStatusTransmitLevel"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnLODUTxLevelOutOfRangeTrap.setStatus(
        ""
    )

gnLODURxLevelOutOfRangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 13)
)
gnLODURxLevelOutOfRangeTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnOduStatusReceiveLevel"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnLODURxLevelOutOfRangeTrap.setStatus(
        ""
    )

gnLODUExtremeTempTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 14)
)
gnLODUExtremeTempTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnOduStatusFahrenheitTemp"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnLODUExtremeTempTrap.setStatus(
        ""
    )

gnLIDUPowerFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 15)
)
gnLIDUPowerFailTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenStatDevicePowerSupply"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnLIDUPowerFailTrap.setStatus(
        ""
    )

gnLCableFaultTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 16)
)
gnLCableFaultTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenStatDeviceCable"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnLCableFaultTrap.setStatus(
        ""
    )

gnLModemFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 17)
)
gnLModemFailTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnLModemFailTrap.setStatus(
        ""
    )

gnLIDUExtremeTempTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 18)
)
gnLIDUExtremeTempTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenStatDeviceFahrenheitTemp"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnLIDUExtremeTempTrap.setStatus(
        ""
    )

gnLLoopbackOnTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 19)
)
gnLLoopbackOnTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnLLoopbackOnTrap.setStatus(
        ""
    )

gnLRemoteCommFaultTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 20)
)
gnLRemoteCommFaultTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnLRemoteCommFaultTrap.setStatus(
        ""
    )

gnLTestRunningTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 21)
)
gnLTestRunningTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnRstCfgTestActivate"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnLTestRunningTrap.setStatus(
        ""
    )

gnLLOFTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 22)
)
gnLLOFTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnLLOFTrap.setStatus(
        ""
    )

gnLLOSTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 23)
)
gnLLOSTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnLLOSTrap.setStatus(
        ""
    )

gnLTIMTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 24)
)
gnLTIMTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnLTIMTrap.setStatus(
        ""
    )

gnLEXCTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 25)
)
gnLEXCTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnRstStatBERCur"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnLEXCTrap.setStatus(
        ""
    )

gnLSDTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 26)
)
gnLSDTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnRstStatBERCur"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnLSDTrap.setStatus(
        ""
    )

gnLRcvAisTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 27)
)
gnLRcvAisTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnLRcvAisTrap.setStatus(
        ""
    )

gnLUnExpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 28)
)
gnLUnExpTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnLUnExpTrap.setStatus(
        ""
    )

gnLLocTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 29)
)
gnLLocTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnLLocTrap.setStatus(
        ""
    )

gnLLopTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 30)
)
gnLLopTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnLLopTrap.setStatus(
        ""
    )

gnLRdiTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 31)
)
gnLRdiTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnLRdiTrap.setStatus(
        ""
    )

gnLSlmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 32)
)
gnLSlmTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnLSlmTrap.setStatus(
        ""
    )

gnLUnqTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 33)
)
gnLUnqTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnLUnqTrap.setStatus(
        ""
    )

gnLExternalAlarm1OnTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 34)
)
gnLExternalAlarm1OnTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenStatDeviceDryContact"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnLExternalAlarm1OnTrap.setStatus(
        ""
    )

gnLExternalAlarm2OnTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 35)
)
gnLExternalAlarm2OnTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenStatDeviceDryContact"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnLExternalAlarm2OnTrap.setStatus(
        ""
    )

gnLExternalAlarm3OnTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 36)
)
gnLExternalAlarm3OnTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenStatDeviceDryContact"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnLExternalAlarm3OnTrap.setStatus(
        ""
    )

gnLExternalAlarm4OnTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 37)
)
gnLExternalAlarm4OnTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenStatDeviceDryContact"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnLExternalAlarm4OnTrap.setStatus(
        ""
    )

gnLExternalAlarm5OnTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 38)
)
gnLExternalAlarm5OnTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenStatDeviceDryContact"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnLExternalAlarm5OnTrap.setStatus(
        ""
    )

gnLExternalAlarm6OnTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 39)
)
gnLExternalAlarm6OnTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenStatDeviceDryContact"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnLExternalAlarm6OnTrap.setStatus(
        ""
    )

gnLExternalAlarm7OnTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 40)
)
gnLExternalAlarm7OnTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenStatDeviceDryContact"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnLExternalAlarm7OnTrap.setStatus(
        ""
    )

gnLExternalAlarm8OnTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 41)
)
gnLExternalAlarm8OnTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenStatDeviceDryContact"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnLExternalAlarm8OnTrap.setStatus(
        ""
    )

gnLSystemFaultTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 42)
)
gnLSystemFaultTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenDrawerXInternalCommunication"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnLSystemFaultTrap.setStatus(
        ""
    )

gnLTftpFaultTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 43)
)
gnLTftpFaultTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnLTftpFaultTrap.setStatus(
        ""
    )

gnLInternalDownloadFaultTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 44)
)
gnLInternalDownloadFaultTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnLInternalDownloadFaultTrap.setStatus(
        ""
    )

gnLIntralinkFaultTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 45)
)
gnLIntralinkFaultTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnLIntralinkFaultTrap.setStatus(
        ""
    )

gnLConfMismatchTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 46)
)
gnLConfMismatchTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnLConfMismatchTrap.setStatus(
        ""
    )

gnLProtectSwitchFaultTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 47)
)
gnLProtectSwitchFaultTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnLProtectSwitchFaultTrap.setStatus(
        ""
    )

gnLProtectCableFaultTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 48)
)
gnLProtectCableFaultTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnLProtectCableFaultTrap.setStatus(
        ""
    )

gnLHeartBeatTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 49)
)
gnLHeartBeatTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnLHeartBeatTrap.setStatus(
        ""
    )

gnLLomTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 50)
)
gnLLomTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnLLomTrap.setStatus(
        ""
    )

gnLHitlessProblemTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 51)
)
gnLHitlessProblemTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnLHitlessProblemTrap.setStatus(
        ""
    )

gnLHitlessRadioLofTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 52)
)
gnLHitlessRadioLofTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnLHitlessRadioLofTrap.setStatus(
        ""
    )

gnLHitlessCableDisconnectTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 53)
)
gnLHitlessCableDisconnectTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnLHitlessCableDisconnectTrap.setStatus(
        ""
    )

gnLPamTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 54)
)
gnLPamTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnLPamTrap.setStatus(
        ""
    )

gnLScmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 55)
)
gnLScmTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnLScmTrap.setStatus(
        ""
    )

gnLInvTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 56)
)
gnLInvTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnLInvTrap.setStatus(
        ""
    )

gnLInbandTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 57)
)
gnLInbandTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnLInbandTrap.setStatus(
        ""
    )

gnWSLOSTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 58)
)
gnWSLOSTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnWSLOSTrap.setStatus(
        ""
    )

gnODUtoODUCableFaultTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 59)
)
gnODUtoODUCableFaultTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnODUtoODUCableFaultTrap.setStatus(
        ""
    )

gnNoSignalReceivedFromODUTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 60)
)
gnNoSignalReceivedFromODUTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnNoSignalReceivedFromODUTrap.setStatus(
        ""
    )

gnProtectionLockoutConfiguredTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 61)
)
gnProtectionLockoutConfiguredTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnProtectionLockoutConfiguredTrap.setStatus(
        ""
    )

gnRFUPowerFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 62)
)
gnRFUPowerFailureTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnRFUPowerFailureTrap.setStatus(
        ""
    )

gnRFURxLevelPathOutOfRangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 63)
)
gnRFURxLevelPathOutOfRangeTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnRFURxLevelPathOutOfRangeTrap.setStatus(
        ""
    )

gnRFUExtremeTemperatureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 64)
)
gnRFUExtremeTemperatureTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnRFUExtremeTemperatureTrap.setStatus(
        ""
    )

gnRFUFanFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 65)
)
gnRFUFanFailureTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnRFUFanFailureTrap.setStatus(
        ""
    )

gnLowSignalToRFUTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 66)
)
gnLowSignalToRFUTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnLowSignalToRFUTrap.setStatus(
        ""
    )

gnRFUXPICClockFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 67)
)
gnRFUXPICClockFailureTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnRFUXPICClockFailureTrap.setStatus(
        ""
    )

gnRFUDelayCalibrationFailure1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 68)
)
gnRFUDelayCalibrationFailure1Trap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnRFUDelayCalibrationFailure1Trap.setStatus(
        ""
    )

gnRFUDelayCalibrationFailure2Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 69)
)
gnRFUDelayCalibrationFailure2Trap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnRFUDelayCalibrationFailure2Trap.setStatus(
        ""
    )

gnLSFPFaultTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 70)
)
gnLSFPFaultTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnLSFPFaultTrap.setStatus(
        ""
    )

gnEncryptionFaultTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 71)
)
gnEncryptionFaultTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnEncryptionFaultTrap.setStatus(
        ""
    )

gnEncryptionSyncLosTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 72)
)
gnEncryptionSyncLosTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnEncryptionSyncLosTrap.setStatus(
        ""
    )

gnEncryptionKepTimout = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 73)
)
gnEncryptionKepTimout.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnEncryptionKepTimout.setStatus(
        ""
    )

gnEncryptionSkTimerElapsed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 74)
)
gnEncryptionSkTimerElapsed.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnEncryptionSkTimerElapsed.setStatus(
        ""
    )

gnEncryptionPowerUpSelfTestFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 75)
)
gnEncryptionPowerUpSelfTestFail.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnEncryptionPowerUpSelfTestFail.setStatus(
        ""
    )

gnEncryptionConditionalTestFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 76)
)
gnEncryptionConditionalTestFail.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnEncryptionConditionalTestFail.setStatus(
        ""
    )

gnEncryptionWillTurnOffOnNextRest = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 77)
)
gnEncryptionWillTurnOffOnNextRest.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnEncryptionWillTurnOffOnNextRest.setStatus(
        ""
    )

gnEncryptionEventReport = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 78)
)
gnEncryptionEventReport.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnEncryptionEventReport.setStatus(
        ""
    )

gnEncryptionTechCardWasDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 79)
)
gnEncryptionTechCardWasDetected.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnEncryptionTechCardWasDetected.setStatus(
        ""
    )

gnAdminPasswordInDefaultState = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 80)
)
gnAdminPasswordInDefaultState.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnAdminPasswordInDefaultState.setStatus(
        ""
    )

gnLinkGroupingProtectionFaultTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 81)
)
gnLinkGroupingProtectionFaultTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnLinkGroupingProtectionFaultTrap.setStatus(
        ""
    )

gnLossOfProtectionTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 82)
)
gnLossOfProtectionTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnLossOfProtectionTrap.setStatus(
        ""
    )

gnTempLicenseTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 83)
)
gnTempLicenseTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnTempLicenseTrap.setStatus(
        ""
    )

gnMultiRadioProblemTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 84)
)
gnMultiRadioProblemTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnMultiRadioProblemTrap.setStatus(
        ""
    )

gnLODUPowerOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 110)
)
gnLODUPowerOkTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnOduStatusPowerSupply"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnLODUPowerOkTrap.setStatus(
        ""
    )

gnLODUSynthLockTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 111)
)
gnLODUSynthLockTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnOduStatusSynthesizerVCOLock"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnLODUSynthLockTrap.setStatus(
        ""
    )

gnLODUTxLevelInRangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 112)
)
gnLODUTxLevelInRangeTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnOduStatusTransmitLevel"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnLODUTxLevelInRangeTrap.setStatus(
        ""
    )

gnLODURxLevelInRangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 113)
)
gnLODURxLevelInRangeTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnOduStatusReceiveLevel"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnLODURxLevelInRangeTrap.setStatus(
        ""
    )

gnLODUNormalTempTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 114)
)
gnLODUNormalTempTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnOduStatusFahrenheitTemp"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnLODUNormalTempTrap.setStatus(
        ""
    )

gnLIDUPowerOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 115)
)
gnLIDUPowerOkTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenStatDevicePowerSupply"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnLIDUPowerOkTrap.setStatus(
        ""
    )

gnLCableOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 116)
)
gnLCableOkTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenStatDeviceCable"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnLCableOkTrap.setStatus(
        ""
    )

gnLModemOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 117)
)
gnLModemOkTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnLModemOkTrap.setStatus(
        ""
    )

gnLIDUNormalTempTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 118)
)
gnLIDUNormalTempTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenStatDeviceFahrenheitTemp"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnLIDUNormalTempTrap.setStatus(
        ""
    )

gnLLoopbackOffTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 119)
)
gnLLoopbackOffTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnLLoopbackOffTrap.setStatus(
        ""
    )

gnLRemoteCommOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 120)
)
gnLRemoteCommOkTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnLRemoteCommOkTrap.setStatus(
        ""
    )

gnLNoTestRunningTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 121)
)
gnLNoTestRunningTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnRstCfgTestActivate"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnLNoTestRunningTrap.setStatus(
        ""
    )

gnLNoLOFTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 122)
)
gnLNoLOFTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnLNoLOFTrap.setStatus(
        ""
    )

gnLNoLOSTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 123)
)
gnLNoLOSTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnLNoLOSTrap.setStatus(
        ""
    )

gnLNoTIMTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 124)
)
gnLNoTIMTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnLNoTIMTrap.setStatus(
        ""
    )

gnLNoEXCTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 125)
)
gnLNoEXCTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnRstStatBERCur"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnLNoEXCTrap.setStatus(
        ""
    )

gnLNoSDTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 126)
)
gnLNoSDTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnRstStatBERCur"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnLNoSDTrap.setStatus(
        ""
    )

gnLNoAisTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 127)
)
gnLNoAisTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnLNoAisTrap.setStatus(
        ""
    )

gnLNoUnExpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 128)
)
gnLNoUnExpTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnLNoUnExpTrap.setStatus(
        ""
    )

gnLNoLocTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 129)
)
gnLNoLocTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnLNoLocTrap.setStatus(
        ""
    )

gnLNoLopTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 130)
)
gnLNoLopTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnLNoLopTrap.setStatus(
        ""
    )

gnLNoRdiTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 131)
)
gnLNoRdiTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnLNoRdiTrap.setStatus(
        ""
    )

gnLNoSlmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 132)
)
gnLNoSlmTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnLNoSlmTrap.setStatus(
        ""
    )

gnLNoUnqTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 133)
)
gnLNoUnqTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnLNoUnqTrap.setStatus(
        ""
    )

gnLExternalAlarm1OffTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 134)
)
gnLExternalAlarm1OffTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenStatDeviceDryContact"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnLExternalAlarm1OffTrap.setStatus(
        ""
    )

gnLExternalAlarm2OffTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 135)
)
gnLExternalAlarm2OffTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenStatDeviceDryContact"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnLExternalAlarm2OffTrap.setStatus(
        ""
    )

gnLExternalAlarm3OffTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 136)
)
gnLExternalAlarm3OffTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenStatDeviceDryContact"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnLExternalAlarm3OffTrap.setStatus(
        ""
    )

gnLExternalAlarm4OffTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 137)
)
gnLExternalAlarm4OffTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenStatDeviceDryContact"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnLExternalAlarm4OffTrap.setStatus(
        ""
    )

gnLExternalAlarm5OffTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 138)
)
gnLExternalAlarm5OffTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenStatDeviceDryContact"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnLExternalAlarm5OffTrap.setStatus(
        ""
    )

gnLExternalAlarm6OffTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 139)
)
gnLExternalAlarm6OffTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenStatDeviceDryContact"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnLExternalAlarm6OffTrap.setStatus(
        ""
    )

gnLExternalAlarm7OffTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 140)
)
gnLExternalAlarm7OffTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenStatDeviceDryContact"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnLExternalAlarm7OffTrap.setStatus(
        ""
    )

gnLExternalAlarm8OffTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 141)
)
gnLExternalAlarm8OffTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenStatDeviceDryContact"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnLExternalAlarm8OffTrap.setStatus(
        ""
    )

gnLSystemOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 142)
)
gnLSystemOkTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenDrawerXInternalCommunication"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnLSystemOkTrap.setStatus(
        ""
    )

gnLTftpOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 143)
)
gnLTftpOkTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnLTftpOkTrap.setStatus(
        ""
    )

gnLInternalDownloadOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 144)
)
gnLInternalDownloadOkTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnLInternalDownloadOkTrap.setStatus(
        ""
    )

gnLIntralinkOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 145)
)
gnLIntralinkOkTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnLIntralinkOkTrap.setStatus(
        ""
    )

gnLNoConfMismatchTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 146)
)
gnLNoConfMismatchTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnLNoConfMismatchTrap.setStatus(
        ""
    )

gnLProtectSwitchOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 147)
)
gnLProtectSwitchOkTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnLProtectSwitchOkTrap.setStatus(
        ""
    )

gnLProtectCableOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 148)
)
gnLProtectCableOkTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnLProtectCableOkTrap.setStatus(
        ""
    )

gnLLomOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 150)
)
gnLLomOkTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnLLomOkTrap.setStatus(
        ""
    )

gnLHitlessProblemOKTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 151)
)
gnLHitlessProblemOKTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnLHitlessProblemOKTrap.setStatus(
        ""
    )

gnLHitlessRadioLofOKTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 152)
)
gnLHitlessRadioLofOKTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnLHitlessRadioLofOKTrap.setStatus(
        ""
    )

gnLHitlessCableDisconnectOKTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 153)
)
gnLHitlessCableDisconnectOKTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnLHitlessCableDisconnectOKTrap.setStatus(
        ""
    )

gnLPamOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 154)
)
gnLPamOkTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnLPamOkTrap.setStatus(
        ""
    )

gnLScmOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 155)
)
gnLScmOkTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnLScmOkTrap.setStatus(
        ""
    )

gnLInvOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 156)
)
gnLInvOkTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnLInvOkTrap.setStatus(
        ""
    )

gnLInbandOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 157)
)
gnLInbandOkTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnLInbandOkTrap.setStatus(
        ""
    )

gnWSNoLOSTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 158)
)
gnWSNoLOSTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnWSNoLOSTrap.setStatus(
        ""
    )

gnODUtoODUCableOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 159)
)
gnODUtoODUCableOkTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnODUtoODUCableOkTrap.setStatus(
        ""
    )

gnSignalReceivedFromODUTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 160)
)
gnSignalReceivedFromODUTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnSignalReceivedFromODUTrap.setStatus(
        ""
    )

gnProtectionLockoutClearededTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 161)
)
gnProtectionLockoutClearededTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnProtectionLockoutClearededTrap.setStatus(
        ""
    )

gnRFUPowerFailureClearedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 162)
)
gnRFUPowerFailureClearedTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnRFUPowerFailureClearedTrap.setStatus(
        ""
    )

gnRFURxLevelPathOutOfRangeClearedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 163)
)
gnRFURxLevelPathOutOfRangeClearedTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnRFURxLevelPathOutOfRangeClearedTrap.setStatus(
        ""
    )

gnRFUExtremeTemperatureClearedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 164)
)
gnRFUExtremeTemperatureClearedTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnRFUExtremeTemperatureClearedTrap.setStatus(
        ""
    )

gnRFUFanFailureClearedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 165)
)
gnRFUFanFailureClearedTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnRFUFanFailureClearedTrap.setStatus(
        ""
    )

gnLowSignalToRFUClearedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 166)
)
gnLowSignalToRFUClearedTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnLowSignalToRFUClearedTrap.setStatus(
        ""
    )

gnRFUXPICClockFailureClearedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 167)
)
gnRFUXPICClockFailureClearedTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnRFUXPICClockFailureClearedTrap.setStatus(
        ""
    )

gnRFUDelayCalibrationFailure1ClearedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 168)
)
gnRFUDelayCalibrationFailure1ClearedTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnRFUDelayCalibrationFailure1ClearedTrap.setStatus(
        ""
    )

gnRFUDelayCalibrationFailure2ClearedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 169)
)
gnRFUDelayCalibrationFailure2ClearedTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnRFUDelayCalibrationFailure2ClearedTrap.setStatus(
        ""
    )

gnLSFPOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 170)
)
gnLSFPOkTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnLSFPOkTrap.setStatus(
        ""
    )

gnEncryptionFaultClearedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 171)
)
gnEncryptionFaultClearedTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnEncryptionFaultClearedTrap.setStatus(
        ""
    )

gnEncryptionSyncLosClearedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 172)
)
gnEncryptionSyncLosClearedTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnEncryptionSyncLosClearedTrap.setStatus(
        ""
    )

gnEncryptionKepTimoutCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 173)
)
gnEncryptionKepTimoutCleared.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnEncryptionKepTimoutCleared.setStatus(
        ""
    )

gnEncryptionSkTimerElapsedCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 174)
)
gnEncryptionSkTimerElapsedCleared.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnEncryptionSkTimerElapsedCleared.setStatus(
        ""
    )

gnEncryptionPowerUpSelfTestFailCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 175)
)
gnEncryptionPowerUpSelfTestFailCleared.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnEncryptionPowerUpSelfTestFailCleared.setStatus(
        ""
    )

gnEncryptionConditionalTestFailCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 176)
)
gnEncryptionConditionalTestFailCleared.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnEncryptionConditionalTestFailCleared.setStatus(
        ""
    )

gnEncryptionWillTurnOffOnNextRestCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 177)
)
gnEncryptionWillTurnOffOnNextRestCleared.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnEncryptionWillTurnOffOnNextRestCleared.setStatus(
        ""
    )

gnEncryptionEventReportCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 178)
)
gnEncryptionEventReportCleared.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnEncryptionEventReportCleared.setStatus(
        ""
    )

gnEncryptionTechCardWasDetectedCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 179)
)
gnEncryptionTechCardWasDetectedCleared.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnEncryptionTechCardWasDetectedCleared.setStatus(
        ""
    )

gnAdminPasswordInDefaultStateCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 180)
)
gnAdminPasswordInDefaultStateCleared.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnAdminPasswordInDefaultStateCleared.setStatus(
        ""
    )

gnLinkGroupingProtectionFaultClearedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 181)
)
gnLinkGroupingProtectionFaultClearedTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnLinkGroupingProtectionFaultClearedTrap.setStatus(
        ""
    )

gnLossOfProtectionClearedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 182)
)
gnLossOfProtectionClearedTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnLossOfProtectionClearedTrap.setStatus(
        ""
    )

gnTempLicenseClearedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 183)
)
gnTempLicenseClearedTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnTempLicenseClearedTrap.setStatus(
        ""
    )

gnMultiRadioProblemOKTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 184)
)
gnMultiRadioProblemOKTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnMultiRadioProblemOKTrap.setStatus(
        ""
    )

gnRODUPowerFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 210)
)
gnRODUPowerFailTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnOduStatusPowerSupply"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnRODUPowerFailTrap.setStatus(
        ""
    )

gnRODUSynthUnLockTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 211)
)
gnRODUSynthUnLockTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnOduStatusSynthesizerVCOLock"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnRODUSynthUnLockTrap.setStatus(
        ""
    )

gnRODUTxLevelOutOfRangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 212)
)
gnRODUTxLevelOutOfRangeTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnOduStatusTransmitLevel"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnRODUTxLevelOutOfRangeTrap.setStatus(
        ""
    )

gnRODURxLevelOutOfRangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 213)
)
gnRODURxLevelOutOfRangeTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnOduStatusReceiveLevel"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnRODURxLevelOutOfRangeTrap.setStatus(
        ""
    )

gnRODUExtremeTempTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 214)
)
gnRODUExtremeTempTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnOduStatusFahrenheitTemp"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnRODUExtremeTempTrap.setStatus(
        ""
    )

gnRIDUPowerFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 215)
)
gnRIDUPowerFailTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenStatDevicePowerSupply"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnRIDUPowerFailTrap.setStatus(
        ""
    )

gnRCableFaultTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 216)
)
gnRCableFaultTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenStatDeviceCable"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnRCableFaultTrap.setStatus(
        ""
    )

gnRModemFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 217)
)
gnRModemFailTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnRModemFailTrap.setStatus(
        ""
    )

gnRIDUExtremeTempTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 218)
)
gnRIDUExtremeTempTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenStatDeviceFahrenheitTemp"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnRIDUExtremeTempTrap.setStatus(
        ""
    )

gnRLoopbackOnTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 219)
)
gnRLoopbackOnTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnRLoopbackOnTrap.setStatus(
        ""
    )

gnRRemoteCommFaultTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 220)
)
gnRRemoteCommFaultTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnRRemoteCommFaultTrap.setStatus(
        ""
    )

gnRTestRunningTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 221)
)
gnRTestRunningTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnRstCfgTestActivate"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnRTestRunningTrap.setStatus(
        ""
    )

gnRLOFTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 222)
)
gnRLOFTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnRLOFTrap.setStatus(
        ""
    )

gnRLOSTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 223)
)
gnRLOSTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnRLOSTrap.setStatus(
        ""
    )

gnRTIMTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 224)
)
gnRTIMTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnRTIMTrap.setStatus(
        ""
    )

gnREXCTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 225)
)
gnREXCTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnRstStatBERCur"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnREXCTrap.setStatus(
        ""
    )

gnRSDTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 226)
)
gnRSDTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnRstStatBERCur"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnRSDTrap.setStatus(
        ""
    )

gnRAisTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 227)
)
gnRAisTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnRAisTrap.setStatus(
        ""
    )

gnRUnExpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 228)
)
gnRUnExpTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnRUnExpTrap.setStatus(
        ""
    )

gnRLocTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 229)
)
gnRLocTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnRLocTrap.setStatus(
        ""
    )

gnRLopTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 230)
)
gnRLopTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnRLopTrap.setStatus(
        ""
    )

gnRRdiTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 231)
)
gnRRdiTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnRRdiTrap.setStatus(
        ""
    )

gnRSlmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 232)
)
gnRSlmTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnRSlmTrap.setStatus(
        ""
    )

gnRUnqTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 233)
)
gnRUnqTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnRUnqTrap.setStatus(
        ""
    )

gnRExternalAlarm1OnTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 234)
)
gnRExternalAlarm1OnTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenStatDeviceDryContact"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnRExternalAlarm1OnTrap.setStatus(
        ""
    )

gnRExternalAlarm2OnTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 235)
)
gnRExternalAlarm2OnTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenStatDeviceDryContact"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnRExternalAlarm2OnTrap.setStatus(
        ""
    )

gnRExternalAlarm3OnTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 236)
)
gnRExternalAlarm3OnTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenStatDeviceDryContact"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnRExternalAlarm3OnTrap.setStatus(
        ""
    )

gnRExternalAlarm4OnTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 237)
)
gnRExternalAlarm4OnTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenStatDeviceDryContact"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnRExternalAlarm4OnTrap.setStatus(
        ""
    )

gnRExternalAlarm5OnTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 238)
)
gnRExternalAlarm5OnTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenStatDeviceDryContact"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnRExternalAlarm5OnTrap.setStatus(
        ""
    )

gnRExternalAlarm6OnTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 239)
)
gnRExternalAlarm6OnTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenStatDeviceDryContact"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnRExternalAlarm6OnTrap.setStatus(
        ""
    )

gnRExternalAlarm7OnTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 240)
)
gnRExternalAlarm7OnTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenStatDeviceDryContact"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnRExternalAlarm7OnTrap.setStatus(
        ""
    )

gnRExternalAlarm8OnTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 241)
)
gnRExternalAlarm8OnTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenStatDeviceDryContact"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnRExternalAlarm8OnTrap.setStatus(
        ""
    )

gnRSystemFaultTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 242)
)
gnRSystemFaultTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenStatInternalCommunication"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnRSystemFaultTrap.setStatus(
        ""
    )

gnRTftpFaultTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 243)
)
gnRTftpFaultTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnRTftpFaultTrap.setStatus(
        ""
    )

gnRInternalDownloadFaultTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 244)
)
gnRInternalDownloadFaultTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnRInternalDownloadFaultTrap.setStatus(
        ""
    )

gnRIntralinkFaultTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 245)
)
gnRIntralinkFaultTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnRIntralinkFaultTrap.setStatus(
        ""
    )

gnRConfMismatchTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 246)
)
gnRConfMismatchTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnRConfMismatchTrap.setStatus(
        ""
    )

gnRProtectSwitchFaultTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 247)
)
gnRProtectSwitchFaultTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnRProtectSwitchFaultTrap.setStatus(
        ""
    )

gnRProtectCableFaultTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 248)
)
gnRProtectCableFaultTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnRProtectCableFaultTrap.setStatus(
        ""
    )

gnRHeartBeatTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 249)
)
gnRHeartBeatTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnRHeartBeatTrap.setStatus(
        ""
    )

gnRLomTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 250)
)
gnRLomTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnRLomTrap.setStatus(
        ""
    )

gnRHitlessRadioLofTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 252)
)
gnRHitlessRadioLofTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnRHitlessRadioLofTrap.setStatus(
        ""
    )

gnRHitlessCableDisconnectTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 253)
)
gnRHitlessCableDisconnectTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnRHitlessCableDisconnectTrap.setStatus(
        ""
    )

gnRODUPowerOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 310)
)
gnRODUPowerOkTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnOduStatusPowerSupply"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnRODUPowerOkTrap.setStatus(
        ""
    )

gnRODUSynthLockTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 311)
)
gnRODUSynthLockTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnOduStatusSynthesizerVCOLock"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnRODUSynthLockTrap.setStatus(
        ""
    )

gnRODUTxLevelInRangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 312)
)
gnRODUTxLevelInRangeTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnOduStatusTransmitLevel"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnRODUTxLevelInRangeTrap.setStatus(
        ""
    )

gnRODURxLevelInRangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 313)
)
gnRODURxLevelInRangeTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnOduStatusReceiveLevel"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnRODURxLevelInRangeTrap.setStatus(
        ""
    )

gnRODUNormalTempTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 314)
)
gnRODUNormalTempTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnOduStatusFahrenheitTemp"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnRODUNormalTempTrap.setStatus(
        ""
    )

gnRIDUPowerOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 315)
)
gnRIDUPowerOkTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenStatDevicePowerSupply"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnRIDUPowerOkTrap.setStatus(
        ""
    )

gnRCableOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 316)
)
gnRCableOkTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenStatDeviceCable"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnRCableOkTrap.setStatus(
        ""
    )

gnRModemOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 317)
)
gnRModemOkTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnRModemOkTrap.setStatus(
        ""
    )

gnRIDUNormalTempTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 318)
)
gnRIDUNormalTempTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenStatDeviceFahrenheitTemp"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnRIDUNormalTempTrap.setStatus(
        ""
    )

gnRLoopbackOffTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 319)
)
gnRLoopbackOffTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnRLoopbackOffTrap.setStatus(
        ""
    )

gnRRemoteCommOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 320)
)
gnRRemoteCommOkTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnRRemoteCommOkTrap.setStatus(
        ""
    )

gnRNoTestRunningTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 321)
)
gnRNoTestRunningTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnRstCfgTestActivate"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnRNoTestRunningTrap.setStatus(
        ""
    )

gnRNoLOFTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 322)
)
gnRNoLOFTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnRNoLOFTrap.setStatus(
        ""
    )

gnRNoLOSTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 323)
)
gnRNoLOSTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnRNoLOSTrap.setStatus(
        ""
    )

gnRNoTIMTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 324)
)
gnRNoTIMTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnRNoTIMTrap.setStatus(
        ""
    )

gnRNoEXCTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 325)
)
gnRNoEXCTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnRstStatBERCur"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnRNoEXCTrap.setStatus(
        ""
    )

gnRNoSDTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 326)
)
gnRNoSDTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnRstStatBERCur"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnRNoSDTrap.setStatus(
        ""
    )

gnRNoAisTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 327)
)
gnRNoAisTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnRNoAisTrap.setStatus(
        ""
    )

gnRNoUnExpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 328)
)
gnRNoUnExpTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnRNoUnExpTrap.setStatus(
        ""
    )

gnRNoLocTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 329)
)
gnRNoLocTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnRNoLocTrap.setStatus(
        ""
    )

gnRNoLopTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 330)
)
gnRNoLopTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnRNoLopTrap.setStatus(
        ""
    )

gnRNoRdiTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 331)
)
gnRNoRdiTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnRNoRdiTrap.setStatus(
        ""
    )

gnRNoSlmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 332)
)
gnRNoSlmTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnRNoSlmTrap.setStatus(
        ""
    )

gnRNoUnqTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 333)
)
gnRNoUnqTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnRNoUnqTrap.setStatus(
        ""
    )

gnRExternalAlarm1OffTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 334)
)
gnRExternalAlarm1OffTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenStatDeviceDryContact"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnRExternalAlarm1OffTrap.setStatus(
        ""
    )

gnRExternalAlarm2OffTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 335)
)
gnRExternalAlarm2OffTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenStatDeviceDryContact"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnRExternalAlarm2OffTrap.setStatus(
        ""
    )

gnRExternalAlarm3OffTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 336)
)
gnRExternalAlarm3OffTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenStatDeviceDryContact"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnRExternalAlarm3OffTrap.setStatus(
        ""
    )

gnRExternalAlarm4OffTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 337)
)
gnRExternalAlarm4OffTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenStatDeviceDryContact"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnRExternalAlarm4OffTrap.setStatus(
        ""
    )

gnRExternalAlarm5OffTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 338)
)
gnRExternalAlarm5OffTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenStatDeviceDryContact"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnRExternalAlarm5OffTrap.setStatus(
        ""
    )

gnRExternalAlarm6OffTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 339)
)
gnRExternalAlarm6OffTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenStatDeviceDryContact"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnRExternalAlarm6OffTrap.setStatus(
        ""
    )

gnRExternalAlarm7OffTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 340)
)
gnRExternalAlarm7OffTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenStatDeviceDryContact"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnRExternalAlarm7OffTrap.setStatus(
        ""
    )

gnRExternalAlarm8OffTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 341)
)
gnRExternalAlarm8OffTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenStatDeviceDryContact"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnRExternalAlarm8OffTrap.setStatus(
        ""
    )

gnRSystemOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 342)
)
gnRSystemOkTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenStatInternalCommunication"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnRSystemOkTrap.setStatus(
        ""
    )

gnRTftpOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 343)
)
gnRTftpOkTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnRTftpOkTrap.setStatus(
        ""
    )

gnRInternalDownloadOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 344)
)
gnRInternalDownloadOkTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnRInternalDownloadOkTrap.setStatus(
        ""
    )

gnRIntralinkOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 345)
)
gnRIntralinkOkTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnRIntralinkOkTrap.setStatus(
        ""
    )

gnRNoConfMismatchTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 346)
)
gnRNoConfMismatchTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnRNoConfMismatchTrap.setStatus(
        ""
    )

gnRProtectCableOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 348)
)
gnRProtectCableOkTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnRProtectCableOkTrap.setStatus(
        ""
    )

gnRLomOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 350)
)
gnRLomOkTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnRLomOkTrap.setStatus(
        ""
    )

gnRHitlessRadioLofOKTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 352)
)
gnRHitlessRadioLofOKTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnRHitlessRadioLofOKTrap.setStatus(
        ""
    )

gnRHitlessCableDisconnectOKTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2281, 0, 353)
)
gnRHitlessCableDisconnectOKTrap.setObjects(
      *(("CERAGON-MIB", "gnGenCfgTrapSeverity"),
        ("CERAGON-MIB", "gnGenCfgAlarmText"),
        ("CERAGON-MIB", "gnGenCfgCLLI"))
)
if mibBuilder.loadTexts:
    gnRHitlessCableDisconnectOKTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CERAGON-MIB",
    **{"ceragon": ceragon,
       "gnODUTrap": gnODUTrap,
       "gnIDUTrap": gnIDUTrap,
       "gnSDHTrap": gnSDHTrap,
       "gnACCESSTrap": gnACCESSTrap,
       "gnODUTrapCleared": gnODUTrapCleared,
       "gnIDUTrapCleared": gnIDUTrapCleared,
       "gnSDHTrapCleared": gnSDHTrapCleared,
       "gnAccessTrapCleared": gnAccessTrapCleared,
       "gnLODUPowerFailTrap": gnLODUPowerFailTrap,
       "gnLODUSynthUnLockTrap": gnLODUSynthUnLockTrap,
       "gnLODUTxLevelOutOfRangeTrap": gnLODUTxLevelOutOfRangeTrap,
       "gnLODURxLevelOutOfRangeTrap": gnLODURxLevelOutOfRangeTrap,
       "gnLODUExtremeTempTrap": gnLODUExtremeTempTrap,
       "gnLIDUPowerFailTrap": gnLIDUPowerFailTrap,
       "gnLCableFaultTrap": gnLCableFaultTrap,
       "gnLModemFailTrap": gnLModemFailTrap,
       "gnLIDUExtremeTempTrap": gnLIDUExtremeTempTrap,
       "gnLLoopbackOnTrap": gnLLoopbackOnTrap,
       "gnLRemoteCommFaultTrap": gnLRemoteCommFaultTrap,
       "gnLTestRunningTrap": gnLTestRunningTrap,
       "gnLLOFTrap": gnLLOFTrap,
       "gnLLOSTrap": gnLLOSTrap,
       "gnLTIMTrap": gnLTIMTrap,
       "gnLEXCTrap": gnLEXCTrap,
       "gnLSDTrap": gnLSDTrap,
       "gnLRcvAisTrap": gnLRcvAisTrap,
       "gnLUnExpTrap": gnLUnExpTrap,
       "gnLLocTrap": gnLLocTrap,
       "gnLLopTrap": gnLLopTrap,
       "gnLRdiTrap": gnLRdiTrap,
       "gnLSlmTrap": gnLSlmTrap,
       "gnLUnqTrap": gnLUnqTrap,
       "gnLExternalAlarm1OnTrap": gnLExternalAlarm1OnTrap,
       "gnLExternalAlarm2OnTrap": gnLExternalAlarm2OnTrap,
       "gnLExternalAlarm3OnTrap": gnLExternalAlarm3OnTrap,
       "gnLExternalAlarm4OnTrap": gnLExternalAlarm4OnTrap,
       "gnLExternalAlarm5OnTrap": gnLExternalAlarm5OnTrap,
       "gnLExternalAlarm6OnTrap": gnLExternalAlarm6OnTrap,
       "gnLExternalAlarm7OnTrap": gnLExternalAlarm7OnTrap,
       "gnLExternalAlarm8OnTrap": gnLExternalAlarm8OnTrap,
       "gnLSystemFaultTrap": gnLSystemFaultTrap,
       "gnLTftpFaultTrap": gnLTftpFaultTrap,
       "gnLInternalDownloadFaultTrap": gnLInternalDownloadFaultTrap,
       "gnLIntralinkFaultTrap": gnLIntralinkFaultTrap,
       "gnLConfMismatchTrap": gnLConfMismatchTrap,
       "gnLProtectSwitchFaultTrap": gnLProtectSwitchFaultTrap,
       "gnLProtectCableFaultTrap": gnLProtectCableFaultTrap,
       "gnLHeartBeatTrap": gnLHeartBeatTrap,
       "gnLLomTrap": gnLLomTrap,
       "gnLHitlessProblemTrap": gnLHitlessProblemTrap,
       "gnLHitlessRadioLofTrap": gnLHitlessRadioLofTrap,
       "gnLHitlessCableDisconnectTrap": gnLHitlessCableDisconnectTrap,
       "gnLPamTrap": gnLPamTrap,
       "gnLScmTrap": gnLScmTrap,
       "gnLInvTrap": gnLInvTrap,
       "gnLInbandTrap": gnLInbandTrap,
       "gnWSLOSTrap": gnWSLOSTrap,
       "gnODUtoODUCableFaultTrap": gnODUtoODUCableFaultTrap,
       "gnNoSignalReceivedFromODUTrap": gnNoSignalReceivedFromODUTrap,
       "gnProtectionLockoutConfiguredTrap": gnProtectionLockoutConfiguredTrap,
       "gnRFUPowerFailureTrap": gnRFUPowerFailureTrap,
       "gnRFURxLevelPathOutOfRangeTrap": gnRFURxLevelPathOutOfRangeTrap,
       "gnRFUExtremeTemperatureTrap": gnRFUExtremeTemperatureTrap,
       "gnRFUFanFailureTrap": gnRFUFanFailureTrap,
       "gnLowSignalToRFUTrap": gnLowSignalToRFUTrap,
       "gnRFUXPICClockFailureTrap": gnRFUXPICClockFailureTrap,
       "gnRFUDelayCalibrationFailure1Trap": gnRFUDelayCalibrationFailure1Trap,
       "gnRFUDelayCalibrationFailure2Trap": gnRFUDelayCalibrationFailure2Trap,
       "gnLSFPFaultTrap": gnLSFPFaultTrap,
       "gnEncryptionFaultTrap": gnEncryptionFaultTrap,
       "gnEncryptionSyncLosTrap": gnEncryptionSyncLosTrap,
       "gnEncryptionKepTimout": gnEncryptionKepTimout,
       "gnEncryptionSkTimerElapsed": gnEncryptionSkTimerElapsed,
       "gnEncryptionPowerUpSelfTestFail": gnEncryptionPowerUpSelfTestFail,
       "gnEncryptionConditionalTestFail": gnEncryptionConditionalTestFail,
       "gnEncryptionWillTurnOffOnNextRest": gnEncryptionWillTurnOffOnNextRest,
       "gnEncryptionEventReport": gnEncryptionEventReport,
       "gnEncryptionTechCardWasDetected": gnEncryptionTechCardWasDetected,
       "gnAdminPasswordInDefaultState": gnAdminPasswordInDefaultState,
       "gnLinkGroupingProtectionFaultTrap": gnLinkGroupingProtectionFaultTrap,
       "gnLossOfProtectionTrap": gnLossOfProtectionTrap,
       "gnTempLicenseTrap": gnTempLicenseTrap,
       "gnMultiRadioProblemTrap": gnMultiRadioProblemTrap,
       "gnLODUPowerOkTrap": gnLODUPowerOkTrap,
       "gnLODUSynthLockTrap": gnLODUSynthLockTrap,
       "gnLODUTxLevelInRangeTrap": gnLODUTxLevelInRangeTrap,
       "gnLODURxLevelInRangeTrap": gnLODURxLevelInRangeTrap,
       "gnLODUNormalTempTrap": gnLODUNormalTempTrap,
       "gnLIDUPowerOkTrap": gnLIDUPowerOkTrap,
       "gnLCableOkTrap": gnLCableOkTrap,
       "gnLModemOkTrap": gnLModemOkTrap,
       "gnLIDUNormalTempTrap": gnLIDUNormalTempTrap,
       "gnLLoopbackOffTrap": gnLLoopbackOffTrap,
       "gnLRemoteCommOkTrap": gnLRemoteCommOkTrap,
       "gnLNoTestRunningTrap": gnLNoTestRunningTrap,
       "gnLNoLOFTrap": gnLNoLOFTrap,
       "gnLNoLOSTrap": gnLNoLOSTrap,
       "gnLNoTIMTrap": gnLNoTIMTrap,
       "gnLNoEXCTrap": gnLNoEXCTrap,
       "gnLNoSDTrap": gnLNoSDTrap,
       "gnLNoAisTrap": gnLNoAisTrap,
       "gnLNoUnExpTrap": gnLNoUnExpTrap,
       "gnLNoLocTrap": gnLNoLocTrap,
       "gnLNoLopTrap": gnLNoLopTrap,
       "gnLNoRdiTrap": gnLNoRdiTrap,
       "gnLNoSlmTrap": gnLNoSlmTrap,
       "gnLNoUnqTrap": gnLNoUnqTrap,
       "gnLExternalAlarm1OffTrap": gnLExternalAlarm1OffTrap,
       "gnLExternalAlarm2OffTrap": gnLExternalAlarm2OffTrap,
       "gnLExternalAlarm3OffTrap": gnLExternalAlarm3OffTrap,
       "gnLExternalAlarm4OffTrap": gnLExternalAlarm4OffTrap,
       "gnLExternalAlarm5OffTrap": gnLExternalAlarm5OffTrap,
       "gnLExternalAlarm6OffTrap": gnLExternalAlarm6OffTrap,
       "gnLExternalAlarm7OffTrap": gnLExternalAlarm7OffTrap,
       "gnLExternalAlarm8OffTrap": gnLExternalAlarm8OffTrap,
       "gnLSystemOkTrap": gnLSystemOkTrap,
       "gnLTftpOkTrap": gnLTftpOkTrap,
       "gnLInternalDownloadOkTrap": gnLInternalDownloadOkTrap,
       "gnLIntralinkOkTrap": gnLIntralinkOkTrap,
       "gnLNoConfMismatchTrap": gnLNoConfMismatchTrap,
       "gnLProtectSwitchOkTrap": gnLProtectSwitchOkTrap,
       "gnLProtectCableOkTrap": gnLProtectCableOkTrap,
       "gnLLomOkTrap": gnLLomOkTrap,
       "gnLHitlessProblemOKTrap": gnLHitlessProblemOKTrap,
       "gnLHitlessRadioLofOKTrap": gnLHitlessRadioLofOKTrap,
       "gnLHitlessCableDisconnectOKTrap": gnLHitlessCableDisconnectOKTrap,
       "gnLPamOkTrap": gnLPamOkTrap,
       "gnLScmOkTrap": gnLScmOkTrap,
       "gnLInvOkTrap": gnLInvOkTrap,
       "gnLInbandOkTrap": gnLInbandOkTrap,
       "gnWSNoLOSTrap": gnWSNoLOSTrap,
       "gnODUtoODUCableOkTrap": gnODUtoODUCableOkTrap,
       "gnSignalReceivedFromODUTrap": gnSignalReceivedFromODUTrap,
       "gnProtectionLockoutClearededTrap": gnProtectionLockoutClearededTrap,
       "gnRFUPowerFailureClearedTrap": gnRFUPowerFailureClearedTrap,
       "gnRFURxLevelPathOutOfRangeClearedTrap": gnRFURxLevelPathOutOfRangeClearedTrap,
       "gnRFUExtremeTemperatureClearedTrap": gnRFUExtremeTemperatureClearedTrap,
       "gnRFUFanFailureClearedTrap": gnRFUFanFailureClearedTrap,
       "gnLowSignalToRFUClearedTrap": gnLowSignalToRFUClearedTrap,
       "gnRFUXPICClockFailureClearedTrap": gnRFUXPICClockFailureClearedTrap,
       "gnRFUDelayCalibrationFailure1ClearedTrap": gnRFUDelayCalibrationFailure1ClearedTrap,
       "gnRFUDelayCalibrationFailure2ClearedTrap": gnRFUDelayCalibrationFailure2ClearedTrap,
       "gnLSFPOkTrap": gnLSFPOkTrap,
       "gnEncryptionFaultClearedTrap": gnEncryptionFaultClearedTrap,
       "gnEncryptionSyncLosClearedTrap": gnEncryptionSyncLosClearedTrap,
       "gnEncryptionKepTimoutCleared": gnEncryptionKepTimoutCleared,
       "gnEncryptionSkTimerElapsedCleared": gnEncryptionSkTimerElapsedCleared,
       "gnEncryptionPowerUpSelfTestFailCleared": gnEncryptionPowerUpSelfTestFailCleared,
       "gnEncryptionConditionalTestFailCleared": gnEncryptionConditionalTestFailCleared,
       "gnEncryptionWillTurnOffOnNextRestCleared": gnEncryptionWillTurnOffOnNextRestCleared,
       "gnEncryptionEventReportCleared": gnEncryptionEventReportCleared,
       "gnEncryptionTechCardWasDetectedCleared": gnEncryptionTechCardWasDetectedCleared,
       "gnAdminPasswordInDefaultStateCleared": gnAdminPasswordInDefaultStateCleared,
       "gnLinkGroupingProtectionFaultClearedTrap": gnLinkGroupingProtectionFaultClearedTrap,
       "gnLossOfProtectionClearedTrap": gnLossOfProtectionClearedTrap,
       "gnTempLicenseClearedTrap": gnTempLicenseClearedTrap,
       "gnMultiRadioProblemOKTrap": gnMultiRadioProblemOKTrap,
       "gnRODUPowerFailTrap": gnRODUPowerFailTrap,
       "gnRODUSynthUnLockTrap": gnRODUSynthUnLockTrap,
       "gnRODUTxLevelOutOfRangeTrap": gnRODUTxLevelOutOfRangeTrap,
       "gnRODURxLevelOutOfRangeTrap": gnRODURxLevelOutOfRangeTrap,
       "gnRODUExtremeTempTrap": gnRODUExtremeTempTrap,
       "gnRIDUPowerFailTrap": gnRIDUPowerFailTrap,
       "gnRCableFaultTrap": gnRCableFaultTrap,
       "gnRModemFailTrap": gnRModemFailTrap,
       "gnRIDUExtremeTempTrap": gnRIDUExtremeTempTrap,
       "gnRLoopbackOnTrap": gnRLoopbackOnTrap,
       "gnRRemoteCommFaultTrap": gnRRemoteCommFaultTrap,
       "gnRTestRunningTrap": gnRTestRunningTrap,
       "gnRLOFTrap": gnRLOFTrap,
       "gnRLOSTrap": gnRLOSTrap,
       "gnRTIMTrap": gnRTIMTrap,
       "gnREXCTrap": gnREXCTrap,
       "gnRSDTrap": gnRSDTrap,
       "gnRAisTrap": gnRAisTrap,
       "gnRUnExpTrap": gnRUnExpTrap,
       "gnRLocTrap": gnRLocTrap,
       "gnRLopTrap": gnRLopTrap,
       "gnRRdiTrap": gnRRdiTrap,
       "gnRSlmTrap": gnRSlmTrap,
       "gnRUnqTrap": gnRUnqTrap,
       "gnRExternalAlarm1OnTrap": gnRExternalAlarm1OnTrap,
       "gnRExternalAlarm2OnTrap": gnRExternalAlarm2OnTrap,
       "gnRExternalAlarm3OnTrap": gnRExternalAlarm3OnTrap,
       "gnRExternalAlarm4OnTrap": gnRExternalAlarm4OnTrap,
       "gnRExternalAlarm5OnTrap": gnRExternalAlarm5OnTrap,
       "gnRExternalAlarm6OnTrap": gnRExternalAlarm6OnTrap,
       "gnRExternalAlarm7OnTrap": gnRExternalAlarm7OnTrap,
       "gnRExternalAlarm8OnTrap": gnRExternalAlarm8OnTrap,
       "gnRSystemFaultTrap": gnRSystemFaultTrap,
       "gnRTftpFaultTrap": gnRTftpFaultTrap,
       "gnRInternalDownloadFaultTrap": gnRInternalDownloadFaultTrap,
       "gnRIntralinkFaultTrap": gnRIntralinkFaultTrap,
       "gnRConfMismatchTrap": gnRConfMismatchTrap,
       "gnRProtectSwitchFaultTrap": gnRProtectSwitchFaultTrap,
       "gnRProtectCableFaultTrap": gnRProtectCableFaultTrap,
       "gnRHeartBeatTrap": gnRHeartBeatTrap,
       "gnRLomTrap": gnRLomTrap,
       "gnRHitlessRadioLofTrap": gnRHitlessRadioLofTrap,
       "gnRHitlessCableDisconnectTrap": gnRHitlessCableDisconnectTrap,
       "gnRODUPowerOkTrap": gnRODUPowerOkTrap,
       "gnRODUSynthLockTrap": gnRODUSynthLockTrap,
       "gnRODUTxLevelInRangeTrap": gnRODUTxLevelInRangeTrap,
       "gnRODURxLevelInRangeTrap": gnRODURxLevelInRangeTrap,
       "gnRODUNormalTempTrap": gnRODUNormalTempTrap,
       "gnRIDUPowerOkTrap": gnRIDUPowerOkTrap,
       "gnRCableOkTrap": gnRCableOkTrap,
       "gnRModemOkTrap": gnRModemOkTrap,
       "gnRIDUNormalTempTrap": gnRIDUNormalTempTrap,
       "gnRLoopbackOffTrap": gnRLoopbackOffTrap,
       "gnRRemoteCommOkTrap": gnRRemoteCommOkTrap,
       "gnRNoTestRunningTrap": gnRNoTestRunningTrap,
       "gnRNoLOFTrap": gnRNoLOFTrap,
       "gnRNoLOSTrap": gnRNoLOSTrap,
       "gnRNoTIMTrap": gnRNoTIMTrap,
       "gnRNoEXCTrap": gnRNoEXCTrap,
       "gnRNoSDTrap": gnRNoSDTrap,
       "gnRNoAisTrap": gnRNoAisTrap,
       "gnRNoUnExpTrap": gnRNoUnExpTrap,
       "gnRNoLocTrap": gnRNoLocTrap,
       "gnRNoLopTrap": gnRNoLopTrap,
       "gnRNoRdiTrap": gnRNoRdiTrap,
       "gnRNoSlmTrap": gnRNoSlmTrap,
       "gnRNoUnqTrap": gnRNoUnqTrap,
       "gnRExternalAlarm1OffTrap": gnRExternalAlarm1OffTrap,
       "gnRExternalAlarm2OffTrap": gnRExternalAlarm2OffTrap,
       "gnRExternalAlarm3OffTrap": gnRExternalAlarm3OffTrap,
       "gnRExternalAlarm4OffTrap": gnRExternalAlarm4OffTrap,
       "gnRExternalAlarm5OffTrap": gnRExternalAlarm5OffTrap,
       "gnRExternalAlarm6OffTrap": gnRExternalAlarm6OffTrap,
       "gnRExternalAlarm7OffTrap": gnRExternalAlarm7OffTrap,
       "gnRExternalAlarm8OffTrap": gnRExternalAlarm8OffTrap,
       "gnRSystemOkTrap": gnRSystemOkTrap,
       "gnRTftpOkTrap": gnRTftpOkTrap,
       "gnRInternalDownloadOkTrap": gnRInternalDownloadOkTrap,
       "gnRIntralinkOkTrap": gnRIntralinkOkTrap,
       "gnRNoConfMismatchTrap": gnRNoConfMismatchTrap,
       "gnRProtectCableOkTrap": gnRProtectCableOkTrap,
       "gnRLomOkTrap": gnRLomOkTrap,
       "gnRHitlessRadioLofOKTrap": gnRHitlessRadioLofOKTrap,
       "gnRHitlessCableDisconnectOKTrap": gnRHitlessCableDisconnectOKTrap,
       "gnOID": gnOID,
       "gnFirstOID": gnFirstOID,
       "gnSystem": gnSystem,
       "gnGeneral": gnGeneral,
       "gnGenStandardOrg": gnGenStandardOrg,
       "gnGenTxFreqRange": gnGenTxFreqRange,
       "gnGenRemoteConnection": gnGenRemoteConnection,
       "gnGenRemoteDistance": gnGenRemoteDistance,
       "gnGenInterLenLocalRemote": gnGenInterLenLocalRemote,
       "gnGenTxFreqLocalRemote": gnGenTxFreqLocalRemote,
       "gnGenRealTimeandDate": gnGenRealTimeandDate,
       "gnGenCfgDeviceTable": gnGenCfgDeviceTable,
       "gnGenCfgDeviceEntry": gnGenCfgDeviceEntry,
       "gnGenCfgDeviceId": gnGenCfgDeviceId,
       "gnGenCfgDeviceResetPerfMon": gnGenCfgDeviceResetPerfMon,
       "gnGenCfgDeviceOperation": gnGenCfgDeviceOperation,
       "gnGenCfgActivateLoopback": gnGenCfgActivateLoopback,
       "gnGenCfgF1DataChanConnector": gnGenCfgF1DataChanConnector,
       "gnGenCfgWaySideConnector": gnGenCfgWaySideConnector,
       "gnGenCfgActivateChanLoopback": gnGenCfgActivateChanLoopback,
       "gnGenCfgInterLenLocalOnly": gnGenCfgInterLenLocalOnly,
       "gnGenCfgSlipIp": gnGenCfgSlipIp,
       "gnGenCfgSlipModemConnection": gnGenCfgSlipModemConnection,
       "gnGenCfgSlipSpeed": gnGenCfgSlipSpeed,
       "gnGenCfgAlarmSeverity": gnGenCfgAlarmSeverity,
       "gnGenCfgODUSerialNumber": gnGenCfgODUSerialNumber,
       "gnGenCfgIDUSerialNumber": gnGenCfgIDUSerialNumber,
       "gnGenCfgAlarmText": gnGenCfgAlarmText,
       "gnGenCfgTrapSeverity": gnGenCfgTrapSeverity,
       "gnGenCfgProductType": gnGenCfgProductType,
       "gnGenCfgLeftMediumConnector": gnGenCfgLeftMediumConnector,
       "gnGenCfgMiddleMediumConnector": gnGenCfgMiddleMediumConnector,
       "gnGenCfgPrimaryClockSource": gnGenCfgPrimaryClockSource,
       "gnGenCfgSecondaryClockSource": gnGenCfgSecondaryClockSource,
       "gnGenCfgTrapOption": gnGenCfgTrapOption,
       "gnGenCfgCLLI": gnGenCfgCLLI,
       "gnGenCfgHeartbeatPeriod": gnGenCfgHeartbeatPeriod,
       "gnGenCfgGetRemoteData": gnGenCfgGetRemoteData,
       "gnGenCfgClearLoopTimeout": gnGenCfgClearLoopTimeout,
       "gnGenCfgSubProductType": gnGenCfgSubProductType,
       "gnGenStatDeviceTable": gnGenStatDeviceTable,
       "gnGenStatDeviceEntry": gnGenStatDeviceEntry,
       "gnGenStatDeviceId": gnGenStatDeviceId,
       "gnGenStatDeviceCelsiusTemp": gnGenStatDeviceCelsiusTemp,
       "gnGenStatDeviceFahrenheitTemp": gnGenStatDeviceFahrenheitTemp,
       "gnGenStatDevicePowerSupply": gnGenStatDevicePowerSupply,
       "gnGenStatDeviceCable": gnGenStatDeviceCable,
       "gnGenStatDeviceDryContact": gnGenStatDeviceDryContact,
       "gnGenStatDeviceLeds": gnGenStatDeviceLeds,
       "gnGenStatInternalCommunication": gnGenStatInternalCommunication,
       "gnGenStatDeviceFanStatus": gnGenStatDeviceFanStatus,
       "gnGenStatDeviceODUStatus": gnGenStatDeviceODUStatus,
       "gnGenStatDeviceIDUStatus": gnGenStatDeviceIDUStatus,
       "gnGenStatDeviceRSTStatus": gnGenStatDeviceRSTStatus,
       "gnGenChannelBandwidth": gnGenChannelBandwidth,
       "gnGenTxFreqNumLocalRemote": gnGenTxFreqNumLocalRemote,
       "gnGenProtocolType": gnGenProtocolType,
       "gnGenLinkId": gnGenLinkId,
       "gnGenMibVersion": gnGenMibVersion,
       "gnGenModemType": gnGenModemType,
       "gnGenRadioSide": gnGenRadioSide,
       "gnGenSystemWorkTime": gnGenSystemWorkTime,
       "gnGenRxFreqNumLocalRemote": gnGenRxFreqNumLocalRemote,
       "gnGenLastCfgTimeandDate": gnGenLastCfgTimeandDate,
       "gnGenMostSevereAlarm": gnGenMostSevereAlarm,
       "gnGenIdcCfgTable": gnGenIdcCfgTable,
       "gnGenIdcCfgEntry": gnGenIdcCfgEntry,
       "gnGenIdcCfgId": gnGenIdcCfgId,
       "gnGenIdcCfgXpicMode": gnGenIdcCfgXpicMode,
       "gnGenIdcCfgResetPerfMon": gnGenIdcCfgResetPerfMon,
       "gnGenIdcCfgOperation": gnGenIdcCfgOperation,
       "gnGenIdcCfgWaySideConnector": gnGenIdcCfgWaySideConnector,
       "gnGenIdcCfgHeartbeatPeriod": gnGenIdcCfgHeartbeatPeriod,
       "gnGenIdcCfgClearLoopTimeout": gnGenIdcCfgClearLoopTimeout,
       "gnGenIdcCfgSlipIp": gnGenIdcCfgSlipIp,
       "gnGenIdcCfgSlipModemConnection": gnGenIdcCfgSlipModemConnection,
       "gnGenIdcCfgSlipSpeed": gnGenIdcCfgSlipSpeed,
       "gnGenIdcCfgAlarmSeverity": gnGenIdcCfgAlarmSeverity,
       "gnGenIdcCfgIDUSerialNumber": gnGenIdcCfgIDUSerialNumber,
       "gnGenIdcCfgTrapOption": gnGenIdcCfgTrapOption,
       "gnGenIdcCfgCLLI": gnGenIdcCfgCLLI,
       "gnGenIdcCfgEowCascadeStatus": gnGenIdcCfgEowCascadeStatus,
       "gnGenIdcCfgSerialPPPAdminStatus": gnGenIdcCfgSerialPPPAdminStatus,
       "gnGenIdcStatTable": gnGenIdcStatTable,
       "gnGenIdcStatEntry": gnGenIdcStatEntry,
       "gnGenIdcStatId": gnGenIdcStatId,
       "gnGenIdcStatXpicSupport": gnGenIdcStatXpicSupport,
       "gnGenIdcStatLeds": gnGenIdcStatLeds,
       "gnGenIdcStatIDUStatus": gnGenIdcStatIDUStatus,
       "gnGenIdcStatMMCCardStatus": gnGenIdcStatMMCCardStatus,
       "gnGenIdcStatDryContact": gnGenIdcStatDryContact,
       "gnGenIdcStatFanStatus": gnGenIdcStatFanStatus,
       "gnGenIdcStatLeftDrawerStatus": gnGenIdcStatLeftDrawerStatus,
       "gnGenIdcStatRightDrawerStatus": gnGenIdcStatRightDrawerStatus,
       "gnGenIdcStatHitlessSupport": gnGenIdcStatHitlessSupport,
       "gnGenIdcStatEowExistence": gnGenIdcStatEowExistence,
       "gnGenIdcStatEowSupport": gnGenIdcStatEowSupport,
       "gnGenIdcStatIduPosition": gnGenIdcStatIduPosition,
       "gnGenIdcStatBoardType": gnGenIdcStatBoardType,
       "gnGenIdcStatAgentIPAddress": gnGenIdcStatAgentIPAddress,
       "gnGenIdcStatInterfaceConnector": gnGenIdcStatInterfaceConnector,
       "gnGenIdcStatIfTableCounter": gnGenIdcStatIfTableCounter,
       "gnGeneralXTable": gnGeneralXTable,
       "gnGeneralXEntry": gnGeneralXEntry,
       "gnGenXId": gnGenXId,
       "gnGenXStandardOrg": gnGenXStandardOrg,
       "gnGenXRemoteConnection": gnGenXRemoteConnection,
       "gnGenXLinkId": gnGenXLinkId,
       "gnGenXModemType": gnGenXModemType,
       "gnGenXRadioSide": gnGenXRadioSide,
       "gnGenXSystemWorkTime": gnGenXSystemWorkTime,
       "gnGenXOperation": gnGenXOperation,
       "gnGenXResetPerfMon": gnGenXResetPerfMon,
       "gnGenXAlarmSeverity": gnGenXAlarmSeverity,
       "gnGenXCarrierSerialNumber": gnGenXCarrierSerialNumber,
       "gnGenXMUXSerialNumber": gnGenXMUXSerialNumber,
       "gnGenXProductType": gnGenXProductType,
       "gnGenXCarrierConnector": gnGenXCarrierConnector,
       "gnGenXInterfacesLeds": gnGenXInterfacesLeds,
       "gnGenXMultiRateMultiConsConf": gnGenXMultiRateMultiConsConf,
       "gnGenXMultiRateMultiConsSupport": gnGenXMultiRateMultiConsSupport,
       "gnGenXWaysideChannel": gnGenXWaysideChannel,
       "gnGenXWaySideLoopback": gnGenXWaySideLoopback,
       "gnGenXSyncIdcDataBase": gnGenXSyncIdcDataBase,
       "gnGenXAesEnable": gnGenXAesEnable,
       "gnGenXAesMkeyMode": gnGenXAesMkeyMode,
       "gnGenXActNumOfInterfaceOnClass1": gnGenXActNumOfInterfaceOnClass1,
       "gnGenXActNumOfInterfaceOnClass2": gnGenXActNumOfInterfaceOnClass2,
       "gnGenXActNumOfInterfaceOnClass3": gnGenXActNumOfInterfaceOnClass3,
       "gnGenXEowStatus": gnGenXEowStatus,
       "gnGenXTempLicenseEnable": gnGenXTempLicenseEnable,
       "gnGenXTempLicenseTimer": gnGenXTempLicenseTimer,
       "gnGenXDefectBlocks": gnGenXDefectBlocks,
       "gnGenXBytesCorrected": gnGenXBytesCorrected,
       "gnGenXPrbsTest": gnGenXPrbsTest,
       "gnGenXClearCounters": gnGenXClearCounters,
       "gnGenXMuxLicense": gnGenXMuxLicense,
       "gnGenAddAlarmExtToTraps": gnGenAddAlarmExtToTraps,
       "gnGenFeatureSupport": gnGenFeatureSupport,
       "gnGeneralMrmcXTable": gnGeneralMrmcXTable,
       "gnGeneralMrmcXEntry": gnGeneralMrmcXEntry,
       "gnGenMrmcXId": gnGenMrmcXId,
       "gnGenMrmcXMrmcVal": gnGenMrmcXMrmcVal,
       "gnGenMrmcXBitRate": gnGenMrmcXBitRate,
       "gnGenMrmcXBandWidth": gnGenMrmcXBandWidth,
       "gnGenMrmcXQam": gnGenMrmcXQam,
       "gnGenMrmcXScriptType": gnGenMrmcXScriptType,
       "gnGenDrawerXTable": gnGenDrawerXTable,
       "gnGenDrawerXEntry": gnGenDrawerXEntry,
       "gnGenDrawerXId": gnGenDrawerXId,
       "gnGenDrawerXName": gnGenDrawerXName,
       "gnGenDrawerXSlot1Status": gnGenDrawerXSlot1Status,
       "gnGenDrawerXSlot2Status": gnGenDrawerXSlot2Status,
       "gnGenDrawerXDeviceLeds": gnGenDrawerXDeviceLeds,
       "gnGenDrawerXInternalCommunication": gnGenDrawerXInternalCommunication,
       "gnGenDrawerXDeviceIDUStatus": gnGenDrawerXDeviceIDUStatus,
       "gnCluster": gnCluster,
       "cluster": cluster,
       "clusterSystemType": clusterSystemType,
       "clusterNumOfSubRacks": clusterNumOfSubRacks,
       "clusterSubRackNum": clusterSubRackNum,
       "clusterFloorNum": clusterFloorNum,
       "clusterIPBase": clusterIPBase,
       "clusterIDCRole": clusterIDCRole,
       "clusterPrimeIPAddress": clusterPrimeIPAddress,
       "clusterPeerIPLastChangeTime": clusterPeerIPLastChangeTime,
       "addressesTable": addressesTable,
       "addressesEntry": addressesEntry,
       "addressesPeerIPId": addressesPeerIPId,
       "addressesPeerIPAddress": addressesPeerIPAddress,
       "primeIDC": primeIDC,
       "primeIDCAutoInternalClockDistribution": primeIDCAutoInternalClockDistribution,
       "primeIDCSynchronizeClockInCluster": primeIDCSynchronizeClockInCluster,
       "backplaneSlotMappingTable": backplaneSlotMappingTable,
       "backplaneSlotMappingEntry": backplaneSlotMappingEntry,
       "backplaneSlotMappingSubrackId": backplaneSlotMappingSubrackId,
       "backplaneSlotMappingFloorId": backplaneSlotMappingFloorId,
       "backplaneSlotMappingDrawerId": backplaneSlotMappingDrawerId,
       "backplaneSlotMappingSubDrawerId": backplaneSlotMappingSubDrawerId,
       "backplaneSlotMappingUnitType": backplaneSlotMappingUnitType,
       "backplaneSlotMappingUnitNumber": backplaneSlotMappingUnitNumber,
       "backplaneSlotMappingUnitIndex": backplaneSlotMappingUnitIndex,
       "gnSubrack": gnSubrack,
       "powerInputTable": powerInputTable,
       "powerInputEntry": powerInputEntry,
       "powerInputId": powerInputId,
       "powerInputAdmin": powerInputAdmin,
       "powerInputStatus": powerInputStatus,
       "powerInputLedStatus": powerInputLedStatus,
       "auxiliaryDrawer": auxiliaryDrawer,
       "auxiliaryDrawerAuxCardType": auxiliaryDrawerAuxCardType,
       "auxiliaryDrawerLedsStatus": auxiliaryDrawerLedsStatus,
       "auxiliaryDrawerBoardHWVersion": auxiliaryDrawerBoardHWVersion,
       "auxiliaryDrawerBoardFWVersion": auxiliaryDrawerBoardFWVersion,
       "auxiliaryDrawerBoardPostResetFWVersion": auxiliaryDrawerBoardPostResetFWVersion,
       "auxiliaryDrawerSerialNumber": auxiliaryDrawerSerialNumber,
       "auxiliaryDrawerBoardReset": auxiliaryDrawerBoardReset,
       "auxiliaryDrawerOrderWireCascading": auxiliaryDrawerOrderWireCascading,
       "xcDrawerTable": xcDrawerTable,
       "xcDrawerEntry": xcDrawerEntry,
       "xcDrawerXCId": xcDrawerXCId,
       "xcDrawerLedsStatus": xcDrawerLedsStatus,
       "xcDrawerBoardHWVersion": xcDrawerBoardHWVersion,
       "xcDrawerBoardFWVersion": xcDrawerBoardFWVersion,
       "xcDrawerBoardPostResetFWVersion": xcDrawerBoardPostResetFWVersion,
       "xcDrawerSerialNumber": xcDrawerSerialNumber,
       "xcDrawerResetXCBoard": xcDrawerResetXCBoard,
       "xcDrawerXCSelfTestResult": xcDrawerXCSelfTestResult,
       "xcDrawerXCActivityRole": xcDrawerXCActivityRole,
       "xcDrawerSyncIdcDataBase": xcDrawerSyncIdcDataBase,
       "xcDrawerXCConnector": xcDrawerXCConnector,
       "gnGenCarrierXTable": gnGenCarrierXTable,
       "gnGenCarrierXEntry": gnGenCarrierXEntry,
       "gnGenCarrierXId": gnGenCarrierXId,
       "gnGenCarrierXResetPerfMon": gnGenCarrierXResetPerfMon,
       "gnGenCarrierXSyncIdcDataBase": gnGenCarrierXSyncIdcDataBase,
       "gnAgn": gnAgn,
       "gnAgnMgrTable": gnAgnMgrTable,
       "gnAgnMgrEntry": gnAgnMgrEntry,
       "gnAgnMgrId": gnAgnMgrId,
       "gnAgnMgrIP": gnAgnMgrIP,
       "gnAgnMgrAlarmGroupMask": gnAgnMgrAlarmGroupMask,
       "gnAgnMgrSeverityFilter": gnAgnMgrSeverityFilter,
       "gnAgnMgrTrapPort": gnAgnMgrTrapPort,
       "gnAgnLogFileData": gnAgnLogFileData,
       "gnAgnLogFileMaxEntries": gnAgnLogFileMaxEntries,
       "gnAgnLogFileValidEntries": gnAgnLogFileValidEntries,
       "gnAgnLogFileAction": gnAgnLogFileAction,
       "gnAgnLogFileTable": gnAgnLogFileTable,
       "gnAgnLogFileEntry": gnAgnLogFileEntry,
       "gnAgnLogFileId": gnAgnLogFileId,
       "gnAgnLogFileValid": gnAgnLogFileValid,
       "gnAgnLogFileDate": gnAgnLogFileDate,
       "gnAgnLogFileTime": gnAgnLogFileTime,
       "gnAgnLogFileSeverity": gnAgnLogFileSeverity,
       "gnAgnLogFileText": gnAgnLogFileText,
       "gnAgnLogFileDeviceCelsiusTemp": gnAgnLogFileDeviceCelsiusTemp,
       "gnAgnLogFileDevicePowerSupply": gnAgnLogFileDevicePowerSupply,
       "gnAgnLogFileInternalCommunication": gnAgnLogFileInternalCommunication,
       "gnAgnLogFileDeviceFanStatus": gnAgnLogFileDeviceFanStatus,
       "gnAgnLogFileDeviceODUStatus": gnAgnLogFileDeviceODUStatus,
       "gnAgnLogFileDeviceIDUStatus": gnAgnLogFileDeviceIDUStatus,
       "gnAgnLogFileOduCelsiusTemp": gnAgnLogFileOduCelsiusTemp,
       "gnAgnLogFileOduReceiveLevel": gnAgnLogFileOduReceiveLevel,
       "gnAgnLogFileOduSynthesizerVCOLock": gnAgnLogFileOduSynthesizerVCOLock,
       "gnAgnLogFileOduPowerSupply": gnAgnLogFileOduPowerSupply,
       "gnAgnLogFileLineBERCur": gnAgnLogFileLineBERCur,
       "gnAgnLogFileRadioBERCur": gnAgnLogFileRadioBERCur,
       "gnAgnLogFileModStatus": gnAgnLogFileModStatus,
       "gnAgnLogFileDemodStatus": gnAgnLogFileDemodStatus,
       "gnAgnLogFileLastDemodDefectBlocks": gnAgnLogFileLastDemodDefectBlocks,
       "gnAgnLogFileLastDemodBytesCorrected": gnAgnLogFileLastDemodBytesCorrected,
       "gnAgnLogFileLastDemodBlocksCorrected": gnAgnLogFileLastDemodBlocksCorrected,
       "gnAgnLogFileUniqueId": gnAgnLogFileUniqueId,
       "gnAgnLogFileSource": gnAgnLogFileSource,
       "gnAgnLogFileTimeT": gnAgnLogFileTimeT,
       "gnAgnLogFileHitlessSwitchLogAdmin": gnAgnLogFileHitlessSwitchLogAdmin,
       "gnAgnLogFileXCSwitchLogAdmin": gnAgnLogFileXCSwitchLogAdmin,
       "gnAgnExternAlarm": gnAgnExternAlarm,
       "gnAgnInExternAlarmTable": gnAgnInExternAlarmTable,
       "gnAgnInExternAlarmEntry": gnAgnInExternAlarmEntry,
       "gnAgnInExternAlarmDevId": gnAgnInExternAlarmDevId,
       "gnAgnInExternAlarmIndex": gnAgnInExternAlarmIndex,
       "gnAgnInExternAlarmEnable": gnAgnInExternAlarmEnable,
       "gnAgnInExternAlarmText": gnAgnInExternAlarmText,
       "gnAgnInExternAlarmSeverity": gnAgnInExternAlarmSeverity,
       "gnAgnOutRelayAlarmTable": gnAgnOutRelayAlarmTable,
       "gnAgnOutRelayAlarmEntry": gnAgnOutRelayAlarmEntry,
       "gnAgnOutRelayAlarmDevId": gnAgnOutRelayAlarmDevId,
       "gnAgnOutRelayAlarmIndex": gnAgnOutRelayAlarmIndex,
       "gnAgnOutRelayAlarmType": gnAgnOutRelayAlarmType,
       "gnAgnFileTransfer": gnAgnFileTransfer,
       "gnAgnFileTransferDestination": gnAgnFileTransferDestination,
       "gnAgnFileTransferServerIP": gnAgnFileTransferServerIP,
       "gnAgnFileTransferFileName": gnAgnFileTransferFileName,
       "gnAgnFileTransferTftpTotalTimeOut": gnAgnFileTransferTftpTotalTimeOut,
       "gnAgnFileTransferTransCmd": gnAgnFileTransferTransCmd,
       "gnAgnFileTransfertFtpStatus": gnAgnFileTransfertFtpStatus,
       "gnAgnFileTransfertftpBlockCount": gnAgnFileTransfertftpBlockCount,
       "gnAgnFileTransferProtocol": gnAgnFileTransferProtocol,
       "gnAgnFileTransferUserName": gnAgnFileTransferUserName,
       "gnAgnFileTransferPassword": gnAgnFileTransferPassword,
       "gnAgnFileTransferIDCVersionControl": gnAgnFileTransferIDCVersionControl,
       "gnAgnFileTransferODCVersionControl": gnAgnFileTransferODCVersionControl,
       "gnAgnInternalDownloadTable": gnAgnInternalDownloadTable,
       "gnAgnInternalDownloadEntry": gnAgnInternalDownloadEntry,
       "gnAgnInternalDownloadId": gnAgnInternalDownloadId,
       "gnAgnInternalDownloadOperation": gnAgnInternalDownloadOperation,
       "gnAgnInternalDownloadAction": gnAgnInternalDownloadAction,
       "gnAgnInternalDownloadStatus": gnAgnInternalDownloadStatus,
       "gnAgnInternalDownloadBlockCount": gnAgnInternalDownloadBlockCount,
       "gnAgnInternalDownloadVersionControl": gnAgnInternalDownloadVersionControl,
       "gnAgnInternalDownloadFileSizeInBytes": gnAgnInternalDownloadFileSizeInBytes,
       "gnAgnInternalDownloadBytesCount": gnAgnInternalDownloadBytesCount,
       "gnAgnInterLinkTable": gnAgnInterLinkTable,
       "gnAgnInterLinkEntry": gnAgnInterLinkEntry,
       "gnAgnInterLinkId": gnAgnInterLinkId,
       "gnAgnInterLinkSide": gnAgnInterLinkSide,
       "gnAgnInterLinkSource": gnAgnInterLinkSource,
       "gnAgnInterLinkDestination": gnAgnInterLinkDestination,
       "gnAgnInterLinkSoftware": gnAgnInterLinkSoftware,
       "gnAgnInterLinkAction": gnAgnInterLinkAction,
       "gnAgnInterLinkStatus": gnAgnInterLinkStatus,
       "gnAgnInterLinkBlockCount": gnAgnInterLinkBlockCount,
       "gnSoftwareVersionTable": gnSoftwareVersionTable,
       "gnSoftwareVersionEntry": gnSoftwareVersionEntry,
       "gnSoftwareVersionId": gnSoftwareVersionId,
       "gnSoftwareVersionIDU": gnSoftwareVersionIDU,
       "gnSoftwareVersionMUX": gnSoftwareVersionMUX,
       "gnSoftwareVersionODU": gnSoftwareVersionODU,
       "gnSoftwareVersionIDUPostResetVersion": gnSoftwareVersionIDUPostResetVersion,
       "gnSoftwareVersionMUXPostResetVersion": gnSoftwareVersionMUXPostResetVersion,
       "gnSoftwareVersionODUPostResetVersion": gnSoftwareVersionODUPostResetVersion,
       "gnSoftwareVersionMuxAlteraVer": gnSoftwareVersionMuxAlteraVer,
       "gnSoftwareIDCVersionControl": gnSoftwareIDCVersionControl,
       "gnSoftwareVersionWSAlteraVer": gnSoftwareVersionWSAlteraVer,
       "gnSoftwareVersionWSPostResetVersion": gnSoftwareVersionWSPostResetVersion,
       "gnSoftwareVersionMrmcVer": gnSoftwareVersionMrmcVer,
       "gnSoftwareVersionMrmcPostResetVer": gnSoftwareVersionMrmcPostResetVer,
       "gnSoftwareVersionBootSoftVer": gnSoftwareVersionBootSoftVer,
       "gnSoftwareVersionBootFlashVer": gnSoftwareVersionBootFlashVer,
       "gnSoftwareVersionAcmLutVer": gnSoftwareVersionAcmLutVer,
       "gnSoftwareVersionAcmLutVerPostResetVer": gnSoftwareVersionAcmLutVerPostResetVer,
       "gnSoftwareVersionSfdVer": gnSoftwareVersionSfdVer,
       "gnAgnNTPCfg": gnAgnNTPCfg,
       "gnAgnNTPCfgServerIP": gnAgnNTPCfgServerIP,
       "gnAgnNTPCfgOffsetFromUTC": gnAgnNTPCfgOffsetFromUTC,
       "gnAgnNTPCfgSummerAdjOffset": gnAgnNTPCfgSummerAdjOffset,
       "gnAgnNTPCfgSummerAdjStart": gnAgnNTPCfgSummerAdjStart,
       "gnAgnNTPCfgSummerAdjEnd": gnAgnNTPCfgSummerAdjEnd,
       "gnAgnNTPCfgEnableAuth": gnAgnNTPCfgEnableAuth,
       "gnAgnNTPCfgAuthSecretKey": gnAgnNTPCfgAuthSecretKey,
       "gnAgnNTPCfgAuthPublicKey": gnAgnNTPCfgAuthPublicKey,
       "gnAgnNTPCfgUpdateInterval": gnAgnNTPCfgUpdateInterval,
       "gnAgnNTPCfgProtocolType": gnAgnNTPCfgProtocolType,
       "gnAgnInBandMng": gnAgnInBandMng,
       "gnAgnInBandMngEthernetIp": gnAgnInBandMngEthernetIp,
       "gnAgnInBandMngEthernetMask": gnAgnInBandMngEthernetMask,
       "gnAgnInBandMngPppIp": gnAgnInBandMngPppIp,
       "gnAgnInBandMngPppMask": gnAgnInBandMngPppMask,
       "gnAgnInBandMngDefRoute": gnAgnInBandMngDefRoute,
       "gnAgnInBandMngEnable": gnAgnInBandMngEnable,
       "gnAgnInBandMngNetworkElementType": gnAgnInBandMngNetworkElementType,
       "gnAgnInBandMngRadioChannel": gnAgnInBandMngRadioChannel,
       "gnAgnInBandMngUnknownPackets": gnAgnInBandMngUnknownPackets,
       "gnAgnInBandMngTTL": gnAgnInBandMngTTL,
       "gnAgnInBandMngRingIpSubnet": gnAgnInBandMngRingIpSubnet,
       "gnAgnInBandMngRingIpMask": gnAgnInBandMngRingIpMask,
       "gnAgnInBandMngNetworkId": gnAgnInBandMngNetworkId,
       "gnAgnInBandMngLineMode": gnAgnInBandMngLineMode,
       "gnAgnInBandMngFiberChannel": gnAgnInBandMngFiberChannel,
       "gnAgnInBandMngTribChannel": gnAgnInBandMngTribChannel,
       "gnAgnInBandMngXChannelTable": gnAgnInBandMngXChannelTable,
       "gnAgnInBandMngXChannelEntry": gnAgnInBandMngXChannelEntry,
       "gnAgnInBandMngXChannelId": gnAgnInBandMngXChannelId,
       "gnAgnInBandMngXChannelIfIndex": gnAgnInBandMngXChannelIfIndex,
       "gnAgnInBandMngXChannelType": gnAgnInBandMngXChannelType,
       "gnAgnInBandMngXChannelState": gnAgnInBandMngXChannelState,
       "gnAgnInBandMngXChannelNeighborIP": gnAgnInBandMngXChannelNeighborIP,
       "gnAgnInBandMngXChannelStatus": gnAgnInBandMngXChannelStatus,
       "gnAgnInBandMngXEnableInbandChannels": gnAgnInBandMngXEnableInbandChannels,
       "gnAgnInBandMngMainGNEInterface": gnAgnInBandMngMainGNEInterface,
       "gnNeighborIP": gnNeighborIP,
       "gnNeighborInBandTable": gnNeighborInBandTable,
       "gnNeighborInBandEntry": gnNeighborInBandEntry,
       "gnNeighborInBandIP": gnNeighborInBandIP,
       "gnNeighborInBandStatus": gnNeighborInBandStatus,
       "gnNeighborMateIP": gnNeighborMateIP,
       "gnNeighborRemoteRadioIP": gnNeighborRemoteRadioIP,
       "gnNeighborInBandXTable": gnNeighborInBandXTable,
       "gnNeighborInBandXEntry": gnNeighborInBandXEntry,
       "gnNeighborInBandXId": gnNeighborInBandXId,
       "gnNeighborInBandXIP": gnNeighborInBandXIP,
       "gnNeighborIpTable": gnNeighborIpTable,
       "gnNeighborIpEntry": gnNeighborIpEntry,
       "gnNeighborIpDetectMode": gnNeighborIpDetectMode,
       "gnNeighborIpAddress": gnNeighborIpAddress,
       "gnNeighborIpRemoteIfIndex": gnNeighborIpRemoteIfIndex,
       "gnNeighborIpRemoteType": gnNeighborIpRemoteType,
       "gnAgnSNMPCfg": gnAgnSNMPCfg,
       "gnAgnSNMPCfgTrapCommunity": gnAgnSNMPCfgTrapCommunity,
       "gnAgnSNMPCfgReadCommunity": gnAgnSNMPCfgReadCommunity,
       "gnAgnSNMPCfgWriteCommunity": gnAgnSNMPCfgWriteCommunity,
       "gnAgnPrvt": gnAgnPrvt,
       "gnAgnPrvtCmd": gnAgnPrvtCmd,
       "gnAgnPrvtCmdStat": gnAgnPrvtCmdStat,
       "gnSoftwareDrawerVersionTable": gnSoftwareDrawerVersionTable,
       "gnSoftwareDrawerVersionEntry": gnSoftwareDrawerVersionEntry,
       "gnSoftwareDrawerId": gnSoftwareDrawerId,
       "gnSoftwareDrawerVersionMUX": gnSoftwareDrawerVersionMUX,
       "gnSoftwareDrawerVersionMUXPostResetVersion": gnSoftwareDrawerVersionMUXPostResetVersion,
       "gnSoftwareDrawerVersionODU": gnSoftwareDrawerVersionODU,
       "gnSoftwareDrawerVersionODUPostResetVersion": gnSoftwareDrawerVersionODUPostResetVersion,
       "gnSoftwareDrawerVersionModemFile": gnSoftwareDrawerVersionModemFile,
       "gnSoftwareDrawerVersionModemFilePostResetVersion": gnSoftwareDrawerVersionModemFilePostResetVersion,
       "gnSoftwareDrawerVersionModemScript": gnSoftwareDrawerVersionModemScript,
       "gnSoftwareDrawerVersionModemScriptPostResetVersion": gnSoftwareDrawerVersionModemScriptPostResetVersion,
       "gnSoftwareDrawerVersionRfuFpgaVersion": gnSoftwareDrawerVersionRfuFpgaVersion,
       "gnAgnCurrentAlarm": gnAgnCurrentAlarm,
       "gnAgnCurrentAlarmLastChange": gnAgnCurrentAlarmLastChange,
       "gnAgnCurrentAlarmTable": gnAgnCurrentAlarmTable,
       "gnAgnCurrentAlarmEntry": gnAgnCurrentAlarmEntry,
       "gnAgnCurrentAlarmCounter": gnAgnCurrentAlarmCounter,
       "gnAgnCurrentAlarmSeverity": gnAgnCurrentAlarmSeverity,
       "gnAgnCurrentAlarmId": gnAgnCurrentAlarmId,
       "gnAgnCurrentAlarmIfIndex": gnAgnCurrentAlarmIfIndex,
       "gnAgnCurrentAlarmOrigin": gnAgnCurrentAlarmOrigin,
       "gnAgnCurrentAlarmUnit": gnAgnCurrentAlarmUnit,
       "gnAgnCurrentAlarmTrapID": gnAgnCurrentAlarmTrapID,
       "gnAgnCurrentAlarmTimeT": gnAgnCurrentAlarmTimeT,
       "gnAgnCurrentAlarmText": gnAgnCurrentAlarmText,
       "gnNMS": gnNMS,
       "gnApplicFileTable": gnApplicFileTable,
       "gnApplicFileEntry": gnApplicFileEntry,
       "gnApplicFileId": gnApplicFileId,
       "gnApplicFileName": gnApplicFileName,
       "gnApplicFileVersion": gnApplicFileVersion,
       "gnApplicFileCreateDate": gnApplicFileCreateDate,
       "gnApplicFileDownloadDate": gnApplicFileDownloadDate,
       "gnApplicFileType": gnApplicFileType,
       "gnApplicFileSubType": gnApplicFileSubType,
       "gnApplicFileFirmware": gnApplicFileFirmware,
       "gnApplicFileGeneralPurpose": gnApplicFileGeneralPurpose,
       "gnApplicFileSize": gnApplicFileSize,
       "gnApplicFileCompressed": gnApplicFileCompressed,
       "gnApplicFileDssSupport": gnApplicFileDssSupport,
       "gnApplicFileCrcSupport": gnApplicFileCrcSupport,
       "gnDiskCapacityData": gnDiskCapacityData,
       "gnDiskUsedspace": gnDiskUsedspace,
       "gnDiskFreespace": gnDiskFreespace,
       "gnUnits": gnUnits,
       "gnODU": gnODU,
       "gnOduCfgTable": gnOduCfgTable,
       "gnOduCfgEntry": gnOduCfgEntry,
       "gnOduCfgTransmitterFrequency": gnOduCfgTransmitterFrequency,
       "gnOduCfgRLPerfMonThresh1": gnOduCfgRLPerfMonThresh1,
       "gnOduCfgRLPerfMonThresh2": gnOduCfgRLPerfMonThresh2,
       "gnOduCfgATPCStatus": gnOduCfgATPCStatus,
       "gnOduCfgMUTEStatus": gnOduCfgMUTEStatus,
       "gnOduCfgAntennaType": gnOduCfgAntennaType,
       "gnOduCfgTransmitLevel": gnOduCfgTransmitLevel,
       "gnOduCfgRealTxFreqNumber": gnOduCfgRealTxFreqNumber,
       "gnOduCfgRealRxFreqNumber": gnOduCfgRealRxFreqNumber,
       "gnOduCfgMinTxFreqNumber": gnOduCfgMinTxFreqNumber,
       "gnOduCfgMaxTxFreqNumber": gnOduCfgMaxTxFreqNumber,
       "gnOduCfgMaxTxLevel": gnOduCfgMaxTxLevel,
       "gnOduCfgRefRsl": gnOduCfgRefRsl,
       "gnOduCfgForceRmtMuteTx": gnOduCfgForceRmtMuteTx,
       "gnOduCfgForceRmtMaxTx": gnOduCfgForceRmtMaxTx,
       "gnOduCfgTLPerfMonThresh1": gnOduCfgTLPerfMonThresh1,
       "gnOduCfgMinRxFreqNumber": gnOduCfgMinRxFreqNumber,
       "gnOduCfgMaxRxFreqNumber": gnOduCfgMaxRxFreqNumber,
       "gnOduCfgOduLoopSupport": gnOduCfgOduLoopSupport,
       "gnOduCfgOduModel": gnOduCfgOduModel,
       "gnOduCfgFreqPlanStandard": gnOduCfgFreqPlanStandard,
       "gnOduCfgFreqDevider": gnOduCfgFreqDevider,
       "gnOduStatusTable": gnOduStatusTable,
       "gnOduStatusEntry": gnOduStatusEntry,
       "gnOduStatusCelsiusTemp": gnOduStatusCelsiusTemp,
       "gnOduStatusFahrenheitTemp": gnOduStatusFahrenheitTemp,
       "gnOduStatusTransmitLevel": gnOduStatusTransmitLevel,
       "gnOduStatusReceiveLevel": gnOduStatusReceiveLevel,
       "gnOduStatusSynthesizerVCOLock": gnOduStatusSynthesizerVCOLock,
       "gnOduStatusPowerSupply": gnOduStatusPowerSupply,
       "gnOduStatusClearLoopTimer": gnOduStatusClearLoopTimer,
       "gnOduMonitor": gnOduMonitor,
       "gnOduMonCurrTable": gnOduMonCurrTable,
       "gnOduMonCurrEntry": gnOduMonCurrEntry,
       "gnOduMonCurrMinRL": gnOduMonCurrMinRL,
       "gnOduMonCurrMaxRL": gnOduMonCurrMaxRL,
       "gnOduMonCurrTLThresh1Exceed": gnOduMonCurrTLThresh1Exceed,
       "gnOduMonCurrRLThresh1Exceed": gnOduMonCurrRLThresh1Exceed,
       "gnOduMonCurrRLThresh2Exceed": gnOduMonCurrRLThresh2Exceed,
       "gnOduMonCurrDayMinRL": gnOduMonCurrDayMinRL,
       "gnOduMonCurrDayMaxRL": gnOduMonCurrDayMaxRL,
       "gnOduMonCurrDayTLThresh1Exceed": gnOduMonCurrDayTLThresh1Exceed,
       "gnOduMonCurrDayRLThresh1Exceed": gnOduMonCurrDayRLThresh1Exceed,
       "gnOduMonCurrDayRLThresh2Exceed": gnOduMonCurrDayRLThresh2Exceed,
       "gnOduMonCurrMinTL": gnOduMonCurrMinTL,
       "gnOduMonCurrMaxTL": gnOduMonCurrMaxTL,
       "gnOduMonCurrDayMinTL": gnOduMonCurrDayMinTL,
       "gnOduMonCurrDayMaxTL": gnOduMonCurrDayMaxTL,
       "gnOduMonIntervalTable": gnOduMonIntervalTable,
       "gnOduMonIntervalEntry": gnOduMonIntervalEntry,
       "gnOduMonIntervalIdx": gnOduMonIntervalIdx,
       "gnOduMonIntervalMinRL": gnOduMonIntervalMinRL,
       "gnOduMonIntervalMaxRL": gnOduMonIntervalMaxRL,
       "gnOduMonIntervalTLThresh1Exceed": gnOduMonIntervalTLThresh1Exceed,
       "gnOduMonIntervalEvent": gnOduMonIntervalEvent,
       "gnOduMonIntervalRLThresh1Exceed": gnOduMonIntervalRLThresh1Exceed,
       "gnOduMonIntervalRLThresh2Exceed": gnOduMonIntervalRLThresh2Exceed,
       "gnOduMonIntervalMinTL": gnOduMonIntervalMinTL,
       "gnOduMonIntervalMaxTL": gnOduMonIntervalMaxTL,
       "gnOduMonDayTable": gnOduMonDayTable,
       "gnOduMonDayEntry": gnOduMonDayEntry,
       "gnOduMonDayIdx": gnOduMonDayIdx,
       "gnOduMonDayMinRL": gnOduMonDayMinRL,
       "gnOduMonDayMaxRL": gnOduMonDayMaxRL,
       "gnOduMonDayTLThresh1Exceed": gnOduMonDayTLThresh1Exceed,
       "gnOduMonDayRLThresh1Exceed": gnOduMonDayRLThresh1Exceed,
       "gnOduMonDayRLThresh2Exceed": gnOduMonDayRLThresh2Exceed,
       "gnOduMonDayMinTL": gnOduMonDayMinTL,
       "gnOduMonDayMaxTL": gnOduMonDayMaxTL,
       "gnOduCfgXTable": gnOduCfgXTable,
       "gnOduCfgXEntry": gnOduCfgXEntry,
       "gnOduCfgXId": gnOduCfgXId,
       "gnOduCfgXTxFreqNumLocalRemote": gnOduCfgXTxFreqNumLocalRemote,
       "gnOduCfgXRLPerfMonThresh1": gnOduCfgXRLPerfMonThresh1,
       "gnOduCfgXRLPerfMonThresh2": gnOduCfgXRLPerfMonThresh2,
       "gnOduCfgXATPCStatus": gnOduCfgXATPCStatus,
       "gnOduCfgXMUTEStatus": gnOduCfgXMUTEStatus,
       "gnOduCfgXAntennaType": gnOduCfgXAntennaType,
       "gnOduCfgXTransmitLevel": gnOduCfgXTransmitLevel,
       "gnOduCfgXRealTxFreqNumber": gnOduCfgXRealTxFreqNumber,
       "gnOduCfgXRealRxFreqNumber": gnOduCfgXRealRxFreqNumber,
       "gnOduCfgXMinTxFreqNumber": gnOduCfgXMinTxFreqNumber,
       "gnOduCfgXMaxTxFreqNumber": gnOduCfgXMaxTxFreqNumber,
       "gnOduCfgXMaxTxLevel": gnOduCfgXMaxTxLevel,
       "gnOduCfgXRefRsl": gnOduCfgXRefRsl,
       "gnOduCfgXForceRmtMuteTx": gnOduCfgXForceRmtMuteTx,
       "gnOduCfgXForceRmtMaxTx": gnOduCfgXForceRmtMaxTx,
       "gnOduCfgXTLPerfMonThresh1": gnOduCfgXTLPerfMonThresh1,
       "gnOduCfgXOperation": gnOduCfgXOperation,
       "gnOduCfgXODUSerialNumber": gnOduCfgXODUSerialNumber,
       "gnOduCfgXChannelBandwidth": gnOduCfgXChannelBandwidth,
       "gnOduCfgXMinRxFreqNumber": gnOduCfgXMinRxFreqNumber,
       "gnOduCfgXMaxRxFreqNumber": gnOduCfgXMaxRxFreqNumber,
       "gnOduCfgXRxFreqNumLocalRemote": gnOduCfgXRxFreqNumLocalRemote,
       "gnOduCfgXOduLoopSupport": gnOduCfgXOduLoopSupport,
       "gnOduCfgXOduModel": gnOduCfgXOduModel,
       "gnOduCfgXFreqPlanStandard": gnOduCfgXFreqPlanStandard,
       "gnOduCfgXFreqDevider": gnOduCfgXFreqDevider,
       "gnOduCfgXLoopbackOption": gnOduCfgXLoopbackOption,
       "gnOduCfgXxpicClockMode": gnOduCfgXxpicClockMode,
       "gnOduCfgXUnfadedReferenceRsl": gnOduCfgXUnfadedReferenceRsl,
       "gnOduCfgXRfuMode": gnOduCfgXRfuMode,
       "gnOduCfgXRslRouteToConnector": gnOduCfgXRslRouteToConnector,
       "gnOduCfgXDelayCalibrationOperation": gnOduCfgXDelayCalibrationOperation,
       "gnOduCfgXDelayCalibrationValue": gnOduCfgXDelayCalibrationValue,
       "gnOduCfgXDelayCalibrationWgType": gnOduCfgXDelayCalibrationWgType,
       "gnOduCfgXOduLog": gnOduCfgXOduLog,
       "gnOduCfgXOduLogPeriod": gnOduCfgXOduLogPeriod,
       "gnOduCfgXXpiPerfMonThresh": gnOduCfgXXpiPerfMonThresh,
       "gnOduStatusXTable": gnOduStatusXTable,
       "gnOduStatusXEntry": gnOduStatusXEntry,
       "gnOduStatusXId": gnOduStatusXId,
       "gnOduStatusXCelsiusTemp": gnOduStatusXCelsiusTemp,
       "gnOduStatusXFahrenheitTemp": gnOduStatusXFahrenheitTemp,
       "gnOduStatusXTransmitLevel": gnOduStatusXTransmitLevel,
       "gnOduStatusXReceiveLevel": gnOduStatusXReceiveLevel,
       "gnOduStatusXSynthesizerVCOLock": gnOduStatusXSynthesizerVCOLock,
       "gnOduStatusXPowerSupply": gnOduStatusXPowerSupply,
       "gnOduStatusXIfcSupported": gnOduStatusXIfcSupported,
       "gnOduStatusXRslDiversity": gnOduStatusXRslDiversity,
       "gnOduStatusXRslCombined": gnOduStatusXRslCombined,
       "gnOduStatusXRfuAddress": gnOduStatusXRfuAddress,
       "gnOduStatusXMinTransmitLevel": gnOduStatusXMinTransmitLevel,
       "gnOduStatusXOduSWVer": gnOduStatusXOduSWVer,
       "gnOduStatusXOduSWPostVer": gnOduStatusXOduSWPostVer,
       "gnOduStatusXRfuFwVer": gnOduStatusXRfuFwVer,
       "gnOduStatusXValidIntervals": gnOduStatusXValidIntervals,
       "gnOduMonitorX": gnOduMonitorX,
       "gnOduMonCurrXTable": gnOduMonCurrXTable,
       "gnOduMonCurrXEntry": gnOduMonCurrXEntry,
       "gnOduMonCurrXId": gnOduMonCurrXId,
       "gnOduMonCurrXMinRL": gnOduMonCurrXMinRL,
       "gnOduMonCurrXMaxRL": gnOduMonCurrXMaxRL,
       "gnOduMonCurrXTLThresh1Exceed": gnOduMonCurrXTLThresh1Exceed,
       "gnOduMonCurrXRLThresh1Exceed": gnOduMonCurrXRLThresh1Exceed,
       "gnOduMonCurrXRLThresh2Exceed": gnOduMonCurrXRLThresh2Exceed,
       "gnOduMonCurrXDayMinRL": gnOduMonCurrXDayMinRL,
       "gnOduMonCurrXDayMaxRL": gnOduMonCurrXDayMaxRL,
       "gnOduMonCurrXDayTLThresh1Exceed": gnOduMonCurrXDayTLThresh1Exceed,
       "gnOduMonCurrXDayRLThresh1Exceed": gnOduMonCurrXDayRLThresh1Exceed,
       "gnOduMonCurrXDayRLThresh2Exceed": gnOduMonCurrXDayRLThresh2Exceed,
       "gnOduMonCurrXMinTL": gnOduMonCurrXMinTL,
       "gnOduMonCurrXMaxTL": gnOduMonCurrXMaxTL,
       "gnOduMonCurrXDayMinTL": gnOduMonCurrXDayMinTL,
       "gnOduMonCurrXDayMaxTL": gnOduMonCurrXDayMaxTL,
       "gnOduMonCurrXXpi": gnOduMonCurrXXpi,
       "gnOduMonCurrXMinXpi": gnOduMonCurrXMinXpi,
       "gnOduMonCurrXMaxXpi": gnOduMonCurrXMaxXpi,
       "gnOduMonCurrXDayMinXpi": gnOduMonCurrXDayMinXpi,
       "gnOduMonCurrXDayMaxXpi": gnOduMonCurrXDayMaxXpi,
       "gnOduMonCurrXXpiThreshExceed": gnOduMonCurrXXpiThreshExceed,
       "gnOduMonCurrXDayXpiThreshExceed": gnOduMonCurrXDayXpiThreshExceed,
       "gnOduMonCurrXMse": gnOduMonCurrXMse,
       "gnOduMonCurrXLastDayIDF": gnOduMonCurrXLastDayIDF,
       "gnOduMonIntervalXTable": gnOduMonIntervalXTable,
       "gnOduMonIntervalXEntry": gnOduMonIntervalXEntry,
       "gnOduMonIntervalXId": gnOduMonIntervalXId,
       "gnOduMonIntervalXIdx": gnOduMonIntervalXIdx,
       "gnOduMonIntervalXMinRL": gnOduMonIntervalXMinRL,
       "gnOduMonIntervalXMaxRL": gnOduMonIntervalXMaxRL,
       "gnOduMonIntervalXTLThresh1Exceed": gnOduMonIntervalXTLThresh1Exceed,
       "gnOduMonIntervalXEvent": gnOduMonIntervalXEvent,
       "gnOduMonIntervalXRLThresh1Exceed": gnOduMonIntervalXRLThresh1Exceed,
       "gnOduMonIntervalXRLThresh2Exceed": gnOduMonIntervalXRLThresh2Exceed,
       "gnOduMonIntervalXMinTL": gnOduMonIntervalXMinTL,
       "gnOduMonIntervalXMaxTL": gnOduMonIntervalXMaxTL,
       "gnOduMonIntervalXMinXpi": gnOduMonIntervalXMinXpi,
       "gnOduMonIntervalXMaxXpi": gnOduMonIntervalXMaxXpi,
       "gnOduMonIntervalXXpiThreshExceed": gnOduMonIntervalXXpiThreshExceed,
       "gnOduMonIntervalXIDF": gnOduMonIntervalXIDF,
       "gnOduMonDayXTable": gnOduMonDayXTable,
       "gnOduMonDayXEntry": gnOduMonDayXEntry,
       "gnOduMonDayXId": gnOduMonDayXId,
       "gnOduMonDayXIdx": gnOduMonDayXIdx,
       "gnOduMonDayXMinRL": gnOduMonDayXMinRL,
       "gnOduMonDayXMaxRL": gnOduMonDayXMaxRL,
       "gnOduMonDayXTLThresh1Exceed": gnOduMonDayXTLThresh1Exceed,
       "gnOduMonDayXRLThresh1Exceed": gnOduMonDayXRLThresh1Exceed,
       "gnOduMonDayXRLThresh2Exceed": gnOduMonDayXRLThresh2Exceed,
       "gnOduMonDayXMinTL": gnOduMonDayXMinTL,
       "gnOduMonDayXMaxTL": gnOduMonDayXMaxTL,
       "gnOduMonDayXMinXpi": gnOduMonDayXMinXpi,
       "gnOduMonDayXMaxXpi": gnOduMonDayXMaxXpi,
       "gnOduMonDayXXpiThreshExceed": gnOduMonDayXXpiThreshExceed,
       "gnOduMonDayXIDF": gnOduMonDayXIDF,
       "gnOduMonCurrDiversityXTable": gnOduMonCurrDiversityXTable,
       "gnOduMonCurrDiversityXEntry": gnOduMonCurrDiversityXEntry,
       "gnOduMonCurrDiversityXId": gnOduMonCurrDiversityXId,
       "gnOduMonCurrDiversityXMinRL": gnOduMonCurrDiversityXMinRL,
       "gnOduMonCurrDiversityXMaxRL": gnOduMonCurrDiversityXMaxRL,
       "gnOduMonCurrDiversityXRLThresh1Exceed": gnOduMonCurrDiversityXRLThresh1Exceed,
       "gnOduMonCurrDiversityXRLThresh2Exceed": gnOduMonCurrDiversityXRLThresh2Exceed,
       "gnOduMonCurrDiversityXDayMinRL": gnOduMonCurrDiversityXDayMinRL,
       "gnOduMonCurrDiversityXDayMaxRL": gnOduMonCurrDiversityXDayMaxRL,
       "gnOduMonCurrDiversityXDayRLThresh1Exceed": gnOduMonCurrDiversityXDayRLThresh1Exceed,
       "gnOduMonCurrDiversityXDayRLThresh2Exceed": gnOduMonCurrDiversityXDayRLThresh2Exceed,
       "gnOduMonIntervalDiversityXTable": gnOduMonIntervalDiversityXTable,
       "gnOduMonIntervalDiversityXEntry": gnOduMonIntervalDiversityXEntry,
       "gnOduMonIntervalDiversityXId": gnOduMonIntervalDiversityXId,
       "gnOduMonIntervalDiversityXIdx": gnOduMonIntervalDiversityXIdx,
       "gnOduMonIntervalDiversityXMinRL": gnOduMonIntervalDiversityXMinRL,
       "gnOduMonIntervalDiversityXMaxRL": gnOduMonIntervalDiversityXMaxRL,
       "gnOduMonIntervalDiversityXRLThresh1Exceed": gnOduMonIntervalDiversityXRLThresh1Exceed,
       "gnOduMonIntervalDiversityXRLThresh2Exceed": gnOduMonIntervalDiversityXRLThresh2Exceed,
       "gnOduMonDayDiversityXTable": gnOduMonDayDiversityXTable,
       "gnOduMonDayDiversityXEntry": gnOduMonDayDiversityXEntry,
       "gnOduMonDayDiversityXId": gnOduMonDayDiversityXId,
       "gnOduMonDayDiversityXIdx": gnOduMonDayDiversityXIdx,
       "gnOduMonDayDiversityXMinRL": gnOduMonDayDiversityXMinRL,
       "gnOduMonDayDiversityXMaxRL": gnOduMonDayDiversityXMaxRL,
       "gnOduMonDayDiversityXRLThresh1Exceed": gnOduMonDayDiversityXRLThresh1Exceed,
       "gnOduMonDayDiversityXRLThresh2Exceed": gnOduMonDayDiversityXRLThresh2Exceed,
       "gnOduMonCurrCombinedXTable": gnOduMonCurrCombinedXTable,
       "gnOduMonCurrCombinedXEntry": gnOduMonCurrCombinedXEntry,
       "gnOduMonCurrCombinedXId": gnOduMonCurrCombinedXId,
       "gnOduMonCurrCombinedXMinRL": gnOduMonCurrCombinedXMinRL,
       "gnOduMonCurrCombinedXMaxRL": gnOduMonCurrCombinedXMaxRL,
       "gnOduMonCurrCombinedXRLThresh1Exceed": gnOduMonCurrCombinedXRLThresh1Exceed,
       "gnOduMonCurrCombinedXRLThresh2Exceed": gnOduMonCurrCombinedXRLThresh2Exceed,
       "gnOduMonCurrCombinedXDayMinRL": gnOduMonCurrCombinedXDayMinRL,
       "gnOduMonCurrCombinedXDayMaxRL": gnOduMonCurrCombinedXDayMaxRL,
       "gnOduMonCurrCombinedXDayRLThresh1Exceed": gnOduMonCurrCombinedXDayRLThresh1Exceed,
       "gnOduMonCurrCombinedXDayRLThresh2Exceed": gnOduMonCurrCombinedXDayRLThresh2Exceed,
       "gnOduMonIntervalCombinedXTable": gnOduMonIntervalCombinedXTable,
       "gnOduMonIntervalCombinedXEntry": gnOduMonIntervalCombinedXEntry,
       "gnOduMonIntervalCombinedXId": gnOduMonIntervalCombinedXId,
       "gnOduMonIntervalCombinedXIdx": gnOduMonIntervalCombinedXIdx,
       "gnOduMonIntervalCombinedXMinRL": gnOduMonIntervalCombinedXMinRL,
       "gnOduMonIntervalCombinedXMaxRL": gnOduMonIntervalCombinedXMaxRL,
       "gnOduMonIntervalCombinedXRLThresh1Exceed": gnOduMonIntervalCombinedXRLThresh1Exceed,
       "gnOduMonIntervalCombinedXRLThresh2Exceed": gnOduMonIntervalCombinedXRLThresh2Exceed,
       "gnOduMonDayCombinedXTable": gnOduMonDayCombinedXTable,
       "gnOduMonDayCombinedXEntry": gnOduMonDayCombinedXEntry,
       "gnOduMonDayCombinedXId": gnOduMonDayCombinedXId,
       "gnOduMonDayCombinedXIdx": gnOduMonDayCombinedXIdx,
       "gnOduMonDayCombinedXMinRL": gnOduMonDayCombinedXMinRL,
       "gnOduMonDayCombinedXMaxRL": gnOduMonDayCombinedXMaxRL,
       "gnOduMonDayCombinedXRLThresh1Exceed": gnOduMonDayCombinedXRLThresh1Exceed,
       "gnOduMonDayCombinedXRLThresh2Exceed": gnOduMonDayCombinedXRLThresh2Exceed,
       "gnIDU": gnIDU,
       "gnMdm": gnMdm,
       "gnMdmStatTable": gnMdmStatTable,
       "gnMdmStatEntry": gnMdmStatEntry,
       "gnMdmModStatus": gnMdmModStatus,
       "gnMdmDemodStatus": gnMdmDemodStatus,
       "gnMdmDefectBlocks": gnMdmDefectBlocks,
       "gnMdmBytesCorrected": gnMdmBytesCorrected,
       "gnMdmClearBC": gnMdmClearBC,
       "gnMdmStatXTable": gnMdmStatXTable,
       "gnMdmStatXEntry": gnMdmStatXEntry,
       "gnMdmStatXId": gnMdmStatXId,
       "gnMdmStatXStandardOrg": gnMdmStatXStandardOrg,
       "gnMdmStatXRemoteConnection": gnMdmStatXRemoteConnection,
       "gnMdmStatXModemType": gnMdmStatXModemType,
       "gnMdmStatXModemWorkTime": gnMdmStatXModemWorkTime,
       "gnMdmStatXModemSerialNumber": gnMdmStatXModemSerialNumber,
       "gnMdmStatXModemFWVer": gnMdmStatXModemFWVer,
       "gnMdmStatXModemFWPostVer": gnMdmStatXModemFWPostVer,
       "gnMdmStatXModemScriptVer": gnMdmStatXModemScriptVer,
       "gnMdmStatXModemScriptPostVer": gnMdmStatXModemScriptPostVer,
       "gnMdmStatXIfLoopbackTimeOut": gnMdmStatXIfLoopbackTimeOut,
       "gnMdmStatXBoardType": gnMdmStatXBoardType,
       "gnMdmStatXDefectedBlocks": gnMdmStatXDefectedBlocks,
       "gnMdmStatXScriptType": gnMdmStatXScriptType,
       "gnMdmStatXAcmValidIntervals": gnMdmStatXAcmValidIntervals,
       "gnMdmStatXAcmSignalValid": gnMdmStatXAcmSignalValid,
       "gnMdmStatXTxConstellation": gnMdmStatXTxConstellation,
       "gnMdmStatXRxConstellation": gnMdmStatXRxConstellation,
       "gnMdmCfgTable": gnMdmCfgTable,
       "gnMdmCfgEntry": gnMdmCfgEntry,
       "gnMdmCfgId": gnMdmCfgId,
       "gnMdmCfgDiversityMode": gnMdmCfgDiversityMode,
       "gnMdmCfgXTable": gnMdmCfgXTable,
       "gnMdmCfgXEntry": gnMdmCfgXEntry,
       "gnMdmCfgXId": gnMdmCfgXId,
       "gnMdmCfgXLatencyType": gnMdmCfgXLatencyType,
       "gnMdmCfgXLinkId": gnMdmCfgXLinkId,
       "gnMdmCfgXRadioSide": gnMdmCfgXRadioSide,
       "gnMdmCfgXMrmcConf": gnMdmCfgXMrmcConf,
       "gnMdmCfgXIfLoopback": gnMdmCfgXIfLoopback,
       "gnMdmCfgXHwReset": gnMdmCfgXHwReset,
       "gnMdmCfgXPrbsTest": gnMdmCfgXPrbsTest,
       "gnMdmCfgXClearCounters": gnMdmCfgXClearCounters,
       "gnMdmCfgXAcmOperationMode": gnMdmCfgXAcmOperationMode,
       "gnMdmCfgXAcmMaximumConstellation": gnMdmCfgXAcmMaximumConstellation,
       "gnMdmAcmStatXTable": gnMdmAcmStatXTable,
       "gnMdmAcmStatXEntry": gnMdmAcmStatXEntry,
       "gnMdmAcmStatXId": gnMdmAcmStatXId,
       "gnMdmAcmStatXQamId": gnMdmAcmStatXQamId,
       "gnMdmAcmStatXRoundedThroughput": gnMdmAcmStatXRoundedThroughput,
       "gnMdmAcmStatXSupportedThroughput": gnMdmAcmStatXSupportedThroughput,
       "gnMdmMonitorX": gnMdmMonitorX,
       "gnMdmAcmMonitorX": gnMdmAcmMonitorX,
       "gnMdmAcmMonCurrXTable": gnMdmAcmMonCurrXTable,
       "gnMdmAcmMonCurrXEntry": gnMdmAcmMonCurrXEntry,
       "gnMdmAcmMonCurrXId": gnMdmAcmMonCurrXId,
       "gnMdmAcmMonCurrXMinConstellation": gnMdmAcmMonCurrXMinConstellation,
       "gnMdmAcmMonCurrXMaxConstellation": gnMdmAcmMonCurrXMaxConstellation,
       "gnMdmAcmMonCurrXIDF": gnMdmAcmMonCurrXIDF,
       "gnMdmAcmMonCurrXDayMinConstellation": gnMdmAcmMonCurrXDayMinConstellation,
       "gnMdmAcmMonCurrXDayMaxConstellation": gnMdmAcmMonCurrXDayMaxConstellation,
       "gnMdmAcmMonCurrXDayIDF": gnMdmAcmMonCurrXDayIDF,
       "gnMdmAcmMonIntervalXTable": gnMdmAcmMonIntervalXTable,
       "gnMdmAcmMonIntervalXEntry": gnMdmAcmMonIntervalXEntry,
       "gnMdmAcmMonIntervalXId": gnMdmAcmMonIntervalXId,
       "gnMdmAcmMonIntervalXIdx": gnMdmAcmMonIntervalXIdx,
       "gnMdmAcmMonIntervalXMinConstellation": gnMdmAcmMonIntervalXMinConstellation,
       "gnMdmAcmMonIntervalXMaxConstellation": gnMdmAcmMonIntervalXMaxConstellation,
       "gnMdmAcmMonIntervalXIDF": gnMdmAcmMonIntervalXIDF,
       "gnMdmAcmMonDayXTable": gnMdmAcmMonDayXTable,
       "gnMdmAcmMonDayXEntry": gnMdmAcmMonDayXEntry,
       "gnMdmAcmMonDayXId": gnMdmAcmMonDayXId,
       "gnMdmAcmMonDayXIdx": gnMdmAcmMonDayXIdx,
       "gnMdmAcmMonDayXMinConstellation": gnMdmAcmMonDayXMinConstellation,
       "gnMdmAcmMonDayXMaxConstellation": gnMdmAcmMonDayXMaxConstellation,
       "gnMdmAcmMonDayXIDF": gnMdmAcmMonDayXIDF,
       "gnSpi": gnSpi,
       "gnSpiCfgTable": gnSpiCfgTable,
       "gnSpiCfgEntry": gnSpiCfgEntry,
       "gnSpiCfgConnector": gnSpiCfgConnector,
       "gnMux": gnMux,
       "gnRstCfgTable": gnRstCfgTable,
       "gnRstCfgEntry": gnRstCfgEntry,
       "gnRstCfgTransmittedJ0": gnRstCfgTransmittedJ0,
       "gnRstCfgExpectedJ0": gnRstCfgExpectedJ0,
       "gnRstCfgTransparencyJ0": gnRstCfgTransparencyJ0,
       "gnRstCfgRSTAISMode": gnRstCfgRSTAISMode,
       "gnRstCfgRstEXCThresh": gnRstCfgRstEXCThresh,
       "gnRstCfgRstSDThresh": gnRstCfgRstSDThresh,
       "gnRstCfgTransparencyE1": gnRstCfgTransparencyE1,
       "gnRstCfgTransparencyF1": gnRstCfgTransparencyF1,
       "gnRstCfgTransparencyUnscrambled": gnRstCfgTransparencyUnscrambled,
       "gnRstCfgMngByteLocation": gnRstCfgMngByteLocation,
       "gnRstCfgE1waysideChannel": gnRstCfgE1waysideChannel,
       "gnRstCfgTransparencyDCCR": gnRstCfgTransparencyDCCR,
       "gnRstCfgTransparencyB1Chan": gnRstCfgTransparencyB1Chan,
       "gnRstCfgTestActivate": gnRstCfgTestActivate,
       "gnRstCfgLoopbackOption": gnRstCfgLoopbackOption,
       "gnRstStatTable": gnRstStatTable,
       "gnRstStatEntry": gnRstStatEntry,
       "gnRstStatReceivedJ0": gnRstStatReceivedJ0,
       "gnRstStatBERCur": gnRstStatBERCur,
       "gnRstStatStatus": gnRstStatStatus,
       "gnRstStatClearLoopTimer": gnRstStatClearLoopTimer,
       "gnRstMon": gnRstMon,
       "gnRstMonCurrTable": gnRstMonCurrTable,
       "gnRstMonCurrEntry": gnRstMonCurrEntry,
       "gnRstMonCurrBBE": gnRstMonCurrBBE,
       "gnRstMonCurrUAS": gnRstMonCurrUAS,
       "gnRstMonCurrLastDayES": gnRstMonCurrLastDayES,
       "gnRstMonCurrLastDaySES": gnRstMonCurrLastDaySES,
       "gnRstMonCurrLastDayBBE": gnRstMonCurrLastDayBBE,
       "gnRstMonCurrLastDayUAS": gnRstMonCurrLastDayUAS,
       "gnRstMonCurrLastDayOFS": gnRstMonCurrLastDayOFS,
       "gnRstMonCurrLastDayIDF": gnRstMonCurrLastDayIDF,
       "gnRstMonIntervalTable": gnRstMonIntervalTable,
       "gnRstMonIntervalEntry": gnRstMonIntervalEntry,
       "gnRstMonIntervalIdx": gnRstMonIntervalIdx,
       "gnRstMonIntervalBBE": gnRstMonIntervalBBE,
       "gnRstMonIntervalUAS": gnRstMonIntervalUAS,
       "gnRstMonIntervalIDF": gnRstMonIntervalIDF,
       "gnRstMonDayTable": gnRstMonDayTable,
       "gnRstMonDayEntry": gnRstMonDayEntry,
       "gnRstMonDayIdx": gnRstMonDayIdx,
       "gnRstMonDayES": gnRstMonDayES,
       "gnRstMonDaySES": gnRstMonDaySES,
       "gnRstMonDayBBE": gnRstMonDayBBE,
       "gnRstMonDayUAS": gnRstMonDayUAS,
       "gnRstMonDayOFS": gnRstMonDayOFS,
       "gnRstMonDayIDF": gnRstMonDayIDF,
       "gnMstCfgTable": gnMstCfgTable,
       "gnMstCfgEntry": gnMstCfgEntry,
       "gnMstCfgEXCThresh": gnMstCfgEXCThresh,
       "gnMstCfgSDThresh": gnMstCfgSDThresh,
       "gnMstStatTable": gnMstStatTable,
       "gnMstStatEntry": gnMstStatEntry,
       "gnMstStatReceivedS1": gnMstStatReceivedS1,
       "gnMstStatStatus": gnMstStatStatus,
       "gnMstStatTransmitS1": gnMstStatTransmitS1,
       "gnMstStatCurrentBer": gnMstStatCurrentBer,
       "gnMstStatReceivedK1": gnMstStatReceivedK1,
       "gnMstStatReceivedK2": gnMstStatReceivedK2,
       "gnMstStatTransmitK1": gnMstStatTransmitK1,
       "gnMstStatTransmitK2": gnMstStatTransmitK2,
       "gnMstMon": gnMstMon,
       "gnMstMonCurrTable": gnMstMonCurrTable,
       "gnMstMonCurrEntry": gnMstMonCurrEntry,
       "gnMstMonCurrBBE": gnMstMonCurrBBE,
       "gnMstMonCurrUAS": gnMstMonCurrUAS,
       "gnMstMonCurrLastDayES": gnMstMonCurrLastDayES,
       "gnMstMonCurrLastDaySES": gnMstMonCurrLastDaySES,
       "gnMstMonCurrLastDayBBE": gnMstMonCurrLastDayBBE,
       "gnMstMonCurrLastDayUAS": gnMstMonCurrLastDayUAS,
       "gnMstMonIntervalTable": gnMstMonIntervalTable,
       "gnMstMonIntervalEntry": gnMstMonIntervalEntry,
       "gnMstMonIntervalIdx": gnMstMonIntervalIdx,
       "gnMstMonIntervalBBE": gnMstMonIntervalBBE,
       "gnMstMonIntervalUAS": gnMstMonIntervalUAS,
       "gnMstMonDayTable": gnMstMonDayTable,
       "gnMstMonDayEntry": gnMstMonDayEntry,
       "gnMstMonDayIdx": gnMstMonDayIdx,
       "gnMstMonDayES": gnMstMonDayES,
       "gnMstMonDaySES": gnMstMonDaySES,
       "gnMstMonDayBBE": gnMstMonDayBBE,
       "gnMstMonDayUAS": gnMstMonDayUAS,
       "gnMstFarEndMonCurrTable": gnMstFarEndMonCurrTable,
       "gnMstFarEndMonCurrEntry": gnMstFarEndMonCurrEntry,
       "gnMstFarEndMonCurrBBE": gnMstFarEndMonCurrBBE,
       "gnMstFarEndMonCurrUAS": gnMstFarEndMonCurrUAS,
       "gnMstFarEndMonCurrLastDayES": gnMstFarEndMonCurrLastDayES,
       "gnMstFarEndMonCurrLastDaySES": gnMstFarEndMonCurrLastDaySES,
       "gnMstFarEndMonCurrLastDayBBE": gnMstFarEndMonCurrLastDayBBE,
       "gnMstFarEndMonCurrLastDayUAS": gnMstFarEndMonCurrLastDayUAS,
       "gnMstFarEndMonIntervalTable": gnMstFarEndMonIntervalTable,
       "gnMstFarEndMonIntervalEntry": gnMstFarEndMonIntervalEntry,
       "gnMstFarEndMonIntervalIdx": gnMstFarEndMonIntervalIdx,
       "gnMstFarEndMonIntervalBBE": gnMstFarEndMonIntervalBBE,
       "gnMstFarEndMonIntervalUAS": gnMstFarEndMonIntervalUAS,
       "gnMstFarEndMonDayTable": gnMstFarEndMonDayTable,
       "gnMstFarEndMonDayEntry": gnMstFarEndMonDayEntry,
       "gnMstFarEndMonDayIdx": gnMstFarEndMonDayIdx,
       "gnMstFarEndMonDayES": gnMstFarEndMonDayES,
       "gnMstFarEndMonDaySES": gnMstFarEndMonDaySES,
       "gnMstFarEndMonDayBBE": gnMstFarEndMonDayBBE,
       "gnMstFarEndMonDayUAS": gnMstFarEndMonDayUAS,
       "gnHptCfgTable": gnHptCfgTable,
       "gnHptCfgEntry": gnHptCfgEntry,
       "gnHptCfgTransmittedJ1": gnHptCfgTransmittedJ1,
       "gnHptCfgExpectedJ1": gnHptCfgExpectedJ1,
       "gnHptCfgMismatchJ1": gnHptCfgMismatchJ1,
       "gnHptCfgTransparencyJ1": gnHptCfgTransparencyJ1,
       "gnHptCfgEXCThresh": gnHptCfgEXCThresh,
       "gnHptCfgSDThresh": gnHptCfgSDThresh,
       "gnHptCfgTug3Structure1": gnHptCfgTug3Structure1,
       "gnHptCfgTug3Structure2": gnHptCfgTug3Structure2,
       "gnHptCfgTug3Structure3": gnHptCfgTug3Structure3,
       "gnHptCfgSignalLabelMismatch": gnHptCfgSignalLabelMismatch,
       "gnHptCfgTrailPT1": gnHptCfgTrailPT1,
       "gnHptCfgTrailPT2": gnHptCfgTrailPT2,
       "gnHptCfgTrailPT3": gnHptCfgTrailPT3,
       "gnHptStatTable": gnHptStatTable,
       "gnHptStatEntry": gnHptStatEntry,
       "gnHptStatReceivedJ1": gnHptStatReceivedJ1,
       "gnHptStatStatus": gnHptStatStatus,
       "gnHptStatCurrentBer": gnHptStatCurrentBer,
       "gnHptStatFarEndCurrentBer": gnHptStatFarEndCurrentBer,
       "gnHptStatReceivedSignalLabel": gnHptStatReceivedSignalLabel,
       "gnHptMon": gnHptMon,
       "gnHptMonCurrTable": gnHptMonCurrTable,
       "gnHptMonCurrEntry": gnHptMonCurrEntry,
       "gnHptMonCurrBBE": gnHptMonCurrBBE,
       "gnHptMonCurrUAS": gnHptMonCurrUAS,
       "gnHptMonCurrLastDayES": gnHptMonCurrLastDayES,
       "gnHptMonCurrLastDaySES": gnHptMonCurrLastDaySES,
       "gnHptMonCurrLastDayBBE": gnHptMonCurrLastDayBBE,
       "gnHptMonCurrLastDayUAS": gnHptMonCurrLastDayUAS,
       "gnHptMonIntervalTable": gnHptMonIntervalTable,
       "gnHptMonIntervalEntry": gnHptMonIntervalEntry,
       "gnHptMonIntervalIdx": gnHptMonIntervalIdx,
       "gnHptMonIntervalBBE": gnHptMonIntervalBBE,
       "gnHptMonIntervalUAS": gnHptMonIntervalUAS,
       "gnHptMonDayTable": gnHptMonDayTable,
       "gnHptMonDayEntry": gnHptMonDayEntry,
       "gnHptMonDayIdx": gnHptMonDayIdx,
       "gnHptMonDayES": gnHptMonDayES,
       "gnHptMonDaySES": gnHptMonDaySES,
       "gnHptMonDayBBE": gnHptMonDayBBE,
       "gnHptMonDayUAS": gnHptMonDayUAS,
       "gnHptFarEndMonCurrTable": gnHptFarEndMonCurrTable,
       "gnHptFarEndMonCurrEntry": gnHptFarEndMonCurrEntry,
       "gnHptFarEndMonCurrBBE": gnHptFarEndMonCurrBBE,
       "gnHptFarEndMonCurrUAS": gnHptFarEndMonCurrUAS,
       "gnHptFarEndMonCurrLastDayES": gnHptFarEndMonCurrLastDayES,
       "gnHptFarEndMonCurrLastDaySES": gnHptFarEndMonCurrLastDaySES,
       "gnHptFarEndMonCurrLastDayBBE": gnHptFarEndMonCurrLastDayBBE,
       "gnHptFarEndMonCurrLastDayUAS": gnHptFarEndMonCurrLastDayUAS,
       "gnHptFarEndMonIntervalTable": gnHptFarEndMonIntervalTable,
       "gnHptFarEndMonIntervalEntry": gnHptFarEndMonIntervalEntry,
       "gnHptFarEndMonIntervalIdx": gnHptFarEndMonIntervalIdx,
       "gnHptFarEndMonIntervalBBE": gnHptFarEndMonIntervalBBE,
       "gnHptFarEndMonIntervalUAS": gnHptFarEndMonIntervalUAS,
       "gnHptFarEndMonDayTable": gnHptFarEndMonDayTable,
       "gnHptFarEndMonDayEntry": gnHptFarEndMonDayEntry,
       "gnHptFarEndMonDayIdx": gnHptFarEndMonDayIdx,
       "gnHptFarEndMonDayES": gnHptFarEndMonDayES,
       "gnHptFarEndMonDaySES": gnHptFarEndMonDaySES,
       "gnHptFarEndMonDayBBE": gnHptFarEndMonDayBBE,
       "gnHptFarEndMonDayUAS": gnHptFarEndMonDayUAS,
       "gnLptCfgTable": gnLptCfgTable,
       "gnLptCfgEntry": gnLptCfgEntry,
       "gnLptCfgEXCThresh": gnLptCfgEXCThresh,
       "gnLptCfgSDThresh": gnLptCfgSDThresh,
       "gnLptStatTable": gnLptStatTable,
       "gnLptStatEntry": gnLptStatEntry,
       "gnLptStatReceivedJ2": gnLptStatReceivedJ2,
       "gnLptStatStatus": gnLptStatStatus,
       "gnLptStatProtectionMode": gnLptStatProtectionMode,
       "gnLptStatCurrentBer": gnLptStatCurrentBer,
       "gnLptStatFarEndCurrentBer": gnLptStatFarEndCurrentBer,
       "gnLptStatReceivedSignalLabel": gnLptStatReceivedSignalLabel,
       "gnLptStatKLM": gnLptStatKLM,
       "gnLptMon": gnLptMon,
       "gnLptMonCurrTable": gnLptMonCurrTable,
       "gnLptMonCurrEntry": gnLptMonCurrEntry,
       "gnLptMonCurrBBE": gnLptMonCurrBBE,
       "gnLptMonCurrUAS": gnLptMonCurrUAS,
       "gnLptMonCurrLastDayES": gnLptMonCurrLastDayES,
       "gnLptMonCurrLastDaySES": gnLptMonCurrLastDaySES,
       "gnLptMonCurrLastDayBBE": gnLptMonCurrLastDayBBE,
       "gnLptMonCurrLastDayUAS": gnLptMonCurrLastDayUAS,
       "gnLptMonIntervalTable": gnLptMonIntervalTable,
       "gnLptMonIntervalEntry": gnLptMonIntervalEntry,
       "gnLptMonIntervalIdx": gnLptMonIntervalIdx,
       "gnLptMonIntervalBBE": gnLptMonIntervalBBE,
       "gnLptMonIntervalUAS": gnLptMonIntervalUAS,
       "gnLptMonDayTable": gnLptMonDayTable,
       "gnLptMonDayEntry": gnLptMonDayEntry,
       "gnLptMonDayIdx": gnLptMonDayIdx,
       "gnLptMonDayES": gnLptMonDayES,
       "gnLptMonDaySES": gnLptMonDaySES,
       "gnLptMonDayBBE": gnLptMonDayBBE,
       "gnLptMonDayUAS": gnLptMonDayUAS,
       "gnLptFarEndMonCurrTable": gnLptFarEndMonCurrTable,
       "gnLptFarEndMonCurrEntry": gnLptFarEndMonCurrEntry,
       "gnLptFarEndMonCurrBBE": gnLptFarEndMonCurrBBE,
       "gnLptFarEndMonCurrUAS": gnLptFarEndMonCurrUAS,
       "gnLptFarEndMonCurrLastDayES": gnLptFarEndMonCurrLastDayES,
       "gnLptFarEndMonCurrLastDaySES": gnLptFarEndMonCurrLastDaySES,
       "gnLptFarEndMonCurrLastDayBBE": gnLptFarEndMonCurrLastDayBBE,
       "gnLptFarEndMonCurrLastDayUAS": gnLptFarEndMonCurrLastDayUAS,
       "gnLptFarEndMonIntervalTable": gnLptFarEndMonIntervalTable,
       "gnLptFarEndMonIntervalEntry": gnLptFarEndMonIntervalEntry,
       "gnLptFarEndMonIntervalIdx": gnLptFarEndMonIntervalIdx,
       "gnLptFarEndMonIntervalBBE": gnLptFarEndMonIntervalBBE,
       "gnLptFarEndMonIntervalUAS": gnLptFarEndMonIntervalUAS,
       "gnLptFarEndMonDayTable": gnLptFarEndMonDayTable,
       "gnLptFarEndMonDayEntry": gnLptFarEndMonDayEntry,
       "gnLptFarEndMonDayIdx": gnLptFarEndMonDayIdx,
       "gnLptFarEndMonDayES": gnLptFarEndMonDayES,
       "gnLptFarEndMonDaySES": gnLptFarEndMonDaySES,
       "gnLptFarEndMonDayBBE": gnLptFarEndMonDayBBE,
       "gnLptFarEndMonDayUAS": gnLptFarEndMonDayUAS,
       "gnMuxCfgXTable": gnMuxCfgXTable,
       "gnMuxCfgXEntry": gnMuxCfgXEntry,
       "gnMuxCfgXId": gnMuxCfgXId,
       "gnMuxCfgXWsAdmin": gnMuxCfgXWsAdmin,
       "gnMuxCfgXWsLoopback": gnMuxCfgXWsLoopback,
       "gnMuxCfgXHwReset": gnMuxCfgXHwReset,
       "gnMUXCfgXTempLicenseEnable": gnMUXCfgXTempLicenseEnable,
       "gnMUXCfgXTempLicenseTimer": gnMUXCfgXTempLicenseTimer,
       "gnMuxStatXTable": gnMuxStatXTable,
       "gnMuxStatXEntry": gnMuxStatXEntry,
       "gnMuxStatXId": gnMuxStatXId,
       "gnMuxStatXMuxSerialNumber": gnMuxStatXMuxSerialNumber,
       "gnMuxStatXIfLeds": gnMuxStatXIfLeds,
       "gnMuxStatXNumOfIfOnClass1": gnMuxStatXNumOfIfOnClass1,
       "gnMuxStatXNumOfIfOnClass2": gnMuxStatXNumOfIfOnClass2,
       "gnMuxStatXNumOfIfOnClass3": gnMuxStatXNumOfIfOnClass3,
       "gnMuxStatXAesAdmin": gnMuxStatXAesAdmin,
       "gnMuxStatXMuxFWVer": gnMuxStatXMuxFWVer,
       "gnMuxStatXMuxFWPostVer": gnMuxStatXMuxFWPostVer,
       "gnMuxStatXBoardConnector": gnMuxStatXBoardConnector,
       "gnMuxStatXBoardType": gnMuxStatXBoardType,
       "gnAux": gnAux,
       "gnAuxGeneral": gnAuxGeneral,
       "gnAuxGeneralTable": gnAuxGeneralTable,
       "gnAuxGeneralEntry": gnAuxGeneralEntry,
       "gnAuxGeneralId": gnAuxGeneralId,
       "gnAuxGeneralSyncIdcDataBase": gnAuxGeneralSyncIdcDataBase,
       "gnWsc": gnWsc,
       "gnWscCfgTable": gnWscCfgTable,
       "gnWscCfgEntry": gnWscCfgEntry,
       "gnWscCfgId": gnWscCfgId,
       "gnWscCfgChNumber": gnWscCfgChNumber,
       "gnWscCfgRouting": gnWscCfgRouting,
       "gnWscCfgEnable": gnWscCfgEnable,
       "gnWscCfgBitRate": gnWscCfgBitRate,
       "gnWscCfgType": gnWscCfgType,
       "gnWscStatTable": gnWscStatTable,
       "gnWscStatEntry": gnWscStatEntry,
       "gnWscStatId": gnWscStatId,
       "gnWscStatChNumber": gnWscStatChNumber,
       "gnWscStatBitRateSupport": gnWscStatBitRateSupport,
       "gnEow": gnEow,
       "gnEowCfgTable": gnEowCfgTable,
       "gnEowCfgEntry": gnEowCfgEntry,
       "gnEowCfgId": gnEowCfgId,
       "gnEowCfgEowLeftEnable": gnEowCfgEowLeftEnable,
       "gnEowCfgEowRightEnable": gnEowCfgEowRightEnable,
       "gnEowCfgEowCascadeEnable": gnEowCfgEowCascadeEnable,
       "gnEowStatTable": gnEowStatTable,
       "gnEowStatEntry": gnEowStatEntry,
       "gnEowStatId": gnEowStatId,
       "gnEowStatEowLeftSupport": gnEowStatEowLeftSupport,
       "gnEowStatEowRightSupport": gnEowStatEowRightSupport,
       "gnUc": gnUc,
       "gnUcCfgTable": gnUcCfgTable,
       "gnUcCfgEntry": gnUcCfgEntry,
       "gnUcCfgId": gnUcCfgId,
       "gnUcCfgChNumber": gnUcCfgChNumber,
       "gnUcCfgRouting": gnUcCfgRouting,
       "gnUcCfgEnable": gnUcCfgEnable,
       "gnUcCfgType": gnUcCfgType,
       "gnUcCfgLoopback": gnUcCfgLoopback,
       "gnUcStatTable": gnUcStatTable,
       "gnUcStatEntry": gnUcStatEntry,
       "gnUcStatId": gnUcStatId,
       "gnUcStatLeftMaxRouteChannel": gnUcStatLeftMaxRouteChannel,
       "gnUcStatRightMaxRouteChannel": gnUcStatRightMaxRouteChannel,
       "gnProtect": gnProtect,
       "gnProtectCfgTable": gnProtectCfgTable,
       "gnProtectCfgEntry": gnProtectCfgEntry,
       "gnProtectCfgId": gnProtectCfgId,
       "gnProtectCfgSwitchRequest": gnProtectCfgSwitchRequest,
       "gnProtectCfgBERSwitch": gnProtectCfgBERSwitch,
       "gnProtectCfgExtInSwitch": gnProtectCfgExtInSwitch,
       "gnProtectCfgOption": gnProtectCfgOption,
       "gnProtectCfgUserCommand": gnProtectCfgUserCommand,
       "gnProtectCfgType": gnProtectCfgType,
       "gnProtectCfgProtectionLockout": gnProtectCfgProtectionLockout,
       "gnProtectCfgSdBERSwitch": gnProtectCfgSdBERSwitch,
       "gnProtectCfgMultiRadioBlock": gnProtectCfgMultiRadioBlock,
       "gnProtectUnitMode": gnProtectUnitMode,
       "gnHitLessCfgTable": gnHitLessCfgTable,
       "gnHitLessCfgEntry": gnHitLessCfgEntry,
       "gnHitLessCfgId": gnHitLessCfgId,
       "gnHitLessCfgSwitchEnable": gnHitLessCfgSwitchEnable,
       "gnHitLessCfgDiversityType": gnHitLessCfgDiversityType,
       "gnHitLessCfgSwitchingMode": gnHitLessCfgSwitchingMode,
       "gnHitLessCfgRevertTime": gnHitLessCfgRevertTime,
       "gnHitLessCfgManualSwitch": gnHitLessCfgManualSwitch,
       "gnHitLessCfgEventCounterCommand": gnHitLessCfgEventCounterCommand,
       "gnHitLessCfgSwitchLock": gnHitLessCfgSwitchLock,
       "gnHitLessStatTable": gnHitLessStatTable,
       "gnHitLessStatEntry": gnHitLessStatEntry,
       "gnHitLessStatId": gnHitLessStatId,
       "gnHitLessStatReceiverStatus": gnHitLessStatReceiverStatus,
       "gnHitLessStatModeStatus": gnHitLessStatModeStatus,
       "gnHitLessStatEventCounter": gnHitLessStatEventCounter,
       "gnHitLessStatAlarmStatus": gnHitLessStatAlarmStatus,
       "gnTribStmProtectCfg": gnTribStmProtectCfg,
       "gnTribStmProtectType": gnTribStmProtectType,
       "gnTribStmMspConnect": gnTribStmMspConnect,
       "gnTribStmMspType": gnTribStmMspType,
       "gnTribStmMspRevertiveMode": gnTribStmMspRevertiveMode,
       "gnTribStmMspProtectRole": gnTribStmMspProtectRole,
       "gnTribStmMspWaitToRestoreTime": gnTribStmMspWaitToRestoreTime,
       "gnTribStmMspUserCommand": gnTribStmMspUserCommand,
       "gnTribStmProtectStat": gnTribStmProtectStat,
       "gnTribStmProtectCurrentState": gnTribStmProtectCurrentState,
       "gnTribStmProtectCableStatus": gnTribStmProtectCableStatus,
       "gnProtectXTable": gnProtectXTable,
       "gnProtectXEntry": gnProtectXEntry,
       "gnProtectXId": gnProtectXId,
       "gnProtectXProtectUnitMode": gnProtectXProtectUnitMode,
       "gnProtectXMultiRadioOhRadioSource": gnProtectXMultiRadioOhRadioSource,
       "gnLinkGroups": gnLinkGroups,
       "topologiesOptionsTable": topologiesOptionsTable,
       "topologiesOptionsEntry": topologiesOptionsEntry,
       "topologiesOptionsGroupTopology": topologiesOptionsGroupTopology,
       "topologiesOptionsMembersCarriers": topologiesOptionsMembersCarriers,
       "topologiesOptionsProtectingCarriers": topologiesOptionsProtectingCarriers,
       "topologiesOptionsName": topologiesOptionsName,
       "linkGroupingTable": linkGroupingTable,
       "linkGroupingEntry": linkGroupingEntry,
       "linkGroupingGroupId": linkGroupingGroupId,
       "linkGroupingGroupAdmin": linkGroupingGroupAdmin,
       "linkGroupingGroupTopology": linkGroupingGroupTopology,
       "linkGroupingExtraTrafficAdmin": linkGroupingExtraTrafficAdmin,
       "linkGroupingGroupName": linkGroupingGroupName,
       "protectionTable": protectionTable,
       "protectionEntry": protectionEntry,
       "protectionGroupId": protectionGroupId,
       "protectionGroupsProtectionAdmin": protectionGroupsProtectionAdmin,
       "protectionNplus1ProtectionMethod": protectionNplus1ProtectionMethod,
       "protectionProtectingCarrierId": protectionProtectingCarrierId,
       "standardProtectionTable": standardProtectionTable,
       "standardProtectionEntry": standardProtectionEntry,
       "standardProtectionGroupId": standardProtectionGroupId,
       "standardProtectionSwitchOnEarlyWarning": standardProtectionSwitchOnEarlyWarning,
       "standardProtectionHighPrioProtectionTh": standardProtectionHighPrioProtectionTh,
       "standardProtectionRevertiveLink": standardProtectionRevertiveLink,
       "standardProtectionRevertiveSwitchTimeOut": standardProtectionRevertiveSwitchTimeOut,
       "membersTable": membersTable,
       "membersEntry": membersEntry,
       "membersGroupId": membersGroupId,
       "membersCarrierId": membersCarrierId,
       "membersProtectionPriorityLevel": membersProtectionPriorityLevel,
       "nplus1ProtectingTable": nplus1ProtectingTable,
       "nplus1ProtectingEntry": nplus1ProtectingEntry,
       "nplus1ProtectingGroupId": nplus1ProtectingGroupId,
       "nplus1ProtectingXCProtectionFraming": nplus1ProtectingXCProtectionFraming,
       "nplus1ProtectingProtectedLinkTx": nplus1ProtectingProtectedLinkTx,
       "nplus1ProtectingProtectedLinkRx": nplus1ProtectingProtectedLinkRx,
       "nplus1ProtectingRequestedLinkTx": nplus1ProtectingRequestedLinkTx,
       "nplus1ProtectingRequestedLinkRx": nplus1ProtectingRequestedLinkRx,
       "nplus1ProtectingSwitchToProtectingCommand": nplus1ProtectingSwitchToProtectingCommand,
       "carrierProtectionTable": carrierProtectionTable,
       "carrierProtectionEntry": carrierProtectionEntry,
       "carrierProtectionXCId": carrierProtectionXCId,
       "carrierProtectionCarrierId": carrierProtectionCarrierId,
       "carrierProtectionLinkGroupNum": carrierProtectionLinkGroupNum,
       "carrierProtectionServedByRemoteXC": carrierProtectionServedByRemoteXC,
       "carrierProtectionRadioStatus": carrierProtectionRadioStatus,
       "carrierProtectionLineFraming": carrierProtectionLineFraming,
       "carrierProtectionLoopback": carrierProtectionLoopback,
       "carrierProtectionLoopbackTimer": carrierProtectionLoopbackTimer,
       "nplus1StandardPMCurrTable": nplus1StandardPMCurrTable,
       "nplus1StandardPMCurrEntry": nplus1StandardPMCurrEntry,
       "nplus1StandardPMCurrCarrierId": nplus1StandardPMCurrCarrierId,
       "nplus1StandardPMCurrTimeElapsed": nplus1StandardPMCurrTimeElapsed,
       "nplus1StandardPMCurrValidIntervals": nplus1StandardPMCurrValidIntervals,
       "nplus1StandardPMCurrLastDayIDF": nplus1StandardPMCurrLastDayIDF,
       "nplus1StandardPMCurrLastDayGroupNum": nplus1StandardPMCurrLastDayGroupNum,
       "nplus1StandardPMCurrPSAC": nplus1StandardPMCurrPSAC,
       "nplus1StandardPMCurrFSRC": nplus1StandardPMCurrFSRC,
       "nplus1StandardPMCurrPSAD": nplus1StandardPMCurrPSAD,
       "nplus1StandardPMCurrFSRD": nplus1StandardPMCurrFSRD,
       "nplus1StandardPMCurrLastDayPSAC": nplus1StandardPMCurrLastDayPSAC,
       "nplus1StandardPMCurrLastDayFSRC": nplus1StandardPMCurrLastDayFSRC,
       "nplus1StandardPMCurrLastDayPSAD": nplus1StandardPMCurrLastDayPSAD,
       "nplus1StandardPMCurrLastDayFSRD": nplus1StandardPMCurrLastDayFSRD,
       "nplus1StandardPMIntervalTable": nplus1StandardPMIntervalTable,
       "nplus1StandardPMIntervalEntry": nplus1StandardPMIntervalEntry,
       "nplus1StandardPMIntervalCarrierId": nplus1StandardPMIntervalCarrierId,
       "nplus1StandardPMIntervalIdx": nplus1StandardPMIntervalIdx,
       "nplus1StandardPMIntervalIDF": nplus1StandardPMIntervalIDF,
       "nplus1StandardPMIntervalGroupNum": nplus1StandardPMIntervalGroupNum,
       "nplus1StandardPMIntervalPSAC": nplus1StandardPMIntervalPSAC,
       "nplus1StandardPMIntervalFSRC": nplus1StandardPMIntervalFSRC,
       "nplus1StandardPMIntervalPSAD": nplus1StandardPMIntervalPSAD,
       "nplus1StandardPMIntervalFSRD": nplus1StandardPMIntervalFSRD,
       "nplus1StandardPMDayTable": nplus1StandardPMDayTable,
       "nplus1StandardPMDayEntry": nplus1StandardPMDayEntry,
       "nplus1StandardPMDayCarrierId": nplus1StandardPMDayCarrierId,
       "nplus1StandardPMDayIdx": nplus1StandardPMDayIdx,
       "nplus1StandardPMDayIDF": nplus1StandardPMDayIDF,
       "nplus1StandardPMDayGroupNum": nplus1StandardPMDayGroupNum,
       "nplus1StandardPMDayPSAC": nplus1StandardPMDayPSAC,
       "nplus1StandardPMDayFSRC": nplus1StandardPMDayFSRC,
       "nplus1StandardPMDayPSAD": nplus1StandardPMDayPSAD,
       "nplus1StandardPMDayFSRD": nplus1StandardPMDayFSRD,
       "gnSSM": gnSSM,
       "gnSSMCfg": gnSSMCfg,
       "gnSSMCfgSSMMode": gnSSMCfgSSMMode,
       "gnSSMCfgPrimaryClockSource": gnSSMCfgPrimaryClockSource,
       "gnSSMCfgPrimaryClockQuality": gnSSMCfgPrimaryClockQuality,
       "gnSSMCfgSecondaryClockSource": gnSSMCfgSecondaryClockSource,
       "gnSSMCfgSecondaryClockQuality": gnSSMCfgSecondaryClockQuality,
       "gnSSMCfgClockUserCommand": gnSSMCfgClockUserCommand,
       "gnSSMCfgClockOutputMute": gnSSMCfgClockOutputMute,
       "gnSSMStat": gnSSMStat,
       "gnSSMStatStatus": gnSSMStatStatus,
       "gnSSMStatCurrentClock": gnSSMStatCurrentClock,
       "gnSSMStatCurrentClockQuality": gnSSMStatCurrentClockQuality,
       "gnSSMStatClockUnitType": gnSSMStatClockUnitType,
       "gnSSMStatHoldoverPeriod": gnSSMStatHoldoverPeriod,
       "gnAccess": gnAccess,
       "gnAccessCfg": gnAccessCfg,
       "gnAccessCfgTable": gnAccessCfgTable,
       "gnAccessCfgEntry": gnAccessCfgEntry,
       "gnAccessCfgLongCableOption": gnAccessCfgLongCableOption,
       "gnAccessCfgLoopbackOption": gnAccessCfgLoopbackOption,
       "gnAccessCfgRunPrbs": gnAccessCfgRunPrbs,
       "gnAccessCfgEXCThresh": gnAccessCfgEXCThresh,
       "gnAccessCfgSDThresh": gnAccessCfgSDThresh,
       "gnAccessCfgTest": gnAccessCfgTest,
       "gnAccessCfgLineCoding": gnAccessCfgLineCoding,
       "gnAccessStat": gnAccessStat,
       "gnAccessStatTable": gnAccessStatTable,
       "gnAccessStatEntry": gnAccessStatEntry,
       "gnAccessStatInterfaceBer": gnAccessStatInterfaceBer,
       "gnAccessStatStatus": gnAccessStatStatus,
       "gnAccessStatPrbsBer": gnAccessStatPrbsBer,
       "gnAccessStatValidIntervals": gnAccessStatValidIntervals,
       "gnFastEthernetCfg": gnFastEthernetCfg,
       "gnFastEthernetCfgTable": gnFastEthernetCfgTable,
       "gnFastEthernetCfgEntry": gnFastEthernetCfgEntry,
       "gnFastEthernetCfgAutoNegotiation": gnFastEthernetCfgAutoNegotiation,
       "gnFastEthernetCfgForceSpeed": gnFastEthernetCfgForceSpeed,
       "gnFastEthernetCfgDynamicBand": gnFastEthernetCfgDynamicBand,
       "gnFastEthernetCfgGigabitEthernet": gnFastEthernetCfgGigabitEthernet,
       "gnFastEthernetCfgDuplexMode": gnFastEthernetCfgDuplexMode,
       "gnFastEthernetCfgQueuingScheme": gnFastEthernetCfgQueuingScheme,
       "gnFastEthernetStat": gnFastEthernetStat,
       "gnFastEthernetStatTable": gnFastEthernetStatTable,
       "gnFastEthernetStatEntry": gnFastEthernetStatEntry,
       "gnFastEthernetStatStatus": gnFastEthernetStatStatus,
       "gnPdhMon": gnPdhMon,
       "gnPdhMonCurrTable": gnPdhMonCurrTable,
       "gnPdhMonCurrEntry": gnPdhMonCurrEntry,
       "gnPdhMonCurrES": gnPdhMonCurrES,
       "gnPdhMonCurrSES": gnPdhMonCurrSES,
       "gnPdhMonCurrBBE": gnPdhMonCurrBBE,
       "gnPdhMonCurrUAS": gnPdhMonCurrUAS,
       "gnPdhMonCurrCV": gnPdhMonCurrCV,
       "gnPdhMonCurrLastDayES": gnPdhMonCurrLastDayES,
       "gnPdhMonCurrLastDaySES": gnPdhMonCurrLastDaySES,
       "gnPdhMonCurrLastDayBBE": gnPdhMonCurrLastDayBBE,
       "gnPdhMonCurrLastDayUAS": gnPdhMonCurrLastDayUAS,
       "gnPdhMonCurrLastDayCV": gnPdhMonCurrLastDayCV,
       "gnPdhMonCurrLastDayIDF": gnPdhMonCurrLastDayIDF,
       "gnPdhMonIntervalTable": gnPdhMonIntervalTable,
       "gnPdhMonIntervalEntry": gnPdhMonIntervalEntry,
       "gnPdhMonIntervalIdx": gnPdhMonIntervalIdx,
       "gnPdhMonIntervalES": gnPdhMonIntervalES,
       "gnPdhMonIntervalSES": gnPdhMonIntervalSES,
       "gnPdhMonIntervalBBE": gnPdhMonIntervalBBE,
       "gnPdhMonIntervalUAS": gnPdhMonIntervalUAS,
       "gnPdhMonIntervalCV": gnPdhMonIntervalCV,
       "gnPdhMonIntervalIDF": gnPdhMonIntervalIDF,
       "gnPdhMonDayTable": gnPdhMonDayTable,
       "gnPdhMonDayEntry": gnPdhMonDayEntry,
       "gnPdhMonDayIdx": gnPdhMonDayIdx,
       "gnPdhMonDayES": gnPdhMonDayES,
       "gnPdhMonDaySES": gnPdhMonDaySES,
       "gnPdhMonDayBBE": gnPdhMonDayBBE,
       "gnPdhMonDayUAS": gnPdhMonDayUAS,
       "gnPdhMonDayCV": gnPdhMonDayCV,
       "gnPdhMonDayIDF": gnPdhMonDayIDF,
       "gnFastEthernetMon": gnFastEthernetMon,
       "gnFastEthernetMonPrivateTable": gnFastEthernetMonPrivateTable,
       "gnFastEthernetMonPrivateEntry": gnFastEthernetMonPrivateEntry,
       "gnFastEthernetMonPrivateAlignmentErrors": gnFastEthernetMonPrivateAlignmentErrors,
       "gnFastEthernetMonPrivateFcsErrors": gnFastEthernetMonPrivateFcsErrors,
       "gnFastEthernetMonPrivateFrameTooLongs": gnFastEthernetMonPrivateFrameTooLongs,
       "gnFastEthernetMonStdHiTable": gnFastEthernetMonStdHiTable,
       "gnFastEthernetMonStdHiEntry": gnFastEthernetMonStdHiEntry,
       "gnFastEthernetMonStdHiInOctetsHC": gnFastEthernetMonStdHiInOctetsHC,
       "gnFastEthernetMonStdHiInUcastPktsHC": gnFastEthernetMonStdHiInUcastPktsHC,
       "gnFastEthernetMonStdHiInNUcastPktsHC": gnFastEthernetMonStdHiInNUcastPktsHC,
       "gnFastEthernetMonStdHiOutOctetsHC": gnFastEthernetMonStdHiOutOctetsHC,
       "gnFastEthernetMonStdHiOutUcastPktsHC": gnFastEthernetMonStdHiOutUcastPktsHC,
       "gnFastEthernetMonStdHiOutNUcastPktsHC": gnFastEthernetMonStdHiOutNUcastPktsHC,
       "gnTrailCfg": gnTrailCfg,
       "gnTrailCfgTable": gnTrailCfgTable,
       "gnTrailCfgEntry": gnTrailCfgEntry,
       "gnTrailCfgTrailName": gnTrailCfgTrailName,
       "gnTrailCfgProtection": gnTrailCfgProtection,
       "gnTrailCfgLowPathIndex": gnTrailCfgLowPathIndex,
       "gnTrailCfgLowPathSide": gnTrailCfgLowPathSide,
       "gnTrailCfgProtectionOptions": gnTrailCfgProtectionOptions,
       "gnTrailCfgMismatchJ2": gnTrailCfgMismatchJ2,
       "gnTrailCfgTransmittedJ2": gnTrailCfgTransmittedJ2,
       "gnTrailCfgExpectedJ2": gnTrailCfgExpectedJ2,
       "gnTrailCfgReversionMode": gnTrailCfgReversionMode,
       "gnTrailCfgProtectionUserCommand": gnTrailCfgProtectionUserCommand,
       "gnTrailCfgHoldOffTime": gnTrailCfgHoldOffTime,
       "gnTrailCfgOscillationGuardTime": gnTrailCfgOscillationGuardTime,
       "gnTrailCfgWaitToRestoreTime": gnTrailCfgWaitToRestoreTime,
       "gnTrailCfgSignalLabelMismatch": gnTrailCfgSignalLabelMismatch,
       "gnTrailCfgBERConsAction": gnTrailCfgBERConsAction,
       "gnTribCfg": gnTribCfg,
       "gnTribCfgTable": gnTribCfgTable,
       "gnTribCfgEntry": gnTribCfgEntry,
       "gnTribCfgLowPathIndex": gnTribCfgLowPathIndex,
       "gnTribCfgLowPathSide": gnTribCfgLowPathSide,
       "gnTribCfgProtection": gnTribCfgProtection,
       "gnTribCfgProtectionOptions": gnTribCfgProtectionOptions,
       "gnTribCfgReversionMode": gnTribCfgReversionMode,
       "gnTribCfgProtectionUserCommand": gnTribCfgProtectionUserCommand,
       "gnTribCfgHoldOffTime": gnTribCfgHoldOffTime,
       "gnTribCfgOscillationGuardTime": gnTribCfgOscillationGuardTime,
       "gnTribCfgWaitToRestoreTime": gnTribCfgWaitToRestoreTime,
       "gnTribCfgKLM": gnTribCfgKLM,
       "gnTrailPassThrough": gnTrailPassThrough,
       "gnTrailPassThroughTable": gnTrailPassThroughTable,
       "gnTrailPassThroughEntry": gnTrailPassThroughEntry,
       "gnTrailPassThroughIndex": gnTrailPassThroughIndex,
       "gnTrailPassThroughName": gnTrailPassThroughName,
       "gnGigabitEthernetCfg": gnGigabitEthernetCfg,
       "gnGigabitEthernetCfgTable": gnGigabitEthernetCfgTable,
       "gnGigabitEthernetCfgEntry": gnGigabitEthernetCfgEntry,
       "gnGigabitEthernetCfgPauseFrameGenerating": gnGigabitEthernetCfgPauseFrameGenerating,
       "gnGigabitEthernetCfgMuteOnExcError": gnGigabitEthernetCfgMuteOnExcError,
       "gnGigabitEthernetCfgMuteOnSd": gnGigabitEthernetCfgMuteOnSd,
       "gnGigabitEthernetCfgMuteOnRemoteRadioFault": gnGigabitEthernetCfgMuteOnRemoteRadioFault,
       "gnGigabitEthernetCfgSpeedAndDuplex": gnGigabitEthernetCfgSpeedAndDuplex,
       "gnGigabitEthernetCfgSchedulerPriorityOption": gnGigabitEthernetCfgSchedulerPriorityOption,
       "gnGigabitEthernetCfgSchedulerQueue1Weight": gnGigabitEthernetCfgSchedulerQueue1Weight,
       "gnGigabitEthernetCfgSchedulerQueue2Weight": gnGigabitEthernetCfgSchedulerQueue2Weight,
       "gnGigabitEthernetCfgSchedulerQueue3Weight": gnGigabitEthernetCfgSchedulerQueue3Weight,
       "gnGigabitEthernetCfgSchedulerQueue4Weight": gnGigabitEthernetCfgSchedulerQueue4Weight,
       "gnGigabitEthernetCfgClassifierFirstPrioUDP": gnGigabitEthernetCfgClassifierFirstPrioUDP,
       "gnGigabitEthernetCfgClassifierPrioBitSource": gnGigabitEthernetCfgClassifierPrioBitSource,
       "gnGigabitEthernetCfgClassifierGroupMinVlanId": gnGigabitEthernetCfgClassifierGroupMinVlanId,
       "gnGigabitEthernetCfgClassifierGroupMaxVlanId": gnGigabitEthernetCfgClassifierGroupMaxVlanId,
       "gnGigabitEthernetCfgClassifierGroupVlanPriority": gnGigabitEthernetCfgClassifierGroupVlanPriority,
       "gnGigabitEthernetCfgClassifierGroupVlanSet": gnGigabitEthernetCfgClassifierGroupVlanSet,
       "gnGigabitEthernetCfgAcmMuteOnMinConstellation": gnGigabitEthernetCfgAcmMuteOnMinConstellation,
       "gnGigabitEthernetCfgEnableAutomaticTxMute": gnGigabitEthernetCfgEnableAutomaticTxMute,
       "gnGigabitEthernetCfgTrafficBISTAdmin": gnGigabitEthernetCfgTrafficBISTAdmin,
       "gnGigabitEthernetCfgClearStatistics": gnGigabitEthernetCfgClearStatistics,
       "gnGigabitEthernetCfgPauseFrameForwarding": gnGigabitEthernetCfgPauseFrameForwarding,
       "gnGigabitEthernetCfgPhyLoopback": gnGigabitEthernetCfgPhyLoopback,
       "gnVlanEthernetStat": gnVlanEthernetStat,
       "gnVlanEthernetStatTable": gnVlanEthernetStatTable,
       "gnVlanEthernetStatEntry": gnVlanEthernetStatEntry,
       "gnVlanEthernetStatGroupId": gnVlanEthernetStatGroupId,
       "gnVlanEthernetStatMinVlanId": gnVlanEthernetStatMinVlanId,
       "gnVlanEthernetStatMaxVlanId": gnVlanEthernetStatMaxVlanId,
       "gnVlanEthernetStatVlanPriority": gnVlanEthernetStatVlanPriority,
       "gnGigabitEthernetStat": gnGigabitEthernetStat,
       "gnGigabitEthernetStatTable": gnGigabitEthernetStatTable,
       "gnGigabitEthernetStatEntry": gnGigabitEthernetStatEntry,
       "gnGigabitEthernetStatBistErrorSeconds": gnGigabitEthernetStatBistErrorSeconds,
       "gnGigabitEthernetStatSpeedAndDuplexSupport": gnGigabitEthernetStatSpeedAndDuplexSupport,
       "gnGigabitEthernetStatValidIntervals": gnGigabitEthernetStatValidIntervals,
       "gnGigabitEthernetStatSpeedAndDuplexMode": gnGigabitEthernetStatSpeedAndDuplexMode,
       "gnGigabitEthernetMon": gnGigabitEthernetMon,
       "gnGigabitEthernetMonCurrTable": gnGigabitEthernetMonCurrTable,
       "gnGigabitEthernetMonCurrEntry": gnGigabitEthernetMonCurrEntry,
       "gnGigabitEthernetMonCurrPacketErrorRate": gnGigabitEthernetMonCurrPacketErrorRate,
       "gnGigabitEthernetMonCurrIDF": gnGigabitEthernetMonCurrIDF,
       "gnGigabitEthernetMonCurrDayPacketErrorRate": gnGigabitEthernetMonCurrDayPacketErrorRate,
       "gnGigabitEthernetMonCurrDayIDF": gnGigabitEthernetMonCurrDayIDF,
       "gnGigabitEthernetMonIntervalTable": gnGigabitEthernetMonIntervalTable,
       "gnGigabitEthernetMonIntervalEntry": gnGigabitEthernetMonIntervalEntry,
       "gnGigabitEthernetMonIntervalIdx": gnGigabitEthernetMonIntervalIdx,
       "gnGigabitEthernetMonIntervalPacketErrorRate": gnGigabitEthernetMonIntervalPacketErrorRate,
       "gnGigabitEthernetMonIntervalIDF": gnGigabitEthernetMonIntervalIDF,
       "gnGigabitEthernetMonDayTable": gnGigabitEthernetMonDayTable,
       "gnGigabitEthernetMonDayEntry": gnGigabitEthernetMonDayEntry,
       "gnGigabitEthernetMonDayIdx": gnGigabitEthernetMonDayIdx,
       "gnGigabitEthernetMonDayPacketErrorRate": gnGigabitEthernetMonDayPacketErrorRate,
       "gnGigabitEthernetMonDayIDF": gnGigabitEthernetMonDayIDF,
       "gnEthStatistic": gnEthStatistic,
       "gnEthStatisticTable": gnEthStatisticTable,
       "gnEthStatisticEntry": gnEthStatisticEntry,
       "gnEthStatisticIfInOctetsMsb": gnEthStatisticIfInOctetsMsb,
       "gnEthStatisticAFrameReceivedOkLsb": gnEthStatisticAFrameReceivedOkLsb,
       "gnEthStatisticAFrameReceivedOkMsb": gnEthStatisticAFrameReceivedOkMsb,
       "gnEthStatisticCRCAlignErrorsMsb": gnEthStatisticCRCAlignErrorsMsb,
       "gnEthStatisticIfInUcastPktsMsb": gnEthStatisticIfInUcastPktsMsb,
       "gnEthStatisticBroadcastPktsMsb": gnEthStatisticBroadcastPktsMsb,
       "gnEthStatisticMulticastPktsMsb": gnEthStatisticMulticastPktsMsb,
       "gnEthStatisticUndersizePktsMsb": gnEthStatisticUndersizePktsMsb,
       "gnEthStatisticOversizePktsMsb": gnEthStatisticOversizePktsMsb,
       "gnEthStatisticPkts64OctetMsb": gnEthStatisticPkts64OctetMsb,
       "gnEthStatisticPkts65to127OctetMsb": gnEthStatisticPkts65to127OctetMsb,
       "gnEthStatisticPkts128to255OctetMsb": gnEthStatisticPkts128to255OctetMsb,
       "gnEthStatisticPkts256to511OctetMsb": gnEthStatisticPkts256to511OctetMsb,
       "gnEthStatisticPkts512to1023OctetMsb": gnEthStatisticPkts512to1023OctetMsb,
       "gnEthStatisticPkts1024to1518OctetMsb": gnEthStatisticPkts1024to1518OctetMsb,
       "gnEthStatisticRadioTransmitFramesLsb": gnEthStatisticRadioTransmitFramesLsb,
       "gnEthStatisticRadioTransmitFramesMsb": gnEthStatisticRadioTransmitFramesMsb,
       "gnEthStatisticDroppedPacketsLsb": gnEthStatisticDroppedPacketsLsb,
       "gnEthStatisticDroppedPacketsMsb": gnEthStatisticDroppedPacketsMsb,
       "gnEthStatisticRadioReceivedFramesLsb": gnEthStatisticRadioReceivedFramesLsb,
       "gnEthStatisticRadioReceivedFramesMsb": gnEthStatisticRadioReceivedFramesMsb,
       "gnEthStatisticRadioReceivedCrcFramesLsb": gnEthStatisticRadioReceivedCrcFramesLsb,
       "gnEthStatisticRadioReceivedCrcFramesMsb": gnEthStatisticRadioReceivedCrcFramesMsb,
       "gnEthStatisticRadioSyncUnlockEventsLsb": gnEthStatisticRadioSyncUnlockEventsLsb,
       "gnEthStatisticRadioSyncUnlockEventsMsb": gnEthStatisticRadioSyncUnlockEventsMsb,
       "gnEthStatisticAFrameTransmittedOkLsb": gnEthStatisticAFrameTransmittedOkLsb,
       "gnEthStatisticAFrameTransmittedOkMsb": gnEthStatisticAFrameTransmittedOkMsb,
       "gnEthStatisticIfOutOctetsMsb": gnEthStatisticIfOutOctetsMsb,
       "gnEthStatisticEtherStatsPktsMsb": gnEthStatisticEtherStatsPktsMsb,
       "gnEthStatisticEtherStatsOctetsMsb": gnEthStatisticEtherStatsOctetsMsb,
       "gnLastDummy": gnLastDummy,
       "gnLastDummyParam": gnLastDummyParam}
)
