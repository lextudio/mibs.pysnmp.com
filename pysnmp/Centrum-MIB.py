# SNMP MIB module (Centrum-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Centrum-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:21:30 2024
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

_Centrum_ObjectIdentity = ObjectIdentity
centrum = _Centrum_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 327)
)
_MibDoc_ObjectIdentity = ObjectIdentity
mibDoc = _MibDoc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 327, 1)
)
_CentrumRemote_ObjectIdentity = ObjectIdentity
centrumRemote = _CentrumRemote_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 327, 1, 1)
)
_Port_ObjectIdentity = ObjectIdentity
port = _Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 1)
)
_PortNumber_Type = Integer32
_PortNumber_Object = MibScalar
portNumber = _PortNumber_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 1, 1),
    _PortNumber_Type()
)
portNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portNumber.setStatus("mandatory")
_PortTable_Object = MibTable
portTable = _PortTable_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    portTable.setStatus("mandatory")
_PortEntry_Object = MibTableRow
portEntry = _PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 1, 2, 1)
)
portEntry.setIndexNames(
    (0, "Centrum-MIB", "portIndex"),
)
if mibBuilder.loadTexts:
    portEntry.setStatus("mandatory")
_PortIndex_Type = Integer32
_PortIndex_Object = MibTableColumn
portIndex = _PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 1, 2, 1, 1),
    _PortIndex_Type()
)
portIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portIndex.setStatus("mandatory")


class _PortId_Type(Integer32):
    """Custom type portId based on Integer32"""
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
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
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
              65)
        )
    )
    namedValues = NamedValues(
        *(("msEthernet", 1),
          ("msTokenRing", 22),
          ("port1", 30),
          ("port2", 31),
          ("port3", 32),
          ("port4", 33),
          ("port5", 34),
          ("port6", 35),
          ("port7", 36),
          ("port8", 37),
          ("s1Async1", 4),
          ("s1Async2", 5),
          ("s1Async3", 6),
          ("s1Async4", 7),
          ("s1Async5", 8),
          ("s1Async6", 9),
          ("s1Async7", 10),
          ("s1Async8", 11),
          ("s1Br1B1", 50),
          ("s1Br1B2", 51),
          ("s1Br2B1", 52),
          ("s1Br2B2", 53),
          ("s1Br3B1", 54),
          ("s1Br3B2", 55),
          ("s1Br4B1", 56),
          ("s1Br4B2", 57),
          ("s1Ethernet", 2),
          ("s1Sync", 3),
          ("s2Async1", 14),
          ("s2Async2", 15),
          ("s2Async3", 16),
          ("s2Async4", 17),
          ("s2Async5", 18),
          ("s2Async6", 19),
          ("s2Async7", 20),
          ("s2Async8", 21),
          ("s2Br1B1", 58),
          ("s2Br1B2", 59),
          ("s2Br2B1", 60),
          ("s2Br2B2", 61),
          ("s2Br3B1", 62),
          ("s2Br3B2", 63),
          ("s2Br4B1", 64),
          ("s2Br4B2", 65),
          ("s2Ethernet", 12),
          ("s2Sync", 13))
    )


_PortId_Type.__name__ = "Integer32"
_PortId_Object = MibTableColumn
portId = _PortId_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 1, 2, 1, 2),
    _PortId_Type()
)
portId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portId.setStatus("mandatory")
_PortSlot_Type = Integer32
_PortSlot_Object = MibTableColumn
portSlot = _PortSlot_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 1, 2, 1, 3),
    _PortSlot_Type()
)
portSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSlot.setStatus("mandatory")
_PortScriptIdx_Type = Integer32
_PortScriptIdx_Object = MibTableColumn
portScriptIdx = _PortScriptIdx_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 1, 2, 1, 4),
    _PortScriptIdx_Type()
)
portScriptIdx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portScriptIdx.setStatus("mandatory")


class _PortBaudrate_Type(Integer32):
    """Custom type portBaudrate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(24,
              48,
              96,
              192,
              384,
              560,
              576,
              1152)
        )
    )
    namedValues = NamedValues(
        *(("baud-115200", 1152),
          ("baud-19200", 192),
          ("baud-2400", 24),
          ("baud-38400", 384),
          ("baud-4800", 48),
          ("baud-56000", 560),
          ("baud-57600", 576),
          ("baud-9600", 96))
    )


_PortBaudrate_Type.__name__ = "Integer32"
_PortBaudrate_Object = MibTableColumn
portBaudrate = _PortBaudrate_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 1, 2, 1, 5),
    _PortBaudrate_Type()
)
portBaudrate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portBaudrate.setStatus("mandatory")


class _PortParity_Type(Integer32):
    """Custom type portParity based on Integer32"""
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
        *(("even", 2),
          ("none", 5),
          ("odd", 1),
          ("one", 4),
          ("zero", 3))
    )


_PortParity_Type.__name__ = "Integer32"
_PortParity_Object = MibTableColumn
portParity = _PortParity_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 1, 2, 1, 6),
    _PortParity_Type()
)
portParity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portParity.setStatus("mandatory")


class _PortStopBits_Type(Integer32):
    """Custom type portStopBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bit-1", 1),
          ("bit-15", 2),
          ("bits-2", 3))
    )


_PortStopBits_Type.__name__ = "Integer32"
_PortStopBits_Object = MibTableColumn
portStopBits = _PortStopBits_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 1, 2, 1, 7),
    _PortStopBits_Type()
)
portStopBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portStopBits.setStatus("mandatory")


class _PortDataBits_Type(Integer32):
    """Custom type portDataBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("bits-5", 5),
          ("bits-6", 6),
          ("bits-7", 7),
          ("bits-8", 8))
    )


_PortDataBits_Type.__name__ = "Integer32"
_PortDataBits_Object = MibTableColumn
portDataBits = _PortDataBits_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 1, 2, 1, 8),
    _PortDataBits_Type()
)
portDataBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portDataBits.setStatus("mandatory")


class _PortCCSP_Type(Integer32):
    """Custom type portCCSP based on Integer32"""
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


_PortCCSP_Type.__name__ = "Integer32"
_PortCCSP_Object = MibTableColumn
portCCSP = _PortCCSP_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 1, 2, 1, 9),
    _PortCCSP_Type()
)
portCCSP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portCCSP.setStatus("mandatory")
_PortPPPProbeInterval_Type = Integer32
_PortPPPProbeInterval_Object = MibTableColumn
portPPPProbeInterval = _PortPPPProbeInterval_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 1, 2, 1, 10),
    _PortPPPProbeInterval_Type()
)
portPPPProbeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portPPPProbeInterval.setStatus("mandatory")
_PortPPPMaxRcvPacketLength_Type = Integer32
_PortPPPMaxRcvPacketLength_Object = MibTableColumn
portPPPMaxRcvPacketLength = _PortPPPMaxRcvPacketLength_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 1, 2, 1, 11),
    _PortPPPMaxRcvPacketLength_Type()
)
portPPPMaxRcvPacketLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portPPPMaxRcvPacketLength.setStatus("mandatory")
_PortPPPAsyncCtrlChar_Type = Integer32
_PortPPPAsyncCtrlChar_Object = MibTableColumn
portPPPAsyncCtrlChar = _PortPPPAsyncCtrlChar_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 1, 2, 1, 12),
    _PortPPPAsyncCtrlChar_Type()
)
portPPPAsyncCtrlChar.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portPPPAsyncCtrlChar.setStatus("mandatory")


class _PortPPPProtCompress_Type(Integer32):
    """Custom type portPPPProtCompress based on Integer32"""
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


_PortPPPProtCompress_Type.__name__ = "Integer32"
_PortPPPProtCompress_Object = MibTableColumn
portPPPProtCompress = _PortPPPProtCompress_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 1, 2, 1, 14),
    _PortPPPProtCompress_Type()
)
portPPPProtCompress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portPPPProtCompress.setStatus("mandatory")


class _PortPPPACCompress_Type(Integer32):
    """Custom type portPPPACCompress based on Integer32"""
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


_PortPPPACCompress_Type.__name__ = "Integer32"
_PortPPPACCompress_Object = MibTableColumn
portPPPACCompress = _PortPPPACCompress_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 1, 2, 1, 15),
    _PortPPPACCompress_Type()
)
portPPPACCompress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portPPPACCompress.setStatus("mandatory")
_PortCRCErrors_Type = Counter32
_PortCRCErrors_Object = MibTableColumn
portCRCErrors = _PortCRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 1, 2, 1, 16),
    _PortCRCErrors_Type()
)
portCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portCRCErrors.setStatus("mandatory")
_PortOversizes_Type = Counter32
_PortOversizes_Object = MibTableColumn
portOversizes = _PortOversizes_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 1, 2, 1, 17),
    _PortOversizes_Type()
)
portOversizes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portOversizes.setStatus("mandatory")
_PortUndersizes_Type = Counter32
_PortUndersizes_Object = MibTableColumn
portUndersizes = _PortUndersizes_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 1, 2, 1, 18),
    _PortUndersizes_Type()
)
portUndersizes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portUndersizes.setStatus("mandatory")
_PortCollisions_Type = Counter32
_PortCollisions_Object = MibTableColumn
portCollisions = _PortCollisions_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 1, 2, 1, 19),
    _PortCollisions_Type()
)
portCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portCollisions.setStatus("mandatory")
_PortInPackets_Type = Counter32
_PortInPackets_Object = MibTableColumn
portInPackets = _PortInPackets_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 1, 2, 1, 20),
    _PortInPackets_Type()
)
portInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portInPackets.setStatus("mandatory")
_PortOutPackets_Type = Counter32
_PortOutPackets_Object = MibTableColumn
portOutPackets = _PortOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 1, 2, 1, 21),
    _PortOutPackets_Type()
)
portOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portOutPackets.setStatus("mandatory")
_PortInBytes_Type = Counter32
_PortInBytes_Object = MibTableColumn
portInBytes = _PortInBytes_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 1, 2, 1, 22),
    _PortInBytes_Type()
)
portInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portInBytes.setStatus("mandatory")
_PortOutBytes_Type = Counter32
_PortOutBytes_Object = MibTableColumn
portOutBytes = _PortOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 1, 2, 1, 23),
    _PortOutBytes_Type()
)
portOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portOutBytes.setStatus("mandatory")
_PortResetPortCounters_Type = Integer32
_PortResetPortCounters_Object = MibTableColumn
portResetPortCounters = _PortResetPortCounters_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 1, 2, 1, 24),
    _PortResetPortCounters_Type()
)
portResetPortCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portResetPortCounters.setStatus("mandatory")
_PortAsyncParityErrors_Type = Counter32
_PortAsyncParityErrors_Object = MibTableColumn
portAsyncParityErrors = _PortAsyncParityErrors_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 1, 2, 1, 25),
    _PortAsyncParityErrors_Type()
)
portAsyncParityErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portAsyncParityErrors.setStatus("mandatory")
_PortAsyncCharFrameErrors_Type = Counter32
_PortAsyncCharFrameErrors_Object = MibTableColumn
portAsyncCharFrameErrors = _PortAsyncCharFrameErrors_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 1, 2, 1, 26),
    _PortAsyncCharFrameErrors_Type()
)
portAsyncCharFrameErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portAsyncCharFrameErrors.setStatus("mandatory")
_PortAsyncOverrunErrors_Type = Counter32
_PortAsyncOverrunErrors_Object = MibTableColumn
portAsyncOverrunErrors = _PortAsyncOverrunErrors_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 1, 2, 1, 27),
    _PortAsyncOverrunErrors_Type()
)
portAsyncOverrunErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portAsyncOverrunErrors.setStatus("mandatory")
_PortAsyncPktCksumErrors_Type = Counter32
_PortAsyncPktCksumErrors_Object = MibTableColumn
portAsyncPktCksumErrors = _PortAsyncPktCksumErrors_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 1, 2, 1, 28),
    _PortAsyncPktCksumErrors_Type()
)
portAsyncPktCksumErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portAsyncPktCksumErrors.setStatus("mandatory")


class _PortCTSState_Type(Integer32):
    """Custom type portCTSState based on Integer32"""
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


_PortCTSState_Type.__name__ = "Integer32"
_PortCTSState_Object = MibTableColumn
portCTSState = _PortCTSState_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 1, 2, 1, 29),
    _PortCTSState_Type()
)
portCTSState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portCTSState.setStatus("mandatory")


class _PortDCDState_Type(Integer32):
    """Custom type portDCDState based on Integer32"""
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


_PortDCDState_Type.__name__ = "Integer32"
_PortDCDState_Object = MibTableColumn
portDCDState = _PortDCDState_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 1, 2, 1, 30),
    _PortDCDState_Type()
)
portDCDState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDCDState.setStatus("mandatory")


class _PortRIState_Type(Integer32):
    """Custom type portRIState based on Integer32"""
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


_PortRIState_Type.__name__ = "Integer32"
_PortRIState_Object = MibTableColumn
portRIState = _PortRIState_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 1, 2, 1, 31),
    _PortRIState_Type()
)
portRIState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portRIState.setStatus("mandatory")
_PortSyncFcsErrors_Type = Counter32
_PortSyncFcsErrors_Object = MibTableColumn
portSyncFcsErrors = _PortSyncFcsErrors_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 1, 2, 1, 32),
    _PortSyncFcsErrors_Type()
)
portSyncFcsErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSyncFcsErrors.setStatus("mandatory")
_PortSyncMemoryErrors_Type = Counter32
_PortSyncMemoryErrors_Object = MibTableColumn
portSyncMemoryErrors = _PortSyncMemoryErrors_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 1, 2, 1, 33),
    _PortSyncMemoryErrors_Type()
)
portSyncMemoryErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSyncMemoryErrors.setStatus("mandatory")
_PortSyncOverrunErrors_Type = Counter32
_PortSyncOverrunErrors_Object = MibTableColumn
portSyncOverrunErrors = _PortSyncOverrunErrors_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 1, 2, 1, 34),
    _PortSyncOverrunErrors_Type()
)
portSyncOverrunErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSyncOverrunErrors.setStatus("mandatory")
_PortSyncUnderrunErrors_Type = Counter32
_PortSyncUnderrunErrors_Object = MibTableColumn
portSyncUnderrunErrors = _PortSyncUnderrunErrors_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 1, 2, 1, 35),
    _PortSyncUnderrunErrors_Type()
)
portSyncUnderrunErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSyncUnderrunErrors.setStatus("mandatory")


class _PortIPCPState_Type(Integer32):
    """Custom type portIPCPState based on Integer32"""
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


_PortIPCPState_Type.__name__ = "Integer32"
_PortIPCPState_Object = MibTableColumn
portIPCPState = _PortIPCPState_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 1, 2, 1, 36),
    _PortIPCPState_Type()
)
portIPCPState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portIPCPState.setStatus("mandatory")


class _PortIPXCPState_Type(Integer32):
    """Custom type portIPXCPState based on Integer32"""
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


_PortIPXCPState_Type.__name__ = "Integer32"
_PortIPXCPState_Object = MibTableColumn
portIPXCPState = _PortIPXCPState_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 1, 2, 1, 37),
    _PortIPXCPState_Type()
)
portIPXCPState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portIPXCPState.setStatus("mandatory")


class _PortBNCPState_Type(Integer32):
    """Custom type portBNCPState based on Integer32"""
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


_PortBNCPState_Type.__name__ = "Integer32"
_PortBNCPState_Object = MibTableColumn
portBNCPState = _PortBNCPState_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 1, 2, 1, 38),
    _PortBNCPState_Type()
)
portBNCPState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portBNCPState.setStatus("mandatory")


class _PortDriverState_Type(Integer32):
    """Custom type portDriverState based on Integer32"""
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
        *(("init", 3),
          ("off", 1),
          ("online", 5),
          ("open", 4),
          ("reset", 2))
    )


_PortDriverState_Type.__name__ = "Integer32"
_PortDriverState_Object = MibTableColumn
portDriverState = _PortDriverState_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 1, 2, 1, 39),
    _PortDriverState_Type()
)
portDriverState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDriverState.setStatus("mandatory")


class _PortSpeed_Type(Integer32):
    """Custom type portSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              16)
        )
    )
    namedValues = NamedValues(
        *(("megabyte-16", 16),
          ("megabyte-4", 4))
    )


_PortSpeed_Type.__name__ = "Integer32"
_PortSpeed_Object = MibTableColumn
portSpeed = _PortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 1, 2, 1, 40),
    _PortSpeed_Type()
)
portSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSpeed.setStatus("mandatory")
_PortTotalErrors_Type = Counter32
_PortTotalErrors_Object = MibTableColumn
portTotalErrors = _PortTotalErrors_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 1, 2, 1, 41),
    _PortTotalErrors_Type()
)
portTotalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portTotalErrors.setStatus("mandatory")
_PortTransmitDiscards_Type = Counter32
_PortTransmitDiscards_Object = MibTableColumn
portTransmitDiscards = _PortTransmitDiscards_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 1, 2, 1, 42),
    _PortTransmitDiscards_Type()
)
portTransmitDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portTransmitDiscards.setStatus("mandatory")
_PortReceiveCongestions_Type = Counter32
_PortReceiveCongestions_Object = MibTableColumn
portReceiveCongestions = _PortReceiveCongestions_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 1, 2, 1, 43),
    _PortReceiveCongestions_Type()
)
portReceiveCongestions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portReceiveCongestions.setStatus("mandatory")
_PortUnknownProtocols_Type = Counter32
_PortUnknownProtocols_Object = MibTableColumn
portUnknownProtocols = _PortUnknownProtocols_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 1, 2, 1, 44),
    _PortUnknownProtocols_Type()
)
portUnknownProtocols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portUnknownProtocols.setStatus("mandatory")


class _PortAccessType_Type(Integer32):
    """Custom type portAccessType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("arap1-0", 2),
          ("auto", 1),
          ("router", 4))
    )


_PortAccessType_Type.__name__ = "Integer32"
_PortAccessType_Object = MibTableColumn
portAccessType = _PortAccessType_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 1, 2, 1, 45),
    _PortAccessType_Type()
)
portAccessType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portAccessType.setStatus("mandatory")
_PortDialHangUp_Type = Integer32
_PortDialHangUp_Object = MibTableColumn
portDialHangUp = _PortDialHangUp_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 1, 2, 1, 46),
    _PortDialHangUp_Type()
)
portDialHangUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portDialHangUp.setStatus("mandatory")


class _PortPortDisabled_Type(Integer32):
    """Custom type portPortDisabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_PortPortDisabled_Type.__name__ = "Integer32"
_PortPortDisabled_Object = MibTableColumn
portPortDisabled = _PortPortDisabled_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 1, 2, 1, 47),
    _PortPortDisabled_Type()
)
portPortDisabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portPortDisabled.setStatus("mandatory")


class _PortArapCompress_Type(Integer32):
    """Custom type portArapCompress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("v42bis", 1))
    )


_PortArapCompress_Type.__name__ = "Integer32"
_PortArapCompress_Object = MibTableColumn
portArapCompress = _PortArapCompress_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 1, 2, 1, 48),
    _PortArapCompress_Type()
)
portArapCompress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portArapCompress.setStatus("mandatory")


class _PortInterFace_Type(Integer32):
    """Custom type portInterFace based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("async", 1),
          ("sync", 2))
    )


_PortInterFace_Type.__name__ = "Integer32"
_PortInterFace_Object = MibTableColumn
portInterFace = _PortInterFace_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 1, 2, 1, 49),
    _PortInterFace_Type()
)
portInterFace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portInterFace.setStatus("mandatory")


class _PortLEDLink_Type(Integer32):
    """Custom type portLEDLink based on Integer32"""
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


_PortLEDLink_Type.__name__ = "Integer32"
_PortLEDLink_Object = MibTableColumn
portLEDLink = _PortLEDLink_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 1, 2, 1, 50),
    _PortLEDLink_Type()
)
portLEDLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portLEDLink.setStatus("mandatory")


class _PortLEDActivity_Type(Integer32):
    """Custom type portLEDActivity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("heavy", 3),
          ("light", 1),
          ("medium", 2))
    )


_PortLEDActivity_Type.__name__ = "Integer32"
_PortLEDActivity_Object = MibTableColumn
portLEDActivity = _PortLEDActivity_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 1, 2, 1, 51),
    _PortLEDActivity_Type()
)
portLEDActivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portLEDActivity.setStatus("mandatory")


class _PortLEDFault_Type(Integer32):
    """Custom type portLEDFault based on Integer32"""
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


_PortLEDFault_Type.__name__ = "Integer32"
_PortLEDFault_Object = MibTableColumn
portLEDFault = _PortLEDFault_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 1, 2, 1, 52),
    _PortLEDFault_Type()
)
portLEDFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portLEDFault.setStatus("mandatory")


class _PortLinkType_Type(Integer32):
    """Custom type portLinkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("dial", 0),
          ("permanent", 1))
    )


_PortLinkType_Type.__name__ = "Integer32"
_PortLinkType_Object = MibTableColumn
portLinkType = _PortLinkType_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 1, 2, 1, 53),
    _PortLinkType_Type()
)
portLinkType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portLinkType.setStatus("mandatory")


class _PortSwitchType_Type(Integer32):
    """Custom type portSwitchType based on Integer32"""
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
        *(("att5ess", 1),
          ("dms100", 2),
          ("ins64", 4),
          ("net3", 6),
          ("ni1", 3),
          ("vn3", 5))
    )


_PortSwitchType_Type.__name__ = "Integer32"
_PortSwitchType_Object = MibTableColumn
portSwitchType = _PortSwitchType_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 1, 2, 1, 54),
    _PortSwitchType_Type()
)
portSwitchType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSwitchType.setStatus("mandatory")


class _PortSPID_1_Type(DisplayString):
    """Custom type portSPID_1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_PortSPID_1_Type.__name__ = "DisplayString"
_PortSPID_1_Object = MibScalar
portSPID_1 = _PortSPID_1_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 1, 2, 1, 55),
    _PortSPID_1_Type()
)
portSPID_1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSPID_1.setStatus("mandatory")


class _PortSPID_2_Type(DisplayString):
    """Custom type portSPID_2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_PortSPID_2_Type.__name__ = "DisplayString"
_PortSPID_2_Object = MibScalar
portSPID_2 = _PortSPID_2_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 1, 2, 1, 56),
    _PortSPID_2_Type()
)
portSPID_2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSPID_2.setStatus("mandatory")


class _PortDirectoryNo_1_Type(DisplayString):
    """Custom type portDirectoryNo_1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_PortDirectoryNo_1_Type.__name__ = "DisplayString"
_PortDirectoryNo_1_Object = MibScalar
portDirectoryNo_1 = _PortDirectoryNo_1_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 1, 2, 1, 57),
    _PortDirectoryNo_1_Type()
)
portDirectoryNo_1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portDirectoryNo_1.setStatus("mandatory")


class _PortDirectoryNo_2_Type(DisplayString):
    """Custom type portDirectoryNo_2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_PortDirectoryNo_2_Type.__name__ = "DisplayString"
_PortDirectoryNo_2_Object = MibScalar
portDirectoryNo_2 = _PortDirectoryNo_2_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 1, 2, 1, 58),
    _PortDirectoryNo_2_Type()
)
portDirectoryNo_2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portDirectoryNo_2.setStatus("mandatory")


class _PortLocalDialNo_1_Type(DisplayString):
    """Custom type portLocalDialNo_1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_PortLocalDialNo_1_Type.__name__ = "DisplayString"
_PortLocalDialNo_1_Object = MibScalar
portLocalDialNo_1 = _PortLocalDialNo_1_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 1, 2, 1, 59),
    _PortLocalDialNo_1_Type()
)
portLocalDialNo_1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portLocalDialNo_1.setStatus("mandatory")


class _PortLocalDialNo_2_Type(DisplayString):
    """Custom type portLocalDialNo_2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_PortLocalDialNo_2_Type.__name__ = "DisplayString"
_PortLocalDialNo_2_Object = MibScalar
portLocalDialNo_2 = _PortLocalDialNo_2_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 1, 2, 1, 60),
    _PortLocalDialNo_2_Type()
)
portLocalDialNo_2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portLocalDialNo_2.setStatus("mandatory")


class _PortLocalSubaddress_1_Type(DisplayString):
    """Custom type portLocalSubaddress_1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_PortLocalSubaddress_1_Type.__name__ = "DisplayString"
_PortLocalSubaddress_1_Object = MibScalar
portLocalSubaddress_1 = _PortLocalSubaddress_1_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 1, 2, 1, 61),
    _PortLocalSubaddress_1_Type()
)
portLocalSubaddress_1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portLocalSubaddress_1.setStatus("mandatory")


class _PortLocalSubaddress_2_Type(DisplayString):
    """Custom type portLocalSubaddress_2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_PortLocalSubaddress_2_Type.__name__ = "DisplayString"
_PortLocalSubaddress_2_Object = MibScalar
portLocalSubaddress_2 = _PortLocalSubaddress_2_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 1, 2, 1, 62),
    _PortLocalSubaddress_2_Type()
)
portLocalSubaddress_2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portLocalSubaddress_2.setStatus("mandatory")


class _PortProtocolMode_Type(Integer32):
    """Custom type portProtocolMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("raw", 5),
          ("v-120", 4))
    )


_PortProtocolMode_Type.__name__ = "Integer32"
_PortProtocolMode_Object = MibTableColumn
portProtocolMode = _PortProtocolMode_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 1, 2, 1, 63),
    _PortProtocolMode_Type()
)
portProtocolMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portProtocolMode.setStatus("mandatory")


class _PortPortReset_Type(Integer32):
    """Custom type portPortReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_PortPortReset_Type.__name__ = "Integer32"
_PortPortReset_Object = MibTableColumn
portPortReset = _PortPortReset_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 1, 2, 1, 64),
    _PortPortReset_Type()
)
portPortReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portPortReset.setStatus("mandatory")
_PortIncomingCalls_Type = Counter32
_PortIncomingCalls_Object = MibTableColumn
portIncomingCalls = _PortIncomingCalls_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 1, 2, 1, 65),
    _PortIncomingCalls_Type()
)
portIncomingCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portIncomingCalls.setStatus("mandatory")
_PortOutgoingCalls_Type = Counter32
_PortOutgoingCalls_Object = MibTableColumn
portOutgoingCalls = _PortOutgoingCalls_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 1, 2, 1, 66),
    _PortOutgoingCalls_Type()
)
portOutgoingCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portOutgoingCalls.setStatus("mandatory")


class _PortRemoteDialNo_Type(DisplayString):
    """Custom type portRemoteDialNo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_PortRemoteDialNo_Type.__name__ = "DisplayString"
_PortRemoteDialNo_Object = MibTableColumn
portRemoteDialNo = _PortRemoteDialNo_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 1, 2, 1, 67),
    _PortRemoteDialNo_Type()
)
portRemoteDialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portRemoteDialNo.setStatus("mandatory")


class _PortRemoteSubaddress_Type(DisplayString):
    """Custom type portRemoteSubaddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_PortRemoteSubaddress_Type.__name__ = "DisplayString"
_PortRemoteSubaddress_Object = MibTableColumn
portRemoteSubaddress = _PortRemoteSubaddress_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 1, 2, 1, 68),
    _PortRemoteSubaddress_Type()
)
portRemoteSubaddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portRemoteSubaddress.setStatus("mandatory")


class _PortISDNInterfaceType_Type(DisplayString):
    """Custom type portISDNInterfaceType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_PortISDNInterfaceType_Type.__name__ = "DisplayString"
_PortISDNInterfaceType_Object = MibTableColumn
portISDNInterfaceType = _PortISDNInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 1, 2, 1, 69),
    _PortISDNInterfaceType_Type()
)
portISDNInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portISDNInterfaceType.setStatus("mandatory")


class _PortPathName_Type(DisplayString):
    """Custom type portPathName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_PortPathName_Type.__name__ = "DisplayString"
_PortPathName_Object = MibTableColumn
portPathName = _PortPathName_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 1, 2, 1, 70),
    _PortPathName_Type()
)
portPathName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portPathName.setStatus("mandatory")


class _PortILCCPState_Type(Integer32):
    """Custom type portILCCPState based on Integer32"""
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


_PortILCCPState_Type.__name__ = "Integer32"
_PortILCCPState_Object = MibTableColumn
portILCCPState = _PortILCCPState_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 1, 2, 1, 71),
    _PortILCCPState_Type()
)
portILCCPState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portILCCPState.setStatus("mandatory")


class _PortCurISDNBChannel_Type(Integer32):
    """Custom type portCurISDNBChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("b-1", 1),
          ("b-2", 2))
    )


_PortCurISDNBChannel_Type.__name__ = "Integer32"
_PortCurISDNBChannel_Object = MibTableColumn
portCurISDNBChannel = _PortCurISDNBChannel_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 1, 2, 1, 72),
    _PortCurISDNBChannel_Type()
)
portCurISDNBChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portCurISDNBChannel.setStatus("mandatory")


class _PortLoginStatus_Type(Integer32):
    """Custom type portLoginStatus based on Integer32"""
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
        *(("dial-in", 2),
          ("dial-out", 3),
          ("disabled", 4),
          ("router", 5),
          ("unused", 1))
    )


_PortLoginStatus_Type.__name__ = "Integer32"
_PortLoginStatus_Object = MibTableColumn
portLoginStatus = _PortLoginStatus_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 1, 2, 1, 73),
    _PortLoginStatus_Type()
)
portLoginStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portLoginStatus.setStatus("mandatory")


class _PortLastConnectBChannel_Type(Integer32):
    """Custom type portLastConnectBChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("b-1", 2),
          ("b-2", 3),
          ("not-used", 1))
    )


_PortLastConnectBChannel_Type.__name__ = "Integer32"
_PortLastConnectBChannel_Object = MibTableColumn
portLastConnectBChannel = _PortLastConnectBChannel_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 1, 2, 1, 74),
    _PortLastConnectBChannel_Type()
)
portLastConnectBChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portLastConnectBChannel.setStatus("mandatory")


class _PortISDNPhyLineStatus_Type(Integer32):
    """Custom type portISDNPhyLineStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("activated", 2),
          ("deactivated", 1))
    )


_PortISDNPhyLineStatus_Type.__name__ = "Integer32"
_PortISDNPhyLineStatus_Object = MibTableColumn
portISDNPhyLineStatus = _PortISDNPhyLineStatus_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 1, 2, 1, 75),
    _PortISDNPhyLineStatus_Type()
)
portISDNPhyLineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portISDNPhyLineStatus.setStatus("mandatory")


class _PortTEIState_Type(Integer32):
    """Custom type portTEIState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("assigned", 2),
          ("unassigned", 1))
    )


_PortTEIState_Type.__name__ = "Integer32"
_PortTEIState_Object = MibTableColumn
portTEIState = _PortTEIState_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 1, 2, 1, 76),
    _PortTEIState_Type()
)
portTEIState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portTEIState.setStatus("mandatory")


class _PortLayer3Status_Type(Integer32):
    """Custom type portLayer3Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("initialized", 2),
          ("uninitialized", 1))
    )


_PortLayer3Status_Type.__name__ = "Integer32"
_PortLayer3Status_Object = MibTableColumn
portLayer3Status = _PortLayer3Status_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 1, 2, 1, 77),
    _PortLayer3Status_Type()
)
portLayer3Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portLayer3Status.setStatus("mandatory")
_PortResetAllCounters_Type = Integer32
_PortResetAllCounters_Object = MibScalar
portResetAllCounters = _PortResetAllCounters_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 1, 3),
    _PortResetAllCounters_Type()
)
portResetAllCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portResetAllCounters.setStatus("mandatory")
_PortSourceRouteTable_Object = MibTable
portSourceRouteTable = _PortSourceRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 1, 4)
)
if mibBuilder.loadTexts:
    portSourceRouteTable.setStatus("mandatory")
_PortSourceRouteEntry_Object = MibTableRow
portSourceRouteEntry = _PortSourceRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 1, 4, 1)
)
portSourceRouteEntry.setIndexNames(
    (0, "Centrum-MIB", "portSRMacAddress"),
)
if mibBuilder.loadTexts:
    portSourceRouteEntry.setStatus("mandatory")


class _PortSRMacAddress_Type(OctetString):
    """Custom type portSRMacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_PortSRMacAddress_Type.__name__ = "OctetString"
_PortSRMacAddress_Object = MibTableColumn
portSRMacAddress = _PortSRMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 1, 4, 1, 1),
    _PortSRMacAddress_Type()
)
portSRMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSRMacAddress.setStatus("mandatory")


class _PortSRState_Type(Integer32):
    """Custom type portSRState based on Integer32"""
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
        *(("empty", 0),
          ("new", 2),
          ("old", 3),
          ("pending", 1))
    )


_PortSRState_Type.__name__ = "Integer32"
_PortSRState_Object = MibTableColumn
portSRState = _PortSRState_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 1, 4, 1, 2),
    _PortSRState_Type()
)
portSRState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSRState.setStatus("mandatory")
_PortSRTimeToLive_Type = Counter32
_PortSRTimeToLive_Object = MibTableColumn
portSRTimeToLive = _PortSRTimeToLive_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 1, 4, 1, 3),
    _PortSRTimeToLive_Type()
)
portSRTimeToLive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSRTimeToLive.setStatus("mandatory")
_PortSRLargestFrame_Type = Integer32
_PortSRLargestFrame_Object = MibTableColumn
portSRLargestFrame = _PortSRLargestFrame_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 1, 4, 1, 4),
    _PortSRLargestFrame_Type()
)
portSRLargestFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSRLargestFrame.setStatus("mandatory")


class _PortSRDirection_Type(Integer32):
    """Custom type portSRDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("backword", 1),
          ("forward", 0))
    )


_PortSRDirection_Type.__name__ = "Integer32"
_PortSRDirection_Object = MibTableColumn
portSRDirection = _PortSRDirection_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 1, 4, 1, 5),
    _PortSRDirection_Type()
)
portSRDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSRDirection.setStatus("mandatory")


class _PortSRRouteDescrpt_Type(DisplayString):
    """Custom type portSRRouteDescrpt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 70),
    )


_PortSRRouteDescrpt_Type.__name__ = "DisplayString"
_PortSRRouteDescrpt_Object = MibTableColumn
portSRRouteDescrpt = _PortSRRouteDescrpt_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 1, 4, 1, 6),
    _PortSRRouteDescrpt_Type()
)
portSRRouteDescrpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSRRouteDescrpt.setStatus("mandatory")


class _PortAllLoginStatus_Type(OctetString):
    """Custom type portAllLoginStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_PortAllLoginStatus_Type.__name__ = "OctetString"
_PortAllLoginStatus_Object = MibScalar
portAllLoginStatus = _PortAllLoginStatus_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 1, 5),
    _PortAllLoginStatus_Type()
)
portAllLoginStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portAllLoginStatus.setStatus("mandatory")


class _PortTokenRingSpeed_Type(Integer32):
    """Custom type portTokenRingSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              16)
        )
    )
    namedValues = NamedValues(
        *(("megabyte-16", 16),
          ("megabyte-4", 4))
    )


_PortTokenRingSpeed_Type.__name__ = "Integer32"
_PortTokenRingSpeed_Object = MibScalar
portTokenRingSpeed = _PortTokenRingSpeed_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 1, 6),
    _PortTokenRingSpeed_Type()
)
portTokenRingSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portTokenRingSpeed.setStatus("mandatory")


class _PortAllLEDStatus_Type(OctetString):
    """Custom type portAllLEDStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_PortAllLEDStatus_Type.__name__ = "OctetString"
_PortAllLEDStatus_Object = MibScalar
portAllLEDStatus = _PortAllLEDStatus_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 1, 7),
    _PortAllLEDStatus_Type()
)
portAllLEDStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portAllLEDStatus.setStatus("mandatory")
_Path_ObjectIdentity = ObjectIdentity
path = _Path_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2)
)
_PrpaNumber_Type = Integer32
_PrpaNumber_Object = MibScalar
prpaNumber = _PrpaNumber_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 1),
    _PrpaNumber_Type()
)
prpaNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prpaNumber.setStatus("mandatory")
_PrpaTable_Object = MibTable
prpaTable = _PrpaTable_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    prpaTable.setStatus("mandatory")
_PrpaEntry_Object = MibTableRow
prpaEntry = _PrpaEntry_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 2, 1)
)
prpaEntry.setIndexNames(
    (0, "Centrum-MIB", "prpaIndex"),
)
if mibBuilder.loadTexts:
    prpaEntry.setStatus("mandatory")
_PrpaIndex_Type = Integer32
_PrpaIndex_Object = MibTableColumn
prpaIndex = _PrpaIndex_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 2, 1, 1),
    _PrpaIndex_Type()
)
prpaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prpaIndex.setStatus("mandatory")


class _PrpaName_Type(DisplayString):
    """Custom type prpaName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_PrpaName_Type.__name__ = "DisplayString"
_PrpaName_Object = MibTableColumn
prpaName = _PrpaName_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 2, 1, 2),
    _PrpaName_Type()
)
prpaName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prpaName.setStatus("mandatory")


class _PrpaType_Type(Integer32):
    """Custom type prpaType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_PrpaType_Type.__name__ = "Integer32"
_PrpaType_Object = MibTableColumn
prpaType = _PrpaType_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 2, 1, 3),
    _PrpaType_Type()
)
prpaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prpaType.setStatus("mandatory")
_PrpaPortIdx_Type = Integer32
_PrpaPortIdx_Object = MibTableColumn
prpaPortIdx = _PrpaPortIdx_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 2, 1, 4),
    _PrpaPortIdx_Type()
)
prpaPortIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prpaPortIdx.setStatus("mandatory")


class _PrpaAutoHangUp_Type(Integer32):
    """Custom type prpaAutoHangUp based on Integer32"""
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


_PrpaAutoHangUp_Type.__name__ = "Integer32"
_PrpaAutoHangUp_Object = MibTableColumn
prpaAutoHangUp = _PrpaAutoHangUp_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 2, 1, 5),
    _PrpaAutoHangUp_Type()
)
prpaAutoHangUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prpaAutoHangUp.setStatus("mandatory")
_PrpaInPackets_Type = Counter32
_PrpaInPackets_Object = MibTableColumn
prpaInPackets = _PrpaInPackets_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 2, 1, 6),
    _PrpaInPackets_Type()
)
prpaInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prpaInPackets.setStatus("mandatory")
_PrpaOutPackets_Type = Counter32
_PrpaOutPackets_Object = MibTableColumn
prpaOutPackets = _PrpaOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 2, 1, 7),
    _PrpaOutPackets_Type()
)
prpaOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prpaOutPackets.setStatus("mandatory")
_PrpaInBytes_Type = Counter32
_PrpaInBytes_Object = MibTableColumn
prpaInBytes = _PrpaInBytes_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 2, 1, 8),
    _PrpaInBytes_Type()
)
prpaInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prpaInBytes.setStatus("mandatory")
_PrpaOutBytes_Type = Counter32
_PrpaOutBytes_Object = MibTableColumn
prpaOutBytes = _PrpaOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 2, 1, 9),
    _PrpaOutBytes_Type()
)
prpaOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prpaOutBytes.setStatus("mandatory")
_PrpaResetPrpaCounters_Type = Integer32
_PrpaResetPrpaCounters_Object = MibTableColumn
prpaResetPrpaCounters = _PrpaResetPrpaCounters_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 2, 1, 10),
    _PrpaResetPrpaCounters_Type()
)
prpaResetPrpaCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prpaResetPrpaCounters.setStatus("mandatory")


class _PrpaLoginStatus_Type(Integer32):
    """Custom type prpaLoginStatus based on Integer32"""
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
        *(("dial-in", 1),
          ("dial-out", 2),
          ("disabled", 3),
          ("unused", 0))
    )


_PrpaLoginStatus_Type.__name__ = "Integer32"
_PrpaLoginStatus_Object = MibTableColumn
prpaLoginStatus = _PrpaLoginStatus_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 2, 1, 11),
    _PrpaLoginStatus_Type()
)
prpaLoginStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prpaLoginStatus.setStatus("mandatory")


class _PrpaLoginUserName_Type(DisplayString):
    """Custom type prpaLoginUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_PrpaLoginUserName_Type.__name__ = "DisplayString"
_PrpaLoginUserName_Object = MibTableColumn
prpaLoginUserName = _PrpaLoginUserName_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 2, 1, 12),
    _PrpaLoginUserName_Type()
)
prpaLoginUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prpaLoginUserName.setStatus("mandatory")


class _PrpaLoginTime_Type(DisplayString):
    """Custom type prpaLoginTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_PrpaLoginTime_Type.__name__ = "DisplayString"
_PrpaLoginTime_Object = MibTableColumn
prpaLoginTime = _PrpaLoginTime_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 2, 1, 13),
    _PrpaLoginTime_Type()
)
prpaLoginTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prpaLoginTime.setStatus("mandatory")


class _PrpaLoginDuration_Type(DisplayString):
    """Custom type prpaLoginDuration based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_PrpaLoginDuration_Type.__name__ = "DisplayString"
_PrpaLoginDuration_Object = MibTableColumn
prpaLoginDuration = _PrpaLoginDuration_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 2, 1, 14),
    _PrpaLoginDuration_Type()
)
prpaLoginDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prpaLoginDuration.setStatus("mandatory")
_PrpaLoginAttempts_Type = Counter32
_PrpaLoginAttempts_Object = MibTableColumn
prpaLoginAttempts = _PrpaLoginAttempts_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 2, 1, 15),
    _PrpaLoginAttempts_Type()
)
prpaLoginAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prpaLoginAttempts.setStatus("mandatory")
_PrpaLoginInPackets_Type = Counter32
_PrpaLoginInPackets_Object = MibTableColumn
prpaLoginInPackets = _PrpaLoginInPackets_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 2, 1, 16),
    _PrpaLoginInPackets_Type()
)
prpaLoginInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prpaLoginInPackets.setStatus("mandatory")
_PrpaLoginOutPackets_Type = Counter32
_PrpaLoginOutPackets_Object = MibTableColumn
prpaLoginOutPackets = _PrpaLoginOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 2, 1, 17),
    _PrpaLoginOutPackets_Type()
)
prpaLoginOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prpaLoginOutPackets.setStatus("mandatory")
_PrpaLoginInBytes_Type = Counter32
_PrpaLoginInBytes_Object = MibTableColumn
prpaLoginInBytes = _PrpaLoginInBytes_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 2, 1, 18),
    _PrpaLoginInBytes_Type()
)
prpaLoginInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prpaLoginInBytes.setStatus("mandatory")
_PrpaLoginOutBytes_Type = Counter32
_PrpaLoginOutBytes_Object = MibTableColumn
prpaLoginOutBytes = _PrpaLoginOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 2, 1, 19),
    _PrpaLoginOutBytes_Type()
)
prpaLoginOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prpaLoginOutBytes.setStatus("mandatory")
_PrpaLoginParityErrors_Type = Counter32
_PrpaLoginParityErrors_Object = MibTableColumn
prpaLoginParityErrors = _PrpaLoginParityErrors_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 2, 1, 20),
    _PrpaLoginParityErrors_Type()
)
prpaLoginParityErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prpaLoginParityErrors.setStatus("mandatory")
_PrpaLoginFrameErrors_Type = Counter32
_PrpaLoginFrameErrors_Object = MibTableColumn
prpaLoginFrameErrors = _PrpaLoginFrameErrors_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 2, 1, 21),
    _PrpaLoginFrameErrors_Type()
)
prpaLoginFrameErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prpaLoginFrameErrors.setStatus("mandatory")
_PrpaLoginOverrunErrors_Type = Counter32
_PrpaLoginOverrunErrors_Object = MibTableColumn
prpaLoginOverrunErrors = _PrpaLoginOverrunErrors_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 2, 1, 22),
    _PrpaLoginOverrunErrors_Type()
)
prpaLoginOverrunErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prpaLoginOverrunErrors.setStatus("mandatory")
_PrpaLoginCksumErrors_Type = Counter32
_PrpaLoginCksumErrors_Object = MibTableColumn
prpaLoginCksumErrors = _PrpaLoginCksumErrors_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 2, 1, 23),
    _PrpaLoginCksumErrors_Type()
)
prpaLoginCksumErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prpaLoginCksumErrors.setStatus("mandatory")


class _PrpaFilterAction_Type(Integer32):
    """Custom type prpaFilterAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discard", 1),
          ("forward", 2))
    )


_PrpaFilterAction_Type.__name__ = "Integer32"
_PrpaFilterAction_Object = MibTableColumn
prpaFilterAction = _PrpaFilterAction_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 2, 1, 24),
    _PrpaFilterAction_Type()
)
prpaFilterAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prpaFilterAction.setStatus("mandatory")
_PrpaFilterMap_Type = Integer32
_PrpaFilterMap_Object = MibTableColumn
prpaFilterMap = _PrpaFilterMap_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 2, 1, 25),
    _PrpaFilterMap_Type()
)
prpaFilterMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prpaFilterMap.setStatus("mandatory")
_PrpaLoggerMap_Type = Integer32
_PrpaLoggerMap_Object = MibTableColumn
prpaLoggerMap = _PrpaLoggerMap_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 2, 1, 26),
    _PrpaLoggerMap_Type()
)
prpaLoggerMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prpaLoggerMap.setStatus("mandatory")
_PrpaFilterCount_Type = Counter32
_PrpaFilterCount_Object = MibTableColumn
prpaFilterCount = _PrpaFilterCount_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 2, 1, 27),
    _PrpaFilterCount_Type()
)
prpaFilterCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prpaFilterCount.setStatus("mandatory")
_PrpaLoggerCount_Type = Counter32
_PrpaLoggerCount_Object = MibTableColumn
prpaLoggerCount = _PrpaLoggerCount_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 2, 1, 28),
    _PrpaLoggerCount_Type()
)
prpaLoggerCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prpaLoggerCount.setStatus("mandatory")
_PrpaDiscardedPackets_Type = Counter32
_PrpaDiscardedPackets_Object = MibTableColumn
prpaDiscardedPackets = _PrpaDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 2, 1, 29),
    _PrpaDiscardedPackets_Type()
)
prpaDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prpaDiscardedPackets.setStatus("mandatory")
_PrpaForwardedPackets_Type = Counter32
_PrpaForwardedPackets_Object = MibTableColumn
prpaForwardedPackets = _PrpaForwardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 2, 1, 30),
    _PrpaForwardedPackets_Type()
)
prpaForwardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prpaForwardedPackets.setStatus("mandatory")
_PrpaReceivedPackets_Type = Counter32
_PrpaReceivedPackets_Object = MibTableColumn
prpaReceivedPackets = _PrpaReceivedPackets_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 2, 1, 31),
    _PrpaReceivedPackets_Type()
)
prpaReceivedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prpaReceivedPackets.setStatus("mandatory")


class _PrpaSmartFiltering_Type(Integer32):
    """Custom type prpaSmartFiltering based on Integer32"""
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


_PrpaSmartFiltering_Type.__name__ = "Integer32"
_PrpaSmartFiltering_Object = MibTableColumn
prpaSmartFiltering = _PrpaSmartFiltering_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 2, 1, 32),
    _PrpaSmartFiltering_Type()
)
prpaSmartFiltering.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prpaSmartFiltering.setStatus("mandatory")
_PrpaCurrentMacAddr_Type = OctetString
_PrpaCurrentMacAddr_Object = MibTableColumn
prpaCurrentMacAddr = _PrpaCurrentMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 2, 1, 33),
    _PrpaCurrentMacAddr_Type()
)
prpaCurrentMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prpaCurrentMacAddr.setStatus("mandatory")


class _PrpaIpEthernetII_Type(Integer32):
    """Custom type prpaIpEthernetII based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_PrpaIpEthernetII_Type.__name__ = "Integer32"
_PrpaIpEthernetII_Object = MibTableColumn
prpaIpEthernetII = _PrpaIpEthernetII_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 2, 1, 34),
    _PrpaIpEthernetII_Type()
)
prpaIpEthernetII.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prpaIpEthernetII.setStatus("mandatory")


class _PrpaIpSnap_Type(Integer32):
    """Custom type prpaIpSnap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_PrpaIpSnap_Type.__name__ = "Integer32"
_PrpaIpSnap_Object = MibTableColumn
prpaIpSnap = _PrpaIpSnap_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 2, 1, 35),
    _PrpaIpSnap_Type()
)
prpaIpSnap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prpaIpSnap.setStatus("mandatory")
_PrpaRemotePcIpAddress_Type = IpAddress
_PrpaRemotePcIpAddress_Object = MibTableColumn
prpaRemotePcIpAddress = _PrpaRemotePcIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 2, 1, 36),
    _PrpaRemotePcIpAddress_Type()
)
prpaRemotePcIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prpaRemotePcIpAddress.setStatus("mandatory")


class _PrpaIpxEn2WithNetBIOS_Type(Integer32):
    """Custom type prpaIpxEn2WithNetBIOS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_PrpaIpxEn2WithNetBIOS_Type.__name__ = "Integer32"
_PrpaIpxEn2WithNetBIOS_Object = MibTableColumn
prpaIpxEn2WithNetBIOS = _PrpaIpxEn2WithNetBIOS_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 2, 1, 37),
    _PrpaIpxEn2WithNetBIOS_Type()
)
prpaIpxEn2WithNetBIOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prpaIpxEn2WithNetBIOS.setStatus("mandatory")


class _PrpaIpx8023WithNetBIOS_Type(Integer32):
    """Custom type prpaIpx8023WithNetBIOS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_PrpaIpx8023WithNetBIOS_Type.__name__ = "Integer32"
_PrpaIpx8023WithNetBIOS_Object = MibTableColumn
prpaIpx8023WithNetBIOS = _PrpaIpx8023WithNetBIOS_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 2, 1, 38),
    _PrpaIpx8023WithNetBIOS_Type()
)
prpaIpx8023WithNetBIOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prpaIpx8023WithNetBIOS.setStatus("mandatory")


class _PrpaIpx8022WithNetBIOS_Type(Integer32):
    """Custom type prpaIpx8022WithNetBIOS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_PrpaIpx8022WithNetBIOS_Type.__name__ = "Integer32"
_PrpaIpx8022WithNetBIOS_Object = MibTableColumn
prpaIpx8022WithNetBIOS = _PrpaIpx8022WithNetBIOS_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 2, 1, 39),
    _PrpaIpx8022WithNetBIOS_Type()
)
prpaIpx8022WithNetBIOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prpaIpx8022WithNetBIOS.setStatus("mandatory")


class _PrpaIpxSnapWithNetBIOS_Type(Integer32):
    """Custom type prpaIpxSnapWithNetBIOS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_PrpaIpxSnapWithNetBIOS_Type.__name__ = "Integer32"
_PrpaIpxSnapWithNetBIOS_Object = MibTableColumn
prpaIpxSnapWithNetBIOS = _PrpaIpxSnapWithNetBIOS_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 2, 1, 40),
    _PrpaIpxSnapWithNetBIOS_Type()
)
prpaIpxSnapWithNetBIOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prpaIpxSnapWithNetBIOS.setStatus("mandatory")


class _PrpaXNS_Type(Integer32):
    """Custom type prpaXNS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_PrpaXNS_Type.__name__ = "Integer32"
_PrpaXNS_Object = MibTableColumn
prpaXNS = _PrpaXNS_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 2, 1, 41),
    _PrpaXNS_Type()
)
prpaXNS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prpaXNS.setStatus("mandatory")


class _PrpaVinesEthernetII_Type(Integer32):
    """Custom type prpaVinesEthernetII based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_PrpaVinesEthernetII_Type.__name__ = "Integer32"
_PrpaVinesEthernetII_Object = MibTableColumn
prpaVinesEthernetII = _PrpaVinesEthernetII_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 2, 1, 42),
    _PrpaVinesEthernetII_Type()
)
prpaVinesEthernetII.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prpaVinesEthernetII.setStatus("mandatory")


class _PrpaVinesSnap_Type(Integer32):
    """Custom type prpaVinesSnap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_PrpaVinesSnap_Type.__name__ = "Integer32"
_PrpaVinesSnap_Object = MibTableColumn
prpaVinesSnap = _PrpaVinesSnap_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 2, 1, 43),
    _PrpaVinesSnap_Type()
)
prpaVinesSnap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prpaVinesSnap.setStatus("mandatory")


class _PrpaNetBIOS_Type(Integer32):
    """Custom type prpaNetBIOS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_PrpaNetBIOS_Type.__name__ = "Integer32"
_PrpaNetBIOS_Object = MibTableColumn
prpaNetBIOS = _PrpaNetBIOS_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 2, 1, 44),
    _PrpaNetBIOS_Type()
)
prpaNetBIOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prpaNetBIOS.setStatus("mandatory")


class _PrpaDECNet_Type(Integer32):
    """Custom type prpaDECNet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_PrpaDECNet_Type.__name__ = "Integer32"
_PrpaDECNet_Object = MibTableColumn
prpaDECNet = _PrpaDECNet_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 2, 1, 45),
    _PrpaDECNet_Type()
)
prpaDECNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prpaDECNet.setStatus("mandatory")


class _PrpaUnknowEthernetII_Type(Integer32):
    """Custom type prpaUnknowEthernetII based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_PrpaUnknowEthernetII_Type.__name__ = "Integer32"
_PrpaUnknowEthernetII_Object = MibTableColumn
prpaUnknowEthernetII = _PrpaUnknowEthernetII_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 2, 1, 46),
    _PrpaUnknowEthernetII_Type()
)
prpaUnknowEthernetII.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prpaUnknowEthernetII.setStatus("mandatory")


class _PrpaUnknownSap_Type(Integer32):
    """Custom type prpaUnknownSap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_PrpaUnknownSap_Type.__name__ = "Integer32"
_PrpaUnknownSap_Object = MibTableColumn
prpaUnknownSap = _PrpaUnknownSap_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 2, 1, 47),
    _PrpaUnknownSap_Type()
)
prpaUnknownSap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prpaUnknownSap.setStatus("mandatory")


class _PrpaUnknownSnap_Type(Integer32):
    """Custom type prpaUnknownSnap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_PrpaUnknownSnap_Type.__name__ = "Integer32"
_PrpaUnknownSnap_Object = MibTableColumn
prpaUnknownSnap = _PrpaUnknownSnap_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 2, 1, 48),
    _PrpaUnknownSnap_Type()
)
prpaUnknownSnap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prpaUnknownSnap.setStatus("mandatory")
_PrpaMulticastAddress_Type = OctetString
_PrpaMulticastAddress_Object = MibTableColumn
prpaMulticastAddress = _PrpaMulticastAddress_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 2, 1, 49),
    _PrpaMulticastAddress_Type()
)
prpaMulticastAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prpaMulticastAddress.setStatus("mandatory")


class _PrpaXNSSap_Type(Integer32):
    """Custom type prpaXNSSap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_PrpaXNSSap_Type.__name__ = "Integer32"
_PrpaXNSSap_Object = MibTableColumn
prpaXNSSap = _PrpaXNSSap_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 2, 1, 50),
    _PrpaXNSSap_Type()
)
prpaXNSSap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prpaXNSSap.setStatus("mandatory")


class _PrpaXNSSnap_Type(Integer32):
    """Custom type prpaXNSSnap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_PrpaXNSSnap_Type.__name__ = "Integer32"
_PrpaXNSSnap_Object = MibTableColumn
prpaXNSSnap = _PrpaXNSSnap_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 2, 1, 51),
    _PrpaXNSSnap_Type()
)
prpaXNSSnap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prpaXNSSnap.setStatus("mandatory")


class _PrpaVinesSap_Type(Integer32):
    """Custom type prpaVinesSap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_PrpaVinesSap_Type.__name__ = "Integer32"
_PrpaVinesSap_Object = MibTableColumn
prpaVinesSap = _PrpaVinesSap_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 2, 1, 52),
    _PrpaVinesSap_Type()
)
prpaVinesSap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prpaVinesSap.setStatus("mandatory")


class _PrpaIpxEn2_Type(Integer32):
    """Custom type prpaIpxEn2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_PrpaIpxEn2_Type.__name__ = "Integer32"
_PrpaIpxEn2_Object = MibTableColumn
prpaIpxEn2 = _PrpaIpxEn2_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 2, 1, 53),
    _PrpaIpxEn2_Type()
)
prpaIpxEn2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prpaIpxEn2.setStatus("mandatory")


class _PrpaIpx8023_Type(Integer32):
    """Custom type prpaIpx8023 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_PrpaIpx8023_Type.__name__ = "Integer32"
_PrpaIpx8023_Object = MibTableColumn
prpaIpx8023 = _PrpaIpx8023_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 2, 1, 54),
    _PrpaIpx8023_Type()
)
prpaIpx8023.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prpaIpx8023.setStatus("mandatory")


class _PrpaIpx8022_Type(Integer32):
    """Custom type prpaIpx8022 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_PrpaIpx8022_Type.__name__ = "Integer32"
_PrpaIpx8022_Object = MibTableColumn
prpaIpx8022 = _PrpaIpx8022_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 2, 1, 55),
    _PrpaIpx8022_Type()
)
prpaIpx8022.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prpaIpx8022.setStatus("mandatory")


class _PrpaIpxSnap_Type(Integer32):
    """Custom type prpaIpxSnap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_PrpaIpxSnap_Type.__name__ = "Integer32"
_PrpaIpxSnap_Object = MibTableColumn
prpaIpxSnap = _PrpaIpxSnap_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 2, 1, 56),
    _PrpaIpxSnap_Type()
)
prpaIpxSnap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prpaIpxSnap.setStatus("mandatory")


class _PrpaPortList_Type(DisplayString):
    """Custom type prpaPortList based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_PrpaPortList_Type.__name__ = "DisplayString"
_PrpaPortList_Object = MibTableColumn
prpaPortList = _PrpaPortList_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 2, 1, 57),
    _PrpaPortList_Type()
)
prpaPortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prpaPortList.setStatus("mandatory")


class _PrpaSpoofState_Type(Integer32):
    """Custom type prpaSpoofState based on Integer32"""
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
        *(("connect", 2),
          ("disabled", 4),
          ("off", 1),
          ("spoofing", 3))
    )


_PrpaSpoofState_Type.__name__ = "Integer32"
_PrpaSpoofState_Object = MibTableColumn
prpaSpoofState = _PrpaSpoofState_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 2, 1, 58),
    _PrpaSpoofState_Type()
)
prpaSpoofState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prpaSpoofState.setStatus("mandatory")


class _PrpaCCPState_Type(Integer32):
    """Custom type prpaCCPState based on Integer32"""
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


_PrpaCCPState_Type.__name__ = "Integer32"
_PrpaCCPState_Object = MibTableColumn
prpaCCPState = _PrpaCCPState_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 2, 1, 59),
    _PrpaCCPState_Type()
)
prpaCCPState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prpaCCPState.setStatus("mandatory")


class _PrpaIPCPState_Type(Integer32):
    """Custom type prpaIPCPState based on Integer32"""
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


_PrpaIPCPState_Type.__name__ = "Integer32"
_PrpaIPCPState_Object = MibTableColumn
prpaIPCPState = _PrpaIPCPState_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 2, 1, 60),
    _PrpaIPCPState_Type()
)
prpaIPCPState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prpaIPCPState.setStatus("mandatory")


class _PrpaIPXCPState_Type(Integer32):
    """Custom type prpaIPXCPState based on Integer32"""
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


_PrpaIPXCPState_Type.__name__ = "Integer32"
_PrpaIPXCPState_Object = MibTableColumn
prpaIPXCPState = _PrpaIPXCPState_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 2, 1, 61),
    _PrpaIPXCPState_Type()
)
prpaIPXCPState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prpaIPXCPState.setStatus("mandatory")


class _PrpaBNCPState_Type(Integer32):
    """Custom type prpaBNCPState based on Integer32"""
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


_PrpaBNCPState_Type.__name__ = "Integer32"
_PrpaBNCPState_Object = MibTableColumn
prpaBNCPState = _PrpaBNCPState_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 2, 1, 62),
    _PrpaBNCPState_Type()
)
prpaBNCPState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prpaBNCPState.setStatus("mandatory")


class _PrpaARAPState_Type(Integer32):
    """Custom type prpaARAPState based on Integer32"""
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


_PrpaARAPState_Type.__name__ = "Integer32"
_PrpaARAPState_Object = MibTableColumn
prpaARAPState = _PrpaARAPState_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 2, 1, 63),
    _PrpaARAPState_Type()
)
prpaARAPState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prpaARAPState.setStatus("mandatory")
_PrpaLinkUtil_Type = Integer32
_PrpaLinkUtil_Object = MibTableColumn
prpaLinkUtil = _PrpaLinkUtil_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 2, 1, 64),
    _PrpaLinkUtil_Type()
)
prpaLinkUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prpaLinkUtil.setStatus("mandatory")
_PlocalNumber_Type = Integer32
_PlocalNumber_Object = MibScalar
plocalNumber = _PlocalNumber_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 3),
    _PlocalNumber_Type()
)
plocalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plocalNumber.setStatus("mandatory")
_PlocalTable_Object = MibTable
plocalTable = _PlocalTable_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 4)
)
if mibBuilder.loadTexts:
    plocalTable.setStatus("mandatory")
_PlocalEntry_Object = MibTableRow
plocalEntry = _PlocalEntry_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 4, 1)
)
plocalEntry.setIndexNames(
    (0, "Centrum-MIB", "plocalIndex"),
)
if mibBuilder.loadTexts:
    plocalEntry.setStatus("mandatory")
_PlocalIndex_Type = Integer32
_PlocalIndex_Object = MibTableColumn
plocalIndex = _PlocalIndex_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 4, 1, 1),
    _PlocalIndex_Type()
)
plocalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plocalIndex.setStatus("mandatory")


class _PlocalName_Type(DisplayString):
    """Custom type plocalName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_PlocalName_Type.__name__ = "DisplayString"
_PlocalName_Object = MibTableColumn
plocalName = _PlocalName_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 4, 1, 2),
    _PlocalName_Type()
)
plocalName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plocalName.setStatus("mandatory")


class _PlocalType_Type(Integer32):
    """Custom type plocalType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_PlocalType_Type.__name__ = "Integer32"
_PlocalType_Object = MibTableColumn
plocalType = _PlocalType_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 4, 1, 3),
    _PlocalType_Type()
)
plocalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plocalType.setStatus("mandatory")
_PlocalPortIdx_Type = Integer32
_PlocalPortIdx_Object = MibTableColumn
plocalPortIdx = _PlocalPortIdx_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 4, 1, 4),
    _PlocalPortIdx_Type()
)
plocalPortIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plocalPortIdx.setStatus("mandatory")
_PlocalInPackets_Type = Counter32
_PlocalInPackets_Object = MibTableColumn
plocalInPackets = _PlocalInPackets_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 4, 1, 5),
    _PlocalInPackets_Type()
)
plocalInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plocalInPackets.setStatus("mandatory")
_PlocalOutPackets_Type = Counter32
_PlocalOutPackets_Object = MibTableColumn
plocalOutPackets = _PlocalOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 4, 1, 6),
    _PlocalOutPackets_Type()
)
plocalOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plocalOutPackets.setStatus("mandatory")
_PlocalInBytes_Type = Counter32
_PlocalInBytes_Object = MibTableColumn
plocalInBytes = _PlocalInBytes_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 4, 1, 7),
    _PlocalInBytes_Type()
)
plocalInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plocalInBytes.setStatus("mandatory")
_PlocalOutBytes_Type = Counter32
_PlocalOutBytes_Object = MibTableColumn
plocalOutBytes = _PlocalOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 4, 1, 8),
    _PlocalOutBytes_Type()
)
plocalOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plocalOutBytes.setStatus("mandatory")
_PlocalResetPlocalCounters_Type = Integer32
_PlocalResetPlocalCounters_Object = MibTableColumn
plocalResetPlocalCounters = _PlocalResetPlocalCounters_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 4, 1, 9),
    _PlocalResetPlocalCounters_Type()
)
plocalResetPlocalCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plocalResetPlocalCounters.setStatus("mandatory")


class _PlocalFilterAction_Type(Integer32):
    """Custom type plocalFilterAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discard", 1),
          ("forward", 2))
    )


_PlocalFilterAction_Type.__name__ = "Integer32"
_PlocalFilterAction_Object = MibTableColumn
plocalFilterAction = _PlocalFilterAction_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 4, 1, 10),
    _PlocalFilterAction_Type()
)
plocalFilterAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plocalFilterAction.setStatus("mandatory")
_PlocalFilterMap_Type = Integer32
_PlocalFilterMap_Object = MibTableColumn
plocalFilterMap = _PlocalFilterMap_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 4, 1, 11),
    _PlocalFilterMap_Type()
)
plocalFilterMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plocalFilterMap.setStatus("mandatory")
_PlocalLoggerMap_Type = Integer32
_PlocalLoggerMap_Object = MibTableColumn
plocalLoggerMap = _PlocalLoggerMap_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 4, 1, 12),
    _PlocalLoggerMap_Type()
)
plocalLoggerMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    plocalLoggerMap.setStatus("mandatory")
_PlocalFilterCount_Type = Counter32
_PlocalFilterCount_Object = MibTableColumn
plocalFilterCount = _PlocalFilterCount_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 4, 1, 13),
    _PlocalFilterCount_Type()
)
plocalFilterCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plocalFilterCount.setStatus("mandatory")
_PlocalLoggerCount_Type = Counter32
_PlocalLoggerCount_Object = MibTableColumn
plocalLoggerCount = _PlocalLoggerCount_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 4, 1, 14),
    _PlocalLoggerCount_Type()
)
plocalLoggerCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plocalLoggerCount.setStatus("mandatory")
_PlocalDiscardedPackets_Type = Counter32
_PlocalDiscardedPackets_Object = MibTableColumn
plocalDiscardedPackets = _PlocalDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 4, 1, 15),
    _PlocalDiscardedPackets_Type()
)
plocalDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plocalDiscardedPackets.setStatus("mandatory")
_PlocalForwardedPackets_Type = Counter32
_PlocalForwardedPackets_Object = MibTableColumn
plocalForwardedPackets = _PlocalForwardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 4, 1, 16),
    _PlocalForwardedPackets_Type()
)
plocalForwardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plocalForwardedPackets.setStatus("mandatory")
_PlocalReceivedPackets_Type = Counter32
_PlocalReceivedPackets_Object = MibTableColumn
plocalReceivedPackets = _PlocalReceivedPackets_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 4, 1, 17),
    _PlocalReceivedPackets_Type()
)
plocalReceivedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plocalReceivedPackets.setStatus("mandatory")
_PrmtNumber_Type = Integer32
_PrmtNumber_Object = MibScalar
prmtNumber = _PrmtNumber_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 5),
    _PrmtNumber_Type()
)
prmtNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prmtNumber.setStatus("mandatory")
_PrmtTable_Object = MibTable
prmtTable = _PrmtTable_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 6)
)
if mibBuilder.loadTexts:
    prmtTable.setStatus("mandatory")
_PrmtEntry_Object = MibTableRow
prmtEntry = _PrmtEntry_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 6, 1)
)
prmtEntry.setIndexNames(
    (0, "Centrum-MIB", "prmtIndex"),
)
if mibBuilder.loadTexts:
    prmtEntry.setStatus("mandatory")
_PrmtIndex_Type = Integer32
_PrmtIndex_Object = MibTableColumn
prmtIndex = _PrmtIndex_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 6, 1, 1),
    _PrmtIndex_Type()
)
prmtIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prmtIndex.setStatus("mandatory")


class _PrmtName_Type(DisplayString):
    """Custom type prmtName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_PrmtName_Type.__name__ = "DisplayString"
_PrmtName_Object = MibTableColumn
prmtName = _PrmtName_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 6, 1, 2),
    _PrmtName_Type()
)
prmtName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prmtName.setStatus("mandatory")


class _PrmtType_Type(Integer32):
    """Custom type prmtType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_PrmtType_Type.__name__ = "Integer32"
_PrmtType_Object = MibTableColumn
prmtType = _PrmtType_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 6, 1, 3),
    _PrmtType_Type()
)
prmtType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prmtType.setStatus("mandatory")


class _PrmtInitiator_Type(Integer32):
    """Custom type prmtInitiator based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("passive", 2))
    )


_PrmtInitiator_Type.__name__ = "Integer32"
_PrmtInitiator_Object = MibTableColumn
prmtInitiator = _PrmtInitiator_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 6, 1, 4),
    _PrmtInitiator_Type()
)
prmtInitiator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prmtInitiator.setStatus("mandatory")
_PrmtCongestThreshold_Type = Integer32
_PrmtCongestThreshold_Object = MibTableColumn
prmtCongestThreshold = _PrmtCongestThreshold_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 6, 1, 5),
    _PrmtCongestThreshold_Type()
)
prmtCongestThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prmtCongestThreshold.setStatus("mandatory")


class _PrmtScheduleType1_Type(Integer32):
    """Custom type prmtScheduleType1 based on Integer32"""
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
        *(("daily", 2),
          ("invalid", 1),
          ("monthly", 4),
          ("weekly", 3))
    )


_PrmtScheduleType1_Type.__name__ = "Integer32"
_PrmtScheduleType1_Object = MibTableColumn
prmtScheduleType1 = _PrmtScheduleType1_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 6, 1, 6),
    _PrmtScheduleType1_Type()
)
prmtScheduleType1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prmtScheduleType1.setStatus("mandatory")
_PrmtDaysScheduled1_Type = Integer32
_PrmtDaysScheduled1_Object = MibTableColumn
prmtDaysScheduled1 = _PrmtDaysScheduled1_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 6, 1, 7),
    _PrmtDaysScheduled1_Type()
)
prmtDaysScheduled1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prmtDaysScheduled1.setStatus("mandatory")
_PrmtStartTime1_Type = OctetString
_PrmtStartTime1_Object = MibTableColumn
prmtStartTime1 = _PrmtStartTime1_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 6, 1, 8),
    _PrmtStartTime1_Type()
)
prmtStartTime1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prmtStartTime1.setStatus("mandatory")
_PrmtHowLong1_Type = OctetString
_PrmtHowLong1_Object = MibTableColumn
prmtHowLong1 = _PrmtHowLong1_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 6, 1, 9),
    _PrmtHowLong1_Type()
)
prmtHowLong1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prmtHowLong1.setStatus("mandatory")


class _PrmtScheduleType2_Type(Integer32):
    """Custom type prmtScheduleType2 based on Integer32"""
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
        *(("daily", 2),
          ("invalid", 1),
          ("monthly", 4),
          ("weekly", 3))
    )


_PrmtScheduleType2_Type.__name__ = "Integer32"
_PrmtScheduleType2_Object = MibTableColumn
prmtScheduleType2 = _PrmtScheduleType2_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 6, 1, 10),
    _PrmtScheduleType2_Type()
)
prmtScheduleType2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prmtScheduleType2.setStatus("mandatory")
_PrmtDaysScheduled2_Type = Integer32
_PrmtDaysScheduled2_Object = MibTableColumn
prmtDaysScheduled2 = _PrmtDaysScheduled2_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 6, 1, 11),
    _PrmtDaysScheduled2_Type()
)
prmtDaysScheduled2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prmtDaysScheduled2.setStatus("mandatory")
_PrmtStartTime2_Type = OctetString
_PrmtStartTime2_Object = MibTableColumn
prmtStartTime2 = _PrmtStartTime2_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 6, 1, 12),
    _PrmtStartTime2_Type()
)
prmtStartTime2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prmtStartTime2.setStatus("mandatory")
_PrmtHowLong2_Type = OctetString
_PrmtHowLong2_Object = MibTableColumn
prmtHowLong2 = _PrmtHowLong2_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 6, 1, 13),
    _PrmtHowLong2_Type()
)
prmtHowLong2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prmtHowLong2.setStatus("mandatory")
_PrmtInPackets_Type = Counter32
_PrmtInPackets_Object = MibTableColumn
prmtInPackets = _PrmtInPackets_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 6, 1, 14),
    _PrmtInPackets_Type()
)
prmtInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prmtInPackets.setStatus("mandatory")
_PrmtOutPackets_Type = Counter32
_PrmtOutPackets_Object = MibTableColumn
prmtOutPackets = _PrmtOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 6, 1, 15),
    _PrmtOutPackets_Type()
)
prmtOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prmtOutPackets.setStatus("mandatory")
_PrmtInBytes_Type = Counter32
_PrmtInBytes_Object = MibTableColumn
prmtInBytes = _PrmtInBytes_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 6, 1, 16),
    _PrmtInBytes_Type()
)
prmtInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prmtInBytes.setStatus("mandatory")
_PrmtOutBytes_Type = Counter32
_PrmtOutBytes_Object = MibTableColumn
prmtOutBytes = _PrmtOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 6, 1, 17),
    _PrmtOutBytes_Type()
)
prmtOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prmtOutBytes.setStatus("mandatory")
_PrmtResetPrmtCounters_Type = Integer32
_PrmtResetPrmtCounters_Object = MibTableColumn
prmtResetPrmtCounters = _PrmtResetPrmtCounters_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 6, 1, 18),
    _PrmtResetPrmtCounters_Type()
)
prmtResetPrmtCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prmtResetPrmtCounters.setStatus("mandatory")


class _PrmtFilterAction_Type(Integer32):
    """Custom type prmtFilterAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discard", 1),
          ("forward", 2))
    )


_PrmtFilterAction_Type.__name__ = "Integer32"
_PrmtFilterAction_Object = MibTableColumn
prmtFilterAction = _PrmtFilterAction_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 6, 1, 19),
    _PrmtFilterAction_Type()
)
prmtFilterAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prmtFilterAction.setStatus("mandatory")
_PrmtFilterMap_Type = Integer32
_PrmtFilterMap_Object = MibTableColumn
prmtFilterMap = _PrmtFilterMap_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 6, 1, 20),
    _PrmtFilterMap_Type()
)
prmtFilterMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prmtFilterMap.setStatus("mandatory")
_PrmtLoggerMap_Type = Integer32
_PrmtLoggerMap_Object = MibTableColumn
prmtLoggerMap = _PrmtLoggerMap_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 6, 1, 21),
    _PrmtLoggerMap_Type()
)
prmtLoggerMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prmtLoggerMap.setStatus("mandatory")
_PrmtFilterCount_Type = Counter32
_PrmtFilterCount_Object = MibTableColumn
prmtFilterCount = _PrmtFilterCount_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 6, 1, 22),
    _PrmtFilterCount_Type()
)
prmtFilterCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prmtFilterCount.setStatus("mandatory")
_PrmtLoggerCount_Type = Counter32
_PrmtLoggerCount_Object = MibTableColumn
prmtLoggerCount = _PrmtLoggerCount_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 6, 1, 23),
    _PrmtLoggerCount_Type()
)
prmtLoggerCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prmtLoggerCount.setStatus("mandatory")
_PrmtDiscardedPackets_Type = Counter32
_PrmtDiscardedPackets_Object = MibTableColumn
prmtDiscardedPackets = _PrmtDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 6, 1, 24),
    _PrmtDiscardedPackets_Type()
)
prmtDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prmtDiscardedPackets.setStatus("mandatory")
_PrmtForwardedPackets_Type = Counter32
_PrmtForwardedPackets_Object = MibTableColumn
prmtForwardedPackets = _PrmtForwardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 6, 1, 25),
    _PrmtForwardedPackets_Type()
)
prmtForwardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prmtForwardedPackets.setStatus("mandatory")
_PrmtReceivedPackets_Type = Counter32
_PrmtReceivedPackets_Object = MibTableColumn
prmtReceivedPackets = _PrmtReceivedPackets_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 6, 1, 26),
    _PrmtReceivedPackets_Type()
)
prmtReceivedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prmtReceivedPackets.setStatus("mandatory")


class _PrmtSmartFiltering_Type(Integer32):
    """Custom type prmtSmartFiltering based on Integer32"""
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


_PrmtSmartFiltering_Type.__name__ = "Integer32"
_PrmtSmartFiltering_Object = MibTableColumn
prmtSmartFiltering = _PrmtSmartFiltering_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 6, 1, 27),
    _PrmtSmartFiltering_Type()
)
prmtSmartFiltering.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prmtSmartFiltering.setStatus("mandatory")
_PrmtOutCongestions_Type = Counter32
_PrmtOutCongestions_Object = MibTableColumn
prmtOutCongestions = _PrmtOutCongestions_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 6, 1, 28),
    _PrmtOutCongestions_Type()
)
prmtOutCongestions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prmtOutCongestions.setStatus("mandatory")


class _PrmtRmtRouterName_Type(DisplayString):
    """Custom type prmtRmtRouterName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PrmtRmtRouterName_Type.__name__ = "DisplayString"
_PrmtRmtRouterName_Object = MibTableColumn
prmtRmtRouterName = _PrmtRmtRouterName_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 6, 1, 29),
    _PrmtRmtRouterName_Type()
)
prmtRmtRouterName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prmtRmtRouterName.setStatus("mandatory")


class _PrmtTypeSelection_Type(Integer32):
    """Custom type prmtTypeSelection based on Integer32"""
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
        *(("on-demand-only", 3),
          ("permanent-only", 1),
          ("permanent-with-backup", 2),
          ("schedule-only", 4))
    )


_PrmtTypeSelection_Type.__name__ = "Integer32"
_PrmtTypeSelection_Object = MibTableColumn
prmtTypeSelection = _PrmtTypeSelection_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 6, 1, 30),
    _PrmtTypeSelection_Type()
)
prmtTypeSelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prmtTypeSelection.setStatus("mandatory")
_PrmtAsyncPortNo_Type = Integer32
_PrmtAsyncPortNo_Object = MibTableColumn
prmtAsyncPortNo = _PrmtAsyncPortNo_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 6, 1, 31),
    _PrmtAsyncPortNo_Type()
)
prmtAsyncPortNo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prmtAsyncPortNo.setStatus("mandatory")
_PrmtISDNPortNo_Type = Integer32
_PrmtISDNPortNo_Object = MibTableColumn
prmtISDNPortNo = _PrmtISDNPortNo_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 6, 1, 32),
    _PrmtISDNPortNo_Type()
)
prmtISDNPortNo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prmtISDNPortNo.setStatus("mandatory")


class _PrmtISDNReqBaudRate_Type(Integer32):
    """Custom type prmtISDNReqBaudRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 3),
          ("br-56000", 1),
          ("br-64000", 2))
    )


_PrmtISDNReqBaudRate_Type.__name__ = "Integer32"
_PrmtISDNReqBaudRate_Object = MibTableColumn
prmtISDNReqBaudRate = _PrmtISDNReqBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 6, 1, 33),
    _PrmtISDNReqBaudRate_Type()
)
prmtISDNReqBaudRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prmtISDNReqBaudRate.setStatus("mandatory")


class _PrmtSpoofState_Type(Integer32):
    """Custom type prmtSpoofState based on Integer32"""
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
        *(("connect", 2),
          ("disabled", 4),
          ("off", 1),
          ("spoofing", 3))
    )


_PrmtSpoofState_Type.__name__ = "Integer32"
_PrmtSpoofState_Object = MibTableColumn
prmtSpoofState = _PrmtSpoofState_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 6, 1, 34),
    _PrmtSpoofState_Type()
)
prmtSpoofState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prmtSpoofState.setStatus("mandatory")


class _PrmtCCPState_Type(Integer32):
    """Custom type prmtCCPState based on Integer32"""
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


_PrmtCCPState_Type.__name__ = "Integer32"
_PrmtCCPState_Object = MibTableColumn
prmtCCPState = _PrmtCCPState_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 6, 1, 35),
    _PrmtCCPState_Type()
)
prmtCCPState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prmtCCPState.setStatus("mandatory")


class _PrmtIPCPState_Type(Integer32):
    """Custom type prmtIPCPState based on Integer32"""
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


_PrmtIPCPState_Type.__name__ = "Integer32"
_PrmtIPCPState_Object = MibTableColumn
prmtIPCPState = _PrmtIPCPState_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 6, 1, 36),
    _PrmtIPCPState_Type()
)
prmtIPCPState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prmtIPCPState.setStatus("mandatory")


class _PrmtIPXCPState_Type(Integer32):
    """Custom type prmtIPXCPState based on Integer32"""
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


_PrmtIPXCPState_Type.__name__ = "Integer32"
_PrmtIPXCPState_Object = MibTableColumn
prmtIPXCPState = _PrmtIPXCPState_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 6, 1, 37),
    _PrmtIPXCPState_Type()
)
prmtIPXCPState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prmtIPXCPState.setStatus("mandatory")


class _PrmtBNCPState_Type(Integer32):
    """Custom type prmtBNCPState based on Integer32"""
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


_PrmtBNCPState_Type.__name__ = "Integer32"
_PrmtBNCPState_Object = MibTableColumn
prmtBNCPState = _PrmtBNCPState_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 6, 1, 38),
    _PrmtBNCPState_Type()
)
prmtBNCPState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prmtBNCPState.setStatus("mandatory")
_PrmtLinkUtil_Type = Integer32
_PrmtLinkUtil_Object = MibTableColumn
prmtLinkUtil = _PrmtLinkUtil_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 6, 1, 39),
    _PrmtLinkUtil_Type()
)
prmtLinkUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prmtLinkUtil.setStatus("mandatory")


class _PrmtPMPortList_Type(DisplayString):
    """Custom type prmtPMPortList based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_PrmtPMPortList_Type.__name__ = "DisplayString"
_PrmtPMPortList_Object = MibTableColumn
prmtPMPortList = _PrmtPMPortList_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 6, 1, 40),
    _PrmtPMPortList_Type()
)
prmtPMPortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prmtPMPortList.setStatus("mandatory")


class _PrmtBUPortList_Type(DisplayString):
    """Custom type prmtBUPortList based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_PrmtBUPortList_Type.__name__ = "DisplayString"
_PrmtBUPortList_Object = MibTableColumn
prmtBUPortList = _PrmtBUPortList_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 6, 1, 41),
    _PrmtBUPortList_Type()
)
prmtBUPortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prmtBUPortList.setStatus("mandatory")


class _PrmtODPortList_Type(DisplayString):
    """Custom type prmtODPortList based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_PrmtODPortList_Type.__name__ = "DisplayString"
_PrmtODPortList_Object = MibTableColumn
prmtODPortList = _PrmtODPortList_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 6, 1, 42),
    _PrmtODPortList_Type()
)
prmtODPortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prmtODPortList.setStatus("mandatory")


class _PrmtSCPortList_Type(DisplayString):
    """Custom type prmtSCPortList based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_PrmtSCPortList_Type.__name__ = "DisplayString"
_PrmtSCPortList_Object = MibTableColumn
prmtSCPortList = _PrmtSCPortList_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 6, 1, 43),
    _PrmtSCPortList_Type()
)
prmtSCPortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prmtSCPortList.setStatus("mandatory")
_PrmtPortTable_Object = MibTable
prmtPortTable = _PrmtPortTable_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 7)
)
if mibBuilder.loadTexts:
    prmtPortTable.setStatus("mandatory")
_PrmtPortEntry_Object = MibTableRow
prmtPortEntry = _PrmtPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 7, 1)
)
prmtPortEntry.setIndexNames(
    (0, "Centrum-MIB", "prmtPortPrmtIdx"),
    (0, "Centrum-MIB", "prmtPortPortIdx"),
)
if mibBuilder.loadTexts:
    prmtPortEntry.setStatus("mandatory")
_PrmtPortPrmtIdx_Type = Integer32
_PrmtPortPrmtIdx_Object = MibTableColumn
prmtPortPrmtIdx = _PrmtPortPrmtIdx_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 7, 1, 1),
    _PrmtPortPrmtIdx_Type()
)
prmtPortPrmtIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prmtPortPrmtIdx.setStatus("mandatory")
_PrmtPortPortIdx_Type = Integer32
_PrmtPortPortIdx_Object = MibTableColumn
prmtPortPortIdx = _PrmtPortPortIdx_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 7, 1, 2),
    _PrmtPortPortIdx_Type()
)
prmtPortPortIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prmtPortPortIdx.setStatus("mandatory")


class _PrmtPortType_Type(Integer32):
    """Custom type prmtPortType based on Integer32"""
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
        *(("backup", 4),
          ("invalid", 1),
          ("on-demand", 2),
          ("permanent", 3),
          ("scheduled", 5))
    )


_PrmtPortType_Type.__name__ = "Integer32"
_PrmtPortType_Object = MibTableColumn
prmtPortType = _PrmtPortType_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 7, 1, 3),
    _PrmtPortType_Type()
)
prmtPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prmtPortType.setStatus("mandatory")


class _PrmtPortPhoneNumber_Type(OctetString):
    """Custom type prmtPortPhoneNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_PrmtPortPhoneNumber_Type.__name__ = "OctetString"
_PrmtPortPhoneNumber_Object = MibTableColumn
prmtPortPhoneNumber = _PrmtPortPhoneNumber_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 7, 1, 4),
    _PrmtPortPhoneNumber_Type()
)
prmtPortPhoneNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prmtPortPhoneNumber.setStatus("mandatory")


class _PrmtPortDirectoryNo_Type(OctetString):
    """Custom type prmtPortDirectoryNo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_PrmtPortDirectoryNo_Type.__name__ = "OctetString"
_PrmtPortDirectoryNo_Object = MibTableColumn
prmtPortDirectoryNo = _PrmtPortDirectoryNo_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 7, 1, 5),
    _PrmtPortDirectoryNo_Type()
)
prmtPortDirectoryNo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prmtPortDirectoryNo.setStatus("mandatory")
_PathResetAllCounters_Type = Integer32
_PathResetAllCounters_Object = MibScalar
pathResetAllCounters = _PathResetAllCounters_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 8),
    _PathResetAllCounters_Type()
)
pathResetAllCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pathResetAllCounters.setStatus("mandatory")
_PrmtPhoneTable_Object = MibTable
prmtPhoneTable = _PrmtPhoneTable_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 9)
)
if mibBuilder.loadTexts:
    prmtPhoneTable.setStatus("mandatory")
_PrmtPhoneEntry_Object = MibTableRow
prmtPhoneEntry = _PrmtPhoneEntry_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 9, 1)
)
prmtPhoneEntry.setIndexNames(
    (0, "Centrum-MIB", "prmtPhonePrmtIdx"),
    (0, "Centrum-MIB", "prmtPhoneIdx"),
)
if mibBuilder.loadTexts:
    prmtPhoneEntry.setStatus("mandatory")
_PrmtPhonePrmtIdx_Type = Integer32
_PrmtPhonePrmtIdx_Object = MibTableColumn
prmtPhonePrmtIdx = _PrmtPhonePrmtIdx_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 9, 1, 1),
    _PrmtPhonePrmtIdx_Type()
)
prmtPhonePrmtIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prmtPhonePrmtIdx.setStatus("mandatory")
_PrmtPhoneIdx_Type = Integer32
_PrmtPhoneIdx_Object = MibTableColumn
prmtPhoneIdx = _PrmtPhoneIdx_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 9, 1, 2),
    _PrmtPhoneIdx_Type()
)
prmtPhoneIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prmtPhoneIdx.setStatus("mandatory")


class _PrmtPhoneType_Type(Integer32):
    """Custom type prmtPhoneType based on Integer32"""
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
        *(("backup-async", 5),
          ("backup-isdn", 4),
          ("invalid", 1),
          ("on-demand-async", 3),
          ("on-demand-isdn", 2),
          ("scheduled-async", 7),
          ("scheduled-isdn", 6))
    )


_PrmtPhoneType_Type.__name__ = "Integer32"
_PrmtPhoneType_Object = MibTableColumn
prmtPhoneType = _PrmtPhoneType_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 9, 1, 3),
    _PrmtPhoneType_Type()
)
prmtPhoneType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prmtPhoneType.setStatus("mandatory")


class _PrmtPhonePhoneNumber_Type(OctetString):
    """Custom type prmtPhonePhoneNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_PrmtPhonePhoneNumber_Type.__name__ = "OctetString"
_PrmtPhonePhoneNumber_Object = MibTableColumn
prmtPhonePhoneNumber = _PrmtPhonePhoneNumber_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 9, 1, 4),
    _PrmtPhonePhoneNumber_Type()
)
prmtPhonePhoneNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prmtPhonePhoneNumber.setStatus("mandatory")


class _PrmtPhoneDirectoryNo_Type(OctetString):
    """Custom type prmtPhoneDirectoryNo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_PrmtPhoneDirectoryNo_Type.__name__ = "OctetString"
_PrmtPhoneDirectoryNo_Object = MibTableColumn
prmtPhoneDirectoryNo = _PrmtPhoneDirectoryNo_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 2, 9, 1, 5),
    _PrmtPhoneDirectoryNo_Type()
)
prmtPhoneDirectoryNo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prmtPhoneDirectoryNo.setStatus("mandatory")
_Crip_ObjectIdentity = ObjectIdentity
crip = _Crip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 3)
)
_IpRpa_ObjectIdentity = ObjectIdentity
ipRpa = _IpRpa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 3, 1)
)
_IpRpaNumber_Type = Integer32
_IpRpaNumber_Object = MibScalar
ipRpaNumber = _IpRpaNumber_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 3, 1, 1),
    _IpRpaNumber_Type()
)
ipRpaNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRpaNumber.setStatus("mandatory")
_IpRpaTable_Object = MibTable
ipRpaTable = _IpRpaTable_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 3, 1, 2)
)
if mibBuilder.loadTexts:
    ipRpaTable.setStatus("mandatory")
_IpRpaEntry_Object = MibTableRow
ipRpaEntry = _IpRpaEntry_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 3, 1, 2, 1)
)
ipRpaEntry.setIndexNames(
    (0, "Centrum-MIB", "ipRpaIndex"),
)
if mibBuilder.loadTexts:
    ipRpaEntry.setStatus("mandatory")
_IpRpaIndex_Type = Integer32
_IpRpaIndex_Object = MibTableColumn
ipRpaIndex = _IpRpaIndex_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 3, 1, 2, 1, 1),
    _IpRpaIndex_Type()
)
ipRpaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRpaIndex.setStatus("mandatory")
_IpRpaCurrentClientIpAddress_Type = IpAddress
_IpRpaCurrentClientIpAddress_Object = MibTableColumn
ipRpaCurrentClientIpAddress = _IpRpaCurrentClientIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 3, 1, 2, 1, 2),
    _IpRpaCurrentClientIpAddress_Type()
)
ipRpaCurrentClientIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRpaCurrentClientIpAddress.setStatus("mandatory")
_IpRpaConfigClientIpAddress_Type = IpAddress
_IpRpaConfigClientIpAddress_Object = MibTableColumn
ipRpaConfigClientIpAddress = _IpRpaConfigClientIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 3, 1, 2, 1, 3),
    _IpRpaConfigClientIpAddress_Type()
)
ipRpaConfigClientIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRpaConfigClientIpAddress.setStatus("mandatory")


class _IpRpaTcpHdrCompress_Type(Integer32):
    """Custom type ipRpaTcpHdrCompress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_IpRpaTcpHdrCompress_Type.__name__ = "Integer32"
_IpRpaTcpHdrCompress_Object = MibTableColumn
ipRpaTcpHdrCompress = _IpRpaTcpHdrCompress_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 3, 1, 2, 1, 4),
    _IpRpaTcpHdrCompress_Type()
)
ipRpaTcpHdrCompress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRpaTcpHdrCompress.setStatus("mandatory")


class _IpRpaType_Type(Integer32):
    """Custom type ipRpaType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_IpRpaType_Type.__name__ = "Integer32"
_IpRpaType_Object = MibTableColumn
ipRpaType = _IpRpaType_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 3, 1, 2, 1, 5),
    _IpRpaType_Type()
)
ipRpaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRpaType.setStatus("mandatory")


class _IpRpaBootpEnabled_Type(Integer32):
    """Custom type ipRpaBootpEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_IpRpaBootpEnabled_Type.__name__ = "Integer32"
_IpRpaBootpEnabled_Object = MibScalar
ipRpaBootpEnabled = _IpRpaBootpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 3, 1, 3),
    _IpRpaBootpEnabled_Type()
)
ipRpaBootpEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRpaBootpEnabled.setStatus("mandatory")


class _IpRpaRarpEnabled_Type(Integer32):
    """Custom type ipRpaRarpEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_IpRpaRarpEnabled_Type.__name__ = "Integer32"
_IpRpaRarpEnabled_Object = MibScalar
ipRpaRarpEnabled = _IpRpaRarpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 3, 1, 4),
    _IpRpaRarpEnabled_Type()
)
ipRpaRarpEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRpaRarpEnabled.setStatus("mandatory")


class _IpRpaBootpOrRarpRequired_Type(Integer32):
    """Custom type ipRpaBootpOrRarpRequired based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_IpRpaBootpOrRarpRequired_Type.__name__ = "Integer32"
_IpRpaBootpOrRarpRequired_Object = MibScalar
ipRpaBootpOrRarpRequired = _IpRpaBootpOrRarpRequired_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 3, 1, 5),
    _IpRpaBootpOrRarpRequired_Type()
)
ipRpaBootpOrRarpRequired.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRpaBootpOrRarpRequired.setStatus("mandatory")
_IpRpaBootpInPackets_Type = Counter32
_IpRpaBootpInPackets_Object = MibScalar
ipRpaBootpInPackets = _IpRpaBootpInPackets_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 3, 1, 6),
    _IpRpaBootpInPackets_Type()
)
ipRpaBootpInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRpaBootpInPackets.setStatus("mandatory")
_IpRpaBootpOutPackets_Type = Counter32
_IpRpaBootpOutPackets_Object = MibScalar
ipRpaBootpOutPackets = _IpRpaBootpOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 3, 1, 7),
    _IpRpaBootpOutPackets_Type()
)
ipRpaBootpOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRpaBootpOutPackets.setStatus("mandatory")
_IpRpaRarpInPackets_Type = Counter32
_IpRpaRarpInPackets_Object = MibScalar
ipRpaRarpInPackets = _IpRpaRarpInPackets_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 3, 1, 8),
    _IpRpaRarpInPackets_Type()
)
ipRpaRarpInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRpaRarpInPackets.setStatus("mandatory")
_IpRpaRarpOutPackets_Type = Counter32
_IpRpaRarpOutPackets_Object = MibScalar
ipRpaRarpOutPackets = _IpRpaRarpOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 3, 1, 9),
    _IpRpaRarpOutPackets_Type()
)
ipRpaRarpOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRpaRarpOutPackets.setStatus("mandatory")
_IpRpaResetAllRasCounters_Type = Integer32
_IpRpaResetAllRasCounters_Object = MibScalar
ipRpaResetAllRasCounters = _IpRpaResetAllRasCounters_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 3, 1, 10),
    _IpRpaResetAllRasCounters_Type()
)
ipRpaResetAllRasCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRpaResetAllRasCounters.setStatus("mandatory")


class _IpRpaPRPAIpHdrCompress_Type(Integer32):
    """Custom type ipRpaPRPAIpHdrCompress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_IpRpaPRPAIpHdrCompress_Type.__name__ = "Integer32"
_IpRpaPRPAIpHdrCompress_Object = MibScalar
ipRpaPRPAIpHdrCompress = _IpRpaPRPAIpHdrCompress_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 3, 1, 11),
    _IpRpaPRPAIpHdrCompress_Type()
)
ipRpaPRPAIpHdrCompress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRpaPRPAIpHdrCompress.setStatus("mandatory")
_IpRt_ObjectIdentity = ObjectIdentity
ipRt = _IpRt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 3, 2)
)
_IpSRouteNumber_Type = Integer32
_IpSRouteNumber_Object = MibScalar
ipSRouteNumber = _IpSRouteNumber_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 3, 2, 1),
    _IpSRouteNumber_Type()
)
ipSRouteNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSRouteNumber.setStatus("mandatory")
_IpSRouteTable_Object = MibTable
ipSRouteTable = _IpSRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 3, 2, 2)
)
if mibBuilder.loadTexts:
    ipSRouteTable.setStatus("mandatory")
_IpSRouteEntry_Object = MibTableRow
ipSRouteEntry = _IpSRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 3, 2, 2, 1)
)
ipSRouteEntry.setIndexNames(
    (0, "Centrum-MIB", "ipSRouteIndex"),
)
if mibBuilder.loadTexts:
    ipSRouteEntry.setStatus("mandatory")
_IpSRouteIndex_Type = Integer32
_IpSRouteIndex_Object = MibTableColumn
ipSRouteIndex = _IpSRouteIndex_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 3, 2, 2, 1, 1),
    _IpSRouteIndex_Type()
)
ipSRouteIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSRouteIndex.setStatus("mandatory")


class _IpSRouteName_Type(DisplayString):
    """Custom type ipSRouteName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_IpSRouteName_Type.__name__ = "DisplayString"
_IpSRouteName_Object = MibTableColumn
ipSRouteName = _IpSRouteName_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 3, 2, 2, 1, 2),
    _IpSRouteName_Type()
)
ipSRouteName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSRouteName.setStatus("mandatory")


class _IpSRouteType_Type(Integer32):
    """Custom type ipSRouteType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_IpSRouteType_Type.__name__ = "Integer32"
_IpSRouteType_Object = MibTableColumn
ipSRouteType = _IpSRouteType_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 3, 2, 2, 1, 3),
    _IpSRouteType_Type()
)
ipSRouteType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSRouteType.setStatus("mandatory")


class _IpSRoutePathType_Type(Integer32):
    """Custom type ipSRoutePathType based on Integer32"""
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


_IpSRoutePathType_Type.__name__ = "Integer32"
_IpSRoutePathType_Object = MibTableColumn
ipSRoutePathType = _IpSRoutePathType_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 3, 2, 2, 1, 4),
    _IpSRoutePathType_Type()
)
ipSRoutePathType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSRoutePathType.setStatus("mandatory")
_IpSRoutePathIdx_Type = Integer32
_IpSRoutePathIdx_Object = MibTableColumn
ipSRoutePathIdx = _IpSRoutePathIdx_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 3, 2, 2, 1, 5),
    _IpSRoutePathIdx_Type()
)
ipSRoutePathIdx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSRoutePathIdx.setStatus("mandatory")
_IpSRouteDestIpAddress_Type = IpAddress
_IpSRouteDestIpAddress_Object = MibTableColumn
ipSRouteDestIpAddress = _IpSRouteDestIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 3, 2, 2, 1, 6),
    _IpSRouteDestIpAddress_Type()
)
ipSRouteDestIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSRouteDestIpAddress.setStatus("mandatory")
_IpSRouteNextRouter_Type = IpAddress
_IpSRouteNextRouter_Object = MibTableColumn
ipSRouteNextRouter = _IpSRouteNextRouter_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 3, 2, 2, 1, 7),
    _IpSRouteNextRouter_Type()
)
ipSRouteNextRouter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSRouteNextRouter.setStatus("mandatory")
_IpSRouteHopCount_Type = Integer32
_IpSRouteHopCount_Object = MibTableColumn
ipSRouteHopCount = _IpSRouteHopCount_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 3, 2, 2, 1, 8),
    _IpSRouteHopCount_Type()
)
ipSRouteHopCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSRouteHopCount.setStatus("mandatory")
_IpPLocalNumber_Type = Integer32
_IpPLocalNumber_Object = MibScalar
ipPLocalNumber = _IpPLocalNumber_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 3, 2, 3),
    _IpPLocalNumber_Type()
)
ipPLocalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPLocalNumber.setStatus("mandatory")
_IpPLocalTable_Object = MibTable
ipPLocalTable = _IpPLocalTable_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 3, 2, 4)
)
if mibBuilder.loadTexts:
    ipPLocalTable.setStatus("mandatory")
_IpPLocalEntry_Object = MibTableRow
ipPLocalEntry = _IpPLocalEntry_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 3, 2, 4, 1)
)
ipPLocalEntry.setIndexNames(
    (0, "Centrum-MIB", "ipPLocalIndex"),
)
if mibBuilder.loadTexts:
    ipPLocalEntry.setStatus("mandatory")
_IpPLocalIndex_Type = Integer32
_IpPLocalIndex_Object = MibTableColumn
ipPLocalIndex = _IpPLocalIndex_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 3, 2, 4, 1, 1),
    _IpPLocalIndex_Type()
)
ipPLocalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPLocalIndex.setStatus("mandatory")
_IpPLocalIpAddress_Type = IpAddress
_IpPLocalIpAddress_Object = MibTableColumn
ipPLocalIpAddress = _IpPLocalIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 3, 2, 4, 1, 2),
    _IpPLocalIpAddress_Type()
)
ipPLocalIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPLocalIpAddress.setStatus("mandatory")
_IpPLocalNetMask_Type = IpAddress
_IpPLocalNetMask_Object = MibTableColumn
ipPLocalNetMask = _IpPLocalNetMask_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 3, 2, 4, 1, 3),
    _IpPLocalNetMask_Type()
)
ipPLocalNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPLocalNetMask.setStatus("mandatory")


class _IpPLocalBcastAddr_Type(Integer32):
    """Custom type ipPLocalBcastAddr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("one-based", 1),
          ("zero-based", 0))
    )


_IpPLocalBcastAddr_Type.__name__ = "Integer32"
_IpPLocalBcastAddr_Object = MibTableColumn
ipPLocalBcastAddr = _IpPLocalBcastAddr_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 3, 2, 4, 1, 4),
    _IpPLocalBcastAddr_Type()
)
ipPLocalBcastAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPLocalBcastAddr.setStatus("mandatory")
_IpPRmtNumber_Type = Integer32
_IpPRmtNumber_Object = MibScalar
ipPRmtNumber = _IpPRmtNumber_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 3, 2, 5),
    _IpPRmtNumber_Type()
)
ipPRmtNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPRmtNumber.setStatus("mandatory")
_IpPRmtTable_Object = MibTable
ipPRmtTable = _IpPRmtTable_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 3, 2, 6)
)
if mibBuilder.loadTexts:
    ipPRmtTable.setStatus("mandatory")
_IpPRmtEntry_Object = MibTableRow
ipPRmtEntry = _IpPRmtEntry_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 3, 2, 6, 1)
)
ipPRmtEntry.setIndexNames(
    (0, "Centrum-MIB", "ipPRmtIndex"),
)
if mibBuilder.loadTexts:
    ipPRmtEntry.setStatus("mandatory")
_IpPRmtIndex_Type = Integer32
_IpPRmtIndex_Object = MibTableColumn
ipPRmtIndex = _IpPRmtIndex_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 3, 2, 6, 1, 1),
    _IpPRmtIndex_Type()
)
ipPRmtIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPRmtIndex.setStatus("mandatory")
_IpPRmtIpAddress_Type = IpAddress
_IpPRmtIpAddress_Object = MibTableColumn
ipPRmtIpAddress = _IpPRmtIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 3, 2, 6, 1, 2),
    _IpPRmtIpAddress_Type()
)
ipPRmtIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPRmtIpAddress.setStatus("mandatory")
_IpPRmtNetMask_Type = IpAddress
_IpPRmtNetMask_Object = MibTableColumn
ipPRmtNetMask = _IpPRmtNetMask_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 3, 2, 6, 1, 3),
    _IpPRmtNetMask_Type()
)
ipPRmtNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPRmtNetMask.setStatus("mandatory")


class _IpPRmtBcastAddr_Type(Integer32):
    """Custom type ipPRmtBcastAddr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("one-based", 1),
          ("zero-based", 0))
    )


_IpPRmtBcastAddr_Type.__name__ = "Integer32"
_IpPRmtBcastAddr_Object = MibTableColumn
ipPRmtBcastAddr = _IpPRmtBcastAddr_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 3, 2, 6, 1, 4),
    _IpPRmtBcastAddr_Type()
)
ipPRmtBcastAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPRmtBcastAddr.setStatus("mandatory")


class _IpPRmtRipUpdate_Type(Integer32):
    """Custom type ipPRmtRipUpdate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("periodic-update", 3),
          ("trigger-update", 2))
    )


_IpPRmtRipUpdate_Type.__name__ = "Integer32"
_IpPRmtRipUpdate_Object = MibTableColumn
ipPRmtRipUpdate = _IpPRmtRipUpdate_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 3, 2, 6, 1, 5),
    _IpPRmtRipUpdate_Type()
)
ipPRmtRipUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPRmtRipUpdate.setStatus("mandatory")


class _IpPRmtType_Type(Integer32):
    """Custom type ipPRmtType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_IpPRmtType_Type.__name__ = "Integer32"
_IpPRmtType_Object = MibTableColumn
ipPRmtType = _IpPRmtType_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 3, 2, 6, 1, 6),
    _IpPRmtType_Type()
)
ipPRmtType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPRmtType.setStatus("mandatory")


class _IpPRmtTcpHdrCompress_Type(Integer32):
    """Custom type ipPRmtTcpHdrCompress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_IpPRmtTcpHdrCompress_Type.__name__ = "Integer32"
_IpPRmtTcpHdrCompress_Object = MibTableColumn
ipPRmtTcpHdrCompress = _IpPRmtTcpHdrCompress_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 3, 2, 6, 1, 7),
    _IpPRmtTcpHdrCompress_Type()
)
ipPRmtTcpHdrCompress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPRmtTcpHdrCompress.setStatus("mandatory")
_IpRtUpdateTime_Type = Integer32
_IpRtUpdateTime_Object = MibScalar
ipRtUpdateTime = _IpRtUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 3, 2, 7),
    _IpRtUpdateTime_Type()
)
ipRtUpdateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRtUpdateTime.setStatus("mandatory")


class _IpRtRipEnabled_Type(Integer32):
    """Custom type ipRtRipEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_IpRtRipEnabled_Type.__name__ = "Integer32"
_IpRtRipEnabled_Object = MibScalar
ipRtRipEnabled = _IpRtRipEnabled_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 3, 2, 8),
    _IpRtRipEnabled_Type()
)
ipRtRipEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRtRipEnabled.setStatus("mandatory")


class _IpRtEnabled_Type(Integer32):
    """Custom type ipRtEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_IpRtEnabled_Type.__name__ = "Integer32"
_IpRtEnabled_Object = MibScalar
ipRtEnabled = _IpRtEnabled_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 3, 2, 9),
    _IpRtEnabled_Type()
)
ipRtEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRtEnabled.setStatus("mandatory")
_IpRtDefaultTTL_Type = Integer32
_IpRtDefaultTTL_Object = MibScalar
ipRtDefaultTTL = _IpRtDefaultTTL_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 3, 2, 10),
    _IpRtDefaultTTL_Type()
)
ipRtDefaultTTL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRtDefaultTTL.setStatus("mandatory")


class _IpRtPoisonReverse_Type(Integer32):
    """Custom type ipRtPoisonReverse based on Integer32"""
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


_IpRtPoisonReverse_Type.__name__ = "Integer32"
_IpRtPoisonReverse_Object = MibScalar
ipRtPoisonReverse = _IpRtPoisonReverse_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 3, 2, 11),
    _IpRtPoisonReverse_Type()
)
ipRtPoisonReverse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRtPoisonReverse.setStatus("mandatory")
_IpRtResetAllCounters_Type = Integer32
_IpRtResetAllCounters_Object = MibScalar
ipRtResetAllCounters = _IpRtResetAllCounters_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 3, 2, 12),
    _IpRtResetAllCounters_Type()
)
ipRtResetAllCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRtResetAllCounters.setStatus("mandatory")
_IpRtInPackets_Type = Counter32
_IpRtInPackets_Object = MibScalar
ipRtInPackets = _IpRtInPackets_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 3, 2, 13),
    _IpRtInPackets_Type()
)
ipRtInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRtInPackets.setStatus("mandatory")
_IpRtOutPackets_Type = Counter32
_IpRtOutPackets_Object = MibScalar
ipRtOutPackets = _IpRtOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 3, 2, 14),
    _IpRtOutPackets_Type()
)
ipRtOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRtOutPackets.setStatus("mandatory")
_IpRtDefaultRouterAddress_Type = IpAddress
_IpRtDefaultRouterAddress_Object = MibScalar
ipRtDefaultRouterAddress = _IpRtDefaultRouterAddress_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 3, 2, 15),
    _IpRtDefaultRouterAddress_Type()
)
ipRtDefaultRouterAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRtDefaultRouterAddress.setStatus("mandatory")


class _IpRtDefaultRouterPathType_Type(Integer32):
    """Custom type ipRtDefaultRouterPathType based on Integer32"""
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


_IpRtDefaultRouterPathType_Type.__name__ = "Integer32"
_IpRtDefaultRouterPathType_Object = MibScalar
ipRtDefaultRouterPathType = _IpRtDefaultRouterPathType_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 3, 2, 16),
    _IpRtDefaultRouterPathType_Type()
)
ipRtDefaultRouterPathType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRtDefaultRouterPathType.setStatus("mandatory")
_IpRtDefaultRouterPathIdx_Type = Integer32
_IpRtDefaultRouterPathIdx_Object = MibScalar
ipRtDefaultRouterPathIdx = _IpRtDefaultRouterPathIdx_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 3, 2, 17),
    _IpRtDefaultRouterPathIdx_Type()
)
ipRtDefaultRouterPathIdx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRtDefaultRouterPathIdx.setStatus("mandatory")


class _IpRtDiscardNBBcastPkts_Type(Integer32):
    """Custom type ipRtDiscardNBBcastPkts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_IpRtDiscardNBBcastPkts_Type.__name__ = "Integer32"
_IpRtDiscardNBBcastPkts_Object = MibScalar
ipRtDiscardNBBcastPkts = _IpRtDiscardNBBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 3, 2, 18),
    _IpRtDiscardNBBcastPkts_Type()
)
ipRtDiscardNBBcastPkts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRtDiscardNBBcastPkts.setStatus("mandatory")
_Ipx_ObjectIdentity = ObjectIdentity
ipx = _Ipx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 4)
)
_IpxRpa_ObjectIdentity = ObjectIdentity
ipxRpa = _IpxRpa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 4, 1)
)


class _IpxRpaNetNumber_Type(OctetString):
    """Custom type ipxRpaNetNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_IpxRpaNetNumber_Type.__name__ = "OctetString"
_IpxRpaNetNumber_Object = MibScalar
ipxRpaNetNumber = _IpxRpaNetNumber_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 4, 1, 1),
    _IpxRpaNetNumber_Type()
)
ipxRpaNetNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxRpaNetNumber.setStatus("mandatory")
_IpxRpaNumber_Type = Integer32
_IpxRpaNumber_Object = MibScalar
ipxRpaNumber = _IpxRpaNumber_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 4, 1, 2),
    _IpxRpaNumber_Type()
)
ipxRpaNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxRpaNumber.setStatus("mandatory")
_IpxRpaTable_Object = MibTable
ipxRpaTable = _IpxRpaTable_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 4, 1, 3)
)
if mibBuilder.loadTexts:
    ipxRpaTable.setStatus("mandatory")
_IpxRpaEntry_Object = MibTableRow
ipxRpaEntry = _IpxRpaEntry_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 4, 1, 3, 1)
)
ipxRpaEntry.setIndexNames(
    (0, "Centrum-MIB", "ipxRpaIndex"),
)
if mibBuilder.loadTexts:
    ipxRpaEntry.setStatus("mandatory")
_IpxRpaIndex_Type = Integer32
_IpxRpaIndex_Object = MibTableColumn
ipxRpaIndex = _IpxRpaIndex_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 4, 1, 3, 1, 1),
    _IpxRpaIndex_Type()
)
ipxRpaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxRpaIndex.setStatus("mandatory")


class _IpxRpaCurrHostAddr_Type(OctetString):
    """Custom type ipxRpaCurrHostAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_IpxRpaCurrHostAddr_Type.__name__ = "OctetString"
_IpxRpaCurrHostAddr_Object = MibTableColumn
ipxRpaCurrHostAddr = _IpxRpaCurrHostAddr_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 4, 1, 3, 1, 2),
    _IpxRpaCurrHostAddr_Type()
)
ipxRpaCurrHostAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxRpaCurrHostAddr.setStatus("mandatory")
_IpxRt_ObjectIdentity = ObjectIdentity
ipxRt = _IpxRt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 4, 2)
)
_IpxSRouteNumber_Type = Integer32
_IpxSRouteNumber_Object = MibScalar
ipxSRouteNumber = _IpxSRouteNumber_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 4, 2, 1),
    _IpxSRouteNumber_Type()
)
ipxSRouteNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxSRouteNumber.setStatus("mandatory")
_IpxSRouteTable_Object = MibTable
ipxSRouteTable = _IpxSRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 4, 2, 2)
)
if mibBuilder.loadTexts:
    ipxSRouteTable.setStatus("mandatory")
_IpxSRouteEntry_Object = MibTableRow
ipxSRouteEntry = _IpxSRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 4, 2, 2, 1)
)
ipxSRouteEntry.setIndexNames(
    (0, "Centrum-MIB", "ipxSRouteIndex"),
)
if mibBuilder.loadTexts:
    ipxSRouteEntry.setStatus("mandatory")
_IpxSRouteIndex_Type = Integer32
_IpxSRouteIndex_Object = MibTableColumn
ipxSRouteIndex = _IpxSRouteIndex_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 4, 2, 2, 1, 1),
    _IpxSRouteIndex_Type()
)
ipxSRouteIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxSRouteIndex.setStatus("mandatory")


class _IpxSRouteName_Type(DisplayString):
    """Custom type ipxSRouteName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_IpxSRouteName_Type.__name__ = "DisplayString"
_IpxSRouteName_Object = MibTableColumn
ipxSRouteName = _IpxSRouteName_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 4, 2, 2, 1, 2),
    _IpxSRouteName_Type()
)
ipxSRouteName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxSRouteName.setStatus("mandatory")


class _IpxSRouteType_Type(Integer32):
    """Custom type ipxSRouteType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_IpxSRouteType_Type.__name__ = "Integer32"
_IpxSRouteType_Object = MibTableColumn
ipxSRouteType = _IpxSRouteType_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 4, 2, 2, 1, 3),
    _IpxSRouteType_Type()
)
ipxSRouteType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxSRouteType.setStatus("mandatory")


class _IpxSRoutePathType_Type(Integer32):
    """Custom type ipxSRoutePathType based on Integer32"""
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


_IpxSRoutePathType_Type.__name__ = "Integer32"
_IpxSRoutePathType_Object = MibTableColumn
ipxSRoutePathType = _IpxSRoutePathType_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 4, 2, 2, 1, 4),
    _IpxSRoutePathType_Type()
)
ipxSRoutePathType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxSRoutePathType.setStatus("mandatory")
_IpxSRoutePathIdx_Type = Integer32
_IpxSRoutePathIdx_Object = MibTableColumn
ipxSRoutePathIdx = _IpxSRoutePathIdx_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 4, 2, 2, 1, 5),
    _IpxSRoutePathIdx_Type()
)
ipxSRoutePathIdx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxSRoutePathIdx.setStatus("mandatory")


class _IpxSRouteDestNetNumber_Type(OctetString):
    """Custom type ipxSRouteDestNetNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_IpxSRouteDestNetNumber_Type.__name__ = "OctetString"
_IpxSRouteDestNetNumber_Object = MibTableColumn
ipxSRouteDestNetNumber = _IpxSRouteDestNetNumber_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 4, 2, 2, 1, 6),
    _IpxSRouteDestNetNumber_Type()
)
ipxSRouteDestNetNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxSRouteDestNetNumber.setStatus("mandatory")


class _IpxSRouteNextHostAddress_Type(OctetString):
    """Custom type ipxSRouteNextHostAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_IpxSRouteNextHostAddress_Type.__name__ = "OctetString"
_IpxSRouteNextHostAddress_Object = MibTableColumn
ipxSRouteNextHostAddress = _IpxSRouteNextHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 4, 2, 2, 1, 8),
    _IpxSRouteNextHostAddress_Type()
)
ipxSRouteNextHostAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxSRouteNextHostAddress.setStatus("mandatory")
_IpxSRouteHopCount_Type = Integer32
_IpxSRouteHopCount_Object = MibTableColumn
ipxSRouteHopCount = _IpxSRouteHopCount_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 4, 2, 2, 1, 9),
    _IpxSRouteHopCount_Type()
)
ipxSRouteHopCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxSRouteHopCount.setStatus("mandatory")
_IpxPLocalNumber_Type = Integer32
_IpxPLocalNumber_Object = MibScalar
ipxPLocalNumber = _IpxPLocalNumber_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 4, 2, 3),
    _IpxPLocalNumber_Type()
)
ipxPLocalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxPLocalNumber.setStatus("mandatory")
_IpxPLocalTable_Object = MibTable
ipxPLocalTable = _IpxPLocalTable_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 4, 2, 4)
)
if mibBuilder.loadTexts:
    ipxPLocalTable.setStatus("mandatory")
_IpxPLocalEntry_Object = MibTableRow
ipxPLocalEntry = _IpxPLocalEntry_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 4, 2, 4, 1)
)
ipxPLocalEntry.setIndexNames(
    (0, "Centrum-MIB", "ipxPLocalIndex"),
)
if mibBuilder.loadTexts:
    ipxPLocalEntry.setStatus("mandatory")
_IpxPLocalIndex_Type = Integer32
_IpxPLocalIndex_Object = MibTableColumn
ipxPLocalIndex = _IpxPLocalIndex_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 4, 2, 4, 1, 1),
    _IpxPLocalIndex_Type()
)
ipxPLocalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxPLocalIndex.setStatus("mandatory")


class _IpxPLocalNetNumber_Type(OctetString):
    """Custom type ipxPLocalNetNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_IpxPLocalNetNumber_Type.__name__ = "OctetString"
_IpxPLocalNetNumber_Object = MibTableColumn
ipxPLocalNetNumber = _IpxPLocalNetNumber_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 4, 2, 4, 1, 2),
    _IpxPLocalNetNumber_Type()
)
ipxPLocalNetNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxPLocalNetNumber.setStatus("mandatory")


class _IpxPLocalDataLinkType_Type(Integer32):
    """Custom type ipxPLocalDataLinkType based on Integer32"""
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
        *(("autolearn", 5),
          ("ethernet", 2),
          ("ieee8022", 4),
          ("ieee8023", 1),
          ("snap", 3),
          ("trsap", 7),
          ("trsnap", 6))
    )


_IpxPLocalDataLinkType_Type.__name__ = "Integer32"
_IpxPLocalDataLinkType_Object = MibTableColumn
ipxPLocalDataLinkType = _IpxPLocalDataLinkType_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 4, 2, 4, 1, 3),
    _IpxPLocalDataLinkType_Type()
)
ipxPLocalDataLinkType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxPLocalDataLinkType.setStatus("mandatory")
_IpxPRmtNumber_Type = Integer32
_IpxPRmtNumber_Object = MibScalar
ipxPRmtNumber = _IpxPRmtNumber_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 4, 2, 5),
    _IpxPRmtNumber_Type()
)
ipxPRmtNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxPRmtNumber.setStatus("mandatory")
_IpxPRmtTable_Object = MibTable
ipxPRmtTable = _IpxPRmtTable_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 4, 2, 6)
)
if mibBuilder.loadTexts:
    ipxPRmtTable.setStatus("mandatory")
_IpxPRmtEntry_Object = MibTableRow
ipxPRmtEntry = _IpxPRmtEntry_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 4, 2, 6, 1)
)
ipxPRmtEntry.setIndexNames(
    (0, "Centrum-MIB", "ipxPRmtIndex"),
)
if mibBuilder.loadTexts:
    ipxPRmtEntry.setStatus("mandatory")
_IpxPRmtIndex_Type = Integer32
_IpxPRmtIndex_Object = MibTableColumn
ipxPRmtIndex = _IpxPRmtIndex_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 4, 2, 6, 1, 1),
    _IpxPRmtIndex_Type()
)
ipxPRmtIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxPRmtIndex.setStatus("mandatory")


class _IpxPRmtNetNumber_Type(OctetString):
    """Custom type ipxPRmtNetNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_IpxPRmtNetNumber_Type.__name__ = "OctetString"
_IpxPRmtNetNumber_Object = MibTableColumn
ipxPRmtNetNumber = _IpxPRmtNetNumber_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 4, 2, 6, 1, 2),
    _IpxPRmtNetNumber_Type()
)
ipxPRmtNetNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxPRmtNetNumber.setStatus("mandatory")


class _IpxPRmtNripUpdate_Type(Integer32):
    """Custom type ipxPRmtNripUpdate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("periodic-update", 3),
          ("trigger-update", 2))
    )


_IpxPRmtNripUpdate_Type.__name__ = "Integer32"
_IpxPRmtNripUpdate_Object = MibTableColumn
ipxPRmtNripUpdate = _IpxPRmtNripUpdate_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 4, 2, 6, 1, 3),
    _IpxPRmtNripUpdate_Type()
)
ipxPRmtNripUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxPRmtNripUpdate.setStatus("mandatory")


class _IpxPRmtType_Type(Integer32):
    """Custom type ipxPRmtType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_IpxPRmtType_Type.__name__ = "Integer32"
_IpxPRmtType_Object = MibTableColumn
ipxPRmtType = _IpxPRmtType_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 4, 2, 6, 1, 4),
    _IpxPRmtType_Type()
)
ipxPRmtType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxPRmtType.setStatus("mandatory")
_IpxRtUpdateTime_Type = Integer32
_IpxRtUpdateTime_Object = MibScalar
ipxRtUpdateTime = _IpxRtUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 4, 2, 7),
    _IpxRtUpdateTime_Type()
)
ipxRtUpdateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxRtUpdateTime.setStatus("mandatory")


class _IpxRtEnabled_Type(Integer32):
    """Custom type ipxRtEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_IpxRtEnabled_Type.__name__ = "Integer32"
_IpxRtEnabled_Object = MibScalar
ipxRtEnabled = _IpxRtEnabled_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 4, 2, 8),
    _IpxRtEnabled_Type()
)
ipxRtEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxRtEnabled.setStatus("mandatory")


class _IpxRtRipEnabled_Type(Integer32):
    """Custom type ipxRtRipEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_IpxRtRipEnabled_Type.__name__ = "Integer32"
_IpxRtRipEnabled_Object = MibScalar
ipxRtRipEnabled = _IpxRtRipEnabled_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 4, 2, 9),
    _IpxRtRipEnabled_Type()
)
ipxRtRipEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxRtRipEnabled.setStatus("mandatory")
_IpxRtResetAllCounters_Type = Integer32
_IpxRtResetAllCounters_Object = MibScalar
ipxRtResetAllCounters = _IpxRtResetAllCounters_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 4, 2, 11),
    _IpxRtResetAllCounters_Type()
)
ipxRtResetAllCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxRtResetAllCounters.setStatus("mandatory")
_IpxRtInPackets_Type = Counter32
_IpxRtInPackets_Object = MibScalar
ipxRtInPackets = _IpxRtInPackets_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 4, 2, 12),
    _IpxRtInPackets_Type()
)
ipxRtInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxRtInPackets.setStatus("mandatory")
_IpxRtOutPackets_Type = Counter32
_IpxRtOutPackets_Object = MibScalar
ipxRtOutPackets = _IpxRtOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 4, 2, 13),
    _IpxRtOutPackets_Type()
)
ipxRtOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxRtOutPackets.setStatus("mandatory")
_IpxRtRipNumber_Type = Integer32
_IpxRtRipNumber_Object = MibScalar
ipxRtRipNumber = _IpxRtRipNumber_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 4, 2, 14),
    _IpxRtRipNumber_Type()
)
ipxRtRipNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxRtRipNumber.setStatus("mandatory")
_IpxRtRipTable_Object = MibTable
ipxRtRipTable = _IpxRtRipTable_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 4, 2, 15)
)
if mibBuilder.loadTexts:
    ipxRtRipTable.setStatus("mandatory")
_IpxRtRipEntry_Object = MibTableRow
ipxRtRipEntry = _IpxRtRipEntry_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 4, 2, 15, 1)
)
ipxRtRipEntry.setIndexNames(
    (0, "Centrum-MIB", "ipxRtRipDestNetNumber"),
)
if mibBuilder.loadTexts:
    ipxRtRipEntry.setStatus("mandatory")


class _IpxRtRipDestNetNumber_Type(OctetString):
    """Custom type ipxRtRipDestNetNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_IpxRtRipDestNetNumber_Type.__name__ = "OctetString"
_IpxRtRipDestNetNumber_Object = MibTableColumn
ipxRtRipDestNetNumber = _IpxRtRipDestNetNumber_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 4, 2, 15, 1, 1),
    _IpxRtRipDestNetNumber_Type()
)
ipxRtRipDestNetNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxRtRipDestNetNumber.setStatus("mandatory")


class _IpxRtRipPathType_Type(Integer32):
    """Custom type ipxRtRipPathType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("proxy", 3),
          ("remote", 2))
    )


_IpxRtRipPathType_Type.__name__ = "Integer32"
_IpxRtRipPathType_Object = MibTableColumn
ipxRtRipPathType = _IpxRtRipPathType_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 4, 2, 15, 1, 2),
    _IpxRtRipPathType_Type()
)
ipxRtRipPathType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxRtRipPathType.setStatus("mandatory")
_IpxRtRipPathIdx_Type = Integer32
_IpxRtRipPathIdx_Object = MibTableColumn
ipxRtRipPathIdx = _IpxRtRipPathIdx_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 4, 2, 15, 1, 3),
    _IpxRtRipPathIdx_Type()
)
ipxRtRipPathIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxRtRipPathIdx.setStatus("mandatory")


class _IpxRtRipNextHostAddress_Type(OctetString):
    """Custom type ipxRtRipNextHostAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_IpxRtRipNextHostAddress_Type.__name__ = "OctetString"
_IpxRtRipNextHostAddress_Object = MibTableColumn
ipxRtRipNextHostAddress = _IpxRtRipNextHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 4, 2, 15, 1, 4),
    _IpxRtRipNextHostAddress_Type()
)
ipxRtRipNextHostAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxRtRipNextHostAddress.setStatus("mandatory")
_IpxRtRipHopCount_Type = Integer32
_IpxRtRipHopCount_Object = MibTableColumn
ipxRtRipHopCount = _IpxRtRipHopCount_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 4, 2, 15, 1, 5),
    _IpxRtRipHopCount_Type()
)
ipxRtRipHopCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxRtRipHopCount.setStatus("mandatory")
_IpxRtRipTicks_Type = Integer32
_IpxRtRipTicks_Object = MibTableColumn
ipxRtRipTicks = _IpxRtRipTicks_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 4, 2, 15, 1, 6),
    _IpxRtRipTicks_Type()
)
ipxRtRipTicks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxRtRipTicks.setStatus("mandatory")


class _IpxRtRipRouteType_Type(Integer32):
    """Custom type ipxRtRipRouteType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("permanent", 1),
          ("static", 3))
    )


_IpxRtRipRouteType_Type.__name__ = "Integer32"
_IpxRtRipRouteType_Object = MibTableColumn
ipxRtRipRouteType = _IpxRtRipRouteType_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 4, 2, 15, 1, 7),
    _IpxRtRipRouteType_Type()
)
ipxRtRipRouteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxRtRipRouteType.setStatus("mandatory")
_IpxRtSapNumber_Type = Integer32
_IpxRtSapNumber_Object = MibScalar
ipxRtSapNumber = _IpxRtSapNumber_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 4, 2, 16),
    _IpxRtSapNumber_Type()
)
ipxRtSapNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxRtSapNumber.setStatus("mandatory")
_IpxRtSapTable_Object = MibTable
ipxRtSapTable = _IpxRtSapTable_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 4, 2, 17)
)
if mibBuilder.loadTexts:
    ipxRtSapTable.setStatus("mandatory")
_IpxRtSapEntry_Object = MibTableRow
ipxRtSapEntry = _IpxRtSapEntry_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 4, 2, 17, 1)
)
ipxRtSapEntry.setIndexNames(
    (0, "Centrum-MIB", "ipxRtSapIndex"),
)
if mibBuilder.loadTexts:
    ipxRtSapEntry.setStatus("mandatory")
_IpxRtSapIndex_Type = Integer32
_IpxRtSapIndex_Object = MibTableColumn
ipxRtSapIndex = _IpxRtSapIndex_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 4, 2, 17, 1, 1),
    _IpxRtSapIndex_Type()
)
ipxRtSapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxRtSapIndex.setStatus("mandatory")


class _IpxRtSapServiceName_Type(OctetString):
    """Custom type ipxRtSapServiceName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(48, 48),
    )


_IpxRtSapServiceName_Type.__name__ = "OctetString"
_IpxRtSapServiceName_Object = MibTableColumn
ipxRtSapServiceName = _IpxRtSapServiceName_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 4, 2, 17, 1, 2),
    _IpxRtSapServiceName_Type()
)
ipxRtSapServiceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxRtSapServiceName.setStatus("mandatory")
_IpxRtSapServiceType_Type = Integer32
_IpxRtSapServiceType_Object = MibTableColumn
ipxRtSapServiceType = _IpxRtSapServiceType_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 4, 2, 17, 1, 3),
    _IpxRtSapServiceType_Type()
)
ipxRtSapServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxRtSapServiceType.setStatus("mandatory")


class _IpxRtSapServerNetNumber_Type(OctetString):
    """Custom type ipxRtSapServerNetNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_IpxRtSapServerNetNumber_Type.__name__ = "OctetString"
_IpxRtSapServerNetNumber_Object = MibTableColumn
ipxRtSapServerNetNumber = _IpxRtSapServerNetNumber_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 4, 2, 17, 1, 4),
    _IpxRtSapServerNetNumber_Type()
)
ipxRtSapServerNetNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxRtSapServerNetNumber.setStatus("mandatory")


class _IpxRtSapServerHostAddress_Type(OctetString):
    """Custom type ipxRtSapServerHostAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_IpxRtSapServerHostAddress_Type.__name__ = "OctetString"
_IpxRtSapServerHostAddress_Object = MibTableColumn
ipxRtSapServerHostAddress = _IpxRtSapServerHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 4, 2, 17, 1, 5),
    _IpxRtSapServerHostAddress_Type()
)
ipxRtSapServerHostAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxRtSapServerHostAddress.setStatus("mandatory")
_IpxSpoofingTime_Type = Integer32
_IpxSpoofingTime_Object = MibScalar
ipxSpoofingTime = _IpxSpoofingTime_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 4, 2, 18),
    _IpxSpoofingTime_Type()
)
ipxSpoofingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxSpoofingTime.setStatus("mandatory")


class _IpxRtDoNBPropagation_Type(Integer32):
    """Custom type ipxRtDoNBPropagation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_IpxRtDoNBPropagation_Type.__name__ = "Integer32"
_IpxRtDoNBPropagation_Object = MibScalar
ipxRtDoNBPropagation = _IpxRtDoNBPropagation_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 4, 2, 19),
    _IpxRtDoNBPropagation_Type()
)
ipxRtDoNBPropagation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxRtDoNBPropagation.setStatus("mandatory")
_Brg_ObjectIdentity = ObjectIdentity
brg = _Brg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 5)
)
_BrgFilterNumber_Type = Integer32
_BrgFilterNumber_Object = MibScalar
brgFilterNumber = _BrgFilterNumber_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 5, 1),
    _BrgFilterNumber_Type()
)
brgFilterNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brgFilterNumber.setStatus("mandatory")
_BrgFilterTable_Object = MibTable
brgFilterTable = _BrgFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 5, 2)
)
if mibBuilder.loadTexts:
    brgFilterTable.setStatus("mandatory")
_BrgFilterEntry_Object = MibTableRow
brgFilterEntry = _BrgFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 5, 2, 1)
)
brgFilterEntry.setIndexNames(
    (0, "Centrum-MIB", "brgFilterIndex"),
)
if mibBuilder.loadTexts:
    brgFilterEntry.setStatus("mandatory")
_BrgFilterIndex_Type = Integer32
_BrgFilterIndex_Object = MibTableColumn
brgFilterIndex = _BrgFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 5, 2, 1, 1),
    _BrgFilterIndex_Type()
)
brgFilterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brgFilterIndex.setStatus("mandatory")


class _BrgFilterName_Type(DisplayString):
    """Custom type brgFilterName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_BrgFilterName_Type.__name__ = "DisplayString"
_BrgFilterName_Object = MibTableColumn
brgFilterName = _BrgFilterName_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 5, 2, 1, 2),
    _BrgFilterName_Type()
)
brgFilterName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brgFilterName.setStatus("mandatory")


class _BrgFilterType_Type(Integer32):
    """Custom type brgFilterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_BrgFilterType_Type.__name__ = "Integer32"
_BrgFilterType_Object = MibTableColumn
brgFilterType = _BrgFilterType_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 5, 2, 1, 3),
    _BrgFilterType_Type()
)
brgFilterType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brgFilterType.setStatus("mandatory")


class _BrgFilterMask1Offset_Type(Integer32):
    """Custom type brgFilterMask1Offset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BrgFilterMask1Offset_Type.__name__ = "Integer32"
_BrgFilterMask1Offset_Object = MibTableColumn
brgFilterMask1Offset = _BrgFilterMask1Offset_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 5, 2, 1, 4),
    _BrgFilterMask1Offset_Type()
)
brgFilterMask1Offset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brgFilterMask1Offset.setStatus("mandatory")
_BrgFilterMask1Value_Type = Integer32
_BrgFilterMask1Value_Object = MibTableColumn
brgFilterMask1Value = _BrgFilterMask1Value_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 5, 2, 1, 5),
    _BrgFilterMask1Value_Type()
)
brgFilterMask1Value.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brgFilterMask1Value.setStatus("mandatory")


class _BrgFilterMask1Type_Type(Integer32):
    """Custom type brgFilterMask1Type based on Integer32"""
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
        *(("and", 4),
          ("equal", 2),
          ("invalid", 1),
          ("not", 5),
          ("or", 3))
    )


_BrgFilterMask1Type_Type.__name__ = "Integer32"
_BrgFilterMask1Type_Object = MibTableColumn
brgFilterMask1Type = _BrgFilterMask1Type_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 5, 2, 1, 6),
    _BrgFilterMask1Type_Type()
)
brgFilterMask1Type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brgFilterMask1Type.setStatus("mandatory")


class _BrgFilterMask1Size_Type(Integer32):
    """Custom type brgFilterMask1Size based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("byte", 1),
          ("half-word", 2),
          ("word", 3))
    )


_BrgFilterMask1Size_Type.__name__ = "Integer32"
_BrgFilterMask1Size_Object = MibTableColumn
brgFilterMask1Size = _BrgFilterMask1Size_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 5, 2, 1, 7),
    _BrgFilterMask1Size_Type()
)
brgFilterMask1Size.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brgFilterMask1Size.setStatus("mandatory")


class _BrgFilterMask2Offset_Type(Integer32):
    """Custom type brgFilterMask2Offset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BrgFilterMask2Offset_Type.__name__ = "Integer32"
_BrgFilterMask2Offset_Object = MibTableColumn
brgFilterMask2Offset = _BrgFilterMask2Offset_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 5, 2, 1, 8),
    _BrgFilterMask2Offset_Type()
)
brgFilterMask2Offset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brgFilterMask2Offset.setStatus("mandatory")
_BrgFilterMask2Value_Type = Integer32
_BrgFilterMask2Value_Object = MibTableColumn
brgFilterMask2Value = _BrgFilterMask2Value_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 5, 2, 1, 9),
    _BrgFilterMask2Value_Type()
)
brgFilterMask2Value.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brgFilterMask2Value.setStatus("mandatory")


class _BrgFilterMask2Type_Type(Integer32):
    """Custom type brgFilterMask2Type based on Integer32"""
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
        *(("and", 4),
          ("equal", 2),
          ("invalid", 1),
          ("not", 5),
          ("or", 3))
    )


_BrgFilterMask2Type_Type.__name__ = "Integer32"
_BrgFilterMask2Type_Object = MibTableColumn
brgFilterMask2Type = _BrgFilterMask2Type_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 5, 2, 1, 10),
    _BrgFilterMask2Type_Type()
)
brgFilterMask2Type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brgFilterMask2Type.setStatus("mandatory")


class _BrgFilterMask2Size_Type(Integer32):
    """Custom type brgFilterMask2Size based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("byte", 1),
          ("half-word", 2),
          ("word", 3))
    )


_BrgFilterMask2Size_Type.__name__ = "Integer32"
_BrgFilterMask2Size_Object = MibTableColumn
brgFilterMask2Size = _BrgFilterMask2Size_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 5, 2, 1, 11),
    _BrgFilterMask2Size_Type()
)
brgFilterMask2Size.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brgFilterMask2Size.setStatus("mandatory")


class _BrgFilterMask3Offset_Type(Integer32):
    """Custom type brgFilterMask3Offset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BrgFilterMask3Offset_Type.__name__ = "Integer32"
_BrgFilterMask3Offset_Object = MibTableColumn
brgFilterMask3Offset = _BrgFilterMask3Offset_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 5, 2, 1, 12),
    _BrgFilterMask3Offset_Type()
)
brgFilterMask3Offset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brgFilterMask3Offset.setStatus("mandatory")
_BrgFilterMask3Value_Type = Integer32
_BrgFilterMask3Value_Object = MibTableColumn
brgFilterMask3Value = _BrgFilterMask3Value_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 5, 2, 1, 13),
    _BrgFilterMask3Value_Type()
)
brgFilterMask3Value.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brgFilterMask3Value.setStatus("mandatory")


class _BrgFilterMask3Type_Type(Integer32):
    """Custom type brgFilterMask3Type based on Integer32"""
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
        *(("and", 4),
          ("equal", 2),
          ("invalid", 1),
          ("not", 5),
          ("or", 3))
    )


_BrgFilterMask3Type_Type.__name__ = "Integer32"
_BrgFilterMask3Type_Object = MibTableColumn
brgFilterMask3Type = _BrgFilterMask3Type_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 5, 2, 1, 14),
    _BrgFilterMask3Type_Type()
)
brgFilterMask3Type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brgFilterMask3Type.setStatus("mandatory")


class _BrgFilterMask3Size_Type(Integer32):
    """Custom type brgFilterMask3Size based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("byte", 1),
          ("half-word", 2),
          ("word", 3))
    )


_BrgFilterMask3Size_Type.__name__ = "Integer32"
_BrgFilterMask3Size_Object = MibTableColumn
brgFilterMask3Size = _BrgFilterMask3Size_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 5, 2, 1, 15),
    _BrgFilterMask3Size_Type()
)
brgFilterMask3Size.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brgFilterMask3Size.setStatus("mandatory")


class _BrgFilterMask4Offset_Type(Integer32):
    """Custom type brgFilterMask4Offset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BrgFilterMask4Offset_Type.__name__ = "Integer32"
_BrgFilterMask4Offset_Object = MibTableColumn
brgFilterMask4Offset = _BrgFilterMask4Offset_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 5, 2, 1, 16),
    _BrgFilterMask4Offset_Type()
)
brgFilterMask4Offset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brgFilterMask4Offset.setStatus("mandatory")
_BrgFilterMask4Value_Type = Integer32
_BrgFilterMask4Value_Object = MibTableColumn
brgFilterMask4Value = _BrgFilterMask4Value_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 5, 2, 1, 17),
    _BrgFilterMask4Value_Type()
)
brgFilterMask4Value.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brgFilterMask4Value.setStatus("mandatory")


class _BrgFilterMask4Type_Type(Integer32):
    """Custom type brgFilterMask4Type based on Integer32"""
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
        *(("and", 4),
          ("equal", 2),
          ("invalid", 1),
          ("not", 5),
          ("or", 3))
    )


_BrgFilterMask4Type_Type.__name__ = "Integer32"
_BrgFilterMask4Type_Object = MibTableColumn
brgFilterMask4Type = _BrgFilterMask4Type_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 5, 2, 1, 18),
    _BrgFilterMask4Type_Type()
)
brgFilterMask4Type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brgFilterMask4Type.setStatus("mandatory")


class _BrgFilterMask4Size_Type(Integer32):
    """Custom type brgFilterMask4Size based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("byte", 1),
          ("half-word", 2),
          ("word", 3))
    )


_BrgFilterMask4Size_Type.__name__ = "Integer32"
_BrgFilterMask4Size_Object = MibTableColumn
brgFilterMask4Size = _BrgFilterMask4Size_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 5, 2, 1, 19),
    _BrgFilterMask4Size_Type()
)
brgFilterMask4Size.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brgFilterMask4Size.setStatus("mandatory")


class _BrgFilterSkipRii_Type(Integer32):
    """Custom type brgFilterSkipRii based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_BrgFilterSkipRii_Type.__name__ = "Integer32"
_BrgFilterSkipRii_Object = MibTableColumn
brgFilterSkipRii = _BrgFilterSkipRii_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 5, 2, 1, 20),
    _BrgFilterSkipRii_Type()
)
brgFilterSkipRii.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brgFilterSkipRii.setStatus("mandatory")
_BrgLoggerNumber_Type = Integer32
_BrgLoggerNumber_Object = MibScalar
brgLoggerNumber = _BrgLoggerNumber_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 5, 3),
    _BrgLoggerNumber_Type()
)
brgLoggerNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brgLoggerNumber.setStatus("mandatory")
_BrgLoggerTable_Object = MibTable
brgLoggerTable = _BrgLoggerTable_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 5, 4)
)
if mibBuilder.loadTexts:
    brgLoggerTable.setStatus("mandatory")
_BrgLoggerEntry_Object = MibTableRow
brgLoggerEntry = _BrgLoggerEntry_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 5, 4, 1)
)
brgLoggerEntry.setIndexNames(
    (0, "Centrum-MIB", "brgLoggerIndex"),
)
if mibBuilder.loadTexts:
    brgLoggerEntry.setStatus("mandatory")
_BrgLoggerIndex_Type = Integer32
_BrgLoggerIndex_Object = MibTableColumn
brgLoggerIndex = _BrgLoggerIndex_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 5, 4, 1, 1),
    _BrgLoggerIndex_Type()
)
brgLoggerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brgLoggerIndex.setStatus("mandatory")


class _BrgLoggerName_Type(DisplayString):
    """Custom type brgLoggerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_BrgLoggerName_Type.__name__ = "DisplayString"
_BrgLoggerName_Object = MibTableColumn
brgLoggerName = _BrgLoggerName_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 5, 4, 1, 2),
    _BrgLoggerName_Type()
)
brgLoggerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brgLoggerName.setStatus("mandatory")


class _BrgLoggerType_Type(Integer32):
    """Custom type brgLoggerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_BrgLoggerType_Type.__name__ = "Integer32"
_BrgLoggerType_Object = MibTableColumn
brgLoggerType = _BrgLoggerType_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 5, 4, 1, 3),
    _BrgLoggerType_Type()
)
brgLoggerType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brgLoggerType.setStatus("mandatory")


class _BrgLoggerMask1Offset_Type(Integer32):
    """Custom type brgLoggerMask1Offset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BrgLoggerMask1Offset_Type.__name__ = "Integer32"
_BrgLoggerMask1Offset_Object = MibTableColumn
brgLoggerMask1Offset = _BrgLoggerMask1Offset_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 5, 4, 1, 4),
    _BrgLoggerMask1Offset_Type()
)
brgLoggerMask1Offset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brgLoggerMask1Offset.setStatus("mandatory")
_BrgLoggerMask1Value_Type = Integer32
_BrgLoggerMask1Value_Object = MibTableColumn
brgLoggerMask1Value = _BrgLoggerMask1Value_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 5, 4, 1, 5),
    _BrgLoggerMask1Value_Type()
)
brgLoggerMask1Value.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brgLoggerMask1Value.setStatus("mandatory")


class _BrgLoggerMask1Type_Type(Integer32):
    """Custom type brgLoggerMask1Type based on Integer32"""
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
        *(("and", 4),
          ("equal", 2),
          ("invalid", 1),
          ("not", 5),
          ("or", 3))
    )


_BrgLoggerMask1Type_Type.__name__ = "Integer32"
_BrgLoggerMask1Type_Object = MibTableColumn
brgLoggerMask1Type = _BrgLoggerMask1Type_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 5, 4, 1, 6),
    _BrgLoggerMask1Type_Type()
)
brgLoggerMask1Type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brgLoggerMask1Type.setStatus("mandatory")


class _BrgLoggerMask1Size_Type(Integer32):
    """Custom type brgLoggerMask1Size based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("byte", 1),
          ("half-word", 2),
          ("word", 3))
    )


_BrgLoggerMask1Size_Type.__name__ = "Integer32"
_BrgLoggerMask1Size_Object = MibTableColumn
brgLoggerMask1Size = _BrgLoggerMask1Size_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 5, 4, 1, 7),
    _BrgLoggerMask1Size_Type()
)
brgLoggerMask1Size.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brgLoggerMask1Size.setStatus("mandatory")


class _BrgLoggerMask2Offset_Type(Integer32):
    """Custom type brgLoggerMask2Offset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BrgLoggerMask2Offset_Type.__name__ = "Integer32"
_BrgLoggerMask2Offset_Object = MibTableColumn
brgLoggerMask2Offset = _BrgLoggerMask2Offset_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 5, 4, 1, 8),
    _BrgLoggerMask2Offset_Type()
)
brgLoggerMask2Offset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brgLoggerMask2Offset.setStatus("mandatory")
_BrgLoggerMask2Value_Type = Integer32
_BrgLoggerMask2Value_Object = MibTableColumn
brgLoggerMask2Value = _BrgLoggerMask2Value_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 5, 4, 1, 9),
    _BrgLoggerMask2Value_Type()
)
brgLoggerMask2Value.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brgLoggerMask2Value.setStatus("mandatory")


class _BrgLoggerMask2Type_Type(Integer32):
    """Custom type brgLoggerMask2Type based on Integer32"""
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
        *(("and", 4),
          ("equal", 2),
          ("invalid", 1),
          ("not", 5),
          ("or", 3))
    )


_BrgLoggerMask2Type_Type.__name__ = "Integer32"
_BrgLoggerMask2Type_Object = MibTableColumn
brgLoggerMask2Type = _BrgLoggerMask2Type_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 5, 4, 1, 10),
    _BrgLoggerMask2Type_Type()
)
brgLoggerMask2Type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brgLoggerMask2Type.setStatus("mandatory")


class _BrgLoggerMask2Size_Type(Integer32):
    """Custom type brgLoggerMask2Size based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("byte", 1),
          ("half-word", 2),
          ("word", 3))
    )


_BrgLoggerMask2Size_Type.__name__ = "Integer32"
_BrgLoggerMask2Size_Object = MibTableColumn
brgLoggerMask2Size = _BrgLoggerMask2Size_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 5, 4, 1, 11),
    _BrgLoggerMask2Size_Type()
)
brgLoggerMask2Size.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brgLoggerMask2Size.setStatus("mandatory")


class _BrgLoggerMask3Offset_Type(Integer32):
    """Custom type brgLoggerMask3Offset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BrgLoggerMask3Offset_Type.__name__ = "Integer32"
_BrgLoggerMask3Offset_Object = MibTableColumn
brgLoggerMask3Offset = _BrgLoggerMask3Offset_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 5, 4, 1, 12),
    _BrgLoggerMask3Offset_Type()
)
brgLoggerMask3Offset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brgLoggerMask3Offset.setStatus("mandatory")
_BrgLoggerMask3Value_Type = Integer32
_BrgLoggerMask3Value_Object = MibTableColumn
brgLoggerMask3Value = _BrgLoggerMask3Value_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 5, 4, 1, 13),
    _BrgLoggerMask3Value_Type()
)
brgLoggerMask3Value.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brgLoggerMask3Value.setStatus("mandatory")


class _BrgLoggerMask3Type_Type(Integer32):
    """Custom type brgLoggerMask3Type based on Integer32"""
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
        *(("and", 4),
          ("equal", 2),
          ("invalid", 1),
          ("not", 5),
          ("or", 3))
    )


_BrgLoggerMask3Type_Type.__name__ = "Integer32"
_BrgLoggerMask3Type_Object = MibTableColumn
brgLoggerMask3Type = _BrgLoggerMask3Type_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 5, 4, 1, 14),
    _BrgLoggerMask3Type_Type()
)
brgLoggerMask3Type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brgLoggerMask3Type.setStatus("mandatory")


class _BrgLoggerMask3Size_Type(Integer32):
    """Custom type brgLoggerMask3Size based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("byte", 1),
          ("half-word", 2),
          ("word", 3))
    )


_BrgLoggerMask3Size_Type.__name__ = "Integer32"
_BrgLoggerMask3Size_Object = MibTableColumn
brgLoggerMask3Size = _BrgLoggerMask3Size_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 5, 4, 1, 15),
    _BrgLoggerMask3Size_Type()
)
brgLoggerMask3Size.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brgLoggerMask3Size.setStatus("mandatory")


class _BrgLoggerMask4Offset_Type(Integer32):
    """Custom type brgLoggerMask4Offset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BrgLoggerMask4Offset_Type.__name__ = "Integer32"
_BrgLoggerMask4Offset_Object = MibTableColumn
brgLoggerMask4Offset = _BrgLoggerMask4Offset_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 5, 4, 1, 16),
    _BrgLoggerMask4Offset_Type()
)
brgLoggerMask4Offset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brgLoggerMask4Offset.setStatus("mandatory")
_BrgLoggerMask4Value_Type = Integer32
_BrgLoggerMask4Value_Object = MibTableColumn
brgLoggerMask4Value = _BrgLoggerMask4Value_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 5, 4, 1, 17),
    _BrgLoggerMask4Value_Type()
)
brgLoggerMask4Value.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brgLoggerMask4Value.setStatus("mandatory")


class _BrgLoggerMask4Type_Type(Integer32):
    """Custom type brgLoggerMask4Type based on Integer32"""
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
        *(("and", 4),
          ("equal", 2),
          ("invalid", 1),
          ("not", 5),
          ("or", 3))
    )


_BrgLoggerMask4Type_Type.__name__ = "Integer32"
_BrgLoggerMask4Type_Object = MibTableColumn
brgLoggerMask4Type = _BrgLoggerMask4Type_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 5, 4, 1, 18),
    _BrgLoggerMask4Type_Type()
)
brgLoggerMask4Type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brgLoggerMask4Type.setStatus("mandatory")


class _BrgLoggerMask4Size_Type(Integer32):
    """Custom type brgLoggerMask4Size based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("byte", 1),
          ("half-word", 2),
          ("word", 3))
    )


_BrgLoggerMask4Size_Type.__name__ = "Integer32"
_BrgLoggerMask4Size_Object = MibTableColumn
brgLoggerMask4Size = _BrgLoggerMask4Size_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 5, 4, 1, 19),
    _BrgLoggerMask4Size_Type()
)
brgLoggerMask4Size.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brgLoggerMask4Size.setStatus("mandatory")


class _BrgLoggerSkipRii_Type(Integer32):
    """Custom type brgLoggerSkipRii based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_BrgLoggerSkipRii_Type.__name__ = "Integer32"
_BrgLoggerSkipRii_Object = MibTableColumn
brgLoggerSkipRii = _BrgLoggerSkipRii_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 5, 4, 1, 20),
    _BrgLoggerSkipRii_Type()
)
brgLoggerSkipRii.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brgLoggerSkipRii.setStatus("mandatory")
_BrgPLocalNumber_Type = Integer32
_BrgPLocalNumber_Object = MibScalar
brgPLocalNumber = _BrgPLocalNumber_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 5, 5),
    _BrgPLocalNumber_Type()
)
brgPLocalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brgPLocalNumber.setStatus("mandatory")
_BrgPLocalTable_Object = MibTable
brgPLocalTable = _BrgPLocalTable_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 5, 6)
)
if mibBuilder.loadTexts:
    brgPLocalTable.setStatus("mandatory")
_BrgPLocalEntry_Object = MibTableRow
brgPLocalEntry = _BrgPLocalEntry_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 5, 6, 1)
)
brgPLocalEntry.setIndexNames(
    (0, "Centrum-MIB", "brgPLocalIndex"),
)
if mibBuilder.loadTexts:
    brgPLocalEntry.setStatus("mandatory")
_BrgPLocalIndex_Type = Integer32
_BrgPLocalIndex_Object = MibTableColumn
brgPLocalIndex = _BrgPLocalIndex_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 5, 6, 1, 1),
    _BrgPLocalIndex_Type()
)
brgPLocalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brgPLocalIndex.setStatus("mandatory")


class _BrgPLocalEnabled_Type(Integer32):
    """Custom type brgPLocalEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_BrgPLocalEnabled_Type.__name__ = "Integer32"
_BrgPLocalEnabled_Object = MibTableColumn
brgPLocalEnabled = _BrgPLocalEnabled_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 5, 6, 1, 2),
    _BrgPLocalEnabled_Type()
)
brgPLocalEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brgPLocalEnabled.setStatus("mandatory")
_BrgStpPLocalPriority_Type = Integer32
_BrgStpPLocalPriority_Object = MibTableColumn
brgStpPLocalPriority = _BrgStpPLocalPriority_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 5, 6, 1, 3),
    _BrgStpPLocalPriority_Type()
)
brgStpPLocalPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brgStpPLocalPriority.setStatus("mandatory")
_BrgStpPLocalCost_Type = Integer32
_BrgStpPLocalCost_Object = MibTableColumn
brgStpPLocalCost = _BrgStpPLocalCost_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 5, 6, 1, 4),
    _BrgStpPLocalCost_Type()
)
brgStpPLocalCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brgStpPLocalCost.setStatus("mandatory")


class _BrgStpPLocalDesigRoot_Type(OctetString):
    """Custom type brgStpPLocalDesigRoot based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_BrgStpPLocalDesigRoot_Type.__name__ = "OctetString"
_BrgStpPLocalDesigRoot_Object = MibTableColumn
brgStpPLocalDesigRoot = _BrgStpPLocalDesigRoot_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 5, 6, 1, 5),
    _BrgStpPLocalDesigRoot_Type()
)
brgStpPLocalDesigRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brgStpPLocalDesigRoot.setStatus("mandatory")
_BrgStpPLocalDesigCost_Type = Integer32
_BrgStpPLocalDesigCost_Object = MibTableColumn
brgStpPLocalDesigCost = _BrgStpPLocalDesigCost_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 5, 6, 1, 6),
    _BrgStpPLocalDesigCost_Type()
)
brgStpPLocalDesigCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brgStpPLocalDesigCost.setStatus("mandatory")


class _BrgStpPLocalDesigBridge_Type(OctetString):
    """Custom type brgStpPLocalDesigBridge based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_BrgStpPLocalDesigBridge_Type.__name__ = "OctetString"
_BrgStpPLocalDesigBridge_Object = MibTableColumn
brgStpPLocalDesigBridge = _BrgStpPLocalDesigBridge_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 5, 6, 1, 7),
    _BrgStpPLocalDesigBridge_Type()
)
brgStpPLocalDesigBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brgStpPLocalDesigBridge.setStatus("mandatory")
_BrgStpPLocalDesigPath_Type = Integer32
_BrgStpPLocalDesigPath_Object = MibTableColumn
brgStpPLocalDesigPath = _BrgStpPLocalDesigPath_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 5, 6, 1, 8),
    _BrgStpPLocalDesigPath_Type()
)
brgStpPLocalDesigPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brgStpPLocalDesigPath.setStatus("mandatory")


class _BrgStpPLocalPathState_Type(Integer32):
    """Custom type brgStpPLocalPathState based on Integer32"""
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
        *(("blocking", 2),
          ("disabled", 255),
          ("forwarding", 4),
          ("learning", 3),
          ("listening", 1))
    )


_BrgStpPLocalPathState_Type.__name__ = "Integer32"
_BrgStpPLocalPathState_Object = MibTableColumn
brgStpPLocalPathState = _BrgStpPLocalPathState_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 5, 6, 1, 9),
    _BrgStpPLocalPathState_Type()
)
brgStpPLocalPathState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brgStpPLocalPathState.setStatus("mandatory")
_BrgPRmtNumber_Type = Integer32
_BrgPRmtNumber_Object = MibScalar
brgPRmtNumber = _BrgPRmtNumber_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 5, 7),
    _BrgPRmtNumber_Type()
)
brgPRmtNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brgPRmtNumber.setStatus("mandatory")
_BrgPRmtTable_Object = MibTable
brgPRmtTable = _BrgPRmtTable_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 5, 8)
)
if mibBuilder.loadTexts:
    brgPRmtTable.setStatus("mandatory")
_BrgPRmtEntry_Object = MibTableRow
brgPRmtEntry = _BrgPRmtEntry_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 5, 8, 1)
)
brgPRmtEntry.setIndexNames(
    (0, "Centrum-MIB", "brgPRmtIndex"),
)
if mibBuilder.loadTexts:
    brgPRmtEntry.setStatus("mandatory")
_BrgPRmtIndex_Type = Integer32
_BrgPRmtIndex_Object = MibTableColumn
brgPRmtIndex = _BrgPRmtIndex_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 5, 8, 1, 1),
    _BrgPRmtIndex_Type()
)
brgPRmtIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brgPRmtIndex.setStatus("mandatory")


class _BrgPRmtEnabled_Type(Integer32):
    """Custom type brgPRmtEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_BrgPRmtEnabled_Type.__name__ = "Integer32"
_BrgPRmtEnabled_Object = MibTableColumn
brgPRmtEnabled = _BrgPRmtEnabled_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 5, 8, 1, 2),
    _BrgPRmtEnabled_Type()
)
brgPRmtEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brgPRmtEnabled.setStatus("mandatory")
_BrgStpPRmtPriority_Type = Integer32
_BrgStpPRmtPriority_Object = MibTableColumn
brgStpPRmtPriority = _BrgStpPRmtPriority_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 5, 8, 1, 3),
    _BrgStpPRmtPriority_Type()
)
brgStpPRmtPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brgStpPRmtPriority.setStatus("mandatory")
_BrgStpPRmtCost_Type = Integer32
_BrgStpPRmtCost_Object = MibTableColumn
brgStpPRmtCost = _BrgStpPRmtCost_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 5, 8, 1, 4),
    _BrgStpPRmtCost_Type()
)
brgStpPRmtCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brgStpPRmtCost.setStatus("mandatory")


class _BrgStpPRmtDesigRoot_Type(OctetString):
    """Custom type brgStpPRmtDesigRoot based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_BrgStpPRmtDesigRoot_Type.__name__ = "OctetString"
_BrgStpPRmtDesigRoot_Object = MibTableColumn
brgStpPRmtDesigRoot = _BrgStpPRmtDesigRoot_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 5, 8, 1, 5),
    _BrgStpPRmtDesigRoot_Type()
)
brgStpPRmtDesigRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brgStpPRmtDesigRoot.setStatus("mandatory")
_BrgStpPRmtDesigCost_Type = Integer32
_BrgStpPRmtDesigCost_Object = MibTableColumn
brgStpPRmtDesigCost = _BrgStpPRmtDesigCost_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 5, 8, 1, 6),
    _BrgStpPRmtDesigCost_Type()
)
brgStpPRmtDesigCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brgStpPRmtDesigCost.setStatus("mandatory")


class _BrgStpPRmtDesigBridge_Type(OctetString):
    """Custom type brgStpPRmtDesigBridge based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_BrgStpPRmtDesigBridge_Type.__name__ = "OctetString"
_BrgStpPRmtDesigBridge_Object = MibTableColumn
brgStpPRmtDesigBridge = _BrgStpPRmtDesigBridge_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 5, 8, 1, 7),
    _BrgStpPRmtDesigBridge_Type()
)
brgStpPRmtDesigBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brgStpPRmtDesigBridge.setStatus("mandatory")
_BrgStpPRmtDesigPath_Type = Integer32
_BrgStpPRmtDesigPath_Object = MibTableColumn
brgStpPRmtDesigPath = _BrgStpPRmtDesigPath_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 5, 8, 1, 8),
    _BrgStpPRmtDesigPath_Type()
)
brgStpPRmtDesigPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brgStpPRmtDesigPath.setStatus("mandatory")


class _BrgStpPRmtPathState_Type(Integer32):
    """Custom type brgStpPRmtPathState based on Integer32"""
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
        *(("blocking", 2),
          ("disabled", 255),
          ("forwarding", 4),
          ("learning", 3),
          ("listening", 1))
    )


_BrgStpPRmtPathState_Type.__name__ = "Integer32"
_BrgStpPRmtPathState_Object = MibTableColumn
brgStpPRmtPathState = _BrgStpPRmtPathState_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 5, 8, 1, 9),
    _BrgStpPRmtPathState_Type()
)
brgStpPRmtPathState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brgStpPRmtPathState.setStatus("mandatory")
_BrgMisc_ObjectIdentity = ObjectIdentity
brgMisc = _BrgMisc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 5, 9)
)


class _BrgSpanningTreeProtocol_Type(Integer32):
    """Custom type brgSpanningTreeProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enable", 2))
    )


_BrgSpanningTreeProtocol_Type.__name__ = "Integer32"
_BrgSpanningTreeProtocol_Object = MibScalar
brgSpanningTreeProtocol = _BrgSpanningTreeProtocol_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 5, 9, 1),
    _BrgSpanningTreeProtocol_Type()
)
brgSpanningTreeProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brgSpanningTreeProtocol.setStatus("mandatory")
_BrgResetAllCounters_Type = Integer32
_BrgResetAllCounters_Object = MibScalar
brgResetAllCounters = _BrgResetAllCounters_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 5, 9, 2),
    _BrgResetAllCounters_Type()
)
brgResetAllCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brgResetAllCounters.setStatus("mandatory")


class _BrgAutoFtrEnabled_Type(Integer32):
    """Custom type brgAutoFtrEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enable", 2))
    )


_BrgAutoFtrEnabled_Type.__name__ = "Integer32"
_BrgAutoFtrEnabled_Object = MibScalar
brgAutoFtrEnabled = _BrgAutoFtrEnabled_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 5, 9, 3),
    _BrgAutoFtrEnabled_Type()
)
brgAutoFtrEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brgAutoFtrEnabled.setStatus("mandatory")


class _BrgPRPASmartFiltering_Type(Integer32):
    """Custom type brgPRPASmartFiltering based on Integer32"""
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


_BrgPRPASmartFiltering_Type.__name__ = "Integer32"
_BrgPRPASmartFiltering_Object = MibScalar
brgPRPASmartFiltering = _BrgPRPASmartFiltering_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 5, 9, 4),
    _BrgPRPASmartFiltering_Type()
)
brgPRPASmartFiltering.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brgPRPASmartFiltering.setStatus("mandatory")


class _BrgPRPAFilterAction_Type(Integer32):
    """Custom type brgPRPAFilterAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discard", 1),
          ("forward", 2))
    )


_BrgPRPAFilterAction_Type.__name__ = "Integer32"
_BrgPRPAFilterAction_Object = MibScalar
brgPRPAFilterAction = _BrgPRPAFilterAction_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 5, 9, 5),
    _BrgPRPAFilterAction_Type()
)
brgPRPAFilterAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brgPRPAFilterAction.setStatus("mandatory")


class _BrgPRPAFilterMap_Type(Integer32):
    """Custom type brgPRPAFilterMap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_BrgPRPAFilterMap_Type.__name__ = "Integer32"
_BrgPRPAFilterMap_Object = MibScalar
brgPRPAFilterMap = _BrgPRPAFilterMap_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 5, 9, 6),
    _BrgPRPAFilterMap_Type()
)
brgPRPAFilterMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brgPRPAFilterMap.setStatus("mandatory")


class _BrgPRPALoggerMap_Type(Integer32):
    """Custom type brgPRPALoggerMap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_BrgPRPALoggerMap_Type.__name__ = "Integer32"
_BrgPRPALoggerMap_Object = MibScalar
brgPRPALoggerMap = _BrgPRPALoggerMap_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 5, 9, 7),
    _BrgPRPALoggerMap_Type()
)
brgPRPALoggerMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brgPRPALoggerMap.setStatus("mandatory")


class _BrgMacHdrComp_Type(Integer32):
    """Custom type brgMacHdrComp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_BrgMacHdrComp_Type.__name__ = "Integer32"
_BrgMacHdrComp_Object = MibScalar
brgMacHdrComp = _BrgMacHdrComp_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 5, 9, 8),
    _BrgMacHdrComp_Type()
)
brgMacHdrComp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brgMacHdrComp.setStatus("mandatory")
_BrgLearnedTable_Object = MibTable
brgLearnedTable = _BrgLearnedTable_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 5, 10)
)
if mibBuilder.loadTexts:
    brgLearnedTable.setStatus("mandatory")
_BrgLearnedEntry_Object = MibTableRow
brgLearnedEntry = _BrgLearnedEntry_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 5, 10, 1)
)
brgLearnedEntry.setIndexNames(
    (0, "Centrum-MIB", "brgLearnedAddress"),
)
if mibBuilder.loadTexts:
    brgLearnedEntry.setStatus("mandatory")


class _BrgLearnedAddress_Type(OctetString):
    """Custom type brgLearnedAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_BrgLearnedAddress_Type.__name__ = "OctetString"
_BrgLearnedAddress_Object = MibTableColumn
brgLearnedAddress = _BrgLearnedAddress_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 5, 10, 1, 1),
    _BrgLearnedAddress_Type()
)
brgLearnedAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brgLearnedAddress.setStatus("mandatory")


class _BrgLearnedPathType_Type(Integer32):
    """Custom type brgLearnedPathType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("permanent", 3),
          ("remote", 2))
    )


_BrgLearnedPathType_Type.__name__ = "Integer32"
_BrgLearnedPathType_Object = MibTableColumn
brgLearnedPathType = _BrgLearnedPathType_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 5, 10, 1, 2),
    _BrgLearnedPathType_Type()
)
brgLearnedPathType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brgLearnedPathType.setStatus("mandatory")
_BrgLearnedPathIdx_Type = Integer32
_BrgLearnedPathIdx_Object = MibTableColumn
brgLearnedPathIdx = _BrgLearnedPathIdx_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 5, 10, 1, 3),
    _BrgLearnedPathIdx_Type()
)
brgLearnedPathIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brgLearnedPathIdx.setStatus("mandatory")


class _BrgLearnedAge_Type(Integer32):
    """Custom type brgLearnedAge based on Integer32"""
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
        *(("middle", 2),
          ("old", 3),
          ("permanent", 4),
          ("young", 1))
    )


_BrgLearnedAge_Type.__name__ = "Integer32"
_BrgLearnedAge_Object = MibTableColumn
brgLearnedAge = _BrgLearnedAge_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 5, 10, 1, 4),
    _BrgLearnedAge_Type()
)
brgLearnedAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brgLearnedAge.setStatus("mandatory")
_BrgTokenRing_ObjectIdentity = ObjectIdentity
brgTokenRing = _BrgTokenRing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 5, 11)
)
_BrgLocalRingNumber_Type = Integer32
_BrgLocalRingNumber_Object = MibScalar
brgLocalRingNumber = _BrgLocalRingNumber_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 5, 11, 1),
    _BrgLocalRingNumber_Type()
)
brgLocalRingNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brgLocalRingNumber.setStatus("mandatory")
_BrgProxyRingNumber_Type = Integer32
_BrgProxyRingNumber_Object = MibScalar
brgProxyRingNumber = _BrgProxyRingNumber_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 5, 11, 2),
    _BrgProxyRingNumber_Type()
)
brgProxyRingNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brgProxyRingNumber.setStatus("mandatory")
_BrgBridgeNumber_Type = Integer32
_BrgBridgeNumber_Object = MibScalar
brgBridgeNumber = _BrgBridgeNumber_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 5, 11, 3),
    _BrgBridgeNumber_Type()
)
brgBridgeNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brgBridgeNumber.setStatus("mandatory")
_Admin_ObjectIdentity = ObjectIdentity
admin = _Admin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6)
)
_AdminUserNumber_Type = Integer32
_AdminUserNumber_Object = MibScalar
adminUserNumber = _AdminUserNumber_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 1),
    _AdminUserNumber_Type()
)
adminUserNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adminUserNumber.setStatus("mandatory")
_AdminUserTable_Object = MibTable
adminUserTable = _AdminUserTable_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 2)
)
if mibBuilder.loadTexts:
    adminUserTable.setStatus("mandatory")
_AdminUserEntry_Object = MibTableRow
adminUserEntry = _AdminUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 2, 1)
)
adminUserEntry.setIndexNames(
    (0, "Centrum-MIB", "adminUserIndex"),
)
if mibBuilder.loadTexts:
    adminUserEntry.setStatus("mandatory")
_AdminUserIndex_Type = Integer32
_AdminUserIndex_Object = MibTableColumn
adminUserIndex = _AdminUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 2, 1, 1),
    _AdminUserIndex_Type()
)
adminUserIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adminUserIndex.setStatus("mandatory")


class _AdminUserName_Type(DisplayString):
    """Custom type adminUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_AdminUserName_Type.__name__ = "DisplayString"
_AdminUserName_Object = MibTableColumn
adminUserName = _AdminUserName_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 2, 1, 2),
    _AdminUserName_Type()
)
adminUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminUserName.setStatus("mandatory")


class _AdminUserType_Type(Integer32):
    """Custom type adminUserType based on Integer32"""
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
        *(("admin", 3),
          ("invalid", 1),
          ("su", 4),
          ("user", 2))
    )


_AdminUserType_Type.__name__ = "Integer32"
_AdminUserType_Object = MibTableColumn
adminUserType = _AdminUserType_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 2, 1, 3),
    _AdminUserType_Type()
)
adminUserType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminUserType.setStatus("mandatory")


class _AdminUserPassword_Type(OctetString):
    """Custom type adminUserPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_AdminUserPassword_Type.__name__ = "OctetString"
_AdminUserPassword_Object = MibTableColumn
adminUserPassword = _AdminUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 2, 1, 4),
    _AdminUserPassword_Type()
)
adminUserPassword.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adminUserPassword.setStatus("mandatory")


class _AdminUserCallBackPhone_Type(OctetString):
    """Custom type adminUserCallBackPhone based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_AdminUserCallBackPhone_Type.__name__ = "OctetString"
_AdminUserCallBackPhone_Object = MibTableColumn
adminUserCallBackPhone = _AdminUserCallBackPhone_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 2, 1, 5),
    _AdminUserCallBackPhone_Type()
)
adminUserCallBackPhone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adminUserCallBackPhone.setStatus("mandatory")


class _AdminEncryptUserPassword_Type(OctetString):
    """Custom type adminEncryptUserPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_AdminEncryptUserPassword_Type.__name__ = "OctetString"
_AdminEncryptUserPassword_Object = MibTableColumn
adminEncryptUserPassword = _AdminEncryptUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 2, 1, 6),
    _AdminEncryptUserPassword_Type()
)
adminEncryptUserPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminEncryptUserPassword.setStatus("mandatory")


class _AdminEncryptCallBackPhone_Type(OctetString):
    """Custom type adminEncryptCallBackPhone based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_AdminEncryptCallBackPhone_Type.__name__ = "OctetString"
_AdminEncryptCallBackPhone_Object = MibTableColumn
adminEncryptCallBackPhone = _AdminEncryptCallBackPhone_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 2, 1, 7),
    _AdminEncryptCallBackPhone_Type()
)
adminEncryptCallBackPhone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminEncryptCallBackPhone.setStatus("mandatory")
_AdminCommNumber_Type = Integer32
_AdminCommNumber_Object = MibScalar
adminCommNumber = _AdminCommNumber_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 3),
    _AdminCommNumber_Type()
)
adminCommNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adminCommNumber.setStatus("mandatory")
_AdminCommTable_Object = MibTable
adminCommTable = _AdminCommTable_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 4)
)
if mibBuilder.loadTexts:
    adminCommTable.setStatus("mandatory")
_AdminCommEntry_Object = MibTableRow
adminCommEntry = _AdminCommEntry_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 4, 1)
)
adminCommEntry.setIndexNames(
    (0, "Centrum-MIB", "adminCommIndex"),
)
if mibBuilder.loadTexts:
    adminCommEntry.setStatus("mandatory")
_AdminCommIndex_Type = Integer32
_AdminCommIndex_Object = MibTableColumn
adminCommIndex = _AdminCommIndex_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 4, 1, 1),
    _AdminCommIndex_Type()
)
adminCommIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adminCommIndex.setStatus("mandatory")


class _AdminCommName_Type(DisplayString):
    """Custom type adminCommName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_AdminCommName_Type.__name__ = "DisplayString"
_AdminCommName_Object = MibTableColumn
adminCommName = _AdminCommName_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 4, 1, 2),
    _AdminCommName_Type()
)
adminCommName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminCommName.setStatus("mandatory")


class _AdminCommType_Type(Integer32):
    """Custom type adminCommType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("readOnly", 2),
          ("readWrite", 3))
    )


_AdminCommType_Type.__name__ = "Integer32"
_AdminCommType_Object = MibTableColumn
adminCommType = _AdminCommType_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 4, 1, 3),
    _AdminCommType_Type()
)
adminCommType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminCommType.setStatus("mandatory")
_AdminCommMgrIpAddress_Type = IpAddress
_AdminCommMgrIpAddress_Object = MibTableColumn
adminCommMgrIpAddress = _AdminCommMgrIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 4, 1, 4),
    _AdminCommMgrIpAddress_Type()
)
adminCommMgrIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminCommMgrIpAddress.setStatus("mandatory")


class _AdminCommMgrIpxNetNumber_Type(OctetString):
    """Custom type adminCommMgrIpxNetNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_AdminCommMgrIpxNetNumber_Type.__name__ = "OctetString"
_AdminCommMgrIpxNetNumber_Object = MibTableColumn
adminCommMgrIpxNetNumber = _AdminCommMgrIpxNetNumber_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 4, 1, 5),
    _AdminCommMgrIpxNetNumber_Type()
)
adminCommMgrIpxNetNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminCommMgrIpxNetNumber.setStatus("mandatory")


class _AdminCommMgrMacAddress_Type(OctetString):
    """Custom type adminCommMgrMacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_AdminCommMgrMacAddress_Type.__name__ = "OctetString"
_AdminCommMgrMacAddress_Object = MibTableColumn
adminCommMgrMacAddress = _AdminCommMgrMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 4, 1, 6),
    _AdminCommMgrMacAddress_Type()
)
adminCommMgrMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminCommMgrMacAddress.setStatus("mandatory")
_AdminScriptNumber_Type = Integer32
_AdminScriptNumber_Object = MibScalar
adminScriptNumber = _AdminScriptNumber_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 5),
    _AdminScriptNumber_Type()
)
adminScriptNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adminScriptNumber.setStatus("mandatory")
_AdminScriptTable_Object = MibTable
adminScriptTable = _AdminScriptTable_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 6)
)
if mibBuilder.loadTexts:
    adminScriptTable.setStatus("mandatory")
_AdminScriptEntry_Object = MibTableRow
adminScriptEntry = _AdminScriptEntry_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 6, 1)
)
adminScriptEntry.setIndexNames(
    (0, "Centrum-MIB", "adminScriptIndex"),
)
if mibBuilder.loadTexts:
    adminScriptEntry.setStatus("mandatory")
_AdminScriptIndex_Type = Integer32
_AdminScriptIndex_Object = MibTableColumn
adminScriptIndex = _AdminScriptIndex_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 6, 1, 1),
    _AdminScriptIndex_Type()
)
adminScriptIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adminScriptIndex.setStatus("mandatory")


class _AdminScriptName_Type(DisplayString):
    """Custom type adminScriptName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_AdminScriptName_Type.__name__ = "DisplayString"
_AdminScriptName_Object = MibTableColumn
adminScriptName = _AdminScriptName_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 6, 1, 2),
    _AdminScriptName_Type()
)
adminScriptName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adminScriptName.setStatus("mandatory")


class _AdminScriptType_Type(Integer32):
    """Custom type adminScriptType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("built-in", 2),
          ("invalid", 1),
          ("user-defined", 3))
    )


_AdminScriptType_Type.__name__ = "Integer32"
_AdminScriptType_Object = MibTableColumn
adminScriptType = _AdminScriptType_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 6, 1, 3),
    _AdminScriptType_Type()
)
adminScriptType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminScriptType.setStatus("mandatory")


class _AdminScript_Type(OctetString):
    """Custom type adminScript based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 527),
    )


_AdminScript_Type.__name__ = "OctetString"
_AdminScript_Object = MibTableColumn
adminScript = _AdminScript_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 6, 1, 4),
    _AdminScript_Type()
)
adminScript.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminScript.setStatus("mandatory")
_AdminRpaLogNumber_Type = Integer32
_AdminRpaLogNumber_Object = MibScalar
adminRpaLogNumber = _AdminRpaLogNumber_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 7),
    _AdminRpaLogNumber_Type()
)
adminRpaLogNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adminRpaLogNumber.setStatus("mandatory")
_AdminRpaLogTable_Object = MibTable
adminRpaLogTable = _AdminRpaLogTable_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 8)
)
if mibBuilder.loadTexts:
    adminRpaLogTable.setStatus("mandatory")
_AdminRpaLogEntry_Object = MibTableRow
adminRpaLogEntry = _AdminRpaLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 8, 1)
)
adminRpaLogEntry.setIndexNames(
    (0, "Centrum-MIB", "adminRpaLogIndex"),
)
if mibBuilder.loadTexts:
    adminRpaLogEntry.setStatus("mandatory")
_AdminRpaLogIndex_Type = Integer32
_AdminRpaLogIndex_Object = MibTableColumn
adminRpaLogIndex = _AdminRpaLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 8, 1, 1),
    _AdminRpaLogIndex_Type()
)
adminRpaLogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adminRpaLogIndex.setStatus("mandatory")


class _AdminRpaLogUserName_Type(DisplayString):
    """Custom type adminRpaLogUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_AdminRpaLogUserName_Type.__name__ = "DisplayString"
_AdminRpaLogUserName_Object = MibTableColumn
adminRpaLogUserName = _AdminRpaLogUserName_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 8, 1, 2),
    _AdminRpaLogUserName_Type()
)
adminRpaLogUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adminRpaLogUserName.setStatus("mandatory")


class _AdminRpaLogTime_Type(DisplayString):
    """Custom type adminRpaLogTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_AdminRpaLogTime_Type.__name__ = "DisplayString"
_AdminRpaLogTime_Object = MibTableColumn
adminRpaLogTime = _AdminRpaLogTime_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 8, 1, 3),
    _AdminRpaLogTime_Type()
)
adminRpaLogTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adminRpaLogTime.setStatus("mandatory")


class _AdminRpaLogDuration_Type(DisplayString):
    """Custom type adminRpaLogDuration based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_AdminRpaLogDuration_Type.__name__ = "DisplayString"
_AdminRpaLogDuration_Object = MibTableColumn
adminRpaLogDuration = _AdminRpaLogDuration_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 8, 1, 4),
    _AdminRpaLogDuration_Type()
)
adminRpaLogDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adminRpaLogDuration.setStatus("mandatory")
_AdminRpaLogAttempts_Type = Counter32
_AdminRpaLogAttempts_Object = MibTableColumn
adminRpaLogAttempts = _AdminRpaLogAttempts_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 8, 1, 5),
    _AdminRpaLogAttempts_Type()
)
adminRpaLogAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adminRpaLogAttempts.setStatus("mandatory")
_AdminRpaLogInPackets_Type = Counter32
_AdminRpaLogInPackets_Object = MibTableColumn
adminRpaLogInPackets = _AdminRpaLogInPackets_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 8, 1, 6),
    _AdminRpaLogInPackets_Type()
)
adminRpaLogInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adminRpaLogInPackets.setStatus("mandatory")
_AdminRpaLogOutPackets_Type = Counter32
_AdminRpaLogOutPackets_Object = MibTableColumn
adminRpaLogOutPackets = _AdminRpaLogOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 8, 1, 7),
    _AdminRpaLogOutPackets_Type()
)
adminRpaLogOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adminRpaLogOutPackets.setStatus("mandatory")
_AdminRpaLogInBytes_Type = Counter32
_AdminRpaLogInBytes_Object = MibTableColumn
adminRpaLogInBytes = _AdminRpaLogInBytes_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 8, 1, 8),
    _AdminRpaLogInBytes_Type()
)
adminRpaLogInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adminRpaLogInBytes.setStatus("mandatory")
_AdminRpaLogOutBytes_Type = Counter32
_AdminRpaLogOutBytes_Object = MibTableColumn
adminRpaLogOutBytes = _AdminRpaLogOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 8, 1, 9),
    _AdminRpaLogOutBytes_Type()
)
adminRpaLogOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adminRpaLogOutBytes.setStatus("mandatory")
_AdminRpaLogParityErrors_Type = Counter32
_AdminRpaLogParityErrors_Object = MibTableColumn
adminRpaLogParityErrors = _AdminRpaLogParityErrors_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 8, 1, 10),
    _AdminRpaLogParityErrors_Type()
)
adminRpaLogParityErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adminRpaLogParityErrors.setStatus("mandatory")
_AdminRpaLogFrameErrors_Type = Counter32
_AdminRpaLogFrameErrors_Object = MibTableColumn
adminRpaLogFrameErrors = _AdminRpaLogFrameErrors_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 8, 1, 11),
    _AdminRpaLogFrameErrors_Type()
)
adminRpaLogFrameErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adminRpaLogFrameErrors.setStatus("mandatory")
_AdminRpaLogOverrunErrors_Type = Counter32
_AdminRpaLogOverrunErrors_Object = MibTableColumn
adminRpaLogOverrunErrors = _AdminRpaLogOverrunErrors_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 8, 1, 12),
    _AdminRpaLogOverrunErrors_Type()
)
adminRpaLogOverrunErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adminRpaLogOverrunErrors.setStatus("mandatory")
_AdminRpaLogCksumErrors_Type = Counter32
_AdminRpaLogCksumErrors_Object = MibTableColumn
adminRpaLogCksumErrors = _AdminRpaLogCksumErrors_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 8, 1, 13),
    _AdminRpaLogCksumErrors_Type()
)
adminRpaLogCksumErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adminRpaLogCksumErrors.setStatus("mandatory")


class _AdminRpaLogDate_Type(DisplayString):
    """Custom type adminRpaLogDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_AdminRpaLogDate_Type.__name__ = "DisplayString"
_AdminRpaLogDate_Object = MibTableColumn
adminRpaLogDate = _AdminRpaLogDate_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 8, 1, 14),
    _AdminRpaLogDate_Type()
)
adminRpaLogDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adminRpaLogDate.setStatus("mandatory")


class _AdminRpaLogPortName_Type(DisplayString):
    """Custom type adminRpaLogPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_AdminRpaLogPortName_Type.__name__ = "DisplayString"
_AdminRpaLogPortName_Object = MibTableColumn
adminRpaLogPortName = _AdminRpaLogPortName_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 8, 1, 15),
    _AdminRpaLogPortName_Type()
)
adminRpaLogPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adminRpaLogPortName.setStatus("mandatory")


class _AdminRpaLogPathName_Type(DisplayString):
    """Custom type adminRpaLogPathName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_AdminRpaLogPathName_Type.__name__ = "DisplayString"
_AdminRpaLogPathName_Object = MibTableColumn
adminRpaLogPathName = _AdminRpaLogPathName_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 8, 1, 16),
    _AdminRpaLogPathName_Type()
)
adminRpaLogPathName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adminRpaLogPathName.setStatus("mandatory")
_AdminMisc_ObjectIdentity = ObjectIdentity
adminMisc = _AdminMisc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 9)
)


class _AdminSysDescr_Type(DisplayString):
    """Custom type adminSysDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AdminSysDescr_Type.__name__ = "DisplayString"
_AdminSysDescr_Object = MibScalar
adminSysDescr = _AdminSysDescr_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 9, 1),
    _AdminSysDescr_Type()
)
adminSysDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adminSysDescr.setStatus("mandatory")


class _AdminNodeName_Type(DisplayString):
    """Custom type adminNodeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_AdminNodeName_Type.__name__ = "DisplayString"
_AdminNodeName_Object = MibScalar
adminNodeName = _AdminNodeName_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 9, 2),
    _AdminNodeName_Type()
)
adminNodeName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminNodeName.setStatus("mandatory")


class _AdminNodePassword_Type(OctetString):
    """Custom type adminNodePassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_AdminNodePassword_Type.__name__ = "OctetString"
_AdminNodePassword_Object = MibScalar
adminNodePassword = _AdminNodePassword_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 9, 3),
    _AdminNodePassword_Type()
)
adminNodePassword.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adminNodePassword.setStatus("mandatory")


class _AdminDate_Type(DisplayString):
    """Custom type adminDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_AdminDate_Type.__name__ = "DisplayString"
_AdminDate_Object = MibScalar
adminDate = _AdminDate_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 9, 4),
    _AdminDate_Type()
)
adminDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminDate.setStatus("mandatory")


class _AdminTime_Type(DisplayString):
    """Custom type adminTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_AdminTime_Type.__name__ = "DisplayString"
_AdminTime_Object = MibScalar
adminTime = _AdminTime_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 9, 5),
    _AdminTime_Type()
)
adminTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminTime.setStatus("mandatory")


class _AdminGreeting_Type(DisplayString):
    """Custom type adminGreeting based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_AdminGreeting_Type.__name__ = "DisplayString"
_AdminGreeting_Object = MibScalar
adminGreeting = _AdminGreeting_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 9, 6),
    _AdminGreeting_Type()
)
adminGreeting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminGreeting.setStatus("mandatory")


class _AdminPrompt_Type(DisplayString):
    """Custom type adminPrompt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_AdminPrompt_Type.__name__ = "DisplayString"
_AdminPrompt_Object = MibScalar
adminPrompt = _AdminPrompt_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 9, 7),
    _AdminPrompt_Type()
)
adminPrompt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminPrompt.setStatus("mandatory")


class _AdminSNMPGetFrom_Type(Integer32):
    """Custom type adminSNMPGetFrom based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("config-value", 2),
          ("current-value", 1))
    )


_AdminSNMPGetFrom_Type.__name__ = "Integer32"
_AdminSNMPGetFrom_Object = MibScalar
adminSNMPGetFrom = _AdminSNMPGetFrom_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 9, 8),
    _AdminSNMPGetFrom_Type()
)
adminSNMPGetFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminSNMPGetFrom.setStatus("mandatory")


class _AdminDoIntegrity_Type(Integer32):
    """Custom type adminDoIntegrity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("integrity-check-OK", 1),
          ("integrity-check-failed", 2))
    )


_AdminDoIntegrity_Type.__name__ = "Integer32"
_AdminDoIntegrity_Object = MibScalar
adminDoIntegrity = _AdminDoIntegrity_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 9, 9),
    _AdminDoIntegrity_Type()
)
adminDoIntegrity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminDoIntegrity.setStatus("mandatory")


class _AdminDoFileload_Type(Integer32):
    """Custom type adminDoFileload based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fileload-OK", 1),
          ("fileload-failed", 2))
    )


_AdminDoFileload_Type.__name__ = "Integer32"
_AdminDoFileload_Object = MibScalar
adminDoFileload = _AdminDoFileload_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 9, 10),
    _AdminDoFileload_Type()
)
adminDoFileload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminDoFileload.setStatus("mandatory")


class _AdminLoadfileName_Type(DisplayString):
    """Custom type adminLoadfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_AdminLoadfileName_Type.__name__ = "DisplayString"
_AdminLoadfileName_Object = MibScalar
adminLoadfileName = _AdminLoadfileName_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 9, 11),
    _AdminLoadfileName_Type()
)
adminLoadfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminLoadfileName.setStatus("mandatory")


class _AdminLastTrap_Type(DisplayString):
    """Custom type adminLastTrap based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AdminLastTrap_Type.__name__ = "DisplayString"
_AdminLastTrap_Object = MibScalar
adminLastTrap = _AdminLastTrap_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 9, 13),
    _AdminLastTrap_Type()
)
adminLastTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adminLastTrap.setStatus("mandatory")
_AdminResetAllUserCounters_Type = Integer32
_AdminResetAllUserCounters_Object = MibScalar
adminResetAllUserCounters = _AdminResetAllUserCounters_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 9, 14),
    _AdminResetAllUserCounters_Type()
)
adminResetAllUserCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminResetAllUserCounters.setStatus("mandatory")
_AdminEraseConfig_Type = Integer32
_AdminEraseConfig_Object = MibScalar
adminEraseConfig = _AdminEraseConfig_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 9, 15),
    _AdminEraseConfig_Type()
)
adminEraseConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminEraseConfig.setStatus("mandatory")


class _AdminUIMsgLevel_Type(Integer32):
    """Custom type adminUIMsgLevel based on Integer32"""
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
        *(("error-level", 2),
          ("panic-level", 1),
          ("status-level", 4),
          ("warning-level", 3))
    )


_AdminUIMsgLevel_Type.__name__ = "Integer32"
_AdminUIMsgLevel_Object = MibScalar
adminUIMsgLevel = _AdminUIMsgLevel_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 9, 16),
    _AdminUIMsgLevel_Type()
)
adminUIMsgLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminUIMsgLevel.setStatus("mandatory")


class _AdminSNMPMsgLevel_Type(Integer32):
    """Custom type adminSNMPMsgLevel based on Integer32"""
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
        *(("error-level", 2),
          ("none", 1),
          ("status-level", 4),
          ("warning-level", 3))
    )


_AdminSNMPMsgLevel_Type.__name__ = "Integer32"
_AdminSNMPMsgLevel_Object = MibScalar
adminSNMPMsgLevel = _AdminSNMPMsgLevel_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 9, 17),
    _AdminSNMPMsgLevel_Type()
)
adminSNMPMsgLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminSNMPMsgLevel.setStatus("mandatory")


class _AdminLoginOption_Type(Integer32):
    """Custom type adminLoginOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nologin", 2),
          ("nopassword", 3),
          ("normal", 1))
    )


_AdminLoginOption_Type.__name__ = "Integer32"
_AdminLoginOption_Object = MibScalar
adminLoginOption = _AdminLoginOption_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 9, 18),
    _AdminLoginOption_Type()
)
adminLoginOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminLoginOption.setStatus("mandatory")
_AdminReboot_Type = Integer32
_AdminReboot_Object = MibScalar
adminReboot = _AdminReboot_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 9, 19),
    _AdminReboot_Type()
)
adminReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminReboot.setStatus("mandatory")
_AdminMajorVersion_Type = Integer32
_AdminMajorVersion_Object = MibScalar
adminMajorVersion = _AdminMajorVersion_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 9, 20),
    _AdminMajorVersion_Type()
)
adminMajorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adminMajorVersion.setStatus("mandatory")
_AdminMinorVersion_Type = Integer32
_AdminMinorVersion_Object = MibScalar
adminMinorVersion = _AdminMinorVersion_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 9, 21),
    _AdminMinorVersion_Type()
)
adminMinorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adminMinorVersion.setStatus("mandatory")
_AdminMIBVersion_Type = Integer32
_AdminMIBVersion_Object = MibScalar
adminMIBVersion = _AdminMIBVersion_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 9, 22),
    _AdminMIBVersion_Type()
)
adminMIBVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adminMIBVersion.setStatus("mandatory")


class _AdminTimeZone_Type(DisplayString):
    """Custom type adminTimeZone based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4),
    )


_AdminTimeZone_Type.__name__ = "DisplayString"
_AdminTimeZone_Object = MibScalar
adminTimeZone = _AdminTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 9, 23),
    _AdminTimeZone_Type()
)
adminTimeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminTimeZone.setStatus("mandatory")


class _AdminSecurityServerType_Type(Integer32):
    """Custom type adminSecurityServerType based on Integer32"""
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
        *(("ab-nameserver", 2),
          ("ace-server", 4),
          ("dce-server", 3),
          ("generic", 7),
          ("internal", 1),
          ("nt", 8),
          ("nw-bindery", 5),
          ("nw-nds", 6))
    )


_AdminSecurityServerType_Type.__name__ = "Integer32"
_AdminSecurityServerType_Object = MibScalar
adminSecurityServerType = _AdminSecurityServerType_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 9, 24),
    _AdminSecurityServerType_Type()
)
adminSecurityServerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adminSecurityServerType.setStatus("mandatory")


class _AdminSecPassword_Type(OctetString):
    """Custom type adminSecPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_AdminSecPassword_Type.__name__ = "OctetString"
_AdminSecPassword_Object = MibScalar
adminSecPassword = _AdminSecPassword_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 9, 25),
    _AdminSecPassword_Type()
)
adminSecPassword.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adminSecPassword.setStatus("mandatory")
_AdminScrtyClntIpAddr_Type = IpAddress
_AdminScrtyClntIpAddr_Object = MibScalar
adminScrtyClntIpAddr = _AdminScrtyClntIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 9, 26),
    _AdminScrtyClntIpAddr_Type()
)
adminScrtyClntIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adminScrtyClntIpAddr.setStatus("mandatory")
_AdminSecondScrtyClntIpAddr_Type = IpAddress
_AdminSecondScrtyClntIpAddr_Object = MibScalar
adminSecondScrtyClntIpAddr = _AdminSecondScrtyClntIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 9, 27),
    _AdminSecondScrtyClntIpAddr_Type()
)
adminSecondScrtyClntIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adminSecondScrtyClntIpAddr.setStatus("mandatory")
_AdminUdpPort_Type = Integer32
_AdminUdpPort_Object = MibScalar
adminUdpPort = _AdminUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 9, 28),
    _AdminUdpPort_Type()
)
adminUdpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adminUdpPort.setStatus("mandatory")
_AdminTelnetAdminPort_Type = Integer32
_AdminTelnetAdminPort_Object = MibScalar
adminTelnetAdminPort = _AdminTelnetAdminPort_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 9, 29),
    _AdminTelnetAdminPort_Type()
)
adminTelnetAdminPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminTelnetAdminPort.setStatus("mandatory")


class _AdminTelnetDialOutAuth_Type(Integer32):
    """Custom type adminTelnetDialOutAuth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_AdminTelnetDialOutAuth_Type.__name__ = "Integer32"
_AdminTelnetDialOutAuth_Object = MibScalar
adminTelnetDialOutAuth = _AdminTelnetDialOutAuth_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 9, 30),
    _AdminTelnetDialOutAuth_Type()
)
adminTelnetDialOutAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminTelnetDialOutAuth.setStatus("mandatory")


class _AdminDialOutEnabled_Type(Integer32):
    """Custom type adminDialOutEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_AdminDialOutEnabled_Type.__name__ = "Integer32"
_AdminDialOutEnabled_Object = MibScalar
adminDialOutEnabled = _AdminDialOutEnabled_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 9, 31),
    _AdminDialOutEnabled_Type()
)
adminDialOutEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminDialOutEnabled.setStatus("mandatory")


class _AdminEncryptNodePassword_Type(OctetString):
    """Custom type adminEncryptNodePassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_AdminEncryptNodePassword_Type.__name__ = "OctetString"
_AdminEncryptNodePassword_Object = MibScalar
adminEncryptNodePassword = _AdminEncryptNodePassword_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 9, 32),
    _AdminEncryptNodePassword_Type()
)
adminEncryptNodePassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminEncryptNodePassword.setStatus("mandatory")


class _AdminEncryptSecurityServerType_Type(OctetString):
    """Custom type adminEncryptSecurityServerType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_AdminEncryptSecurityServerType_Type.__name__ = "OctetString"
_AdminEncryptSecurityServerType_Object = MibScalar
adminEncryptSecurityServerType = _AdminEncryptSecurityServerType_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 9, 33),
    _AdminEncryptSecurityServerType_Type()
)
adminEncryptSecurityServerType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminEncryptSecurityServerType.setStatus("mandatory")


class _AdminEncryptSecPassword_Type(OctetString):
    """Custom type adminEncryptSecPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_AdminEncryptSecPassword_Type.__name__ = "OctetString"
_AdminEncryptSecPassword_Object = MibScalar
adminEncryptSecPassword = _AdminEncryptSecPassword_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 9, 34),
    _AdminEncryptSecPassword_Type()
)
adminEncryptSecPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminEncryptSecPassword.setStatus("mandatory")


class _AdminEncryptScrtyClntIpAddr_Type(OctetString):
    """Custom type adminEncryptScrtyClntIpAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_AdminEncryptScrtyClntIpAddr_Type.__name__ = "OctetString"
_AdminEncryptScrtyClntIpAddr_Object = MibScalar
adminEncryptScrtyClntIpAddr = _AdminEncryptScrtyClntIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 9, 35),
    _AdminEncryptScrtyClntIpAddr_Type()
)
adminEncryptScrtyClntIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminEncryptScrtyClntIpAddr.setStatus("mandatory")


class _AdminEncryptSecondScrtyClntIpAddr_Type(OctetString):
    """Custom type adminEncryptSecondScrtyClntIpAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_AdminEncryptSecondScrtyClntIpAddr_Type.__name__ = "OctetString"
_AdminEncryptSecondScrtyClntIpAddr_Object = MibScalar
adminEncryptSecondScrtyClntIpAddr = _AdminEncryptSecondScrtyClntIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 9, 36),
    _AdminEncryptSecondScrtyClntIpAddr_Type()
)
adminEncryptSecondScrtyClntIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminEncryptSecondScrtyClntIpAddr.setStatus("mandatory")


class _AdminEncryptUdpPort_Type(OctetString):
    """Custom type adminEncryptUdpPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_AdminEncryptUdpPort_Type.__name__ = "OctetString"
_AdminEncryptUdpPort_Object = MibScalar
adminEncryptUdpPort = _AdminEncryptUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 9, 37),
    _AdminEncryptUdpPort_Type()
)
adminEncryptUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminEncryptUdpPort.setStatus("mandatory")
_AdminEPromSize_Type = Integer32
_AdminEPromSize_Object = MibScalar
adminEPromSize = _AdminEPromSize_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 9, 38),
    _AdminEPromSize_Type()
)
adminEPromSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adminEPromSize.setStatus("mandatory")
_AdminNVRamSize_Type = Integer32
_AdminNVRamSize_Object = MibScalar
adminNVRamSize = _AdminNVRamSize_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 9, 39),
    _AdminNVRamSize_Type()
)
adminNVRamSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adminNVRamSize.setStatus("mandatory")
_AdminFlashRomSize_Type = Integer32
_AdminFlashRomSize_Object = MibScalar
adminFlashRomSize = _AdminFlashRomSize_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 9, 40),
    _AdminFlashRomSize_Type()
)
adminFlashRomSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adminFlashRomSize.setStatus("mandatory")
_AdminLocalDRamSize_Type = Integer32
_AdminLocalDRamSize_Object = MibScalar
adminLocalDRamSize = _AdminLocalDRamSize_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 9, 41),
    _AdminLocalDRamSize_Type()
)
adminLocalDRamSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adminLocalDRamSize.setStatus("mandatory")
_AdminSharedDRamSize_Type = Integer32
_AdminSharedDRamSize_Object = MibScalar
adminSharedDRamSize = _AdminSharedDRamSize_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 9, 42),
    _AdminSharedDRamSize_Type()
)
adminSharedDRamSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adminSharedDRamSize.setStatus("mandatory")
_AdminHWRev_Type = Integer32
_AdminHWRev_Object = MibScalar
adminHWRev = _AdminHWRev_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 9, 43),
    _AdminHWRev_Type()
)
adminHWRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adminHWRev.setStatus("mandatory")


class _AdminEncryptSuperUserPassword_Type(OctetString):
    """Custom type adminEncryptSuperUserPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_AdminEncryptSuperUserPassword_Type.__name__ = "OctetString"
_AdminEncryptSuperUserPassword_Object = MibScalar
adminEncryptSuperUserPassword = _AdminEncryptSuperUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 9, 44),
    _AdminEncryptSuperUserPassword_Type()
)
adminEncryptSuperUserPassword.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adminEncryptSuperUserPassword.setStatus("mandatory")


class _AdminNewGreeting_Type(DisplayString):
    """Custom type adminNewGreeting based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AdminNewGreeting_Type.__name__ = "DisplayString"
_AdminNewGreeting_Object = MibScalar
adminNewGreeting = _AdminNewGreeting_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 9, 45),
    _AdminNewGreeting_Type()
)
adminNewGreeting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminNewGreeting.setStatus("mandatory")
_AdminTFTPServerIpAddr_Type = IpAddress
_AdminTFTPServerIpAddr_Object = MibScalar
adminTFTPServerIpAddr = _AdminTFTPServerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 9, 46),
    _AdminTFTPServerIpAddr_Type()
)
adminTFTPServerIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminTFTPServerIpAddr.setStatus("mandatory")


class _AdminSaveConfig_Type(Integer32):
    """Custom type adminSaveConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("save-OK", 1),
          ("save-failed", 2))
    )


_AdminSaveConfig_Type.__name__ = "Integer32"
_AdminSaveConfig_Object = MibScalar
adminSaveConfig = _AdminSaveConfig_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 9, 47),
    _AdminSaveConfig_Type()
)
adminSaveConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminSaveConfig.setStatus("mandatory")
_AdminMaintenanceVersion_Type = Integer32
_AdminMaintenanceVersion_Object = MibScalar
adminMaintenanceVersion = _AdminMaintenanceVersion_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 9, 48),
    _AdminMaintenanceVersion_Type()
)
adminMaintenanceVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adminMaintenanceVersion.setStatus("mandatory")
_AdminCheckConsoleModem_Type = Integer32
_AdminCheckConsoleModem_Object = MibScalar
adminCheckConsoleModem = _AdminCheckConsoleModem_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 9, 49),
    _AdminCheckConsoleModem_Type()
)
adminCheckConsoleModem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminCheckConsoleModem.setStatus("mandatory")
_AdminConsoleImageDownload_Type = Integer32
_AdminConsoleImageDownload_Object = MibScalar
adminConsoleImageDownload = _AdminConsoleImageDownload_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 9, 50),
    _AdminConsoleImageDownload_Type()
)
adminConsoleImageDownload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminConsoleImageDownload.setStatus("mandatory")
_AdminConsoleConfigUpload_Type = Integer32
_AdminConsoleConfigUpload_Object = MibScalar
adminConsoleConfigUpload = _AdminConsoleConfigUpload_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 9, 51),
    _AdminConsoleConfigUpload_Type()
)
adminConsoleConfigUpload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminConsoleConfigUpload.setStatus("mandatory")
_AdminConsoleConfigDownload_Type = Integer32
_AdminConsoleConfigDownload_Object = MibScalar
adminConsoleConfigDownload = _AdminConsoleConfigDownload_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 9, 52),
    _AdminConsoleConfigDownload_Type()
)
adminConsoleConfigDownload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminConsoleConfigDownload.setStatus("mandatory")
_AdminRasIdleTime_Type = Integer32
_AdminRasIdleTime_Object = MibScalar
adminRasIdleTime = _AdminRasIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 9, 53),
    _AdminRasIdleTime_Type()
)
adminRasIdleTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminRasIdleTime.setStatus("mandatory")
_AdminRouterIdleTime_Type = Integer32
_AdminRouterIdleTime_Object = MibScalar
adminRouterIdleTime = _AdminRouterIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 9, 54),
    _AdminRouterIdleTime_Type()
)
adminRouterIdleTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminRouterIdleTime.setStatus("mandatory")
_AdminRasSpoofTime_Type = Integer32
_AdminRasSpoofTime_Object = MibScalar
adminRasSpoofTime = _AdminRasSpoofTime_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 9, 55),
    _AdminRasSpoofTime_Type()
)
adminRasSpoofTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminRasSpoofTime.setStatus("mandatory")
_AdminRouterSpoofTime_Type = Integer32
_AdminRouterSpoofTime_Object = MibScalar
adminRouterSpoofTime = _AdminRouterSpoofTime_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 9, 56),
    _AdminRouterSpoofTime_Type()
)
adminRouterSpoofTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminRouterSpoofTime.setStatus("mandatory")
_AdminLnkUtilHighThld_Type = Integer32
_AdminLnkUtilHighThld_Object = MibScalar
adminLnkUtilHighThld = _AdminLnkUtilHighThld_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 9, 57),
    _AdminLnkUtilHighThld_Type()
)
adminLnkUtilHighThld.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminLnkUtilHighThld.setStatus("mandatory")
_AdminLnkUtilLowThld_Type = Integer32
_AdminLnkUtilLowThld_Object = MibScalar
adminLnkUtilLowThld = _AdminLnkUtilLowThld_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 9, 58),
    _AdminLnkUtilLowThld_Type()
)
adminLnkUtilLowThld.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminLnkUtilLowThld.setStatus("mandatory")


class _AdminCallerIdCheck_Type(Integer32):
    """Custom type adminCallerIdCheck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_AdminCallerIdCheck_Type.__name__ = "Integer32"
_AdminCallerIdCheck_Object = MibScalar
adminCallerIdCheck = _AdminCallerIdCheck_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 9, 59),
    _AdminCallerIdCheck_Type()
)
adminCallerIdCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminCallerIdCheck.setStatus("mandatory")


class _AdminISDNRequiredBaudrate_Type(Integer32):
    """Custom type adminISDNRequiredBaudrate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 3),
          ("br-56000", 1),
          ("br-64000", 2))
    )


_AdminISDNRequiredBaudrate_Type.__name__ = "Integer32"
_AdminISDNRequiredBaudrate_Object = MibScalar
adminISDNRequiredBaudrate = _AdminISDNRequiredBaudrate_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 9, 60),
    _AdminISDNRequiredBaudrate_Type()
)
adminISDNRequiredBaudrate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminISDNRequiredBaudrate.setStatus("mandatory")


class _AdminRouterCCPEnabled_Type(Integer32):
    """Custom type adminRouterCCPEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_AdminRouterCCPEnabled_Type.__name__ = "Integer32"
_AdminRouterCCPEnabled_Object = MibScalar
adminRouterCCPEnabled = _AdminRouterCCPEnabled_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 9, 61),
    _AdminRouterCCPEnabled_Type()
)
adminRouterCCPEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminRouterCCPEnabled.setStatus("mandatory")


class _AdminSuggestFlag_Type(Integer32):
    """Custom type adminSuggestFlag based on Integer32"""
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


_AdminSuggestFlag_Type.__name__ = "Integer32"
_AdminSuggestFlag_Object = MibScalar
adminSuggestFlag = _AdminSuggestFlag_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 9, 62),
    _AdminSuggestFlag_Type()
)
adminSuggestFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminSuggestFlag.setStatus("mandatory")


class _AdminEEVersionNo_Type(OctetString):
    """Custom type adminEEVersionNo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_AdminEEVersionNo_Type.__name__ = "OctetString"
_AdminEEVersionNo_Object = MibScalar
adminEEVersionNo = _AdminEEVersionNo_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 9, 63),
    _AdminEEVersionNo_Type()
)
adminEEVersionNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adminEEVersionNo.setStatus("mandatory")
_AdminMdSetupNumber_Type = Integer32
_AdminMdSetupNumber_Object = MibScalar
adminMdSetupNumber = _AdminMdSetupNumber_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 10),
    _AdminMdSetupNumber_Type()
)
adminMdSetupNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adminMdSetupNumber.setStatus("mandatory")
_AdminMdSetupTable_Object = MibTable
adminMdSetupTable = _AdminMdSetupTable_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 11)
)
if mibBuilder.loadTexts:
    adminMdSetupTable.setStatus("mandatory")
_AdminMdSetupEntry_Object = MibTableRow
adminMdSetupEntry = _AdminMdSetupEntry_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 11, 1)
)
adminMdSetupEntry.setIndexNames(
    (0, "Centrum-MIB", "adminMdSetupIndex"),
)
if mibBuilder.loadTexts:
    adminMdSetupEntry.setStatus("mandatory")
_AdminMdSetupIndex_Type = Integer32
_AdminMdSetupIndex_Object = MibTableColumn
adminMdSetupIndex = _AdminMdSetupIndex_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 11, 1, 1),
    _AdminMdSetupIndex_Type()
)
adminMdSetupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adminMdSetupIndex.setStatus("mandatory")


class _AdminMdSetupType_Type(Integer32):
    """Custom type adminMdSetupType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("built-in", 2),
          ("invalid", 1),
          ("user-defined", 3))
    )


_AdminMdSetupType_Type.__name__ = "Integer32"
_AdminMdSetupType_Object = MibTableColumn
adminMdSetupType = _AdminMdSetupType_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 11, 1, 2),
    _AdminMdSetupType_Type()
)
adminMdSetupType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminMdSetupType.setStatus("mandatory")


class _AdminMdSetupName_Type(DisplayString):
    """Custom type adminMdSetupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_AdminMdSetupName_Type.__name__ = "DisplayString"
_AdminMdSetupName_Object = MibTableColumn
adminMdSetupName = _AdminMdSetupName_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 11, 1, 3),
    _AdminMdSetupName_Type()
)
adminMdSetupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminMdSetupName.setStatus("mandatory")


class _AdminMdSetupATCmd_Type(DisplayString):
    """Custom type adminMdSetupATCmd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 79),
    )


_AdminMdSetupATCmd_Type.__name__ = "DisplayString"
_AdminMdSetupATCmd_Object = MibTableColumn
adminMdSetupATCmd = _AdminMdSetupATCmd_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 11, 1, 4),
    _AdminMdSetupATCmd_Type()
)
adminMdSetupATCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminMdSetupATCmd.setStatus("mandatory")


class _AdminMdSetupARAP1_0ATCmd_Type(DisplayString):
    """Custom type adminMdSetupARAP1_0ATCmd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 79),
    )


_AdminMdSetupARAP1_0ATCmd_Type.__name__ = "DisplayString"
_AdminMdSetupARAP1_0ATCmd_Object = MibScalar
adminMdSetupARAP1_0ATCmd = _AdminMdSetupARAP1_0ATCmd_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 11, 1, 5),
    _AdminMdSetupARAP1_0ATCmd_Type()
)
adminMdSetupARAP1_0ATCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminMdSetupARAP1_0ATCmd.setStatus("mandatory")


class _AdminMdSetupIncomingCall_Type(Integer32):
    """Custom type adminMdSetupIncomingCall based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ri", 1),
          ("ring", 2))
    )


_AdminMdSetupIncomingCall_Type.__name__ = "Integer32"
_AdminMdSetupIncomingCall_Object = MibTableColumn
adminMdSetupIncomingCall = _AdminMdSetupIncomingCall_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 11, 1, 6),
    _AdminMdSetupIncomingCall_Type()
)
adminMdSetupIncomingCall.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminMdSetupIncomingCall.setStatus("mandatory")


class _AdminMdSetupConnIndication_Type(Integer32):
    """Custom type adminMdSetupConnIndication based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("connect", 1),
          ("dcd", 2))
    )


_AdminMdSetupConnIndication_Type.__name__ = "Integer32"
_AdminMdSetupConnIndication_Object = MibTableColumn
adminMdSetupConnIndication = _AdminMdSetupConnIndication_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 11, 1, 7),
    _AdminMdSetupConnIndication_Type()
)
adminMdSetupConnIndication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminMdSetupConnIndication.setStatus("mandatory")
_AdminMdSetupCallTimeOut_Type = Integer32
_AdminMdSetupCallTimeOut_Object = MibTableColumn
adminMdSetupCallTimeOut = _AdminMdSetupCallTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 11, 1, 8),
    _AdminMdSetupCallTimeOut_Type()
)
adminMdSetupCallTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminMdSetupCallTimeOut.setStatus("mandatory")
_AdminMdSetupCallDelay_Type = Integer32
_AdminMdSetupCallDelay_Object = MibTableColumn
adminMdSetupCallDelay = _AdminMdSetupCallDelay_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 11, 1, 9),
    _AdminMdSetupCallDelay_Type()
)
adminMdSetupCallDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminMdSetupCallDelay.setStatus("mandatory")
_AdminCallerIDNumber_Type = Integer32
_AdminCallerIDNumber_Object = MibScalar
adminCallerIDNumber = _AdminCallerIDNumber_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 12),
    _AdminCallerIDNumber_Type()
)
adminCallerIDNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adminCallerIDNumber.setStatus("mandatory")
_AdminCallerIDTable_Object = MibTable
adminCallerIDTable = _AdminCallerIDTable_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 13)
)
if mibBuilder.loadTexts:
    adminCallerIDTable.setStatus("mandatory")
_AdminCallerIDEntry_Object = MibTableRow
adminCallerIDEntry = _AdminCallerIDEntry_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 13, 1)
)
adminCallerIDEntry.setIndexNames(
    (0, "Centrum-MIB", "adminCallerIDIndex"),
)
if mibBuilder.loadTexts:
    adminCallerIDEntry.setStatus("mandatory")
_AdminCallerIDIndex_Type = Integer32
_AdminCallerIDIndex_Object = MibTableColumn
adminCallerIDIndex = _AdminCallerIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 13, 1, 1),
    _AdminCallerIDIndex_Type()
)
adminCallerIDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adminCallerIDIndex.setStatus("mandatory")


class _AdminCallerIDName_Type(DisplayString):
    """Custom type adminCallerIDName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_AdminCallerIDName_Type.__name__ = "DisplayString"
_AdminCallerIDName_Object = MibTableColumn
adminCallerIDName = _AdminCallerIDName_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 13, 1, 2),
    _AdminCallerIDName_Type()
)
adminCallerIDName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminCallerIDName.setStatus("mandatory")


class _AdminCallerIDType_Type(Integer32):
    """Custom type adminCallerIDType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_AdminCallerIDType_Type.__name__ = "Integer32"
_AdminCallerIDType_Object = MibTableColumn
adminCallerIDType = _AdminCallerIDType_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 13, 1, 3),
    _AdminCallerIDType_Type()
)
adminCallerIDType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminCallerIDType.setStatus("mandatory")


class _AdminCallerIDComment_Type(DisplayString):
    """Custom type adminCallerIDComment based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_AdminCallerIDComment_Type.__name__ = "DisplayString"
_AdminCallerIDComment_Object = MibTableColumn
adminCallerIDComment = _AdminCallerIDComment_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 6, 13, 1, 4),
    _AdminCallerIDComment_Type()
)
adminCallerIDComment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminCallerIDComment.setStatus("mandatory")
_Crat_ObjectIdentity = ObjectIdentity
crat = _Crat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 7)
)
_AtRpa_ObjectIdentity = ObjectIdentity
atRpa = _AtRpa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 7, 1)
)
_AtRpaNumber_Type = Integer32
_AtRpaNumber_Object = MibScalar
atRpaNumber = _AtRpaNumber_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 7, 1, 1),
    _AtRpaNumber_Type()
)
atRpaNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atRpaNumber.setStatus("mandatory")
_AtRpaTable_Object = MibTable
atRpaTable = _AtRpaTable_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 7, 1, 2)
)
if mibBuilder.loadTexts:
    atRpaTable.setStatus("mandatory")
_AtRpaEntry_Object = MibTableRow
atRpaEntry = _AtRpaEntry_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 7, 1, 2, 1)
)
atRpaEntry.setIndexNames(
    (0, "Centrum-MIB", "atRpaIndex"),
)
if mibBuilder.loadTexts:
    atRpaEntry.setStatus("mandatory")
_AtRpaIndex_Type = Integer32
_AtRpaIndex_Object = MibTableColumn
atRpaIndex = _AtRpaIndex_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 7, 1, 2, 1, 1),
    _AtRpaIndex_Type()
)
atRpaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atRpaIndex.setStatus("mandatory")


class _AtRpaNetworkAddress_Type(OctetString):
    """Custom type atRpaNetworkAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_AtRpaNetworkAddress_Type.__name__ = "OctetString"
_AtRpaNetworkAddress_Object = MibTableColumn
atRpaNetworkAddress = _AtRpaNetworkAddress_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 7, 1, 2, 1, 2),
    _AtRpaNetworkAddress_Type()
)
atRpaNetworkAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atRpaNetworkAddress.setStatus("mandatory")
_AtRpaState_Type = Integer32
_AtRpaState_Object = MibTableColumn
atRpaState = _AtRpaState_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 7, 1, 2, 1, 3),
    _AtRpaState_Type()
)
atRpaState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atRpaState.setStatus("mandatory")


class _AtRpaDialInZone_Type(OctetString):
    """Custom type atRpaDialInZone based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AtRpaDialInZone_Type.__name__ = "OctetString"
_AtRpaDialInZone_Object = MibScalar
atRpaDialInZone = _AtRpaDialInZone_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 7, 1, 3),
    _AtRpaDialInZone_Type()
)
atRpaDialInZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atRpaDialInZone.setStatus("mandatory")
_AtRpaMaxConnTime_Type = Integer32
_AtRpaMaxConnTime_Object = MibScalar
atRpaMaxConnTime = _AtRpaMaxConnTime_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 7, 1, 4),
    _AtRpaMaxConnTime_Type()
)
atRpaMaxConnTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atRpaMaxConnTime.setStatus("mandatory")


class _AtRpaNoNbpMulticast_Type(Integer32):
    """Custom type atRpaNoNbpMulticast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_AtRpaNoNbpMulticast_Type.__name__ = "Integer32"
_AtRpaNoNbpMulticast_Object = MibScalar
atRpaNoNbpMulticast = _AtRpaNoNbpMulticast_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 7, 1, 5),
    _AtRpaNoNbpMulticast_Type()
)
atRpaNoNbpMulticast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atRpaNoNbpMulticast.setStatus("mandatory")
_AtRt_ObjectIdentity = ObjectIdentity
atRt = _AtRt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 7, 2)
)
_AtPLocalNumber_Type = Integer32
_AtPLocalNumber_Object = MibScalar
atPLocalNumber = _AtPLocalNumber_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 7, 2, 1),
    _AtPLocalNumber_Type()
)
atPLocalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atPLocalNumber.setStatus("mandatory")
_AtPLocalTable_Object = MibTable
atPLocalTable = _AtPLocalTable_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 7, 2, 2)
)
if mibBuilder.loadTexts:
    atPLocalTable.setStatus("mandatory")
_AtPLocalEntry_Object = MibTableRow
atPLocalEntry = _AtPLocalEntry_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 7, 2, 2, 1)
)
atPLocalEntry.setIndexNames(
    (0, "Centrum-MIB", "atPLocalIndex"),
)
if mibBuilder.loadTexts:
    atPLocalEntry.setStatus("mandatory")
_AtPLocalIndex_Type = Integer32
_AtPLocalIndex_Object = MibTableColumn
atPLocalIndex = _AtPLocalIndex_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 7, 2, 2, 1, 1),
    _AtPLocalIndex_Type()
)
atPLocalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atPLocalIndex.setStatus("mandatory")


class _AtPLocalNetAddress_Type(OctetString):
    """Custom type atPLocalNetAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_AtPLocalNetAddress_Type.__name__ = "OctetString"
_AtPLocalNetAddress_Object = MibTableColumn
atPLocalNetAddress = _AtPLocalNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 7, 2, 2, 1, 2),
    _AtPLocalNetAddress_Type()
)
atPLocalNetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atPLocalNetAddress.setStatus("mandatory")
_AtPLocalNetStart_Type = Integer32
_AtPLocalNetStart_Object = MibTableColumn
atPLocalNetStart = _AtPLocalNetStart_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 7, 2, 2, 1, 3),
    _AtPLocalNetStart_Type()
)
atPLocalNetStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atPLocalNetStart.setStatus("mandatory")
_AtPLocalNetEnd_Type = Integer32
_AtPLocalNetEnd_Object = MibTableColumn
atPLocalNetEnd = _AtPLocalNetEnd_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 7, 2, 2, 1, 4),
    _AtPLocalNetEnd_Type()
)
atPLocalNetEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atPLocalNetEnd.setStatus("mandatory")


class _AtPLocalDefaultRouter_Type(OctetString):
    """Custom type atPLocalDefaultRouter based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_AtPLocalDefaultRouter_Type.__name__ = "OctetString"
_AtPLocalDefaultRouter_Object = MibTableColumn
atPLocalDefaultRouter = _AtPLocalDefaultRouter_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 7, 2, 2, 1, 5),
    _AtPLocalDefaultRouter_Type()
)
atPLocalDefaultRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atPLocalDefaultRouter.setStatus("mandatory")


class _AtPLocalLocalZone_Type(OctetString):
    """Custom type atPLocalLocalZone based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AtPLocalLocalZone_Type.__name__ = "OctetString"
_AtPLocalLocalZone_Object = MibTableColumn
atPLocalLocalZone = _AtPLocalLocalZone_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 7, 2, 2, 1, 6),
    _AtPLocalLocalZone_Type()
)
atPLocalLocalZone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atPLocalLocalZone.setStatus("mandatory")
_AtAarpTable_Object = MibTable
atAarpTable = _AtAarpTable_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 7, 2, 3)
)
if mibBuilder.loadTexts:
    atAarpTable.setStatus("mandatory")
_AtAarpEntry_Object = MibTableRow
atAarpEntry = _AtAarpEntry_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 7, 2, 3, 1)
)
atAarpEntry.setIndexNames(
    (0, "Centrum-MIB", "atAarpIfIndex"),
    (0, "Centrum-MIB", "atAarpNetAddress"),
)
if mibBuilder.loadTexts:
    atAarpEntry.setStatus("mandatory")
_AtAarpIfIndex_Type = Integer32
_AtAarpIfIndex_Object = MibTableColumn
atAarpIfIndex = _AtAarpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 7, 2, 3, 1, 1),
    _AtAarpIfIndex_Type()
)
atAarpIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atAarpIfIndex.setStatus("mandatory")


class _AtAarpPhysAddress_Type(OctetString):
    """Custom type atAarpPhysAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_AtAarpPhysAddress_Type.__name__ = "OctetString"
_AtAarpPhysAddress_Object = MibTableColumn
atAarpPhysAddress = _AtAarpPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 7, 2, 3, 1, 2),
    _AtAarpPhysAddress_Type()
)
atAarpPhysAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atAarpPhysAddress.setStatus("mandatory")


class _AtAarpNetAddress_Type(OctetString):
    """Custom type atAarpNetAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_AtAarpNetAddress_Type.__name__ = "OctetString"
_AtAarpNetAddress_Object = MibTableColumn
atAarpNetAddress = _AtAarpNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 7, 2, 3, 1, 3),
    _AtAarpNetAddress_Type()
)
atAarpNetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atAarpNetAddress.setStatus("mandatory")
_AtBestRouterCacheTable_Object = MibTable
atBestRouterCacheTable = _AtBestRouterCacheTable_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 7, 2, 4)
)
if mibBuilder.loadTexts:
    atBestRouterCacheTable.setStatus("mandatory")
_AtBestRouterCacheEntry_Object = MibTableRow
atBestRouterCacheEntry = _AtBestRouterCacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 7, 2, 4, 1)
)
atBestRouterCacheEntry.setIndexNames(
    (0, "Centrum-MIB", "atBestRouterCacheIfIndex"),
    (0, "Centrum-MIB", "atBestRouterCacheNetAddress"),
)
if mibBuilder.loadTexts:
    atBestRouterCacheEntry.setStatus("mandatory")
_AtBestRouterCacheIfIndex_Type = Integer32
_AtBestRouterCacheIfIndex_Object = MibTableColumn
atBestRouterCacheIfIndex = _AtBestRouterCacheIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 7, 2, 4, 1, 1),
    _AtBestRouterCacheIfIndex_Type()
)
atBestRouterCacheIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atBestRouterCacheIfIndex.setStatus("mandatory")


class _AtBestRouterCachePhysAddress_Type(OctetString):
    """Custom type atBestRouterCachePhysAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_AtBestRouterCachePhysAddress_Type.__name__ = "OctetString"
_AtBestRouterCachePhysAddress_Object = MibTableColumn
atBestRouterCachePhysAddress = _AtBestRouterCachePhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 7, 2, 4, 1, 2),
    _AtBestRouterCachePhysAddress_Type()
)
atBestRouterCachePhysAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atBestRouterCachePhysAddress.setStatus("mandatory")


class _AtBestRouterCacheNetAddress_Type(OctetString):
    """Custom type atBestRouterCacheNetAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_AtBestRouterCacheNetAddress_Type.__name__ = "OctetString"
_AtBestRouterCacheNetAddress_Object = MibTableColumn
atBestRouterCacheNetAddress = _AtBestRouterCacheNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 7, 2, 4, 1, 3),
    _AtBestRouterCacheNetAddress_Type()
)
atBestRouterCacheNetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atBestRouterCacheNetAddress.setStatus("mandatory")


class _AtRtProtocolEnabled_Type(Integer32):
    """Custom type atRtProtocolEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_AtRtProtocolEnabled_Type.__name__ = "Integer32"
_AtRtProtocolEnabled_Object = MibScalar
atRtProtocolEnabled = _AtRtProtocolEnabled_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 7, 2, 5),
    _AtRtProtocolEnabled_Type()
)
atRtProtocolEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atRtProtocolEnabled.setStatus("mandatory")
_AtRtInPackets_Type = Counter32
_AtRtInPackets_Object = MibScalar
atRtInPackets = _AtRtInPackets_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 7, 2, 6),
    _AtRtInPackets_Type()
)
atRtInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atRtInPackets.setStatus("mandatory")
_AtRtOutPackets_Type = Counter32
_AtRtOutPackets_Object = MibScalar
atRtOutPackets = _AtRtOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 7, 2, 7),
    _AtRtOutPackets_Type()
)
atRtOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atRtOutPackets.setStatus("mandatory")
_AtRtResetAllCounters_Type = Integer32
_AtRtResetAllCounters_Object = MibScalar
atRtResetAllCounters = _AtRtResetAllCounters_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 7, 2, 8),
    _AtRtResetAllCounters_Type()
)
atRtResetAllCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atRtResetAllCounters.setStatus("mandatory")


class _AtRtZoneFilterAction_Type(Integer32):
    """Custom type atRtZoneFilterAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discard", 1),
          ("forward", 2))
    )


_AtRtZoneFilterAction_Type.__name__ = "Integer32"
_AtRtZoneFilterAction_Object = MibScalar
atRtZoneFilterAction = _AtRtZoneFilterAction_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 7, 2, 9),
    _AtRtZoneFilterAction_Type()
)
atRtZoneFilterAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atRtZoneFilterAction.setStatus("mandatory")
_AtZoneFilterTable_Object = MibTable
atZoneFilterTable = _AtZoneFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 7, 2, 10)
)
if mibBuilder.loadTexts:
    atZoneFilterTable.setStatus("mandatory")
_AtZoneFilterEntry_Object = MibTableRow
atZoneFilterEntry = _AtZoneFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 7, 2, 10, 1)
)
atZoneFilterEntry.setIndexNames(
    (0, "Centrum-MIB", "atZoneFilterIndex"),
)
if mibBuilder.loadTexts:
    atZoneFilterEntry.setStatus("mandatory")
_AtZoneFilterIndex_Type = Integer32
_AtZoneFilterIndex_Object = MibTableColumn
atZoneFilterIndex = _AtZoneFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 7, 2, 10, 1, 1),
    _AtZoneFilterIndex_Type()
)
atZoneFilterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atZoneFilterIndex.setStatus("mandatory")


class _AtZoneFilterName_Type(DisplayString):
    """Custom type atZoneFilterName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AtZoneFilterName_Type.__name__ = "DisplayString"
_AtZoneFilterName_Object = MibTableColumn
atZoneFilterName = _AtZoneFilterName_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 7, 2, 10, 1, 2),
    _AtZoneFilterName_Type()
)
atZoneFilterName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atZoneFilterName.setStatus("mandatory")


class _AtZoneFilterType_Type(Integer32):
    """Custom type atZoneFilterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_AtZoneFilterType_Type.__name__ = "Integer32"
_AtZoneFilterType_Object = MibTableColumn
atZoneFilterType = _AtZoneFilterType_Object(
    (1, 3, 6, 1, 4, 1, 327, 1, 1, 7, 2, 10, 1, 3),
    _AtZoneFilterType_Type()
)
atZoneFilterType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atZoneFilterType.setStatus("mandatory")

# Managed Objects groups


# Notification objects

userLogInTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 327, 0, 16)
)
userLogInTrap.setObjects(
    ("Centrum-MIB", "adminLastTrap")
)
if mibBuilder.loadTexts:
    userLogInTrap.setStatus(
        ""
    )

userLogOutTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 327, 0, 17)
)
userLogOutTrap.setObjects(
    ("Centrum-MIB", "adminLastTrap")
)
if mibBuilder.loadTexts:
    userLogOutTrap.setStatus(
        ""
    )

userSessionTimeOutTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 327, 0, 18)
)
userSessionTimeOutTrap.setObjects(
    ("Centrum-MIB", "adminLastTrap")
)
if mibBuilder.loadTexts:
    userSessionTimeOutTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Centrum-MIB",
    **{"centrum": centrum,
       "userLogInTrap": userLogInTrap,
       "userLogOutTrap": userLogOutTrap,
       "userSessionTimeOutTrap": userSessionTimeOutTrap,
       "mibDoc": mibDoc,
       "centrumRemote": centrumRemote,
       "port": port,
       "portNumber": portNumber,
       "portTable": portTable,
       "portEntry": portEntry,
       "portIndex": portIndex,
       "portId": portId,
       "portSlot": portSlot,
       "portScriptIdx": portScriptIdx,
       "portBaudrate": portBaudrate,
       "portParity": portParity,
       "portStopBits": portStopBits,
       "portDataBits": portDataBits,
       "portCCSP": portCCSP,
       "portPPPProbeInterval": portPPPProbeInterval,
       "portPPPMaxRcvPacketLength": portPPPMaxRcvPacketLength,
       "portPPPAsyncCtrlChar": portPPPAsyncCtrlChar,
       "portPPPProtCompress": portPPPProtCompress,
       "portPPPACCompress": portPPPACCompress,
       "portCRCErrors": portCRCErrors,
       "portOversizes": portOversizes,
       "portUndersizes": portUndersizes,
       "portCollisions": portCollisions,
       "portInPackets": portInPackets,
       "portOutPackets": portOutPackets,
       "portInBytes": portInBytes,
       "portOutBytes": portOutBytes,
       "portResetPortCounters": portResetPortCounters,
       "portAsyncParityErrors": portAsyncParityErrors,
       "portAsyncCharFrameErrors": portAsyncCharFrameErrors,
       "portAsyncOverrunErrors": portAsyncOverrunErrors,
       "portAsyncPktCksumErrors": portAsyncPktCksumErrors,
       "portCTSState": portCTSState,
       "portDCDState": portDCDState,
       "portRIState": portRIState,
       "portSyncFcsErrors": portSyncFcsErrors,
       "portSyncMemoryErrors": portSyncMemoryErrors,
       "portSyncOverrunErrors": portSyncOverrunErrors,
       "portSyncUnderrunErrors": portSyncUnderrunErrors,
       "portIPCPState": portIPCPState,
       "portIPXCPState": portIPXCPState,
       "portBNCPState": portBNCPState,
       "portDriverState": portDriverState,
       "portSpeed": portSpeed,
       "portTotalErrors": portTotalErrors,
       "portTransmitDiscards": portTransmitDiscards,
       "portReceiveCongestions": portReceiveCongestions,
       "portUnknownProtocols": portUnknownProtocols,
       "portAccessType": portAccessType,
       "portDialHangUp": portDialHangUp,
       "portPortDisabled": portPortDisabled,
       "portArapCompress": portArapCompress,
       "portInterFace": portInterFace,
       "portLEDLink": portLEDLink,
       "portLEDActivity": portLEDActivity,
       "portLEDFault": portLEDFault,
       "portLinkType": portLinkType,
       "portSwitchType": portSwitchType,
       "portSPID-1": portSPID_1,
       "portSPID-2": portSPID_2,
       "portDirectoryNo-1": portDirectoryNo_1,
       "portDirectoryNo-2": portDirectoryNo_2,
       "portLocalDialNo-1": portLocalDialNo_1,
       "portLocalDialNo-2": portLocalDialNo_2,
       "portLocalSubaddress-1": portLocalSubaddress_1,
       "portLocalSubaddress-2": portLocalSubaddress_2,
       "portProtocolMode": portProtocolMode,
       "portPortReset": portPortReset,
       "portIncomingCalls": portIncomingCalls,
       "portOutgoingCalls": portOutgoingCalls,
       "portRemoteDialNo": portRemoteDialNo,
       "portRemoteSubaddress": portRemoteSubaddress,
       "portISDNInterfaceType": portISDNInterfaceType,
       "portPathName": portPathName,
       "portILCCPState": portILCCPState,
       "portCurISDNBChannel": portCurISDNBChannel,
       "portLoginStatus": portLoginStatus,
       "portLastConnectBChannel": portLastConnectBChannel,
       "portISDNPhyLineStatus": portISDNPhyLineStatus,
       "portTEIState": portTEIState,
       "portLayer3Status": portLayer3Status,
       "portResetAllCounters": portResetAllCounters,
       "portSourceRouteTable": portSourceRouteTable,
       "portSourceRouteEntry": portSourceRouteEntry,
       "portSRMacAddress": portSRMacAddress,
       "portSRState": portSRState,
       "portSRTimeToLive": portSRTimeToLive,
       "portSRLargestFrame": portSRLargestFrame,
       "portSRDirection": portSRDirection,
       "portSRRouteDescrpt": portSRRouteDescrpt,
       "portAllLoginStatus": portAllLoginStatus,
       "portTokenRingSpeed": portTokenRingSpeed,
       "portAllLEDStatus": portAllLEDStatus,
       "path": path,
       "prpaNumber": prpaNumber,
       "prpaTable": prpaTable,
       "prpaEntry": prpaEntry,
       "prpaIndex": prpaIndex,
       "prpaName": prpaName,
       "prpaType": prpaType,
       "prpaPortIdx": prpaPortIdx,
       "prpaAutoHangUp": prpaAutoHangUp,
       "prpaInPackets": prpaInPackets,
       "prpaOutPackets": prpaOutPackets,
       "prpaInBytes": prpaInBytes,
       "prpaOutBytes": prpaOutBytes,
       "prpaResetPrpaCounters": prpaResetPrpaCounters,
       "prpaLoginStatus": prpaLoginStatus,
       "prpaLoginUserName": prpaLoginUserName,
       "prpaLoginTime": prpaLoginTime,
       "prpaLoginDuration": prpaLoginDuration,
       "prpaLoginAttempts": prpaLoginAttempts,
       "prpaLoginInPackets": prpaLoginInPackets,
       "prpaLoginOutPackets": prpaLoginOutPackets,
       "prpaLoginInBytes": prpaLoginInBytes,
       "prpaLoginOutBytes": prpaLoginOutBytes,
       "prpaLoginParityErrors": prpaLoginParityErrors,
       "prpaLoginFrameErrors": prpaLoginFrameErrors,
       "prpaLoginOverrunErrors": prpaLoginOverrunErrors,
       "prpaLoginCksumErrors": prpaLoginCksumErrors,
       "prpaFilterAction": prpaFilterAction,
       "prpaFilterMap": prpaFilterMap,
       "prpaLoggerMap": prpaLoggerMap,
       "prpaFilterCount": prpaFilterCount,
       "prpaLoggerCount": prpaLoggerCount,
       "prpaDiscardedPackets": prpaDiscardedPackets,
       "prpaForwardedPackets": prpaForwardedPackets,
       "prpaReceivedPackets": prpaReceivedPackets,
       "prpaSmartFiltering": prpaSmartFiltering,
       "prpaCurrentMacAddr": prpaCurrentMacAddr,
       "prpaIpEthernetII": prpaIpEthernetII,
       "prpaIpSnap": prpaIpSnap,
       "prpaRemotePcIpAddress": prpaRemotePcIpAddress,
       "prpaIpxEn2WithNetBIOS": prpaIpxEn2WithNetBIOS,
       "prpaIpx8023WithNetBIOS": prpaIpx8023WithNetBIOS,
       "prpaIpx8022WithNetBIOS": prpaIpx8022WithNetBIOS,
       "prpaIpxSnapWithNetBIOS": prpaIpxSnapWithNetBIOS,
       "prpaXNS": prpaXNS,
       "prpaVinesEthernetII": prpaVinesEthernetII,
       "prpaVinesSnap": prpaVinesSnap,
       "prpaNetBIOS": prpaNetBIOS,
       "prpaDECNet": prpaDECNet,
       "prpaUnknowEthernetII": prpaUnknowEthernetII,
       "prpaUnknownSap": prpaUnknownSap,
       "prpaUnknownSnap": prpaUnknownSnap,
       "prpaMulticastAddress": prpaMulticastAddress,
       "prpaXNSSap": prpaXNSSap,
       "prpaXNSSnap": prpaXNSSnap,
       "prpaVinesSap": prpaVinesSap,
       "prpaIpxEn2": prpaIpxEn2,
       "prpaIpx8023": prpaIpx8023,
       "prpaIpx8022": prpaIpx8022,
       "prpaIpxSnap": prpaIpxSnap,
       "prpaPortList": prpaPortList,
       "prpaSpoofState": prpaSpoofState,
       "prpaCCPState": prpaCCPState,
       "prpaIPCPState": prpaIPCPState,
       "prpaIPXCPState": prpaIPXCPState,
       "prpaBNCPState": prpaBNCPState,
       "prpaARAPState": prpaARAPState,
       "prpaLinkUtil": prpaLinkUtil,
       "plocalNumber": plocalNumber,
       "plocalTable": plocalTable,
       "plocalEntry": plocalEntry,
       "plocalIndex": plocalIndex,
       "plocalName": plocalName,
       "plocalType": plocalType,
       "plocalPortIdx": plocalPortIdx,
       "plocalInPackets": plocalInPackets,
       "plocalOutPackets": plocalOutPackets,
       "plocalInBytes": plocalInBytes,
       "plocalOutBytes": plocalOutBytes,
       "plocalResetPlocalCounters": plocalResetPlocalCounters,
       "plocalFilterAction": plocalFilterAction,
       "plocalFilterMap": plocalFilterMap,
       "plocalLoggerMap": plocalLoggerMap,
       "plocalFilterCount": plocalFilterCount,
       "plocalLoggerCount": plocalLoggerCount,
       "plocalDiscardedPackets": plocalDiscardedPackets,
       "plocalForwardedPackets": plocalForwardedPackets,
       "plocalReceivedPackets": plocalReceivedPackets,
       "prmtNumber": prmtNumber,
       "prmtTable": prmtTable,
       "prmtEntry": prmtEntry,
       "prmtIndex": prmtIndex,
       "prmtName": prmtName,
       "prmtType": prmtType,
       "prmtInitiator": prmtInitiator,
       "prmtCongestThreshold": prmtCongestThreshold,
       "prmtScheduleType1": prmtScheduleType1,
       "prmtDaysScheduled1": prmtDaysScheduled1,
       "prmtStartTime1": prmtStartTime1,
       "prmtHowLong1": prmtHowLong1,
       "prmtScheduleType2": prmtScheduleType2,
       "prmtDaysScheduled2": prmtDaysScheduled2,
       "prmtStartTime2": prmtStartTime2,
       "prmtHowLong2": prmtHowLong2,
       "prmtInPackets": prmtInPackets,
       "prmtOutPackets": prmtOutPackets,
       "prmtInBytes": prmtInBytes,
       "prmtOutBytes": prmtOutBytes,
       "prmtResetPrmtCounters": prmtResetPrmtCounters,
       "prmtFilterAction": prmtFilterAction,
       "prmtFilterMap": prmtFilterMap,
       "prmtLoggerMap": prmtLoggerMap,
       "prmtFilterCount": prmtFilterCount,
       "prmtLoggerCount": prmtLoggerCount,
       "prmtDiscardedPackets": prmtDiscardedPackets,
       "prmtForwardedPackets": prmtForwardedPackets,
       "prmtReceivedPackets": prmtReceivedPackets,
       "prmtSmartFiltering": prmtSmartFiltering,
       "prmtOutCongestions": prmtOutCongestions,
       "prmtRmtRouterName": prmtRmtRouterName,
       "prmtTypeSelection": prmtTypeSelection,
       "prmtAsyncPortNo": prmtAsyncPortNo,
       "prmtISDNPortNo": prmtISDNPortNo,
       "prmtISDNReqBaudRate": prmtISDNReqBaudRate,
       "prmtSpoofState": prmtSpoofState,
       "prmtCCPState": prmtCCPState,
       "prmtIPCPState": prmtIPCPState,
       "prmtIPXCPState": prmtIPXCPState,
       "prmtBNCPState": prmtBNCPState,
       "prmtLinkUtil": prmtLinkUtil,
       "prmtPMPortList": prmtPMPortList,
       "prmtBUPortList": prmtBUPortList,
       "prmtODPortList": prmtODPortList,
       "prmtSCPortList": prmtSCPortList,
       "prmtPortTable": prmtPortTable,
       "prmtPortEntry": prmtPortEntry,
       "prmtPortPrmtIdx": prmtPortPrmtIdx,
       "prmtPortPortIdx": prmtPortPortIdx,
       "prmtPortType": prmtPortType,
       "prmtPortPhoneNumber": prmtPortPhoneNumber,
       "prmtPortDirectoryNo": prmtPortDirectoryNo,
       "pathResetAllCounters": pathResetAllCounters,
       "prmtPhoneTable": prmtPhoneTable,
       "prmtPhoneEntry": prmtPhoneEntry,
       "prmtPhonePrmtIdx": prmtPhonePrmtIdx,
       "prmtPhoneIdx": prmtPhoneIdx,
       "prmtPhoneType": prmtPhoneType,
       "prmtPhonePhoneNumber": prmtPhonePhoneNumber,
       "prmtPhoneDirectoryNo": prmtPhoneDirectoryNo,
       "crip": crip,
       "ipRpa": ipRpa,
       "ipRpaNumber": ipRpaNumber,
       "ipRpaTable": ipRpaTable,
       "ipRpaEntry": ipRpaEntry,
       "ipRpaIndex": ipRpaIndex,
       "ipRpaCurrentClientIpAddress": ipRpaCurrentClientIpAddress,
       "ipRpaConfigClientIpAddress": ipRpaConfigClientIpAddress,
       "ipRpaTcpHdrCompress": ipRpaTcpHdrCompress,
       "ipRpaType": ipRpaType,
       "ipRpaBootpEnabled": ipRpaBootpEnabled,
       "ipRpaRarpEnabled": ipRpaRarpEnabled,
       "ipRpaBootpOrRarpRequired": ipRpaBootpOrRarpRequired,
       "ipRpaBootpInPackets": ipRpaBootpInPackets,
       "ipRpaBootpOutPackets": ipRpaBootpOutPackets,
       "ipRpaRarpInPackets": ipRpaRarpInPackets,
       "ipRpaRarpOutPackets": ipRpaRarpOutPackets,
       "ipRpaResetAllRasCounters": ipRpaResetAllRasCounters,
       "ipRpaPRPAIpHdrCompress": ipRpaPRPAIpHdrCompress,
       "ipRt": ipRt,
       "ipSRouteNumber": ipSRouteNumber,
       "ipSRouteTable": ipSRouteTable,
       "ipSRouteEntry": ipSRouteEntry,
       "ipSRouteIndex": ipSRouteIndex,
       "ipSRouteName": ipSRouteName,
       "ipSRouteType": ipSRouteType,
       "ipSRoutePathType": ipSRoutePathType,
       "ipSRoutePathIdx": ipSRoutePathIdx,
       "ipSRouteDestIpAddress": ipSRouteDestIpAddress,
       "ipSRouteNextRouter": ipSRouteNextRouter,
       "ipSRouteHopCount": ipSRouteHopCount,
       "ipPLocalNumber": ipPLocalNumber,
       "ipPLocalTable": ipPLocalTable,
       "ipPLocalEntry": ipPLocalEntry,
       "ipPLocalIndex": ipPLocalIndex,
       "ipPLocalIpAddress": ipPLocalIpAddress,
       "ipPLocalNetMask": ipPLocalNetMask,
       "ipPLocalBcastAddr": ipPLocalBcastAddr,
       "ipPRmtNumber": ipPRmtNumber,
       "ipPRmtTable": ipPRmtTable,
       "ipPRmtEntry": ipPRmtEntry,
       "ipPRmtIndex": ipPRmtIndex,
       "ipPRmtIpAddress": ipPRmtIpAddress,
       "ipPRmtNetMask": ipPRmtNetMask,
       "ipPRmtBcastAddr": ipPRmtBcastAddr,
       "ipPRmtRipUpdate": ipPRmtRipUpdate,
       "ipPRmtType": ipPRmtType,
       "ipPRmtTcpHdrCompress": ipPRmtTcpHdrCompress,
       "ipRtUpdateTime": ipRtUpdateTime,
       "ipRtRipEnabled": ipRtRipEnabled,
       "ipRtEnabled": ipRtEnabled,
       "ipRtDefaultTTL": ipRtDefaultTTL,
       "ipRtPoisonReverse": ipRtPoisonReverse,
       "ipRtResetAllCounters": ipRtResetAllCounters,
       "ipRtInPackets": ipRtInPackets,
       "ipRtOutPackets": ipRtOutPackets,
       "ipRtDefaultRouterAddress": ipRtDefaultRouterAddress,
       "ipRtDefaultRouterPathType": ipRtDefaultRouterPathType,
       "ipRtDefaultRouterPathIdx": ipRtDefaultRouterPathIdx,
       "ipRtDiscardNBBcastPkts": ipRtDiscardNBBcastPkts,
       "ipx": ipx,
       "ipxRpa": ipxRpa,
       "ipxRpaNetNumber": ipxRpaNetNumber,
       "ipxRpaNumber": ipxRpaNumber,
       "ipxRpaTable": ipxRpaTable,
       "ipxRpaEntry": ipxRpaEntry,
       "ipxRpaIndex": ipxRpaIndex,
       "ipxRpaCurrHostAddr": ipxRpaCurrHostAddr,
       "ipxRt": ipxRt,
       "ipxSRouteNumber": ipxSRouteNumber,
       "ipxSRouteTable": ipxSRouteTable,
       "ipxSRouteEntry": ipxSRouteEntry,
       "ipxSRouteIndex": ipxSRouteIndex,
       "ipxSRouteName": ipxSRouteName,
       "ipxSRouteType": ipxSRouteType,
       "ipxSRoutePathType": ipxSRoutePathType,
       "ipxSRoutePathIdx": ipxSRoutePathIdx,
       "ipxSRouteDestNetNumber": ipxSRouteDestNetNumber,
       "ipxSRouteNextHostAddress": ipxSRouteNextHostAddress,
       "ipxSRouteHopCount": ipxSRouteHopCount,
       "ipxPLocalNumber": ipxPLocalNumber,
       "ipxPLocalTable": ipxPLocalTable,
       "ipxPLocalEntry": ipxPLocalEntry,
       "ipxPLocalIndex": ipxPLocalIndex,
       "ipxPLocalNetNumber": ipxPLocalNetNumber,
       "ipxPLocalDataLinkType": ipxPLocalDataLinkType,
       "ipxPRmtNumber": ipxPRmtNumber,
       "ipxPRmtTable": ipxPRmtTable,
       "ipxPRmtEntry": ipxPRmtEntry,
       "ipxPRmtIndex": ipxPRmtIndex,
       "ipxPRmtNetNumber": ipxPRmtNetNumber,
       "ipxPRmtNripUpdate": ipxPRmtNripUpdate,
       "ipxPRmtType": ipxPRmtType,
       "ipxRtUpdateTime": ipxRtUpdateTime,
       "ipxRtEnabled": ipxRtEnabled,
       "ipxRtRipEnabled": ipxRtRipEnabled,
       "ipxRtResetAllCounters": ipxRtResetAllCounters,
       "ipxRtInPackets": ipxRtInPackets,
       "ipxRtOutPackets": ipxRtOutPackets,
       "ipxRtRipNumber": ipxRtRipNumber,
       "ipxRtRipTable": ipxRtRipTable,
       "ipxRtRipEntry": ipxRtRipEntry,
       "ipxRtRipDestNetNumber": ipxRtRipDestNetNumber,
       "ipxRtRipPathType": ipxRtRipPathType,
       "ipxRtRipPathIdx": ipxRtRipPathIdx,
       "ipxRtRipNextHostAddress": ipxRtRipNextHostAddress,
       "ipxRtRipHopCount": ipxRtRipHopCount,
       "ipxRtRipTicks": ipxRtRipTicks,
       "ipxRtRipRouteType": ipxRtRipRouteType,
       "ipxRtSapNumber": ipxRtSapNumber,
       "ipxRtSapTable": ipxRtSapTable,
       "ipxRtSapEntry": ipxRtSapEntry,
       "ipxRtSapIndex": ipxRtSapIndex,
       "ipxRtSapServiceName": ipxRtSapServiceName,
       "ipxRtSapServiceType": ipxRtSapServiceType,
       "ipxRtSapServerNetNumber": ipxRtSapServerNetNumber,
       "ipxRtSapServerHostAddress": ipxRtSapServerHostAddress,
       "ipxSpoofingTime": ipxSpoofingTime,
       "ipxRtDoNBPropagation": ipxRtDoNBPropagation,
       "brg": brg,
       "brgFilterNumber": brgFilterNumber,
       "brgFilterTable": brgFilterTable,
       "brgFilterEntry": brgFilterEntry,
       "brgFilterIndex": brgFilterIndex,
       "brgFilterName": brgFilterName,
       "brgFilterType": brgFilterType,
       "brgFilterMask1Offset": brgFilterMask1Offset,
       "brgFilterMask1Value": brgFilterMask1Value,
       "brgFilterMask1Type": brgFilterMask1Type,
       "brgFilterMask1Size": brgFilterMask1Size,
       "brgFilterMask2Offset": brgFilterMask2Offset,
       "brgFilterMask2Value": brgFilterMask2Value,
       "brgFilterMask2Type": brgFilterMask2Type,
       "brgFilterMask2Size": brgFilterMask2Size,
       "brgFilterMask3Offset": brgFilterMask3Offset,
       "brgFilterMask3Value": brgFilterMask3Value,
       "brgFilterMask3Type": brgFilterMask3Type,
       "brgFilterMask3Size": brgFilterMask3Size,
       "brgFilterMask4Offset": brgFilterMask4Offset,
       "brgFilterMask4Value": brgFilterMask4Value,
       "brgFilterMask4Type": brgFilterMask4Type,
       "brgFilterMask4Size": brgFilterMask4Size,
       "brgFilterSkipRii": brgFilterSkipRii,
       "brgLoggerNumber": brgLoggerNumber,
       "brgLoggerTable": brgLoggerTable,
       "brgLoggerEntry": brgLoggerEntry,
       "brgLoggerIndex": brgLoggerIndex,
       "brgLoggerName": brgLoggerName,
       "brgLoggerType": brgLoggerType,
       "brgLoggerMask1Offset": brgLoggerMask1Offset,
       "brgLoggerMask1Value": brgLoggerMask1Value,
       "brgLoggerMask1Type": brgLoggerMask1Type,
       "brgLoggerMask1Size": brgLoggerMask1Size,
       "brgLoggerMask2Offset": brgLoggerMask2Offset,
       "brgLoggerMask2Value": brgLoggerMask2Value,
       "brgLoggerMask2Type": brgLoggerMask2Type,
       "brgLoggerMask2Size": brgLoggerMask2Size,
       "brgLoggerMask3Offset": brgLoggerMask3Offset,
       "brgLoggerMask3Value": brgLoggerMask3Value,
       "brgLoggerMask3Type": brgLoggerMask3Type,
       "brgLoggerMask3Size": brgLoggerMask3Size,
       "brgLoggerMask4Offset": brgLoggerMask4Offset,
       "brgLoggerMask4Value": brgLoggerMask4Value,
       "brgLoggerMask4Type": brgLoggerMask4Type,
       "brgLoggerMask4Size": brgLoggerMask4Size,
       "brgLoggerSkipRii": brgLoggerSkipRii,
       "brgPLocalNumber": brgPLocalNumber,
       "brgPLocalTable": brgPLocalTable,
       "brgPLocalEntry": brgPLocalEntry,
       "brgPLocalIndex": brgPLocalIndex,
       "brgPLocalEnabled": brgPLocalEnabled,
       "brgStpPLocalPriority": brgStpPLocalPriority,
       "brgStpPLocalCost": brgStpPLocalCost,
       "brgStpPLocalDesigRoot": brgStpPLocalDesigRoot,
       "brgStpPLocalDesigCost": brgStpPLocalDesigCost,
       "brgStpPLocalDesigBridge": brgStpPLocalDesigBridge,
       "brgStpPLocalDesigPath": brgStpPLocalDesigPath,
       "brgStpPLocalPathState": brgStpPLocalPathState,
       "brgPRmtNumber": brgPRmtNumber,
       "brgPRmtTable": brgPRmtTable,
       "brgPRmtEntry": brgPRmtEntry,
       "brgPRmtIndex": brgPRmtIndex,
       "brgPRmtEnabled": brgPRmtEnabled,
       "brgStpPRmtPriority": brgStpPRmtPriority,
       "brgStpPRmtCost": brgStpPRmtCost,
       "brgStpPRmtDesigRoot": brgStpPRmtDesigRoot,
       "brgStpPRmtDesigCost": brgStpPRmtDesigCost,
       "brgStpPRmtDesigBridge": brgStpPRmtDesigBridge,
       "brgStpPRmtDesigPath": brgStpPRmtDesigPath,
       "brgStpPRmtPathState": brgStpPRmtPathState,
       "brgMisc": brgMisc,
       "brgSpanningTreeProtocol": brgSpanningTreeProtocol,
       "brgResetAllCounters": brgResetAllCounters,
       "brgAutoFtrEnabled": brgAutoFtrEnabled,
       "brgPRPASmartFiltering": brgPRPASmartFiltering,
       "brgPRPAFilterAction": brgPRPAFilterAction,
       "brgPRPAFilterMap": brgPRPAFilterMap,
       "brgPRPALoggerMap": brgPRPALoggerMap,
       "brgMacHdrComp": brgMacHdrComp,
       "brgLearnedTable": brgLearnedTable,
       "brgLearnedEntry": brgLearnedEntry,
       "brgLearnedAddress": brgLearnedAddress,
       "brgLearnedPathType": brgLearnedPathType,
       "brgLearnedPathIdx": brgLearnedPathIdx,
       "brgLearnedAge": brgLearnedAge,
       "brgTokenRing": brgTokenRing,
       "brgLocalRingNumber": brgLocalRingNumber,
       "brgProxyRingNumber": brgProxyRingNumber,
       "brgBridgeNumber": brgBridgeNumber,
       "admin": admin,
       "adminUserNumber": adminUserNumber,
       "adminUserTable": adminUserTable,
       "adminUserEntry": adminUserEntry,
       "adminUserIndex": adminUserIndex,
       "adminUserName": adminUserName,
       "adminUserType": adminUserType,
       "adminUserPassword": adminUserPassword,
       "adminUserCallBackPhone": adminUserCallBackPhone,
       "adminEncryptUserPassword": adminEncryptUserPassword,
       "adminEncryptCallBackPhone": adminEncryptCallBackPhone,
       "adminCommNumber": adminCommNumber,
       "adminCommTable": adminCommTable,
       "adminCommEntry": adminCommEntry,
       "adminCommIndex": adminCommIndex,
       "adminCommName": adminCommName,
       "adminCommType": adminCommType,
       "adminCommMgrIpAddress": adminCommMgrIpAddress,
       "adminCommMgrIpxNetNumber": adminCommMgrIpxNetNumber,
       "adminCommMgrMacAddress": adminCommMgrMacAddress,
       "adminScriptNumber": adminScriptNumber,
       "adminScriptTable": adminScriptTable,
       "adminScriptEntry": adminScriptEntry,
       "adminScriptIndex": adminScriptIndex,
       "adminScriptName": adminScriptName,
       "adminScriptType": adminScriptType,
       "adminScript": adminScript,
       "adminRpaLogNumber": adminRpaLogNumber,
       "adminRpaLogTable": adminRpaLogTable,
       "adminRpaLogEntry": adminRpaLogEntry,
       "adminRpaLogIndex": adminRpaLogIndex,
       "adminRpaLogUserName": adminRpaLogUserName,
       "adminRpaLogTime": adminRpaLogTime,
       "adminRpaLogDuration": adminRpaLogDuration,
       "adminRpaLogAttempts": adminRpaLogAttempts,
       "adminRpaLogInPackets": adminRpaLogInPackets,
       "adminRpaLogOutPackets": adminRpaLogOutPackets,
       "adminRpaLogInBytes": adminRpaLogInBytes,
       "adminRpaLogOutBytes": adminRpaLogOutBytes,
       "adminRpaLogParityErrors": adminRpaLogParityErrors,
       "adminRpaLogFrameErrors": adminRpaLogFrameErrors,
       "adminRpaLogOverrunErrors": adminRpaLogOverrunErrors,
       "adminRpaLogCksumErrors": adminRpaLogCksumErrors,
       "adminRpaLogDate": adminRpaLogDate,
       "adminRpaLogPortName": adminRpaLogPortName,
       "adminRpaLogPathName": adminRpaLogPathName,
       "adminMisc": adminMisc,
       "adminSysDescr": adminSysDescr,
       "adminNodeName": adminNodeName,
       "adminNodePassword": adminNodePassword,
       "adminDate": adminDate,
       "adminTime": adminTime,
       "adminGreeting": adminGreeting,
       "adminPrompt": adminPrompt,
       "adminSNMPGetFrom": adminSNMPGetFrom,
       "adminDoIntegrity": adminDoIntegrity,
       "adminDoFileload": adminDoFileload,
       "adminLoadfileName": adminLoadfileName,
       "adminLastTrap": adminLastTrap,
       "adminResetAllUserCounters": adminResetAllUserCounters,
       "adminEraseConfig": adminEraseConfig,
       "adminUIMsgLevel": adminUIMsgLevel,
       "adminSNMPMsgLevel": adminSNMPMsgLevel,
       "adminLoginOption": adminLoginOption,
       "adminReboot": adminReboot,
       "adminMajorVersion": adminMajorVersion,
       "adminMinorVersion": adminMinorVersion,
       "adminMIBVersion": adminMIBVersion,
       "adminTimeZone": adminTimeZone,
       "adminSecurityServerType": adminSecurityServerType,
       "adminSecPassword": adminSecPassword,
       "adminScrtyClntIpAddr": adminScrtyClntIpAddr,
       "adminSecondScrtyClntIpAddr": adminSecondScrtyClntIpAddr,
       "adminUdpPort": adminUdpPort,
       "adminTelnetAdminPort": adminTelnetAdminPort,
       "adminTelnetDialOutAuth": adminTelnetDialOutAuth,
       "adminDialOutEnabled": adminDialOutEnabled,
       "adminEncryptNodePassword": adminEncryptNodePassword,
       "adminEncryptSecurityServerType": adminEncryptSecurityServerType,
       "adminEncryptSecPassword": adminEncryptSecPassword,
       "adminEncryptScrtyClntIpAddr": adminEncryptScrtyClntIpAddr,
       "adminEncryptSecondScrtyClntIpAddr": adminEncryptSecondScrtyClntIpAddr,
       "adminEncryptUdpPort": adminEncryptUdpPort,
       "adminEPromSize": adminEPromSize,
       "adminNVRamSize": adminNVRamSize,
       "adminFlashRomSize": adminFlashRomSize,
       "adminLocalDRamSize": adminLocalDRamSize,
       "adminSharedDRamSize": adminSharedDRamSize,
       "adminHWRev": adminHWRev,
       "adminEncryptSuperUserPassword": adminEncryptSuperUserPassword,
       "adminNewGreeting": adminNewGreeting,
       "adminTFTPServerIpAddr": adminTFTPServerIpAddr,
       "adminSaveConfig": adminSaveConfig,
       "adminMaintenanceVersion": adminMaintenanceVersion,
       "adminCheckConsoleModem": adminCheckConsoleModem,
       "adminConsoleImageDownload": adminConsoleImageDownload,
       "adminConsoleConfigUpload": adminConsoleConfigUpload,
       "adminConsoleConfigDownload": adminConsoleConfigDownload,
       "adminRasIdleTime": adminRasIdleTime,
       "adminRouterIdleTime": adminRouterIdleTime,
       "adminRasSpoofTime": adminRasSpoofTime,
       "adminRouterSpoofTime": adminRouterSpoofTime,
       "adminLnkUtilHighThld": adminLnkUtilHighThld,
       "adminLnkUtilLowThld": adminLnkUtilLowThld,
       "adminCallerIdCheck": adminCallerIdCheck,
       "adminISDNRequiredBaudrate": adminISDNRequiredBaudrate,
       "adminRouterCCPEnabled": adminRouterCCPEnabled,
       "adminSuggestFlag": adminSuggestFlag,
       "adminEEVersionNo": adminEEVersionNo,
       "adminMdSetupNumber": adminMdSetupNumber,
       "adminMdSetupTable": adminMdSetupTable,
       "adminMdSetupEntry": adminMdSetupEntry,
       "adminMdSetupIndex": adminMdSetupIndex,
       "adminMdSetupType": adminMdSetupType,
       "adminMdSetupName": adminMdSetupName,
       "adminMdSetupATCmd": adminMdSetupATCmd,
       "adminMdSetupARAP1-0ATCmd": adminMdSetupARAP1_0ATCmd,
       "adminMdSetupIncomingCall": adminMdSetupIncomingCall,
       "adminMdSetupConnIndication": adminMdSetupConnIndication,
       "adminMdSetupCallTimeOut": adminMdSetupCallTimeOut,
       "adminMdSetupCallDelay": adminMdSetupCallDelay,
       "adminCallerIDNumber": adminCallerIDNumber,
       "adminCallerIDTable": adminCallerIDTable,
       "adminCallerIDEntry": adminCallerIDEntry,
       "adminCallerIDIndex": adminCallerIDIndex,
       "adminCallerIDName": adminCallerIDName,
       "adminCallerIDType": adminCallerIDType,
       "adminCallerIDComment": adminCallerIDComment,
       "crat": crat,
       "atRpa": atRpa,
       "atRpaNumber": atRpaNumber,
       "atRpaTable": atRpaTable,
       "atRpaEntry": atRpaEntry,
       "atRpaIndex": atRpaIndex,
       "atRpaNetworkAddress": atRpaNetworkAddress,
       "atRpaState": atRpaState,
       "atRpaDialInZone": atRpaDialInZone,
       "atRpaMaxConnTime": atRpaMaxConnTime,
       "atRpaNoNbpMulticast": atRpaNoNbpMulticast,
       "atRt": atRt,
       "atPLocalNumber": atPLocalNumber,
       "atPLocalTable": atPLocalTable,
       "atPLocalEntry": atPLocalEntry,
       "atPLocalIndex": atPLocalIndex,
       "atPLocalNetAddress": atPLocalNetAddress,
       "atPLocalNetStart": atPLocalNetStart,
       "atPLocalNetEnd": atPLocalNetEnd,
       "atPLocalDefaultRouter": atPLocalDefaultRouter,
       "atPLocalLocalZone": atPLocalLocalZone,
       "atAarpTable": atAarpTable,
       "atAarpEntry": atAarpEntry,
       "atAarpIfIndex": atAarpIfIndex,
       "atAarpPhysAddress": atAarpPhysAddress,
       "atAarpNetAddress": atAarpNetAddress,
       "atBestRouterCacheTable": atBestRouterCacheTable,
       "atBestRouterCacheEntry": atBestRouterCacheEntry,
       "atBestRouterCacheIfIndex": atBestRouterCacheIfIndex,
       "atBestRouterCachePhysAddress": atBestRouterCachePhysAddress,
       "atBestRouterCacheNetAddress": atBestRouterCacheNetAddress,
       "atRtProtocolEnabled": atRtProtocolEnabled,
       "atRtInPackets": atRtInPackets,
       "atRtOutPackets": atRtOutPackets,
       "atRtResetAllCounters": atRtResetAllCounters,
       "atRtZoneFilterAction": atRtZoneFilterAction,
       "atZoneFilterTable": atZoneFilterTable,
       "atZoneFilterEntry": atZoneFilterEntry,
       "atZoneFilterIndex": atZoneFilterIndex,
       "atZoneFilterName": atZoneFilterName,
       "atZoneFilterType": atZoneFilterType}
)
