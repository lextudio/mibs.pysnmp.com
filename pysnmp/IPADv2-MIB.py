# SNMP MIB module (IPADv2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IPADv2-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:10:39 2024
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

(ddsNetBPVCount,
 ddsNetFDLCount,
 ddsNetLOSCount,
 ddsNetOOFCount,
 ddsNetOOSCount,
 serialDteDTRAlarmStatus,
 t1e1AISCount,
 t1e1BPVSCount,
 t1e1CSSCount,
 t1e1ESCount,
 t1e1LOSSCount,
 t1e1OOFSCount,
 t1e1RASCount,
 t1e1SESCount,
 t1e1UASCount) = mibBuilder.importSymbols(
    "DS8200v2-MIB",
    "ddsNetBPVCount",
    "ddsNetFDLCount",
    "ddsNetLOSCount",
    "ddsNetOOFCount",
    "ddsNetOOSCount",
    "serialDteDTRAlarmStatus",
    "t1e1AISCount",
    "t1e1BPVSCount",
    "t1e1CSSCount",
    "t1e1ESCount",
    "t1e1LOSSCount",
    "t1e1OOFSCount",
    "t1e1RASCount",
    "t1e1SESCount",
    "t1e1UASCount")

(hbu,
 verilink) = mibBuilder.importSymbols(
    "DS8200v2-TC-MIB",
    "hbu",
    "verilink")

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

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

ipad = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 321, 100, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IpadFrPort_ObjectIdentity = ObjectIdentity
ipadFrPort = _IpadFrPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 1)
)
_IpadFrPortTable_Object = MibTable
ipadFrPortTable = _IpadFrPortTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ipadFrPortTable.setStatus("current")
_IpadFrPortTableEntry_Object = MibTableRow
ipadFrPortTableEntry = _IpadFrPortTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 1, 1, 1)
)
ipadFrPortTableEntry.setIndexNames(
    (0, "IPADv2-MIB", "ipadFrPortService"),
)
if mibBuilder.loadTexts:
    ipadFrPortTableEntry.setStatus("current")
_IpadFrPortService_Type = Integer32
_IpadFrPortService_Object = MibTableColumn
ipadFrPortService = _IpadFrPortService_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 1, 1, 1, 1),
    _IpadFrPortService_Type()
)
ipadFrPortService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadFrPortService.setStatus("current")


class _IpadFrPortActive_Type(Integer32):
    """Custom type ipadFrPortActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("other", 1),
          ("yes", 3))
    )


_IpadFrPortActive_Type.__name__ = "Integer32"
_IpadFrPortActive_Object = MibTableColumn
ipadFrPortActive = _IpadFrPortActive_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 1, 1, 1, 2),
    _IpadFrPortActive_Type()
)
ipadFrPortActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadFrPortActive.setStatus("current")


class _IpadFrPortLMIType_Type(Integer32):
    """Custom type ipadFrPortLMIType based on Integer32"""
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
        *(("ansi", 3),
          ("ccitt", 2),
          ("lmi", 4),
          ("none", 5),
          ("other", 1))
    )


_IpadFrPortLMIType_Type.__name__ = "Integer32"
_IpadFrPortLMIType_Object = MibTableColumn
ipadFrPortLMIType = _IpadFrPortLMIType_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 1, 1, 1, 3),
    _IpadFrPortLMIType_Type()
)
ipadFrPortLMIType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadFrPortLMIType.setStatus("current")


class _IpadFrPortLMIMode_Type(Integer32):
    """Custom type ipadFrPortLMIMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("monitoring", 3),
          ("other", 1),
          ("sourcing", 2))
    )


_IpadFrPortLMIMode_Type.__name__ = "Integer32"
_IpadFrPortLMIMode_Object = MibTableColumn
ipadFrPortLMIMode = _IpadFrPortLMIMode_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 1, 1, 1, 4),
    _IpadFrPortLMIMode_Type()
)
ipadFrPortLMIMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadFrPortLMIMode.setStatus("current")
_IpadFrPortRxInvAlmThreshold_Type = Integer32
_IpadFrPortRxInvAlmThreshold_Object = MibTableColumn
ipadFrPortRxInvAlmThreshold = _IpadFrPortRxInvAlmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 1, 1, 1, 5),
    _IpadFrPortRxInvAlmThreshold_Type()
)
ipadFrPortRxInvAlmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadFrPortRxInvAlmThreshold.setStatus("current")


class _IpadFrPortRxInvAlmAlarm_Type(Integer32):
    """Custom type ipadFrPortRxInvAlmAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noAlarm", 2),
          ("other", 1),
          ("thresholdExceeded", 3))
    )


_IpadFrPortRxInvAlmAlarm_Type.__name__ = "Integer32"
_IpadFrPortRxInvAlmAlarm_Object = MibTableColumn
ipadFrPortRxInvAlmAlarm = _IpadFrPortRxInvAlmAlarm_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 1, 1, 1, 6),
    _IpadFrPortRxInvAlmAlarm_Type()
)
ipadFrPortRxInvAlmAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadFrPortRxInvAlmAlarm.setStatus("current")
_IpadFrPortTxAlmThreshold_Type = Integer32
_IpadFrPortTxAlmThreshold_Object = MibTableColumn
ipadFrPortTxAlmThreshold = _IpadFrPortTxAlmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 1, 1, 1, 7),
    _IpadFrPortTxAlmThreshold_Type()
)
ipadFrPortTxAlmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadFrPortTxAlmThreshold.setStatus("current")


class _IpadFrPortTxAlmAlarm_Type(Integer32):
    """Custom type ipadFrPortTxAlmAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noAlarm", 2),
          ("other", 1),
          ("thresholdExceeded", 3))
    )


_IpadFrPortTxAlmAlarm_Type.__name__ = "Integer32"
_IpadFrPortTxAlmAlarm_Object = MibTableColumn
ipadFrPortTxAlmAlarm = _IpadFrPortTxAlmAlarm_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 1, 1, 1, 8),
    _IpadFrPortTxAlmAlarm_Type()
)
ipadFrPortTxAlmAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadFrPortTxAlmAlarm.setStatus("current")
_IpadFrPortRxAlmThreshold_Type = Integer32
_IpadFrPortRxAlmThreshold_Object = MibTableColumn
ipadFrPortRxAlmThreshold = _IpadFrPortRxAlmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 1, 1, 1, 9),
    _IpadFrPortRxAlmThreshold_Type()
)
ipadFrPortRxAlmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadFrPortRxAlmThreshold.setStatus("current")


class _IpadFrPortRxAlmAlarm_Type(Integer32):
    """Custom type ipadFrPortRxAlmAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noAlarm", 2),
          ("other", 1),
          ("thresholdExceeded", 3))
    )


_IpadFrPortRxAlmAlarm_Type.__name__ = "Integer32"
_IpadFrPortRxAlmAlarm_Object = MibTableColumn
ipadFrPortRxAlmAlarm = _IpadFrPortRxAlmAlarm_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 1, 1, 1, 10),
    _IpadFrPortRxAlmAlarm_Type()
)
ipadFrPortRxAlmAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadFrPortRxAlmAlarm.setStatus("current")


class _IpadFrPortAlarmReset_Type(Integer32):
    """Custom type ipadFrPortAlarmReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("frPortAlarmResetClearAlarms", 2),
          ("frPortAlarmResetClearStats", 3),
          ("frPortAlarmResetOther", 1))
    )


_IpadFrPortAlarmReset_Type.__name__ = "Integer32"
_IpadFrPortAlarmReset_Object = MibTableColumn
ipadFrPortAlarmReset = _IpadFrPortAlarmReset_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 1, 1, 1, 11),
    _IpadFrPortAlarmReset_Type()
)
ipadFrPortAlarmReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadFrPortAlarmReset.setStatus("current")
_IpadService_ObjectIdentity = ObjectIdentity
ipadService = _IpadService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 2)
)
_IpadServiceTable_Object = MibTable
ipadServiceTable = _IpadServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ipadServiceTable.setStatus("current")
_IpadServiceTableEntry_Object = MibTableRow
ipadServiceTableEntry = _IpadServiceTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 2, 1, 1)
)
ipadServiceTableEntry.setIndexNames(
    (0, "IPADv2-MIB", "ipadServiceIndex"),
)
if mibBuilder.loadTexts:
    ipadServiceTableEntry.setStatus("current")
_IpadServiceIndex_Type = Integer32
_IpadServiceIndex_Object = MibTableColumn
ipadServiceIndex = _IpadServiceIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 2, 1, 1, 1),
    _IpadServiceIndex_Type()
)
ipadServiceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadServiceIndex.setStatus("current")


class _IpadServiceifIndex_Type(Integer32):
    """Custom type ipadServiceifIndex based on Integer32"""
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
              100)
        )
    )
    namedValues = NamedValues(
        *(("atmCES", 9),
          ("auxiliary", 7),
          ("disabled", 0),
          ("ethernet", 6),
          ("modem", 10),
          ("network1", 2),
          ("network2", 3),
          ("network3", 8),
          ("supervisor", 1),
          ("user1", 4),
          ("user2", 5),
          ("virtual", 100))
    )


_IpadServiceifIndex_Type.__name__ = "Integer32"
_IpadServiceifIndex_Object = MibTableColumn
ipadServiceifIndex = _IpadServiceifIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 2, 1, 1, 2),
    _IpadServiceifIndex_Type()
)
ipadServiceifIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadServiceifIndex.setStatus("current")


class _IpadServiceType_Type(Integer32):
    """Custom type ipadServiceType based on Integer32"""
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
              15)
        )
    )
    namedValues = NamedValues(
        *(("atm", 12),
          ("atmCES", 14),
          ("frameRelay", 5),
          ("frameRelayMonitor", 6),
          ("hdlcPPP", 13),
          ("ip", 7),
          ("modem", 15),
          ("other", 1),
          ("parallelIO", 11),
          ("ppp", 3),
          ("pppMonitor", 4),
          ("scada", 10),
          ("serial", 8),
          ("tdm", 2),
          ("tty", 9))
    )


_IpadServiceType_Type.__name__ = "Integer32"
_IpadServiceType_Object = MibTableColumn
ipadServiceType = _IpadServiceType_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 2, 1, 1, 3),
    _IpadServiceType_Type()
)
ipadServiceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadServiceType.setStatus("current")
_IpadServicePair_Type = Integer32
_IpadServicePair_Object = MibTableColumn
ipadServicePair = _IpadServicePair_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 2, 1, 1, 4),
    _IpadServicePair_Type()
)
ipadServicePair.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadServicePair.setStatus("current")


class _IpadServiceStatus_Type(Integer32):
    """Custom type ipadServiceStatus based on Integer32"""
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
        *(("changed", 7),
          ("connecting", 9),
          ("dead", 6),
          ("down", 3),
          ("idle", 2),
          ("other", 1),
          ("physicalUp", 4),
          ("protocolUp", 5),
          ("training", 8))
    )


_IpadServiceStatus_Type.__name__ = "Integer32"
_IpadServiceStatus_Object = MibTableColumn
ipadServiceStatus = _IpadServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 2, 1, 1, 5),
    _IpadServiceStatus_Type()
)
ipadServiceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadServiceStatus.setStatus("current")


class _IpadServiceAddService_Type(Integer32):
    """Custom type ipadServiceAddService based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("addService", 1)
    )


_IpadServiceAddService_Type.__name__ = "Integer32"
_IpadServiceAddService_Object = MibScalar
ipadServiceAddService = _IpadServiceAddService_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 2, 2),
    _IpadServiceAddService_Type()
)
ipadServiceAddService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadServiceAddService.setStatus("current")
_IpadServiceDeleteService_Type = Integer32
_IpadServiceDeleteService_Object = MibScalar
ipadServiceDeleteService = _IpadServiceDeleteService_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 2, 3),
    _IpadServiceDeleteService_Type()
)
ipadServiceDeleteService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadServiceDeleteService.setStatus("current")
_IpadChannel_ObjectIdentity = ObjectIdentity
ipadChannel = _IpadChannel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 3)
)
_IpadChannelTable_Object = MibTable
ipadChannelTable = _IpadChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 3, 1)
)
if mibBuilder.loadTexts:
    ipadChannelTable.setStatus("current")
_IpadChannelTableEntry_Object = MibTableRow
ipadChannelTableEntry = _IpadChannelTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 3, 1, 1)
)
ipadChannelTableEntry.setIndexNames(
    (0, "IPADv2-MIB", "ipadChannelifIndex"),
    (0, "IPADv2-MIB", "ipadChannelIndex"),
)
if mibBuilder.loadTexts:
    ipadChannelTableEntry.setStatus("current")
_IpadChannelifIndex_Type = Integer32
_IpadChannelifIndex_Object = MibTableColumn
ipadChannelifIndex = _IpadChannelifIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 3, 1, 1, 1),
    _IpadChannelifIndex_Type()
)
ipadChannelifIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadChannelifIndex.setStatus("current")
_IpadChannelIndex_Type = Integer32
_IpadChannelIndex_Object = MibTableColumn
ipadChannelIndex = _IpadChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 3, 1, 1, 2),
    _IpadChannelIndex_Type()
)
ipadChannelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadChannelIndex.setStatus("current")
_IpadChannelService_Type = Integer32
_IpadChannelService_Object = MibTableColumn
ipadChannelService = _IpadChannelService_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 3, 1, 1, 3),
    _IpadChannelService_Type()
)
ipadChannelService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadChannelService.setStatus("current")
_IpadChannelPair_Type = Integer32
_IpadChannelPair_Object = MibTableColumn
ipadChannelPair = _IpadChannelPair_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 3, 1, 1, 4),
    _IpadChannelPair_Type()
)
ipadChannelPair.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadChannelPair.setStatus("current")


class _IpadChannelRate_Type(Integer32):
    """Custom type ipadChannelRate based on Integer32"""
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
        *(("other", 1),
          ("rate56", 2),
          ("rate64", 3),
          ("rate8", 4))
    )


_IpadChannelRate_Type.__name__ = "Integer32"
_IpadChannelRate_Object = MibTableColumn
ipadChannelRate = _IpadChannelRate_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 3, 1, 1, 5),
    _IpadChannelRate_Type()
)
ipadChannelRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadChannelRate.setStatus("current")
_IpadChannelIdlePattern_Type = Integer32
_IpadChannelIdlePattern_Object = MibTableColumn
ipadChannelIdlePattern = _IpadChannelIdlePattern_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 3, 1, 1, 6),
    _IpadChannelIdlePattern_Type()
)
ipadChannelIdlePattern.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadChannelIdlePattern.setStatus("current")
_IpadDLCI_ObjectIdentity = ObjectIdentity
ipadDLCI = _IpadDLCI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 4)
)
_IpadDLCITable_Object = MibTable
ipadDLCITable = _IpadDLCITable_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 4, 1)
)
if mibBuilder.loadTexts:
    ipadDLCITable.setStatus("current")
_IpadDLCITableEntry_Object = MibTableRow
ipadDLCITableEntry = _IpadDLCITableEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 4, 1, 1)
)
ipadDLCITableEntry.setIndexNames(
    (0, "IPADv2-MIB", "ipadDLCIservice"),
    (0, "IPADv2-MIB", "ipadDLCInumber"),
)
if mibBuilder.loadTexts:
    ipadDLCITableEntry.setStatus("current")
_IpadDLCIservice_Type = Integer32
_IpadDLCIservice_Object = MibTableColumn
ipadDLCIservice = _IpadDLCIservice_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 4, 1, 1, 1),
    _IpadDLCIservice_Type()
)
ipadDLCIservice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDLCIservice.setStatus("current")
_IpadDLCInumber_Type = Integer32
_IpadDLCInumber_Object = MibTableColumn
ipadDLCInumber = _IpadDLCInumber_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 4, 1, 1, 2),
    _IpadDLCInumber_Type()
)
ipadDLCInumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDLCInumber.setStatus("current")


class _IpadDLCIactive_Type(Integer32):
    """Custom type ipadDLCIactive based on Integer32"""
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
        *(("no", 2),
          ("other", 1),
          ("pending", 4),
          ("yes", 3))
    )


_IpadDLCIactive_Type.__name__ = "Integer32"
_IpadDLCIactive_Object = MibTableColumn
ipadDLCIactive = _IpadDLCIactive_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 4, 1, 1, 3),
    _IpadDLCIactive_Type()
)
ipadDLCIactive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDLCIactive.setStatus("current")


class _IpadDLCIcongestion_Type(Integer32):
    """Custom type ipadDLCIcongestion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("other", 1),
          ("yes", 3))
    )


_IpadDLCIcongestion_Type.__name__ = "Integer32"
_IpadDLCIcongestion_Object = MibTableColumn
ipadDLCIcongestion = _IpadDLCIcongestion_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 4, 1, 1, 4),
    _IpadDLCIcongestion_Type()
)
ipadDLCIcongestion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDLCIcongestion.setStatus("current")
_IpadDLCIremote_Type = Integer32
_IpadDLCIremote_Object = MibTableColumn
ipadDLCIremote = _IpadDLCIremote_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 4, 1, 1, 5),
    _IpadDLCIremote_Type()
)
ipadDLCIremote.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDLCIremote.setStatus("current")


class _IpadDLCIremoteUnit_Type(DisplayString):
    """Custom type ipadDLCIremoteUnit based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_IpadDLCIremoteUnit_Type.__name__ = "DisplayString"
_IpadDLCIremoteUnit_Object = MibTableColumn
ipadDLCIremoteUnit = _IpadDLCIremoteUnit_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 4, 1, 1, 6),
    _IpadDLCIremoteUnit_Type()
)
ipadDLCIremoteUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDLCIremoteUnit.setStatus("current")


class _IpadDLCIremoteEquipActive_Type(Integer32):
    """Custom type ipadDLCIremoteEquipActive based on Integer32"""
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
        *(("active", 3),
          ("inactive", 2),
          ("other", 1),
          ("sosAlarm", 4))
    )


_IpadDLCIremoteEquipActive_Type.__name__ = "Integer32"
_IpadDLCIremoteEquipActive_Object = MibTableColumn
ipadDLCIremoteEquipActive = _IpadDLCIremoteEquipActive_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 4, 1, 1, 7),
    _IpadDLCIremoteEquipActive_Type()
)
ipadDLCIremoteEquipActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDLCIremoteEquipActive.setStatus("current")


class _IpadDLCIencapsulation_Type(Integer32):
    """Custom type ipadDLCIencapsulation based on Integer32"""
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
        *(("other", 1),
          ("proprietary", 3),
          ("rfc1490", 2),
          ("rfc1490withCompression", 5),
          ("rfc1490withEncryption", 4))
    )


_IpadDLCIencapsulation_Type.__name__ = "Integer32"
_IpadDLCIencapsulation_Object = MibTableColumn
ipadDLCIencapsulation = _IpadDLCIencapsulation_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 4, 1, 1, 8),
    _IpadDLCIencapsulation_Type()
)
ipadDLCIencapsulation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadDLCIencapsulation.setStatus("current")


class _IpadDLCIproprietary_Type(Integer32):
    """Custom type ipadDLCIproprietary based on Integer32"""
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
        *(("ethertype", 4),
          ("ip", 2),
          ("ipx", 3),
          ("none", 5),
          ("other", 1))
    )


_IpadDLCIproprietary_Type.__name__ = "Integer32"
_IpadDLCIproprietary_Object = MibTableColumn
ipadDLCIproprietary = _IpadDLCIproprietary_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 4, 1, 1, 9),
    _IpadDLCIproprietary_Type()
)
ipadDLCIproprietary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadDLCIproprietary.setStatus("current")
_IpadDLCIpropOffset_Type = Integer32
_IpadDLCIpropOffset_Object = MibTableColumn
ipadDLCIpropOffset = _IpadDLCIpropOffset_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 4, 1, 1, 10),
    _IpadDLCIpropOffset_Type()
)
ipadDLCIpropOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadDLCIpropOffset.setStatus("current")


class _IpadDLCIinBand_Type(Integer32):
    """Custom type ipadDLCIinBand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("other", 1),
          ("yes", 3))
    )


_IpadDLCIinBand_Type.__name__ = "Integer32"
_IpadDLCIinBand_Object = MibTableColumn
ipadDLCIinBand = _IpadDLCIinBand_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 4, 1, 1, 11),
    _IpadDLCIinBand_Type()
)
ipadDLCIinBand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadDLCIinBand.setStatus("current")
_IpadDLCICIR_Type = Integer32
_IpadDLCICIR_Object = MibTableColumn
ipadDLCICIR = _IpadDLCICIR_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 4, 1, 1, 12),
    _IpadDLCICIR_Type()
)
ipadDLCICIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadDLCICIR.setStatus("current")
_IpadDLCIBe_Type = Integer32
_IpadDLCIBe_Object = MibTableColumn
ipadDLCIBe = _IpadDLCIBe_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 4, 1, 1, 13),
    _IpadDLCIBe_Type()
)
ipadDLCIBe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadDLCIBe.setStatus("current")
_IpadDLCIminBC_Type = Integer32
_IpadDLCIminBC_Object = MibTableColumn
ipadDLCIminBC = _IpadDLCIminBC_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 4, 1, 1, 14),
    _IpadDLCIminBC_Type()
)
ipadDLCIminBC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadDLCIminBC.setStatus("current")


class _IpadDLCIrxMon_Type(Integer32):
    """Custom type ipadDLCIrxMon based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("other", 1),
          ("yes", 3))
    )


_IpadDLCIrxMon_Type.__name__ = "Integer32"
_IpadDLCIrxMon_Object = MibTableColumn
ipadDLCIrxMon = _IpadDLCIrxMon_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 4, 1, 1, 15),
    _IpadDLCIrxMon_Type()
)
ipadDLCIrxMon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadDLCIrxMon.setStatus("current")


class _IpadDLCIdEctrl_Type(Integer32):
    """Custom type ipadDLCIdEctrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("other", 1),
          ("yes", 3))
    )


_IpadDLCIdEctrl_Type.__name__ = "Integer32"
_IpadDLCIdEctrl_Object = MibTableColumn
ipadDLCIdEctrl = _IpadDLCIdEctrl_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 4, 1, 1, 16),
    _IpadDLCIdEctrl_Type()
)
ipadDLCIdEctrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadDLCIdEctrl.setStatus("current")


class _IpadDLCIenableDelay_Type(Integer32):
    """Custom type ipadDLCIenableDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 3),
          ("other", 1))
    )


_IpadDLCIenableDelay_Type.__name__ = "Integer32"
_IpadDLCIenableDelay_Object = MibTableColumn
ipadDLCIenableDelay = _IpadDLCIenableDelay_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 4, 1, 1, 17),
    _IpadDLCIenableDelay_Type()
)
ipadDLCIenableDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadDLCIenableDelay.setStatus("current")
_IpadDLCItxExCIRThreshold_Type = Integer32
_IpadDLCItxExCIRThreshold_Object = MibTableColumn
ipadDLCItxExCIRThreshold = _IpadDLCItxExCIRThreshold_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 4, 1, 1, 18),
    _IpadDLCItxExCIRThreshold_Type()
)
ipadDLCItxExCIRThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadDLCItxExCIRThreshold.setStatus("current")


class _IpadDLCItxExCIRAlarm_Type(Integer32):
    """Custom type ipadDLCItxExCIRAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noAlarm", 2),
          ("other", 1),
          ("thresholdExceeded", 3))
    )


_IpadDLCItxExCIRAlarm_Type.__name__ = "Integer32"
_IpadDLCItxExCIRAlarm_Object = MibTableColumn
ipadDLCItxExCIRAlarm = _IpadDLCItxExCIRAlarm_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 4, 1, 1, 19),
    _IpadDLCItxExCIRAlarm_Type()
)
ipadDLCItxExCIRAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDLCItxExCIRAlarm.setStatus("current")
_IpadDLCItxExBeThreshold_Type = Integer32
_IpadDLCItxExBeThreshold_Object = MibTableColumn
ipadDLCItxExBeThreshold = _IpadDLCItxExBeThreshold_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 4, 1, 1, 20),
    _IpadDLCItxExBeThreshold_Type()
)
ipadDLCItxExBeThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadDLCItxExBeThreshold.setStatus("current")


class _IpadDLCItxExBeAlarm_Type(Integer32):
    """Custom type ipadDLCItxExBeAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noAlarm", 2),
          ("other", 1),
          ("thresholdExceeded", 3))
    )


_IpadDLCItxExBeAlarm_Type.__name__ = "Integer32"
_IpadDLCItxExBeAlarm_Object = MibTableColumn
ipadDLCItxExBeAlarm = _IpadDLCItxExBeAlarm_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 4, 1, 1, 21),
    _IpadDLCItxExBeAlarm_Type()
)
ipadDLCItxExBeAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDLCItxExBeAlarm.setStatus("current")
_IpadDLCIrxCongThreshold_Type = Integer32
_IpadDLCIrxCongThreshold_Object = MibTableColumn
ipadDLCIrxCongThreshold = _IpadDLCIrxCongThreshold_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 4, 1, 1, 22),
    _IpadDLCIrxCongThreshold_Type()
)
ipadDLCIrxCongThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadDLCIrxCongThreshold.setStatus("current")


class _IpadDLCIrxCongAlarm_Type(Integer32):
    """Custom type ipadDLCIrxCongAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noAlarm", 2),
          ("other", 1),
          ("thresholdExceeded", 3))
    )


_IpadDLCIrxCongAlarm_Type.__name__ = "Integer32"
_IpadDLCIrxCongAlarm_Object = MibTableColumn
ipadDLCIrxCongAlarm = _IpadDLCIrxCongAlarm_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 4, 1, 1, 23),
    _IpadDLCIrxCongAlarm_Type()
)
ipadDLCIrxCongAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDLCIrxCongAlarm.setStatus("current")


class _IpadDLCIrxBECNinCIR_Type(Integer32):
    """Custom type ipadDLCIrxBECNinCIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alarmCondition", 3),
          ("noAlarm", 2),
          ("other", 1))
    )


_IpadDLCIrxBECNinCIR_Type.__name__ = "Integer32"
_IpadDLCIrxBECNinCIR_Object = MibTableColumn
ipadDLCIrxBECNinCIR = _IpadDLCIrxBECNinCIR_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 4, 1, 1, 24),
    _IpadDLCIrxBECNinCIR_Type()
)
ipadDLCIrxBECNinCIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDLCIrxBECNinCIR.setStatus("current")
_IpadDLCIUASThreshold_Type = Integer32
_IpadDLCIUASThreshold_Object = MibTableColumn
ipadDLCIUASThreshold = _IpadDLCIUASThreshold_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 4, 1, 1, 25),
    _IpadDLCIUASThreshold_Type()
)
ipadDLCIUASThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadDLCIUASThreshold.setStatus("current")


class _IpadDLCIUASAlarm_Type(Integer32):
    """Custom type ipadDLCIUASAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noAlarm", 2),
          ("other", 1),
          ("thresholdExceeded", 3))
    )


_IpadDLCIUASAlarm_Type.__name__ = "Integer32"
_IpadDLCIUASAlarm_Object = MibTableColumn
ipadDLCIUASAlarm = _IpadDLCIUASAlarm_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 4, 1, 1, 26),
    _IpadDLCIUASAlarm_Type()
)
ipadDLCIUASAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDLCIUASAlarm.setStatus("current")


class _IpadDLCIAlarmReset_Type(Integer32):
    """Custom type ipadDLCIAlarmReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dlciAlarmResetClearAlarms", 2),
          ("dlciAlarmResetClearStats", 3),
          ("dlciAlarmResetOther", 1))
    )


_IpadDLCIAlarmReset_Type.__name__ = "Integer32"
_IpadDLCIAlarmReset_Object = MibTableColumn
ipadDLCIAlarmReset = _IpadDLCIAlarmReset_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 4, 1, 1, 27),
    _IpadDLCIAlarmReset_Type()
)
ipadDLCIAlarmReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadDLCIAlarmReset.setStatus("current")


class _IpadDLCIRoundTripDelaySize_Type(Integer32):
    """Custom type ipadDLCIRoundTripDelaySize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1500),
    )


_IpadDLCIRoundTripDelaySize_Type.__name__ = "Integer32"
_IpadDLCIRoundTripDelaySize_Object = MibTableColumn
ipadDLCIRoundTripDelaySize = _IpadDLCIRoundTripDelaySize_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 4, 1, 1, 28),
    _IpadDLCIRoundTripDelaySize_Type()
)
ipadDLCIRoundTripDelaySize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadDLCIRoundTripDelaySize.setStatus("current")


class _IpadDLCIRoundTripDelayRate_Type(Integer32):
    """Custom type ipadDLCIRoundTripDelayRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 900),
    )


_IpadDLCIRoundTripDelayRate_Type.__name__ = "Integer32"
_IpadDLCIRoundTripDelayRate_Object = MibTableColumn
ipadDLCIRoundTripDelayRate = _IpadDLCIRoundTripDelayRate_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 4, 1, 1, 29),
    _IpadDLCIRoundTripDelayRate_Type()
)
ipadDLCIRoundTripDelayRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadDLCIRoundTripDelayRate.setStatus("current")
_IpadDLCIRemoteFramesOfferedWithinCIR_Type = Integer32
_IpadDLCIRemoteFramesOfferedWithinCIR_Object = MibTableColumn
ipadDLCIRemoteFramesOfferedWithinCIR = _IpadDLCIRemoteFramesOfferedWithinCIR_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 4, 1, 1, 30),
    _IpadDLCIRemoteFramesOfferedWithinCIR_Type()
)
ipadDLCIRemoteFramesOfferedWithinCIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDLCIRemoteFramesOfferedWithinCIR.setStatus("current")
_IpadDLCIRemoteFramesOfferedWithinBE_Type = Integer32
_IpadDLCIRemoteFramesOfferedWithinBE_Object = MibTableColumn
ipadDLCIRemoteFramesOfferedWithinBE = _IpadDLCIRemoteFramesOfferedWithinBE_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 4, 1, 1, 31),
    _IpadDLCIRemoteFramesOfferedWithinBE_Type()
)
ipadDLCIRemoteFramesOfferedWithinBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDLCIRemoteFramesOfferedWithinBE.setStatus("current")
_IpadDLCIFramesReceived_Type = Integer32
_IpadDLCIFramesReceived_Object = MibTableColumn
ipadDLCIFramesReceived = _IpadDLCIFramesReceived_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 4, 1, 1, 32),
    _IpadDLCIFramesReceived_Type()
)
ipadDLCIFramesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDLCIFramesReceived.setStatus("current")
_IpadDLCIRemoteDataOfferedWithinCIR_Type = Integer32
_IpadDLCIRemoteDataOfferedWithinCIR_Object = MibTableColumn
ipadDLCIRemoteDataOfferedWithinCIR = _IpadDLCIRemoteDataOfferedWithinCIR_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 4, 1, 1, 33),
    _IpadDLCIRemoteDataOfferedWithinCIR_Type()
)
ipadDLCIRemoteDataOfferedWithinCIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDLCIRemoteDataOfferedWithinCIR.setStatus("current")
_IpadDLCIRemoteDataOfferedWithinBE_Type = Integer32
_IpadDLCIRemoteDataOfferedWithinBE_Object = MibTableColumn
ipadDLCIRemoteDataOfferedWithinBE = _IpadDLCIRemoteDataOfferedWithinBE_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 4, 1, 1, 34),
    _IpadDLCIRemoteDataOfferedWithinBE_Type()
)
ipadDLCIRemoteDataOfferedWithinBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDLCIRemoteDataOfferedWithinBE.setStatus("current")
_IpadDLCIDataReceived_Type = Integer32
_IpadDLCIDataReceived_Object = MibTableColumn
ipadDLCIDataReceived = _IpadDLCIDataReceived_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 4, 1, 1, 35),
    _IpadDLCIDataReceived_Type()
)
ipadDLCIDataReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDLCIDataReceived.setStatus("current")
_IpadDLCIRemoteIPAddress_Type = IpAddress
_IpadDLCIRemoteIPAddress_Object = MibTableColumn
ipadDLCIRemoteIPAddress = _IpadDLCIRemoteIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 4, 1, 1, 36),
    _IpadDLCIRemoteIPAddress_Type()
)
ipadDLCIRemoteIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDLCIRemoteIPAddress.setStatus("current")


class _IpadDLCICompressionStatus_Type(Integer32):
    """Custom type ipadDLCICompressionStatus based on Integer32"""
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
          ("enabledAndNegotiated", 3),
          ("enabledButNotNegotiated", 4),
          ("other", 1))
    )


_IpadDLCICompressionStatus_Type.__name__ = "Integer32"
_IpadDLCICompressionStatus_Object = MibTableColumn
ipadDLCICompressionStatus = _IpadDLCICompressionStatus_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 4, 1, 1, 37),
    _IpadDLCICompressionStatus_Type()
)
ipadDLCICompressionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDLCICompressionStatus.setStatus("current")
_IpadDLCICompressionTxOctetsIn_Type = Integer32
_IpadDLCICompressionTxOctetsIn_Object = MibTableColumn
ipadDLCICompressionTxOctetsIn = _IpadDLCICompressionTxOctetsIn_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 4, 1, 1, 38),
    _IpadDLCICompressionTxOctetsIn_Type()
)
ipadDLCICompressionTxOctetsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDLCICompressionTxOctetsIn.setStatus("current")
_IpadDLCICompressionTxOctetsOut_Type = Integer32
_IpadDLCICompressionTxOctetsOut_Object = MibTableColumn
ipadDLCICompressionTxOctetsOut = _IpadDLCICompressionTxOctetsOut_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 4, 1, 1, 39),
    _IpadDLCICompressionTxOctetsOut_Type()
)
ipadDLCICompressionTxOctetsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDLCICompressionTxOctetsOut.setStatus("current")
_IpadDLCICompressionRxOctetsIn_Type = Integer32
_IpadDLCICompressionRxOctetsIn_Object = MibTableColumn
ipadDLCICompressionRxOctetsIn = _IpadDLCICompressionRxOctetsIn_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 4, 1, 1, 40),
    _IpadDLCICompressionRxOctetsIn_Type()
)
ipadDLCICompressionRxOctetsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDLCICompressionRxOctetsIn.setStatus("current")
_IpadDLCICompressionRxOctetsOut_Type = Integer32
_IpadDLCICompressionRxOctetsOut_Object = MibTableColumn
ipadDLCICompressionRxOctetsOut = _IpadDLCICompressionRxOctetsOut_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 4, 1, 1, 41),
    _IpadDLCICompressionRxOctetsOut_Type()
)
ipadDLCICompressionRxOctetsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDLCICompressionRxOctetsOut.setStatus("current")
_IpadDLCILastChange_Type = TimeTicks
_IpadDLCILastChange_Object = MibScalar
ipadDLCILastChange = _IpadDLCILastChange_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 4, 2),
    _IpadDLCILastChange_Type()
)
ipadDLCILastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDLCILastChange.setStatus("current")
_IpadEndpoint_ObjectIdentity = ObjectIdentity
ipadEndpoint = _IpadEndpoint_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 5)
)
_IpadEndpointTable_Object = MibTable
ipadEndpointTable = _IpadEndpointTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 5, 1)
)
if mibBuilder.loadTexts:
    ipadEndpointTable.setStatus("current")
_IpadEndpointTableEntry_Object = MibTableRow
ipadEndpointTableEntry = _IpadEndpointTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 5, 1, 1)
)
ipadEndpointTableEntry.setIndexNames(
    (0, "IPADv2-MIB", "ipadEndpointIndex"),
)
if mibBuilder.loadTexts:
    ipadEndpointTableEntry.setStatus("current")
_IpadEndpointIndex_Type = Integer32
_IpadEndpointIndex_Object = MibTableColumn
ipadEndpointIndex = _IpadEndpointIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 5, 1, 1, 1),
    _IpadEndpointIndex_Type()
)
ipadEndpointIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadEndpointIndex.setStatus("current")


class _IpadEndpointName_Type(DisplayString):
    """Custom type ipadEndpointName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_IpadEndpointName_Type.__name__ = "DisplayString"
_IpadEndpointName_Object = MibTableColumn
ipadEndpointName = _IpadEndpointName_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 5, 1, 1, 2),
    _IpadEndpointName_Type()
)
ipadEndpointName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadEndpointName.setStatus("current")
_IpadEndpointService_Type = Integer32
_IpadEndpointService_Object = MibTableColumn
ipadEndpointService = _IpadEndpointService_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 5, 1, 1, 3),
    _IpadEndpointService_Type()
)
ipadEndpointService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadEndpointService.setStatus("current")
_IpadEndpointDLCInumber_Type = Integer32
_IpadEndpointDLCInumber_Object = MibTableColumn
ipadEndpointDLCInumber = _IpadEndpointDLCInumber_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 5, 1, 1, 4),
    _IpadEndpointDLCInumber_Type()
)
ipadEndpointDLCInumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadEndpointDLCInumber.setStatus("current")


class _IpadEndpointType_Type(Integer32):
    """Custom type ipadEndpointType based on Integer32"""
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
        *(("frLocal", 2),
          ("frSwitched", 3),
          ("ipRoute", 4),
          ("other", 1))
    )


_IpadEndpointType_Type.__name__ = "Integer32"
_IpadEndpointType_Object = MibTableColumn
ipadEndpointType = _IpadEndpointType_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 5, 1, 1, 5),
    _IpadEndpointType_Type()
)
ipadEndpointType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadEndpointType.setStatus("current")
_IpadEndpointForward_Type = Integer32
_IpadEndpointForward_Object = MibTableColumn
ipadEndpointForward = _IpadEndpointForward_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 5, 1, 1, 6),
    _IpadEndpointForward_Type()
)
ipadEndpointForward.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadEndpointForward.setStatus("current")
_IpadEndpointBackup_Type = Integer32
_IpadEndpointBackup_Object = MibTableColumn
ipadEndpointBackup = _IpadEndpointBackup_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 5, 1, 1, 7),
    _IpadEndpointBackup_Type()
)
ipadEndpointBackup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadEndpointBackup.setStatus("current")
_IpadEndpointRefSLP_Type = Integer32
_IpadEndpointRefSLP_Object = MibTableColumn
ipadEndpointRefSLP = _IpadEndpointRefSLP_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 5, 1, 1, 8),
    _IpadEndpointRefSLP_Type()
)
ipadEndpointRefSLP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadEndpointRefSLP.setStatus("current")
_IpadEndpointRemoteIpAddr_Type = IpAddress
_IpadEndpointRemoteIpAddr_Object = MibTableColumn
ipadEndpointRemoteIpAddr = _IpadEndpointRemoteIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 5, 1, 1, 9),
    _IpadEndpointRemoteIpAddr_Type()
)
ipadEndpointRemoteIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadEndpointRemoteIpAddr.setStatus("current")
_IpadEndpointRemoteIpMask_Type = IpAddress
_IpadEndpointRemoteIpMask_Object = MibTableColumn
ipadEndpointRemoteIpMask = _IpadEndpointRemoteIpMask_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 5, 1, 1, 10),
    _IpadEndpointRemoteIpMask_Type()
)
ipadEndpointRemoteIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadEndpointRemoteIpMask.setStatus("current")


class _IpadEndpointAddEndpoint_Type(DisplayString):
    """Custom type ipadEndpointAddEndpoint based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_IpadEndpointAddEndpoint_Type.__name__ = "DisplayString"
_IpadEndpointAddEndpoint_Object = MibScalar
ipadEndpointAddEndpoint = _IpadEndpointAddEndpoint_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 5, 2),
    _IpadEndpointAddEndpoint_Type()
)
ipadEndpointAddEndpoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadEndpointAddEndpoint.setStatus("current")


class _IpadEndpointDeleteEndpoint_Type(DisplayString):
    """Custom type ipadEndpointDeleteEndpoint based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_IpadEndpointDeleteEndpoint_Type.__name__ = "DisplayString"
_IpadEndpointDeleteEndpoint_Object = MibScalar
ipadEndpointDeleteEndpoint = _IpadEndpointDeleteEndpoint_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 5, 3),
    _IpadEndpointDeleteEndpoint_Type()
)
ipadEndpointDeleteEndpoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadEndpointDeleteEndpoint.setStatus("current")
_IpadEndpointLastChange_Type = TimeTicks
_IpadEndpointLastChange_Object = MibScalar
ipadEndpointLastChange = _IpadEndpointLastChange_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 5, 4),
    _IpadEndpointLastChange_Type()
)
ipadEndpointLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadEndpointLastChange.setStatus("current")
_IpadUser_ObjectIdentity = ObjectIdentity
ipadUser = _IpadUser_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 6)
)
_IpadUserTable_Object = MibTable
ipadUserTable = _IpadUserTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 6, 1)
)
if mibBuilder.loadTexts:
    ipadUserTable.setStatus("current")
_IpadUserTableEntry_Object = MibTableRow
ipadUserTableEntry = _IpadUserTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 6, 1, 1)
)
ipadUserTableEntry.setIndexNames(
    (0, "IPADv2-MIB", "ipadUserIndex"),
)
if mibBuilder.loadTexts:
    ipadUserTableEntry.setStatus("current")
_IpadUserIndex_Type = Integer32
_IpadUserIndex_Object = MibTableColumn
ipadUserIndex = _IpadUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 6, 1, 1, 1),
    _IpadUserIndex_Type()
)
ipadUserIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadUserIndex.setStatus("current")


class _IpadUserFilterByDLCI_Type(Integer32):
    """Custom type ipadUserFilterByDLCI based on Integer32"""
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


_IpadUserFilterByDLCI_Type.__name__ = "Integer32"
_IpadUserFilterByDLCI_Object = MibTableColumn
ipadUserFilterByDLCI = _IpadUserFilterByDLCI_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 6, 1, 1, 2),
    _IpadUserFilterByDLCI_Type()
)
ipadUserFilterByDLCI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadUserFilterByDLCI.setStatus("current")
_IpadUserService_Type = Integer32
_IpadUserService_Object = MibTableColumn
ipadUserService = _IpadUserService_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 6, 1, 1, 3),
    _IpadUserService_Type()
)
ipadUserService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadUserService.setStatus("current")
_IpadUserDLCI_Type = Integer32
_IpadUserDLCI_Object = MibTableColumn
ipadUserDLCI = _IpadUserDLCI_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 6, 1, 1, 4),
    _IpadUserDLCI_Type()
)
ipadUserDLCI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadUserDLCI.setStatus("current")


class _IpadUserFilterByIPAddress_Type(Integer32):
    """Custom type ipadUserFilterByIPAddress based on Integer32"""
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


_IpadUserFilterByIPAddress_Type.__name__ = "Integer32"
_IpadUserFilterByIPAddress_Object = MibTableColumn
ipadUserFilterByIPAddress = _IpadUserFilterByIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 6, 1, 1, 5),
    _IpadUserFilterByIPAddress_Type()
)
ipadUserFilterByIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadUserFilterByIPAddress.setStatus("current")
_IpadUserIPAddress_Type = IpAddress
_IpadUserIPAddress_Object = MibTableColumn
ipadUserIPAddress = _IpadUserIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 6, 1, 1, 6),
    _IpadUserIPAddress_Type()
)
ipadUserIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadUserIPAddress.setStatus("current")
_IpadUserIPMask_Type = IpAddress
_IpadUserIPMask_Object = MibTableColumn
ipadUserIPMask = _IpadUserIPMask_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 6, 1, 1, 7),
    _IpadUserIPMask_Type()
)
ipadUserIPMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadUserIPMask.setStatus("current")


class _IpadUserFilterByIPPort_Type(Integer32):
    """Custom type ipadUserFilterByIPPort based on Integer32"""
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


_IpadUserFilterByIPPort_Type.__name__ = "Integer32"
_IpadUserFilterByIPPort_Object = MibTableColumn
ipadUserFilterByIPPort = _IpadUserFilterByIPPort_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 6, 1, 1, 8),
    _IpadUserFilterByIPPort_Type()
)
ipadUserFilterByIPPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadUserFilterByIPPort.setStatus("current")


class _IpadUserIPPort_Type(Integer32):
    """Custom type ipadUserIPPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              7,
              11,
              17,
              20,
              21,
              23,
              25,
              31,
              37,
              42,
              53,
              66,
              69,
              70,
              79,
              80,
              88,
              92,
              101,
              107,
              109,
              110,
              111,
              113,
              119,
              137,
              138,
              139,
              153,
              161,
              162,
              163,
              164,
              169,
              179,
              194,
              201,
              202,
              204,
              206,
              213,
              395,
              396,
              444,
              494,
              533,
              540,
              541,
              600,
              749)
        )
    )
    namedValues = NamedValues(
        *(("atecho", 204),
          ("atnbp", 202),
          ("atrtmp", 201),
          ("atzis", 206),
          ("auth", 113),
          ("bgp", 179),
          ("cmipagent", 164),
          ("cmipman", 163),
          ("domain", 53),
          ("echo", 7),
          ("finger", 79),
          ("ftp", 21),
          ("ftpdata", 20),
          ("gopher", 70),
          ("hostname", 101),
          ("http", 80),
          ("ipcserver", 600),
          ("ipx", 213),
          ("irc", 194),
          ("kerberos", 88),
          ("kerberosadm", 749),
          ("msgauth", 31),
          ("nameserver", 42),
          ("netbiosdgm", 138),
          ("netbiosns", 137),
          ("netbiosssn", 139),
          ("netcp", 395),
          ("netwall", 533),
          ("netwareip", 396),
          ("nntp", 119),
          ("npp", 92),
          ("pop2", 109),
          ("pop3", 110),
          ("povray", 494),
          ("qotd", 17),
          ("rje", 5),
          ("rtelnet", 107),
          ("send", 169),
          ("sgmp", 153),
          ("smtp", 25),
          ("snmp", 161),
          ("snmptrap", 162),
          ("snpp", 444),
          ("sqlnet", 66),
          ("sunrpc", 111),
          ("systat", 11),
          ("telnet", 23),
          ("tftp", 69),
          ("time", 37),
          ("uucp", 540),
          ("uucprlogin", 541))
    )


_IpadUserIPPort_Type.__name__ = "Integer32"
_IpadUserIPPort_Object = MibTableColumn
ipadUserIPPort = _IpadUserIPPort_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 6, 1, 1, 9),
    _IpadUserIPPort_Type()
)
ipadUserIPPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadUserIPPort.setStatus("current")
_IpadUserTxAlmThreshold_Type = Integer32
_IpadUserTxAlmThreshold_Object = MibTableColumn
ipadUserTxAlmThreshold = _IpadUserTxAlmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 6, 1, 1, 10),
    _IpadUserTxAlmThreshold_Type()
)
ipadUserTxAlmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadUserTxAlmThreshold.setStatus("current")


class _IpadUserTxAlmAlarm_Type(Integer32):
    """Custom type ipadUserTxAlmAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noAlarm", 2),
          ("other", 1),
          ("thresholdExceeded", 3))
    )


_IpadUserTxAlmAlarm_Type.__name__ = "Integer32"
_IpadUserTxAlmAlarm_Object = MibTableColumn
ipadUserTxAlmAlarm = _IpadUserTxAlmAlarm_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 6, 1, 1, 11),
    _IpadUserTxAlmAlarm_Type()
)
ipadUserTxAlmAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadUserTxAlmAlarm.setStatus("current")


class _IpadUserAlarmReset_Type(Integer32):
    """Custom type ipadUserAlarmReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("userAlarmResetClearAlarms", 2),
          ("userAlarmResetClearStats", 3),
          ("userAlarmResetOther", 1))
    )


_IpadUserAlarmReset_Type.__name__ = "Integer32"
_IpadUserAlarmReset_Object = MibTableColumn
ipadUserAlarmReset = _IpadUserAlarmReset_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 6, 1, 1, 12),
    _IpadUserAlarmReset_Type()
)
ipadUserAlarmReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadUserAlarmReset.setStatus("current")
_IpadUserVpi_Type = Integer32
_IpadUserVpi_Object = MibTableColumn
ipadUserVpi = _IpadUserVpi_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 6, 1, 1, 13),
    _IpadUserVpi_Type()
)
ipadUserVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadUserVpi.setStatus("current")
_IpadUserVci_Type = Integer32
_IpadUserVci_Object = MibTableColumn
ipadUserVci = _IpadUserVci_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 6, 1, 1, 14),
    _IpadUserVci_Type()
)
ipadUserVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadUserVci.setStatus("current")


class _IpadUserFilterByVpiVci_Type(Integer32):
    """Custom type ipadUserFilterByVpiVci based on Integer32"""
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


_IpadUserFilterByVpiVci_Type.__name__ = "Integer32"
_IpadUserFilterByVpiVci_Object = MibTableColumn
ipadUserFilterByVpiVci = _IpadUserFilterByVpiVci_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 6, 1, 1, 15),
    _IpadUserFilterByVpiVci_Type()
)
ipadUserFilterByVpiVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadUserFilterByVpiVci.setStatus("current")
_IpadUserIPStatTimeRemaining_Type = Integer32
_IpadUserIPStatTimeRemaining_Object = MibScalar
ipadUserIPStatTimeRemaining = _IpadUserIPStatTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 6, 2),
    _IpadUserIPStatTimeRemaining_Type()
)
ipadUserIPStatTimeRemaining.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadUserIPStatTimeRemaining.setStatus("current")
_IpadUserIPStatTimeDuration_Type = Integer32
_IpadUserIPStatTimeDuration_Object = MibScalar
ipadUserIPStatTimeDuration = _IpadUserIPStatTimeDuration_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 6, 3),
    _IpadUserIPStatTimeDuration_Type()
)
ipadUserIPStatTimeDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadUserIPStatTimeDuration.setStatus("current")
_IpadUserIPStatStartTime_Type = TimeTicks
_IpadUserIPStatStartTime_Object = MibScalar
ipadUserIPStatStartTime = _IpadUserIPStatStartTime_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 6, 4),
    _IpadUserIPStatStartTime_Type()
)
ipadUserIPStatStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadUserIPStatStartTime.setStatus("current")
_IpadUserIPStatRequestedReportSize_Type = Integer32
_IpadUserIPStatRequestedReportSize_Object = MibScalar
ipadUserIPStatRequestedReportSize = _IpadUserIPStatRequestedReportSize_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 6, 5),
    _IpadUserIPStatRequestedReportSize_Type()
)
ipadUserIPStatRequestedReportSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadUserIPStatRequestedReportSize.setStatus("current")
_IpadUserIPStatGrantedReportSize_Type = Integer32
_IpadUserIPStatGrantedReportSize_Object = MibScalar
ipadUserIPStatGrantedReportSize = _IpadUserIPStatGrantedReportSize_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 6, 6),
    _IpadUserIPStatGrantedReportSize_Type()
)
ipadUserIPStatGrantedReportSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadUserIPStatGrantedReportSize.setStatus("current")
_IpadUserIPStatReportNumber_Type = Integer32
_IpadUserIPStatReportNumber_Object = MibScalar
ipadUserIPStatReportNumber = _IpadUserIPStatReportNumber_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 6, 7),
    _IpadUserIPStatReportNumber_Type()
)
ipadUserIPStatReportNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadUserIPStatReportNumber.setStatus("current")


class _IpadUserIPStatDiscardType_Type(Integer32):
    """Custom type ipadUserIPStatDiscardType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("byFrames", 2),
          ("byOctets", 3),
          ("byTime", 1))
    )


_IpadUserIPStatDiscardType_Type.__name__ = "Integer32"
_IpadUserIPStatDiscardType_Object = MibScalar
ipadUserIPStatDiscardType = _IpadUserIPStatDiscardType_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 6, 8),
    _IpadUserIPStatDiscardType_Type()
)
ipadUserIPStatDiscardType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadUserIPStatDiscardType.setStatus("current")
_IpadPPP_ObjectIdentity = ObjectIdentity
ipadPPP = _IpadPPP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 7)
)
_IpadPPPCfgTable_Object = MibTable
ipadPPPCfgTable = _IpadPPPCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 1)
)
if mibBuilder.loadTexts:
    ipadPPPCfgTable.setStatus("current")
_IpadPPPCfgTableEntry_Object = MibTableRow
ipadPPPCfgTableEntry = _IpadPPPCfgTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 1, 1)
)
ipadPPPCfgTableEntry.setIndexNames(
    (0, "IPADv2-MIB", "ipadPPPCfgService"),
)
if mibBuilder.loadTexts:
    ipadPPPCfgTableEntry.setStatus("current")
_IpadPPPCfgService_Type = Integer32
_IpadPPPCfgService_Object = MibTableColumn
ipadPPPCfgService = _IpadPPPCfgService_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 1, 1, 1),
    _IpadPPPCfgService_Type()
)
ipadPPPCfgService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadPPPCfgService.setStatus("current")


class _IpadPPPCfgDialMode_Type(Integer32):
    """Custom type ipadPPPCfgDialMode based on Integer32"""
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
        *(("demanddial", 4),
          ("dialup", 3),
          ("direct", 2),
          ("other", 1))
    )


_IpadPPPCfgDialMode_Type.__name__ = "Integer32"
_IpadPPPCfgDialMode_Object = MibTableColumn
ipadPPPCfgDialMode = _IpadPPPCfgDialMode_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 1, 1, 2),
    _IpadPPPCfgDialMode_Type()
)
ipadPPPCfgDialMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadPPPCfgDialMode.setStatus("current")
_IpadPPPCfgInactivityTimer_Type = Integer32
_IpadPPPCfgInactivityTimer_Object = MibTableColumn
ipadPPPCfgInactivityTimer = _IpadPPPCfgInactivityTimer_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 1, 1, 3),
    _IpadPPPCfgInactivityTimer_Type()
)
ipadPPPCfgInactivityTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadPPPCfgInactivityTimer.setStatus("current")


class _IpadPPPCfgNegotiationInit_Type(Integer32):
    """Custom type ipadPPPCfgNegotiationInit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("other", 1),
          ("yes", 3))
    )


_IpadPPPCfgNegotiationInit_Type.__name__ = "Integer32"
_IpadPPPCfgNegotiationInit_Object = MibTableColumn
ipadPPPCfgNegotiationInit = _IpadPPPCfgNegotiationInit_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 1, 1, 4),
    _IpadPPPCfgNegotiationInit_Type()
)
ipadPPPCfgNegotiationInit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadPPPCfgNegotiationInit.setStatus("current")
_IpadPPPCfgMRU_Type = Integer32
_IpadPPPCfgMRU_Object = MibTableColumn
ipadPPPCfgMRU = _IpadPPPCfgMRU_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 1, 1, 5),
    _IpadPPPCfgMRU_Type()
)
ipadPPPCfgMRU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadPPPCfgMRU.setStatus("current")
_IpadPPPCfgACCM_Type = Integer32
_IpadPPPCfgACCM_Object = MibTableColumn
ipadPPPCfgACCM = _IpadPPPCfgACCM_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 1, 1, 6),
    _IpadPPPCfgACCM_Type()
)
ipadPPPCfgACCM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadPPPCfgACCM.setStatus("current")


class _IpadPPPCfgNegMRU_Type(Integer32):
    """Custom type ipadPPPCfgNegMRU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("other", 1),
          ("yes", 3))
    )


_IpadPPPCfgNegMRU_Type.__name__ = "Integer32"
_IpadPPPCfgNegMRU_Object = MibTableColumn
ipadPPPCfgNegMRU = _IpadPPPCfgNegMRU_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 1, 1, 7),
    _IpadPPPCfgNegMRU_Type()
)
ipadPPPCfgNegMRU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadPPPCfgNegMRU.setStatus("current")


class _IpadPPPCfgNegACCM_Type(Integer32):
    """Custom type ipadPPPCfgNegACCM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("other", 1),
          ("yes", 3))
    )


_IpadPPPCfgNegACCM_Type.__name__ = "Integer32"
_IpadPPPCfgNegACCM_Object = MibTableColumn
ipadPPPCfgNegACCM = _IpadPPPCfgNegACCM_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 1, 1, 8),
    _IpadPPPCfgNegACCM_Type()
)
ipadPPPCfgNegACCM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadPPPCfgNegACCM.setStatus("current")


class _IpadPPPCfgNegMagic_Type(Integer32):
    """Custom type ipadPPPCfgNegMagic based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("other", 1),
          ("yes", 3))
    )


_IpadPPPCfgNegMagic_Type.__name__ = "Integer32"
_IpadPPPCfgNegMagic_Object = MibTableColumn
ipadPPPCfgNegMagic = _IpadPPPCfgNegMagic_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 1, 1, 9),
    _IpadPPPCfgNegMagic_Type()
)
ipadPPPCfgNegMagic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadPPPCfgNegMagic.setStatus("current")


class _IpadPPPCfgNegCompression_Type(Integer32):
    """Custom type ipadPPPCfgNegCompression based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("other", 1),
          ("yes", 3))
    )


_IpadPPPCfgNegCompression_Type.__name__ = "Integer32"
_IpadPPPCfgNegCompression_Object = MibTableColumn
ipadPPPCfgNegCompression = _IpadPPPCfgNegCompression_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 1, 1, 10),
    _IpadPPPCfgNegCompression_Type()
)
ipadPPPCfgNegCompression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadPPPCfgNegCompression.setStatus("current")


class _IpadPPPCfgNegAddress_Type(Integer32):
    """Custom type ipadPPPCfgNegAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("other", 1),
          ("yes", 3))
    )


_IpadPPPCfgNegAddress_Type.__name__ = "Integer32"
_IpadPPPCfgNegAddress_Object = MibTableColumn
ipadPPPCfgNegAddress = _IpadPPPCfgNegAddress_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 1, 1, 11),
    _IpadPPPCfgNegAddress_Type()
)
ipadPPPCfgNegAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadPPPCfgNegAddress.setStatus("current")


class _IpadPPPCfgNegPAP_Type(Integer32):
    """Custom type ipadPPPCfgNegPAP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("other", 1),
          ("yes", 3))
    )


_IpadPPPCfgNegPAP_Type.__name__ = "Integer32"
_IpadPPPCfgNegPAP_Object = MibTableColumn
ipadPPPCfgNegPAP = _IpadPPPCfgNegPAP_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 1, 1, 12),
    _IpadPPPCfgNegPAP_Type()
)
ipadPPPCfgNegPAP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadPPPCfgNegPAP.setStatus("current")


class _IpadPPPCfgNegCHAP_Type(Integer32):
    """Custom type ipadPPPCfgNegCHAP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("other", 1),
          ("yes", 3))
    )


_IpadPPPCfgNegCHAP_Type.__name__ = "Integer32"
_IpadPPPCfgNegCHAP_Object = MibTableColumn
ipadPPPCfgNegCHAP = _IpadPPPCfgNegCHAP_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 1, 1, 13),
    _IpadPPPCfgNegCHAP_Type()
)
ipadPPPCfgNegCHAP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadPPPCfgNegCHAP.setStatus("current")


class _IpadPPPCfgAllowPAP_Type(Integer32):
    """Custom type ipadPPPCfgAllowPAP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("other", 1),
          ("yes", 3))
    )


_IpadPPPCfgAllowPAP_Type.__name__ = "Integer32"
_IpadPPPCfgAllowPAP_Object = MibTableColumn
ipadPPPCfgAllowPAP = _IpadPPPCfgAllowPAP_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 1, 1, 14),
    _IpadPPPCfgAllowPAP_Type()
)
ipadPPPCfgAllowPAP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadPPPCfgAllowPAP.setStatus("current")


class _IpadPPPCfgAllowCHAP_Type(Integer32):
    """Custom type ipadPPPCfgAllowCHAP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("other", 1),
          ("yes", 3))
    )


_IpadPPPCfgAllowCHAP_Type.__name__ = "Integer32"
_IpadPPPCfgAllowCHAP_Object = MibTableColumn
ipadPPPCfgAllowCHAP = _IpadPPPCfgAllowCHAP_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 1, 1, 15),
    _IpadPPPCfgAllowCHAP_Type()
)
ipadPPPCfgAllowCHAP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadPPPCfgAllowCHAP.setStatus("current")


class _IpadPPPCfgPAPUsername_Type(DisplayString):
    """Custom type ipadPPPCfgPAPUsername based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_IpadPPPCfgPAPUsername_Type.__name__ = "DisplayString"
_IpadPPPCfgPAPUsername_Object = MibTableColumn
ipadPPPCfgPAPUsername = _IpadPPPCfgPAPUsername_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 1, 1, 16),
    _IpadPPPCfgPAPUsername_Type()
)
ipadPPPCfgPAPUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadPPPCfgPAPUsername.setStatus("current")


class _IpadPPPCfgPAPPassword_Type(DisplayString):
    """Custom type ipadPPPCfgPAPPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_IpadPPPCfgPAPPassword_Type.__name__ = "DisplayString"
_IpadPPPCfgPAPPassword_Object = MibTableColumn
ipadPPPCfgPAPPassword = _IpadPPPCfgPAPPassword_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 1, 1, 17),
    _IpadPPPCfgPAPPassword_Type()
)
ipadPPPCfgPAPPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadPPPCfgPAPPassword.setStatus("current")


class _IpadPPPCfgCHAPUsername_Type(DisplayString):
    """Custom type ipadPPPCfgCHAPUsername based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_IpadPPPCfgCHAPUsername_Type.__name__ = "DisplayString"
_IpadPPPCfgCHAPUsername_Object = MibTableColumn
ipadPPPCfgCHAPUsername = _IpadPPPCfgCHAPUsername_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 1, 1, 18),
    _IpadPPPCfgCHAPUsername_Type()
)
ipadPPPCfgCHAPUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadPPPCfgCHAPUsername.setStatus("current")


class _IpadPPPCfgCHAPSecret_Type(DisplayString):
    """Custom type ipadPPPCfgCHAPSecret based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_IpadPPPCfgCHAPSecret_Type.__name__ = "DisplayString"
_IpadPPPCfgCHAPSecret_Object = MibTableColumn
ipadPPPCfgCHAPSecret = _IpadPPPCfgCHAPSecret_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 1, 1, 19),
    _IpadPPPCfgCHAPSecret_Type()
)
ipadPPPCfgCHAPSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadPPPCfgCHAPSecret.setStatus("current")
_IpadPPPCfgPortIpAddress_Type = IpAddress
_IpadPPPCfgPortIpAddress_Object = MibTableColumn
ipadPPPCfgPortIpAddress = _IpadPPPCfgPortIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 1, 1, 20),
    _IpadPPPCfgPortIpAddress_Type()
)
ipadPPPCfgPortIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadPPPCfgPortIpAddress.setStatus("current")
_IpadPPPCfgPeerIpAddress_Type = IpAddress
_IpadPPPCfgPeerIpAddress_Object = MibTableColumn
ipadPPPCfgPeerIpAddress = _IpadPPPCfgPeerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 1, 1, 21),
    _IpadPPPCfgPeerIpAddress_Type()
)
ipadPPPCfgPeerIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadPPPCfgPeerIpAddress.setStatus("current")


class _IpadPPPCfgNegIpAddress_Type(Integer32):
    """Custom type ipadPPPCfgNegIpAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("other", 1),
          ("yes", 3))
    )


_IpadPPPCfgNegIpAddress_Type.__name__ = "Integer32"
_IpadPPPCfgNegIpAddress_Object = MibTableColumn
ipadPPPCfgNegIpAddress = _IpadPPPCfgNegIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 1, 1, 22),
    _IpadPPPCfgNegIpAddress_Type()
)
ipadPPPCfgNegIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadPPPCfgNegIpAddress.setStatus("current")


class _IpadPPPCfgNegIPCPCompression_Type(Integer32):
    """Custom type ipadPPPCfgNegIPCPCompression based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("other", 1),
          ("yes", 3))
    )


_IpadPPPCfgNegIPCPCompression_Type.__name__ = "Integer32"
_IpadPPPCfgNegIPCPCompression_Object = MibTableColumn
ipadPPPCfgNegIPCPCompression = _IpadPPPCfgNegIPCPCompression_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 1, 1, 23),
    _IpadPPPCfgNegIPCPCompression_Type()
)
ipadPPPCfgNegIPCPCompression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadPPPCfgNegIPCPCompression.setStatus("current")
_IpadPPPCfgSubnetMask_Type = IpAddress
_IpadPPPCfgSubnetMask_Object = MibTableColumn
ipadPPPCfgSubnetMask = _IpadPPPCfgSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 1, 1, 24),
    _IpadPPPCfgSubnetMask_Type()
)
ipadPPPCfgSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadPPPCfgSubnetMask.setStatus("current")
_IpadPPPCfgAuthChallengeInterval_Type = Integer32
_IpadPPPCfgAuthChallengeInterval_Object = MibTableColumn
ipadPPPCfgAuthChallengeInterval = _IpadPPPCfgAuthChallengeInterval_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 1, 1, 25),
    _IpadPPPCfgAuthChallengeInterval_Type()
)
ipadPPPCfgAuthChallengeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadPPPCfgAuthChallengeInterval.setStatus("current")


class _IpadPPPCfgEndpoint_Type(DisplayString):
    """Custom type ipadPPPCfgEndpoint based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_IpadPPPCfgEndpoint_Type.__name__ = "DisplayString"
_IpadPPPCfgEndpoint_Object = MibTableColumn
ipadPPPCfgEndpoint = _IpadPPPCfgEndpoint_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 1, 1, 26),
    _IpadPPPCfgEndpoint_Type()
)
ipadPPPCfgEndpoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadPPPCfgEndpoint.setStatus("current")


class _IpadPPPCfgNegIpMask_Type(Integer32):
    """Custom type ipadPPPCfgNegIpMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("other", 1),
          ("yes", 3))
    )


_IpadPPPCfgNegIpMask_Type.__name__ = "Integer32"
_IpadPPPCfgNegIpMask_Object = MibTableColumn
ipadPPPCfgNegIpMask = _IpadPPPCfgNegIpMask_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 1, 1, 27),
    _IpadPPPCfgNegIpMask_Type()
)
ipadPPPCfgNegIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadPPPCfgNegIpMask.setStatus("current")


class _IpadPPPCfgNegDNSAddress_Type(Integer32):
    """Custom type ipadPPPCfgNegDNSAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("other", 1),
          ("yes", 3))
    )


_IpadPPPCfgNegDNSAddress_Type.__name__ = "Integer32"
_IpadPPPCfgNegDNSAddress_Object = MibTableColumn
ipadPPPCfgNegDNSAddress = _IpadPPPCfgNegDNSAddress_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 1, 1, 28),
    _IpadPPPCfgNegDNSAddress_Type()
)
ipadPPPCfgNegDNSAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadPPPCfgNegDNSAddress.setStatus("current")
_IpadPPPPAPTable_Object = MibTable
ipadPPPPAPTable = _IpadPPPPAPTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 2)
)
if mibBuilder.loadTexts:
    ipadPPPPAPTable.setStatus("current")
_IpadPPPPAPTableEntry_Object = MibTableRow
ipadPPPPAPTableEntry = _IpadPPPPAPTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 2, 1)
)
ipadPPPPAPTableEntry.setIndexNames(
    (0, "IPADv2-MIB", "ipadPPPPAPTableIndex"),
)
if mibBuilder.loadTexts:
    ipadPPPPAPTableEntry.setStatus("current")
_IpadPPPPAPTableIndex_Type = Integer32
_IpadPPPPAPTableIndex_Object = MibTableColumn
ipadPPPPAPTableIndex = _IpadPPPPAPTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 2, 1, 1),
    _IpadPPPPAPTableIndex_Type()
)
ipadPPPPAPTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadPPPPAPTableIndex.setStatus("current")


class _IpadPPPPAPTableUsername_Type(DisplayString):
    """Custom type ipadPPPPAPTableUsername based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_IpadPPPPAPTableUsername_Type.__name__ = "DisplayString"
_IpadPPPPAPTableUsername_Object = MibTableColumn
ipadPPPPAPTableUsername = _IpadPPPPAPTableUsername_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 2, 1, 2),
    _IpadPPPPAPTableUsername_Type()
)
ipadPPPPAPTableUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadPPPPAPTableUsername.setStatus("current")


class _IpadPPPPAPTablePassword_Type(DisplayString):
    """Custom type ipadPPPPAPTablePassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_IpadPPPPAPTablePassword_Type.__name__ = "DisplayString"
_IpadPPPPAPTablePassword_Object = MibTableColumn
ipadPPPPAPTablePassword = _IpadPPPPAPTablePassword_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 2, 1, 3),
    _IpadPPPPAPTablePassword_Type()
)
ipadPPPPAPTablePassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadPPPPAPTablePassword.setStatus("current")
_IpadPPPCHAPTable_Object = MibTable
ipadPPPCHAPTable = _IpadPPPCHAPTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 3)
)
if mibBuilder.loadTexts:
    ipadPPPCHAPTable.setStatus("current")
_IpadPPPCHAPTableEntry_Object = MibTableRow
ipadPPPCHAPTableEntry = _IpadPPPCHAPTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 3, 1)
)
ipadPPPCHAPTableEntry.setIndexNames(
    (0, "IPADv2-MIB", "ipadPPPCHAPTableIndex"),
)
if mibBuilder.loadTexts:
    ipadPPPCHAPTableEntry.setStatus("current")
_IpadPPPCHAPTableIndex_Type = Integer32
_IpadPPPCHAPTableIndex_Object = MibTableColumn
ipadPPPCHAPTableIndex = _IpadPPPCHAPTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 3, 1, 1),
    _IpadPPPCHAPTableIndex_Type()
)
ipadPPPCHAPTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadPPPCHAPTableIndex.setStatus("current")


class _IpadPPPCHAPTableUsername_Type(DisplayString):
    """Custom type ipadPPPCHAPTableUsername based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_IpadPPPCHAPTableUsername_Type.__name__ = "DisplayString"
_IpadPPPCHAPTableUsername_Object = MibTableColumn
ipadPPPCHAPTableUsername = _IpadPPPCHAPTableUsername_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 3, 1, 2),
    _IpadPPPCHAPTableUsername_Type()
)
ipadPPPCHAPTableUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadPPPCHAPTableUsername.setStatus("current")


class _IpadPPPCHAPTableSecret_Type(DisplayString):
    """Custom type ipadPPPCHAPTableSecret based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_IpadPPPCHAPTableSecret_Type.__name__ = "DisplayString"
_IpadPPPCHAPTableSecret_Object = MibTableColumn
ipadPPPCHAPTableSecret = _IpadPPPCHAPTableSecret_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 3, 1, 3),
    _IpadPPPCHAPTableSecret_Type()
)
ipadPPPCHAPTableSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadPPPCHAPTableSecret.setStatus("current")
_IpadModem_ObjectIdentity = ObjectIdentity
ipadModem = _IpadModem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 8)
)
_IpadModemDialTable_Object = MibTable
ipadModemDialTable = _IpadModemDialTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 8, 1)
)
if mibBuilder.loadTexts:
    ipadModemDialTable.setStatus("current")
_IpadModemDialTableEntry_Object = MibTableRow
ipadModemDialTableEntry = _IpadModemDialTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 8, 1, 1)
)
ipadModemDialTableEntry.setIndexNames(
    (0, "IPADv2-MIB", "ipadModemDialTableIndex"),
)
if mibBuilder.loadTexts:
    ipadModemDialTableEntry.setStatus("current")
_IpadModemDialTableIndex_Type = Integer32
_IpadModemDialTableIndex_Object = MibTableColumn
ipadModemDialTableIndex = _IpadModemDialTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 8, 1, 1, 1),
    _IpadModemDialTableIndex_Type()
)
ipadModemDialTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadModemDialTableIndex.setStatus("current")
_IpadModemDialDataIndex_Type = Integer32
_IpadModemDialDataIndex_Object = MibTableColumn
ipadModemDialDataIndex = _IpadModemDialDataIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 8, 1, 1, 2),
    _IpadModemDialDataIndex_Type()
)
ipadModemDialDataIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadModemDialDataIndex.setStatus("current")


class _IpadModemDialNumber_Type(DisplayString):
    """Custom type ipadModemDialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 60),
    )


_IpadModemDialNumber_Type.__name__ = "DisplayString"
_IpadModemDialNumber_Object = MibTableColumn
ipadModemDialNumber = _IpadModemDialNumber_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 8, 1, 1, 3),
    _IpadModemDialNumber_Type()
)
ipadModemDialNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadModemDialNumber.setStatus("current")
_IpadModemDialAbortTimer_Type = Integer32
_IpadModemDialAbortTimer_Object = MibTableColumn
ipadModemDialAbortTimer = _IpadModemDialAbortTimer_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 8, 1, 1, 4),
    _IpadModemDialAbortTimer_Type()
)
ipadModemDialAbortTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadModemDialAbortTimer.setStatus("current")
_IpadModemDialRedialAttempts_Type = Integer32
_IpadModemDialRedialAttempts_Object = MibTableColumn
ipadModemDialRedialAttempts = _IpadModemDialRedialAttempts_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 8, 1, 1, 5),
    _IpadModemDialRedialAttempts_Type()
)
ipadModemDialRedialAttempts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadModemDialRedialAttempts.setStatus("current")
_IpadModemDialDelayBeforeRedial_Type = Integer32
_IpadModemDialDelayBeforeRedial_Object = MibTableColumn
ipadModemDialDelayBeforeRedial = _IpadModemDialDelayBeforeRedial_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 8, 1, 1, 6),
    _IpadModemDialDelayBeforeRedial_Type()
)
ipadModemDialDelayBeforeRedial.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadModemDialDelayBeforeRedial.setStatus("current")


class _IpadModemDialLoginScript_Type(DisplayString):
    """Custom type ipadModemDialLoginScript based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 60),
    )


_IpadModemDialLoginScript_Type.__name__ = "DisplayString"
_IpadModemDialLoginScript_Object = MibTableColumn
ipadModemDialLoginScript = _IpadModemDialLoginScript_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 8, 1, 1, 7),
    _IpadModemDialLoginScript_Type()
)
ipadModemDialLoginScript.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadModemDialLoginScript.setStatus("current")


class _IpadModemDialUsername_Type(DisplayString):
    """Custom type ipadModemDialUsername based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_IpadModemDialUsername_Type.__name__ = "DisplayString"
_IpadModemDialUsername_Object = MibTableColumn
ipadModemDialUsername = _IpadModemDialUsername_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 8, 1, 1, 8),
    _IpadModemDialUsername_Type()
)
ipadModemDialUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadModemDialUsername.setStatus("current")


class _IpadModemDialPassword_Type(DisplayString):
    """Custom type ipadModemDialPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_IpadModemDialPassword_Type.__name__ = "DisplayString"
_IpadModemDialPassword_Object = MibTableColumn
ipadModemDialPassword = _IpadModemDialPassword_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 8, 1, 1, 9),
    _IpadModemDialPassword_Type()
)
ipadModemDialPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadModemDialPassword.setStatus("current")


class _IpadModemDialChallengeScript_Type(DisplayString):
    """Custom type ipadModemDialChallengeScript based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 60),
    )


_IpadModemDialChallengeScript_Type.__name__ = "DisplayString"
_IpadModemDialChallengeScript_Object = MibTableColumn
ipadModemDialChallengeScript = _IpadModemDialChallengeScript_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 8, 1, 1, 10),
    _IpadModemDialChallengeScript_Type()
)
ipadModemDialChallengeScript.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadModemDialChallengeScript.setStatus("current")
_IpadModemDialAnswerRings_Type = Integer32
_IpadModemDialAnswerRings_Object = MibTableColumn
ipadModemDialAnswerRings = _IpadModemDialAnswerRings_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 8, 1, 1, 11),
    _IpadModemDialAnswerRings_Type()
)
ipadModemDialAnswerRings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadModemDialAnswerRings.setStatus("current")


class _IpadModemDialCommand_Type(Integer32):
    """Custom type ipadModemDialCommand based on Integer32"""
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
        *(("answerNow", 4),
          ("dialNow", 3),
          ("disconnectNow", 5),
          ("other", 1),
          ("setupNow", 2))
    )


_IpadModemDialCommand_Type.__name__ = "Integer32"
_IpadModemDialCommand_Object = MibTableColumn
ipadModemDialCommand = _IpadModemDialCommand_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 8, 1, 1, 12),
    _IpadModemDialCommand_Type()
)
ipadModemDialCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadModemDialCommand.setStatus("current")


class _IpadModemDialStatus_Type(Integer32):
    """Custom type ipadModemDialStatus based on Integer32"""
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("answering", 5),
          ("awaitingCallback", 11),
          ("dialWait", 12),
          ("dialing", 4),
          ("disabled", 2),
          ("disconnecting", 8),
          ("error", 9),
          ("idle", 3),
          ("negotiating", 6),
          ("online", 7),
          ("other", 1),
          ("ringing", 13),
          ("setup", 10))
    )


_IpadModemDialStatus_Type.__name__ = "Integer32"
_IpadModemDialStatus_Object = MibTableColumn
ipadModemDialStatus = _IpadModemDialStatus_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 8, 1, 1, 13),
    _IpadModemDialStatus_Type()
)
ipadModemDialStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadModemDialStatus.setStatus("current")


class _IpadModemDialSecurity_Type(Integer32):
    """Custom type ipadModemDialSecurity based on Integer32"""
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
        *(("callback", 4),
          ("callbackVerify", 5),
          ("disable", 2),
          ("other", 1),
          ("password", 3))
    )


_IpadModemDialSecurity_Type.__name__ = "Integer32"
_IpadModemDialSecurity_Object = MibTableColumn
ipadModemDialSecurity = _IpadModemDialSecurity_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 8, 1, 1, 14),
    _IpadModemDialSecurity_Type()
)
ipadModemDialSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadModemDialSecurity.setStatus("current")
_IpadModemDialCallbackRedialDelay_Type = Integer32
_IpadModemDialCallbackRedialDelay_Object = MibTableColumn
ipadModemDialCallbackRedialDelay = _IpadModemDialCallbackRedialDelay_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 8, 1, 1, 15),
    _IpadModemDialCallbackRedialDelay_Type()
)
ipadModemDialCallbackRedialDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadModemDialCallbackRedialDelay.setStatus("current")
_IpadModemDialCallbackTimeout_Type = Integer32
_IpadModemDialCallbackTimeout_Object = MibTableColumn
ipadModemDialCallbackTimeout = _IpadModemDialCallbackTimeout_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 8, 1, 1, 16),
    _IpadModemDialCallbackTimeout_Type()
)
ipadModemDialCallbackTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadModemDialCallbackTimeout.setStatus("current")


class _IpadModemDialCallbackChalScript_Type(DisplayString):
    """Custom type ipadModemDialCallbackChalScript based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 60),
    )


_IpadModemDialCallbackChalScript_Type.__name__ = "DisplayString"
_IpadModemDialCallbackChalScript_Object = MibTableColumn
ipadModemDialCallbackChalScript = _IpadModemDialCallbackChalScript_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 8, 1, 1, 17),
    _IpadModemDialCallbackChalScript_Type()
)
ipadModemDialCallbackChalScript.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadModemDialCallbackChalScript.setStatus("current")


class _IpadModemDialCallbackRspScript_Type(DisplayString):
    """Custom type ipadModemDialCallbackRspScript based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 60),
    )


_IpadModemDialCallbackRspScript_Type.__name__ = "DisplayString"
_IpadModemDialCallbackRspScript_Object = MibTableColumn
ipadModemDialCallbackRspScript = _IpadModemDialCallbackRspScript_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 8, 1, 1, 18),
    _IpadModemDialCallbackRspScript_Type()
)
ipadModemDialCallbackRspScript.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadModemDialCallbackRspScript.setStatus("current")
_IpadModemDataTable_Object = MibTable
ipadModemDataTable = _IpadModemDataTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 8, 2)
)
if mibBuilder.loadTexts:
    ipadModemDataTable.setStatus("current")
_IpadModemDataTableEntry_Object = MibTableRow
ipadModemDataTableEntry = _IpadModemDataTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 8, 2, 1)
)
ipadModemDataTableEntry.setIndexNames(
    (0, "IPADv2-MIB", "ipadModemDataTableIndex"),
)
if mibBuilder.loadTexts:
    ipadModemDataTableEntry.setStatus("current")
_IpadModemDataTableIndex_Type = Integer32
_IpadModemDataTableIndex_Object = MibTableColumn
ipadModemDataTableIndex = _IpadModemDataTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 8, 2, 1, 1),
    _IpadModemDataTableIndex_Type()
)
ipadModemDataTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadModemDataTableIndex.setStatus("current")


class _IpadModemDataModemName_Type(DisplayString):
    """Custom type ipadModemDataModemName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_IpadModemDataModemName_Type.__name__ = "DisplayString"
_IpadModemDataModemName_Object = MibTableColumn
ipadModemDataModemName = _IpadModemDataModemName_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 8, 2, 1, 2),
    _IpadModemDataModemName_Type()
)
ipadModemDataModemName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadModemDataModemName.setStatus("current")


class _IpadModemDataSetupScript_Type(DisplayString):
    """Custom type ipadModemDataSetupScript based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 60),
    )


_IpadModemDataSetupScript_Type.__name__ = "DisplayString"
_IpadModemDataSetupScript_Object = MibTableColumn
ipadModemDataSetupScript = _IpadModemDataSetupScript_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 8, 2, 1, 3),
    _IpadModemDataSetupScript_Type()
)
ipadModemDataSetupScript.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadModemDataSetupScript.setStatus("current")


class _IpadModemDataDialingScript_Type(DisplayString):
    """Custom type ipadModemDataDialingScript based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 60),
    )


_IpadModemDataDialingScript_Type.__name__ = "DisplayString"
_IpadModemDataDialingScript_Object = MibTableColumn
ipadModemDataDialingScript = _IpadModemDataDialingScript_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 8, 2, 1, 4),
    _IpadModemDataDialingScript_Type()
)
ipadModemDataDialingScript.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadModemDataDialingScript.setStatus("current")


class _IpadModemDataAnswerScript_Type(DisplayString):
    """Custom type ipadModemDataAnswerScript based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 60),
    )


_IpadModemDataAnswerScript_Type.__name__ = "DisplayString"
_IpadModemDataAnswerScript_Object = MibTableColumn
ipadModemDataAnswerScript = _IpadModemDataAnswerScript_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 8, 2, 1, 5),
    _IpadModemDataAnswerScript_Type()
)
ipadModemDataAnswerScript.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadModemDataAnswerScript.setStatus("current")


class _IpadModemDataHangupScript_Type(DisplayString):
    """Custom type ipadModemDataHangupScript based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 60),
    )


_IpadModemDataHangupScript_Type.__name__ = "DisplayString"
_IpadModemDataHangupScript_Object = MibTableColumn
ipadModemDataHangupScript = _IpadModemDataHangupScript_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 8, 2, 1, 6),
    _IpadModemDataHangupScript_Type()
)
ipadModemDataHangupScript.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadModemDataHangupScript.setStatus("current")


class _IpadModemDataSyncScript_Type(DisplayString):
    """Custom type ipadModemDataSyncScript based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 60),
    )


_IpadModemDataSyncScript_Type.__name__ = "DisplayString"
_IpadModemDataSyncScript_Object = MibTableColumn
ipadModemDataSyncScript = _IpadModemDataSyncScript_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 8, 2, 1, 7),
    _IpadModemDataSyncScript_Type()
)
ipadModemDataSyncScript.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadModemDataSyncScript.setStatus("current")


class _IpadModemDataSyncMethod_Type(Integer32):
    """Custom type ipadModemDataSyncMethod based on Integer32"""
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
        *(("none", 2),
          ("other", 1),
          ("rfc1662", 5),
          ("sync", 3),
          ("v80", 4),
          ("v80crc", 6))
    )


_IpadModemDataSyncMethod_Type.__name__ = "Integer32"
_IpadModemDataSyncMethod_Object = MibTableColumn
ipadModemDataSyncMethod = _IpadModemDataSyncMethod_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 8, 2, 1, 8),
    _IpadModemDataSyncMethod_Type()
)
ipadModemDataSyncMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadModemDataSyncMethod.setStatus("current")


class _IpadModemDataSetupScript2_Type(DisplayString):
    """Custom type ipadModemDataSetupScript2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 60),
    )


_IpadModemDataSetupScript2_Type.__name__ = "DisplayString"
_IpadModemDataSetupScript2_Object = MibTableColumn
ipadModemDataSetupScript2 = _IpadModemDataSetupScript2_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 8, 2, 1, 9),
    _IpadModemDataSetupScript2_Type()
)
ipadModemDataSetupScript2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadModemDataSetupScript2.setStatus("current")


class _IpadModemDataSetupScript3_Type(DisplayString):
    """Custom type ipadModemDataSetupScript3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 60),
    )


_IpadModemDataSetupScript3_Type.__name__ = "DisplayString"
_IpadModemDataSetupScript3_Object = MibTableColumn
ipadModemDataSetupScript3 = _IpadModemDataSetupScript3_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 8, 2, 1, 10),
    _IpadModemDataSetupScript3_Type()
)
ipadModemDataSetupScript3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadModemDataSetupScript3.setStatus("current")


class _IpadModemDataSetupScript4_Type(DisplayString):
    """Custom type ipadModemDataSetupScript4 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 60),
    )


_IpadModemDataSetupScript4_Type.__name__ = "DisplayString"
_IpadModemDataSetupScript4_Object = MibTableColumn
ipadModemDataSetupScript4 = _IpadModemDataSetupScript4_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 8, 2, 1, 11),
    _IpadModemDataSetupScript4_Type()
)
ipadModemDataSetupScript4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadModemDataSetupScript4.setStatus("current")


class _IpadModemDataSetupScript5_Type(DisplayString):
    """Custom type ipadModemDataSetupScript5 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 60),
    )


_IpadModemDataSetupScript5_Type.__name__ = "DisplayString"
_IpadModemDataSetupScript5_Object = MibTableColumn
ipadModemDataSetupScript5 = _IpadModemDataSetupScript5_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 8, 2, 1, 12),
    _IpadModemDataSetupScript5_Type()
)
ipadModemDataSetupScript5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadModemDataSetupScript5.setStatus("current")
_IpadDbuTable_Object = MibTable
ipadDbuTable = _IpadDbuTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 8, 3)
)
if mibBuilder.loadTexts:
    ipadDbuTable.setStatus("current")
_IpadDbuTableEntry_Object = MibTableRow
ipadDbuTableEntry = _IpadDbuTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 8, 3, 1)
)
ipadDbuTableEntry.setIndexNames(
    (0, "IPADv2-MIB", "ipadDbuIndex"),
)
if mibBuilder.loadTexts:
    ipadDbuTableEntry.setStatus("current")
_IpadDbuIndex_Type = Integer32
_IpadDbuIndex_Object = MibTableColumn
ipadDbuIndex = _IpadDbuIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 8, 3, 1, 1),
    _IpadDbuIndex_Type()
)
ipadDbuIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDbuIndex.setStatus("current")


class _IpadDbuOperation_Type(Integer32):
    """Custom type ipadDbuOperation based on Integer32"""
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
        *(("automatic", 3),
          ("automaticDaily", 4),
          ("disable", 2),
          ("forceBackup", 5),
          ("other", 1),
          ("testAnswer", 7),
          ("testOriginate", 6))
    )


_IpadDbuOperation_Type.__name__ = "Integer32"
_IpadDbuOperation_Object = MibTableColumn
ipadDbuOperation = _IpadDbuOperation_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 8, 3, 1, 2),
    _IpadDbuOperation_Type()
)
ipadDbuOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadDbuOperation.setStatus("current")
_IpadDbuMonitoredifIndex_Type = Integer32
_IpadDbuMonitoredifIndex_Object = MibTableColumn
ipadDbuMonitoredifIndex = _IpadDbuMonitoredifIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 8, 3, 1, 7),
    _IpadDbuMonitoredifIndex_Type()
)
ipadDbuMonitoredifIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadDbuMonitoredifIndex.setStatus("current")


class _IpadDbuActivator1_Type(Integer32):
    """Custom type ipadDbuActivator1 based on Integer32"""
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("ais", 12),
          ("any", 3),
          ("bpv", 10),
          ("carrier", 4),
          ("cs", 9),
          ("disable", 2),
          ("es", 5),
          ("los", 8),
          ("oof", 11),
          ("oos", 14),
          ("other", 1),
          ("ras", 13),
          ("ses", 6),
          ("uas", 7))
    )


_IpadDbuActivator1_Type.__name__ = "Integer32"
_IpadDbuActivator1_Object = MibTableColumn
ipadDbuActivator1 = _IpadDbuActivator1_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 8, 3, 1, 8),
    _IpadDbuActivator1_Type()
)
ipadDbuActivator1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadDbuActivator1.setStatus("current")


class _IpadDbuActivator2_Type(Integer32):
    """Custom type ipadDbuActivator2 based on Integer32"""
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("ais", 12),
          ("any", 3),
          ("bpv", 10),
          ("carrier", 4),
          ("cs", 9),
          ("disable", 2),
          ("es", 5),
          ("los", 8),
          ("oof", 11),
          ("oos", 14),
          ("other", 1),
          ("ras", 13),
          ("ses", 6),
          ("uas", 7))
    )


_IpadDbuActivator2_Type.__name__ = "Integer32"
_IpadDbuActivator2_Object = MibTableColumn
ipadDbuActivator2 = _IpadDbuActivator2_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 8, 3, 1, 9),
    _IpadDbuActivator2_Type()
)
ipadDbuActivator2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadDbuActivator2.setStatus("current")
_IpadDbuRevertDelay_Type = Integer32
_IpadDbuRevertDelay_Object = MibTableColumn
ipadDbuRevertDelay = _IpadDbuRevertDelay_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 8, 3, 1, 10),
    _IpadDbuRevertDelay_Type()
)
ipadDbuRevertDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadDbuRevertDelay.setStatus("current")
_IpadDbuTrapDelay_Type = Integer32
_IpadDbuTrapDelay_Object = MibTableColumn
ipadDbuTrapDelay = _IpadDbuTrapDelay_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 8, 3, 1, 11),
    _IpadDbuTrapDelay_Type()
)
ipadDbuTrapDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadDbuTrapDelay.setStatus("current")


class _IpadDbuStatus_Type(Integer32):
    """Custom type ipadDbuStatus based on Integer32"""
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
              17)
        )
    )
    namedValues = NamedValues(
        *(("active", 9),
          ("answering", 6),
          ("awaitingCallback", 8),
          ("dialWait", 16),
          ("dialing", 5),
          ("disabled", 2),
          ("disallowed", 4),
          ("disconnecting", 10),
          ("error", 14),
          ("negotiating", 7),
          ("other", 1),
          ("ringing", 17),
          ("setup", 15),
          ("standby", 3),
          ("testFailed", 13),
          ("testPassed", 12),
          ("testWaiting", 11))
    )


_IpadDbuStatus_Type.__name__ = "Integer32"
_IpadDbuStatus_Object = MibTableColumn
ipadDbuStatus = _IpadDbuStatus_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 8, 3, 1, 12),
    _IpadDbuStatus_Type()
)
ipadDbuStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDbuStatus.setStatus("current")


class _IpadDbuTrap_Type(Integer32):
    """Custom type ipadDbuTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 3),
          ("other", 1))
    )


_IpadDbuTrap_Type.__name__ = "Integer32"
_IpadDbuTrap_Object = MibTableColumn
ipadDbuTrap = _IpadDbuTrap_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 8, 3, 1, 13),
    _IpadDbuTrap_Type()
)
ipadDbuTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadDbuTrap.setStatus("current")
_IpadDbuDailyTable_Object = MibTable
ipadDbuDailyTable = _IpadDbuDailyTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 8, 4)
)
if mibBuilder.loadTexts:
    ipadDbuDailyTable.setStatus("current")
_IpadDbuDailyTableEntry_Object = MibTableRow
ipadDbuDailyTableEntry = _IpadDbuDailyTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 8, 4, 1)
)
ipadDbuDailyTableEntry.setIndexNames(
    (0, "IPADv2-MIB", "ipadDbuDailyIndex"),
    (0, "IPADv2-MIB", "ipadDbuDailyDayOfWeek"),
)
if mibBuilder.loadTexts:
    ipadDbuDailyTableEntry.setStatus("current")
_IpadDbuDailyIndex_Type = Integer32
_IpadDbuDailyIndex_Object = MibTableColumn
ipadDbuDailyIndex = _IpadDbuDailyIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 8, 4, 1, 1),
    _IpadDbuDailyIndex_Type()
)
ipadDbuDailyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDbuDailyIndex.setStatus("current")


class _IpadDbuDailyDayOfWeek_Type(Integer32):
    """Custom type ipadDbuDailyDayOfWeek based on Integer32"""
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
        *(("friday", 6),
          ("monday", 2),
          ("saturday", 7),
          ("sunday", 1),
          ("thursday", 5),
          ("tuesday", 3),
          ("wednesday", 4))
    )


_IpadDbuDailyDayOfWeek_Type.__name__ = "Integer32"
_IpadDbuDailyDayOfWeek_Object = MibTableColumn
ipadDbuDailyDayOfWeek = _IpadDbuDailyDayOfWeek_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 8, 4, 1, 2),
    _IpadDbuDailyDayOfWeek_Type()
)
ipadDbuDailyDayOfWeek.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDbuDailyDayOfWeek.setStatus("current")


class _IpadDbuDailyStart_Type(Integer32):
    """Custom type ipadDbuDailyStart based on Integer32"""
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
              24)
        )
    )
    namedValues = NamedValues(
        *(("hour00", 1),
          ("hour01", 2),
          ("hour02", 3),
          ("hour03", 4),
          ("hour04", 5),
          ("hour05", 6),
          ("hour06", 7),
          ("hour07", 8),
          ("hour08", 9),
          ("hour09", 10),
          ("hour10", 11),
          ("hour11", 12),
          ("hour12", 13),
          ("hour13", 14),
          ("hour14", 15),
          ("hour15", 16),
          ("hour16", 17),
          ("hour17", 18),
          ("hour18", 19),
          ("hour19", 20),
          ("hour20", 21),
          ("hour21", 22),
          ("hour22", 23),
          ("hour23", 24))
    )


_IpadDbuDailyStart_Type.__name__ = "Integer32"
_IpadDbuDailyStart_Object = MibTableColumn
ipadDbuDailyStart = _IpadDbuDailyStart_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 8, 4, 1, 3),
    _IpadDbuDailyStart_Type()
)
ipadDbuDailyStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadDbuDailyStart.setStatus("current")


class _IpadDbuDailyLength_Type(Integer32):
    """Custom type ipadDbuDailyLength based on Integer32"""
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
              25)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("hour01", 2),
          ("hour02", 3),
          ("hour03", 4),
          ("hour04", 5),
          ("hour05", 6),
          ("hour06", 7),
          ("hour07", 8),
          ("hour08", 9),
          ("hour09", 10),
          ("hour10", 11),
          ("hour11", 12),
          ("hour12", 13),
          ("hour13", 14),
          ("hour14", 15),
          ("hour15", 16),
          ("hour16", 17),
          ("hour17", 18),
          ("hour18", 19),
          ("hour19", 20),
          ("hour20", 21),
          ("hour21", 22),
          ("hour22", 23),
          ("hour23", 24),
          ("hour24", 25))
    )


_IpadDbuDailyLength_Type.__name__ = "Integer32"
_IpadDbuDailyLength_Object = MibTableColumn
ipadDbuDailyLength = _IpadDbuDailyLength_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 8, 4, 1, 4),
    _IpadDbuDailyLength_Type()
)
ipadDbuDailyLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadDbuDailyLength.setStatus("current")
_IpadSvcAware_ObjectIdentity = ObjectIdentity
ipadSvcAware = _IpadSvcAware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9)
)
_IpadFrPortStatsTable_Object = MibTable
ipadFrPortStatsTable = _IpadFrPortStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 1)
)
if mibBuilder.loadTexts:
    ipadFrPortStatsTable.setStatus("current")
_IpadFrPortStatsEntry_Object = MibTableRow
ipadFrPortStatsEntry = _IpadFrPortStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 1, 1)
)
ipadFrPortStatsEntry.setIndexNames(
    (0, "IPADv2-MIB", "ipadFrPortStatsService"),
    (0, "IPADv2-MIB", "ipadFrPortStatsPeriod"),
)
if mibBuilder.loadTexts:
    ipadFrPortStatsEntry.setStatus("current")
_IpadFrPortStatsService_Type = Integer32
_IpadFrPortStatsService_Object = MibTableColumn
ipadFrPortStatsService = _IpadFrPortStatsService_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 1, 1, 1),
    _IpadFrPortStatsService_Type()
)
ipadFrPortStatsService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadFrPortStatsService.setStatus("current")


class _IpadFrPortStatsPeriod_Type(Integer32):
    """Custom type ipadFrPortStatsPeriod based on Integer32"""
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
              74,
              75,
              76,
              77,
              78,
              79,
              80,
              81,
              82,
              83,
              84,
              85,
              86,
              87,
              88,
              89,
              90,
              91,
              92,
              93,
              94,
              95,
              96,
              97,
              98)
        )
    )
    namedValues = NamedValues(
        *(("portStatsCurrent", 2),
          ("portStatsSummary", 1),
          ("portStatsperiod1", 3),
          ("portStatsperiod10", 12),
          ("portStatsperiod11", 13),
          ("portStatsperiod12", 14),
          ("portStatsperiod13", 15),
          ("portStatsperiod14", 16),
          ("portStatsperiod15", 17),
          ("portStatsperiod16", 18),
          ("portStatsperiod17", 19),
          ("portStatsperiod18", 20),
          ("portStatsperiod19", 21),
          ("portStatsperiod2", 4),
          ("portStatsperiod20", 22),
          ("portStatsperiod21", 23),
          ("portStatsperiod22", 24),
          ("portStatsperiod23", 25),
          ("portStatsperiod24", 26),
          ("portStatsperiod25", 27),
          ("portStatsperiod26", 28),
          ("portStatsperiod27", 29),
          ("portStatsperiod28", 30),
          ("portStatsperiod29", 31),
          ("portStatsperiod3", 5),
          ("portStatsperiod30", 32),
          ("portStatsperiod31", 33),
          ("portStatsperiod32", 34),
          ("portStatsperiod33", 35),
          ("portStatsperiod34", 36),
          ("portStatsperiod35", 37),
          ("portStatsperiod36", 38),
          ("portStatsperiod37", 39),
          ("portStatsperiod38", 40),
          ("portStatsperiod39", 41),
          ("portStatsperiod4", 6),
          ("portStatsperiod40", 42),
          ("portStatsperiod41", 43),
          ("portStatsperiod42", 44),
          ("portStatsperiod43", 45),
          ("portStatsperiod44", 46),
          ("portStatsperiod45", 47),
          ("portStatsperiod46", 48),
          ("portStatsperiod47", 49),
          ("portStatsperiod48", 50),
          ("portStatsperiod49", 51),
          ("portStatsperiod5", 7),
          ("portStatsperiod50", 52),
          ("portStatsperiod51", 53),
          ("portStatsperiod52", 54),
          ("portStatsperiod53", 55),
          ("portStatsperiod54", 56),
          ("portStatsperiod55", 57),
          ("portStatsperiod56", 58),
          ("portStatsperiod57", 59),
          ("portStatsperiod58", 60),
          ("portStatsperiod59", 61),
          ("portStatsperiod6", 8),
          ("portStatsperiod60", 62),
          ("portStatsperiod61", 63),
          ("portStatsperiod62", 64),
          ("portStatsperiod63", 65),
          ("portStatsperiod64", 66),
          ("portStatsperiod65", 67),
          ("portStatsperiod66", 68),
          ("portStatsperiod67", 69),
          ("portStatsperiod68", 70),
          ("portStatsperiod69", 71),
          ("portStatsperiod7", 9),
          ("portStatsperiod70", 72),
          ("portStatsperiod71", 73),
          ("portStatsperiod72", 74),
          ("portStatsperiod73", 75),
          ("portStatsperiod74", 76),
          ("portStatsperiod75", 77),
          ("portStatsperiod76", 78),
          ("portStatsperiod77", 79),
          ("portStatsperiod78", 80),
          ("portStatsperiod79", 81),
          ("portStatsperiod8", 10),
          ("portStatsperiod80", 82),
          ("portStatsperiod81", 83),
          ("portStatsperiod82", 84),
          ("portStatsperiod83", 85),
          ("portStatsperiod84", 86),
          ("portStatsperiod85", 87),
          ("portStatsperiod86", 88),
          ("portStatsperiod87", 89),
          ("portStatsperiod88", 90),
          ("portStatsperiod89", 91),
          ("portStatsperiod9", 11),
          ("portStatsperiod90", 92),
          ("portStatsperiod91", 93),
          ("portStatsperiod92", 94),
          ("portStatsperiod93", 95),
          ("portStatsperiod94", 96),
          ("portStatsperiod95", 97),
          ("portStatsperiod96", 98))
    )


_IpadFrPortStatsPeriod_Type.__name__ = "Integer32"
_IpadFrPortStatsPeriod_Object = MibTableColumn
ipadFrPortStatsPeriod = _IpadFrPortStatsPeriod_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 1, 1, 2),
    _IpadFrPortStatsPeriod_Type()
)
ipadFrPortStatsPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadFrPortStatsPeriod.setStatus("current")
_IpadFrPortStatsTxFrames_Type = Integer32
_IpadFrPortStatsTxFrames_Object = MibTableColumn
ipadFrPortStatsTxFrames = _IpadFrPortStatsTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 1, 1, 3),
    _IpadFrPortStatsTxFrames_Type()
)
ipadFrPortStatsTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadFrPortStatsTxFrames.setStatus("current")
_IpadFrPortStatsRxFrames_Type = Integer32
_IpadFrPortStatsRxFrames_Object = MibTableColumn
ipadFrPortStatsRxFrames = _IpadFrPortStatsRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 1, 1, 4),
    _IpadFrPortStatsRxFrames_Type()
)
ipadFrPortStatsRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadFrPortStatsRxFrames.setStatus("current")
_IpadFrPortStatsTxOctets_Type = Integer32
_IpadFrPortStatsTxOctets_Object = MibTableColumn
ipadFrPortStatsTxOctets = _IpadFrPortStatsTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 1, 1, 5),
    _IpadFrPortStatsTxOctets_Type()
)
ipadFrPortStatsTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadFrPortStatsTxOctets.setStatus("current")
_IpadFrPortStatsRxOctets_Type = Integer32
_IpadFrPortStatsRxOctets_Object = MibTableColumn
ipadFrPortStatsRxOctets = _IpadFrPortStatsRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 1, 1, 6),
    _IpadFrPortStatsRxOctets_Type()
)
ipadFrPortStatsRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadFrPortStatsRxOctets.setStatus("current")
_IpadFrPortStatsTxMgmtFrames_Type = Integer32
_IpadFrPortStatsTxMgmtFrames_Object = MibTableColumn
ipadFrPortStatsTxMgmtFrames = _IpadFrPortStatsTxMgmtFrames_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 1, 1, 7),
    _IpadFrPortStatsTxMgmtFrames_Type()
)
ipadFrPortStatsTxMgmtFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadFrPortStatsTxMgmtFrames.setStatus("current")
_IpadFrPortStatsRxMgmtFrames_Type = Integer32
_IpadFrPortStatsRxMgmtFrames_Object = MibTableColumn
ipadFrPortStatsRxMgmtFrames = _IpadFrPortStatsRxMgmtFrames_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 1, 1, 8),
    _IpadFrPortStatsRxMgmtFrames_Type()
)
ipadFrPortStatsRxMgmtFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadFrPortStatsRxMgmtFrames.setStatus("current")
_IpadFrPortStatsTxMgmtOctets_Type = Integer32
_IpadFrPortStatsTxMgmtOctets_Object = MibTableColumn
ipadFrPortStatsTxMgmtOctets = _IpadFrPortStatsTxMgmtOctets_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 1, 1, 9),
    _IpadFrPortStatsTxMgmtOctets_Type()
)
ipadFrPortStatsTxMgmtOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadFrPortStatsTxMgmtOctets.setStatus("current")
_IpadFrPortStatsRxMgmtOctets_Type = Integer32
_IpadFrPortStatsRxMgmtOctets_Object = MibTableColumn
ipadFrPortStatsRxMgmtOctets = _IpadFrPortStatsRxMgmtOctets_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 1, 1, 10),
    _IpadFrPortStatsRxMgmtOctets_Type()
)
ipadFrPortStatsRxMgmtOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadFrPortStatsRxMgmtOctets.setStatus("current")
_IpadFrPortStatsRxFECN_Type = Integer32
_IpadFrPortStatsRxFECN_Object = MibTableColumn
ipadFrPortStatsRxFECN = _IpadFrPortStatsRxFECN_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 1, 1, 11),
    _IpadFrPortStatsRxFECN_Type()
)
ipadFrPortStatsRxFECN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadFrPortStatsRxFECN.setStatus("current")
_IpadFrPortStatsRxBECN_Type = Integer32
_IpadFrPortStatsRxBECN_Object = MibTableColumn
ipadFrPortStatsRxBECN = _IpadFrPortStatsRxBECN_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 1, 1, 12),
    _IpadFrPortStatsRxBECN_Type()
)
ipadFrPortStatsRxBECN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadFrPortStatsRxBECN.setStatus("current")
_IpadFrPortStatsRxInvalid_Type = Integer32
_IpadFrPortStatsRxInvalid_Object = MibTableColumn
ipadFrPortStatsRxInvalid = _IpadFrPortStatsRxInvalid_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 1, 1, 13),
    _IpadFrPortStatsRxInvalid_Type()
)
ipadFrPortStatsRxInvalid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadFrPortStatsRxInvalid.setStatus("current")
_IpadFrPortStatsTxStatInq_Type = Integer32
_IpadFrPortStatsTxStatInq_Object = MibTableColumn
ipadFrPortStatsTxStatInq = _IpadFrPortStatsTxStatInq_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 1, 1, 14),
    _IpadFrPortStatsTxStatInq_Type()
)
ipadFrPortStatsTxStatInq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadFrPortStatsTxStatInq.setStatus("current")
_IpadFrPortStatsRxStatInq_Type = Integer32
_IpadFrPortStatsRxStatInq_Object = MibTableColumn
ipadFrPortStatsRxStatInq = _IpadFrPortStatsRxStatInq_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 1, 1, 15),
    _IpadFrPortStatsRxStatInq_Type()
)
ipadFrPortStatsRxStatInq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadFrPortStatsRxStatInq.setStatus("current")
_IpadFrPortStatsTxStatResp_Type = Integer32
_IpadFrPortStatsTxStatResp_Object = MibTableColumn
ipadFrPortStatsTxStatResp = _IpadFrPortStatsTxStatResp_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 1, 1, 16),
    _IpadFrPortStatsTxStatResp_Type()
)
ipadFrPortStatsTxStatResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadFrPortStatsTxStatResp.setStatus("current")
_IpadFrPortStatsRxStatResp_Type = Integer32
_IpadFrPortStatsRxStatResp_Object = MibTableColumn
ipadFrPortStatsRxStatResp = _IpadFrPortStatsRxStatResp_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 1, 1, 17),
    _IpadFrPortStatsRxStatResp_Type()
)
ipadFrPortStatsRxStatResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadFrPortStatsRxStatResp.setStatus("current")
_IpadFrPortStatsRxInvLMI_Type = Integer32
_IpadFrPortStatsRxInvLMI_Object = MibTableColumn
ipadFrPortStatsRxInvLMI = _IpadFrPortStatsRxInvLMI_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 1, 1, 18),
    _IpadFrPortStatsRxInvLMI_Type()
)
ipadFrPortStatsRxInvLMI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadFrPortStatsRxInvLMI.setStatus("current")
_IpadFrPortStatsPeak_Type = Integer32
_IpadFrPortStatsPeak_Object = MibTableColumn
ipadFrPortStatsPeak = _IpadFrPortStatsPeak_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 1, 1, 19),
    _IpadFrPortStatsPeak_Type()
)
ipadFrPortStatsPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadFrPortStatsPeak.setStatus("current")
_IpadFrPortStatsAverage_Type = Integer32
_IpadFrPortStatsAverage_Object = MibTableColumn
ipadFrPortStatsAverage = _IpadFrPortStatsAverage_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 1, 1, 20),
    _IpadFrPortStatsAverage_Type()
)
ipadFrPortStatsAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadFrPortStatsAverage.setStatus("current")
_IpadFrPortStatsTimeStamp_Type = TimeTicks
_IpadFrPortStatsTimeStamp_Object = MibTableColumn
ipadFrPortStatsTimeStamp = _IpadFrPortStatsTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 1, 1, 21),
    _IpadFrPortStatsTimeStamp_Type()
)
ipadFrPortStatsTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadFrPortStatsTimeStamp.setStatus("current")
_IpadFrPortStatsTxAvgPercent_Type = Integer32
_IpadFrPortStatsTxAvgPercent_Object = MibTableColumn
ipadFrPortStatsTxAvgPercent = _IpadFrPortStatsTxAvgPercent_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 1, 1, 22),
    _IpadFrPortStatsTxAvgPercent_Type()
)
ipadFrPortStatsTxAvgPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadFrPortStatsTxAvgPercent.setStatus("current")
_IpadFrPortStatsTxMaxPercent_Type = Integer32
_IpadFrPortStatsTxMaxPercent_Object = MibTableColumn
ipadFrPortStatsTxMaxPercent = _IpadFrPortStatsTxMaxPercent_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 1, 1, 23),
    _IpadFrPortStatsTxMaxPercent_Type()
)
ipadFrPortStatsTxMaxPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadFrPortStatsTxMaxPercent.setStatus("current")
_IpadFrPortStatsTxInstantPercent_Type = Integer32
_IpadFrPortStatsTxInstantPercent_Object = MibTableColumn
ipadFrPortStatsTxInstantPercent = _IpadFrPortStatsTxInstantPercent_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 1, 1, 24),
    _IpadFrPortStatsTxInstantPercent_Type()
)
ipadFrPortStatsTxInstantPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadFrPortStatsTxInstantPercent.setStatus("current")
_IpadFrPortStatsTx20PercentSec_Type = Integer32
_IpadFrPortStatsTx20PercentSec_Object = MibTableColumn
ipadFrPortStatsTx20PercentSec = _IpadFrPortStatsTx20PercentSec_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 1, 1, 25),
    _IpadFrPortStatsTx20PercentSec_Type()
)
ipadFrPortStatsTx20PercentSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadFrPortStatsTx20PercentSec.setStatus("current")
_IpadFrPortStatsTx40PercentSec_Type = Integer32
_IpadFrPortStatsTx40PercentSec_Object = MibTableColumn
ipadFrPortStatsTx40PercentSec = _IpadFrPortStatsTx40PercentSec_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 1, 1, 26),
    _IpadFrPortStatsTx40PercentSec_Type()
)
ipadFrPortStatsTx40PercentSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadFrPortStatsTx40PercentSec.setStatus("current")
_IpadFrPortStatsTx60PercentSec_Type = Integer32
_IpadFrPortStatsTx60PercentSec_Object = MibTableColumn
ipadFrPortStatsTx60PercentSec = _IpadFrPortStatsTx60PercentSec_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 1, 1, 27),
    _IpadFrPortStatsTx60PercentSec_Type()
)
ipadFrPortStatsTx60PercentSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadFrPortStatsTx60PercentSec.setStatus("current")
_IpadFrPortStatsTx80PercentSec_Type = Integer32
_IpadFrPortStatsTx80PercentSec_Object = MibTableColumn
ipadFrPortStatsTx80PercentSec = _IpadFrPortStatsTx80PercentSec_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 1, 1, 28),
    _IpadFrPortStatsTx80PercentSec_Type()
)
ipadFrPortStatsTx80PercentSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadFrPortStatsTx80PercentSec.setStatus("current")
_IpadFrPortStatsTx100PercentSec_Type = Integer32
_IpadFrPortStatsTx100PercentSec_Object = MibTableColumn
ipadFrPortStatsTx100PercentSec = _IpadFrPortStatsTx100PercentSec_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 1, 1, 29),
    _IpadFrPortStatsTx100PercentSec_Type()
)
ipadFrPortStatsTx100PercentSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadFrPortStatsTx100PercentSec.setStatus("current")
_IpadFrPortStatsRxAvgPercent_Type = Integer32
_IpadFrPortStatsRxAvgPercent_Object = MibTableColumn
ipadFrPortStatsRxAvgPercent = _IpadFrPortStatsRxAvgPercent_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 1, 1, 30),
    _IpadFrPortStatsRxAvgPercent_Type()
)
ipadFrPortStatsRxAvgPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadFrPortStatsRxAvgPercent.setStatus("current")
_IpadFrPortStatsRxMaxPercent_Type = Integer32
_IpadFrPortStatsRxMaxPercent_Object = MibTableColumn
ipadFrPortStatsRxMaxPercent = _IpadFrPortStatsRxMaxPercent_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 1, 1, 31),
    _IpadFrPortStatsRxMaxPercent_Type()
)
ipadFrPortStatsRxMaxPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadFrPortStatsRxMaxPercent.setStatus("current")
_IpadFrPortStatsRxInstantPercent_Type = Integer32
_IpadFrPortStatsRxInstantPercent_Object = MibTableColumn
ipadFrPortStatsRxInstantPercent = _IpadFrPortStatsRxInstantPercent_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 1, 1, 32),
    _IpadFrPortStatsRxInstantPercent_Type()
)
ipadFrPortStatsRxInstantPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadFrPortStatsRxInstantPercent.setStatus("current")
_IpadFrPortStatsRx20PercentSec_Type = Integer32
_IpadFrPortStatsRx20PercentSec_Object = MibTableColumn
ipadFrPortStatsRx20PercentSec = _IpadFrPortStatsRx20PercentSec_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 1, 1, 33),
    _IpadFrPortStatsRx20PercentSec_Type()
)
ipadFrPortStatsRx20PercentSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadFrPortStatsRx20PercentSec.setStatus("current")
_IpadFrPortStatsRx40PercentSec_Type = Integer32
_IpadFrPortStatsRx40PercentSec_Object = MibTableColumn
ipadFrPortStatsRx40PercentSec = _IpadFrPortStatsRx40PercentSec_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 1, 1, 34),
    _IpadFrPortStatsRx40PercentSec_Type()
)
ipadFrPortStatsRx40PercentSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadFrPortStatsRx40PercentSec.setStatus("current")
_IpadFrPortStatsRx60PercentSec_Type = Integer32
_IpadFrPortStatsRx60PercentSec_Object = MibTableColumn
ipadFrPortStatsRx60PercentSec = _IpadFrPortStatsRx60PercentSec_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 1, 1, 35),
    _IpadFrPortStatsRx60PercentSec_Type()
)
ipadFrPortStatsRx60PercentSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadFrPortStatsRx60PercentSec.setStatus("current")
_IpadFrPortStatsRx80PercentSec_Type = Integer32
_IpadFrPortStatsRx80PercentSec_Object = MibTableColumn
ipadFrPortStatsRx80PercentSec = _IpadFrPortStatsRx80PercentSec_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 1, 1, 36),
    _IpadFrPortStatsRx80PercentSec_Type()
)
ipadFrPortStatsRx80PercentSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadFrPortStatsRx80PercentSec.setStatus("current")
_IpadFrPortStatsRx100PercentSec_Type = Integer32
_IpadFrPortStatsRx100PercentSec_Object = MibTableColumn
ipadFrPortStatsRx100PercentSec = _IpadFrPortStatsRx100PercentSec_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 1, 1, 37),
    _IpadFrPortStatsRx100PercentSec_Type()
)
ipadFrPortStatsRx100PercentSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadFrPortStatsRx100PercentSec.setStatus("current")


class _IpadFrPortStatsValidIntervals_Type(Integer32):
    """Custom type ipadFrPortStatsValidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_IpadFrPortStatsValidIntervals_Type.__name__ = "Integer32"
_IpadFrPortStatsValidIntervals_Object = MibTableColumn
ipadFrPortStatsValidIntervals = _IpadFrPortStatsValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 1, 1, 38),
    _IpadFrPortStatsValidIntervals_Type()
)
ipadFrPortStatsValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadFrPortStatsValidIntervals.setStatus("current")
_IpadDLCIstatsTable_Object = MibTable
ipadDLCIstatsTable = _IpadDLCIstatsTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 2)
)
if mibBuilder.loadTexts:
    ipadDLCIstatsTable.setStatus("current")
_IpadDLCIstatsEntry_Object = MibTableRow
ipadDLCIstatsEntry = _IpadDLCIstatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 2, 1)
)
ipadDLCIstatsEntry.setIndexNames(
    (0, "IPADv2-MIB", "ipadDLCIstatsService"),
    (0, "IPADv2-MIB", "ipadDLCIstatsDLCI"),
    (0, "IPADv2-MIB", "ipadDLCIstatsPeriod"),
)
if mibBuilder.loadTexts:
    ipadDLCIstatsEntry.setStatus("current")
_IpadDLCIstatsService_Type = Integer32
_IpadDLCIstatsService_Object = MibTableColumn
ipadDLCIstatsService = _IpadDLCIstatsService_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 2, 1, 1),
    _IpadDLCIstatsService_Type()
)
ipadDLCIstatsService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDLCIstatsService.setStatus("current")
_IpadDLCIstatsDLCI_Type = Integer32
_IpadDLCIstatsDLCI_Object = MibTableColumn
ipadDLCIstatsDLCI = _IpadDLCIstatsDLCI_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 2, 1, 2),
    _IpadDLCIstatsDLCI_Type()
)
ipadDLCIstatsDLCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDLCIstatsDLCI.setStatus("current")


class _IpadDLCIstatsPeriod_Type(Integer32):
    """Custom type ipadDLCIstatsPeriod based on Integer32"""
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
              74,
              75,
              76,
              77,
              78,
              79,
              80,
              81,
              82,
              83,
              84,
              85,
              86,
              87,
              88,
              89,
              90,
              91,
              92,
              93,
              94,
              95,
              96,
              97,
              98)
        )
    )
    namedValues = NamedValues(
        *(("dlciStatsCurrent", 2),
          ("dlciStatsSummary", 1),
          ("dlciStatsperiod1", 3),
          ("dlciStatsperiod10", 12),
          ("dlciStatsperiod11", 13),
          ("dlciStatsperiod12", 14),
          ("dlciStatsperiod13", 15),
          ("dlciStatsperiod14", 16),
          ("dlciStatsperiod15", 17),
          ("dlciStatsperiod16", 18),
          ("dlciStatsperiod17", 19),
          ("dlciStatsperiod18", 20),
          ("dlciStatsperiod19", 21),
          ("dlciStatsperiod2", 4),
          ("dlciStatsperiod20", 22),
          ("dlciStatsperiod21", 23),
          ("dlciStatsperiod22", 24),
          ("dlciStatsperiod23", 25),
          ("dlciStatsperiod24", 26),
          ("dlciStatsperiod25", 27),
          ("dlciStatsperiod26", 28),
          ("dlciStatsperiod27", 29),
          ("dlciStatsperiod28", 30),
          ("dlciStatsperiod29", 31),
          ("dlciStatsperiod3", 5),
          ("dlciStatsperiod30", 32),
          ("dlciStatsperiod31", 33),
          ("dlciStatsperiod32", 34),
          ("dlciStatsperiod33", 35),
          ("dlciStatsperiod34", 36),
          ("dlciStatsperiod35", 37),
          ("dlciStatsperiod36", 38),
          ("dlciStatsperiod37", 39),
          ("dlciStatsperiod38", 40),
          ("dlciStatsperiod39", 41),
          ("dlciStatsperiod4", 6),
          ("dlciStatsperiod40", 42),
          ("dlciStatsperiod41", 43),
          ("dlciStatsperiod42", 44),
          ("dlciStatsperiod43", 45),
          ("dlciStatsperiod44", 46),
          ("dlciStatsperiod45", 47),
          ("dlciStatsperiod46", 48),
          ("dlciStatsperiod47", 49),
          ("dlciStatsperiod48", 50),
          ("dlciStatsperiod49", 51),
          ("dlciStatsperiod5", 7),
          ("dlciStatsperiod50", 52),
          ("dlciStatsperiod51", 53),
          ("dlciStatsperiod52", 54),
          ("dlciStatsperiod53", 55),
          ("dlciStatsperiod54", 56),
          ("dlciStatsperiod55", 57),
          ("dlciStatsperiod56", 58),
          ("dlciStatsperiod57", 59),
          ("dlciStatsperiod58", 60),
          ("dlciStatsperiod59", 61),
          ("dlciStatsperiod6", 8),
          ("dlciStatsperiod60", 62),
          ("dlciStatsperiod61", 63),
          ("dlciStatsperiod62", 64),
          ("dlciStatsperiod63", 65),
          ("dlciStatsperiod64", 66),
          ("dlciStatsperiod65", 67),
          ("dlciStatsperiod66", 68),
          ("dlciStatsperiod67", 69),
          ("dlciStatsperiod68", 70),
          ("dlciStatsperiod69", 71),
          ("dlciStatsperiod7", 9),
          ("dlciStatsperiod70", 72),
          ("dlciStatsperiod71", 73),
          ("dlciStatsperiod72", 74),
          ("dlciStatsperiod73", 75),
          ("dlciStatsperiod74", 76),
          ("dlciStatsperiod75", 77),
          ("dlciStatsperiod76", 78),
          ("dlciStatsperiod77", 79),
          ("dlciStatsperiod78", 80),
          ("dlciStatsperiod79", 81),
          ("dlciStatsperiod8", 10),
          ("dlciStatsperiod80", 82),
          ("dlciStatsperiod81", 83),
          ("dlciStatsperiod82", 84),
          ("dlciStatsperiod83", 85),
          ("dlciStatsperiod84", 86),
          ("dlciStatsperiod85", 87),
          ("dlciStatsperiod86", 88),
          ("dlciStatsperiod87", 89),
          ("dlciStatsperiod88", 90),
          ("dlciStatsperiod89", 91),
          ("dlciStatsperiod9", 11),
          ("dlciStatsperiod90", 92),
          ("dlciStatsperiod91", 93),
          ("dlciStatsperiod92", 94),
          ("dlciStatsperiod93", 95),
          ("dlciStatsperiod94", 96),
          ("dlciStatsperiod95", 97),
          ("dlciStatsperiod96", 98))
    )


_IpadDLCIstatsPeriod_Type.__name__ = "Integer32"
_IpadDLCIstatsPeriod_Object = MibTableColumn
ipadDLCIstatsPeriod = _IpadDLCIstatsPeriod_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 2, 1, 3),
    _IpadDLCIstatsPeriod_Type()
)
ipadDLCIstatsPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDLCIstatsPeriod.setStatus("current")
_IpadDLCIstatsTxFrames_Type = Integer32
_IpadDLCIstatsTxFrames_Object = MibTableColumn
ipadDLCIstatsTxFrames = _IpadDLCIstatsTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 2, 1, 4),
    _IpadDLCIstatsTxFrames_Type()
)
ipadDLCIstatsTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDLCIstatsTxFrames.setStatus("current")
_IpadDLCIstatsRxFrames_Type = Integer32
_IpadDLCIstatsRxFrames_Object = MibTableColumn
ipadDLCIstatsRxFrames = _IpadDLCIstatsRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 2, 1, 5),
    _IpadDLCIstatsRxFrames_Type()
)
ipadDLCIstatsRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDLCIstatsRxFrames.setStatus("current")
_IpadDLCIstatsTxOctets_Type = Integer32
_IpadDLCIstatsTxOctets_Object = MibTableColumn
ipadDLCIstatsTxOctets = _IpadDLCIstatsTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 2, 1, 6),
    _IpadDLCIstatsTxOctets_Type()
)
ipadDLCIstatsTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDLCIstatsTxOctets.setStatus("current")
_IpadDLCIstatsRxOctets_Type = Integer32
_IpadDLCIstatsRxOctets_Object = MibTableColumn
ipadDLCIstatsRxOctets = _IpadDLCIstatsRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 2, 1, 7),
    _IpadDLCIstatsRxOctets_Type()
)
ipadDLCIstatsRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDLCIstatsRxOctets.setStatus("current")
_IpadDLCIstatsRxFECN_Type = Integer32
_IpadDLCIstatsRxFECN_Object = MibTableColumn
ipadDLCIstatsRxFECN = _IpadDLCIstatsRxFECN_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 2, 1, 8),
    _IpadDLCIstatsRxFECN_Type()
)
ipadDLCIstatsRxFECN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDLCIstatsRxFECN.setStatus("current")
_IpadDLCIstatsRxBECN_Type = Integer32
_IpadDLCIstatsRxBECN_Object = MibTableColumn
ipadDLCIstatsRxBECN = _IpadDLCIstatsRxBECN_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 2, 1, 9),
    _IpadDLCIstatsRxBECN_Type()
)
ipadDLCIstatsRxBECN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDLCIstatsRxBECN.setStatus("current")
_IpadDLCIstatsRxDE_Type = Integer32
_IpadDLCIstatsRxDE_Object = MibTableColumn
ipadDLCIstatsRxDE = _IpadDLCIstatsRxDE_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 2, 1, 10),
    _IpadDLCIstatsRxDE_Type()
)
ipadDLCIstatsRxDE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDLCIstatsRxDE.setStatus("current")
_IpadDLCIstatsTxExcessCIR_Type = Integer32
_IpadDLCIstatsTxExcessCIR_Object = MibTableColumn
ipadDLCIstatsTxExcessCIR = _IpadDLCIstatsTxExcessCIR_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 2, 1, 11),
    _IpadDLCIstatsTxExcessCIR_Type()
)
ipadDLCIstatsTxExcessCIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDLCIstatsTxExcessCIR.setStatus("current")
_IpadDLCIstatsTxExcessBe_Type = Integer32
_IpadDLCIstatsTxExcessBe_Object = MibTableColumn
ipadDLCIstatsTxExcessBe = _IpadDLCIstatsTxExcessBe_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 2, 1, 12),
    _IpadDLCIstatsTxExcessBe_Type()
)
ipadDLCIstatsTxExcessBe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDLCIstatsTxExcessBe.setStatus("current")
_IpadDLCIstatsTxMgmtFrames_Type = Integer32
_IpadDLCIstatsTxMgmtFrames_Object = MibTableColumn
ipadDLCIstatsTxMgmtFrames = _IpadDLCIstatsTxMgmtFrames_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 2, 1, 13),
    _IpadDLCIstatsTxMgmtFrames_Type()
)
ipadDLCIstatsTxMgmtFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDLCIstatsTxMgmtFrames.setStatus("current")
_IpadDLCIstatsRxMgmtFrames_Type = Integer32
_IpadDLCIstatsRxMgmtFrames_Object = MibTableColumn
ipadDLCIstatsRxMgmtFrames = _IpadDLCIstatsRxMgmtFrames_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 2, 1, 14),
    _IpadDLCIstatsRxMgmtFrames_Type()
)
ipadDLCIstatsRxMgmtFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDLCIstatsRxMgmtFrames.setStatus("current")
_IpadDLCIstatsTxMgmtOctets_Type = Integer32
_IpadDLCIstatsTxMgmtOctets_Object = MibTableColumn
ipadDLCIstatsTxMgmtOctets = _IpadDLCIstatsTxMgmtOctets_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 2, 1, 15),
    _IpadDLCIstatsTxMgmtOctets_Type()
)
ipadDLCIstatsTxMgmtOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDLCIstatsTxMgmtOctets.setStatus("current")
_IpadDLCIstatsRxMgmtOctets_Type = Integer32
_IpadDLCIstatsRxMgmtOctets_Object = MibTableColumn
ipadDLCIstatsRxMgmtOctets = _IpadDLCIstatsRxMgmtOctets_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 2, 1, 16),
    _IpadDLCIstatsRxMgmtOctets_Type()
)
ipadDLCIstatsRxMgmtOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDLCIstatsRxMgmtOctets.setStatus("current")
_IpadDLCIstatsPeak_Type = Integer32
_IpadDLCIstatsPeak_Object = MibTableColumn
ipadDLCIstatsPeak = _IpadDLCIstatsPeak_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 2, 1, 17),
    _IpadDLCIstatsPeak_Type()
)
ipadDLCIstatsPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDLCIstatsPeak.setStatus("current")
_IpadDLCIstatsAverage_Type = Integer32
_IpadDLCIstatsAverage_Object = MibTableColumn
ipadDLCIstatsAverage = _IpadDLCIstatsAverage_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 2, 1, 18),
    _IpadDLCIstatsAverage_Type()
)
ipadDLCIstatsAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDLCIstatsAverage.setStatus("current")
_IpadDLCIstatsDelayPeak_Type = Integer32
_IpadDLCIstatsDelayPeak_Object = MibTableColumn
ipadDLCIstatsDelayPeak = _IpadDLCIstatsDelayPeak_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 2, 1, 19),
    _IpadDLCIstatsDelayPeak_Type()
)
ipadDLCIstatsDelayPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDLCIstatsDelayPeak.setStatus("current")
_IpadDLCIstatsDelayAverage_Type = Integer32
_IpadDLCIstatsDelayAverage_Object = MibTableColumn
ipadDLCIstatsDelayAverage = _IpadDLCIstatsDelayAverage_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 2, 1, 20),
    _IpadDLCIstatsDelayAverage_Type()
)
ipadDLCIstatsDelayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDLCIstatsDelayAverage.setStatus("current")
_IpadDLCIstatsRoundTripTimeouts_Type = Integer32
_IpadDLCIstatsRoundTripTimeouts_Object = MibTableColumn
ipadDLCIstatsRoundTripTimeouts = _IpadDLCIstatsRoundTripTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 2, 1, 21),
    _IpadDLCIstatsRoundTripTimeouts_Type()
)
ipadDLCIstatsRoundTripTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDLCIstatsRoundTripTimeouts.setStatus("current")
_IpadDLCIstatsUAS_Type = Integer32
_IpadDLCIstatsUAS_Object = MibTableColumn
ipadDLCIstatsUAS = _IpadDLCIstatsUAS_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 2, 1, 22),
    _IpadDLCIstatsUAS_Type()
)
ipadDLCIstatsUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDLCIstatsUAS.setStatus("current")
_IpadDLCIstatsFdrCir_Type = Integer32
_IpadDLCIstatsFdrCir_Object = MibTableColumn
ipadDLCIstatsFdrCir = _IpadDLCIstatsFdrCir_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 2, 1, 23),
    _IpadDLCIstatsFdrCir_Type()
)
ipadDLCIstatsFdrCir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDLCIstatsFdrCir.setStatus("current")
_IpadDLCIstatsDdrCir_Type = Integer32
_IpadDLCIstatsDdrCir_Object = MibTableColumn
ipadDLCIstatsDdrCir = _IpadDLCIstatsDdrCir_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 2, 1, 24),
    _IpadDLCIstatsDdrCir_Type()
)
ipadDLCIstatsDdrCir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDLCIstatsDdrCir.setStatus("current")
_IpadDLCIstatsFdrBe_Type = Integer32
_IpadDLCIstatsFdrBe_Object = MibTableColumn
ipadDLCIstatsFdrBe = _IpadDLCIstatsFdrBe_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 2, 1, 25),
    _IpadDLCIstatsFdrBe_Type()
)
ipadDLCIstatsFdrBe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDLCIstatsFdrBe.setStatus("current")
_IpadDLCIstatsDdrBe_Type = Integer32
_IpadDLCIstatsDdrBe_Object = MibTableColumn
ipadDLCIstatsDdrBe = _IpadDLCIstatsDdrBe_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 2, 1, 26),
    _IpadDLCIstatsDdrBe_Type()
)
ipadDLCIstatsDdrBe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDLCIstatsDdrBe.setStatus("current")
_IpadDLCIstatsTimeStamp_Type = TimeTicks
_IpadDLCIstatsTimeStamp_Object = MibTableColumn
ipadDLCIstatsTimeStamp = _IpadDLCIstatsTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 2, 1, 27),
    _IpadDLCIstatsTimeStamp_Type()
)
ipadDLCIstatsTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDLCIstatsTimeStamp.setStatus("current")
_IpadDLCIstatsRemoteFramesOfferedWithinCIR_Type = Integer32
_IpadDLCIstatsRemoteFramesOfferedWithinCIR_Object = MibTableColumn
ipadDLCIstatsRemoteFramesOfferedWithinCIR = _IpadDLCIstatsRemoteFramesOfferedWithinCIR_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 2, 1, 28),
    _IpadDLCIstatsRemoteFramesOfferedWithinCIR_Type()
)
ipadDLCIstatsRemoteFramesOfferedWithinCIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDLCIstatsRemoteFramesOfferedWithinCIR.setStatus("current")
_IpadDLCIstatsRemoteFramesOfferedWithinBE_Type = Integer32
_IpadDLCIstatsRemoteFramesOfferedWithinBE_Object = MibTableColumn
ipadDLCIstatsRemoteFramesOfferedWithinBE = _IpadDLCIstatsRemoteFramesOfferedWithinBE_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 2, 1, 29),
    _IpadDLCIstatsRemoteFramesOfferedWithinBE_Type()
)
ipadDLCIstatsRemoteFramesOfferedWithinBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDLCIstatsRemoteFramesOfferedWithinBE.setStatus("current")
_IpadDLCIstatsFramesReceived_Type = Integer32
_IpadDLCIstatsFramesReceived_Object = MibTableColumn
ipadDLCIstatsFramesReceived = _IpadDLCIstatsFramesReceived_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 2, 1, 30),
    _IpadDLCIstatsFramesReceived_Type()
)
ipadDLCIstatsFramesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDLCIstatsFramesReceived.setStatus("current")
_IpadDLCIstatsFDRCIR_Type = DisplayString
_IpadDLCIstatsFDRCIR_Object = MibTableColumn
ipadDLCIstatsFDRCIR = _IpadDLCIstatsFDRCIR_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 2, 1, 31),
    _IpadDLCIstatsFDRCIR_Type()
)
ipadDLCIstatsFDRCIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDLCIstatsFDRCIR.setStatus("current")
_IpadDLCIstatsFDRBE_Type = DisplayString
_IpadDLCIstatsFDRBE_Object = MibTableColumn
ipadDLCIstatsFDRBE = _IpadDLCIstatsFDRBE_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 2, 1, 32),
    _IpadDLCIstatsFDRBE_Type()
)
ipadDLCIstatsFDRBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDLCIstatsFDRBE.setStatus("current")
_IpadDLCIstatsRemoteDataOfferedWithinCIR_Type = Integer32
_IpadDLCIstatsRemoteDataOfferedWithinCIR_Object = MibTableColumn
ipadDLCIstatsRemoteDataOfferedWithinCIR = _IpadDLCIstatsRemoteDataOfferedWithinCIR_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 2, 1, 33),
    _IpadDLCIstatsRemoteDataOfferedWithinCIR_Type()
)
ipadDLCIstatsRemoteDataOfferedWithinCIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDLCIstatsRemoteDataOfferedWithinCIR.setStatus("current")
_IpadDLCIstatsRemoteDataOfferedWithinBE_Type = Integer32
_IpadDLCIstatsRemoteDataOfferedWithinBE_Object = MibTableColumn
ipadDLCIstatsRemoteDataOfferedWithinBE = _IpadDLCIstatsRemoteDataOfferedWithinBE_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 2, 1, 34),
    _IpadDLCIstatsRemoteDataOfferedWithinBE_Type()
)
ipadDLCIstatsRemoteDataOfferedWithinBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDLCIstatsRemoteDataOfferedWithinBE.setStatus("current")
_IpadDLCIstatsDataReceived_Type = Integer32
_IpadDLCIstatsDataReceived_Object = MibTableColumn
ipadDLCIstatsDataReceived = _IpadDLCIstatsDataReceived_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 2, 1, 35),
    _IpadDLCIstatsDataReceived_Type()
)
ipadDLCIstatsDataReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDLCIstatsDataReceived.setStatus("current")
_IpadDLCIstatsDDRCIR_Type = DisplayString
_IpadDLCIstatsDDRCIR_Object = MibTableColumn
ipadDLCIstatsDDRCIR = _IpadDLCIstatsDDRCIR_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 2, 1, 36),
    _IpadDLCIstatsDDRCIR_Type()
)
ipadDLCIstatsDDRCIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDLCIstatsDDRCIR.setStatus("current")
_IpadDLCIstatsDDRBE_Type = DisplayString
_IpadDLCIstatsDDRBE_Object = MibTableColumn
ipadDLCIstatsDDRBE = _IpadDLCIstatsDDRBE_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 2, 1, 37),
    _IpadDLCIstatsDDRBE_Type()
)
ipadDLCIstatsDDRBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDLCIstatsDDRBE.setStatus("current")
_IpadDLCIstatsAvgPercent_Type = Integer32
_IpadDLCIstatsAvgPercent_Object = MibTableColumn
ipadDLCIstatsAvgPercent = _IpadDLCIstatsAvgPercent_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 2, 1, 38),
    _IpadDLCIstatsAvgPercent_Type()
)
ipadDLCIstatsAvgPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDLCIstatsAvgPercent.setStatus("current")
_IpadDLCIstatsMaxPercent_Type = Integer32
_IpadDLCIstatsMaxPercent_Object = MibTableColumn
ipadDLCIstatsMaxPercent = _IpadDLCIstatsMaxPercent_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 2, 1, 39),
    _IpadDLCIstatsMaxPercent_Type()
)
ipadDLCIstatsMaxPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDLCIstatsMaxPercent.setStatus("current")
_IpadDLCIstatsInstantPercent_Type = Integer32
_IpadDLCIstatsInstantPercent_Object = MibTableColumn
ipadDLCIstatsInstantPercent = _IpadDLCIstatsInstantPercent_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 2, 1, 40),
    _IpadDLCIstatsInstantPercent_Type()
)
ipadDLCIstatsInstantPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDLCIstatsInstantPercent.setStatus("current")
_IpadDLCIstats20PercentSec_Type = Integer32
_IpadDLCIstats20PercentSec_Object = MibTableColumn
ipadDLCIstats20PercentSec = _IpadDLCIstats20PercentSec_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 2, 1, 41),
    _IpadDLCIstats20PercentSec_Type()
)
ipadDLCIstats20PercentSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDLCIstats20PercentSec.setStatus("current")
_IpadDLCIstats40PercentSec_Type = Integer32
_IpadDLCIstats40PercentSec_Object = MibTableColumn
ipadDLCIstats40PercentSec = _IpadDLCIstats40PercentSec_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 2, 1, 42),
    _IpadDLCIstats40PercentSec_Type()
)
ipadDLCIstats40PercentSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDLCIstats40PercentSec.setStatus("current")
_IpadDLCIstats60PercentSec_Type = Integer32
_IpadDLCIstats60PercentSec_Object = MibTableColumn
ipadDLCIstats60PercentSec = _IpadDLCIstats60PercentSec_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 2, 1, 43),
    _IpadDLCIstats60PercentSec_Type()
)
ipadDLCIstats60PercentSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDLCIstats60PercentSec.setStatus("current")
_IpadDLCIstats80PercentSec_Type = Integer32
_IpadDLCIstats80PercentSec_Object = MibTableColumn
ipadDLCIstats80PercentSec = _IpadDLCIstats80PercentSec_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 2, 1, 44),
    _IpadDLCIstats80PercentSec_Type()
)
ipadDLCIstats80PercentSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDLCIstats80PercentSec.setStatus("current")
_IpadDLCIstats100PercentSec_Type = Integer32
_IpadDLCIstats100PercentSec_Object = MibTableColumn
ipadDLCIstats100PercentSec = _IpadDLCIstats100PercentSec_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 2, 1, 45),
    _IpadDLCIstats100PercentSec_Type()
)
ipadDLCIstats100PercentSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDLCIstats100PercentSec.setStatus("current")


class _IpadDLCIstatsValidIntervals_Type(Integer32):
    """Custom type ipadDLCIstatsValidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_IpadDLCIstatsValidIntervals_Type.__name__ = "Integer32"
_IpadDLCIstatsValidIntervals_Object = MibTableColumn
ipadDLCIstatsValidIntervals = _IpadDLCIstatsValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 2, 1, 46),
    _IpadDLCIstatsValidIntervals_Type()
)
ipadDLCIstatsValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDLCIstatsValidIntervals.setStatus("current")
_IpadDLCIstatsCompressionTxOctetsIn_Type = Integer32
_IpadDLCIstatsCompressionTxOctetsIn_Object = MibTableColumn
ipadDLCIstatsCompressionTxOctetsIn = _IpadDLCIstatsCompressionTxOctetsIn_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 2, 1, 47),
    _IpadDLCIstatsCompressionTxOctetsIn_Type()
)
ipadDLCIstatsCompressionTxOctetsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDLCIstatsCompressionTxOctetsIn.setStatus("current")
_IpadDLCIstatsCompressionTxOctetsOut_Type = Integer32
_IpadDLCIstatsCompressionTxOctetsOut_Object = MibTableColumn
ipadDLCIstatsCompressionTxOctetsOut = _IpadDLCIstatsCompressionTxOctetsOut_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 2, 1, 48),
    _IpadDLCIstatsCompressionTxOctetsOut_Type()
)
ipadDLCIstatsCompressionTxOctetsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDLCIstatsCompressionTxOctetsOut.setStatus("current")
_IpadDLCIstatsCompressionRxOctetsIn_Type = Integer32
_IpadDLCIstatsCompressionRxOctetsIn_Object = MibTableColumn
ipadDLCIstatsCompressionRxOctetsIn = _IpadDLCIstatsCompressionRxOctetsIn_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 2, 1, 49),
    _IpadDLCIstatsCompressionRxOctetsIn_Type()
)
ipadDLCIstatsCompressionRxOctetsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDLCIstatsCompressionRxOctetsIn.setStatus("current")
_IpadDLCIstatsCompressionRxOctetsOut_Type = Integer32
_IpadDLCIstatsCompressionRxOctetsOut_Object = MibTableColumn
ipadDLCIstatsCompressionRxOctetsOut = _IpadDLCIstatsCompressionRxOctetsOut_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 2, 1, 50),
    _IpadDLCIstatsCompressionRxOctetsOut_Type()
)
ipadDLCIstatsCompressionRxOctetsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDLCIstatsCompressionRxOctetsOut.setStatus("current")
_IpadDLCIstatsCompressionTxRatio_Type = DisplayString
_IpadDLCIstatsCompressionTxRatio_Object = MibTableColumn
ipadDLCIstatsCompressionTxRatio = _IpadDLCIstatsCompressionTxRatio_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 2, 1, 51),
    _IpadDLCIstatsCompressionTxRatio_Type()
)
ipadDLCIstatsCompressionTxRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDLCIstatsCompressionTxRatio.setStatus("current")
_IpadDLCIstatsCompressionRxRatio_Type = DisplayString
_IpadDLCIstatsCompressionRxRatio_Object = MibTableColumn
ipadDLCIstatsCompressionRxRatio = _IpadDLCIstatsCompressionRxRatio_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 2, 1, 52),
    _IpadDLCIstatsCompressionRxRatio_Type()
)
ipadDLCIstatsCompressionRxRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDLCIstatsCompressionRxRatio.setStatus("current")
_IpadUserStatsTable_Object = MibTable
ipadUserStatsTable = _IpadUserStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 3)
)
if mibBuilder.loadTexts:
    ipadUserStatsTable.setStatus("current")
_IpadUserStatsEntry_Object = MibTableRow
ipadUserStatsEntry = _IpadUserStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 3, 1)
)
ipadUserStatsEntry.setIndexNames(
    (0, "IPADv2-MIB", "ipadUserStatsIndex"),
    (0, "IPADv2-MIB", "ipadUserStatsPeriod"),
)
if mibBuilder.loadTexts:
    ipadUserStatsEntry.setStatus("current")
_IpadUserStatsIndex_Type = Integer32
_IpadUserStatsIndex_Object = MibTableColumn
ipadUserStatsIndex = _IpadUserStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 3, 1, 1),
    _IpadUserStatsIndex_Type()
)
ipadUserStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadUserStatsIndex.setStatus("current")


class _IpadUserStatsPeriod_Type(Integer32):
    """Custom type ipadUserStatsPeriod based on Integer32"""
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
              74,
              75,
              76,
              77,
              78,
              79,
              80,
              81,
              82,
              83,
              84,
              85,
              86,
              87,
              88,
              89,
              90,
              91,
              92,
              93,
              94,
              95,
              96,
              97,
              98)
        )
    )
    namedValues = NamedValues(
        *(("userStatsCurrent", 2),
          ("userStatsSummary", 1),
          ("userStatsperiod1", 3),
          ("userStatsperiod10", 12),
          ("userStatsperiod11", 13),
          ("userStatsperiod12", 14),
          ("userStatsperiod13", 15),
          ("userStatsperiod14", 16),
          ("userStatsperiod15", 17),
          ("userStatsperiod16", 18),
          ("userStatsperiod17", 19),
          ("userStatsperiod18", 20),
          ("userStatsperiod19", 21),
          ("userStatsperiod2", 4),
          ("userStatsperiod20", 22),
          ("userStatsperiod21", 23),
          ("userStatsperiod22", 24),
          ("userStatsperiod23", 25),
          ("userStatsperiod24", 26),
          ("userStatsperiod25", 27),
          ("userStatsperiod26", 28),
          ("userStatsperiod27", 29),
          ("userStatsperiod28", 30),
          ("userStatsperiod29", 31),
          ("userStatsperiod3", 5),
          ("userStatsperiod30", 32),
          ("userStatsperiod31", 33),
          ("userStatsperiod32", 34),
          ("userStatsperiod33", 35),
          ("userStatsperiod34", 36),
          ("userStatsperiod35", 37),
          ("userStatsperiod36", 38),
          ("userStatsperiod37", 39),
          ("userStatsperiod38", 40),
          ("userStatsperiod39", 41),
          ("userStatsperiod4", 6),
          ("userStatsperiod40", 42),
          ("userStatsperiod41", 43),
          ("userStatsperiod42", 44),
          ("userStatsperiod43", 45),
          ("userStatsperiod44", 46),
          ("userStatsperiod45", 47),
          ("userStatsperiod46", 48),
          ("userStatsperiod47", 49),
          ("userStatsperiod48", 50),
          ("userStatsperiod49", 51),
          ("userStatsperiod5", 7),
          ("userStatsperiod50", 52),
          ("userStatsperiod51", 53),
          ("userStatsperiod52", 54),
          ("userStatsperiod53", 55),
          ("userStatsperiod54", 56),
          ("userStatsperiod55", 57),
          ("userStatsperiod56", 58),
          ("userStatsperiod57", 59),
          ("userStatsperiod58", 60),
          ("userStatsperiod59", 61),
          ("userStatsperiod6", 8),
          ("userStatsperiod60", 62),
          ("userStatsperiod61", 63),
          ("userStatsperiod62", 64),
          ("userStatsperiod63", 65),
          ("userStatsperiod64", 66),
          ("userStatsperiod65", 67),
          ("userStatsperiod66", 68),
          ("userStatsperiod67", 69),
          ("userStatsperiod68", 70),
          ("userStatsperiod69", 71),
          ("userStatsperiod7", 9),
          ("userStatsperiod70", 72),
          ("userStatsperiod71", 73),
          ("userStatsperiod72", 74),
          ("userStatsperiod73", 75),
          ("userStatsperiod74", 76),
          ("userStatsperiod75", 77),
          ("userStatsperiod76", 78),
          ("userStatsperiod77", 79),
          ("userStatsperiod78", 80),
          ("userStatsperiod79", 81),
          ("userStatsperiod8", 10),
          ("userStatsperiod80", 82),
          ("userStatsperiod81", 83),
          ("userStatsperiod82", 84),
          ("userStatsperiod83", 85),
          ("userStatsperiod84", 86),
          ("userStatsperiod85", 87),
          ("userStatsperiod86", 88),
          ("userStatsperiod87", 89),
          ("userStatsperiod88", 90),
          ("userStatsperiod89", 91),
          ("userStatsperiod9", 11),
          ("userStatsperiod90", 92),
          ("userStatsperiod91", 93),
          ("userStatsperiod92", 94),
          ("userStatsperiod93", 95),
          ("userStatsperiod94", 96),
          ("userStatsperiod95", 97),
          ("userStatsperiod96", 98))
    )


_IpadUserStatsPeriod_Type.__name__ = "Integer32"
_IpadUserStatsPeriod_Object = MibTableColumn
ipadUserStatsPeriod = _IpadUserStatsPeriod_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 3, 1, 2),
    _IpadUserStatsPeriod_Type()
)
ipadUserStatsPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadUserStatsPeriod.setStatus("current")
_IpadUserStatsTxFrames_Type = Integer32
_IpadUserStatsTxFrames_Object = MibTableColumn
ipadUserStatsTxFrames = _IpadUserStatsTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 3, 1, 3),
    _IpadUserStatsTxFrames_Type()
)
ipadUserStatsTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadUserStatsTxFrames.setStatus("current")
_IpadUserStatsRxFrames_Type = Integer32
_IpadUserStatsRxFrames_Object = MibTableColumn
ipadUserStatsRxFrames = _IpadUserStatsRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 3, 1, 4),
    _IpadUserStatsRxFrames_Type()
)
ipadUserStatsRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadUserStatsRxFrames.setStatus("current")
_IpadUserStatsTxOctets_Type = Integer32
_IpadUserStatsTxOctets_Object = MibTableColumn
ipadUserStatsTxOctets = _IpadUserStatsTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 3, 1, 5),
    _IpadUserStatsTxOctets_Type()
)
ipadUserStatsTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadUserStatsTxOctets.setStatus("current")
_IpadUserStatsRxOctets_Type = Integer32
_IpadUserStatsRxOctets_Object = MibTableColumn
ipadUserStatsRxOctets = _IpadUserStatsRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 3, 1, 6),
    _IpadUserStatsRxOctets_Type()
)
ipadUserStatsRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadUserStatsRxOctets.setStatus("current")
_IpadUserStatsTxRatePeak_Type = Integer32
_IpadUserStatsTxRatePeak_Object = MibTableColumn
ipadUserStatsTxRatePeak = _IpadUserStatsTxRatePeak_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 3, 1, 7),
    _IpadUserStatsTxRatePeak_Type()
)
ipadUserStatsTxRatePeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadUserStatsTxRatePeak.setStatus("current")
_IpadUserStatsTxRateAverage_Type = Integer32
_IpadUserStatsTxRateAverage_Object = MibTableColumn
ipadUserStatsTxRateAverage = _IpadUserStatsTxRateAverage_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 3, 1, 8),
    _IpadUserStatsTxRateAverage_Type()
)
ipadUserStatsTxRateAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadUserStatsTxRateAverage.setStatus("current")
_IpadUserStatsTimeStamp_Type = TimeTicks
_IpadUserStatsTimeStamp_Object = MibTableColumn
ipadUserStatsTimeStamp = _IpadUserStatsTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 3, 1, 9),
    _IpadUserStatsTimeStamp_Type()
)
ipadUserStatsTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadUserStatsTimeStamp.setStatus("current")
_IpadIPTopNStatsTable_Object = MibTable
ipadIPTopNStatsTable = _IpadIPTopNStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 4)
)
if mibBuilder.loadTexts:
    ipadIPTopNStatsTable.setStatus("current")
_IpadIPTopNStatsEntry_Object = MibTableRow
ipadIPTopNStatsEntry = _IpadIPTopNStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 4, 1)
)
ipadIPTopNStatsEntry.setIndexNames(
    (0, "IPADv2-MIB", "ipadIPTopNStatsIndex"),
)
if mibBuilder.loadTexts:
    ipadIPTopNStatsEntry.setStatus("current")
_IpadIPTopNStatsIndex_Type = Integer32
_IpadIPTopNStatsIndex_Object = MibTableColumn
ipadIPTopNStatsIndex = _IpadIPTopNStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 4, 1, 1),
    _IpadIPTopNStatsIndex_Type()
)
ipadIPTopNStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadIPTopNStatsIndex.setStatus("current")


class _IpadIPTopNStatsAddress_Type(OctetString):
    """Custom type ipadIPTopNStatsAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_IpadIPTopNStatsAddress_Type.__name__ = "OctetString"
_IpadIPTopNStatsAddress_Object = MibTableColumn
ipadIPTopNStatsAddress = _IpadIPTopNStatsAddress_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 4, 1, 2),
    _IpadIPTopNStatsAddress_Type()
)
ipadIPTopNStatsAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadIPTopNStatsAddress.setStatus("current")
_IpadIPTopNStatsTimestamp_Type = TimeTicks
_IpadIPTopNStatsTimestamp_Object = MibTableColumn
ipadIPTopNStatsTimestamp = _IpadIPTopNStatsTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 4, 1, 3),
    _IpadIPTopNStatsTimestamp_Type()
)
ipadIPTopNStatsTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadIPTopNStatsTimestamp.setStatus("current")
_IpadIPTopNStatsRxFrames_Type = Integer32
_IpadIPTopNStatsRxFrames_Object = MibTableColumn
ipadIPTopNStatsRxFrames = _IpadIPTopNStatsRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 4, 1, 4),
    _IpadIPTopNStatsRxFrames_Type()
)
ipadIPTopNStatsRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadIPTopNStatsRxFrames.setStatus("current")
_IpadIPTopNStatsRxOctets_Type = Integer32
_IpadIPTopNStatsRxOctets_Object = MibTableColumn
ipadIPTopNStatsRxOctets = _IpadIPTopNStatsRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 4, 1, 5),
    _IpadIPTopNStatsRxOctets_Type()
)
ipadIPTopNStatsRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadIPTopNStatsRxOctets.setStatus("current")
_IpadIPTopNStatsTxFrames_Type = Integer32
_IpadIPTopNStatsTxFrames_Object = MibTableColumn
ipadIPTopNStatsTxFrames = _IpadIPTopNStatsTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 4, 1, 6),
    _IpadIPTopNStatsTxFrames_Type()
)
ipadIPTopNStatsTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadIPTopNStatsTxFrames.setStatus("current")
_IpadIPTopNStatsTxOctets_Type = Integer32
_IpadIPTopNStatsTxOctets_Object = MibTableColumn
ipadIPTopNStatsTxOctets = _IpadIPTopNStatsTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 4, 1, 7),
    _IpadIPTopNStatsTxOctets_Type()
)
ipadIPTopNStatsTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadIPTopNStatsTxOctets.setStatus("current")
_IpadPktSwitch_ObjectIdentity = ObjectIdentity
ipadPktSwitch = _IpadPktSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 10)
)


class _IpadPktSwOperatingMode_Type(Integer32):
    """Custom type ipadPktSwOperatingMode based on Integer32"""
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
              25)
        )
    )
    namedValues = NamedValues(
        *(("monitor", 3),
          ("other", 1),
          ("packet", 4),
          ("profile10", 14),
          ("profile11", 15),
          ("profile12", 16),
          ("profile13", 17),
          ("profile14", 18),
          ("profile15", 19),
          ("profile16", 20),
          ("profile17", 21),
          ("profile18", 22),
          ("profile19", 23),
          ("profile2", 6),
          ("profile20", 24),
          ("profile21", 25),
          ("profile3", 7),
          ("profile4", 8),
          ("profile5", 9),
          ("profile6", 10),
          ("profile7", 11),
          ("profile8", 12),
          ("profile9", 13),
          ("remoteConfig", 5),
          ("tdm", 2))
    )


_IpadPktSwOperatingMode_Type.__name__ = "Integer32"
_IpadPktSwOperatingMode_Object = MibScalar
ipadPktSwOperatingMode = _IpadPktSwOperatingMode_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 10, 1),
    _IpadPktSwOperatingMode_Type()
)
ipadPktSwOperatingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadPktSwOperatingMode.setStatus("current")
_IpadPktSwCfgTable_Object = MibTable
ipadPktSwCfgTable = _IpadPktSwCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 10, 2)
)
if mibBuilder.loadTexts:
    ipadPktSwCfgTable.setStatus("current")
_IpadPktSwCfgTableEntry_Object = MibTableRow
ipadPktSwCfgTableEntry = _IpadPktSwCfgTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 10, 2, 1)
)
ipadPktSwCfgTableEntry.setIndexNames(
    (0, "IPADv2-MIB", "ipadPktSwCfgService"),
)
if mibBuilder.loadTexts:
    ipadPktSwCfgTableEntry.setStatus("current")
_IpadPktSwCfgService_Type = Integer32
_IpadPktSwCfgService_Object = MibTableColumn
ipadPktSwCfgService = _IpadPktSwCfgService_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 10, 2, 1, 1),
    _IpadPktSwCfgService_Type()
)
ipadPktSwCfgService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadPktSwCfgService.setStatus("current")


class _IpadPktSwCfgInterfaceType_Type(Integer32):
    """Custom type ipadPktSwCfgInterfaceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ni", 2),
          ("nni", 3),
          ("uni", 1))
    )


_IpadPktSwCfgInterfaceType_Type.__name__ = "Integer32"
_IpadPktSwCfgInterfaceType_Object = MibTableColumn
ipadPktSwCfgInterfaceType = _IpadPktSwCfgInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 10, 2, 1, 2),
    _IpadPktSwCfgInterfaceType_Type()
)
ipadPktSwCfgInterfaceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadPktSwCfgInterfaceType.setStatus("current")


class _IpadPktSwCfgLnkMgmtType_Type(Integer32):
    """Custom type ipadPktSwCfgLnkMgmtType based on Integer32"""
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
        *(("ansi", 4),
          ("auto", 2),
          ("ccitt", 3),
          ("lmi", 5),
          ("none", 6),
          ("other", 1))
    )


_IpadPktSwCfgLnkMgmtType_Type.__name__ = "Integer32"
_IpadPktSwCfgLnkMgmtType_Object = MibTableColumn
ipadPktSwCfgLnkMgmtType = _IpadPktSwCfgLnkMgmtType_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 10, 2, 1, 3),
    _IpadPktSwCfgLnkMgmtType_Type()
)
ipadPktSwCfgLnkMgmtType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadPktSwCfgLnkMgmtType.setStatus("current")
_IpadPktSwCfgMaxFrameSize_Type = Integer32
_IpadPktSwCfgMaxFrameSize_Object = MibTableColumn
ipadPktSwCfgMaxFrameSize = _IpadPktSwCfgMaxFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 10, 2, 1, 4),
    _IpadPktSwCfgMaxFrameSize_Type()
)
ipadPktSwCfgMaxFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadPktSwCfgMaxFrameSize.setStatus("current")
_IpadPktSwCfgnN1_Type = Integer32
_IpadPktSwCfgnN1_Object = MibTableColumn
ipadPktSwCfgnN1 = _IpadPktSwCfgnN1_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 10, 2, 1, 5),
    _IpadPktSwCfgnN1_Type()
)
ipadPktSwCfgnN1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadPktSwCfgnN1.setStatus("current")
_IpadPktSwCfgnN2_Type = Integer32
_IpadPktSwCfgnN2_Object = MibTableColumn
ipadPktSwCfgnN2 = _IpadPktSwCfgnN2_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 10, 2, 1, 6),
    _IpadPktSwCfgnN2_Type()
)
ipadPktSwCfgnN2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadPktSwCfgnN2.setStatus("current")
_IpadPktSwCfgnN3_Type = Integer32
_IpadPktSwCfgnN3_Object = MibTableColumn
ipadPktSwCfgnN3 = _IpadPktSwCfgnN3_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 10, 2, 1, 7),
    _IpadPktSwCfgnN3_Type()
)
ipadPktSwCfgnN3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadPktSwCfgnN3.setStatus("current")
_IpadPktSwCfgnT1_Type = Integer32
_IpadPktSwCfgnT1_Object = MibTableColumn
ipadPktSwCfgnT1 = _IpadPktSwCfgnT1_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 10, 2, 1, 8),
    _IpadPktSwCfgnT1_Type()
)
ipadPktSwCfgnT1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadPktSwCfgnT1.setStatus("current")
_IpadPktSwCfgDefCIR_Type = Integer32
_IpadPktSwCfgDefCIR_Object = MibTableColumn
ipadPktSwCfgDefCIR = _IpadPktSwCfgDefCIR_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 10, 2, 1, 9),
    _IpadPktSwCfgDefCIR_Type()
)
ipadPktSwCfgDefCIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadPktSwCfgDefCIR.setStatus("current")
_IpadPktSwCfgDefExBurst_Type = Integer32
_IpadPktSwCfgDefExBurst_Object = MibTableColumn
ipadPktSwCfgDefExBurst = _IpadPktSwCfgDefExBurst_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 10, 2, 1, 10),
    _IpadPktSwCfgDefExBurst_Type()
)
ipadPktSwCfgDefExBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadPktSwCfgDefExBurst.setStatus("current")


class _IpadPktSwCfgCIREE_Type(Integer32):
    """Custom type ipadPktSwCfgCIREE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("other", 1),
          ("yes", 3))
    )


_IpadPktSwCfgCIREE_Type.__name__ = "Integer32"
_IpadPktSwCfgCIREE_Object = MibTableColumn
ipadPktSwCfgCIREE = _IpadPktSwCfgCIREE_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 10, 2, 1, 11),
    _IpadPktSwCfgCIREE_Type()
)
ipadPktSwCfgCIREE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadPktSwCfgCIREE.setStatus("current")


class _IpadPktSwCfgLinkInjection_Type(Integer32):
    """Custom type ipadPktSwCfgLinkInjection based on Integer32"""
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
        *(("buffered", 3),
          ("forced", 4),
          ("other", 1),
          ("standard", 2))
    )


_IpadPktSwCfgLinkInjection_Type.__name__ = "Integer32"
_IpadPktSwCfgLinkInjection_Object = MibTableColumn
ipadPktSwCfgLinkInjection = _IpadPktSwCfgLinkInjection_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 10, 2, 1, 12),
    _IpadPktSwCfgLinkInjection_Type()
)
ipadPktSwCfgLinkInjection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadPktSwCfgLinkInjection.setStatus("current")


class _IpadPktSwCfgAutoDiagnostic_Type(Integer32):
    """Custom type ipadPktSwCfgAutoDiagnostic based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("other", 1),
          ("yes", 3))
    )


_IpadPktSwCfgAutoDiagnostic_Type.__name__ = "Integer32"
_IpadPktSwCfgAutoDiagnostic_Object = MibTableColumn
ipadPktSwCfgAutoDiagnostic = _IpadPktSwCfgAutoDiagnostic_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 10, 2, 1, 13),
    _IpadPktSwCfgAutoDiagnostic_Type()
)
ipadPktSwCfgAutoDiagnostic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadPktSwCfgAutoDiagnostic.setStatus("current")


class _IpadPktSwCfgAutoDiscovery_Type(Integer32):
    """Custom type ipadPktSwCfgAutoDiscovery based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("other", 1),
          ("yes", 3))
    )


_IpadPktSwCfgAutoDiscovery_Type.__name__ = "Integer32"
_IpadPktSwCfgAutoDiscovery_Object = MibTableColumn
ipadPktSwCfgAutoDiscovery = _IpadPktSwCfgAutoDiscovery_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 10, 2, 1, 14),
    _IpadPktSwCfgAutoDiscovery_Type()
)
ipadPktSwCfgAutoDiscovery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadPktSwCfgAutoDiscovery.setStatus("current")


class _IpadPktSwCfgMgmtDLCI_Type(Integer32):
    """Custom type ipadPktSwCfgMgmtDLCI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_IpadPktSwCfgMgmtDLCI_Type.__name__ = "Integer32"
_IpadPktSwCfgMgmtDLCI_Object = MibTableColumn
ipadPktSwCfgMgmtDLCI = _IpadPktSwCfgMgmtDLCI_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 10, 2, 1, 15),
    _IpadPktSwCfgMgmtDLCI_Type()
)
ipadPktSwCfgMgmtDLCI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadPktSwCfgMgmtDLCI.setStatus("current")


class _IpadPktSwCfgRoundTripDelaySize_Type(Integer32):
    """Custom type ipadPktSwCfgRoundTripDelaySize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1500),
    )


_IpadPktSwCfgRoundTripDelaySize_Type.__name__ = "Integer32"
_IpadPktSwCfgRoundTripDelaySize_Object = MibTableColumn
ipadPktSwCfgRoundTripDelaySize = _IpadPktSwCfgRoundTripDelaySize_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 10, 2, 1, 16),
    _IpadPktSwCfgRoundTripDelaySize_Type()
)
ipadPktSwCfgRoundTripDelaySize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadPktSwCfgRoundTripDelaySize.setStatus("current")


class _IpadPktSwCfgRoundTripDelayRate_Type(Integer32):
    """Custom type ipadPktSwCfgRoundTripDelayRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 900),
    )


_IpadPktSwCfgRoundTripDelayRate_Type.__name__ = "Integer32"
_IpadPktSwCfgRoundTripDelayRate_Object = MibTableColumn
ipadPktSwCfgRoundTripDelayRate = _IpadPktSwCfgRoundTripDelayRate_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 10, 2, 1, 17),
    _IpadPktSwCfgRoundTripDelayRate_Type()
)
ipadPktSwCfgRoundTripDelayRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadPktSwCfgRoundTripDelayRate.setStatus("current")


class _IpadPktSwCfgAutoIPMgmtAddr_Type(Integer32):
    """Custom type ipadPktSwCfgAutoIPMgmtAddr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("other", 1),
          ("yes", 3))
    )


_IpadPktSwCfgAutoIPMgmtAddr_Type.__name__ = "Integer32"
_IpadPktSwCfgAutoIPMgmtAddr_Object = MibTableColumn
ipadPktSwCfgAutoIPMgmtAddr = _IpadPktSwCfgAutoIPMgmtAddr_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 10, 2, 1, 18),
    _IpadPktSwCfgAutoIPMgmtAddr_Type()
)
ipadPktSwCfgAutoIPMgmtAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadPktSwCfgAutoIPMgmtAddr.setStatus("current")


class _IpadPktSwCfgNormalTxQueueSize_Type(Integer32):
    """Custom type ipadPktSwCfgNormalTxQueueSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_IpadPktSwCfgNormalTxQueueSize_Type.__name__ = "Integer32"
_IpadPktSwCfgNormalTxQueueSize_Object = MibTableColumn
ipadPktSwCfgNormalTxQueueSize = _IpadPktSwCfgNormalTxQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 10, 2, 1, 19),
    _IpadPktSwCfgNormalTxQueueSize_Type()
)
ipadPktSwCfgNormalTxQueueSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadPktSwCfgNormalTxQueueSize.setStatus("current")
_IpadPktSwCfgAddDLCI_Type = Integer32
_IpadPktSwCfgAddDLCI_Object = MibTableColumn
ipadPktSwCfgAddDLCI = _IpadPktSwCfgAddDLCI_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 10, 2, 1, 20),
    _IpadPktSwCfgAddDLCI_Type()
)
ipadPktSwCfgAddDLCI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadPktSwCfgAddDLCI.setStatus("current")
_IpadPktSwCfgDeleteDLCI_Type = Integer32
_IpadPktSwCfgDeleteDLCI_Object = MibTableColumn
ipadPktSwCfgDeleteDLCI = _IpadPktSwCfgDeleteDLCI_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 10, 2, 1, 21),
    _IpadPktSwCfgDeleteDLCI_Type()
)
ipadPktSwCfgDeleteDLCI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadPktSwCfgDeleteDLCI.setStatus("current")
_IpadTrapDest_ObjectIdentity = ObjectIdentity
ipadTrapDest = _IpadTrapDest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 11)
)
_IpadTrapDestTable_Object = MibTable
ipadTrapDestTable = _IpadTrapDestTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 11, 1)
)
if mibBuilder.loadTexts:
    ipadTrapDestTable.setStatus("current")
_IpadTrapDestTableEntry_Object = MibTableRow
ipadTrapDestTableEntry = _IpadTrapDestTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 11, 1, 1)
)
ipadTrapDestTableEntry.setIndexNames(
    (0, "IPADv2-MIB", "ipadTrapDestIndex"),
)
if mibBuilder.loadTexts:
    ipadTrapDestTableEntry.setStatus("current")
_IpadTrapDestIndex_Type = Integer32
_IpadTrapDestIndex_Object = MibTableColumn
ipadTrapDestIndex = _IpadTrapDestIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 11, 1, 1, 1),
    _IpadTrapDestIndex_Type()
)
ipadTrapDestIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadTrapDestIndex.setStatus("current")
_IpadTrapDestination_Type = IpAddress
_IpadTrapDestination_Object = MibTableColumn
ipadTrapDestination = _IpadTrapDestination_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 11, 1, 1, 2),
    _IpadTrapDestination_Type()
)
ipadTrapDestination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadTrapDestination.setStatus("current")
_IpadMisc_ObjectIdentity = ObjectIdentity
ipadMisc = _IpadMisc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 12)
)
_IpadMiscPortSettings_Object = MibTable
ipadMiscPortSettings = _IpadMiscPortSettings_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 12, 1)
)
if mibBuilder.loadTexts:
    ipadMiscPortSettings.setStatus("current")
_IpadMiscPortSettingsEntry_Object = MibTableRow
ipadMiscPortSettingsEntry = _IpadMiscPortSettingsEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 12, 1, 1)
)
ipadMiscPortSettingsEntry.setIndexNames(
    (0, "IPADv2-MIB", "ipadMiscPortSettingsIndex"),
)
if mibBuilder.loadTexts:
    ipadMiscPortSettingsEntry.setStatus("current")
_IpadMiscPortSettingsIndex_Type = Integer32
_IpadMiscPortSettingsIndex_Object = MibTableColumn
ipadMiscPortSettingsIndex = _IpadMiscPortSettingsIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 12, 1, 1, 1),
    _IpadMiscPortSettingsIndex_Type()
)
ipadMiscPortSettingsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadMiscPortSettingsIndex.setStatus("current")


class _IpadMiscPortSettingsSerialType_Type(Integer32):
    """Custom type ipadMiscPortSettingsSerialType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dce", 2),
          ("dte", 3),
          ("other", 1))
    )


_IpadMiscPortSettingsSerialType_Type.__name__ = "Integer32"
_IpadMiscPortSettingsSerialType_Object = MibTableColumn
ipadMiscPortSettingsSerialType = _IpadMiscPortSettingsSerialType_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 12, 1, 1, 2),
    _IpadMiscPortSettingsSerialType_Type()
)
ipadMiscPortSettingsSerialType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadMiscPortSettingsSerialType.setStatus("current")


class _IpadMiscPortSettingsModemControl_Type(Integer32):
    """Custom type ipadMiscPortSettingsModemControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 3),
          ("other", 1))
    )


_IpadMiscPortSettingsModemControl_Type.__name__ = "Integer32"
_IpadMiscPortSettingsModemControl_Object = MibTableColumn
ipadMiscPortSettingsModemControl = _IpadMiscPortSettingsModemControl_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 12, 1, 1, 3),
    _IpadMiscPortSettingsModemControl_Type()
)
ipadMiscPortSettingsModemControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadMiscPortSettingsModemControl.setStatus("current")


class _IpadMiscClearStatusCounts_Type(Integer32):
    """Custom type ipadMiscClearStatusCounts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clearAll", 2),
          ("other", 1))
    )


_IpadMiscClearStatusCounts_Type.__name__ = "Integer32"
_IpadMiscClearStatusCounts_Object = MibScalar
ipadMiscClearStatusCounts = _IpadMiscClearStatusCounts_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 12, 2),
    _IpadMiscClearStatusCounts_Type()
)
ipadMiscClearStatusCounts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadMiscClearStatusCounts.setStatus("current")


class _IpadMiscEnableServiceAware_Type(Integer32):
    """Custom type ipadMiscEnableServiceAware based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 3),
          ("other", 1))
    )


_IpadMiscEnableServiceAware_Type.__name__ = "Integer32"
_IpadMiscEnableServiceAware_Object = MibScalar
ipadMiscEnableServiceAware = _IpadMiscEnableServiceAware_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 12, 3),
    _IpadMiscEnableServiceAware_Type()
)
ipadMiscEnableServiceAware.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadMiscEnableServiceAware.setStatus("current")
_IpadMiscShdslConfigTable_Object = MibTable
ipadMiscShdslConfigTable = _IpadMiscShdslConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 12, 4)
)
if mibBuilder.loadTexts:
    ipadMiscShdslConfigTable.setStatus("current")
_IpadMiscShdslConfigEntry_Object = MibTableRow
ipadMiscShdslConfigEntry = _IpadMiscShdslConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 12, 4, 1)
)
ipadMiscShdslConfigEntry.setIndexNames(
    (0, "IPADv2-MIB", "ipadMiscShdslConfigIndex"),
)
if mibBuilder.loadTexts:
    ipadMiscShdslConfigEntry.setStatus("current")
_IpadMiscShdslConfigIndex_Type = Integer32
_IpadMiscShdslConfigIndex_Object = MibTableColumn
ipadMiscShdslConfigIndex = _IpadMiscShdslConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 12, 4, 1, 1),
    _IpadMiscShdslConfigIndex_Type()
)
ipadMiscShdslConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadMiscShdslConfigIndex.setStatus("current")


class _IpadMiscShdslTerminalType_Type(Integer32):
    """Custom type ipadMiscShdslTerminalType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("isXtuC", 2),
          ("isXtuR", 3),
          ("other", 1))
    )


_IpadMiscShdslTerminalType_Type.__name__ = "Integer32"
_IpadMiscShdslTerminalType_Object = MibTableColumn
ipadMiscShdslTerminalType = _IpadMiscShdslTerminalType_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 12, 4, 1, 2),
    _IpadMiscShdslTerminalType_Type()
)
ipadMiscShdslTerminalType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadMiscShdslTerminalType.setStatus("current")


class _IpadMiscShdslTiming_Type(Integer32):
    """Custom type ipadMiscShdslTiming based on Integer32"""
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
        *(("shdslTimingEqDTE", 4),
          ("shdslTimingInternal", 2),
          ("shdslTimingNetwork", 3),
          ("shdslTimingOther", 1),
          ("shdslTimingPort1", 6),
          ("shdslTimingPort2", 7),
          ("shdslTimingStation", 5))
    )


_IpadMiscShdslTiming_Type.__name__ = "Integer32"
_IpadMiscShdslTiming_Object = MibTableColumn
ipadMiscShdslTiming = _IpadMiscShdslTiming_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 12, 4, 1, 3),
    _IpadMiscShdslTiming_Type()
)
ipadMiscShdslTiming.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadMiscShdslTiming.setStatus("current")


class _IpadMiscShdslStationInTiming_Type(Integer32):
    """Custom type ipadMiscShdslStationInTiming based on Integer32"""
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
        *(("shdslStationInTiming1544", 3),
          ("shdslStationInTiming2048", 4),
          ("shdslStationInTimingNX64", 2),
          ("shdslStationInTimingOther", 1))
    )


_IpadMiscShdslStationInTiming_Type.__name__ = "Integer32"
_IpadMiscShdslStationInTiming_Object = MibTableColumn
ipadMiscShdslStationInTiming = _IpadMiscShdslStationInTiming_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 12, 4, 1, 4),
    _IpadMiscShdslStationInTiming_Type()
)
ipadMiscShdslStationInTiming.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadMiscShdslStationInTiming.setStatus("current")
_IpadMiscShdslStationTimingNxMultiple_Type = Integer32
_IpadMiscShdslStationTimingNxMultiple_Object = MibTableColumn
ipadMiscShdslStationTimingNxMultiple = _IpadMiscShdslStationTimingNxMultiple_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 12, 4, 1, 5),
    _IpadMiscShdslStationTimingNxMultiple_Type()
)
ipadMiscShdslStationTimingNxMultiple.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadMiscShdslStationTimingNxMultiple.setStatus("current")


class _IpadMiscShdslAutomaticRetrain_Type(Integer32):
    """Custom type ipadMiscShdslAutomaticRetrain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 3),
          ("other", 1))
    )


_IpadMiscShdslAutomaticRetrain_Type.__name__ = "Integer32"
_IpadMiscShdslAutomaticRetrain_Object = MibTableColumn
ipadMiscShdslAutomaticRetrain = _IpadMiscShdslAutomaticRetrain_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 12, 4, 1, 6),
    _IpadMiscShdslAutomaticRetrain_Type()
)
ipadMiscShdslAutomaticRetrain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadMiscShdslAutomaticRetrain.setStatus("current")
_IpadMiscShdslStatusTable_Object = MibTable
ipadMiscShdslStatusTable = _IpadMiscShdslStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 12, 5)
)
if mibBuilder.loadTexts:
    ipadMiscShdslStatusTable.setStatus("current")
_IpadMiscShdslStatusEntry_Object = MibTableRow
ipadMiscShdslStatusEntry = _IpadMiscShdslStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 12, 5, 1)
)
ipadMiscShdslStatusEntry.setIndexNames(
    (0, "IPADv2-MIB", "ipadMiscShdslStatusIndex"),
)
if mibBuilder.loadTexts:
    ipadMiscShdslStatusEntry.setStatus("current")
_IpadMiscShdslStatusIndex_Type = Integer32
_IpadMiscShdslStatusIndex_Object = MibTableColumn
ipadMiscShdslStatusIndex = _IpadMiscShdslStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 12, 5, 1, 1),
    _IpadMiscShdslStatusIndex_Type()
)
ipadMiscShdslStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadMiscShdslStatusIndex.setStatus("current")


class _IpadMiscShdslConnectionStatus_Type(Integer32):
    """Custom type ipadMiscShdslConnectionStatus based on Integer32"""
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
        *(("data", 4),
          ("handshake", 2),
          ("idle", 1),
          ("training", 3))
    )


_IpadMiscShdslConnectionStatus_Type.__name__ = "Integer32"
_IpadMiscShdslConnectionStatus_Object = MibTableColumn
ipadMiscShdslConnectionStatus = _IpadMiscShdslConnectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 12, 5, 1, 2),
    _IpadMiscShdslConnectionStatus_Type()
)
ipadMiscShdslConnectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadMiscShdslConnectionStatus.setStatus("current")


class _IpadMiscShdslDetailedConnectionStatus_Type(DisplayString):
    """Custom type ipadMiscShdslDetailedConnectionStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_IpadMiscShdslDetailedConnectionStatus_Type.__name__ = "DisplayString"
_IpadMiscShdslDetailedConnectionStatus_Object = MibTableColumn
ipadMiscShdslDetailedConnectionStatus = _IpadMiscShdslDetailedConnectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 12, 5, 1, 3),
    _IpadMiscShdslDetailedConnectionStatus_Type()
)
ipadMiscShdslDetailedConnectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadMiscShdslDetailedConnectionStatus.setStatus("current")
_IpadMiscShdslEOCInMessages_Type = Integer32
_IpadMiscShdslEOCInMessages_Object = MibTableColumn
ipadMiscShdslEOCInMessages = _IpadMiscShdslEOCInMessages_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 12, 5, 1, 4),
    _IpadMiscShdslEOCInMessages_Type()
)
ipadMiscShdslEOCInMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadMiscShdslEOCInMessages.setStatus("current")
_IpadMiscShdslEOCOutMessages_Type = Integer32
_IpadMiscShdslEOCOutMessages_Object = MibTableColumn
ipadMiscShdslEOCOutMessages = _IpadMiscShdslEOCOutMessages_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 12, 5, 1, 5),
    _IpadMiscShdslEOCOutMessages_Type()
)
ipadMiscShdslEOCOutMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadMiscShdslEOCOutMessages.setStatus("current")


class _IpadMiscShdslConnectionStatusPair2_Type(Integer32):
    """Custom type ipadMiscShdslConnectionStatusPair2 based on Integer32"""
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
        *(("data", 4),
          ("handshake", 2),
          ("idle", 1),
          ("training", 3))
    )


_IpadMiscShdslConnectionStatusPair2_Type.__name__ = "Integer32"
_IpadMiscShdslConnectionStatusPair2_Object = MibTableColumn
ipadMiscShdslConnectionStatusPair2 = _IpadMiscShdslConnectionStatusPair2_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 12, 5, 1, 6),
    _IpadMiscShdslConnectionStatusPair2_Type()
)
ipadMiscShdslConnectionStatusPair2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadMiscShdslConnectionStatusPair2.setStatus("current")


class _IpadMiscShdslDetailedConnectionStatusPair2_Type(DisplayString):
    """Custom type ipadMiscShdslDetailedConnectionStatusPair2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_IpadMiscShdslDetailedConnectionStatusPair2_Type.__name__ = "DisplayString"
_IpadMiscShdslDetailedConnectionStatusPair2_Object = MibTableColumn
ipadMiscShdslDetailedConnectionStatusPair2 = _IpadMiscShdslDetailedConnectionStatusPair2_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 12, 5, 1, 7),
    _IpadMiscShdslDetailedConnectionStatusPair2_Type()
)
ipadMiscShdslDetailedConnectionStatusPair2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadMiscShdslDetailedConnectionStatusPair2.setStatus("current")


class _IpadMiscEnableSupervisoryPort_Type(Integer32):
    """Custom type ipadMiscEnableSupervisoryPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 3),
          ("other", 1))
    )


_IpadMiscEnableSupervisoryPort_Type.__name__ = "Integer32"
_IpadMiscEnableSupervisoryPort_Object = MibScalar
ipadMiscEnableSupervisoryPort = _IpadMiscEnableSupervisoryPort_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 12, 6),
    _IpadMiscEnableSupervisoryPort_Type()
)
ipadMiscEnableSupervisoryPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadMiscEnableSupervisoryPort.setStatus("current")


class _IpadMiscEnableButtons_Type(Integer32):
    """Custom type ipadMiscEnableButtons based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 3),
          ("other", 1))
    )


_IpadMiscEnableButtons_Type.__name__ = "Integer32"
_IpadMiscEnableButtons_Object = MibScalar
ipadMiscEnableButtons = _IpadMiscEnableButtons_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 12, 7),
    _IpadMiscEnableButtons_Type()
)
ipadMiscEnableButtons.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadMiscEnableButtons.setStatus("current")


class _IpadMiscBootupConsoleAvail_Type(Integer32):
    """Custom type ipadMiscBootupConsoleAvail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 3),
          ("other", 1))
    )


_IpadMiscBootupConsoleAvail_Type.__name__ = "Integer32"
_IpadMiscBootupConsoleAvail_Object = MibScalar
ipadMiscBootupConsoleAvail = _IpadMiscBootupConsoleAvail_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 12, 8),
    _IpadMiscBootupConsoleAvail_Type()
)
ipadMiscBootupConsoleAvail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadMiscBootupConsoleAvail.setStatus("current")


class _IpadMiscEnableLEDs_Type(Integer32):
    """Custom type ipadMiscEnableLEDs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 3),
          ("other", 1))
    )


_IpadMiscEnableLEDs_Type.__name__ = "Integer32"
_IpadMiscEnableLEDs_Object = MibScalar
ipadMiscEnableLEDs = _IpadMiscEnableLEDs_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 12, 9),
    _IpadMiscEnableLEDs_Type()
)
ipadMiscEnableLEDs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadMiscEnableLEDs.setStatus("current")


class _IpadMiscDisableLAN_Type(Integer32):
    """Custom type ipadMiscDisableLAN based on Integer32"""
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
        *(("disable", 2),
          ("enable", 3),
          ("full10", 5),
          ("full100", 7),
          ("half10", 4),
          ("half100", 6),
          ("other", 1))
    )


_IpadMiscDisableLAN_Type.__name__ = "Integer32"
_IpadMiscDisableLAN_Object = MibScalar
ipadMiscDisableLAN = _IpadMiscDisableLAN_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 12, 10),
    _IpadMiscDisableLAN_Type()
)
ipadMiscDisableLAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadMiscDisableLAN.setStatus("current")


class _IpadMiscLANStatus_Type(Integer32):
    """Custom type ipadMiscLANStatus based on Integer32"""
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
        *(("down", 1),
          ("full10", 3),
          ("full100", 5),
          ("half10", 2),
          ("half100", 4),
          ("na", 6))
    )


_IpadMiscLANStatus_Type.__name__ = "Integer32"
_IpadMiscLANStatus_Object = MibScalar
ipadMiscLANStatus = _IpadMiscLANStatus_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 12, 11),
    _IpadMiscLANStatus_Type()
)
ipadMiscLANStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadMiscLANStatus.setStatus("current")
_IpadRouter_ObjectIdentity = ObjectIdentity
ipadRouter = _IpadRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 13)
)
_IpadSoftKey_ObjectIdentity = ObjectIdentity
ipadSoftKey = _IpadSoftKey_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 14)
)
_IpadSoftKeyTable_Object = MibTable
ipadSoftKeyTable = _IpadSoftKeyTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 14, 1)
)
if mibBuilder.loadTexts:
    ipadSoftKeyTable.setStatus("current")
_IpadSoftKeyTableEntry_Object = MibTableRow
ipadSoftKeyTableEntry = _IpadSoftKeyTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 14, 1, 1)
)
ipadSoftKeyTableEntry.setIndexNames(
    (0, "IPADv2-MIB", "ipadSoftKeyIndex"),
)
if mibBuilder.loadTexts:
    ipadSoftKeyTableEntry.setStatus("current")
_IpadSoftKeyIndex_Type = Integer32
_IpadSoftKeyIndex_Object = MibTableColumn
ipadSoftKeyIndex = _IpadSoftKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 14, 1, 1, 1),
    _IpadSoftKeyIndex_Type()
)
ipadSoftKeyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadSoftKeyIndex.setStatus("current")


class _IpadSoftKeyAcronym_Type(DisplayString):
    """Custom type ipadSoftKeyAcronym based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_IpadSoftKeyAcronym_Type.__name__ = "DisplayString"
_IpadSoftKeyAcronym_Object = MibTableColumn
ipadSoftKeyAcronym = _IpadSoftKeyAcronym_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 14, 1, 1, 2),
    _IpadSoftKeyAcronym_Type()
)
ipadSoftKeyAcronym.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadSoftKeyAcronym.setStatus("current")


class _IpadSoftKeyDescription_Type(DisplayString):
    """Custom type ipadSoftKeyDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_IpadSoftKeyDescription_Type.__name__ = "DisplayString"
_IpadSoftKeyDescription_Object = MibTableColumn
ipadSoftKeyDescription = _IpadSoftKeyDescription_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 14, 1, 1, 3),
    _IpadSoftKeyDescription_Type()
)
ipadSoftKeyDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadSoftKeyDescription.setStatus("current")


class _IpadSoftKeyExpirationDate_Type(DisplayString):
    """Custom type ipadSoftKeyExpirationDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_IpadSoftKeyExpirationDate_Type.__name__ = "DisplayString"
_IpadSoftKeyExpirationDate_Object = MibTableColumn
ipadSoftKeyExpirationDate = _IpadSoftKeyExpirationDate_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 14, 1, 1, 4),
    _IpadSoftKeyExpirationDate_Type()
)
ipadSoftKeyExpirationDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadSoftKeyExpirationDate.setStatus("current")


class _IpadSoftKeyEntry_Type(DisplayString):
    """Custom type ipadSoftKeyEntry based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_IpadSoftKeyEntry_Type.__name__ = "DisplayString"
_IpadSoftKeyEntry_Object = MibScalar
ipadSoftKeyEntry = _IpadSoftKeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 14, 2),
    _IpadSoftKeyEntry_Type()
)
ipadSoftKeyEntry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadSoftKeyEntry.setStatus("current")
_IpadTCPServer_ObjectIdentity = ObjectIdentity
ipadTCPServer = _IpadTCPServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 15)
)


class _IpadTCPServerEnable_Type(Integer32):
    """Custom type ipadTCPServerEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 3),
          ("other", 1))
    )


_IpadTCPServerEnable_Type.__name__ = "Integer32"
_IpadTCPServerEnable_Object = MibScalar
ipadTCPServerEnable = _IpadTCPServerEnable_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 15, 1),
    _IpadTCPServerEnable_Type()
)
ipadTCPServerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadTCPServerEnable.setStatus("current")
_IpadTCPServerConnTable_Object = MibTable
ipadTCPServerConnTable = _IpadTCPServerConnTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 15, 2)
)
if mibBuilder.loadTexts:
    ipadTCPServerConnTable.setStatus("current")
_IpadTCPServerConnTableEntry_Object = MibTableRow
ipadTCPServerConnTableEntry = _IpadTCPServerConnTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 15, 2, 1)
)
ipadTCPServerConnTableEntry.setIndexNames(
    (0, "IPADv2-MIB", "ipadTCPServerConnIndex"),
)
if mibBuilder.loadTexts:
    ipadTCPServerConnTableEntry.setStatus("current")
_IpadTCPServerConnIndex_Type = Integer32
_IpadTCPServerConnIndex_Object = MibTableColumn
ipadTCPServerConnIndex = _IpadTCPServerConnIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 15, 2, 1, 1),
    _IpadTCPServerConnIndex_Type()
)
ipadTCPServerConnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadTCPServerConnIndex.setStatus("current")


class _IpadTCPServerConnEndpoint_Type(DisplayString):
    """Custom type ipadTCPServerConnEndpoint based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_IpadTCPServerConnEndpoint_Type.__name__ = "DisplayString"
_IpadTCPServerConnEndpoint_Object = MibTableColumn
ipadTCPServerConnEndpoint = _IpadTCPServerConnEndpoint_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 15, 2, 1, 2),
    _IpadTCPServerConnEndpoint_Type()
)
ipadTCPServerConnEndpoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadTCPServerConnEndpoint.setStatus("current")


class _IpadTCPServerConnLocalPort_Type(Integer32):
    """Custom type ipadTCPServerConnLocalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IpadTCPServerConnLocalPort_Type.__name__ = "Integer32"
_IpadTCPServerConnLocalPort_Object = MibTableColumn
ipadTCPServerConnLocalPort = _IpadTCPServerConnLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 15, 2, 1, 3),
    _IpadTCPServerConnLocalPort_Type()
)
ipadTCPServerConnLocalPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadTCPServerConnLocalPort.setStatus("current")


class _IpadTCPServerConnEnableEntry_Type(Integer32):
    """Custom type ipadTCPServerConnEnableEntry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 3),
          ("other", 1))
    )


_IpadTCPServerConnEnableEntry_Type.__name__ = "Integer32"
_IpadTCPServerConnEnableEntry_Object = MibTableColumn
ipadTCPServerConnEnableEntry = _IpadTCPServerConnEnableEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 15, 2, 1, 4),
    _IpadTCPServerConnEnableEntry_Type()
)
ipadTCPServerConnEnableEntry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadTCPServerConnEnableEntry.setStatus("current")


class _IpadTCPServerAddConnEntry_Type(Integer32):
    """Custom type ipadTCPServerAddConnEntry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("addnew", 2),
          ("other", 1))
    )


_IpadTCPServerAddConnEntry_Type.__name__ = "Integer32"
_IpadTCPServerAddConnEntry_Object = MibScalar
ipadTCPServerAddConnEntry = _IpadTCPServerAddConnEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 15, 3),
    _IpadTCPServerAddConnEntry_Type()
)
ipadTCPServerAddConnEntry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadTCPServerAddConnEntry.setStatus("current")
_IpadTCPServerDeleteConnEntry_Type = Integer32
_IpadTCPServerDeleteConnEntry_Object = MibScalar
ipadTCPServerDeleteConnEntry = _IpadTCPServerDeleteConnEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 15, 4),
    _IpadTCPServerDeleteConnEntry_Type()
)
ipadTCPServerDeleteConnEntry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadTCPServerDeleteConnEntry.setStatus("current")
_IpadTCPServerHostAccessTable_Object = MibTable
ipadTCPServerHostAccessTable = _IpadTCPServerHostAccessTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 15, 5)
)
if mibBuilder.loadTexts:
    ipadTCPServerHostAccessTable.setStatus("current")
_IpadTCPServerHostAccessTableEntry_Object = MibTableRow
ipadTCPServerHostAccessTableEntry = _IpadTCPServerHostAccessTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 15, 5, 1)
)
ipadTCPServerHostAccessTableEntry.setIndexNames(
    (0, "IPADv2-MIB", "ipadTCPServerHostAccessIndex"),
)
if mibBuilder.loadTexts:
    ipadTCPServerHostAccessTableEntry.setStatus("current")
_IpadTCPServerHostAccessIndex_Type = Integer32
_IpadTCPServerHostAccessIndex_Object = MibTableColumn
ipadTCPServerHostAccessIndex = _IpadTCPServerHostAccessIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 15, 5, 1, 1),
    _IpadTCPServerHostAccessIndex_Type()
)
ipadTCPServerHostAccessIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadTCPServerHostAccessIndex.setStatus("current")
_IpadTCPServerHostAccessIPAddr_Type = IpAddress
_IpadTCPServerHostAccessIPAddr_Object = MibTableColumn
ipadTCPServerHostAccessIPAddr = _IpadTCPServerHostAccessIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 15, 5, 1, 2),
    _IpadTCPServerHostAccessIPAddr_Type()
)
ipadTCPServerHostAccessIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadTCPServerHostAccessIPAddr.setStatus("current")
_IpadSCADAConfig_ObjectIdentity = ObjectIdentity
ipadSCADAConfig = _IpadSCADAConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 16)
)
_IpadSCADAConfigTable_Object = MibTable
ipadSCADAConfigTable = _IpadSCADAConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 16, 1)
)
if mibBuilder.loadTexts:
    ipadSCADAConfigTable.setStatus("current")
_IpadSCADAConfigTableEntry_Object = MibTableRow
ipadSCADAConfigTableEntry = _IpadSCADAConfigTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 16, 1, 1)
)
ipadSCADAConfigTableEntry.setIndexNames(
    (0, "IPADv2-MIB", "ipadSCADACfgIndex"),
)
if mibBuilder.loadTexts:
    ipadSCADAConfigTableEntry.setStatus("current")
_IpadSCADACfgIndex_Type = Integer32
_IpadSCADACfgIndex_Object = MibTableColumn
ipadSCADACfgIndex = _IpadSCADACfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 16, 1, 1, 1),
    _IpadSCADACfgIndex_Type()
)
ipadSCADACfgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadSCADACfgIndex.setStatus("current")
_IpadSCADACfgMessageSize_Type = Integer32
_IpadSCADACfgMessageSize_Object = MibTableColumn
ipadSCADACfgMessageSize = _IpadSCADACfgMessageSize_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 16, 1, 1, 2),
    _IpadSCADACfgMessageSize_Type()
)
ipadSCADACfgMessageSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadSCADACfgMessageSize.setStatus("current")
_IpadSCADACfgIdleCharDelay_Type = Integer32
_IpadSCADACfgIdleCharDelay_Object = MibTableColumn
ipadSCADACfgIdleCharDelay = _IpadSCADACfgIdleCharDelay_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 16, 1, 1, 3),
    _IpadSCADACfgIdleCharDelay_Type()
)
ipadSCADACfgIdleCharDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadSCADACfgIdleCharDelay.setStatus("current")
_IpadSCADACfgInputTerminator_Type = Integer32
_IpadSCADACfgInputTerminator_Object = MibTableColumn
ipadSCADACfgInputTerminator = _IpadSCADACfgInputTerminator_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 16, 1, 1, 4),
    _IpadSCADACfgInputTerminator_Type()
)
ipadSCADACfgInputTerminator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadSCADACfgInputTerminator.setStatus("current")


class _IpadSCADACfgAddDevLst_Type(Integer32):
    """Custom type ipadSCADACfgAddDevLst based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("addnew", 2),
          ("other", 1))
    )


_IpadSCADACfgAddDevLst_Type.__name__ = "Integer32"
_IpadSCADACfgAddDevLst_Object = MibTableColumn
ipadSCADACfgAddDevLst = _IpadSCADACfgAddDevLst_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 16, 1, 1, 5),
    _IpadSCADACfgAddDevLst_Type()
)
ipadSCADACfgAddDevLst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadSCADACfgAddDevLst.setStatus("current")
_IpadSCADACfgDeleteDevLst_Type = Integer32
_IpadSCADACfgDeleteDevLst_Object = MibTableColumn
ipadSCADACfgDeleteDevLst = _IpadSCADACfgDeleteDevLst_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 16, 1, 1, 6),
    _IpadSCADACfgDeleteDevLst_Type()
)
ipadSCADACfgDeleteDevLst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadSCADACfgDeleteDevLst.setStatus("current")


class _IpadSCADACfgDataDirection_Type(Integer32):
    """Custom type ipadSCADACfgDataDirection based on Integer32"""
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
        *(("both", 2),
          ("input", 4),
          ("other", 1),
          ("output", 3))
    )


_IpadSCADACfgDataDirection_Type.__name__ = "Integer32"
_IpadSCADACfgDataDirection_Object = MibTableColumn
ipadSCADACfgDataDirection = _IpadSCADACfgDataDirection_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 16, 1, 1, 7),
    _IpadSCADACfgDataDirection_Type()
)
ipadSCADACfgDataDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadSCADACfgDataDirection.setStatus("current")


class _IpadSCADACfgProtocol_Type(Integer32):
    """Custom type ipadSCADACfgProtocol based on Integer32"""
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
        *(("async", 2),
          ("other", 1),
          ("syncVancommHost", 3),
          ("syncVancommRTU", 4))
    )


_IpadSCADACfgProtocol_Type.__name__ = "Integer32"
_IpadSCADACfgProtocol_Object = MibTableColumn
ipadSCADACfgProtocol = _IpadSCADACfgProtocol_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 16, 1, 1, 8),
    _IpadSCADACfgProtocol_Type()
)
ipadSCADACfgProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadSCADACfgProtocol.setStatus("current")


class _IpadSCADACfgLoopback_Type(Integer32):
    """Custom type ipadSCADACfgLoopback based on Integer32"""
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
        *(("both", 4),
          ("network", 2),
          ("none", 1),
          ("port", 3))
    )


_IpadSCADACfgLoopback_Type.__name__ = "Integer32"
_IpadSCADACfgLoopback_Object = MibTableColumn
ipadSCADACfgLoopback = _IpadSCADACfgLoopback_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 16, 1, 1, 9),
    _IpadSCADACfgLoopback_Type()
)
ipadSCADACfgLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadSCADACfgLoopback.setStatus("current")
_IpadSCADAStats_ObjectIdentity = ObjectIdentity
ipadSCADAStats = _IpadSCADAStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 17)
)
_IpadSCADAStatsTable_Object = MibTable
ipadSCADAStatsTable = _IpadSCADAStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 17, 1)
)
if mibBuilder.loadTexts:
    ipadSCADAStatsTable.setStatus("current")
_IpadSCADAStatsTableEntry_Object = MibTableRow
ipadSCADAStatsTableEntry = _IpadSCADAStatsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 17, 1, 1)
)
ipadSCADAStatsTableEntry.setIndexNames(
    (0, "IPADv2-MIB", "ipadSCADAStatsIndex"),
)
if mibBuilder.loadTexts:
    ipadSCADAStatsTableEntry.setStatus("current")
_IpadSCADAStatsIndex_Type = Integer32
_IpadSCADAStatsIndex_Object = MibTableColumn
ipadSCADAStatsIndex = _IpadSCADAStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 17, 1, 1, 1),
    _IpadSCADAStatsIndex_Type()
)
ipadSCADAStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadSCADAStatsIndex.setStatus("current")
_IpadSCADAStatsTxChars_Type = Integer32
_IpadSCADAStatsTxChars_Object = MibTableColumn
ipadSCADAStatsTxChars = _IpadSCADAStatsTxChars_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 17, 1, 1, 2),
    _IpadSCADAStatsTxChars_Type()
)
ipadSCADAStatsTxChars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadSCADAStatsTxChars.setStatus("current")
_IpadSCADAStatsRxChars_Type = Integer32
_IpadSCADAStatsRxChars_Object = MibTableColumn
ipadSCADAStatsRxChars = _IpadSCADAStatsRxChars_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 17, 1, 1, 3),
    _IpadSCADAStatsRxChars_Type()
)
ipadSCADAStatsRxChars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadSCADAStatsRxChars.setStatus("current")
_IpadSCADAStatsTxMsgs_Type = Integer32
_IpadSCADAStatsTxMsgs_Object = MibTableColumn
ipadSCADAStatsTxMsgs = _IpadSCADAStatsTxMsgs_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 17, 1, 1, 4),
    _IpadSCADAStatsTxMsgs_Type()
)
ipadSCADAStatsTxMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadSCADAStatsTxMsgs.setStatus("current")
_IpadSCADAStatsRxMsgs_Type = Integer32
_IpadSCADAStatsRxMsgs_Object = MibTableColumn
ipadSCADAStatsRxMsgs = _IpadSCADAStatsRxMsgs_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 17, 1, 1, 5),
    _IpadSCADAStatsRxMsgs_Type()
)
ipadSCADAStatsRxMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadSCADAStatsRxMsgs.setStatus("current")
_IpadSCADAStatsRxParityErrors_Type = Integer32
_IpadSCADAStatsRxParityErrors_Object = MibTableColumn
ipadSCADAStatsRxParityErrors = _IpadSCADAStatsRxParityErrors_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 17, 1, 1, 6),
    _IpadSCADAStatsRxParityErrors_Type()
)
ipadSCADAStatsRxParityErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadSCADAStatsRxParityErrors.setStatus("current")
_IpadSCADAStatsRxFramingErrors_Type = Integer32
_IpadSCADAStatsRxFramingErrors_Object = MibTableColumn
ipadSCADAStatsRxFramingErrors = _IpadSCADAStatsRxFramingErrors_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 17, 1, 1, 7),
    _IpadSCADAStatsRxFramingErrors_Type()
)
ipadSCADAStatsRxFramingErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadSCADAStatsRxFramingErrors.setStatus("current")


class _IpadSCADAStatsClear_Type(Integer32):
    """Custom type ipadSCADAStatsClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipadSCADAStatsClearNow", 2),
          ("ipadSCADAStatsClearOther", 1))
    )


_IpadSCADAStatsClear_Type.__name__ = "Integer32"
_IpadSCADAStatsClear_Object = MibTableColumn
ipadSCADAStatsClear = _IpadSCADAStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 17, 1, 1, 8),
    _IpadSCADAStatsClear_Type()
)
ipadSCADAStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadSCADAStatsClear.setStatus("current")
_IpadSCADADevLst_ObjectIdentity = ObjectIdentity
ipadSCADADevLst = _IpadSCADADevLst_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 18)
)
_IpadSCADADevLstTable_Object = MibTable
ipadSCADADevLstTable = _IpadSCADADevLstTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 18, 1)
)
if mibBuilder.loadTexts:
    ipadSCADADevLstTable.setStatus("current")
_IpadSCADADevLstTableEntry_Object = MibTableRow
ipadSCADADevLstTableEntry = _IpadSCADADevLstTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 18, 1, 1)
)
ipadSCADADevLstTableEntry.setIndexNames(
    (0, "IPADv2-MIB", "ipadSCADADevLstIndex"),
    (0, "IPADv2-MIB", "ipadSCADADevLstDevIndex"),
)
if mibBuilder.loadTexts:
    ipadSCADADevLstTableEntry.setStatus("current")
_IpadSCADADevLstIndex_Type = Integer32
_IpadSCADADevLstIndex_Object = MibTableColumn
ipadSCADADevLstIndex = _IpadSCADADevLstIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 18, 1, 1, 1),
    _IpadSCADADevLstIndex_Type()
)
ipadSCADADevLstIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadSCADADevLstIndex.setStatus("current")
_IpadSCADADevLstDevIndex_Type = Integer32
_IpadSCADADevLstDevIndex_Object = MibTableColumn
ipadSCADADevLstDevIndex = _IpadSCADADevLstDevIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 18, 1, 1, 2),
    _IpadSCADADevLstDevIndex_Type()
)
ipadSCADADevLstDevIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadSCADADevLstDevIndex.setStatus("current")


class _IpadSCADADevLstEndpointName_Type(DisplayString):
    """Custom type ipadSCADADevLstEndpointName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_IpadSCADADevLstEndpointName_Type.__name__ = "DisplayString"
_IpadSCADADevLstEndpointName_Object = MibTableColumn
ipadSCADADevLstEndpointName = _IpadSCADADevLstEndpointName_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 18, 1, 1, 3),
    _IpadSCADADevLstEndpointName_Type()
)
ipadSCADADevLstEndpointName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadSCADADevLstEndpointName.setStatus("current")


class _IpadSCADADevLstEntryStatus_Type(Integer32):
    """Custom type ipadSCADADevLstEntryStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 3),
          ("other", 1))
    )


_IpadSCADADevLstEntryStatus_Type.__name__ = "Integer32"
_IpadSCADADevLstEntryStatus_Object = MibTableColumn
ipadSCADADevLstEntryStatus = _IpadSCADADevLstEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 18, 1, 1, 4),
    _IpadSCADADevLstEntryStatus_Type()
)
ipadSCADADevLstEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadSCADADevLstEntryStatus.setStatus("current")
_IpadDS0Config_ObjectIdentity = ObjectIdentity
ipadDS0Config = _IpadDS0Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 19)
)
_IpadDS0ConfigTable_Object = MibTable
ipadDS0ConfigTable = _IpadDS0ConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 19, 1)
)
if mibBuilder.loadTexts:
    ipadDS0ConfigTable.setStatus("current")
_IpadDS0ConfigTableEntry_Object = MibTableRow
ipadDS0ConfigTableEntry = _IpadDS0ConfigTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 19, 1, 1)
)
ipadDS0ConfigTableEntry.setIndexNames(
    (0, "IPADv2-MIB", "ipadDS0ConfigIndex"),
)
if mibBuilder.loadTexts:
    ipadDS0ConfigTableEntry.setStatus("current")
_IpadDS0ConfigIndex_Type = Integer32
_IpadDS0ConfigIndex_Object = MibTableColumn
ipadDS0ConfigIndex = _IpadDS0ConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 19, 1, 1, 1),
    _IpadDS0ConfigIndex_Type()
)
ipadDS0ConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDS0ConfigIndex.setStatus("current")
_IpadDS0ConfigNumberDS0_Type = Integer32
_IpadDS0ConfigNumberDS0_Object = MibTableColumn
ipadDS0ConfigNumberDS0 = _IpadDS0ConfigNumberDS0_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 19, 1, 1, 2),
    _IpadDS0ConfigNumberDS0_Type()
)
ipadDS0ConfigNumberDS0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDS0ConfigNumberDS0.setStatus("current")
_IpadDS0ConfigResetTimer_Type = Integer32
_IpadDS0ConfigResetTimer_Object = MibTableColumn
ipadDS0ConfigResetTimer = _IpadDS0ConfigResetTimer_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 19, 1, 1, 3),
    _IpadDS0ConfigResetTimer_Type()
)
ipadDS0ConfigResetTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadDS0ConfigResetTimer.setStatus("current")
_IpadDS0ConfigHighUtil_Type = Integer32
_IpadDS0ConfigHighUtil_Object = MibTableColumn
ipadDS0ConfigHighUtil = _IpadDS0ConfigHighUtil_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 19, 1, 1, 4),
    _IpadDS0ConfigHighUtil_Type()
)
ipadDS0ConfigHighUtil.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadDS0ConfigHighUtil.setStatus("current")
_IpadDS0ConfigHighUtilThreshold_Type = Integer32
_IpadDS0ConfigHighUtilThreshold_Object = MibTableColumn
ipadDS0ConfigHighUtilThreshold = _IpadDS0ConfigHighUtilThreshold_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 19, 1, 1, 5),
    _IpadDS0ConfigHighUtilThreshold_Type()
)
ipadDS0ConfigHighUtilThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadDS0ConfigHighUtilThreshold.setStatus("current")


class _IpadDS0ConfigHighUtilStatus_Type(Integer32):
    """Custom type ipadDS0ConfigHighUtilStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("exists", 3),
          ("notExist", 2),
          ("other", 1))
    )


_IpadDS0ConfigHighUtilStatus_Type.__name__ = "Integer32"
_IpadDS0ConfigHighUtilStatus_Object = MibTableColumn
ipadDS0ConfigHighUtilStatus = _IpadDS0ConfigHighUtilStatus_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 19, 1, 1, 6),
    _IpadDS0ConfigHighUtilStatus_Type()
)
ipadDS0ConfigHighUtilStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDS0ConfigHighUtilStatus.setStatus("current")
_IpadDS0ConfigHighUtilCount_Type = Integer32
_IpadDS0ConfigHighUtilCount_Object = MibTableColumn
ipadDS0ConfigHighUtilCount = _IpadDS0ConfigHighUtilCount_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 19, 1, 1, 7),
    _IpadDS0ConfigHighUtilCount_Type()
)
ipadDS0ConfigHighUtilCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDS0ConfigHighUtilCount.setStatus("current")


class _IpadDS0ConfigHighUtilAlarm_Type(Integer32):
    """Custom type ipadDS0ConfigHighUtilAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noAlarm", 2),
          ("other", 1),
          ("thresholdExceeded", 3))
    )


_IpadDS0ConfigHighUtilAlarm_Type.__name__ = "Integer32"
_IpadDS0ConfigHighUtilAlarm_Object = MibTableColumn
ipadDS0ConfigHighUtilAlarm = _IpadDS0ConfigHighUtilAlarm_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 19, 1, 1, 8),
    _IpadDS0ConfigHighUtilAlarm_Type()
)
ipadDS0ConfigHighUtilAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDS0ConfigHighUtilAlarm.setStatus("current")
_IpadDS0ConfigLowUtil_Type = Integer32
_IpadDS0ConfigLowUtil_Object = MibTableColumn
ipadDS0ConfigLowUtil = _IpadDS0ConfigLowUtil_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 19, 1, 1, 9),
    _IpadDS0ConfigLowUtil_Type()
)
ipadDS0ConfigLowUtil.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadDS0ConfigLowUtil.setStatus("current")


class _IpadDS0ConfigLowUtilAlarm_Type(Integer32):
    """Custom type ipadDS0ConfigLowUtilAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noAlarm", 2),
          ("other", 1),
          ("thresholdExceeded", 3))
    )


_IpadDS0ConfigLowUtilAlarm_Type.__name__ = "Integer32"
_IpadDS0ConfigLowUtilAlarm_Object = MibTableColumn
ipadDS0ConfigLowUtilAlarm = _IpadDS0ConfigLowUtilAlarm_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 19, 1, 1, 10),
    _IpadDS0ConfigLowUtilAlarm_Type()
)
ipadDS0ConfigLowUtilAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDS0ConfigLowUtilAlarm.setStatus("current")


class _IpadDS0ConfigReset_Type(Integer32):
    """Custom type ipadDS0ConfigReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clearAlarms", 2),
          ("clearHistory", 3),
          ("none", 1))
    )


_IpadDS0ConfigReset_Type.__name__ = "Integer32"
_IpadDS0ConfigReset_Object = MibTableColumn
ipadDS0ConfigReset = _IpadDS0ConfigReset_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 19, 1, 1, 11),
    _IpadDS0ConfigReset_Type()
)
ipadDS0ConfigReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadDS0ConfigReset.setStatus("current")
_IpadDS0Hist24_ObjectIdentity = ObjectIdentity
ipadDS0Hist24 = _IpadDS0Hist24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 20)
)
_IpadDS0Hist24Table_Object = MibTable
ipadDS0Hist24Table = _IpadDS0Hist24Table_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 20, 1)
)
if mibBuilder.loadTexts:
    ipadDS0Hist24Table.setStatus("current")
_IpadDS0Hist24TableEntry_Object = MibTableRow
ipadDS0Hist24TableEntry = _IpadDS0Hist24TableEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 20, 1, 1)
)
ipadDS0Hist24TableEntry.setIndexNames(
    (0, "IPADv2-MIB", "ipadDS0Hist24Index"),
    (0, "IPADv2-MIB", "ipadDS0Hist24HistoricalIndex"),
)
if mibBuilder.loadTexts:
    ipadDS0Hist24TableEntry.setStatus("current")
_IpadDS0Hist24Index_Type = Integer32
_IpadDS0Hist24Index_Object = MibTableColumn
ipadDS0Hist24Index = _IpadDS0Hist24Index_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 20, 1, 1, 1),
    _IpadDS0Hist24Index_Type()
)
ipadDS0Hist24Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDS0Hist24Index.setStatus("current")


class _IpadDS0Hist24HistoricalIndex_Type(Integer32):
    """Custom type ipadDS0Hist24HistoricalIndex based on Integer32"""
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
              74,
              75,
              76,
              77,
              78,
              79,
              80,
              81,
              82,
              83,
              84,
              85,
              86,
              87,
              88,
              89,
              90,
              91,
              92,
              93,
              94,
              95,
              96,
              97,
              98)
        )
    )
    namedValues = NamedValues(
        *(("statCurrent", 2),
          ("statPeriod1", 3),
          ("statPeriod10", 12),
          ("statPeriod11", 13),
          ("statPeriod12", 14),
          ("statPeriod13", 15),
          ("statPeriod14", 16),
          ("statPeriod15", 17),
          ("statPeriod16", 18),
          ("statPeriod17", 19),
          ("statPeriod18", 20),
          ("statPeriod19", 21),
          ("statPeriod2", 4),
          ("statPeriod20", 22),
          ("statPeriod21", 23),
          ("statPeriod22", 24),
          ("statPeriod23", 25),
          ("statPeriod24", 26),
          ("statPeriod25", 27),
          ("statPeriod26", 28),
          ("statPeriod27", 29),
          ("statPeriod28", 30),
          ("statPeriod29", 31),
          ("statPeriod3", 5),
          ("statPeriod30", 32),
          ("statPeriod31", 33),
          ("statPeriod32", 34),
          ("statPeriod33", 35),
          ("statPeriod34", 36),
          ("statPeriod35", 37),
          ("statPeriod36", 38),
          ("statPeriod37", 39),
          ("statPeriod38", 40),
          ("statPeriod39", 41),
          ("statPeriod4", 6),
          ("statPeriod40", 42),
          ("statPeriod41", 43),
          ("statPeriod42", 44),
          ("statPeriod43", 45),
          ("statPeriod44", 46),
          ("statPeriod45", 47),
          ("statPeriod46", 48),
          ("statPeriod47", 49),
          ("statPeriod48", 50),
          ("statPeriod49", 51),
          ("statPeriod5", 7),
          ("statPeriod50", 52),
          ("statPeriod51", 53),
          ("statPeriod52", 54),
          ("statPeriod53", 55),
          ("statPeriod54", 56),
          ("statPeriod55", 57),
          ("statPeriod56", 58),
          ("statPeriod57", 59),
          ("statPeriod58", 60),
          ("statPeriod59", 61),
          ("statPeriod6", 8),
          ("statPeriod60", 62),
          ("statPeriod61", 63),
          ("statPeriod62", 64),
          ("statPeriod63", 65),
          ("statPeriod64", 66),
          ("statPeriod65", 67),
          ("statPeriod66", 68),
          ("statPeriod67", 69),
          ("statPeriod68", 70),
          ("statPeriod69", 71),
          ("statPeriod7", 9),
          ("statPeriod70", 72),
          ("statPeriod71", 73),
          ("statPeriod72", 74),
          ("statPeriod73", 75),
          ("statPeriod74", 76),
          ("statPeriod75", 77),
          ("statPeriod76", 78),
          ("statPeriod77", 79),
          ("statPeriod78", 80),
          ("statPeriod79", 81),
          ("statPeriod8", 10),
          ("statPeriod80", 82),
          ("statPeriod81", 83),
          ("statPeriod82", 84),
          ("statPeriod83", 85),
          ("statPeriod84", 86),
          ("statPeriod85", 87),
          ("statPeriod86", 88),
          ("statPeriod87", 89),
          ("statPeriod88", 90),
          ("statPeriod89", 91),
          ("statPeriod9", 11),
          ("statPeriod90", 92),
          ("statPeriod91", 93),
          ("statPeriod92", 94),
          ("statPeriod93", 95),
          ("statPeriod94", 96),
          ("statPeriod95", 97),
          ("statPeriod96", 98),
          ("statSummary", 1))
    )


_IpadDS0Hist24HistoricalIndex_Type.__name__ = "Integer32"
_IpadDS0Hist24HistoricalIndex_Object = MibTableColumn
ipadDS0Hist24HistoricalIndex = _IpadDS0Hist24HistoricalIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 20, 1, 1, 2),
    _IpadDS0Hist24HistoricalIndex_Type()
)
ipadDS0Hist24HistoricalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDS0Hist24HistoricalIndex.setStatus("current")
_IpadDS0Hist24Timestamp_Type = TimeTicks
_IpadDS0Hist24Timestamp_Object = MibTableColumn
ipadDS0Hist24Timestamp = _IpadDS0Hist24Timestamp_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 20, 1, 1, 3),
    _IpadDS0Hist24Timestamp_Type()
)
ipadDS0Hist24Timestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDS0Hist24Timestamp.setStatus("current")
_IpadDS0Hist24HighUtilSeconds_Type = Integer32
_IpadDS0Hist24HighUtilSeconds_Object = MibTableColumn
ipadDS0Hist24HighUtilSeconds = _IpadDS0Hist24HighUtilSeconds_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 20, 1, 1, 4),
    _IpadDS0Hist24HighUtilSeconds_Type()
)
ipadDS0Hist24HighUtilSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDS0Hist24HighUtilSeconds.setStatus("current")
_IpadDS0Hist24Utilization_Type = Integer32
_IpadDS0Hist24Utilization_Object = MibTableColumn
ipadDS0Hist24Utilization = _IpadDS0Hist24Utilization_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 20, 1, 1, 5),
    _IpadDS0Hist24Utilization_Type()
)
ipadDS0Hist24Utilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDS0Hist24Utilization.setStatus("current")
_IpadDS0Hist30_ObjectIdentity = ObjectIdentity
ipadDS0Hist30 = _IpadDS0Hist30_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 21)
)
_IpadDS0Hist30Table_Object = MibTable
ipadDS0Hist30Table = _IpadDS0Hist30Table_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 21, 1)
)
if mibBuilder.loadTexts:
    ipadDS0Hist30Table.setStatus("current")
_IpadDS0Hist30TableEntry_Object = MibTableRow
ipadDS0Hist30TableEntry = _IpadDS0Hist30TableEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 21, 1, 1)
)
ipadDS0Hist30TableEntry.setIndexNames(
    (0, "IPADv2-MIB", "ipadDS0Hist30Index"),
    (0, "IPADv2-MIB", "ipadDS0Hist30HistoricalIndex"),
)
if mibBuilder.loadTexts:
    ipadDS0Hist30TableEntry.setStatus("current")
_IpadDS0Hist30Index_Type = Integer32
_IpadDS0Hist30Index_Object = MibTableColumn
ipadDS0Hist30Index = _IpadDS0Hist30Index_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 21, 1, 1, 1),
    _IpadDS0Hist30Index_Type()
)
ipadDS0Hist30Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDS0Hist30Index.setStatus("current")


class _IpadDS0Hist30HistoricalIndex_Type(Integer32):
    """Custom type ipadDS0Hist30HistoricalIndex based on Integer32"""
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
              31)
        )
    )
    namedValues = NamedValues(
        *(("statDay1", 2),
          ("statDay10", 11),
          ("statDay11", 12),
          ("statDay12", 13),
          ("statDay13", 14),
          ("statDay14", 15),
          ("statDay15", 16),
          ("statDay16", 17),
          ("statDay17", 18),
          ("statDay18", 19),
          ("statDay19", 20),
          ("statDay2", 3),
          ("statDay20", 21),
          ("statDay21", 22),
          ("statDay22", 23),
          ("statDay23", 24),
          ("statDay24", 25),
          ("statDay25", 26),
          ("statDay26", 27),
          ("statDay27", 28),
          ("statDay28", 29),
          ("statDay29", 30),
          ("statDay3", 4),
          ("statDay30", 31),
          ("statDay4", 5),
          ("statDay5", 6),
          ("statDay6", 7),
          ("statDay7", 8),
          ("statDay8", 9),
          ("statDay9", 10),
          ("statSummary", 1))
    )


_IpadDS0Hist30HistoricalIndex_Type.__name__ = "Integer32"
_IpadDS0Hist30HistoricalIndex_Object = MibTableColumn
ipadDS0Hist30HistoricalIndex = _IpadDS0Hist30HistoricalIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 21, 1, 1, 2),
    _IpadDS0Hist30HistoricalIndex_Type()
)
ipadDS0Hist30HistoricalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDS0Hist30HistoricalIndex.setStatus("current")
_IpadDS0Hist30Timestamp_Type = TimeTicks
_IpadDS0Hist30Timestamp_Object = MibTableColumn
ipadDS0Hist30Timestamp = _IpadDS0Hist30Timestamp_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 21, 1, 1, 3),
    _IpadDS0Hist30Timestamp_Type()
)
ipadDS0Hist30Timestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDS0Hist30Timestamp.setStatus("current")
_IpadDS0Hist30HighUtilSeconds_Type = Integer32
_IpadDS0Hist30HighUtilSeconds_Object = MibTableColumn
ipadDS0Hist30HighUtilSeconds = _IpadDS0Hist30HighUtilSeconds_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 21, 1, 1, 4),
    _IpadDS0Hist30HighUtilSeconds_Type()
)
ipadDS0Hist30HighUtilSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDS0Hist30HighUtilSeconds.setStatus("current")
_IpadDS0Hist30Utilization_Type = Integer32
_IpadDS0Hist30Utilization_Object = MibTableColumn
ipadDS0Hist30Utilization = _IpadDS0Hist30Utilization_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 21, 1, 1, 5),
    _IpadDS0Hist30Utilization_Type()
)
ipadDS0Hist30Utilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDS0Hist30Utilization.setStatus("current")
_IpadHDLCConfig_ObjectIdentity = ObjectIdentity
ipadHDLCConfig = _IpadHDLCConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 22)
)
_IpadHDLCConfigTable_Object = MibTable
ipadHDLCConfigTable = _IpadHDLCConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 22, 1)
)
if mibBuilder.loadTexts:
    ipadHDLCConfigTable.setStatus("current")
_IpadHDLCConfigTableEntry_Object = MibTableRow
ipadHDLCConfigTableEntry = _IpadHDLCConfigTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 22, 1, 1)
)
ipadHDLCConfigTableEntry.setIndexNames(
    (0, "IPADv2-MIB", "ipadHDLCConfigIndex"),
)
if mibBuilder.loadTexts:
    ipadHDLCConfigTableEntry.setStatus("current")
_IpadHDLCConfigIndex_Type = Integer32
_IpadHDLCConfigIndex_Object = MibTableColumn
ipadHDLCConfigIndex = _IpadHDLCConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 22, 1, 1, 1),
    _IpadHDLCConfigIndex_Type()
)
ipadHDLCConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadHDLCConfigIndex.setStatus("current")
_IpadHDLCConfigService_Type = Integer32
_IpadHDLCConfigService_Object = MibTableColumn
ipadHDLCConfigService = _IpadHDLCConfigService_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 22, 1, 1, 2),
    _IpadHDLCConfigService_Type()
)
ipadHDLCConfigService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadHDLCConfigService.setStatus("current")
_IpadHDLCConfigServiceBPS_Type = Integer32
_IpadHDLCConfigServiceBPS_Object = MibTableColumn
ipadHDLCConfigServiceBPS = _IpadHDLCConfigServiceBPS_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 22, 1, 1, 3),
    _IpadHDLCConfigServiceBPS_Type()
)
ipadHDLCConfigServiceBPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadHDLCConfigServiceBPS.setStatus("current")
_IpadHDLCConfigResetTimer_Type = Integer32
_IpadHDLCConfigResetTimer_Object = MibTableColumn
ipadHDLCConfigResetTimer = _IpadHDLCConfigResetTimer_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 22, 1, 1, 4),
    _IpadHDLCConfigResetTimer_Type()
)
ipadHDLCConfigResetTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadHDLCConfigResetTimer.setStatus("current")
_IpadHDLCConfigRxHighUtil_Type = Integer32
_IpadHDLCConfigRxHighUtil_Object = MibTableColumn
ipadHDLCConfigRxHighUtil = _IpadHDLCConfigRxHighUtil_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 22, 1, 1, 5),
    _IpadHDLCConfigRxHighUtil_Type()
)
ipadHDLCConfigRxHighUtil.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadHDLCConfigRxHighUtil.setStatus("current")
_IpadHDLCConfigRxHighUtilThreshold_Type = Integer32
_IpadHDLCConfigRxHighUtilThreshold_Object = MibTableColumn
ipadHDLCConfigRxHighUtilThreshold = _IpadHDLCConfigRxHighUtilThreshold_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 22, 1, 1, 6),
    _IpadHDLCConfigRxHighUtilThreshold_Type()
)
ipadHDLCConfigRxHighUtilThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadHDLCConfigRxHighUtilThreshold.setStatus("current")


class _IpadHDLCConfigRxHighUtilStatus_Type(Integer32):
    """Custom type ipadHDLCConfigRxHighUtilStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("exists", 3),
          ("notExist", 2),
          ("other", 1))
    )


_IpadHDLCConfigRxHighUtilStatus_Type.__name__ = "Integer32"
_IpadHDLCConfigRxHighUtilStatus_Object = MibTableColumn
ipadHDLCConfigRxHighUtilStatus = _IpadHDLCConfigRxHighUtilStatus_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 22, 1, 1, 7),
    _IpadHDLCConfigRxHighUtilStatus_Type()
)
ipadHDLCConfigRxHighUtilStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadHDLCConfigRxHighUtilStatus.setStatus("current")
_IpadHDLCConfigRxHighUtilCount_Type = Integer32
_IpadHDLCConfigRxHighUtilCount_Object = MibTableColumn
ipadHDLCConfigRxHighUtilCount = _IpadHDLCConfigRxHighUtilCount_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 22, 1, 1, 8),
    _IpadHDLCConfigRxHighUtilCount_Type()
)
ipadHDLCConfigRxHighUtilCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadHDLCConfigRxHighUtilCount.setStatus("current")


class _IpadHDLCConfigRxHighUtilAlarm_Type(Integer32):
    """Custom type ipadHDLCConfigRxHighUtilAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noAlarm", 2),
          ("other", 1),
          ("thresholdExceeded", 3))
    )


_IpadHDLCConfigRxHighUtilAlarm_Type.__name__ = "Integer32"
_IpadHDLCConfigRxHighUtilAlarm_Object = MibTableColumn
ipadHDLCConfigRxHighUtilAlarm = _IpadHDLCConfigRxHighUtilAlarm_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 22, 1, 1, 9),
    _IpadHDLCConfigRxHighUtilAlarm_Type()
)
ipadHDLCConfigRxHighUtilAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadHDLCConfigRxHighUtilAlarm.setStatus("current")
_IpadHDLCConfigRxLowUtil_Type = Integer32
_IpadHDLCConfigRxLowUtil_Object = MibTableColumn
ipadHDLCConfigRxLowUtil = _IpadHDLCConfigRxLowUtil_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 22, 1, 1, 10),
    _IpadHDLCConfigRxLowUtil_Type()
)
ipadHDLCConfigRxLowUtil.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadHDLCConfigRxLowUtil.setStatus("current")


class _IpadHDLCConfigRxLowUtilAlarm_Type(Integer32):
    """Custom type ipadHDLCConfigRxLowUtilAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noAlarm", 2),
          ("other", 1),
          ("thresholdExceeded", 3))
    )


_IpadHDLCConfigRxLowUtilAlarm_Type.__name__ = "Integer32"
_IpadHDLCConfigRxLowUtilAlarm_Object = MibTableColumn
ipadHDLCConfigRxLowUtilAlarm = _IpadHDLCConfigRxLowUtilAlarm_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 22, 1, 1, 11),
    _IpadHDLCConfigRxLowUtilAlarm_Type()
)
ipadHDLCConfigRxLowUtilAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadHDLCConfigRxLowUtilAlarm.setStatus("current")
_IpadHDLCConfigTxHighUtil_Type = Integer32
_IpadHDLCConfigTxHighUtil_Object = MibTableColumn
ipadHDLCConfigTxHighUtil = _IpadHDLCConfigTxHighUtil_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 22, 1, 1, 12),
    _IpadHDLCConfigTxHighUtil_Type()
)
ipadHDLCConfigTxHighUtil.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadHDLCConfigTxHighUtil.setStatus("current")
_IpadHDLCConfigTxHighUtilThreshold_Type = Integer32
_IpadHDLCConfigTxHighUtilThreshold_Object = MibTableColumn
ipadHDLCConfigTxHighUtilThreshold = _IpadHDLCConfigTxHighUtilThreshold_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 22, 1, 1, 13),
    _IpadHDLCConfigTxHighUtilThreshold_Type()
)
ipadHDLCConfigTxHighUtilThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadHDLCConfigTxHighUtilThreshold.setStatus("current")


class _IpadHDLCConfigTxHighUtilStatus_Type(Integer32):
    """Custom type ipadHDLCConfigTxHighUtilStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("exists", 3),
          ("notExist", 2),
          ("other", 1))
    )


_IpadHDLCConfigTxHighUtilStatus_Type.__name__ = "Integer32"
_IpadHDLCConfigTxHighUtilStatus_Object = MibTableColumn
ipadHDLCConfigTxHighUtilStatus = _IpadHDLCConfigTxHighUtilStatus_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 22, 1, 1, 14),
    _IpadHDLCConfigTxHighUtilStatus_Type()
)
ipadHDLCConfigTxHighUtilStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadHDLCConfigTxHighUtilStatus.setStatus("current")
_IpadHDLCConfigTxHighUtilCount_Type = Integer32
_IpadHDLCConfigTxHighUtilCount_Object = MibTableColumn
ipadHDLCConfigTxHighUtilCount = _IpadHDLCConfigTxHighUtilCount_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 22, 1, 1, 15),
    _IpadHDLCConfigTxHighUtilCount_Type()
)
ipadHDLCConfigTxHighUtilCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadHDLCConfigTxHighUtilCount.setStatus("current")


class _IpadHDLCConfigTxHighUtilAlarm_Type(Integer32):
    """Custom type ipadHDLCConfigTxHighUtilAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noAlarm", 2),
          ("other", 1),
          ("thresholdExceeded", 3))
    )


_IpadHDLCConfigTxHighUtilAlarm_Type.__name__ = "Integer32"
_IpadHDLCConfigTxHighUtilAlarm_Object = MibTableColumn
ipadHDLCConfigTxHighUtilAlarm = _IpadHDLCConfigTxHighUtilAlarm_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 22, 1, 1, 16),
    _IpadHDLCConfigTxHighUtilAlarm_Type()
)
ipadHDLCConfigTxHighUtilAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadHDLCConfigTxHighUtilAlarm.setStatus("current")
_IpadHDLCConfigTxLowUtil_Type = Integer32
_IpadHDLCConfigTxLowUtil_Object = MibTableColumn
ipadHDLCConfigTxLowUtil = _IpadHDLCConfigTxLowUtil_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 22, 1, 1, 17),
    _IpadHDLCConfigTxLowUtil_Type()
)
ipadHDLCConfigTxLowUtil.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadHDLCConfigTxLowUtil.setStatus("current")


class _IpadHDLCConfigTxLowUtilAlarm_Type(Integer32):
    """Custom type ipadHDLCConfigTxLowUtilAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noAlarm", 2),
          ("other", 1),
          ("thresholdExceeded", 3))
    )


_IpadHDLCConfigTxLowUtilAlarm_Type.__name__ = "Integer32"
_IpadHDLCConfigTxLowUtilAlarm_Object = MibTableColumn
ipadHDLCConfigTxLowUtilAlarm = _IpadHDLCConfigTxLowUtilAlarm_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 22, 1, 1, 18),
    _IpadHDLCConfigTxLowUtilAlarm_Type()
)
ipadHDLCConfigTxLowUtilAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadHDLCConfigTxLowUtilAlarm.setStatus("current")


class _IpadHDLCConfigReset_Type(Integer32):
    """Custom type ipadHDLCConfigReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clearAlarms", 2),
          ("clearHistory", 3),
          ("none", 1))
    )


_IpadHDLCConfigReset_Type.__name__ = "Integer32"
_IpadHDLCConfigReset_Object = MibTableColumn
ipadHDLCConfigReset = _IpadHDLCConfigReset_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 22, 1, 1, 19),
    _IpadHDLCConfigReset_Type()
)
ipadHDLCConfigReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadHDLCConfigReset.setStatus("current")
_IpadHDLCHist24_ObjectIdentity = ObjectIdentity
ipadHDLCHist24 = _IpadHDLCHist24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 23)
)
_IpadHDLCHist24Table_Object = MibTable
ipadHDLCHist24Table = _IpadHDLCHist24Table_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 23, 1)
)
if mibBuilder.loadTexts:
    ipadHDLCHist24Table.setStatus("current")
_IpadHDLCHist24TableEntry_Object = MibTableRow
ipadHDLCHist24TableEntry = _IpadHDLCHist24TableEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 23, 1, 1)
)
ipadHDLCHist24TableEntry.setIndexNames(
    (0, "IPADv2-MIB", "ipadHDLCHist24Index"),
    (0, "IPADv2-MIB", "ipadHDLCHist24HistoricalIndex"),
)
if mibBuilder.loadTexts:
    ipadHDLCHist24TableEntry.setStatus("current")
_IpadHDLCHist24Index_Type = Integer32
_IpadHDLCHist24Index_Object = MibTableColumn
ipadHDLCHist24Index = _IpadHDLCHist24Index_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 23, 1, 1, 1),
    _IpadHDLCHist24Index_Type()
)
ipadHDLCHist24Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadHDLCHist24Index.setStatus("current")


class _IpadHDLCHist24HistoricalIndex_Type(Integer32):
    """Custom type ipadHDLCHist24HistoricalIndex based on Integer32"""
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
              74,
              75,
              76,
              77,
              78,
              79,
              80,
              81,
              82,
              83,
              84,
              85,
              86,
              87,
              88,
              89,
              90,
              91,
              92,
              93,
              94,
              95,
              96,
              97,
              98)
        )
    )
    namedValues = NamedValues(
        *(("statCurrent", 2),
          ("statPeriod1", 3),
          ("statPeriod10", 12),
          ("statPeriod11", 13),
          ("statPeriod12", 14),
          ("statPeriod13", 15),
          ("statPeriod14", 16),
          ("statPeriod15", 17),
          ("statPeriod16", 18),
          ("statPeriod17", 19),
          ("statPeriod18", 20),
          ("statPeriod19", 21),
          ("statPeriod2", 4),
          ("statPeriod20", 22),
          ("statPeriod21", 23),
          ("statPeriod22", 24),
          ("statPeriod23", 25),
          ("statPeriod24", 26),
          ("statPeriod25", 27),
          ("statPeriod26", 28),
          ("statPeriod27", 29),
          ("statPeriod28", 30),
          ("statPeriod29", 31),
          ("statPeriod3", 5),
          ("statPeriod30", 32),
          ("statPeriod31", 33),
          ("statPeriod32", 34),
          ("statPeriod33", 35),
          ("statPeriod34", 36),
          ("statPeriod35", 37),
          ("statPeriod36", 38),
          ("statPeriod37", 39),
          ("statPeriod38", 40),
          ("statPeriod39", 41),
          ("statPeriod4", 6),
          ("statPeriod40", 42),
          ("statPeriod41", 43),
          ("statPeriod42", 44),
          ("statPeriod43", 45),
          ("statPeriod44", 46),
          ("statPeriod45", 47),
          ("statPeriod46", 48),
          ("statPeriod47", 49),
          ("statPeriod48", 50),
          ("statPeriod49", 51),
          ("statPeriod5", 7),
          ("statPeriod50", 52),
          ("statPeriod51", 53),
          ("statPeriod52", 54),
          ("statPeriod53", 55),
          ("statPeriod54", 56),
          ("statPeriod55", 57),
          ("statPeriod56", 58),
          ("statPeriod57", 59),
          ("statPeriod58", 60),
          ("statPeriod59", 61),
          ("statPeriod6", 8),
          ("statPeriod60", 62),
          ("statPeriod61", 63),
          ("statPeriod62", 64),
          ("statPeriod63", 65),
          ("statPeriod64", 66),
          ("statPeriod65", 67),
          ("statPeriod66", 68),
          ("statPeriod67", 69),
          ("statPeriod68", 70),
          ("statPeriod69", 71),
          ("statPeriod7", 9),
          ("statPeriod70", 72),
          ("statPeriod71", 73),
          ("statPeriod72", 74),
          ("statPeriod73", 75),
          ("statPeriod74", 76),
          ("statPeriod75", 77),
          ("statPeriod76", 78),
          ("statPeriod77", 79),
          ("statPeriod78", 80),
          ("statPeriod79", 81),
          ("statPeriod8", 10),
          ("statPeriod80", 82),
          ("statPeriod81", 83),
          ("statPeriod82", 84),
          ("statPeriod83", 85),
          ("statPeriod84", 86),
          ("statPeriod85", 87),
          ("statPeriod86", 88),
          ("statPeriod87", 89),
          ("statPeriod88", 90),
          ("statPeriod89", 91),
          ("statPeriod9", 11),
          ("statPeriod90", 92),
          ("statPeriod91", 93),
          ("statPeriod92", 94),
          ("statPeriod93", 95),
          ("statPeriod94", 96),
          ("statPeriod95", 97),
          ("statPeriod96", 98),
          ("statSummary", 1))
    )


_IpadHDLCHist24HistoricalIndex_Type.__name__ = "Integer32"
_IpadHDLCHist24HistoricalIndex_Object = MibTableColumn
ipadHDLCHist24HistoricalIndex = _IpadHDLCHist24HistoricalIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 23, 1, 1, 2),
    _IpadHDLCHist24HistoricalIndex_Type()
)
ipadHDLCHist24HistoricalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadHDLCHist24HistoricalIndex.setStatus("current")
_IpadHDLCHist24Timestamp_Type = TimeTicks
_IpadHDLCHist24Timestamp_Object = MibTableColumn
ipadHDLCHist24Timestamp = _IpadHDLCHist24Timestamp_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 23, 1, 1, 3),
    _IpadHDLCHist24Timestamp_Type()
)
ipadHDLCHist24Timestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadHDLCHist24Timestamp.setStatus("current")
_IpadHDLCHist24RxHighUtilSeconds_Type = Integer32
_IpadHDLCHist24RxHighUtilSeconds_Object = MibTableColumn
ipadHDLCHist24RxHighUtilSeconds = _IpadHDLCHist24RxHighUtilSeconds_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 23, 1, 1, 4),
    _IpadHDLCHist24RxHighUtilSeconds_Type()
)
ipadHDLCHist24RxHighUtilSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadHDLCHist24RxHighUtilSeconds.setStatus("current")
_IpadHDLCHist24RxUtilization_Type = Integer32
_IpadHDLCHist24RxUtilization_Object = MibTableColumn
ipadHDLCHist24RxUtilization = _IpadHDLCHist24RxUtilization_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 23, 1, 1, 5),
    _IpadHDLCHist24RxUtilization_Type()
)
ipadHDLCHist24RxUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadHDLCHist24RxUtilization.setStatus("current")
_IpadHDLCHist24TxHighUtilSeconds_Type = Integer32
_IpadHDLCHist24TxHighUtilSeconds_Object = MibTableColumn
ipadHDLCHist24TxHighUtilSeconds = _IpadHDLCHist24TxHighUtilSeconds_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 23, 1, 1, 6),
    _IpadHDLCHist24TxHighUtilSeconds_Type()
)
ipadHDLCHist24TxHighUtilSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadHDLCHist24TxHighUtilSeconds.setStatus("current")
_IpadHDLCHist24TxUtilization_Type = Integer32
_IpadHDLCHist24TxUtilization_Object = MibTableColumn
ipadHDLCHist24TxUtilization = _IpadHDLCHist24TxUtilization_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 23, 1, 1, 7),
    _IpadHDLCHist24TxUtilization_Type()
)
ipadHDLCHist24TxUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadHDLCHist24TxUtilization.setStatus("current")
_IpadHDLCHist30_ObjectIdentity = ObjectIdentity
ipadHDLCHist30 = _IpadHDLCHist30_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 24)
)
_IpadHDLCHist30Table_Object = MibTable
ipadHDLCHist30Table = _IpadHDLCHist30Table_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 24, 1)
)
if mibBuilder.loadTexts:
    ipadHDLCHist30Table.setStatus("current")
_IpadHDLCHist30TableEntry_Object = MibTableRow
ipadHDLCHist30TableEntry = _IpadHDLCHist30TableEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 24, 1, 1)
)
ipadHDLCHist30TableEntry.setIndexNames(
    (0, "IPADv2-MIB", "ipadHDLCHist30Index"),
    (0, "IPADv2-MIB", "ipadHDLCHist30HistoricalIndex"),
)
if mibBuilder.loadTexts:
    ipadHDLCHist30TableEntry.setStatus("current")
_IpadHDLCHist30Index_Type = Integer32
_IpadHDLCHist30Index_Object = MibTableColumn
ipadHDLCHist30Index = _IpadHDLCHist30Index_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 24, 1, 1, 1),
    _IpadHDLCHist30Index_Type()
)
ipadHDLCHist30Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadHDLCHist30Index.setStatus("current")


class _IpadHDLCHist30HistoricalIndex_Type(Integer32):
    """Custom type ipadHDLCHist30HistoricalIndex based on Integer32"""
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
              31)
        )
    )
    namedValues = NamedValues(
        *(("statDay1", 2),
          ("statDay10", 11),
          ("statDay11", 12),
          ("statDay12", 13),
          ("statDay13", 14),
          ("statDay14", 15),
          ("statDay15", 16),
          ("statDay16", 17),
          ("statDay17", 18),
          ("statDay18", 19),
          ("statDay19", 20),
          ("statDay2", 3),
          ("statDay20", 21),
          ("statDay21", 22),
          ("statDay22", 23),
          ("statDay23", 24),
          ("statDay24", 25),
          ("statDay25", 26),
          ("statDay26", 27),
          ("statDay27", 28),
          ("statDay28", 29),
          ("statDay29", 30),
          ("statDay3", 4),
          ("statDay30", 31),
          ("statDay4", 5),
          ("statDay5", 6),
          ("statDay6", 7),
          ("statDay7", 8),
          ("statDay8", 9),
          ("statDay9", 10),
          ("statSummary", 1))
    )


_IpadHDLCHist30HistoricalIndex_Type.__name__ = "Integer32"
_IpadHDLCHist30HistoricalIndex_Object = MibTableColumn
ipadHDLCHist30HistoricalIndex = _IpadHDLCHist30HistoricalIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 24, 1, 1, 2),
    _IpadHDLCHist30HistoricalIndex_Type()
)
ipadHDLCHist30HistoricalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadHDLCHist30HistoricalIndex.setStatus("current")
_IpadHDLCHist30Timestamp_Type = TimeTicks
_IpadHDLCHist30Timestamp_Object = MibTableColumn
ipadHDLCHist30Timestamp = _IpadHDLCHist30Timestamp_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 24, 1, 1, 3),
    _IpadHDLCHist30Timestamp_Type()
)
ipadHDLCHist30Timestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadHDLCHist30Timestamp.setStatus("current")
_IpadHDLCHist30RxHighUtilSeconds_Type = Integer32
_IpadHDLCHist30RxHighUtilSeconds_Object = MibTableColumn
ipadHDLCHist30RxHighUtilSeconds = _IpadHDLCHist30RxHighUtilSeconds_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 24, 1, 1, 4),
    _IpadHDLCHist30RxHighUtilSeconds_Type()
)
ipadHDLCHist30RxHighUtilSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadHDLCHist30RxHighUtilSeconds.setStatus("current")
_IpadHDLCHist30RxUtilization_Type = Integer32
_IpadHDLCHist30RxUtilization_Object = MibTableColumn
ipadHDLCHist30RxUtilization = _IpadHDLCHist30RxUtilization_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 24, 1, 1, 5),
    _IpadHDLCHist30RxUtilization_Type()
)
ipadHDLCHist30RxUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadHDLCHist30RxUtilization.setStatus("current")
_IpadHDLCHist30TxHighUtilSeconds_Type = Integer32
_IpadHDLCHist30TxHighUtilSeconds_Object = MibTableColumn
ipadHDLCHist30TxHighUtilSeconds = _IpadHDLCHist30TxHighUtilSeconds_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 24, 1, 1, 6),
    _IpadHDLCHist30TxHighUtilSeconds_Type()
)
ipadHDLCHist30TxHighUtilSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadHDLCHist30TxHighUtilSeconds.setStatus("current")
_IpadHDLCHist30TxUtilization_Type = Integer32
_IpadHDLCHist30TxUtilization_Object = MibTableColumn
ipadHDLCHist30TxUtilization = _IpadHDLCHist30TxUtilization_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 24, 1, 1, 7),
    _IpadHDLCHist30TxUtilization_Type()
)
ipadHDLCHist30TxUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadHDLCHist30TxUtilization.setStatus("current")
_IpadAtm_ObjectIdentity = ObjectIdentity
ipadAtm = _IpadAtm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 25)
)
_IpadNat_ObjectIdentity = ObjectIdentity
ipadNat = _IpadNat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 26)
)
_IpadDhcp_ObjectIdentity = ObjectIdentity
ipadDhcp = _IpadDhcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 27)
)
_IpadBridge_ObjectIdentity = ObjectIdentity
ipadBridge = _IpadBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 28)
)
_IpadSmtp_ObjectIdentity = ObjectIdentity
ipadSmtp = _IpadSmtp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 29)
)
_IpadSmtpMailServer_Type = IpAddress
_IpadSmtpMailServer_Object = MibScalar
ipadSmtpMailServer = _IpadSmtpMailServer_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 29, 1),
    _IpadSmtpMailServer_Type()
)
ipadSmtpMailServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadSmtpMailServer.setStatus("current")
_IpadSmtpDomainName_Type = DisplayString
_IpadSmtpDomainName_Object = MibScalar
ipadSmtpDomainName = _IpadSmtpDomainName_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 29, 2),
    _IpadSmtpDomainName_Type()
)
ipadSmtpDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadSmtpDomainName.setStatus("current")
_IpadSmtpMailFrom_Type = DisplayString
_IpadSmtpMailFrom_Object = MibScalar
ipadSmtpMailFrom = _IpadSmtpMailFrom_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 29, 3),
    _IpadSmtpMailFrom_Type()
)
ipadSmtpMailFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadSmtpMailFrom.setStatus("current")
_IpadSmtpRecipient1_Type = DisplayString
_IpadSmtpRecipient1_Object = MibScalar
ipadSmtpRecipient1 = _IpadSmtpRecipient1_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 29, 4),
    _IpadSmtpRecipient1_Type()
)
ipadSmtpRecipient1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadSmtpRecipient1.setStatus("current")
_IpadSmtpRecipient2_Type = DisplayString
_IpadSmtpRecipient2_Object = MibScalar
ipadSmtpRecipient2 = _IpadSmtpRecipient2_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 29, 5),
    _IpadSmtpRecipient2_Type()
)
ipadSmtpRecipient2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadSmtpRecipient2.setStatus("current")
_IpadSmtpRecipient3_Type = DisplayString
_IpadSmtpRecipient3_Object = MibScalar
ipadSmtpRecipient3 = _IpadSmtpRecipient3_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 29, 6),
    _IpadSmtpRecipient3_Type()
)
ipadSmtpRecipient3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadSmtpRecipient3.setStatus("current")
_IpadSmtpRecipient4_Type = DisplayString
_IpadSmtpRecipient4_Object = MibScalar
ipadSmtpRecipient4 = _IpadSmtpRecipient4_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 29, 7),
    _IpadSmtpRecipient4_Type()
)
ipadSmtpRecipient4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadSmtpRecipient4.setStatus("current")
_IpadSmtpRecipient5_Type = DisplayString
_IpadSmtpRecipient5_Object = MibScalar
ipadSmtpRecipient5 = _IpadSmtpRecipient5_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 29, 8),
    _IpadSmtpRecipient5_Type()
)
ipadSmtpRecipient5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadSmtpRecipient5.setStatus("current")
_IpadEncryption_ObjectIdentity = ObjectIdentity
ipadEncryption = _IpadEncryption_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 30)
)


class _IpadEncryptionEnable_Type(Integer32):
    """Custom type ipadEncryptionEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 3),
          ("other", 1))
    )


_IpadEncryptionEnable_Type.__name__ = "Integer32"
_IpadEncryptionEnable_Object = MibScalar
ipadEncryptionEnable = _IpadEncryptionEnable_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 30, 1),
    _IpadEncryptionEnable_Type()
)
ipadEncryptionEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadEncryptionEnable.setStatus("current")


class _IpadEncryptionStartupKey_Type(DisplayString):
    """Custom type ipadEncryptionStartupKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 56),
    )


_IpadEncryptionStartupKey_Type.__name__ = "DisplayString"
_IpadEncryptionStartupKey_Object = MibScalar
ipadEncryptionStartupKey = _IpadEncryptionStartupKey_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 30, 2),
    _IpadEncryptionStartupKey_Type()
)
ipadEncryptionStartupKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadEncryptionStartupKey.setStatus("current")


class _IpadEncryptionStartupKeyConfirm_Type(DisplayString):
    """Custom type ipadEncryptionStartupKeyConfirm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 56),
    )


_IpadEncryptionStartupKeyConfirm_Type.__name__ = "DisplayString"
_IpadEncryptionStartupKeyConfirm_Object = MibScalar
ipadEncryptionStartupKeyConfirm = _IpadEncryptionStartupKeyConfirm_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 30, 3),
    _IpadEncryptionStartupKeyConfirm_Type()
)
ipadEncryptionStartupKeyConfirm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadEncryptionStartupKeyConfirm.setStatus("current")


class _IpadEncryptionType_Type(Integer32):
    """Custom type ipadEncryptionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("blowfish", 1),
          ("des", 2),
          ("triple-des", 3))
    )


_IpadEncryptionType_Type.__name__ = "Integer32"
_IpadEncryptionType_Object = MibScalar
ipadEncryptionType = _IpadEncryptionType_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 30, 4),
    _IpadEncryptionType_Type()
)
ipadEncryptionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadEncryptionType.setStatus("current")


class _IpadEncryptionKey1_Type(DisplayString):
    """Custom type ipadEncryptionKey1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 56),
    )


_IpadEncryptionKey1_Type.__name__ = "DisplayString"
_IpadEncryptionKey1_Object = MibScalar
ipadEncryptionKey1 = _IpadEncryptionKey1_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 30, 5),
    _IpadEncryptionKey1_Type()
)
ipadEncryptionKey1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadEncryptionKey1.setStatus("current")


class _IpadEncryptionKey2_Type(DisplayString):
    """Custom type ipadEncryptionKey2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 56),
    )


_IpadEncryptionKey2_Type.__name__ = "DisplayString"
_IpadEncryptionKey2_Object = MibScalar
ipadEncryptionKey2 = _IpadEncryptionKey2_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 30, 6),
    _IpadEncryptionKey2_Type()
)
ipadEncryptionKey2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadEncryptionKey2.setStatus("current")


class _IpadEncryptionKey3_Type(DisplayString):
    """Custom type ipadEncryptionKey3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 56),
    )


_IpadEncryptionKey3_Type.__name__ = "DisplayString"
_IpadEncryptionKey3_Object = MibScalar
ipadEncryptionKey3 = _IpadEncryptionKey3_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 30, 7),
    _IpadEncryptionKey3_Type()
)
ipadEncryptionKey3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadEncryptionKey3.setStatus("current")


class _IpadEncryptionKey4_Type(DisplayString):
    """Custom type ipadEncryptionKey4 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 56),
    )


_IpadEncryptionKey4_Type.__name__ = "DisplayString"
_IpadEncryptionKey4_Object = MibScalar
ipadEncryptionKey4 = _IpadEncryptionKey4_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 30, 8),
    _IpadEncryptionKey4_Type()
)
ipadEncryptionKey4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadEncryptionKey4.setStatus("current")


class _IpadEncryptionKey5_Type(DisplayString):
    """Custom type ipadEncryptionKey5 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 56),
    )


_IpadEncryptionKey5_Type.__name__ = "DisplayString"
_IpadEncryptionKey5_Object = MibScalar
ipadEncryptionKey5 = _IpadEncryptionKey5_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 30, 9),
    _IpadEncryptionKey5_Type()
)
ipadEncryptionKey5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadEncryptionKey5.setStatus("current")


class _IpadEncryptionKey6_Type(DisplayString):
    """Custom type ipadEncryptionKey6 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 56),
    )


_IpadEncryptionKey6_Type.__name__ = "DisplayString"
_IpadEncryptionKey6_Object = MibScalar
ipadEncryptionKey6 = _IpadEncryptionKey6_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 30, 10),
    _IpadEncryptionKey6_Type()
)
ipadEncryptionKey6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadEncryptionKey6.setStatus("current")


class _IpadEncryptionKey7_Type(DisplayString):
    """Custom type ipadEncryptionKey7 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 56),
    )


_IpadEncryptionKey7_Type.__name__ = "DisplayString"
_IpadEncryptionKey7_Object = MibScalar
ipadEncryptionKey7 = _IpadEncryptionKey7_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 30, 11),
    _IpadEncryptionKey7_Type()
)
ipadEncryptionKey7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadEncryptionKey7.setStatus("current")


class _IpadEncryptionKey8_Type(DisplayString):
    """Custom type ipadEncryptionKey8 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 56),
    )


_IpadEncryptionKey8_Type.__name__ = "DisplayString"
_IpadEncryptionKey8_Object = MibScalar
ipadEncryptionKey8 = _IpadEncryptionKey8_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 30, 12),
    _IpadEncryptionKey8_Type()
)
ipadEncryptionKey8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadEncryptionKey8.setStatus("current")


class _IpadEncryptionKey9_Type(DisplayString):
    """Custom type ipadEncryptionKey9 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 56),
    )


_IpadEncryptionKey9_Type.__name__ = "DisplayString"
_IpadEncryptionKey9_Object = MibScalar
ipadEncryptionKey9 = _IpadEncryptionKey9_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 30, 13),
    _IpadEncryptionKey9_Type()
)
ipadEncryptionKey9.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadEncryptionKey9.setStatus("current")


class _IpadEncryptionKey10_Type(DisplayString):
    """Custom type ipadEncryptionKey10 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 56),
    )


_IpadEncryptionKey10_Type.__name__ = "DisplayString"
_IpadEncryptionKey10_Object = MibScalar
ipadEncryptionKey10 = _IpadEncryptionKey10_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 30, 14),
    _IpadEncryptionKey10_Type()
)
ipadEncryptionKey10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadEncryptionKey10.setStatus("current")
_IpadEncryptionKeyLife_Type = Integer32
_IpadEncryptionKeyLife_Object = MibScalar
ipadEncryptionKeyLife = _IpadEncryptionKeyLife_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 30, 15),
    _IpadEncryptionKeyLife_Type()
)
ipadEncryptionKeyLife.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadEncryptionKeyLife.setStatus("current")
_IpadAutoLearnDS0_ObjectIdentity = ObjectIdentity
ipadAutoLearnDS0 = _IpadAutoLearnDS0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 31)
)
_IpadAutoLearnDS0Table_Object = MibTable
ipadAutoLearnDS0Table = _IpadAutoLearnDS0Table_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 31, 1)
)
if mibBuilder.loadTexts:
    ipadAutoLearnDS0Table.setStatus("current")
_IpadAutoLearnDS0TableEntry_Object = MibTableRow
ipadAutoLearnDS0TableEntry = _IpadAutoLearnDS0TableEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 31, 1, 1)
)
ipadAutoLearnDS0TableEntry.setIndexNames(
    (0, "IPADv2-MIB", "ipadAutoLearnDS0Index"),
)
if mibBuilder.loadTexts:
    ipadAutoLearnDS0TableEntry.setStatus("current")
_IpadAutoLearnDS0Index_Type = Integer32
_IpadAutoLearnDS0Index_Object = MibTableColumn
ipadAutoLearnDS0Index = _IpadAutoLearnDS0Index_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 31, 1, 1, 1),
    _IpadAutoLearnDS0Index_Type()
)
ipadAutoLearnDS0Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadAutoLearnDS0Index.setStatus("current")


class _IpadAutoLearnDS0Boot_Type(Integer32):
    """Custom type ipadAutoLearnDS0Boot based on Integer32"""
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
        *(("carrierDown", 4),
          ("disable", 2),
          ("enable", 3),
          ("other", 1),
          ("serviceDown", 5))
    )


_IpadAutoLearnDS0Boot_Type.__name__ = "Integer32"
_IpadAutoLearnDS0Boot_Object = MibTableColumn
ipadAutoLearnDS0Boot = _IpadAutoLearnDS0Boot_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 31, 1, 1, 2),
    _IpadAutoLearnDS0Boot_Type()
)
ipadAutoLearnDS0Boot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadAutoLearnDS0Boot.setStatus("current")


class _IpadAutoLearnDS0Rate_Type(Integer32):
    """Custom type ipadAutoLearnDS0Rate based on Integer32"""
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
        *(("auto", 2),
          ("learnAs56K", 3),
          ("learnAs64K", 4),
          ("learnAsVoice", 5),
          ("other", 1))
    )


_IpadAutoLearnDS0Rate_Type.__name__ = "Integer32"
_IpadAutoLearnDS0Rate_Object = MibTableColumn
ipadAutoLearnDS0Rate = _IpadAutoLearnDS0Rate_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 31, 1, 1, 3),
    _IpadAutoLearnDS0Rate_Type()
)
ipadAutoLearnDS0Rate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadAutoLearnDS0Rate.setStatus("current")


class _IpadAutoLearnDS0Command_Type(Integer32):
    """Custom type ipadAutoLearnDS0Command based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("learnNow", 2),
          ("none", 1))
    )


_IpadAutoLearnDS0Command_Type.__name__ = "Integer32"
_IpadAutoLearnDS0Command_Object = MibTableColumn
ipadAutoLearnDS0Command = _IpadAutoLearnDS0Command_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 31, 1, 1, 4),
    _IpadAutoLearnDS0Command_Type()
)
ipadAutoLearnDS0Command.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadAutoLearnDS0Command.setStatus("current")
_IpadUnitAccess_ObjectIdentity = ObjectIdentity
ipadUnitAccess = _IpadUnitAccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 32)
)
_IpadUnitAccessTable_Object = MibTable
ipadUnitAccessTable = _IpadUnitAccessTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 32, 1)
)
if mibBuilder.loadTexts:
    ipadUnitAccessTable.setStatus("current")
_IpadUnitAccessTableEntry_Object = MibTableRow
ipadUnitAccessTableEntry = _IpadUnitAccessTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 32, 1, 1)
)
ipadUnitAccessTableEntry.setIndexNames(
    (0, "IPADv2-MIB", "ipadAutoLearnDS0Index"),
)
if mibBuilder.loadTexts:
    ipadUnitAccessTableEntry.setStatus("current")
_IpadUnitAccessIndex_Type = Integer32
_IpadUnitAccessIndex_Object = MibTableColumn
ipadUnitAccessIndex = _IpadUnitAccessIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 32, 1, 1, 1),
    _IpadUnitAccessIndex_Type()
)
ipadUnitAccessIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadUnitAccessIndex.setStatus("current")
_IpadUnitAccessIpa_Type = IpAddress
_IpadUnitAccessIpa_Object = MibTableColumn
ipadUnitAccessIpa = _IpadUnitAccessIpa_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 32, 1, 1, 2),
    _IpadUnitAccessIpa_Type()
)
ipadUnitAccessIpa.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadUnitAccessIpa.setStatus("current")
_IpadUnitAccessMask_Type = IpAddress
_IpadUnitAccessMask_Object = MibTableColumn
ipadUnitAccessMask = _IpadUnitAccessMask_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 32, 1, 1, 3),
    _IpadUnitAccessMask_Type()
)
ipadUnitAccessMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadUnitAccessMask.setStatus("current")
_IpadTFTPDownload_ObjectIdentity = ObjectIdentity
ipadTFTPDownload = _IpadTFTPDownload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 33)
)
_IpadTFTPDownloadServerIpa_Type = IpAddress
_IpadTFTPDownloadServerIpa_Object = MibScalar
ipadTFTPDownloadServerIpa = _IpadTFTPDownloadServerIpa_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 33, 1),
    _IpadTFTPDownloadServerIpa_Type()
)
ipadTFTPDownloadServerIpa.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadTFTPDownloadServerIpa.setStatus("current")


class _IpadTFTPDownloadFileName_Type(DisplayString):
    """Custom type ipadTFTPDownloadFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_IpadTFTPDownloadFileName_Type.__name__ = "DisplayString"
_IpadTFTPDownloadFileName_Object = MibScalar
ipadTFTPDownloadFileName = _IpadTFTPDownloadFileName_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 33, 2),
    _IpadTFTPDownloadFileName_Type()
)
ipadTFTPDownloadFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadTFTPDownloadFileName.setStatus("current")


class _IpadTFTPDownloadAction_Type(Integer32):
    """Custom type ipadTFTPDownloadAction based on Integer32"""
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
        *(("abort", 3),
          ("getfile", 1),
          ("idle", 4),
          ("putfile", 2))
    )


_IpadTFTPDownloadAction_Type.__name__ = "Integer32"
_IpadTFTPDownloadAction_Object = MibScalar
ipadTFTPDownloadAction = _IpadTFTPDownloadAction_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 33, 3),
    _IpadTFTPDownloadAction_Type()
)
ipadTFTPDownloadAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadTFTPDownloadAction.setStatus("current")


class _IpadTFTPDownloadStatus_Type(Integer32):
    """Custom type ipadTFTPDownloadStatus based on Integer32"""
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
        *(("aborting", 4),
          ("fileAccessFailed", 7),
          ("gettingfile", 2),
          ("idle", 1),
          ("invalidFile", 8),
          ("invalidFileName", 6),
          ("puttingfile", 3),
          ("successful", 5))
    )


_IpadTFTPDownloadStatus_Type.__name__ = "Integer32"
_IpadTFTPDownloadStatus_Object = MibScalar
ipadTFTPDownloadStatus = _IpadTFTPDownloadStatus_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 33, 4),
    _IpadTFTPDownloadStatus_Type()
)
ipadTFTPDownloadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadTFTPDownloadStatus.setStatus("current")
_IpadDataLineMonitor_ObjectIdentity = ObjectIdentity
ipadDataLineMonitor = _IpadDataLineMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 34)
)
_IpadDLMConfig_ObjectIdentity = ObjectIdentity
ipadDLMConfig = _IpadDLMConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 34, 1)
)


class _IpadDLMConfigMode_Type(Integer32):
    """Custom type ipadDLMConfigMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("analyze", 2),
          ("live", 3),
          ("other", 1))
    )


_IpadDLMConfigMode_Type.__name__ = "Integer32"
_IpadDLMConfigMode_Object = MibScalar
ipadDLMConfigMode = _IpadDLMConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 34, 1, 1),
    _IpadDLMConfigMode_Type()
)
ipadDLMConfigMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadDLMConfigMode.setStatus("current")


class _IpadDLMConfigBufferManagement_Type(Integer32):
    """Custom type ipadDLMConfigBufferManagement based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("stopOnFull", 3),
          ("wrap", 2))
    )


_IpadDLMConfigBufferManagement_Type.__name__ = "Integer32"
_IpadDLMConfigBufferManagement_Object = MibScalar
ipadDLMConfigBufferManagement = _IpadDLMConfigBufferManagement_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 34, 1, 2),
    _IpadDLMConfigBufferManagement_Type()
)
ipadDLMConfigBufferManagement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadDLMConfigBufferManagement.setStatus("current")
_IpadDLMTable_Object = MibTable
ipadDLMTable = _IpadDLMTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 34, 2)
)
if mibBuilder.loadTexts:
    ipadDLMTable.setStatus("current")
_IpadDLMTableEntry_Object = MibTableRow
ipadDLMTableEntry = _IpadDLMTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 34, 2, 1)
)
ipadDLMTableEntry.setIndexNames(
    (0, "IPADv2-MIB", "ipadDLMServiceIndex"),
)
if mibBuilder.loadTexts:
    ipadDLMTableEntry.setStatus("current")
_IpadDLMServiceIndex_Type = Integer32
_IpadDLMServiceIndex_Object = MibTableColumn
ipadDLMServiceIndex = _IpadDLMServiceIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 34, 2, 1, 1),
    _IpadDLMServiceIndex_Type()
)
ipadDLMServiceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDLMServiceIndex.setStatus("current")


class _IpadDLMEnable_Type(Integer32):
    """Custom type ipadDLMEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 3),
          ("other", 1))
    )


_IpadDLMEnable_Type.__name__ = "Integer32"
_IpadDLMEnable_Object = MibTableColumn
ipadDLMEnable = _IpadDLMEnable_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 34, 2, 1, 2),
    _IpadDLMEnable_Type()
)
ipadDLMEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadDLMEnable.setStatus("current")


class _IpadDLMTxRxFilter_Type(Integer32):
    """Custom type ipadDLMTxRxFilter based on Integer32"""
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
        *(("all", 2),
          ("other", 1),
          ("receiveOnly", 4),
          ("transmitOnly", 3))
    )


_IpadDLMTxRxFilter_Type.__name__ = "Integer32"
_IpadDLMTxRxFilter_Object = MibTableColumn
ipadDLMTxRxFilter = _IpadDLMTxRxFilter_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 34, 2, 1, 3),
    _IpadDLMTxRxFilter_Type()
)
ipadDLMTxRxFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadDLMTxRxFilter.setStatus("current")


class _IpadDLMPatternEnable_Type(Integer32):
    """Custom type ipadDLMPatternEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 3),
          ("other", 1))
    )


_IpadDLMPatternEnable_Type.__name__ = "Integer32"
_IpadDLMPatternEnable_Object = MibTableColumn
ipadDLMPatternEnable = _IpadDLMPatternEnable_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 34, 2, 1, 4),
    _IpadDLMPatternEnable_Type()
)
ipadDLMPatternEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadDLMPatternEnable.setStatus("current")
_IpadDLMPattern_Type = Integer32
_IpadDLMPattern_Object = MibTableColumn
ipadDLMPattern = _IpadDLMPattern_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 34, 2, 1, 5),
    _IpadDLMPattern_Type()
)
ipadDLMPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadDLMPattern.setStatus("current")
_IpadDLMPatternMask_Type = Integer32
_IpadDLMPatternMask_Object = MibTableColumn
ipadDLMPatternMask = _IpadDLMPatternMask_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 34, 2, 1, 6),
    _IpadDLMPatternMask_Type()
)
ipadDLMPatternMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadDLMPatternMask.setStatus("current")


class _IpadDLMPatternOffset_Type(Integer32):
    """Custom type ipadDLMPatternOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_IpadDLMPatternOffset_Type.__name__ = "Integer32"
_IpadDLMPatternOffset_Object = MibTableColumn
ipadDLMPatternOffset = _IpadDLMPatternOffset_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 34, 2, 1, 7),
    _IpadDLMPatternOffset_Type()
)
ipadDLMPatternOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadDLMPatternOffset.setStatus("current")
_IpadDLMPacketTable_Object = MibTable
ipadDLMPacketTable = _IpadDLMPacketTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 34, 3)
)
if mibBuilder.loadTexts:
    ipadDLMPacketTable.setStatus("current")
_IpadDLMPacketTableEntry_Object = MibTableRow
ipadDLMPacketTableEntry = _IpadDLMPacketTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 34, 3, 1)
)
ipadDLMPacketTableEntry.setIndexNames(
    (0, "IPADv2-MIB", "ipadDLMPacketIndex"),
)
if mibBuilder.loadTexts:
    ipadDLMPacketTableEntry.setStatus("current")
_IpadDLMPacketIndex_Type = Integer32
_IpadDLMPacketIndex_Object = MibTableColumn
ipadDLMPacketIndex = _IpadDLMPacketIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 34, 3, 1, 1),
    _IpadDLMPacketIndex_Type()
)
ipadDLMPacketIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDLMPacketIndex.setStatus("current")
_IpadDLMPacketServiceIndex_Type = Integer32
_IpadDLMPacketServiceIndex_Object = MibTableColumn
ipadDLMPacketServiceIndex = _IpadDLMPacketServiceIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 34, 3, 1, 2),
    _IpadDLMPacketServiceIndex_Type()
)
ipadDLMPacketServiceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDLMPacketServiceIndex.setStatus("current")
_IpadDLMPacketTimestamp_Type = TimeTicks
_IpadDLMPacketTimestamp_Object = MibTableColumn
ipadDLMPacketTimestamp = _IpadDLMPacketTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 34, 3, 1, 3),
    _IpadDLMPacketTimestamp_Type()
)
ipadDLMPacketTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDLMPacketTimestamp.setStatus("current")


class _IpadDLMPacketDataDirection_Type(Integer32):
    """Custom type ipadDLMPacketDataDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("receive", 3),
          ("transmit", 2))
    )


_IpadDLMPacketDataDirection_Type.__name__ = "Integer32"
_IpadDLMPacketDataDirection_Object = MibTableColumn
ipadDLMPacketDataDirection = _IpadDLMPacketDataDirection_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 34, 3, 1, 4),
    _IpadDLMPacketDataDirection_Type()
)
ipadDLMPacketDataDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDLMPacketDataDirection.setStatus("current")
_IpadDLMPacketSize_Type = Integer32
_IpadDLMPacketSize_Object = MibTableColumn
ipadDLMPacketSize = _IpadDLMPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 34, 3, 1, 5),
    _IpadDLMPacketSize_Type()
)
ipadDLMPacketSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDLMPacketSize.setStatus("current")


class _IpadDLMPacketData_Type(OctetString):
    """Custom type ipadDLMPacketData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_IpadDLMPacketData_Type.__name__ = "OctetString"
_IpadDLMPacketData_Object = MibTableColumn
ipadDLMPacketData = _IpadDLMPacketData_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 34, 3, 1, 6),
    _IpadDLMPacketData_Type()
)
ipadDLMPacketData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDLMPacketData.setStatus("current")
_IpadOrigPing_ObjectIdentity = ObjectIdentity
ipadOrigPing = _IpadOrigPing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 35)
)


class _IpadOrigPingCommand_Type(Integer32):
    """Custom type ipadOrigPingCommand based on Integer32"""
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
        *(("clearStats", 4),
          ("other", 1),
          ("start", 3),
          ("stop", 2))
    )


_IpadOrigPingCommand_Type.__name__ = "Integer32"
_IpadOrigPingCommand_Object = MibScalar
ipadOrigPingCommand = _IpadOrigPingCommand_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 35, 1),
    _IpadOrigPingCommand_Type()
)
ipadOrigPingCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadOrigPingCommand.setStatus("current")
_IpadOrigPingDestIPAddr_Type = IpAddress
_IpadOrigPingDestIPAddr_Object = MibScalar
ipadOrigPingDestIPAddr = _IpadOrigPingDestIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 35, 2),
    _IpadOrigPingDestIPAddr_Type()
)
ipadOrigPingDestIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadOrigPingDestIPAddr.setStatus("current")
_IpadOrigPingTimeout_Type = Integer32
_IpadOrigPingTimeout_Object = MibScalar
ipadOrigPingTimeout = _IpadOrigPingTimeout_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 35, 3),
    _IpadOrigPingTimeout_Type()
)
ipadOrigPingTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadOrigPingTimeout.setStatus("current")
_IpadOrigPingSize_Type = Integer32
_IpadOrigPingSize_Object = MibScalar
ipadOrigPingSize = _IpadOrigPingSize_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 35, 4),
    _IpadOrigPingSize_Type()
)
ipadOrigPingSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadOrigPingSize.setStatus("current")
_IpadOrigPingToSend_Type = Integer32
_IpadOrigPingToSend_Object = MibScalar
ipadOrigPingToSend = _IpadOrigPingToSend_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 35, 5),
    _IpadOrigPingToSend_Type()
)
ipadOrigPingToSend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadOrigPingToSend.setStatus("current")
_IpadOrigPingSent_Type = Integer32
_IpadOrigPingSent_Object = MibScalar
ipadOrigPingSent = _IpadOrigPingSent_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 35, 6),
    _IpadOrigPingSent_Type()
)
ipadOrigPingSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadOrigPingSent.setStatus("current")
_IpadOrigPingReplies_Type = Integer32
_IpadOrigPingReplies_Object = MibScalar
ipadOrigPingReplies = _IpadOrigPingReplies_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 35, 7),
    _IpadOrigPingReplies_Type()
)
ipadOrigPingReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadOrigPingReplies.setStatus("current")
_IpadOrigPingDelayMin_Type = Integer32
_IpadOrigPingDelayMin_Object = MibScalar
ipadOrigPingDelayMin = _IpadOrigPingDelayMin_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 35, 8),
    _IpadOrigPingDelayMin_Type()
)
ipadOrigPingDelayMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadOrigPingDelayMin.setStatus("current")
_IpadOrigPingDelayAvg_Type = Integer32
_IpadOrigPingDelayAvg_Object = MibScalar
ipadOrigPingDelayAvg = _IpadOrigPingDelayAvg_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 35, 9),
    _IpadOrigPingDelayAvg_Type()
)
ipadOrigPingDelayAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadOrigPingDelayAvg.setStatus("current")
_IpadOrigPingDelayMax_Type = Integer32
_IpadOrigPingDelayMax_Object = MibScalar
ipadOrigPingDelayMax = _IpadOrigPingDelayMax_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 35, 10),
    _IpadOrigPingDelayMax_Type()
)
ipadOrigPingDelayMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadOrigPingDelayMax.setStatus("current")


class _IpadOrigPingReport_Type(DisplayString):
    """Custom type ipadOrigPingReport based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_IpadOrigPingReport_Type.__name__ = "DisplayString"
_IpadOrigPingReport_Object = MibScalar
ipadOrigPingReport = _IpadOrigPingReport_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 35, 11),
    _IpadOrigPingReport_Type()
)
ipadOrigPingReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadOrigPingReport.setStatus("current")


class _IpadOrigPingExceptReport_Type(DisplayString):
    """Custom type ipadOrigPingExceptReport based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_IpadOrigPingExceptReport_Type.__name__ = "DisplayString"
_IpadOrigPingExceptReport_Object = MibScalar
ipadOrigPingExceptReport = _IpadOrigPingExceptReport_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 35, 12),
    _IpadOrigPingExceptReport_Type()
)
ipadOrigPingExceptReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadOrigPingExceptReport.setStatus("current")
_IpadTraps_ObjectIdentity = ObjectIdentity
ipadTraps = _IpadTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 999)
)
_IpadTrapsPrefix_ObjectIdentity = ObjectIdentity
ipadTrapsPrefix = _IpadTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 999, 0)
)

# Managed Objects groups


# Notification objects

ipadFrPortRxInvalidFramesExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 999, 0, 25000)
)
ipadFrPortRxInvalidFramesExceeded.setObjects(
    ("IPADv2-MIB", "ipadFrPortRxInvAlmAlarm")
)
if mibBuilder.loadTexts:
    ipadFrPortRxInvalidFramesExceeded.setStatus(
        "current"
    )

ipadFrPortRxThroughputExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 999, 0, 25001)
)
ipadFrPortRxThroughputExceeded.setObjects(
    ("IPADv2-MIB", "ipadFrPortRxAlmAlarm")
)
if mibBuilder.loadTexts:
    ipadFrPortRxThroughputExceeded.setStatus(
        "current"
    )

ipadFrPortTxThroughputExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 999, 0, 25002)
)
ipadFrPortTxThroughputExceeded.setObjects(
    ("IPADv2-MIB", "ipadFrPortTxAlmAlarm")
)
if mibBuilder.loadTexts:
    ipadFrPortTxThroughputExceeded.setStatus(
        "current"
    )

ipadDLCItxCIRexceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 999, 0, 25003)
)
ipadDLCItxCIRexceeded.setObjects(
    ("IPADv2-MIB", "ipadDLCItxExCIRAlarm")
)
if mibBuilder.loadTexts:
    ipadDLCItxCIRexceeded.setStatus(
        "current"
    )

ipadDLCItxBEexceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 999, 0, 25004)
)
ipadDLCItxBEexceeded.setObjects(
    ("IPADv2-MIB", "ipadDLCItxExBeAlarm")
)
if mibBuilder.loadTexts:
    ipadDLCItxBEexceeded.setStatus(
        "current"
    )

ipadDLCIRxCongestionExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 999, 0, 25005)
)
ipadDLCIRxCongestionExceeded.setObjects(
    ("IPADv2-MIB", "ipadDLCIrxCongAlarm")
)
if mibBuilder.loadTexts:
    ipadDLCIRxCongestionExceeded.setStatus(
        "current"
    )

ipadUserTxExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 999, 0, 25006)
)
ipadUserTxExceeded.setObjects(
    ("IPADv2-MIB", "ipadUserTxAlmAlarm")
)
if mibBuilder.loadTexts:
    ipadUserTxExceeded.setStatus(
        "current"
    )

ipadDlciRxBECNinCIRAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 999, 0, 25007)
)
ipadDlciRxBECNinCIRAlarm.setObjects(
    ("IPADv2-MIB", "ipadDLCIrxBECNinCIR")
)
if mibBuilder.loadTexts:
    ipadDlciRxBECNinCIRAlarm.setStatus(
        "current"
    )

ipadDlciUASExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 999, 0, 25008)
)
ipadDlciUASExceeded.setObjects(
    ("IPADv2-MIB", "ipadDLCIUASAlarm")
)
if mibBuilder.loadTexts:
    ipadDlciUASExceeded.setStatus(
        "current"
    )

ipadserialDteDTRAlarmExists = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 999, 0, 25009)
)
ipadserialDteDTRAlarmExists.setObjects(
    ("DS8200v2-MIB", "serialDteDTRAlarmStatus")
)
if mibBuilder.loadTexts:
    ipadserialDteDTRAlarmExists.setStatus(
        "current"
    )

ipadt1e1ESAlarmDeclared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 999, 0, 25010)
)
ipadt1e1ESAlarmDeclared.setObjects(
    ("DS8200v2-MIB", "t1e1ESCount")
)
if mibBuilder.loadTexts:
    ipadt1e1ESAlarmDeclared.setStatus(
        "current"
    )

ipadt1e1SESAlarmDeclared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 999, 0, 25011)
)
ipadt1e1SESAlarmDeclared.setObjects(
    ("DS8200v2-MIB", "t1e1SESCount")
)
if mibBuilder.loadTexts:
    ipadt1e1SESAlarmDeclared.setStatus(
        "current"
    )

ipadt1e1LOSSAlarmDeclared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 999, 0, 25012)
)
ipadt1e1LOSSAlarmDeclared.setObjects(
    ("DS8200v2-MIB", "t1e1LOSSCount")
)
if mibBuilder.loadTexts:
    ipadt1e1LOSSAlarmDeclared.setStatus(
        "current"
    )

ipadt1e1UASAlarmDeclared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 999, 0, 25013)
)
ipadt1e1UASAlarmDeclared.setObjects(
    ("DS8200v2-MIB", "t1e1UASCount")
)
if mibBuilder.loadTexts:
    ipadt1e1UASAlarmDeclared.setStatus(
        "current"
    )

ipadt1e1CSSAlarmDeclared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 999, 0, 25014)
)
ipadt1e1CSSAlarmDeclared.setObjects(
    ("DS8200v2-MIB", "t1e1CSSCount")
)
if mibBuilder.loadTexts:
    ipadt1e1CSSAlarmDeclared.setStatus(
        "current"
    )

ipadt1e1BPVSAlarmDeclared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 999, 0, 25015)
)
ipadt1e1BPVSAlarmDeclared.setObjects(
    ("DS8200v2-MIB", "t1e1BPVSCount")
)
if mibBuilder.loadTexts:
    ipadt1e1BPVSAlarmDeclared.setStatus(
        "current"
    )

ipadt1e1OOFSAlarmDeclared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 999, 0, 25016)
)
ipadt1e1OOFSAlarmDeclared.setObjects(
    ("DS8200v2-MIB", "t1e1OOFSCount")
)
if mibBuilder.loadTexts:
    ipadt1e1OOFSAlarmDeclared.setStatus(
        "current"
    )

ipadt1e1AISAlarmExists = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 999, 0, 25017)
)
ipadt1e1AISAlarmExists.setObjects(
    ("DS8200v2-MIB", "t1e1AISCount")
)
if mibBuilder.loadTexts:
    ipadt1e1AISAlarmExists.setStatus(
        "current"
    )

ipadt1e1RASAlarmExists = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 999, 0, 25018)
)
ipadt1e1RASAlarmExists.setObjects(
    ("DS8200v2-MIB", "t1e1RASCount")
)
if mibBuilder.loadTexts:
    ipadt1e1RASAlarmExists.setStatus(
        "current"
    )

ipadDLCIremoteSOSAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 999, 0, 25019)
)
ipadDLCIremoteSOSAlarm.setObjects(
    ("IPADv2-MIB", "ipadDLCIremoteEquipActive")
)
if mibBuilder.loadTexts:
    ipadDLCIremoteSOSAlarm.setStatus(
        "current"
    )

ipadDdsLOSSAlarmDeclared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 999, 0, 25020)
)
ipadDdsLOSSAlarmDeclared.setObjects(
    ("DS8200v2-MIB", "ddsNetLOSCount")
)
if mibBuilder.loadTexts:
    ipadDdsLOSSAlarmDeclared.setStatus(
        "current"
    )

ipadDdsOOFSAlarmDeclared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 999, 0, 25021)
)
ipadDdsOOFSAlarmDeclared.setObjects(
    ("DS8200v2-MIB", "ddsNetOOFCount")
)
if mibBuilder.loadTexts:
    ipadDdsOOFSAlarmDeclared.setStatus(
        "current"
    )

ipadDdsOOSSAlarmDeclared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 999, 0, 25022)
)
ipadDdsOOSSAlarmDeclared.setObjects(
    ("DS8200v2-MIB", "ddsNetOOSCount")
)
if mibBuilder.loadTexts:
    ipadDdsOOSSAlarmDeclared.setStatus(
        "current"
    )

ipadDdsFDLSAlarmDeclared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 999, 0, 25023)
)
ipadDdsFDLSAlarmDeclared.setObjects(
    ("DS8200v2-MIB", "ddsNetFDLCount")
)
if mibBuilder.loadTexts:
    ipadDdsFDLSAlarmDeclared.setStatus(
        "current"
    )

ipadDdsBPVSAlarmDeclared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 999, 0, 25024)
)
ipadDdsBPVSAlarmDeclared.setObjects(
    ("DS8200v2-MIB", "ddsNetBPVCount")
)
if mibBuilder.loadTexts:
    ipadDdsBPVSAlarmDeclared.setStatus(
        "current"
    )

ipadDS0HighAlarmDeclared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 999, 0, 25025)
)
ipadDS0HighAlarmDeclared.setObjects(
    ("IPADv2-MIB", "ipadDS0ConfigHighUtilCount")
)
if mibBuilder.loadTexts:
    ipadDS0HighAlarmDeclared.setStatus(
        "current"
    )

ipadDS0LowAlarmDeclared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 999, 0, 25026)
)
ipadDS0LowAlarmDeclared.setObjects(
    ("IPADv2-MIB", "ipadDS0ConfigLowUtilAlarm")
)
if mibBuilder.loadTexts:
    ipadDS0LowAlarmDeclared.setStatus(
        "current"
    )

ipadHDLCRxHighAlarmDeclared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 999, 0, 25027)
)
ipadHDLCRxHighAlarmDeclared.setObjects(
    ("IPADv2-MIB", "ipadHDLCConfigRxHighUtilCount")
)
if mibBuilder.loadTexts:
    ipadHDLCRxHighAlarmDeclared.setStatus(
        "current"
    )

ipadHDLCRxLowAlarmDeclared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 999, 0, 25028)
)
ipadHDLCRxLowAlarmDeclared.setObjects(
    ("IPADv2-MIB", "ipadHDLCConfigRxLowUtilAlarm")
)
if mibBuilder.loadTexts:
    ipadHDLCRxLowAlarmDeclared.setStatus(
        "current"
    )

ipadHDLCTxHighAlarmDeclared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 999, 0, 25029)
)
ipadHDLCTxHighAlarmDeclared.setObjects(
    ("IPADv2-MIB", "ipadHDLCConfigTxHighUtilCount")
)
if mibBuilder.loadTexts:
    ipadHDLCTxHighAlarmDeclared.setStatus(
        "current"
    )

ipadHDLCTxLowAlarmDeclared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 999, 0, 25030)
)
ipadHDLCTxLowAlarmDeclared.setObjects(
    ("IPADv2-MIB", "ipadHDLCConfigTxLowUtilAlarm")
)
if mibBuilder.loadTexts:
    ipadHDLCTxLowAlarmDeclared.setStatus(
        "current"
    )

ipadDbuActivated = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 999, 0, 25031)
)
ipadDbuActivated.setObjects(
    ("IPADv2-MIB", "ipadDbuStatus")
)
if mibBuilder.loadTexts:
    ipadDbuActivated.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IPADv2-MIB",
    **{"ipad": ipad,
       "ipadFrPort": ipadFrPort,
       "ipadFrPortTable": ipadFrPortTable,
       "ipadFrPortTableEntry": ipadFrPortTableEntry,
       "ipadFrPortService": ipadFrPortService,
       "ipadFrPortActive": ipadFrPortActive,
       "ipadFrPortLMIType": ipadFrPortLMIType,
       "ipadFrPortLMIMode": ipadFrPortLMIMode,
       "ipadFrPortRxInvAlmThreshold": ipadFrPortRxInvAlmThreshold,
       "ipadFrPortRxInvAlmAlarm": ipadFrPortRxInvAlmAlarm,
       "ipadFrPortTxAlmThreshold": ipadFrPortTxAlmThreshold,
       "ipadFrPortTxAlmAlarm": ipadFrPortTxAlmAlarm,
       "ipadFrPortRxAlmThreshold": ipadFrPortRxAlmThreshold,
       "ipadFrPortRxAlmAlarm": ipadFrPortRxAlmAlarm,
       "ipadFrPortAlarmReset": ipadFrPortAlarmReset,
       "ipadService": ipadService,
       "ipadServiceTable": ipadServiceTable,
       "ipadServiceTableEntry": ipadServiceTableEntry,
       "ipadServiceIndex": ipadServiceIndex,
       "ipadServiceifIndex": ipadServiceifIndex,
       "ipadServiceType": ipadServiceType,
       "ipadServicePair": ipadServicePair,
       "ipadServiceStatus": ipadServiceStatus,
       "ipadServiceAddService": ipadServiceAddService,
       "ipadServiceDeleteService": ipadServiceDeleteService,
       "ipadChannel": ipadChannel,
       "ipadChannelTable": ipadChannelTable,
       "ipadChannelTableEntry": ipadChannelTableEntry,
       "ipadChannelifIndex": ipadChannelifIndex,
       "ipadChannelIndex": ipadChannelIndex,
       "ipadChannelService": ipadChannelService,
       "ipadChannelPair": ipadChannelPair,
       "ipadChannelRate": ipadChannelRate,
       "ipadChannelIdlePattern": ipadChannelIdlePattern,
       "ipadDLCI": ipadDLCI,
       "ipadDLCITable": ipadDLCITable,
       "ipadDLCITableEntry": ipadDLCITableEntry,
       "ipadDLCIservice": ipadDLCIservice,
       "ipadDLCInumber": ipadDLCInumber,
       "ipadDLCIactive": ipadDLCIactive,
       "ipadDLCIcongestion": ipadDLCIcongestion,
       "ipadDLCIremote": ipadDLCIremote,
       "ipadDLCIremoteUnit": ipadDLCIremoteUnit,
       "ipadDLCIremoteEquipActive": ipadDLCIremoteEquipActive,
       "ipadDLCIencapsulation": ipadDLCIencapsulation,
       "ipadDLCIproprietary": ipadDLCIproprietary,
       "ipadDLCIpropOffset": ipadDLCIpropOffset,
       "ipadDLCIinBand": ipadDLCIinBand,
       "ipadDLCICIR": ipadDLCICIR,
       "ipadDLCIBe": ipadDLCIBe,
       "ipadDLCIminBC": ipadDLCIminBC,
       "ipadDLCIrxMon": ipadDLCIrxMon,
       "ipadDLCIdEctrl": ipadDLCIdEctrl,
       "ipadDLCIenableDelay": ipadDLCIenableDelay,
       "ipadDLCItxExCIRThreshold": ipadDLCItxExCIRThreshold,
       "ipadDLCItxExCIRAlarm": ipadDLCItxExCIRAlarm,
       "ipadDLCItxExBeThreshold": ipadDLCItxExBeThreshold,
       "ipadDLCItxExBeAlarm": ipadDLCItxExBeAlarm,
       "ipadDLCIrxCongThreshold": ipadDLCIrxCongThreshold,
       "ipadDLCIrxCongAlarm": ipadDLCIrxCongAlarm,
       "ipadDLCIrxBECNinCIR": ipadDLCIrxBECNinCIR,
       "ipadDLCIUASThreshold": ipadDLCIUASThreshold,
       "ipadDLCIUASAlarm": ipadDLCIUASAlarm,
       "ipadDLCIAlarmReset": ipadDLCIAlarmReset,
       "ipadDLCIRoundTripDelaySize": ipadDLCIRoundTripDelaySize,
       "ipadDLCIRoundTripDelayRate": ipadDLCIRoundTripDelayRate,
       "ipadDLCIRemoteFramesOfferedWithinCIR": ipadDLCIRemoteFramesOfferedWithinCIR,
       "ipadDLCIRemoteFramesOfferedWithinBE": ipadDLCIRemoteFramesOfferedWithinBE,
       "ipadDLCIFramesReceived": ipadDLCIFramesReceived,
       "ipadDLCIRemoteDataOfferedWithinCIR": ipadDLCIRemoteDataOfferedWithinCIR,
       "ipadDLCIRemoteDataOfferedWithinBE": ipadDLCIRemoteDataOfferedWithinBE,
       "ipadDLCIDataReceived": ipadDLCIDataReceived,
       "ipadDLCIRemoteIPAddress": ipadDLCIRemoteIPAddress,
       "ipadDLCICompressionStatus": ipadDLCICompressionStatus,
       "ipadDLCICompressionTxOctetsIn": ipadDLCICompressionTxOctetsIn,
       "ipadDLCICompressionTxOctetsOut": ipadDLCICompressionTxOctetsOut,
       "ipadDLCICompressionRxOctetsIn": ipadDLCICompressionRxOctetsIn,
       "ipadDLCICompressionRxOctetsOut": ipadDLCICompressionRxOctetsOut,
       "ipadDLCILastChange": ipadDLCILastChange,
       "ipadEndpoint": ipadEndpoint,
       "ipadEndpointTable": ipadEndpointTable,
       "ipadEndpointTableEntry": ipadEndpointTableEntry,
       "ipadEndpointIndex": ipadEndpointIndex,
       "ipadEndpointName": ipadEndpointName,
       "ipadEndpointService": ipadEndpointService,
       "ipadEndpointDLCInumber": ipadEndpointDLCInumber,
       "ipadEndpointType": ipadEndpointType,
       "ipadEndpointForward": ipadEndpointForward,
       "ipadEndpointBackup": ipadEndpointBackup,
       "ipadEndpointRefSLP": ipadEndpointRefSLP,
       "ipadEndpointRemoteIpAddr": ipadEndpointRemoteIpAddr,
       "ipadEndpointRemoteIpMask": ipadEndpointRemoteIpMask,
       "ipadEndpointAddEndpoint": ipadEndpointAddEndpoint,
       "ipadEndpointDeleteEndpoint": ipadEndpointDeleteEndpoint,
       "ipadEndpointLastChange": ipadEndpointLastChange,
       "ipadUser": ipadUser,
       "ipadUserTable": ipadUserTable,
       "ipadUserTableEntry": ipadUserTableEntry,
       "ipadUserIndex": ipadUserIndex,
       "ipadUserFilterByDLCI": ipadUserFilterByDLCI,
       "ipadUserService": ipadUserService,
       "ipadUserDLCI": ipadUserDLCI,
       "ipadUserFilterByIPAddress": ipadUserFilterByIPAddress,
       "ipadUserIPAddress": ipadUserIPAddress,
       "ipadUserIPMask": ipadUserIPMask,
       "ipadUserFilterByIPPort": ipadUserFilterByIPPort,
       "ipadUserIPPort": ipadUserIPPort,
       "ipadUserTxAlmThreshold": ipadUserTxAlmThreshold,
       "ipadUserTxAlmAlarm": ipadUserTxAlmAlarm,
       "ipadUserAlarmReset": ipadUserAlarmReset,
       "ipadUserVpi": ipadUserVpi,
       "ipadUserVci": ipadUserVci,
       "ipadUserFilterByVpiVci": ipadUserFilterByVpiVci,
       "ipadUserIPStatTimeRemaining": ipadUserIPStatTimeRemaining,
       "ipadUserIPStatTimeDuration": ipadUserIPStatTimeDuration,
       "ipadUserIPStatStartTime": ipadUserIPStatStartTime,
       "ipadUserIPStatRequestedReportSize": ipadUserIPStatRequestedReportSize,
       "ipadUserIPStatGrantedReportSize": ipadUserIPStatGrantedReportSize,
       "ipadUserIPStatReportNumber": ipadUserIPStatReportNumber,
       "ipadUserIPStatDiscardType": ipadUserIPStatDiscardType,
       "ipadPPP": ipadPPP,
       "ipadPPPCfgTable": ipadPPPCfgTable,
       "ipadPPPCfgTableEntry": ipadPPPCfgTableEntry,
       "ipadPPPCfgService": ipadPPPCfgService,
       "ipadPPPCfgDialMode": ipadPPPCfgDialMode,
       "ipadPPPCfgInactivityTimer": ipadPPPCfgInactivityTimer,
       "ipadPPPCfgNegotiationInit": ipadPPPCfgNegotiationInit,
       "ipadPPPCfgMRU": ipadPPPCfgMRU,
       "ipadPPPCfgACCM": ipadPPPCfgACCM,
       "ipadPPPCfgNegMRU": ipadPPPCfgNegMRU,
       "ipadPPPCfgNegACCM": ipadPPPCfgNegACCM,
       "ipadPPPCfgNegMagic": ipadPPPCfgNegMagic,
       "ipadPPPCfgNegCompression": ipadPPPCfgNegCompression,
       "ipadPPPCfgNegAddress": ipadPPPCfgNegAddress,
       "ipadPPPCfgNegPAP": ipadPPPCfgNegPAP,
       "ipadPPPCfgNegCHAP": ipadPPPCfgNegCHAP,
       "ipadPPPCfgAllowPAP": ipadPPPCfgAllowPAP,
       "ipadPPPCfgAllowCHAP": ipadPPPCfgAllowCHAP,
       "ipadPPPCfgPAPUsername": ipadPPPCfgPAPUsername,
       "ipadPPPCfgPAPPassword": ipadPPPCfgPAPPassword,
       "ipadPPPCfgCHAPUsername": ipadPPPCfgCHAPUsername,
       "ipadPPPCfgCHAPSecret": ipadPPPCfgCHAPSecret,
       "ipadPPPCfgPortIpAddress": ipadPPPCfgPortIpAddress,
       "ipadPPPCfgPeerIpAddress": ipadPPPCfgPeerIpAddress,
       "ipadPPPCfgNegIpAddress": ipadPPPCfgNegIpAddress,
       "ipadPPPCfgNegIPCPCompression": ipadPPPCfgNegIPCPCompression,
       "ipadPPPCfgSubnetMask": ipadPPPCfgSubnetMask,
       "ipadPPPCfgAuthChallengeInterval": ipadPPPCfgAuthChallengeInterval,
       "ipadPPPCfgEndpoint": ipadPPPCfgEndpoint,
       "ipadPPPCfgNegIpMask": ipadPPPCfgNegIpMask,
       "ipadPPPCfgNegDNSAddress": ipadPPPCfgNegDNSAddress,
       "ipadPPPPAPTable": ipadPPPPAPTable,
       "ipadPPPPAPTableEntry": ipadPPPPAPTableEntry,
       "ipadPPPPAPTableIndex": ipadPPPPAPTableIndex,
       "ipadPPPPAPTableUsername": ipadPPPPAPTableUsername,
       "ipadPPPPAPTablePassword": ipadPPPPAPTablePassword,
       "ipadPPPCHAPTable": ipadPPPCHAPTable,
       "ipadPPPCHAPTableEntry": ipadPPPCHAPTableEntry,
       "ipadPPPCHAPTableIndex": ipadPPPCHAPTableIndex,
       "ipadPPPCHAPTableUsername": ipadPPPCHAPTableUsername,
       "ipadPPPCHAPTableSecret": ipadPPPCHAPTableSecret,
       "ipadModem": ipadModem,
       "ipadModemDialTable": ipadModemDialTable,
       "ipadModemDialTableEntry": ipadModemDialTableEntry,
       "ipadModemDialTableIndex": ipadModemDialTableIndex,
       "ipadModemDialDataIndex": ipadModemDialDataIndex,
       "ipadModemDialNumber": ipadModemDialNumber,
       "ipadModemDialAbortTimer": ipadModemDialAbortTimer,
       "ipadModemDialRedialAttempts": ipadModemDialRedialAttempts,
       "ipadModemDialDelayBeforeRedial": ipadModemDialDelayBeforeRedial,
       "ipadModemDialLoginScript": ipadModemDialLoginScript,
       "ipadModemDialUsername": ipadModemDialUsername,
       "ipadModemDialPassword": ipadModemDialPassword,
       "ipadModemDialChallengeScript": ipadModemDialChallengeScript,
       "ipadModemDialAnswerRings": ipadModemDialAnswerRings,
       "ipadModemDialCommand": ipadModemDialCommand,
       "ipadModemDialStatus": ipadModemDialStatus,
       "ipadModemDialSecurity": ipadModemDialSecurity,
       "ipadModemDialCallbackRedialDelay": ipadModemDialCallbackRedialDelay,
       "ipadModemDialCallbackTimeout": ipadModemDialCallbackTimeout,
       "ipadModemDialCallbackChalScript": ipadModemDialCallbackChalScript,
       "ipadModemDialCallbackRspScript": ipadModemDialCallbackRspScript,
       "ipadModemDataTable": ipadModemDataTable,
       "ipadModemDataTableEntry": ipadModemDataTableEntry,
       "ipadModemDataTableIndex": ipadModemDataTableIndex,
       "ipadModemDataModemName": ipadModemDataModemName,
       "ipadModemDataSetupScript": ipadModemDataSetupScript,
       "ipadModemDataDialingScript": ipadModemDataDialingScript,
       "ipadModemDataAnswerScript": ipadModemDataAnswerScript,
       "ipadModemDataHangupScript": ipadModemDataHangupScript,
       "ipadModemDataSyncScript": ipadModemDataSyncScript,
       "ipadModemDataSyncMethod": ipadModemDataSyncMethod,
       "ipadModemDataSetupScript2": ipadModemDataSetupScript2,
       "ipadModemDataSetupScript3": ipadModemDataSetupScript3,
       "ipadModemDataSetupScript4": ipadModemDataSetupScript4,
       "ipadModemDataSetupScript5": ipadModemDataSetupScript5,
       "ipadDbuTable": ipadDbuTable,
       "ipadDbuTableEntry": ipadDbuTableEntry,
       "ipadDbuIndex": ipadDbuIndex,
       "ipadDbuOperation": ipadDbuOperation,
       "ipadDbuMonitoredifIndex": ipadDbuMonitoredifIndex,
       "ipadDbuActivator1": ipadDbuActivator1,
       "ipadDbuActivator2": ipadDbuActivator2,
       "ipadDbuRevertDelay": ipadDbuRevertDelay,
       "ipadDbuTrapDelay": ipadDbuTrapDelay,
       "ipadDbuStatus": ipadDbuStatus,
       "ipadDbuTrap": ipadDbuTrap,
       "ipadDbuDailyTable": ipadDbuDailyTable,
       "ipadDbuDailyTableEntry": ipadDbuDailyTableEntry,
       "ipadDbuDailyIndex": ipadDbuDailyIndex,
       "ipadDbuDailyDayOfWeek": ipadDbuDailyDayOfWeek,
       "ipadDbuDailyStart": ipadDbuDailyStart,
       "ipadDbuDailyLength": ipadDbuDailyLength,
       "ipadSvcAware": ipadSvcAware,
       "ipadFrPortStatsTable": ipadFrPortStatsTable,
       "ipadFrPortStatsEntry": ipadFrPortStatsEntry,
       "ipadFrPortStatsService": ipadFrPortStatsService,
       "ipadFrPortStatsPeriod": ipadFrPortStatsPeriod,
       "ipadFrPortStatsTxFrames": ipadFrPortStatsTxFrames,
       "ipadFrPortStatsRxFrames": ipadFrPortStatsRxFrames,
       "ipadFrPortStatsTxOctets": ipadFrPortStatsTxOctets,
       "ipadFrPortStatsRxOctets": ipadFrPortStatsRxOctets,
       "ipadFrPortStatsTxMgmtFrames": ipadFrPortStatsTxMgmtFrames,
       "ipadFrPortStatsRxMgmtFrames": ipadFrPortStatsRxMgmtFrames,
       "ipadFrPortStatsTxMgmtOctets": ipadFrPortStatsTxMgmtOctets,
       "ipadFrPortStatsRxMgmtOctets": ipadFrPortStatsRxMgmtOctets,
       "ipadFrPortStatsRxFECN": ipadFrPortStatsRxFECN,
       "ipadFrPortStatsRxBECN": ipadFrPortStatsRxBECN,
       "ipadFrPortStatsRxInvalid": ipadFrPortStatsRxInvalid,
       "ipadFrPortStatsTxStatInq": ipadFrPortStatsTxStatInq,
       "ipadFrPortStatsRxStatInq": ipadFrPortStatsRxStatInq,
       "ipadFrPortStatsTxStatResp": ipadFrPortStatsTxStatResp,
       "ipadFrPortStatsRxStatResp": ipadFrPortStatsRxStatResp,
       "ipadFrPortStatsRxInvLMI": ipadFrPortStatsRxInvLMI,
       "ipadFrPortStatsPeak": ipadFrPortStatsPeak,
       "ipadFrPortStatsAverage": ipadFrPortStatsAverage,
       "ipadFrPortStatsTimeStamp": ipadFrPortStatsTimeStamp,
       "ipadFrPortStatsTxAvgPercent": ipadFrPortStatsTxAvgPercent,
       "ipadFrPortStatsTxMaxPercent": ipadFrPortStatsTxMaxPercent,
       "ipadFrPortStatsTxInstantPercent": ipadFrPortStatsTxInstantPercent,
       "ipadFrPortStatsTx20PercentSec": ipadFrPortStatsTx20PercentSec,
       "ipadFrPortStatsTx40PercentSec": ipadFrPortStatsTx40PercentSec,
       "ipadFrPortStatsTx60PercentSec": ipadFrPortStatsTx60PercentSec,
       "ipadFrPortStatsTx80PercentSec": ipadFrPortStatsTx80PercentSec,
       "ipadFrPortStatsTx100PercentSec": ipadFrPortStatsTx100PercentSec,
       "ipadFrPortStatsRxAvgPercent": ipadFrPortStatsRxAvgPercent,
       "ipadFrPortStatsRxMaxPercent": ipadFrPortStatsRxMaxPercent,
       "ipadFrPortStatsRxInstantPercent": ipadFrPortStatsRxInstantPercent,
       "ipadFrPortStatsRx20PercentSec": ipadFrPortStatsRx20PercentSec,
       "ipadFrPortStatsRx40PercentSec": ipadFrPortStatsRx40PercentSec,
       "ipadFrPortStatsRx60PercentSec": ipadFrPortStatsRx60PercentSec,
       "ipadFrPortStatsRx80PercentSec": ipadFrPortStatsRx80PercentSec,
       "ipadFrPortStatsRx100PercentSec": ipadFrPortStatsRx100PercentSec,
       "ipadFrPortStatsValidIntervals": ipadFrPortStatsValidIntervals,
       "ipadDLCIstatsTable": ipadDLCIstatsTable,
       "ipadDLCIstatsEntry": ipadDLCIstatsEntry,
       "ipadDLCIstatsService": ipadDLCIstatsService,
       "ipadDLCIstatsDLCI": ipadDLCIstatsDLCI,
       "ipadDLCIstatsPeriod": ipadDLCIstatsPeriod,
       "ipadDLCIstatsTxFrames": ipadDLCIstatsTxFrames,
       "ipadDLCIstatsRxFrames": ipadDLCIstatsRxFrames,
       "ipadDLCIstatsTxOctets": ipadDLCIstatsTxOctets,
       "ipadDLCIstatsRxOctets": ipadDLCIstatsRxOctets,
       "ipadDLCIstatsRxFECN": ipadDLCIstatsRxFECN,
       "ipadDLCIstatsRxBECN": ipadDLCIstatsRxBECN,
       "ipadDLCIstatsRxDE": ipadDLCIstatsRxDE,
       "ipadDLCIstatsTxExcessCIR": ipadDLCIstatsTxExcessCIR,
       "ipadDLCIstatsTxExcessBe": ipadDLCIstatsTxExcessBe,
       "ipadDLCIstatsTxMgmtFrames": ipadDLCIstatsTxMgmtFrames,
       "ipadDLCIstatsRxMgmtFrames": ipadDLCIstatsRxMgmtFrames,
       "ipadDLCIstatsTxMgmtOctets": ipadDLCIstatsTxMgmtOctets,
       "ipadDLCIstatsRxMgmtOctets": ipadDLCIstatsRxMgmtOctets,
       "ipadDLCIstatsPeak": ipadDLCIstatsPeak,
       "ipadDLCIstatsAverage": ipadDLCIstatsAverage,
       "ipadDLCIstatsDelayPeak": ipadDLCIstatsDelayPeak,
       "ipadDLCIstatsDelayAverage": ipadDLCIstatsDelayAverage,
       "ipadDLCIstatsRoundTripTimeouts": ipadDLCIstatsRoundTripTimeouts,
       "ipadDLCIstatsUAS": ipadDLCIstatsUAS,
       "ipadDLCIstatsFdrCir": ipadDLCIstatsFdrCir,
       "ipadDLCIstatsDdrCir": ipadDLCIstatsDdrCir,
       "ipadDLCIstatsFdrBe": ipadDLCIstatsFdrBe,
       "ipadDLCIstatsDdrBe": ipadDLCIstatsDdrBe,
       "ipadDLCIstatsTimeStamp": ipadDLCIstatsTimeStamp,
       "ipadDLCIstatsRemoteFramesOfferedWithinCIR": ipadDLCIstatsRemoteFramesOfferedWithinCIR,
       "ipadDLCIstatsRemoteFramesOfferedWithinBE": ipadDLCIstatsRemoteFramesOfferedWithinBE,
       "ipadDLCIstatsFramesReceived": ipadDLCIstatsFramesReceived,
       "ipadDLCIstatsFDRCIR": ipadDLCIstatsFDRCIR,
       "ipadDLCIstatsFDRBE": ipadDLCIstatsFDRBE,
       "ipadDLCIstatsRemoteDataOfferedWithinCIR": ipadDLCIstatsRemoteDataOfferedWithinCIR,
       "ipadDLCIstatsRemoteDataOfferedWithinBE": ipadDLCIstatsRemoteDataOfferedWithinBE,
       "ipadDLCIstatsDataReceived": ipadDLCIstatsDataReceived,
       "ipadDLCIstatsDDRCIR": ipadDLCIstatsDDRCIR,
       "ipadDLCIstatsDDRBE": ipadDLCIstatsDDRBE,
       "ipadDLCIstatsAvgPercent": ipadDLCIstatsAvgPercent,
       "ipadDLCIstatsMaxPercent": ipadDLCIstatsMaxPercent,
       "ipadDLCIstatsInstantPercent": ipadDLCIstatsInstantPercent,
       "ipadDLCIstats20PercentSec": ipadDLCIstats20PercentSec,
       "ipadDLCIstats40PercentSec": ipadDLCIstats40PercentSec,
       "ipadDLCIstats60PercentSec": ipadDLCIstats60PercentSec,
       "ipadDLCIstats80PercentSec": ipadDLCIstats80PercentSec,
       "ipadDLCIstats100PercentSec": ipadDLCIstats100PercentSec,
       "ipadDLCIstatsValidIntervals": ipadDLCIstatsValidIntervals,
       "ipadDLCIstatsCompressionTxOctetsIn": ipadDLCIstatsCompressionTxOctetsIn,
       "ipadDLCIstatsCompressionTxOctetsOut": ipadDLCIstatsCompressionTxOctetsOut,
       "ipadDLCIstatsCompressionRxOctetsIn": ipadDLCIstatsCompressionRxOctetsIn,
       "ipadDLCIstatsCompressionRxOctetsOut": ipadDLCIstatsCompressionRxOctetsOut,
       "ipadDLCIstatsCompressionTxRatio": ipadDLCIstatsCompressionTxRatio,
       "ipadDLCIstatsCompressionRxRatio": ipadDLCIstatsCompressionRxRatio,
       "ipadUserStatsTable": ipadUserStatsTable,
       "ipadUserStatsEntry": ipadUserStatsEntry,
       "ipadUserStatsIndex": ipadUserStatsIndex,
       "ipadUserStatsPeriod": ipadUserStatsPeriod,
       "ipadUserStatsTxFrames": ipadUserStatsTxFrames,
       "ipadUserStatsRxFrames": ipadUserStatsRxFrames,
       "ipadUserStatsTxOctets": ipadUserStatsTxOctets,
       "ipadUserStatsRxOctets": ipadUserStatsRxOctets,
       "ipadUserStatsTxRatePeak": ipadUserStatsTxRatePeak,
       "ipadUserStatsTxRateAverage": ipadUserStatsTxRateAverage,
       "ipadUserStatsTimeStamp": ipadUserStatsTimeStamp,
       "ipadIPTopNStatsTable": ipadIPTopNStatsTable,
       "ipadIPTopNStatsEntry": ipadIPTopNStatsEntry,
       "ipadIPTopNStatsIndex": ipadIPTopNStatsIndex,
       "ipadIPTopNStatsAddress": ipadIPTopNStatsAddress,
       "ipadIPTopNStatsTimestamp": ipadIPTopNStatsTimestamp,
       "ipadIPTopNStatsRxFrames": ipadIPTopNStatsRxFrames,
       "ipadIPTopNStatsRxOctets": ipadIPTopNStatsRxOctets,
       "ipadIPTopNStatsTxFrames": ipadIPTopNStatsTxFrames,
       "ipadIPTopNStatsTxOctets": ipadIPTopNStatsTxOctets,
       "ipadPktSwitch": ipadPktSwitch,
       "ipadPktSwOperatingMode": ipadPktSwOperatingMode,
       "ipadPktSwCfgTable": ipadPktSwCfgTable,
       "ipadPktSwCfgTableEntry": ipadPktSwCfgTableEntry,
       "ipadPktSwCfgService": ipadPktSwCfgService,
       "ipadPktSwCfgInterfaceType": ipadPktSwCfgInterfaceType,
       "ipadPktSwCfgLnkMgmtType": ipadPktSwCfgLnkMgmtType,
       "ipadPktSwCfgMaxFrameSize": ipadPktSwCfgMaxFrameSize,
       "ipadPktSwCfgnN1": ipadPktSwCfgnN1,
       "ipadPktSwCfgnN2": ipadPktSwCfgnN2,
       "ipadPktSwCfgnN3": ipadPktSwCfgnN3,
       "ipadPktSwCfgnT1": ipadPktSwCfgnT1,
       "ipadPktSwCfgDefCIR": ipadPktSwCfgDefCIR,
       "ipadPktSwCfgDefExBurst": ipadPktSwCfgDefExBurst,
       "ipadPktSwCfgCIREE": ipadPktSwCfgCIREE,
       "ipadPktSwCfgLinkInjection": ipadPktSwCfgLinkInjection,
       "ipadPktSwCfgAutoDiagnostic": ipadPktSwCfgAutoDiagnostic,
       "ipadPktSwCfgAutoDiscovery": ipadPktSwCfgAutoDiscovery,
       "ipadPktSwCfgMgmtDLCI": ipadPktSwCfgMgmtDLCI,
       "ipadPktSwCfgRoundTripDelaySize": ipadPktSwCfgRoundTripDelaySize,
       "ipadPktSwCfgRoundTripDelayRate": ipadPktSwCfgRoundTripDelayRate,
       "ipadPktSwCfgAutoIPMgmtAddr": ipadPktSwCfgAutoIPMgmtAddr,
       "ipadPktSwCfgNormalTxQueueSize": ipadPktSwCfgNormalTxQueueSize,
       "ipadPktSwCfgAddDLCI": ipadPktSwCfgAddDLCI,
       "ipadPktSwCfgDeleteDLCI": ipadPktSwCfgDeleteDLCI,
       "ipadTrapDest": ipadTrapDest,
       "ipadTrapDestTable": ipadTrapDestTable,
       "ipadTrapDestTableEntry": ipadTrapDestTableEntry,
       "ipadTrapDestIndex": ipadTrapDestIndex,
       "ipadTrapDestination": ipadTrapDestination,
       "ipadMisc": ipadMisc,
       "ipadMiscPortSettings": ipadMiscPortSettings,
       "ipadMiscPortSettingsEntry": ipadMiscPortSettingsEntry,
       "ipadMiscPortSettingsIndex": ipadMiscPortSettingsIndex,
       "ipadMiscPortSettingsSerialType": ipadMiscPortSettingsSerialType,
       "ipadMiscPortSettingsModemControl": ipadMiscPortSettingsModemControl,
       "ipadMiscClearStatusCounts": ipadMiscClearStatusCounts,
       "ipadMiscEnableServiceAware": ipadMiscEnableServiceAware,
       "ipadMiscShdslConfigTable": ipadMiscShdslConfigTable,
       "ipadMiscShdslConfigEntry": ipadMiscShdslConfigEntry,
       "ipadMiscShdslConfigIndex": ipadMiscShdslConfigIndex,
       "ipadMiscShdslTerminalType": ipadMiscShdslTerminalType,
       "ipadMiscShdslTiming": ipadMiscShdslTiming,
       "ipadMiscShdslStationInTiming": ipadMiscShdslStationInTiming,
       "ipadMiscShdslStationTimingNxMultiple": ipadMiscShdslStationTimingNxMultiple,
       "ipadMiscShdslAutomaticRetrain": ipadMiscShdslAutomaticRetrain,
       "ipadMiscShdslStatusTable": ipadMiscShdslStatusTable,
       "ipadMiscShdslStatusEntry": ipadMiscShdslStatusEntry,
       "ipadMiscShdslStatusIndex": ipadMiscShdslStatusIndex,
       "ipadMiscShdslConnectionStatus": ipadMiscShdslConnectionStatus,
       "ipadMiscShdslDetailedConnectionStatus": ipadMiscShdslDetailedConnectionStatus,
       "ipadMiscShdslEOCInMessages": ipadMiscShdslEOCInMessages,
       "ipadMiscShdslEOCOutMessages": ipadMiscShdslEOCOutMessages,
       "ipadMiscShdslConnectionStatusPair2": ipadMiscShdslConnectionStatusPair2,
       "ipadMiscShdslDetailedConnectionStatusPair2": ipadMiscShdslDetailedConnectionStatusPair2,
       "ipadMiscEnableSupervisoryPort": ipadMiscEnableSupervisoryPort,
       "ipadMiscEnableButtons": ipadMiscEnableButtons,
       "ipadMiscBootupConsoleAvail": ipadMiscBootupConsoleAvail,
       "ipadMiscEnableLEDs": ipadMiscEnableLEDs,
       "ipadMiscDisableLAN": ipadMiscDisableLAN,
       "ipadMiscLANStatus": ipadMiscLANStatus,
       "ipadRouter": ipadRouter,
       "ipadSoftKey": ipadSoftKey,
       "ipadSoftKeyTable": ipadSoftKeyTable,
       "ipadSoftKeyTableEntry": ipadSoftKeyTableEntry,
       "ipadSoftKeyIndex": ipadSoftKeyIndex,
       "ipadSoftKeyAcronym": ipadSoftKeyAcronym,
       "ipadSoftKeyDescription": ipadSoftKeyDescription,
       "ipadSoftKeyExpirationDate": ipadSoftKeyExpirationDate,
       "ipadSoftKeyEntry": ipadSoftKeyEntry,
       "ipadTCPServer": ipadTCPServer,
       "ipadTCPServerEnable": ipadTCPServerEnable,
       "ipadTCPServerConnTable": ipadTCPServerConnTable,
       "ipadTCPServerConnTableEntry": ipadTCPServerConnTableEntry,
       "ipadTCPServerConnIndex": ipadTCPServerConnIndex,
       "ipadTCPServerConnEndpoint": ipadTCPServerConnEndpoint,
       "ipadTCPServerConnLocalPort": ipadTCPServerConnLocalPort,
       "ipadTCPServerConnEnableEntry": ipadTCPServerConnEnableEntry,
       "ipadTCPServerAddConnEntry": ipadTCPServerAddConnEntry,
       "ipadTCPServerDeleteConnEntry": ipadTCPServerDeleteConnEntry,
       "ipadTCPServerHostAccessTable": ipadTCPServerHostAccessTable,
       "ipadTCPServerHostAccessTableEntry": ipadTCPServerHostAccessTableEntry,
       "ipadTCPServerHostAccessIndex": ipadTCPServerHostAccessIndex,
       "ipadTCPServerHostAccessIPAddr": ipadTCPServerHostAccessIPAddr,
       "ipadSCADAConfig": ipadSCADAConfig,
       "ipadSCADAConfigTable": ipadSCADAConfigTable,
       "ipadSCADAConfigTableEntry": ipadSCADAConfigTableEntry,
       "ipadSCADACfgIndex": ipadSCADACfgIndex,
       "ipadSCADACfgMessageSize": ipadSCADACfgMessageSize,
       "ipadSCADACfgIdleCharDelay": ipadSCADACfgIdleCharDelay,
       "ipadSCADACfgInputTerminator": ipadSCADACfgInputTerminator,
       "ipadSCADACfgAddDevLst": ipadSCADACfgAddDevLst,
       "ipadSCADACfgDeleteDevLst": ipadSCADACfgDeleteDevLst,
       "ipadSCADACfgDataDirection": ipadSCADACfgDataDirection,
       "ipadSCADACfgProtocol": ipadSCADACfgProtocol,
       "ipadSCADACfgLoopback": ipadSCADACfgLoopback,
       "ipadSCADAStats": ipadSCADAStats,
       "ipadSCADAStatsTable": ipadSCADAStatsTable,
       "ipadSCADAStatsTableEntry": ipadSCADAStatsTableEntry,
       "ipadSCADAStatsIndex": ipadSCADAStatsIndex,
       "ipadSCADAStatsTxChars": ipadSCADAStatsTxChars,
       "ipadSCADAStatsRxChars": ipadSCADAStatsRxChars,
       "ipadSCADAStatsTxMsgs": ipadSCADAStatsTxMsgs,
       "ipadSCADAStatsRxMsgs": ipadSCADAStatsRxMsgs,
       "ipadSCADAStatsRxParityErrors": ipadSCADAStatsRxParityErrors,
       "ipadSCADAStatsRxFramingErrors": ipadSCADAStatsRxFramingErrors,
       "ipadSCADAStatsClear": ipadSCADAStatsClear,
       "ipadSCADADevLst": ipadSCADADevLst,
       "ipadSCADADevLstTable": ipadSCADADevLstTable,
       "ipadSCADADevLstTableEntry": ipadSCADADevLstTableEntry,
       "ipadSCADADevLstIndex": ipadSCADADevLstIndex,
       "ipadSCADADevLstDevIndex": ipadSCADADevLstDevIndex,
       "ipadSCADADevLstEndpointName": ipadSCADADevLstEndpointName,
       "ipadSCADADevLstEntryStatus": ipadSCADADevLstEntryStatus,
       "ipadDS0Config": ipadDS0Config,
       "ipadDS0ConfigTable": ipadDS0ConfigTable,
       "ipadDS0ConfigTableEntry": ipadDS0ConfigTableEntry,
       "ipadDS0ConfigIndex": ipadDS0ConfigIndex,
       "ipadDS0ConfigNumberDS0": ipadDS0ConfigNumberDS0,
       "ipadDS0ConfigResetTimer": ipadDS0ConfigResetTimer,
       "ipadDS0ConfigHighUtil": ipadDS0ConfigHighUtil,
       "ipadDS0ConfigHighUtilThreshold": ipadDS0ConfigHighUtilThreshold,
       "ipadDS0ConfigHighUtilStatus": ipadDS0ConfigHighUtilStatus,
       "ipadDS0ConfigHighUtilCount": ipadDS0ConfigHighUtilCount,
       "ipadDS0ConfigHighUtilAlarm": ipadDS0ConfigHighUtilAlarm,
       "ipadDS0ConfigLowUtil": ipadDS0ConfigLowUtil,
       "ipadDS0ConfigLowUtilAlarm": ipadDS0ConfigLowUtilAlarm,
       "ipadDS0ConfigReset": ipadDS0ConfigReset,
       "ipadDS0Hist24": ipadDS0Hist24,
       "ipadDS0Hist24Table": ipadDS0Hist24Table,
       "ipadDS0Hist24TableEntry": ipadDS0Hist24TableEntry,
       "ipadDS0Hist24Index": ipadDS0Hist24Index,
       "ipadDS0Hist24HistoricalIndex": ipadDS0Hist24HistoricalIndex,
       "ipadDS0Hist24Timestamp": ipadDS0Hist24Timestamp,
       "ipadDS0Hist24HighUtilSeconds": ipadDS0Hist24HighUtilSeconds,
       "ipadDS0Hist24Utilization": ipadDS0Hist24Utilization,
       "ipadDS0Hist30": ipadDS0Hist30,
       "ipadDS0Hist30Table": ipadDS0Hist30Table,
       "ipadDS0Hist30TableEntry": ipadDS0Hist30TableEntry,
       "ipadDS0Hist30Index": ipadDS0Hist30Index,
       "ipadDS0Hist30HistoricalIndex": ipadDS0Hist30HistoricalIndex,
       "ipadDS0Hist30Timestamp": ipadDS0Hist30Timestamp,
       "ipadDS0Hist30HighUtilSeconds": ipadDS0Hist30HighUtilSeconds,
       "ipadDS0Hist30Utilization": ipadDS0Hist30Utilization,
       "ipadHDLCConfig": ipadHDLCConfig,
       "ipadHDLCConfigTable": ipadHDLCConfigTable,
       "ipadHDLCConfigTableEntry": ipadHDLCConfigTableEntry,
       "ipadHDLCConfigIndex": ipadHDLCConfigIndex,
       "ipadHDLCConfigService": ipadHDLCConfigService,
       "ipadHDLCConfigServiceBPS": ipadHDLCConfigServiceBPS,
       "ipadHDLCConfigResetTimer": ipadHDLCConfigResetTimer,
       "ipadHDLCConfigRxHighUtil": ipadHDLCConfigRxHighUtil,
       "ipadHDLCConfigRxHighUtilThreshold": ipadHDLCConfigRxHighUtilThreshold,
       "ipadHDLCConfigRxHighUtilStatus": ipadHDLCConfigRxHighUtilStatus,
       "ipadHDLCConfigRxHighUtilCount": ipadHDLCConfigRxHighUtilCount,
       "ipadHDLCConfigRxHighUtilAlarm": ipadHDLCConfigRxHighUtilAlarm,
       "ipadHDLCConfigRxLowUtil": ipadHDLCConfigRxLowUtil,
       "ipadHDLCConfigRxLowUtilAlarm": ipadHDLCConfigRxLowUtilAlarm,
       "ipadHDLCConfigTxHighUtil": ipadHDLCConfigTxHighUtil,
       "ipadHDLCConfigTxHighUtilThreshold": ipadHDLCConfigTxHighUtilThreshold,
       "ipadHDLCConfigTxHighUtilStatus": ipadHDLCConfigTxHighUtilStatus,
       "ipadHDLCConfigTxHighUtilCount": ipadHDLCConfigTxHighUtilCount,
       "ipadHDLCConfigTxHighUtilAlarm": ipadHDLCConfigTxHighUtilAlarm,
       "ipadHDLCConfigTxLowUtil": ipadHDLCConfigTxLowUtil,
       "ipadHDLCConfigTxLowUtilAlarm": ipadHDLCConfigTxLowUtilAlarm,
       "ipadHDLCConfigReset": ipadHDLCConfigReset,
       "ipadHDLCHist24": ipadHDLCHist24,
       "ipadHDLCHist24Table": ipadHDLCHist24Table,
       "ipadHDLCHist24TableEntry": ipadHDLCHist24TableEntry,
       "ipadHDLCHist24Index": ipadHDLCHist24Index,
       "ipadHDLCHist24HistoricalIndex": ipadHDLCHist24HistoricalIndex,
       "ipadHDLCHist24Timestamp": ipadHDLCHist24Timestamp,
       "ipadHDLCHist24RxHighUtilSeconds": ipadHDLCHist24RxHighUtilSeconds,
       "ipadHDLCHist24RxUtilization": ipadHDLCHist24RxUtilization,
       "ipadHDLCHist24TxHighUtilSeconds": ipadHDLCHist24TxHighUtilSeconds,
       "ipadHDLCHist24TxUtilization": ipadHDLCHist24TxUtilization,
       "ipadHDLCHist30": ipadHDLCHist30,
       "ipadHDLCHist30Table": ipadHDLCHist30Table,
       "ipadHDLCHist30TableEntry": ipadHDLCHist30TableEntry,
       "ipadHDLCHist30Index": ipadHDLCHist30Index,
       "ipadHDLCHist30HistoricalIndex": ipadHDLCHist30HistoricalIndex,
       "ipadHDLCHist30Timestamp": ipadHDLCHist30Timestamp,
       "ipadHDLCHist30RxHighUtilSeconds": ipadHDLCHist30RxHighUtilSeconds,
       "ipadHDLCHist30RxUtilization": ipadHDLCHist30RxUtilization,
       "ipadHDLCHist30TxHighUtilSeconds": ipadHDLCHist30TxHighUtilSeconds,
       "ipadHDLCHist30TxUtilization": ipadHDLCHist30TxUtilization,
       "ipadAtm": ipadAtm,
       "ipadNat": ipadNat,
       "ipadDhcp": ipadDhcp,
       "ipadBridge": ipadBridge,
       "ipadSmtp": ipadSmtp,
       "ipadSmtpMailServer": ipadSmtpMailServer,
       "ipadSmtpDomainName": ipadSmtpDomainName,
       "ipadSmtpMailFrom": ipadSmtpMailFrom,
       "ipadSmtpRecipient1": ipadSmtpRecipient1,
       "ipadSmtpRecipient2": ipadSmtpRecipient2,
       "ipadSmtpRecipient3": ipadSmtpRecipient3,
       "ipadSmtpRecipient4": ipadSmtpRecipient4,
       "ipadSmtpRecipient5": ipadSmtpRecipient5,
       "ipadEncryption": ipadEncryption,
       "ipadEncryptionEnable": ipadEncryptionEnable,
       "ipadEncryptionStartupKey": ipadEncryptionStartupKey,
       "ipadEncryptionStartupKeyConfirm": ipadEncryptionStartupKeyConfirm,
       "ipadEncryptionType": ipadEncryptionType,
       "ipadEncryptionKey1": ipadEncryptionKey1,
       "ipadEncryptionKey2": ipadEncryptionKey2,
       "ipadEncryptionKey3": ipadEncryptionKey3,
       "ipadEncryptionKey4": ipadEncryptionKey4,
       "ipadEncryptionKey5": ipadEncryptionKey5,
       "ipadEncryptionKey6": ipadEncryptionKey6,
       "ipadEncryptionKey7": ipadEncryptionKey7,
       "ipadEncryptionKey8": ipadEncryptionKey8,
       "ipadEncryptionKey9": ipadEncryptionKey9,
       "ipadEncryptionKey10": ipadEncryptionKey10,
       "ipadEncryptionKeyLife": ipadEncryptionKeyLife,
       "ipadAutoLearnDS0": ipadAutoLearnDS0,
       "ipadAutoLearnDS0Table": ipadAutoLearnDS0Table,
       "ipadAutoLearnDS0TableEntry": ipadAutoLearnDS0TableEntry,
       "ipadAutoLearnDS0Index": ipadAutoLearnDS0Index,
       "ipadAutoLearnDS0Boot": ipadAutoLearnDS0Boot,
       "ipadAutoLearnDS0Rate": ipadAutoLearnDS0Rate,
       "ipadAutoLearnDS0Command": ipadAutoLearnDS0Command,
       "ipadUnitAccess": ipadUnitAccess,
       "ipadUnitAccessTable": ipadUnitAccessTable,
       "ipadUnitAccessTableEntry": ipadUnitAccessTableEntry,
       "ipadUnitAccessIndex": ipadUnitAccessIndex,
       "ipadUnitAccessIpa": ipadUnitAccessIpa,
       "ipadUnitAccessMask": ipadUnitAccessMask,
       "ipadTFTPDownload": ipadTFTPDownload,
       "ipadTFTPDownloadServerIpa": ipadTFTPDownloadServerIpa,
       "ipadTFTPDownloadFileName": ipadTFTPDownloadFileName,
       "ipadTFTPDownloadAction": ipadTFTPDownloadAction,
       "ipadTFTPDownloadStatus": ipadTFTPDownloadStatus,
       "ipadDataLineMonitor": ipadDataLineMonitor,
       "ipadDLMConfig": ipadDLMConfig,
       "ipadDLMConfigMode": ipadDLMConfigMode,
       "ipadDLMConfigBufferManagement": ipadDLMConfigBufferManagement,
       "ipadDLMTable": ipadDLMTable,
       "ipadDLMTableEntry": ipadDLMTableEntry,
       "ipadDLMServiceIndex": ipadDLMServiceIndex,
       "ipadDLMEnable": ipadDLMEnable,
       "ipadDLMTxRxFilter": ipadDLMTxRxFilter,
       "ipadDLMPatternEnable": ipadDLMPatternEnable,
       "ipadDLMPattern": ipadDLMPattern,
       "ipadDLMPatternMask": ipadDLMPatternMask,
       "ipadDLMPatternOffset": ipadDLMPatternOffset,
       "ipadDLMPacketTable": ipadDLMPacketTable,
       "ipadDLMPacketTableEntry": ipadDLMPacketTableEntry,
       "ipadDLMPacketIndex": ipadDLMPacketIndex,
       "ipadDLMPacketServiceIndex": ipadDLMPacketServiceIndex,
       "ipadDLMPacketTimestamp": ipadDLMPacketTimestamp,
       "ipadDLMPacketDataDirection": ipadDLMPacketDataDirection,
       "ipadDLMPacketSize": ipadDLMPacketSize,
       "ipadDLMPacketData": ipadDLMPacketData,
       "ipadOrigPing": ipadOrigPing,
       "ipadOrigPingCommand": ipadOrigPingCommand,
       "ipadOrigPingDestIPAddr": ipadOrigPingDestIPAddr,
       "ipadOrigPingTimeout": ipadOrigPingTimeout,
       "ipadOrigPingSize": ipadOrigPingSize,
       "ipadOrigPingToSend": ipadOrigPingToSend,
       "ipadOrigPingSent": ipadOrigPingSent,
       "ipadOrigPingReplies": ipadOrigPingReplies,
       "ipadOrigPingDelayMin": ipadOrigPingDelayMin,
       "ipadOrigPingDelayAvg": ipadOrigPingDelayAvg,
       "ipadOrigPingDelayMax": ipadOrigPingDelayMax,
       "ipadOrigPingReport": ipadOrigPingReport,
       "ipadOrigPingExceptReport": ipadOrigPingExceptReport,
       "ipadTraps": ipadTraps,
       "ipadTrapsPrefix": ipadTrapsPrefix,
       "ipadFrPortRxInvalidFramesExceeded": ipadFrPortRxInvalidFramesExceeded,
       "ipadFrPortRxThroughputExceeded": ipadFrPortRxThroughputExceeded,
       "ipadFrPortTxThroughputExceeded": ipadFrPortTxThroughputExceeded,
       "ipadDLCItxCIRexceeded": ipadDLCItxCIRexceeded,
       "ipadDLCItxBEexceeded": ipadDLCItxBEexceeded,
       "ipadDLCIRxCongestionExceeded": ipadDLCIRxCongestionExceeded,
       "ipadUserTxExceeded": ipadUserTxExceeded,
       "ipadDlciRxBECNinCIRAlarm": ipadDlciRxBECNinCIRAlarm,
       "ipadDlciUASExceeded": ipadDlciUASExceeded,
       "ipadserialDteDTRAlarmExists": ipadserialDteDTRAlarmExists,
       "ipadt1e1ESAlarmDeclared": ipadt1e1ESAlarmDeclared,
       "ipadt1e1SESAlarmDeclared": ipadt1e1SESAlarmDeclared,
       "ipadt1e1LOSSAlarmDeclared": ipadt1e1LOSSAlarmDeclared,
       "ipadt1e1UASAlarmDeclared": ipadt1e1UASAlarmDeclared,
       "ipadt1e1CSSAlarmDeclared": ipadt1e1CSSAlarmDeclared,
       "ipadt1e1BPVSAlarmDeclared": ipadt1e1BPVSAlarmDeclared,
       "ipadt1e1OOFSAlarmDeclared": ipadt1e1OOFSAlarmDeclared,
       "ipadt1e1AISAlarmExists": ipadt1e1AISAlarmExists,
       "ipadt1e1RASAlarmExists": ipadt1e1RASAlarmExists,
       "ipadDLCIremoteSOSAlarm": ipadDLCIremoteSOSAlarm,
       "ipadDdsLOSSAlarmDeclared": ipadDdsLOSSAlarmDeclared,
       "ipadDdsOOFSAlarmDeclared": ipadDdsOOFSAlarmDeclared,
       "ipadDdsOOSSAlarmDeclared": ipadDdsOOSSAlarmDeclared,
       "ipadDdsFDLSAlarmDeclared": ipadDdsFDLSAlarmDeclared,
       "ipadDdsBPVSAlarmDeclared": ipadDdsBPVSAlarmDeclared,
       "ipadDS0HighAlarmDeclared": ipadDS0HighAlarmDeclared,
       "ipadDS0LowAlarmDeclared": ipadDS0LowAlarmDeclared,
       "ipadHDLCRxHighAlarmDeclared": ipadHDLCRxHighAlarmDeclared,
       "ipadHDLCRxLowAlarmDeclared": ipadHDLCRxLowAlarmDeclared,
       "ipadHDLCTxHighAlarmDeclared": ipadHDLCTxHighAlarmDeclared,
       "ipadHDLCTxLowAlarmDeclared": ipadHDLCTxLowAlarmDeclared,
       "ipadDbuActivated": ipadDbuActivated}
)
