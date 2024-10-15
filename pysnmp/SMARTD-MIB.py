# SNMP MIB module (SMARTD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SMARTD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:55:32 2024
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

(lannet,) = mibBuilder.importSymbols(
    "GEN-MIB",
    "lannet")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class Timeout(Integer32):
    """Custom type Timeout based on Integer32"""




class MacAddress(OctetString):
    """Custom type MacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SmartDevices_ObjectIdentity = ObjectIdentity
smartDevices = _SmartDevices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 27)
)
_SmartGeneral_ObjectIdentity = ObjectIdentity
smartGeneral = _SmartGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 27, 1)
)
_SmartGenSWVersion_Type = DisplayString
_SmartGenSWVersion_Object = MibScalar
smartGenSWVersion = _SmartGenSWVersion_Object(
    (1, 3, 6, 1, 4, 1, 81, 27, 1, 1),
    _SmartGenSWVersion_Type()
)
smartGenSWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smartGenSWVersion.setStatus("mandatory")
_SmartGenOSVersion_Type = DisplayString
_SmartGenOSVersion_Object = MibScalar
smartGenOSVersion = _SmartGenOSVersion_Object(
    (1, 3, 6, 1, 4, 1, 81, 27, 1, 2),
    _SmartGenOSVersion_Type()
)
smartGenOSVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smartGenOSVersion.setStatus("mandatory")
_SmartGenSoftwareDscr_Type = DisplayString
_SmartGenSoftwareDscr_Object = MibScalar
smartGenSoftwareDscr = _SmartGenSoftwareDscr_Object(
    (1, 3, 6, 1, 4, 1, 81, 27, 1, 3),
    _SmartGenSoftwareDscr_Type()
)
smartGenSoftwareDscr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smartGenSoftwareDscr.setStatus("mandatory")
_SmartGenBootVersion_Type = DisplayString
_SmartGenBootVersion_Object = MibScalar
smartGenBootVersion = _SmartGenBootVersion_Object(
    (1, 3, 6, 1, 4, 1, 81, 27, 1, 4),
    _SmartGenBootVersion_Type()
)
smartGenBootVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smartGenBootVersion.setStatus("mandatory")


class _SmartGenReset_Type(Integer32):
    """Custom type smartGenReset based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_SmartGenReset_Type.__name__ = "Integer32"
_SmartGenReset_Object = MibScalar
smartGenReset = _SmartGenReset_Object(
    (1, 3, 6, 1, 4, 1, 81, 27, 1, 5),
    _SmartGenReset_Type()
)
smartGenReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smartGenReset.setStatus("mandatory")
_SmartGenHardwareVersion_Type = DisplayString
_SmartGenHardwareVersion_Object = MibScalar
smartGenHardwareVersion = _SmartGenHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 81, 27, 1, 6),
    _SmartGenHardwareVersion_Type()
)
smartGenHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smartGenHardwareVersion.setStatus("mandatory")


class _SmartGenMonitoringPort_Type(Integer32):
    """Custom type smartGenMonitoringPort based on Integer32"""
    defaultValue = 16


_SmartGenMonitoringPort_Object = MibScalar
smartGenMonitoringPort = _SmartGenMonitoringPort_Object(
    (1, 3, 6, 1, 4, 1, 81, 27, 1, 7),
    _SmartGenMonitoringPort_Type()
)
smartGenMonitoringPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smartGenMonitoringPort.setStatus("mandatory")


class _SmartGenMonitoredPort_Type(Integer32):
    """Custom type smartGenMonitoredPort based on Integer32"""
    defaultValue = 0


_SmartGenMonitoredPort_Object = MibScalar
smartGenMonitoredPort = _SmartGenMonitoredPort_Object(
    (1, 3, 6, 1, 4, 1, 81, 27, 1, 8),
    _SmartGenMonitoredPort_Type()
)
smartGenMonitoredPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smartGenMonitoredPort.setStatus("mandatory")
_SmartGenLastChange_Type = TimeTicks
_SmartGenLastChange_Object = MibScalar
smartGenLastChange = _SmartGenLastChange_Object(
    (1, 3, 6, 1, 4, 1, 81, 27, 1, 9),
    _SmartGenLastChange_Type()
)
smartGenLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smartGenLastChange.setStatus("mandatory")


class _SmartGenMonitorMode_Type(Integer32):
    """Custom type smartGenMonitorMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 255),
          ("off", 2),
          ("on", 1))
    )


_SmartGenMonitorMode_Type.__name__ = "Integer32"
_SmartGenMonitorMode_Object = MibScalar
smartGenMonitorMode = _SmartGenMonitorMode_Object(
    (1, 3, 6, 1, 4, 1, 81, 27, 1, 10),
    _SmartGenMonitorMode_Type()
)
smartGenMonitorMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smartGenMonitorMode.setStatus("mandatory")


class _SmartGenNetworkPrefix_Type(OctetString):
    """Custom type smartGenNetworkPrefix based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(13, 13),
    )


_SmartGenNetworkPrefix_Type.__name__ = "OctetString"
_SmartGenNetworkPrefix_Object = MibScalar
smartGenNetworkPrefix = _SmartGenNetworkPrefix_Object(
    (1, 3, 6, 1, 4, 1, 81, 27, 1, 11),
    _SmartGenNetworkPrefix_Type()
)
smartGenNetworkPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smartGenNetworkPrefix.setStatus("mandatory")


class _SmartGenConnectMode_Type(Integer32):
    """Custom type smartGenConnectMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("lane10", 1),
          ("notSupported", 255),
          ("pvc", 2))
    )


_SmartGenConnectMode_Type.__name__ = "Integer32"
_SmartGenConnectMode_Object = MibScalar
smartGenConnectMode = _SmartGenConnectMode_Object(
    (1, 3, 6, 1, 4, 1, 81, 27, 1, 12),
    _SmartGenConnectMode_Type()
)
smartGenConnectMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smartGenConnectMode.setStatus("mandatory")


class _SmartGenPvcVP_Type(Integer32):
    """Custom type smartGenPvcVP based on Integer32"""
    defaultValue = 0


_SmartGenPvcVP_Object = MibScalar
smartGenPvcVP = _SmartGenPvcVP_Object(
    (1, 3, 6, 1, 4, 1, 81, 27, 1, 13),
    _SmartGenPvcVP_Type()
)
smartGenPvcVP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smartGenPvcVP.setStatus("mandatory")


class _SmartGenPvcVC_Type(Integer32):
    """Custom type smartGenPvcVC based on Integer32"""
    defaultValue = 100


_SmartGenPvcVC_Object = MibScalar
smartGenPvcVC = _SmartGenPvcVC_Object(
    (1, 3, 6, 1, 4, 1, 81, 27, 1, 14),
    _SmartGenPvcVC_Type()
)
smartGenPvcVC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smartGenPvcVC.setStatus("mandatory")
_SmartGenSlotNumber_Type = Integer32
_SmartGenSlotNumber_Object = MibScalar
smartGenSlotNumber = _SmartGenSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 81, 27, 1, 15),
    _SmartGenSlotNumber_Type()
)
smartGenSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smartGenSlotNumber.setStatus("mandatory")


class _SmartGenHubMgmtIfType_Type(Integer32):
    """Custom type smartGenHubMgmtIfType based on Integer32"""
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
              255)
        )
    )
    namedValues = NamedValues(
        *(("aal5", 49),
          ("arcnet", 35),
          ("arcnetPlus", 36),
          ("atm", 37),
          ("basicIsdn", 20),
          ("cept", 19),
          ("ddn-x25", 4),
          ("ds3", 30),
          ("eon", 25),
          ("ethernet-3Mbit", 26),
          ("ethernet-csmacd", 6),
          ("fddi", 15),
          ("frameRelay", 32),
          ("frameRelayService", 44),
          ("hdh1822", 3),
          ("hippi", 47),
          ("hssi", 46),
          ("hyperchannel", 14),
          ("ip", 255),
          ("iso88022llc", 41),
          ("iso88023-csmacd", 7),
          ("iso88024-tokenBus", 8),
          ("iso88025-tokenRing", 9),
          ("iso88026-man", 10),
          ("lapb", 16),
          ("localTalk", 42),
          ("miox25", 38),
          ("modem", 48),
          ("none", 1),
          ("nsip", 27),
          ("para", 34),
          ("ppp", 23),
          ("primaryIsdn", 21),
          ("propMultiplexor", 54),
          ("propPointToPointSerial", 22),
          ("propVirtual", 53),
          ("proteon-10MBit", 12),
          ("proteon-80MBit", 13),
          ("regular1822", 2),
          ("rfc877-x25", 5),
          ("rs232", 33),
          ("sdlc", 17),
          ("sip", 31),
          ("slip", 28),
          ("smdsDxi", 43),
          ("smdsIcip", 52),
          ("softwareLoopback", 24),
          ("sonet", 39),
          ("sonetPath", 50),
          ("sonetVT", 51),
          ("starLan", 11),
          ("t1-carrier", 18),
          ("ultra", 29),
          ("v35", 45),
          ("x25ple", 40))
    )


_SmartGenHubMgmtIfType_Type.__name__ = "Integer32"
_SmartGenHubMgmtIfType_Object = MibScalar
smartGenHubMgmtIfType = _SmartGenHubMgmtIfType_Object(
    (1, 3, 6, 1, 4, 1, 81, 27, 1, 16),
    _SmartGenHubMgmtIfType_Type()
)
smartGenHubMgmtIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smartGenHubMgmtIfType.setStatus("mandatory")


class _SmartGenHubAddr_Type(OctetString):
    """Custom type smartGenHubAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SmartGenHubAddr_Type.__name__ = "OctetString"
_SmartGenHubAddr_Object = MibScalar
smartGenHubAddr = _SmartGenHubAddr_Object(
    (1, 3, 6, 1, 4, 1, 81, 27, 1, 17),
    _SmartGenHubAddr_Type()
)
smartGenHubAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smartGenHubAddr.setStatus("mandatory")
_SmartAgent_ObjectIdentity = ObjectIdentity
smartAgent = _SmartAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 27, 2)
)


class _SmartAgCoprocCommStatus_Type(Integer32):
    """Custom type smartAgCoprocCommStatus based on Integer32"""
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
        *(("commProblems", 2),
          ("ok", 1),
          ("timeout", 3))
    )


_SmartAgCoprocCommStatus_Type.__name__ = "Integer32"
_SmartAgCoprocCommStatus_Object = MibScalar
smartAgCoprocCommStatus = _SmartAgCoprocCommStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 27, 2, 1),
    _SmartAgCoprocCommStatus_Type()
)
smartAgCoprocCommStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smartAgCoprocCommStatus.setStatus("mandatory")


class _SmartAgCommDebugMode_Type(Integer32):
    """Custom type smartAgCommDebugMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_SmartAgCommDebugMode_Type.__name__ = "Integer32"
_SmartAgCommDebugMode_Object = MibScalar
smartAgCommDebugMode = _SmartAgCommDebugMode_Object(
    (1, 3, 6, 1, 4, 1, 81, 27, 2, 2),
    _SmartAgCommDebugMode_Type()
)
smartAgCommDebugMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smartAgCommDebugMode.setStatus("mandatory")


class _SmartAgConfigChangeTraps_Type(Integer32):
    """Custom type smartAgConfigChangeTraps based on Integer32"""
    defaultValue = 1

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


_SmartAgConfigChangeTraps_Type.__name__ = "Integer32"
_SmartAgConfigChangeTraps_Object = MibScalar
smartAgConfigChangeTraps = _SmartAgConfigChangeTraps_Object(
    (1, 3, 6, 1, 4, 1, 81, 27, 2, 3),
    _SmartAgConfigChangeTraps_Type()
)
smartAgConfigChangeTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smartAgConfigChangeTraps.setStatus("mandatory")


class _SmartAgFaultTraps_Type(Integer32):
    """Custom type smartAgFaultTraps based on Integer32"""
    defaultValue = 1

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


_SmartAgFaultTraps_Type.__name__ = "Integer32"
_SmartAgFaultTraps_Object = MibScalar
smartAgFaultTraps = _SmartAgFaultTraps_Object(
    (1, 3, 6, 1, 4, 1, 81, 27, 2, 4),
    _SmartAgFaultTraps_Type()
)
smartAgFaultTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smartAgFaultTraps.setStatus("mandatory")


class _SmartAgLaneFaultTraps_Type(Integer32):
    """Custom type smartAgLaneFaultTraps based on Integer32"""
    defaultValue = 1

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


_SmartAgLaneFaultTraps_Type.__name__ = "Integer32"
_SmartAgLaneFaultTraps_Object = MibScalar
smartAgLaneFaultTraps = _SmartAgLaneFaultTraps_Object(
    (1, 3, 6, 1, 4, 1, 81, 27, 2, 5),
    _SmartAgLaneFaultTraps_Type()
)
smartAgLaneFaultTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smartAgLaneFaultTraps.setStatus("mandatory")


class _SmartAgSoftwareStatus_Type(Integer32):
    """Custom type smartAgSoftwareStatus based on Integer32"""
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
        *(("downLoadOfDownload", 4),
          ("downLoading", 3),
          ("loaded", 2),
          ("unLoadable", 1))
    )


_SmartAgSoftwareStatus_Type.__name__ = "Integer32"
_SmartAgSoftwareStatus_Object = MibScalar
smartAgSoftwareStatus = _SmartAgSoftwareStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 27, 2, 6),
    _SmartAgSoftwareStatus_Type()
)
smartAgSoftwareStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smartAgSoftwareStatus.setStatus("mandatory")
_SmartIfExtension_ObjectIdentity = ObjectIdentity
smartIfExtension = _SmartIfExtension_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 27, 3)
)
_SmartIfExtensionTable_Object = MibTable
smartIfExtensionTable = _SmartIfExtensionTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 27, 3, 1)
)
if mibBuilder.loadTexts:
    smartIfExtensionTable.setStatus("mandatory")
_SmartIfExtensionEntry_Object = MibTableRow
smartIfExtensionEntry = _SmartIfExtensionEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 27, 3, 1, 1)
)
smartIfExtensionEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    smartIfExtensionEntry.setStatus("mandatory")


class _SmartIfExtensionEthStatus_Type(Integer32):
    """Custom type smartIfExtensionEthStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 255),
          ("ok", 1),
          ("rld", 2),
          ("tld", 4))
    )


_SmartIfExtensionEthStatus_Type.__name__ = "Integer32"
_SmartIfExtensionEthStatus_Object = MibTableColumn
smartIfExtensionEthStatus = _SmartIfExtensionEthStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 27, 3, 1, 1, 1),
    _SmartIfExtensionEthStatus_Type()
)
smartIfExtensionEthStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smartIfExtensionEthStatus.setStatus("mandatory")


class _SmartIfExtensionActivity_Type(Integer32):
    """Custom type smartIfExtensionActivity based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("active", 3),
          ("notActive", 1),
          ("notSupported", 255),
          ("standby", 2))
    )


_SmartIfExtensionActivity_Type.__name__ = "Integer32"
_SmartIfExtensionActivity_Object = MibTableColumn
smartIfExtensionActivity = _SmartIfExtensionActivity_Object(
    (1, 3, 6, 1, 4, 1, 81, 27, 3, 1, 1, 2),
    _SmartIfExtensionActivity_Type()
)
smartIfExtensionActivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smartIfExtensionActivity.setStatus("mandatory")


class _SmartIfExtensionViNet_Type(Integer32):
    """Custom type smartIfExtensionViNet based on Integer32"""
    defaultValue = 0


_SmartIfExtensionViNet_Object = MibTableColumn
smartIfExtensionViNet = _SmartIfExtensionViNet_Object(
    (1, 3, 6, 1, 4, 1, 81, 27, 3, 1, 1, 3),
    _SmartIfExtensionViNet_Type()
)
smartIfExtensionViNet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smartIfExtensionViNet.setStatus("mandatory")


class _SmartIfExtensionPriorityLevel_Type(Integer32):
    """Custom type smartIfExtensionPriorityLevel based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              5,
              255)
        )
    )
    namedValues = NamedValues(
        *(("default", 5),
          ("notSupported", 255),
          ("video", 3))
    )


_SmartIfExtensionPriorityLevel_Type.__name__ = "Integer32"
_SmartIfExtensionPriorityLevel_Object = MibTableColumn
smartIfExtensionPriorityLevel = _SmartIfExtensionPriorityLevel_Object(
    (1, 3, 6, 1, 4, 1, 81, 27, 3, 1, 1, 4),
    _SmartIfExtensionPriorityLevel_Type()
)
smartIfExtensionPriorityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smartIfExtensionPriorityLevel.setStatus("mandatory")


class _SmartIfExtensionBridgeEnable_Type(Integer32):
    """Custom type smartIfExtensionBridgeEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("notSupported", 255))
    )


_SmartIfExtensionBridgeEnable_Type.__name__ = "Integer32"
_SmartIfExtensionBridgeEnable_Object = MibTableColumn
smartIfExtensionBridgeEnable = _SmartIfExtensionBridgeEnable_Object(
    (1, 3, 6, 1, 4, 1, 81, 27, 3, 1, 1, 5),
    _SmartIfExtensionBridgeEnable_Type()
)
smartIfExtensionBridgeEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smartIfExtensionBridgeEnable.setStatus("mandatory")


class _SmartIfExtensionBackPressure_Type(Integer32):
    """Custom type smartIfExtensionBackPressure based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("notSupported", 255))
    )


_SmartIfExtensionBackPressure_Type.__name__ = "Integer32"
_SmartIfExtensionBackPressure_Object = MibTableColumn
smartIfExtensionBackPressure = _SmartIfExtensionBackPressure_Object(
    (1, 3, 6, 1, 4, 1, 81, 27, 3, 1, 1, 6),
    _SmartIfExtensionBackPressure_Type()
)
smartIfExtensionBackPressure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smartIfExtensionBackPressure.setStatus("mandatory")


class _SmartIfExtensionSTAEnable_Type(Integer32):
    """Custom type smartIfExtensionSTAEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("notSupported", 255))
    )


_SmartIfExtensionSTAEnable_Type.__name__ = "Integer32"
_SmartIfExtensionSTAEnable_Object = MibTableColumn
smartIfExtensionSTAEnable = _SmartIfExtensionSTAEnable_Object(
    (1, 3, 6, 1, 4, 1, 81, 27, 3, 1, 1, 7),
    _SmartIfExtensionSTAEnable_Type()
)
smartIfExtensionSTAEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smartIfExtensionSTAEnable.setStatus("mandatory")
_SmartViNet_ObjectIdentity = ObjectIdentity
smartViNet = _SmartViNet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 27, 4)
)


class _SmartViNetMaxNumOfNets_Type(Integer32):
    """Custom type smartViNetMaxNumOfNets based on Integer32"""
    defaultValue = 16


_SmartViNetMaxNumOfNets_Object = MibScalar
smartViNetMaxNumOfNets = _SmartViNetMaxNumOfNets_Object(
    (1, 3, 6, 1, 4, 1, 81, 27, 4, 1),
    _SmartViNetMaxNumOfNets_Type()
)
smartViNetMaxNumOfNets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smartViNetMaxNumOfNets.setStatus("mandatory")


class _SmartViNetCurrentBridge_Type(Integer32):
    """Custom type smartViNetCurrentBridge based on Integer32"""
    defaultValue = 0


_SmartViNetCurrentBridge_Object = MibScalar
smartViNetCurrentBridge = _SmartViNetCurrentBridge_Object(
    (1, 3, 6, 1, 4, 1, 81, 27, 4, 2),
    _SmartViNetCurrentBridge_Type()
)
smartViNetCurrentBridge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smartViNetCurrentBridge.setStatus("mandatory")
_SmartViNetTable_Object = MibTable
smartViNetTable = _SmartViNetTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 27, 4, 3)
)
if mibBuilder.loadTexts:
    smartViNetTable.setStatus("mandatory")
_SmartViNetEntry_Object = MibTableRow
smartViNetEntry = _SmartViNetEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 27, 4, 3, 1)
)
smartViNetEntry.setIndexNames(
    (0, "SMARTD-MIB", "smartViNetNumberPlusOne"),
)
if mibBuilder.loadTexts:
    smartViNetEntry.setStatus("mandatory")
_SmartViNetNumberPlusOne_Type = Integer32
_SmartViNetNumberPlusOne_Object = MibTableColumn
smartViNetNumberPlusOne = _SmartViNetNumberPlusOne_Object(
    (1, 3, 6, 1, 4, 1, 81, 27, 4, 3, 1, 1),
    _SmartViNetNumberPlusOne_Type()
)
smartViNetNumberPlusOne.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smartViNetNumberPlusOne.setStatus("mandatory")
_SmartViNetNumOfMembers_Type = Integer32
_SmartViNetNumOfMembers_Object = MibTableColumn
smartViNetNumOfMembers = _SmartViNetNumOfMembers_Object(
    (1, 3, 6, 1, 4, 1, 81, 27, 4, 3, 1, 2),
    _SmartViNetNumOfMembers_Type()
)
smartViNetNumOfMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smartViNetNumOfMembers.setStatus("mandatory")
_SmartViNetElanTable_Object = MibTable
smartViNetElanTable = _SmartViNetElanTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 27, 4, 4)
)
if mibBuilder.loadTexts:
    smartViNetElanTable.setStatus("mandatory")
_SmartViNetElanEntry_Object = MibTableRow
smartViNetElanEntry = _SmartViNetElanEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 27, 4, 4, 1)
)
smartViNetElanEntry.setIndexNames(
    (0, "SMARTD-MIB", "smartViNetElanAssociation"),
)
if mibBuilder.loadTexts:
    smartViNetElanEntry.setStatus("mandatory")
_SmartViNetElanAssociation_Type = Integer32
_SmartViNetElanAssociation_Object = MibTableColumn
smartViNetElanAssociation = _SmartViNetElanAssociation_Object(
    (1, 3, 6, 1, 4, 1, 81, 27, 4, 4, 1, 1),
    _SmartViNetElanAssociation_Type()
)
smartViNetElanAssociation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smartViNetElanAssociation.setStatus("mandatory")


class _SmartViNetElanViNet_Type(Integer32):
    """Custom type smartViNetElanViNet based on Integer32"""
    defaultValue = 511


_SmartViNetElanViNet_Object = MibTableColumn
smartViNetElanViNet = _SmartViNetElanViNet_Object(
    (1, 3, 6, 1, 4, 1, 81, 27, 4, 4, 1, 2),
    _SmartViNetElanViNet_Type()
)
smartViNetElanViNet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smartViNetElanViNet.setStatus("mandatory")


class _SmartViNetElanName_Type(DisplayString):
    """Custom type smartViNetElanName based on DisplayString"""
    defaultValue = OctetString("default")


_SmartViNetElanName_Object = MibTableColumn
smartViNetElanName = _SmartViNetElanName_Object(
    (1, 3, 6, 1, 4, 1, 81, 27, 4, 4, 1, 3),
    _SmartViNetElanName_Type()
)
smartViNetElanName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smartViNetElanName.setStatus("mandatory")


class _SmartViNetElanEntryStatus_Type(Integer32):
    """Custom type smartViNetElanEntryStatus based on Integer32"""
    defaultValue = 1

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
        *(("active", 1),
          ("createAndWait", 4),
          ("destroy", 5),
          ("notInService", 2),
          ("notReady", 3))
    )


_SmartViNetElanEntryStatus_Type.__name__ = "Integer32"
_SmartViNetElanEntryStatus_Object = MibTableColumn
smartViNetElanEntryStatus = _SmartViNetElanEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 27, 4, 4, 1, 4),
    _SmartViNetElanEntryStatus_Type()
)
smartViNetElanEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smartViNetElanEntryStatus.setStatus("mandatory")


class _SmartViNetElanIfIndex_Type(Integer32):
    """Custom type smartViNetElanIfIndex based on Integer32"""
    defaultValue = 0


_SmartViNetElanIfIndex_Object = MibTableColumn
smartViNetElanIfIndex = _SmartViNetElanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 81, 27, 4, 4, 1, 5),
    _SmartViNetElanIfIndex_Type()
)
smartViNetElanIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smartViNetElanIfIndex.setStatus("mandatory")
_SmartViNetFdbTable_Object = MibTable
smartViNetFdbTable = _SmartViNetFdbTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 27, 4, 5)
)
if mibBuilder.loadTexts:
    smartViNetFdbTable.setStatus("mandatory")
_SmartViNetFdbEntry_Object = MibTableRow
smartViNetFdbEntry = _SmartViNetFdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 27, 4, 5, 1)
)
smartViNetFdbEntry.setIndexNames(
    (0, "SMARTD-MIB", "smartViNetFdbPlusOne"),
    (0, "SMARTD-MIB", "smartViNetFdbAddress"),
)
if mibBuilder.loadTexts:
    smartViNetFdbEntry.setStatus("mandatory")
_SmartViNetFdbPlusOne_Type = Integer32
_SmartViNetFdbPlusOne_Object = MibTableColumn
smartViNetFdbPlusOne = _SmartViNetFdbPlusOne_Object(
    (1, 3, 6, 1, 4, 1, 81, 27, 4, 5, 1, 1),
    _SmartViNetFdbPlusOne_Type()
)
smartViNetFdbPlusOne.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smartViNetFdbPlusOne.setStatus("mandatory")
_SmartViNetFdbAddress_Type = MacAddress
_SmartViNetFdbAddress_Object = MibTableColumn
smartViNetFdbAddress = _SmartViNetFdbAddress_Object(
    (1, 3, 6, 1, 4, 1, 81, 27, 4, 5, 1, 2),
    _SmartViNetFdbAddress_Type()
)
smartViNetFdbAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smartViNetFdbAddress.setStatus("mandatory")
_SmartViNetFdbPort_Type = Integer32
_SmartViNetFdbPort_Object = MibTableColumn
smartViNetFdbPort = _SmartViNetFdbPort_Object(
    (1, 3, 6, 1, 4, 1, 81, 27, 4, 5, 1, 3),
    _SmartViNetFdbPort_Type()
)
smartViNetFdbPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smartViNetFdbPort.setStatus("mandatory")


class _SmartViNetFdbStatus_Type(Integer32):
    """Custom type smartViNetFdbStatus based on Integer32"""
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
        *(("invalid", 2),
          ("learned", 3),
          ("mgmt", 5),
          ("other", 1),
          ("self", 4))
    )


_SmartViNetFdbStatus_Type.__name__ = "Integer32"
_SmartViNetFdbStatus_Object = MibTableColumn
smartViNetFdbStatus = _SmartViNetFdbStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 27, 4, 5, 1, 4),
    _SmartViNetFdbStatus_Type()
)
smartViNetFdbStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smartViNetFdbStatus.setStatus("mandatory")
_SmartViNetStpTable_Object = MibTable
smartViNetStpTable = _SmartViNetStpTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 27, 4, 6)
)
if mibBuilder.loadTexts:
    smartViNetStpTable.setStatus("mandatory")
_SmartViNetStpEntry_Object = MibTableRow
smartViNetStpEntry = _SmartViNetStpEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 27, 4, 6, 1)
)
smartViNetStpEntry.setIndexNames(
    (0, "SMARTD-MIB", "smartViNetStpPlusOne"),
)
if mibBuilder.loadTexts:
    smartViNetStpEntry.setStatus("mandatory")
_SmartViNetStpPlusOne_Type = Integer32
_SmartViNetStpPlusOne_Object = MibTableColumn
smartViNetStpPlusOne = _SmartViNetStpPlusOne_Object(
    (1, 3, 6, 1, 4, 1, 81, 27, 4, 6, 1, 1),
    _SmartViNetStpPlusOne_Type()
)
smartViNetStpPlusOne.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smartViNetStpPlusOne.setStatus("mandatory")


class _SmartViNetStpPriority_Type(Integer32):
    """Custom type smartViNetStpPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SmartViNetStpPriority_Type.__name__ = "Integer32"
_SmartViNetStpPriority_Object = MibTableColumn
smartViNetStpPriority = _SmartViNetStpPriority_Object(
    (1, 3, 6, 1, 4, 1, 81, 27, 4, 6, 1, 2),
    _SmartViNetStpPriority_Type()
)
smartViNetStpPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smartViNetStpPriority.setStatus("mandatory")
_SmartViNetStpTimeSinceTopologyChange_Type = TimeTicks
_SmartViNetStpTimeSinceTopologyChange_Object = MibTableColumn
smartViNetStpTimeSinceTopologyChange = _SmartViNetStpTimeSinceTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 81, 27, 4, 6, 1, 3),
    _SmartViNetStpTimeSinceTopologyChange_Type()
)
smartViNetStpTimeSinceTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smartViNetStpTimeSinceTopologyChange.setStatus("mandatory")
_SmartViNetStpTopChanges_Type = Counter32
_SmartViNetStpTopChanges_Object = MibTableColumn
smartViNetStpTopChanges = _SmartViNetStpTopChanges_Object(
    (1, 3, 6, 1, 4, 1, 81, 27, 4, 6, 1, 4),
    _SmartViNetStpTopChanges_Type()
)
smartViNetStpTopChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smartViNetStpTopChanges.setStatus("mandatory")


class _SmartViNetStpDesignatedRoot_Type(OctetString):
    """Custom type smartViNetStpDesignatedRoot based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_SmartViNetStpDesignatedRoot_Type.__name__ = "OctetString"
_SmartViNetStpDesignatedRoot_Object = MibTableColumn
smartViNetStpDesignatedRoot = _SmartViNetStpDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 81, 27, 4, 6, 1, 5),
    _SmartViNetStpDesignatedRoot_Type()
)
smartViNetStpDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smartViNetStpDesignatedRoot.setStatus("mandatory")
_SmartViNetStpRootCost_Type = Integer32
_SmartViNetStpRootCost_Object = MibTableColumn
smartViNetStpRootCost = _SmartViNetStpRootCost_Object(
    (1, 3, 6, 1, 4, 1, 81, 27, 4, 6, 1, 6),
    _SmartViNetStpRootCost_Type()
)
smartViNetStpRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smartViNetStpRootCost.setStatus("mandatory")
_SmartViNetStpRootPort_Type = Integer32
_SmartViNetStpRootPort_Object = MibTableColumn
smartViNetStpRootPort = _SmartViNetStpRootPort_Object(
    (1, 3, 6, 1, 4, 1, 81, 27, 4, 6, 1, 7),
    _SmartViNetStpRootPort_Type()
)
smartViNetStpRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smartViNetStpRootPort.setStatus("mandatory")
_SmartViNetStpMaxAge_Type = Timeout
_SmartViNetStpMaxAge_Object = MibTableColumn
smartViNetStpMaxAge = _SmartViNetStpMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 81, 27, 4, 6, 1, 8),
    _SmartViNetStpMaxAge_Type()
)
smartViNetStpMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smartViNetStpMaxAge.setStatus("mandatory")
_SmartViNetStpHelloTime_Type = Timeout
_SmartViNetStpHelloTime_Object = MibTableColumn
smartViNetStpHelloTime = _SmartViNetStpHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 81, 27, 4, 6, 1, 9),
    _SmartViNetStpHelloTime_Type()
)
smartViNetStpHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smartViNetStpHelloTime.setStatus("mandatory")
_SmartViNetStpHoldTime_Type = Integer32
_SmartViNetStpHoldTime_Object = MibTableColumn
smartViNetStpHoldTime = _SmartViNetStpHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 81, 27, 4, 6, 1, 10),
    _SmartViNetStpHoldTime_Type()
)
smartViNetStpHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smartViNetStpHoldTime.setStatus("mandatory")
_SmartViNetStpForwardDelay_Type = Timeout
_SmartViNetStpForwardDelay_Object = MibTableColumn
smartViNetStpForwardDelay = _SmartViNetStpForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 81, 27, 4, 6, 1, 11),
    _SmartViNetStpForwardDelay_Type()
)
smartViNetStpForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smartViNetStpForwardDelay.setStatus("mandatory")


class _SmartViNetStpBridgeMaxAge_Type(Timeout):
    """Custom type smartViNetStpBridgeMaxAge based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(600, 4000),
    )


_SmartViNetStpBridgeMaxAge_Type.__name__ = "Timeout"
_SmartViNetStpBridgeMaxAge_Object = MibTableColumn
smartViNetStpBridgeMaxAge = _SmartViNetStpBridgeMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 81, 27, 4, 6, 1, 12),
    _SmartViNetStpBridgeMaxAge_Type()
)
smartViNetStpBridgeMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smartViNetStpBridgeMaxAge.setStatus("mandatory")


class _SmartViNetStpBridgeHelloTime_Type(Timeout):
    """Custom type smartViNetStpBridgeHelloTime based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_SmartViNetStpBridgeHelloTime_Type.__name__ = "Timeout"
_SmartViNetStpBridgeHelloTime_Object = MibTableColumn
smartViNetStpBridgeHelloTime = _SmartViNetStpBridgeHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 81, 27, 4, 6, 1, 13),
    _SmartViNetStpBridgeHelloTime_Type()
)
smartViNetStpBridgeHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smartViNetStpBridgeHelloTime.setStatus("mandatory")


class _SmartViNetStpBridgeForwardDelay_Type(Timeout):
    """Custom type smartViNetStpBridgeForwardDelay based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(400, 3000),
    )


_SmartViNetStpBridgeForwardDelay_Type.__name__ = "Timeout"
_SmartViNetStpBridgeForwardDelay_Object = MibTableColumn
smartViNetStpBridgeForwardDelay = _SmartViNetStpBridgeForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 81, 27, 4, 6, 1, 14),
    _SmartViNetStpBridgeForwardDelay_Type()
)
smartViNetStpBridgeForwardDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smartViNetStpBridgeForwardDelay.setStatus("mandatory")
_SmartViNetStpLastChange_Type = TimeTicks
_SmartViNetStpLastChange_Object = MibTableColumn
smartViNetStpLastChange = _SmartViNetStpLastChange_Object(
    (1, 3, 6, 1, 4, 1, 81, 27, 4, 6, 1, 15),
    _SmartViNetStpLastChange_Type()
)
smartViNetStpLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smartViNetStpLastChange.setStatus("mandatory")


class _SmartViNetConsoleManagement_Type(Integer32):
    """Custom type smartViNetConsoleManagement based on Integer32"""
    defaultValue = 0


_SmartViNetConsoleManagement_Object = MibScalar
smartViNetConsoleManagement = _SmartViNetConsoleManagement_Object(
    (1, 3, 6, 1, 4, 1, 81, 27, 4, 7),
    _SmartViNetConsoleManagement_Type()
)
smartViNetConsoleManagement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smartViNetConsoleManagement.setStatus("mandatory")
_SmartFatherHub_ObjectIdentity = ObjectIdentity
smartFatherHub = _SmartFatherHub_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 27, 5)
)


class _SmartFatherNumberOfMac_Type(Integer32):
    """Custom type smartFatherNumberOfMac based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_SmartFatherNumberOfMac_Type.__name__ = "Integer32"
_SmartFatherNumberOfMac_Object = MibScalar
smartFatherNumberOfMac = _SmartFatherNumberOfMac_Object(
    (1, 3, 6, 1, 4, 1, 81, 27, 5, 1),
    _SmartFatherNumberOfMac_Type()
)
smartFatherNumberOfMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smartFatherNumberOfMac.setStatus("mandatory")


class _SmartFatherMacList_Type(OctetString):
    """Custom type smartFatherMacList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 36),
    )


_SmartFatherMacList_Type.__name__ = "OctetString"
_SmartFatherMacList_Object = MibScalar
smartFatherMacList = _SmartFatherMacList_Object(
    (1, 3, 6, 1, 4, 1, 81, 27, 5, 2),
    _SmartFatherMacList_Type()
)
smartFatherMacList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smartFatherMacList.setStatus("mandatory")
_SmartLSFddi_ObjectIdentity = ObjectIdentity
smartLSFddi = _SmartLSFddi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 27, 6)
)
_SmartLSFTable_Object = MibTable
smartLSFTable = _SmartLSFTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 27, 6, 1)
)
if mibBuilder.loadTexts:
    smartLSFTable.setStatus("mandatory")
_SmartLSFEntry_Object = MibTableRow
smartLSFEntry = _SmartLSFEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 27, 6, 1, 1)
)
smartLSFEntry.setIndexNames(
    (0, "SMARTD-MIB", "smartLSFMACAddr"),
)
if mibBuilder.loadTexts:
    smartLSFEntry.setStatus("mandatory")
_SmartLSFMACAddr_Type = OctetString
_SmartLSFMACAddr_Object = MibTableColumn
smartLSFMACAddr = _SmartLSFMACAddr_Object(
    (1, 3, 6, 1, 4, 1, 81, 27, 6, 1, 1, 1),
    _SmartLSFMACAddr_Type()
)
smartLSFMACAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smartLSFMACAddr.setStatus("mandatory")


class _SmartLSFEntryStatus_Type(Integer32):
    """Custom type smartLSFEntryStatus based on Integer32"""
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
        *(("active", 1),
          ("createAndWait", 4),
          ("destroy", 5),
          ("notInService", 2),
          ("notReady", 3))
    )


_SmartLSFEntryStatus_Type.__name__ = "Integer32"
_SmartLSFEntryStatus_Object = MibTableColumn
smartLSFEntryStatus = _SmartLSFEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 27, 6, 1, 1, 2),
    _SmartLSFEntryStatus_Type()
)
smartLSFEntryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smartLSFEntryStatus.setStatus("mandatory")
_MacInFrames_Type = Counter32
_MacInFrames_Object = MibScalar
macInFrames = _MacInFrames_Object(
    (1, 3, 6, 1, 4, 1, 81, 27, 6, 2),
    _MacInFrames_Type()
)
macInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macInFrames.setStatus("mandatory")
_MacCopiedFrames_Type = Counter32
_MacCopiedFrames_Object = MibScalar
macCopiedFrames = _MacCopiedFrames_Object(
    (1, 3, 6, 1, 4, 1, 81, 27, 6, 3),
    _MacCopiedFrames_Type()
)
macCopiedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macCopiedFrames.setStatus("mandatory")
_MacOutFrames_Type = Counter32
_MacOutFrames_Object = MibScalar
macOutFrames = _MacOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 81, 27, 6, 4),
    _MacOutFrames_Type()
)
macOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macOutFrames.setStatus("mandatory")
_MacTokenRcvd_Type = Counter32
_MacTokenRcvd_Object = MibScalar
macTokenRcvd = _MacTokenRcvd_Object(
    (1, 3, 6, 1, 4, 1, 81, 27, 6, 5),
    _MacTokenRcvd_Type()
)
macTokenRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macTokenRcvd.setStatus("mandatory")
_MacErrFrames_Type = Counter32
_MacErrFrames_Object = MibScalar
macErrFrames = _MacErrFrames_Object(
    (1, 3, 6, 1, 4, 1, 81, 27, 6, 6),
    _MacErrFrames_Type()
)
macErrFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macErrFrames.setStatus("mandatory")
_MacLostFrames_Type = Counter32
_MacLostFrames_Object = MibScalar
macLostFrames = _MacLostFrames_Object(
    (1, 3, 6, 1, 4, 1, 81, 27, 6, 7),
    _MacLostFrames_Type()
)
macLostFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macLostFrames.setStatus("mandatory")
_MacNotCopiedFrames_Type = Counter32
_MacNotCopiedFrames_Object = MibScalar
macNotCopiedFrames = _MacNotCopiedFrames_Object(
    (1, 3, 6, 1, 4, 1, 81, 27, 6, 8),
    _MacNotCopiedFrames_Type()
)
macNotCopiedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macNotCopiedFrames.setStatus("mandatory")
_MacRingOpState_Type = Counter32
_MacRingOpState_Object = MibScalar
macRingOpState = _MacRingOpState_Object(
    (1, 3, 6, 1, 4, 1, 81, 27, 6, 9),
    _MacRingOpState_Type()
)
macRingOpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macRingOpState.setStatus("mandatory")
_FddiRingUtilization_Type = Integer32
_FddiRingUtilization_Object = MibScalar
fddiRingUtilization = _FddiRingUtilization_Object(
    (1, 3, 6, 1, 4, 1, 81, 27, 6, 10),
    _FddiRingUtilization_Type()
)
fddiRingUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddiRingUtilization.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SMARTD-MIB",
    **{"Timeout": Timeout,
       "MacAddress": MacAddress,
       "smartDevices": smartDevices,
       "smartGeneral": smartGeneral,
       "smartGenSWVersion": smartGenSWVersion,
       "smartGenOSVersion": smartGenOSVersion,
       "smartGenSoftwareDscr": smartGenSoftwareDscr,
       "smartGenBootVersion": smartGenBootVersion,
       "smartGenReset": smartGenReset,
       "smartGenHardwareVersion": smartGenHardwareVersion,
       "smartGenMonitoringPort": smartGenMonitoringPort,
       "smartGenMonitoredPort": smartGenMonitoredPort,
       "smartGenLastChange": smartGenLastChange,
       "smartGenMonitorMode": smartGenMonitorMode,
       "smartGenNetworkPrefix": smartGenNetworkPrefix,
       "smartGenConnectMode": smartGenConnectMode,
       "smartGenPvcVP": smartGenPvcVP,
       "smartGenPvcVC": smartGenPvcVC,
       "smartGenSlotNumber": smartGenSlotNumber,
       "smartGenHubMgmtIfType": smartGenHubMgmtIfType,
       "smartGenHubAddr": smartGenHubAddr,
       "smartAgent": smartAgent,
       "smartAgCoprocCommStatus": smartAgCoprocCommStatus,
       "smartAgCommDebugMode": smartAgCommDebugMode,
       "smartAgConfigChangeTraps": smartAgConfigChangeTraps,
       "smartAgFaultTraps": smartAgFaultTraps,
       "smartAgLaneFaultTraps": smartAgLaneFaultTraps,
       "smartAgSoftwareStatus": smartAgSoftwareStatus,
       "smartIfExtension": smartIfExtension,
       "smartIfExtensionTable": smartIfExtensionTable,
       "smartIfExtensionEntry": smartIfExtensionEntry,
       "smartIfExtensionEthStatus": smartIfExtensionEthStatus,
       "smartIfExtensionActivity": smartIfExtensionActivity,
       "smartIfExtensionViNet": smartIfExtensionViNet,
       "smartIfExtensionPriorityLevel": smartIfExtensionPriorityLevel,
       "smartIfExtensionBridgeEnable": smartIfExtensionBridgeEnable,
       "smartIfExtensionBackPressure": smartIfExtensionBackPressure,
       "smartIfExtensionSTAEnable": smartIfExtensionSTAEnable,
       "smartViNet": smartViNet,
       "smartViNetMaxNumOfNets": smartViNetMaxNumOfNets,
       "smartViNetCurrentBridge": smartViNetCurrentBridge,
       "smartViNetTable": smartViNetTable,
       "smartViNetEntry": smartViNetEntry,
       "smartViNetNumberPlusOne": smartViNetNumberPlusOne,
       "smartViNetNumOfMembers": smartViNetNumOfMembers,
       "smartViNetElanTable": smartViNetElanTable,
       "smartViNetElanEntry": smartViNetElanEntry,
       "smartViNetElanAssociation": smartViNetElanAssociation,
       "smartViNetElanViNet": smartViNetElanViNet,
       "smartViNetElanName": smartViNetElanName,
       "smartViNetElanEntryStatus": smartViNetElanEntryStatus,
       "smartViNetElanIfIndex": smartViNetElanIfIndex,
       "smartViNetFdbTable": smartViNetFdbTable,
       "smartViNetFdbEntry": smartViNetFdbEntry,
       "smartViNetFdbPlusOne": smartViNetFdbPlusOne,
       "smartViNetFdbAddress": smartViNetFdbAddress,
       "smartViNetFdbPort": smartViNetFdbPort,
       "smartViNetFdbStatus": smartViNetFdbStatus,
       "smartViNetStpTable": smartViNetStpTable,
       "smartViNetStpEntry": smartViNetStpEntry,
       "smartViNetStpPlusOne": smartViNetStpPlusOne,
       "smartViNetStpPriority": smartViNetStpPriority,
       "smartViNetStpTimeSinceTopologyChange": smartViNetStpTimeSinceTopologyChange,
       "smartViNetStpTopChanges": smartViNetStpTopChanges,
       "smartViNetStpDesignatedRoot": smartViNetStpDesignatedRoot,
       "smartViNetStpRootCost": smartViNetStpRootCost,
       "smartViNetStpRootPort": smartViNetStpRootPort,
       "smartViNetStpMaxAge": smartViNetStpMaxAge,
       "smartViNetStpHelloTime": smartViNetStpHelloTime,
       "smartViNetStpHoldTime": smartViNetStpHoldTime,
       "smartViNetStpForwardDelay": smartViNetStpForwardDelay,
       "smartViNetStpBridgeMaxAge": smartViNetStpBridgeMaxAge,
       "smartViNetStpBridgeHelloTime": smartViNetStpBridgeHelloTime,
       "smartViNetStpBridgeForwardDelay": smartViNetStpBridgeForwardDelay,
       "smartViNetStpLastChange": smartViNetStpLastChange,
       "smartViNetConsoleManagement": smartViNetConsoleManagement,
       "smartFatherHub": smartFatherHub,
       "smartFatherNumberOfMac": smartFatherNumberOfMac,
       "smartFatherMacList": smartFatherMacList,
       "smartLSFddi": smartLSFddi,
       "smartLSFTable": smartLSFTable,
       "smartLSFEntry": smartLSFEntry,
       "smartLSFMACAddr": smartLSFMACAddr,
       "smartLSFEntryStatus": smartLSFEntryStatus,
       "macInFrames": macInFrames,
       "macCopiedFrames": macCopiedFrames,
       "macOutFrames": macOutFrames,
       "macTokenRcvd": macTokenRcvd,
       "macErrFrames": macErrFrames,
       "macLostFrames": macLostFrames,
       "macNotCopiedFrames": macNotCopiedFrames,
       "macRingOpState": macRingOpState,
       "fddiRingUtilization": fddiRingUtilization}
)
