# SNMP MIB module (IPAD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IPAD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:10:42 2024
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

_Verilink_ObjectIdentity = ObjectIdentity
verilink = _Verilink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 321)
)
_Hbu_ObjectIdentity = ObjectIdentity
hbu = _Hbu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 321, 100)
)
_Ipad_ObjectIdentity = ObjectIdentity
ipad = _Ipad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 321, 100, 1)
)
_IpadFrPort_ObjectIdentity = ObjectIdentity
ipadFrPort = _IpadFrPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 1)
)
_IpadFrPortTable_Object = MibTable
ipadFrPortTable = _IpadFrPortTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ipadFrPortTable.setStatus("optional")
_IpadFrPortTableEntry_Object = MibTableRow
ipadFrPortTableEntry = _IpadFrPortTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 1, 1, 1)
)
ipadFrPortTableEntry.setIndexNames(
    (0, "IPAD-MIB", "ipadFrPortService"),
)
if mibBuilder.loadTexts:
    ipadFrPortTableEntry.setStatus("mandatory")
_IpadFrPortService_Type = Integer32
_IpadFrPortService_Object = MibTableColumn
ipadFrPortService = _IpadFrPortService_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 1, 1, 1, 1),
    _IpadFrPortService_Type()
)
ipadFrPortService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadFrPortService.setStatus("mandatory")


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
    ipadFrPortActive.setStatus("mandatory")


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
    ipadFrPortLMIType.setStatus("mandatory")


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
    ipadFrPortLMIMode.setStatus("mandatory")
_IpadFrPortRxInvAlmThreshold_Type = Integer32
_IpadFrPortRxInvAlmThreshold_Object = MibTableColumn
ipadFrPortRxInvAlmThreshold = _IpadFrPortRxInvAlmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 1, 1, 1, 5),
    _IpadFrPortRxInvAlmThreshold_Type()
)
ipadFrPortRxInvAlmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadFrPortRxInvAlmThreshold.setStatus("mandatory")


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
    ipadFrPortRxInvAlmAlarm.setStatus("mandatory")
_IpadFrPortTxAlmThreshold_Type = Integer32
_IpadFrPortTxAlmThreshold_Object = MibTableColumn
ipadFrPortTxAlmThreshold = _IpadFrPortTxAlmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 1, 1, 1, 7),
    _IpadFrPortTxAlmThreshold_Type()
)
ipadFrPortTxAlmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadFrPortTxAlmThreshold.setStatus("mandatory")


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
    ipadFrPortTxAlmAlarm.setStatus("mandatory")
_IpadFrPortRxAlmThreshold_Type = Integer32
_IpadFrPortRxAlmThreshold_Object = MibTableColumn
ipadFrPortRxAlmThreshold = _IpadFrPortRxAlmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 1, 1, 1, 9),
    _IpadFrPortRxAlmThreshold_Type()
)
ipadFrPortRxAlmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadFrPortRxAlmThreshold.setStatus("mandatory")


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
    ipadFrPortRxAlmAlarm.setStatus("mandatory")
_IpadService_ObjectIdentity = ObjectIdentity
ipadService = _IpadService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 2)
)
_IpadServiceTable_Object = MibTable
ipadServiceTable = _IpadServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ipadServiceTable.setStatus("optional")
_IpadServiceTableEntry_Object = MibTableRow
ipadServiceTableEntry = _IpadServiceTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 2, 1, 1)
)
ipadServiceTableEntry.setIndexNames(
    (0, "IPAD-MIB", "ipadServiceIndex"),
)
if mibBuilder.loadTexts:
    ipadServiceTableEntry.setStatus("mandatory")
_IpadServiceIndex_Type = Integer32
_IpadServiceIndex_Object = MibTableColumn
ipadServiceIndex = _IpadServiceIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 2, 1, 1, 1),
    _IpadServiceIndex_Type()
)
ipadServiceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadServiceIndex.setStatus("mandatory")


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
              6)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("ethernet", 6),
          ("network1", 2),
          ("network2", 3),
          ("supervisor", 1),
          ("user1", 4),
          ("user2", 5))
    )


_IpadServiceifIndex_Type.__name__ = "Integer32"
_IpadServiceifIndex_Object = MibTableColumn
ipadServiceifIndex = _IpadServiceifIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 2, 1, 1, 2),
    _IpadServiceifIndex_Type()
)
ipadServiceifIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadServiceifIndex.setStatus("mandatory")


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
              9)
        )
    )
    namedValues = NamedValues(
        *(("frameRelay", 5),
          ("frameRelayMonitor", 6),
          ("ip", 7),
          ("other", 1),
          ("ppp", 3),
          ("pppMonitor", 4),
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
    ipadServiceType.setStatus("mandatory")
_IpadServicePair_Type = Integer32
_IpadServicePair_Object = MibTableColumn
ipadServicePair = _IpadServicePair_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 2, 1, 1, 4),
    _IpadServicePair_Type()
)
ipadServicePair.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadServicePair.setStatus("mandatory")


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
    ipadServiceAddService.setStatus("mandatory")
_IpadServiceDeleteService_Type = Integer32
_IpadServiceDeleteService_Object = MibScalar
ipadServiceDeleteService = _IpadServiceDeleteService_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 2, 3),
    _IpadServiceDeleteService_Type()
)
ipadServiceDeleteService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadServiceDeleteService.setStatus("mandatory")
_IpadChannel_ObjectIdentity = ObjectIdentity
ipadChannel = _IpadChannel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 3)
)
_IpadChannelTable_Object = MibTable
ipadChannelTable = _IpadChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 3, 1)
)
if mibBuilder.loadTexts:
    ipadChannelTable.setStatus("optional")
_IpadChannelTableEntry_Object = MibTableRow
ipadChannelTableEntry = _IpadChannelTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 3, 1, 1)
)
ipadChannelTableEntry.setIndexNames(
    (0, "IPAD-MIB", "ipadChannelifIndex"),
    (0, "IPAD-MIB", "ipadChannelIndex"),
)
if mibBuilder.loadTexts:
    ipadChannelTableEntry.setStatus("mandatory")


class _IpadChannelifIndex_Type(Integer32):
    """Custom type ipadChannelifIndex based on Integer32"""
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
        *(("ethernet", 6),
          ("network1", 2),
          ("network2", 3),
          ("supervisor", 1),
          ("user1", 4),
          ("user2", 5))
    )


_IpadChannelifIndex_Type.__name__ = "Integer32"
_IpadChannelifIndex_Object = MibTableColumn
ipadChannelifIndex = _IpadChannelifIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 3, 1, 1, 1),
    _IpadChannelifIndex_Type()
)
ipadChannelifIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadChannelifIndex.setStatus("mandatory")
_IpadChannelIndex_Type = Integer32
_IpadChannelIndex_Object = MibTableColumn
ipadChannelIndex = _IpadChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 3, 1, 1, 2),
    _IpadChannelIndex_Type()
)
ipadChannelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadChannelIndex.setStatus("mandatory")
_IpadChannelService_Type = Integer32
_IpadChannelService_Object = MibTableColumn
ipadChannelService = _IpadChannelService_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 3, 1, 1, 3),
    _IpadChannelService_Type()
)
ipadChannelService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadChannelService.setStatus("mandatory")
_IpadChannelPair_Type = Integer32
_IpadChannelPair_Object = MibTableColumn
ipadChannelPair = _IpadChannelPair_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 3, 1, 1, 4),
    _IpadChannelPair_Type()
)
ipadChannelPair.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadChannelPair.setStatus("mandatory")


class _IpadChannelRate_Type(Integer32):
    """Custom type ipadChannelRate based on Integer32"""
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
          ("rate56", 2),
          ("rate64", 3))
    )


_IpadChannelRate_Type.__name__ = "Integer32"
_IpadChannelRate_Object = MibTableColumn
ipadChannelRate = _IpadChannelRate_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 3, 1, 1, 5),
    _IpadChannelRate_Type()
)
ipadChannelRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadChannelRate.setStatus("mandatory")
_IpadDLCI_ObjectIdentity = ObjectIdentity
ipadDLCI = _IpadDLCI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 4)
)
_IpadDLCITable_Object = MibTable
ipadDLCITable = _IpadDLCITable_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 4, 1)
)
if mibBuilder.loadTexts:
    ipadDLCITable.setStatus("optional")
_IpadDLCITableEntry_Object = MibTableRow
ipadDLCITableEntry = _IpadDLCITableEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 4, 1, 1)
)
ipadDLCITableEntry.setIndexNames(
    (0, "IPAD-MIB", "ipadDLCIservice"),
    (0, "IPAD-MIB", "ipadDLCInumber"),
)
if mibBuilder.loadTexts:
    ipadDLCITableEntry.setStatus("mandatory")
_IpadDLCIservice_Type = Integer32
_IpadDLCIservice_Object = MibTableColumn
ipadDLCIservice = _IpadDLCIservice_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 4, 1, 1, 1),
    _IpadDLCIservice_Type()
)
ipadDLCIservice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDLCIservice.setStatus("mandatory")
_IpadDLCInumber_Type = Integer32
_IpadDLCInumber_Object = MibTableColumn
ipadDLCInumber = _IpadDLCInumber_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 4, 1, 1, 2),
    _IpadDLCInumber_Type()
)
ipadDLCInumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDLCInumber.setStatus("mandatory")


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
    ipadDLCIactive.setStatus("mandatory")


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
    ipadDLCIcongestion.setStatus("mandatory")
_IpadDLCIremote_Type = Integer32
_IpadDLCIremote_Object = MibTableColumn
ipadDLCIremote = _IpadDLCIremote_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 4, 1, 1, 5),
    _IpadDLCIremote_Type()
)
ipadDLCIremote.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDLCIremote.setStatus("mandatory")


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
    ipadDLCIremoteUnit.setStatus("mandatory")


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
    ipadDLCIremoteEquipActive.setStatus("mandatory")


class _IpadDLCIencapsulation_Type(Integer32):
    """Custom type ipadDLCIencapsulation based on Integer32"""
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
          ("proprietary", 3),
          ("rfc1490", 2))
    )


_IpadDLCIencapsulation_Type.__name__ = "Integer32"
_IpadDLCIencapsulation_Object = MibTableColumn
ipadDLCIencapsulation = _IpadDLCIencapsulation_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 4, 1, 1, 8),
    _IpadDLCIencapsulation_Type()
)
ipadDLCIencapsulation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadDLCIencapsulation.setStatus("mandatory")


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
    ipadDLCIproprietary.setStatus("mandatory")
_IpadDLCIpropOffset_Type = Integer32
_IpadDLCIpropOffset_Object = MibTableColumn
ipadDLCIpropOffset = _IpadDLCIpropOffset_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 4, 1, 1, 10),
    _IpadDLCIpropOffset_Type()
)
ipadDLCIpropOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadDLCIpropOffset.setStatus("mandatory")


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
    ipadDLCIinBand.setStatus("mandatory")
_IpadDLCICIR_Type = Integer32
_IpadDLCICIR_Object = MibTableColumn
ipadDLCICIR = _IpadDLCICIR_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 4, 1, 1, 12),
    _IpadDLCICIR_Type()
)
ipadDLCICIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadDLCICIR.setStatus("mandatory")
_IpadDLCIBe_Type = Integer32
_IpadDLCIBe_Object = MibTableColumn
ipadDLCIBe = _IpadDLCIBe_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 4, 1, 1, 13),
    _IpadDLCIBe_Type()
)
ipadDLCIBe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadDLCIBe.setStatus("mandatory")
_IpadDLCIminBC_Type = Integer32
_IpadDLCIminBC_Object = MibTableColumn
ipadDLCIminBC = _IpadDLCIminBC_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 4, 1, 1, 14),
    _IpadDLCIminBC_Type()
)
ipadDLCIminBC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadDLCIminBC.setStatus("mandatory")


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
    ipadDLCIrxMon.setStatus("mandatory")


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
    ipadDLCIdEctrl.setStatus("mandatory")


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
    ipadDLCIenableDelay.setStatus("mandatory")
_IpadDLCItxExCIRThreshold_Type = Integer32
_IpadDLCItxExCIRThreshold_Object = MibTableColumn
ipadDLCItxExCIRThreshold = _IpadDLCItxExCIRThreshold_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 4, 1, 1, 18),
    _IpadDLCItxExCIRThreshold_Type()
)
ipadDLCItxExCIRThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadDLCItxExCIRThreshold.setStatus("mandatory")


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
    ipadDLCItxExCIRAlarm.setStatus("mandatory")
_IpadDLCItxExBeThreshold_Type = Integer32
_IpadDLCItxExBeThreshold_Object = MibTableColumn
ipadDLCItxExBeThreshold = _IpadDLCItxExBeThreshold_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 4, 1, 1, 20),
    _IpadDLCItxExBeThreshold_Type()
)
ipadDLCItxExBeThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadDLCItxExBeThreshold.setStatus("mandatory")


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
    ipadDLCItxExBeAlarm.setStatus("mandatory")
_IpadDLCIrxCongThreshold_Type = Integer32
_IpadDLCIrxCongThreshold_Object = MibTableColumn
ipadDLCIrxCongThreshold = _IpadDLCIrxCongThreshold_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 4, 1, 1, 22),
    _IpadDLCIrxCongThreshold_Type()
)
ipadDLCIrxCongThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadDLCIrxCongThreshold.setStatus("mandatory")


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
    ipadDLCIrxCongAlarm.setStatus("mandatory")


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
    ipadDLCIrxBECNinCIR.setStatus("mandatory")
_IpadDLCIUASThreshold_Type = Integer32
_IpadDLCIUASThreshold_Object = MibTableColumn
ipadDLCIUASThreshold = _IpadDLCIUASThreshold_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 4, 1, 1, 25),
    _IpadDLCIUASThreshold_Type()
)
ipadDLCIUASThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadDLCIUASThreshold.setStatus("mandatory")


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
    ipadDLCIUASAlarm.setStatus("mandatory")
_IpadDLCILastChange_Type = TimeTicks
_IpadDLCILastChange_Object = MibScalar
ipadDLCILastChange = _IpadDLCILastChange_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 4, 2),
    _IpadDLCILastChange_Type()
)
ipadDLCILastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDLCILastChange.setStatus("mandatory")
_IpadEndpoint_ObjectIdentity = ObjectIdentity
ipadEndpoint = _IpadEndpoint_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 5)
)
_IpadEndpointTable_Object = MibTable
ipadEndpointTable = _IpadEndpointTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 5, 1)
)
if mibBuilder.loadTexts:
    ipadEndpointTable.setStatus("optional")
_IpadEndpointTableEntry_Object = MibTableRow
ipadEndpointTableEntry = _IpadEndpointTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 5, 1, 1)
)
ipadEndpointTableEntry.setIndexNames(
    (0, "IPAD-MIB", "ipadEndpointIndex"),
)
if mibBuilder.loadTexts:
    ipadEndpointTableEntry.setStatus("mandatory")
_IpadEndpointIndex_Type = Integer32
_IpadEndpointIndex_Object = MibTableColumn
ipadEndpointIndex = _IpadEndpointIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 5, 1, 1, 1),
    _IpadEndpointIndex_Type()
)
ipadEndpointIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadEndpointIndex.setStatus("mandatory")


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
    ipadEndpointName.setStatus("mandatory")
_IpadEndpointService_Type = Integer32
_IpadEndpointService_Object = MibTableColumn
ipadEndpointService = _IpadEndpointService_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 5, 1, 1, 3),
    _IpadEndpointService_Type()
)
ipadEndpointService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadEndpointService.setStatus("mandatory")
_IpadEndpointDLCInumber_Type = Integer32
_IpadEndpointDLCInumber_Object = MibTableColumn
ipadEndpointDLCInumber = _IpadEndpointDLCInumber_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 5, 1, 1, 4),
    _IpadEndpointDLCInumber_Type()
)
ipadEndpointDLCInumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadEndpointDLCInumber.setStatus("mandatory")


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
        *(("ipRoute", 4),
          ("local", 2),
          ("other", 1),
          ("switched", 3))
    )


_IpadEndpointType_Type.__name__ = "Integer32"
_IpadEndpointType_Object = MibTableColumn
ipadEndpointType = _IpadEndpointType_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 5, 1, 1, 5),
    _IpadEndpointType_Type()
)
ipadEndpointType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadEndpointType.setStatus("mandatory")
_IpadEndpointForward_Type = Integer32
_IpadEndpointForward_Object = MibTableColumn
ipadEndpointForward = _IpadEndpointForward_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 5, 1, 1, 6),
    _IpadEndpointForward_Type()
)
ipadEndpointForward.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadEndpointForward.setStatus("mandatory")
_IpadEndpointBackup_Type = Integer32
_IpadEndpointBackup_Object = MibTableColumn
ipadEndpointBackup = _IpadEndpointBackup_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 5, 1, 1, 7),
    _IpadEndpointBackup_Type()
)
ipadEndpointBackup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadEndpointBackup.setStatus("mandatory")
_IpadEndpointRefSLP_Type = Integer32
_IpadEndpointRefSLP_Object = MibTableColumn
ipadEndpointRefSLP = _IpadEndpointRefSLP_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 5, 1, 1, 8),
    _IpadEndpointRefSLP_Type()
)
ipadEndpointRefSLP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadEndpointRefSLP.setStatus("mandatory")
_IpadEndpointRemoteIpAddr_Type = IpAddress
_IpadEndpointRemoteIpAddr_Object = MibTableColumn
ipadEndpointRemoteIpAddr = _IpadEndpointRemoteIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 5, 1, 1, 9),
    _IpadEndpointRemoteIpAddr_Type()
)
ipadEndpointRemoteIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadEndpointRemoteIpAddr.setStatus("mandatory")
_IpadEndpointRemoteIpMask_Type = IpAddress
_IpadEndpointRemoteIpMask_Object = MibTableColumn
ipadEndpointRemoteIpMask = _IpadEndpointRemoteIpMask_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 5, 1, 1, 10),
    _IpadEndpointRemoteIpMask_Type()
)
ipadEndpointRemoteIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadEndpointRemoteIpMask.setStatus("mandatory")


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
    ipadEndpointAddEndpoint.setStatus("mandatory")


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
    ipadEndpointDeleteEndpoint.setStatus("mandatory")
_IpadEndpointLastChange_Type = TimeTicks
_IpadEndpointLastChange_Object = MibScalar
ipadEndpointLastChange = _IpadEndpointLastChange_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 5, 4),
    _IpadEndpointLastChange_Type()
)
ipadEndpointLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadEndpointLastChange.setStatus("mandatory")
_IpadUser_ObjectIdentity = ObjectIdentity
ipadUser = _IpadUser_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 6)
)
_IpadUserTable_Object = MibTable
ipadUserTable = _IpadUserTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 6, 1)
)
if mibBuilder.loadTexts:
    ipadUserTable.setStatus("optional")
_IpadUserTableEntry_Object = MibTableRow
ipadUserTableEntry = _IpadUserTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 6, 1, 1)
)
ipadUserTableEntry.setIndexNames(
    (0, "IPAD-MIB", "ipadUserIndex"),
)
if mibBuilder.loadTexts:
    ipadUserTableEntry.setStatus("mandatory")
_IpadUserIndex_Type = Integer32
_IpadUserIndex_Object = MibTableColumn
ipadUserIndex = _IpadUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 6, 1, 1, 1),
    _IpadUserIndex_Type()
)
ipadUserIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadUserIndex.setStatus("mandatory")


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
    ipadUserFilterByDLCI.setStatus("mandatory")
_IpadUserService_Type = Integer32
_IpadUserService_Object = MibTableColumn
ipadUserService = _IpadUserService_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 6, 1, 1, 3),
    _IpadUserService_Type()
)
ipadUserService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadUserService.setStatus("mandatory")
_IpadUserDLCI_Type = Integer32
_IpadUserDLCI_Object = MibTableColumn
ipadUserDLCI = _IpadUserDLCI_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 6, 1, 1, 4),
    _IpadUserDLCI_Type()
)
ipadUserDLCI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadUserDLCI.setStatus("mandatory")


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
    ipadUserFilterByIPAddress.setStatus("mandatory")
_IpadUserIPAddress_Type = IpAddress
_IpadUserIPAddress_Object = MibTableColumn
ipadUserIPAddress = _IpadUserIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 6, 1, 1, 6),
    _IpadUserIPAddress_Type()
)
ipadUserIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadUserIPAddress.setStatus("mandatory")
_IpadUserIPMask_Type = IpAddress
_IpadUserIPMask_Object = MibTableColumn
ipadUserIPMask = _IpadUserIPMask_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 6, 1, 1, 7),
    _IpadUserIPMask_Type()
)
ipadUserIPMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadUserIPMask.setStatus("mandatory")


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
    ipadUserFilterByIPPort.setStatus("mandatory")


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
    ipadUserIPPort.setStatus("mandatory")
_IpadUserTxAlmThreshold_Type = Integer32
_IpadUserTxAlmThreshold_Object = MibTableColumn
ipadUserTxAlmThreshold = _IpadUserTxAlmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 6, 1, 1, 10),
    _IpadUserTxAlmThreshold_Type()
)
ipadUserTxAlmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadUserTxAlmThreshold.setStatus("mandatory")


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
    ipadUserTxAlmAlarm.setStatus("mandatory")
_IpadUserIPStatTimeRemaining_Type = Integer32
_IpadUserIPStatTimeRemaining_Object = MibScalar
ipadUserIPStatTimeRemaining = _IpadUserIPStatTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 6, 2),
    _IpadUserIPStatTimeRemaining_Type()
)
ipadUserIPStatTimeRemaining.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadUserIPStatTimeRemaining.setStatus("mandatory")
_IpadUserIPStatTimeDuration_Type = Integer32
_IpadUserIPStatTimeDuration_Object = MibScalar
ipadUserIPStatTimeDuration = _IpadUserIPStatTimeDuration_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 6, 3),
    _IpadUserIPStatTimeDuration_Type()
)
ipadUserIPStatTimeDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadUserIPStatTimeDuration.setStatus("mandatory")
_IpadUserIPStatStartTime_Type = TimeTicks
_IpadUserIPStatStartTime_Object = MibScalar
ipadUserIPStatStartTime = _IpadUserIPStatStartTime_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 6, 4),
    _IpadUserIPStatStartTime_Type()
)
ipadUserIPStatStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadUserIPStatStartTime.setStatus("mandatory")
_IpadUserIPStatRequestedReportSize_Type = Integer32
_IpadUserIPStatRequestedReportSize_Object = MibScalar
ipadUserIPStatRequestedReportSize = _IpadUserIPStatRequestedReportSize_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 6, 5),
    _IpadUserIPStatRequestedReportSize_Type()
)
ipadUserIPStatRequestedReportSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadUserIPStatRequestedReportSize.setStatus("mandatory")
_IpadUserIPStatGrantedReportSize_Type = Integer32
_IpadUserIPStatGrantedReportSize_Object = MibScalar
ipadUserIPStatGrantedReportSize = _IpadUserIPStatGrantedReportSize_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 6, 6),
    _IpadUserIPStatGrantedReportSize_Type()
)
ipadUserIPStatGrantedReportSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadUserIPStatGrantedReportSize.setStatus("mandatory")
_IpadUserIPStatReportNumber_Type = Integer32
_IpadUserIPStatReportNumber_Object = MibScalar
ipadUserIPStatReportNumber = _IpadUserIPStatReportNumber_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 6, 7),
    _IpadUserIPStatReportNumber_Type()
)
ipadUserIPStatReportNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadUserIPStatReportNumber.setStatus("mandatory")


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
    ipadUserIPStatDiscardType.setStatus("mandatory")
_IpadPPP_ObjectIdentity = ObjectIdentity
ipadPPP = _IpadPPP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 7)
)
_IpadPPPCfgTable_Object = MibTable
ipadPPPCfgTable = _IpadPPPCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 1)
)
if mibBuilder.loadTexts:
    ipadPPPCfgTable.setStatus("optional")
_IpadPPPCfgTableEntry_Object = MibTableRow
ipadPPPCfgTableEntry = _IpadPPPCfgTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 1, 1)
)
ipadPPPCfgTableEntry.setIndexNames(
    (0, "IPAD-MIB", "ipadPPPCfgService"),
)
if mibBuilder.loadTexts:
    ipadPPPCfgTableEntry.setStatus("mandatory")
_IpadPPPCfgService_Type = Integer32
_IpadPPPCfgService_Object = MibTableColumn
ipadPPPCfgService = _IpadPPPCfgService_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 1, 1, 1),
    _IpadPPPCfgService_Type()
)
ipadPPPCfgService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadPPPCfgService.setStatus("mandatory")


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
    ipadPPPCfgDialMode.setStatus("mandatory")
_IpadPPPCfgInactivityTimer_Type = Integer32
_IpadPPPCfgInactivityTimer_Object = MibTableColumn
ipadPPPCfgInactivityTimer = _IpadPPPCfgInactivityTimer_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 1, 1, 3),
    _IpadPPPCfgInactivityTimer_Type()
)
ipadPPPCfgInactivityTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadPPPCfgInactivityTimer.setStatus("mandatory")


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
    ipadPPPCfgNegotiationInit.setStatus("mandatory")
_IpadPPPCfgMRU_Type = Integer32
_IpadPPPCfgMRU_Object = MibTableColumn
ipadPPPCfgMRU = _IpadPPPCfgMRU_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 1, 1, 5),
    _IpadPPPCfgMRU_Type()
)
ipadPPPCfgMRU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadPPPCfgMRU.setStatus("mandatory")
_IpadPPPCfgACCM_Type = Integer32
_IpadPPPCfgACCM_Object = MibTableColumn
ipadPPPCfgACCM = _IpadPPPCfgACCM_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 1, 1, 6),
    _IpadPPPCfgACCM_Type()
)
ipadPPPCfgACCM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadPPPCfgACCM.setStatus("mandatory")


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
    ipadPPPCfgNegMRU.setStatus("mandatory")


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
    ipadPPPCfgNegACCM.setStatus("mandatory")


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
    ipadPPPCfgNegMagic.setStatus("mandatory")


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
    ipadPPPCfgNegCompression.setStatus("mandatory")


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
    ipadPPPCfgNegAddress.setStatus("mandatory")


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
    ipadPPPCfgNegPAP.setStatus("mandatory")


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
    ipadPPPCfgNegCHAP.setStatus("mandatory")


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
    ipadPPPCfgAllowPAP.setStatus("mandatory")


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
    ipadPPPCfgAllowCHAP.setStatus("mandatory")


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
    ipadPPPCfgPAPUsername.setStatus("mandatory")


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
    ipadPPPCfgPAPPassword.setStatus("mandatory")


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
    ipadPPPCfgCHAPUsername.setStatus("mandatory")


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
    ipadPPPCfgCHAPSecret.setStatus("mandatory")
_IpadPPPCfgPortIpAddress_Type = IpAddress
_IpadPPPCfgPortIpAddress_Object = MibTableColumn
ipadPPPCfgPortIpAddress = _IpadPPPCfgPortIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 1, 1, 20),
    _IpadPPPCfgPortIpAddress_Type()
)
ipadPPPCfgPortIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadPPPCfgPortIpAddress.setStatus("mandatory")
_IpadPPPCfgPeerIpAddress_Type = IpAddress
_IpadPPPCfgPeerIpAddress_Object = MibTableColumn
ipadPPPCfgPeerIpAddress = _IpadPPPCfgPeerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 1, 1, 21),
    _IpadPPPCfgPeerIpAddress_Type()
)
ipadPPPCfgPeerIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadPPPCfgPeerIpAddress.setStatus("mandatory")


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
    ipadPPPCfgNegIpAddress.setStatus("mandatory")


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
    ipadPPPCfgNegIPCPCompression.setStatus("mandatory")
_IpadPPPCfgSubnetMask_Type = IpAddress
_IpadPPPCfgSubnetMask_Object = MibTableColumn
ipadPPPCfgSubnetMask = _IpadPPPCfgSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 1, 1, 24),
    _IpadPPPCfgSubnetMask_Type()
)
ipadPPPCfgSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadPPPCfgSubnetMask.setStatus("mandatory")
_IpadPPPCfgAuthChallengeInterval_Type = Integer32
_IpadPPPCfgAuthChallengeInterval_Object = MibTableColumn
ipadPPPCfgAuthChallengeInterval = _IpadPPPCfgAuthChallengeInterval_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 1, 1, 25),
    _IpadPPPCfgAuthChallengeInterval_Type()
)
ipadPPPCfgAuthChallengeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadPPPCfgAuthChallengeInterval.setStatus("mandatory")
_IpadPPPPAPTable_Object = MibTable
ipadPPPPAPTable = _IpadPPPPAPTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 2)
)
if mibBuilder.loadTexts:
    ipadPPPPAPTable.setStatus("optional")
_IpadPPPPAPTableEntry_Object = MibTableRow
ipadPPPPAPTableEntry = _IpadPPPPAPTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 2, 1)
)
ipadPPPPAPTableEntry.setIndexNames(
    (0, "IPAD-MIB", "ipadPPPPAPTableIndex"),
)
if mibBuilder.loadTexts:
    ipadPPPPAPTableEntry.setStatus("mandatory")
_IpadPPPPAPTableIndex_Type = Integer32
_IpadPPPPAPTableIndex_Object = MibTableColumn
ipadPPPPAPTableIndex = _IpadPPPPAPTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 2, 1, 1),
    _IpadPPPPAPTableIndex_Type()
)
ipadPPPPAPTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadPPPPAPTableIndex.setStatus("mandatory")


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
    ipadPPPPAPTableUsername.setStatus("mandatory")


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
    ipadPPPPAPTablePassword.setStatus("mandatory")
_IpadPPPCHAPTable_Object = MibTable
ipadPPPCHAPTable = _IpadPPPCHAPTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 3)
)
if mibBuilder.loadTexts:
    ipadPPPCHAPTable.setStatus("optional")
_IpadPPPCHAPTableEntry_Object = MibTableRow
ipadPPPCHAPTableEntry = _IpadPPPCHAPTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 3, 1)
)
ipadPPPCHAPTableEntry.setIndexNames(
    (0, "IPAD-MIB", "ipadPPPCHAPTableIndex"),
)
if mibBuilder.loadTexts:
    ipadPPPCHAPTableEntry.setStatus("mandatory")
_IpadPPPCHAPTableIndex_Type = Integer32
_IpadPPPCHAPTableIndex_Object = MibTableColumn
ipadPPPCHAPTableIndex = _IpadPPPCHAPTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 3, 1, 1),
    _IpadPPPCHAPTableIndex_Type()
)
ipadPPPCHAPTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadPPPCHAPTableIndex.setStatus("mandatory")


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
    ipadPPPCHAPTableUsername.setStatus("mandatory")


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
    ipadPPPCHAPTableSecret.setStatus("mandatory")
_IpadModem_ObjectIdentity = ObjectIdentity
ipadModem = _IpadModem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 8)
)
_IpadModemDialTable_Object = MibTable
ipadModemDialTable = _IpadModemDialTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 8, 1)
)
if mibBuilder.loadTexts:
    ipadModemDialTable.setStatus("optional")
_IpadModemDialTableEntry_Object = MibTableRow
ipadModemDialTableEntry = _IpadModemDialTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 8, 1, 1)
)
ipadModemDialTableEntry.setIndexNames(
    (0, "IPAD-MIB", "ipadModemDialTableIndex"),
)
if mibBuilder.loadTexts:
    ipadModemDialTableEntry.setStatus("mandatory")


class _IpadModemDialTableIndex_Type(Integer32):
    """Custom type ipadModemDialTableIndex based on Integer32"""
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
        *(("ethernet", 6),
          ("network1", 2),
          ("network2", 3),
          ("supervisor", 1),
          ("user1", 4),
          ("user2", 5))
    )


_IpadModemDialTableIndex_Type.__name__ = "Integer32"
_IpadModemDialTableIndex_Object = MibTableColumn
ipadModemDialTableIndex = _IpadModemDialTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 8, 1, 1, 1),
    _IpadModemDialTableIndex_Type()
)
ipadModemDialTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadModemDialTableIndex.setStatus("mandatory")
_IpadModemDialDataIndex_Type = Integer32
_IpadModemDialDataIndex_Object = MibTableColumn
ipadModemDialDataIndex = _IpadModemDialDataIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 8, 1, 1, 2),
    _IpadModemDialDataIndex_Type()
)
ipadModemDialDataIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadModemDialDataIndex.setStatus("mandatory")


class _IpadModemDialNumber_Type(DisplayString):
    """Custom type ipadModemDialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_IpadModemDialNumber_Type.__name__ = "DisplayString"
_IpadModemDialNumber_Object = MibTableColumn
ipadModemDialNumber = _IpadModemDialNumber_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 8, 1, 1, 3),
    _IpadModemDialNumber_Type()
)
ipadModemDialNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadModemDialNumber.setStatus("mandatory")
_IpadModemDialAbortTimer_Type = Integer32
_IpadModemDialAbortTimer_Object = MibTableColumn
ipadModemDialAbortTimer = _IpadModemDialAbortTimer_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 8, 1, 1, 4),
    _IpadModemDialAbortTimer_Type()
)
ipadModemDialAbortTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadModemDialAbortTimer.setStatus("mandatory")
_IpadModemDialRedialAttempts_Type = Integer32
_IpadModemDialRedialAttempts_Object = MibTableColumn
ipadModemDialRedialAttempts = _IpadModemDialRedialAttempts_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 8, 1, 1, 5),
    _IpadModemDialRedialAttempts_Type()
)
ipadModemDialRedialAttempts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadModemDialRedialAttempts.setStatus("mandatory")
_IpadModemDialDelayBeforeRedial_Type = Integer32
_IpadModemDialDelayBeforeRedial_Object = MibTableColumn
ipadModemDialDelayBeforeRedial = _IpadModemDialDelayBeforeRedial_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 8, 1, 1, 6),
    _IpadModemDialDelayBeforeRedial_Type()
)
ipadModemDialDelayBeforeRedial.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadModemDialDelayBeforeRedial.setStatus("mandatory")


class _IpadModemDialLoginScript_Type(DisplayString):
    """Custom type ipadModemDialLoginScript based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_IpadModemDialLoginScript_Type.__name__ = "DisplayString"
_IpadModemDialLoginScript_Object = MibTableColumn
ipadModemDialLoginScript = _IpadModemDialLoginScript_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 8, 1, 1, 7),
    _IpadModemDialLoginScript_Type()
)
ipadModemDialLoginScript.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadModemDialLoginScript.setStatus("mandatory")


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
    ipadModemDialUsername.setStatus("mandatory")


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
    ipadModemDialPassword.setStatus("mandatory")
_IpadModemDataTable_Object = MibTable
ipadModemDataTable = _IpadModemDataTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 8, 2)
)
if mibBuilder.loadTexts:
    ipadModemDataTable.setStatus("optional")
_IpadModemDataTableEntry_Object = MibTableRow
ipadModemDataTableEntry = _IpadModemDataTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 8, 2, 1)
)
ipadModemDataTableEntry.setIndexNames(
    (0, "IPAD-MIB", "ipadModemDataTableIndex"),
)
if mibBuilder.loadTexts:
    ipadModemDataTableEntry.setStatus("mandatory")
_IpadModemDataTableIndex_Type = Integer32
_IpadModemDataTableIndex_Object = MibTableColumn
ipadModemDataTableIndex = _IpadModemDataTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 8, 2, 1, 1),
    _IpadModemDataTableIndex_Type()
)
ipadModemDataTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadModemDataTableIndex.setStatus("mandatory")


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
    ipadModemDataModemName.setStatus("mandatory")


class _IpadModemDataSetupScript_Type(DisplayString):
    """Custom type ipadModemDataSetupScript based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_IpadModemDataSetupScript_Type.__name__ = "DisplayString"
_IpadModemDataSetupScript_Object = MibTableColumn
ipadModemDataSetupScript = _IpadModemDataSetupScript_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 8, 2, 1, 3),
    _IpadModemDataSetupScript_Type()
)
ipadModemDataSetupScript.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadModemDataSetupScript.setStatus("mandatory")


class _IpadModemDataDialingScript_Type(DisplayString):
    """Custom type ipadModemDataDialingScript based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_IpadModemDataDialingScript_Type.__name__ = "DisplayString"
_IpadModemDataDialingScript_Object = MibTableColumn
ipadModemDataDialingScript = _IpadModemDataDialingScript_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 8, 2, 1, 4),
    _IpadModemDataDialingScript_Type()
)
ipadModemDataDialingScript.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadModemDataDialingScript.setStatus("mandatory")


class _IpadModemDataAnswerScript_Type(DisplayString):
    """Custom type ipadModemDataAnswerScript based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_IpadModemDataAnswerScript_Type.__name__ = "DisplayString"
_IpadModemDataAnswerScript_Object = MibTableColumn
ipadModemDataAnswerScript = _IpadModemDataAnswerScript_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 8, 2, 1, 5),
    _IpadModemDataAnswerScript_Type()
)
ipadModemDataAnswerScript.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadModemDataAnswerScript.setStatus("mandatory")


class _IpadModemDataHangupScript_Type(DisplayString):
    """Custom type ipadModemDataHangupScript based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_IpadModemDataHangupScript_Type.__name__ = "DisplayString"
_IpadModemDataHangupScript_Object = MibTableColumn
ipadModemDataHangupScript = _IpadModemDataHangupScript_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 8, 2, 1, 6),
    _IpadModemDataHangupScript_Type()
)
ipadModemDataHangupScript.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadModemDataHangupScript.setStatus("mandatory")
_IpadSvcAware_ObjectIdentity = ObjectIdentity
ipadSvcAware = _IpadSvcAware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9)
)
_IpadFrPortStatsTable_Object = MibTable
ipadFrPortStatsTable = _IpadFrPortStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 1)
)
if mibBuilder.loadTexts:
    ipadFrPortStatsTable.setStatus("optional")
_IpadFrPortStatsEntry_Object = MibTableRow
ipadFrPortStatsEntry = _IpadFrPortStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 1, 1)
)
ipadFrPortStatsEntry.setIndexNames(
    (0, "IPAD-MIB", "ipadFrPortStatsService"),
    (0, "IPAD-MIB", "ipadFrPortStatsPeriod"),
)
if mibBuilder.loadTexts:
    ipadFrPortStatsEntry.setStatus("mandatory")
_IpadFrPortStatsService_Type = Integer32
_IpadFrPortStatsService_Object = MibTableColumn
ipadFrPortStatsService = _IpadFrPortStatsService_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 1, 1, 1),
    _IpadFrPortStatsService_Type()
)
ipadFrPortStatsService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadFrPortStatsService.setStatus("mandatory")


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
    ipadFrPortStatsPeriod.setStatus("mandatory")
_IpadFrPortStatsTxFrames_Type = Integer32
_IpadFrPortStatsTxFrames_Object = MibTableColumn
ipadFrPortStatsTxFrames = _IpadFrPortStatsTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 1, 1, 3),
    _IpadFrPortStatsTxFrames_Type()
)
ipadFrPortStatsTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadFrPortStatsTxFrames.setStatus("mandatory")
_IpadFrPortStatsRxFrames_Type = Integer32
_IpadFrPortStatsRxFrames_Object = MibTableColumn
ipadFrPortStatsRxFrames = _IpadFrPortStatsRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 1, 1, 4),
    _IpadFrPortStatsRxFrames_Type()
)
ipadFrPortStatsRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadFrPortStatsRxFrames.setStatus("mandatory")
_IpadFrPortStatsTxOctets_Type = Integer32
_IpadFrPortStatsTxOctets_Object = MibTableColumn
ipadFrPortStatsTxOctets = _IpadFrPortStatsTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 1, 1, 5),
    _IpadFrPortStatsTxOctets_Type()
)
ipadFrPortStatsTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadFrPortStatsTxOctets.setStatus("mandatory")
_IpadFrPortStatsRxOctets_Type = Integer32
_IpadFrPortStatsRxOctets_Object = MibTableColumn
ipadFrPortStatsRxOctets = _IpadFrPortStatsRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 1, 1, 6),
    _IpadFrPortStatsRxOctets_Type()
)
ipadFrPortStatsRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadFrPortStatsRxOctets.setStatus("mandatory")
_IpadFrPortStatsTxMgmtFrames_Type = Integer32
_IpadFrPortStatsTxMgmtFrames_Object = MibTableColumn
ipadFrPortStatsTxMgmtFrames = _IpadFrPortStatsTxMgmtFrames_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 1, 1, 7),
    _IpadFrPortStatsTxMgmtFrames_Type()
)
ipadFrPortStatsTxMgmtFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadFrPortStatsTxMgmtFrames.setStatus("mandatory")
_IpadFrPortStatsRxMgmtFrames_Type = Integer32
_IpadFrPortStatsRxMgmtFrames_Object = MibTableColumn
ipadFrPortStatsRxMgmtFrames = _IpadFrPortStatsRxMgmtFrames_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 1, 1, 8),
    _IpadFrPortStatsRxMgmtFrames_Type()
)
ipadFrPortStatsRxMgmtFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadFrPortStatsRxMgmtFrames.setStatus("mandatory")
_IpadFrPortStatsTxMgmtOctets_Type = Integer32
_IpadFrPortStatsTxMgmtOctets_Object = MibTableColumn
ipadFrPortStatsTxMgmtOctets = _IpadFrPortStatsTxMgmtOctets_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 1, 1, 9),
    _IpadFrPortStatsTxMgmtOctets_Type()
)
ipadFrPortStatsTxMgmtOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadFrPortStatsTxMgmtOctets.setStatus("mandatory")
_IpadFrPortStatsRxMgmtOctets_Type = Integer32
_IpadFrPortStatsRxMgmtOctets_Object = MibTableColumn
ipadFrPortStatsRxMgmtOctets = _IpadFrPortStatsRxMgmtOctets_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 1, 1, 10),
    _IpadFrPortStatsRxMgmtOctets_Type()
)
ipadFrPortStatsRxMgmtOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadFrPortStatsRxMgmtOctets.setStatus("mandatory")
_IpadFrPortStatsRxFECN_Type = Integer32
_IpadFrPortStatsRxFECN_Object = MibTableColumn
ipadFrPortStatsRxFECN = _IpadFrPortStatsRxFECN_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 1, 1, 11),
    _IpadFrPortStatsRxFECN_Type()
)
ipadFrPortStatsRxFECN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadFrPortStatsRxFECN.setStatus("mandatory")
_IpadFrPortStatsRxBECN_Type = Integer32
_IpadFrPortStatsRxBECN_Object = MibTableColumn
ipadFrPortStatsRxBECN = _IpadFrPortStatsRxBECN_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 1, 1, 12),
    _IpadFrPortStatsRxBECN_Type()
)
ipadFrPortStatsRxBECN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadFrPortStatsRxBECN.setStatus("mandatory")
_IpadFrPortStatsRxInvalid_Type = Integer32
_IpadFrPortStatsRxInvalid_Object = MibTableColumn
ipadFrPortStatsRxInvalid = _IpadFrPortStatsRxInvalid_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 1, 1, 13),
    _IpadFrPortStatsRxInvalid_Type()
)
ipadFrPortStatsRxInvalid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadFrPortStatsRxInvalid.setStatus("mandatory")
_IpadFrPortStatsTxStatInq_Type = Integer32
_IpadFrPortStatsTxStatInq_Object = MibTableColumn
ipadFrPortStatsTxStatInq = _IpadFrPortStatsTxStatInq_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 1, 1, 14),
    _IpadFrPortStatsTxStatInq_Type()
)
ipadFrPortStatsTxStatInq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadFrPortStatsTxStatInq.setStatus("mandatory")
_IpadFrPortStatsRxStatInq_Type = Integer32
_IpadFrPortStatsRxStatInq_Object = MibTableColumn
ipadFrPortStatsRxStatInq = _IpadFrPortStatsRxStatInq_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 1, 1, 15),
    _IpadFrPortStatsRxStatInq_Type()
)
ipadFrPortStatsRxStatInq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadFrPortStatsRxStatInq.setStatus("mandatory")
_IpadFrPortStatsTxStatResp_Type = Integer32
_IpadFrPortStatsTxStatResp_Object = MibTableColumn
ipadFrPortStatsTxStatResp = _IpadFrPortStatsTxStatResp_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 1, 1, 16),
    _IpadFrPortStatsTxStatResp_Type()
)
ipadFrPortStatsTxStatResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadFrPortStatsTxStatResp.setStatus("mandatory")
_IpadFrPortStatsRxStatResp_Type = Integer32
_IpadFrPortStatsRxStatResp_Object = MibTableColumn
ipadFrPortStatsRxStatResp = _IpadFrPortStatsRxStatResp_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 1, 1, 17),
    _IpadFrPortStatsRxStatResp_Type()
)
ipadFrPortStatsRxStatResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadFrPortStatsRxStatResp.setStatus("mandatory")
_IpadFrPortStatsRxInvLMI_Type = Integer32
_IpadFrPortStatsRxInvLMI_Object = MibTableColumn
ipadFrPortStatsRxInvLMI = _IpadFrPortStatsRxInvLMI_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 1, 1, 18),
    _IpadFrPortStatsRxInvLMI_Type()
)
ipadFrPortStatsRxInvLMI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadFrPortStatsRxInvLMI.setStatus("mandatory")
_IpadFrPortStatsPeak_Type = Integer32
_IpadFrPortStatsPeak_Object = MibTableColumn
ipadFrPortStatsPeak = _IpadFrPortStatsPeak_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 1, 1, 19),
    _IpadFrPortStatsPeak_Type()
)
ipadFrPortStatsPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadFrPortStatsPeak.setStatus("mandatory")
_IpadFrPortStatsAverage_Type = Integer32
_IpadFrPortStatsAverage_Object = MibTableColumn
ipadFrPortStatsAverage = _IpadFrPortStatsAverage_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 1, 1, 20),
    _IpadFrPortStatsAverage_Type()
)
ipadFrPortStatsAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadFrPortStatsAverage.setStatus("mandatory")
_IpadDLCIstatsTable_Object = MibTable
ipadDLCIstatsTable = _IpadDLCIstatsTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 2)
)
if mibBuilder.loadTexts:
    ipadDLCIstatsTable.setStatus("optional")
_IpadDLCIstatsEntry_Object = MibTableRow
ipadDLCIstatsEntry = _IpadDLCIstatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 2, 1)
)
ipadDLCIstatsEntry.setIndexNames(
    (0, "IPAD-MIB", "ipadDLCIstatsService"),
    (0, "IPAD-MIB", "ipadDLCIstatsDLCI"),
    (0, "IPAD-MIB", "ipadDLCIstatsPeriod"),
)
if mibBuilder.loadTexts:
    ipadDLCIstatsEntry.setStatus("mandatory")
_IpadDLCIstatsService_Type = Integer32
_IpadDLCIstatsService_Object = MibTableColumn
ipadDLCIstatsService = _IpadDLCIstatsService_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 2, 1, 1),
    _IpadDLCIstatsService_Type()
)
ipadDLCIstatsService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDLCIstatsService.setStatus("mandatory")
_IpadDLCIstatsDLCI_Type = Integer32
_IpadDLCIstatsDLCI_Object = MibTableColumn
ipadDLCIstatsDLCI = _IpadDLCIstatsDLCI_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 2, 1, 2),
    _IpadDLCIstatsDLCI_Type()
)
ipadDLCIstatsDLCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDLCIstatsDLCI.setStatus("mandatory")


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
    ipadDLCIstatsPeriod.setStatus("mandatory")
_IpadDLCIstatsTxFrames_Type = Integer32
_IpadDLCIstatsTxFrames_Object = MibTableColumn
ipadDLCIstatsTxFrames = _IpadDLCIstatsTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 2, 1, 4),
    _IpadDLCIstatsTxFrames_Type()
)
ipadDLCIstatsTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDLCIstatsTxFrames.setStatus("mandatory")
_IpadDLCIstatsRxFrames_Type = Integer32
_IpadDLCIstatsRxFrames_Object = MibTableColumn
ipadDLCIstatsRxFrames = _IpadDLCIstatsRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 2, 1, 5),
    _IpadDLCIstatsRxFrames_Type()
)
ipadDLCIstatsRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDLCIstatsRxFrames.setStatus("mandatory")
_IpadDLCIstatsTxOctets_Type = Integer32
_IpadDLCIstatsTxOctets_Object = MibTableColumn
ipadDLCIstatsTxOctets = _IpadDLCIstatsTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 2, 1, 6),
    _IpadDLCIstatsTxOctets_Type()
)
ipadDLCIstatsTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDLCIstatsTxOctets.setStatus("mandatory")
_IpadDLCIstatsRxOctets_Type = Integer32
_IpadDLCIstatsRxOctets_Object = MibTableColumn
ipadDLCIstatsRxOctets = _IpadDLCIstatsRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 2, 1, 7),
    _IpadDLCIstatsRxOctets_Type()
)
ipadDLCIstatsRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDLCIstatsRxOctets.setStatus("mandatory")
_IpadDLCIstatsRxFECN_Type = Integer32
_IpadDLCIstatsRxFECN_Object = MibTableColumn
ipadDLCIstatsRxFECN = _IpadDLCIstatsRxFECN_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 2, 1, 8),
    _IpadDLCIstatsRxFECN_Type()
)
ipadDLCIstatsRxFECN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDLCIstatsRxFECN.setStatus("mandatory")
_IpadDLCIstatsRxBECN_Type = Integer32
_IpadDLCIstatsRxBECN_Object = MibTableColumn
ipadDLCIstatsRxBECN = _IpadDLCIstatsRxBECN_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 2, 1, 9),
    _IpadDLCIstatsRxBECN_Type()
)
ipadDLCIstatsRxBECN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDLCIstatsRxBECN.setStatus("mandatory")
_IpadDLCIstatsRxDE_Type = Integer32
_IpadDLCIstatsRxDE_Object = MibTableColumn
ipadDLCIstatsRxDE = _IpadDLCIstatsRxDE_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 2, 1, 10),
    _IpadDLCIstatsRxDE_Type()
)
ipadDLCIstatsRxDE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDLCIstatsRxDE.setStatus("mandatory")
_IpadDLCIstatsTxExcessCIR_Type = Integer32
_IpadDLCIstatsTxExcessCIR_Object = MibTableColumn
ipadDLCIstatsTxExcessCIR = _IpadDLCIstatsTxExcessCIR_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 2, 1, 11),
    _IpadDLCIstatsTxExcessCIR_Type()
)
ipadDLCIstatsTxExcessCIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDLCIstatsTxExcessCIR.setStatus("mandatory")
_IpadDLCIstatsTxExcessBe_Type = Integer32
_IpadDLCIstatsTxExcessBe_Object = MibTableColumn
ipadDLCIstatsTxExcessBe = _IpadDLCIstatsTxExcessBe_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 2, 1, 12),
    _IpadDLCIstatsTxExcessBe_Type()
)
ipadDLCIstatsTxExcessBe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDLCIstatsTxExcessBe.setStatus("mandatory")
_IpadDLCIstatsTxMgmtFrames_Type = Integer32
_IpadDLCIstatsTxMgmtFrames_Object = MibTableColumn
ipadDLCIstatsTxMgmtFrames = _IpadDLCIstatsTxMgmtFrames_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 2, 1, 13),
    _IpadDLCIstatsTxMgmtFrames_Type()
)
ipadDLCIstatsTxMgmtFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDLCIstatsTxMgmtFrames.setStatus("mandatory")
_IpadDLCIstatsRxMgmtFrames_Type = Integer32
_IpadDLCIstatsRxMgmtFrames_Object = MibTableColumn
ipadDLCIstatsRxMgmtFrames = _IpadDLCIstatsRxMgmtFrames_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 2, 1, 14),
    _IpadDLCIstatsRxMgmtFrames_Type()
)
ipadDLCIstatsRxMgmtFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDLCIstatsRxMgmtFrames.setStatus("mandatory")
_IpadDLCIstatsTxMgmtOctets_Type = Integer32
_IpadDLCIstatsTxMgmtOctets_Object = MibTableColumn
ipadDLCIstatsTxMgmtOctets = _IpadDLCIstatsTxMgmtOctets_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 2, 1, 15),
    _IpadDLCIstatsTxMgmtOctets_Type()
)
ipadDLCIstatsTxMgmtOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDLCIstatsTxMgmtOctets.setStatus("mandatory")
_IpadDLCIstatsRxMgmtOctets_Type = Integer32
_IpadDLCIstatsRxMgmtOctets_Object = MibTableColumn
ipadDLCIstatsRxMgmtOctets = _IpadDLCIstatsRxMgmtOctets_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 2, 1, 16),
    _IpadDLCIstatsRxMgmtOctets_Type()
)
ipadDLCIstatsRxMgmtOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDLCIstatsRxMgmtOctets.setStatus("mandatory")
_IpadDLCIstatsPeak_Type = Integer32
_IpadDLCIstatsPeak_Object = MibTableColumn
ipadDLCIstatsPeak = _IpadDLCIstatsPeak_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 2, 1, 17),
    _IpadDLCIstatsPeak_Type()
)
ipadDLCIstatsPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDLCIstatsPeak.setStatus("mandatory")
_IpadDLCIstatsAverage_Type = Integer32
_IpadDLCIstatsAverage_Object = MibTableColumn
ipadDLCIstatsAverage = _IpadDLCIstatsAverage_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 2, 1, 18),
    _IpadDLCIstatsAverage_Type()
)
ipadDLCIstatsAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDLCIstatsAverage.setStatus("mandatory")
_IpadDLCIstatsDelayPeak_Type = Integer32
_IpadDLCIstatsDelayPeak_Object = MibTableColumn
ipadDLCIstatsDelayPeak = _IpadDLCIstatsDelayPeak_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 2, 1, 19),
    _IpadDLCIstatsDelayPeak_Type()
)
ipadDLCIstatsDelayPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDLCIstatsDelayPeak.setStatus("mandatory")
_IpadDLCIstatsDelayAverage_Type = Integer32
_IpadDLCIstatsDelayAverage_Object = MibTableColumn
ipadDLCIstatsDelayAverage = _IpadDLCIstatsDelayAverage_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 2, 1, 20),
    _IpadDLCIstatsDelayAverage_Type()
)
ipadDLCIstatsDelayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDLCIstatsDelayAverage.setStatus("mandatory")
_IpadDLCIstatsRoundTripTimeouts_Type = Integer32
_IpadDLCIstatsRoundTripTimeouts_Object = MibTableColumn
ipadDLCIstatsRoundTripTimeouts = _IpadDLCIstatsRoundTripTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 2, 1, 21),
    _IpadDLCIstatsRoundTripTimeouts_Type()
)
ipadDLCIstatsRoundTripTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDLCIstatsRoundTripTimeouts.setStatus("mandatory")
_IpadDLCIstatsUAS_Type = Integer32
_IpadDLCIstatsUAS_Object = MibTableColumn
ipadDLCIstatsUAS = _IpadDLCIstatsUAS_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 2, 1, 22),
    _IpadDLCIstatsUAS_Type()
)
ipadDLCIstatsUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadDLCIstatsUAS.setStatus("mandatory")
_IpadUserStatsTable_Object = MibTable
ipadUserStatsTable = _IpadUserStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 3)
)
if mibBuilder.loadTexts:
    ipadUserStatsTable.setStatus("optional")
_IpadUserStatsEntry_Object = MibTableRow
ipadUserStatsEntry = _IpadUserStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 3, 1)
)
ipadUserStatsEntry.setIndexNames(
    (0, "IPAD-MIB", "ipadUserStatsIndex"),
    (0, "IPAD-MIB", "ipadUserStatsPeriod"),
)
if mibBuilder.loadTexts:
    ipadUserStatsEntry.setStatus("mandatory")
_IpadUserStatsIndex_Type = Integer32
_IpadUserStatsIndex_Object = MibTableColumn
ipadUserStatsIndex = _IpadUserStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 3, 1, 1),
    _IpadUserStatsIndex_Type()
)
ipadUserStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadUserStatsIndex.setStatus("mandatory")


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
    ipadUserStatsPeriod.setStatus("mandatory")
_IpadUserStatsTxFrames_Type = Integer32
_IpadUserStatsTxFrames_Object = MibTableColumn
ipadUserStatsTxFrames = _IpadUserStatsTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 3, 1, 3),
    _IpadUserStatsTxFrames_Type()
)
ipadUserStatsTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadUserStatsTxFrames.setStatus("mandatory")
_IpadUserStatsRxFrames_Type = Integer32
_IpadUserStatsRxFrames_Object = MibTableColumn
ipadUserStatsRxFrames = _IpadUserStatsRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 3, 1, 4),
    _IpadUserStatsRxFrames_Type()
)
ipadUserStatsRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadUserStatsRxFrames.setStatus("mandatory")
_IpadUserStatsTxOctets_Type = Integer32
_IpadUserStatsTxOctets_Object = MibTableColumn
ipadUserStatsTxOctets = _IpadUserStatsTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 3, 1, 5),
    _IpadUserStatsTxOctets_Type()
)
ipadUserStatsTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadUserStatsTxOctets.setStatus("mandatory")
_IpadUserStatsRxOctets_Type = Integer32
_IpadUserStatsRxOctets_Object = MibTableColumn
ipadUserStatsRxOctets = _IpadUserStatsRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 3, 1, 6),
    _IpadUserStatsRxOctets_Type()
)
ipadUserStatsRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadUserStatsRxOctets.setStatus("mandatory")
_IpadUserStatsTxRatePeak_Type = Integer32
_IpadUserStatsTxRatePeak_Object = MibTableColumn
ipadUserStatsTxRatePeak = _IpadUserStatsTxRatePeak_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 3, 1, 7),
    _IpadUserStatsTxRatePeak_Type()
)
ipadUserStatsTxRatePeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadUserStatsTxRatePeak.setStatus("mandatory")
_IpadUserStatsTxRateAverage_Type = Integer32
_IpadUserStatsTxRateAverage_Object = MibTableColumn
ipadUserStatsTxRateAverage = _IpadUserStatsTxRateAverage_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 3, 1, 8),
    _IpadUserStatsTxRateAverage_Type()
)
ipadUserStatsTxRateAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadUserStatsTxRateAverage.setStatus("mandatory")
_IpadIPTopNStatsTable_Object = MibTable
ipadIPTopNStatsTable = _IpadIPTopNStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 4)
)
if mibBuilder.loadTexts:
    ipadIPTopNStatsTable.setStatus("optional")
_IpadIPTopNStatsEntry_Object = MibTableRow
ipadIPTopNStatsEntry = _IpadIPTopNStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 4, 1)
)
ipadIPTopNStatsEntry.setIndexNames(
    (0, "IPAD-MIB", "ipadIPTopNStatsIndex"),
)
if mibBuilder.loadTexts:
    ipadIPTopNStatsEntry.setStatus("mandatory")
_IpadIPTopNStatsIndex_Type = Integer32
_IpadIPTopNStatsIndex_Object = MibTableColumn
ipadIPTopNStatsIndex = _IpadIPTopNStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 4, 1, 1),
    _IpadIPTopNStatsIndex_Type()
)
ipadIPTopNStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadIPTopNStatsIndex.setStatus("mandatory")


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
    ipadIPTopNStatsAddress.setStatus("mandatory")
_IpadIPTopNStatsTimestamp_Type = TimeTicks
_IpadIPTopNStatsTimestamp_Object = MibTableColumn
ipadIPTopNStatsTimestamp = _IpadIPTopNStatsTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 4, 1, 3),
    _IpadIPTopNStatsTimestamp_Type()
)
ipadIPTopNStatsTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadIPTopNStatsTimestamp.setStatus("mandatory")
_IpadIPTopNStatsRxFrames_Type = Integer32
_IpadIPTopNStatsRxFrames_Object = MibTableColumn
ipadIPTopNStatsRxFrames = _IpadIPTopNStatsRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 4, 1, 4),
    _IpadIPTopNStatsRxFrames_Type()
)
ipadIPTopNStatsRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadIPTopNStatsRxFrames.setStatus("mandatory")
_IpadIPTopNStatsRxOctets_Type = Integer32
_IpadIPTopNStatsRxOctets_Object = MibTableColumn
ipadIPTopNStatsRxOctets = _IpadIPTopNStatsRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 4, 1, 5),
    _IpadIPTopNStatsRxOctets_Type()
)
ipadIPTopNStatsRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadIPTopNStatsRxOctets.setStatus("mandatory")
_IpadIPTopNStatsTxFrames_Type = Integer32
_IpadIPTopNStatsTxFrames_Object = MibTableColumn
ipadIPTopNStatsTxFrames = _IpadIPTopNStatsTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 4, 1, 6),
    _IpadIPTopNStatsTxFrames_Type()
)
ipadIPTopNStatsTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadIPTopNStatsTxFrames.setStatus("mandatory")
_IpadIPTopNStatsTxOctets_Type = Integer32
_IpadIPTopNStatsTxOctets_Object = MibTableColumn
ipadIPTopNStatsTxOctets = _IpadIPTopNStatsTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 9, 4, 1, 7),
    _IpadIPTopNStatsTxOctets_Type()
)
ipadIPTopNStatsTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadIPTopNStatsTxOctets.setStatus("mandatory")
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
              5)
        )
    )
    namedValues = NamedValues(
        *(("monitor", 3),
          ("other", 1),
          ("packet", 4),
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
    ipadPktSwOperatingMode.setStatus("mandatory")
_IpadPktSwCfgTable_Object = MibTable
ipadPktSwCfgTable = _IpadPktSwCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 10, 2)
)
if mibBuilder.loadTexts:
    ipadPktSwCfgTable.setStatus("optional")
_IpadPktSwCfgTableEntry_Object = MibTableRow
ipadPktSwCfgTableEntry = _IpadPktSwCfgTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 10, 2, 1)
)
ipadPktSwCfgTableEntry.setIndexNames(
    (0, "IPAD-MIB", "ipadPktSwCfgService"),
)
if mibBuilder.loadTexts:
    ipadPktSwCfgTableEntry.setStatus("mandatory")
_IpadPktSwCfgService_Type = Integer32
_IpadPktSwCfgService_Object = MibTableColumn
ipadPktSwCfgService = _IpadPktSwCfgService_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 10, 2, 1, 1),
    _IpadPktSwCfgService_Type()
)
ipadPktSwCfgService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadPktSwCfgService.setStatus("mandatory")


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
    ipadPktSwCfgInterfaceType.setStatus("mandatory")


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
    ipadPktSwCfgLnkMgmtType.setStatus("mandatory")
_IpadPktSwCfgMaxFrameSize_Type = Integer32
_IpadPktSwCfgMaxFrameSize_Object = MibTableColumn
ipadPktSwCfgMaxFrameSize = _IpadPktSwCfgMaxFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 10, 2, 1, 4),
    _IpadPktSwCfgMaxFrameSize_Type()
)
ipadPktSwCfgMaxFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadPktSwCfgMaxFrameSize.setStatus("mandatory")
_IpadPktSwCfgnN1_Type = Integer32
_IpadPktSwCfgnN1_Object = MibTableColumn
ipadPktSwCfgnN1 = _IpadPktSwCfgnN1_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 10, 2, 1, 5),
    _IpadPktSwCfgnN1_Type()
)
ipadPktSwCfgnN1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadPktSwCfgnN1.setStatus("mandatory")
_IpadPktSwCfgnN2_Type = Integer32
_IpadPktSwCfgnN2_Object = MibTableColumn
ipadPktSwCfgnN2 = _IpadPktSwCfgnN2_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 10, 2, 1, 6),
    _IpadPktSwCfgnN2_Type()
)
ipadPktSwCfgnN2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadPktSwCfgnN2.setStatus("mandatory")
_IpadPktSwCfgnN3_Type = Integer32
_IpadPktSwCfgnN3_Object = MibTableColumn
ipadPktSwCfgnN3 = _IpadPktSwCfgnN3_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 10, 2, 1, 7),
    _IpadPktSwCfgnN3_Type()
)
ipadPktSwCfgnN3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadPktSwCfgnN3.setStatus("mandatory")
_IpadPktSwCfgnT1_Type = Integer32
_IpadPktSwCfgnT1_Object = MibTableColumn
ipadPktSwCfgnT1 = _IpadPktSwCfgnT1_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 10, 2, 1, 8),
    _IpadPktSwCfgnT1_Type()
)
ipadPktSwCfgnT1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadPktSwCfgnT1.setStatus("mandatory")
_IpadPktSwCfgDefCIR_Type = Integer32
_IpadPktSwCfgDefCIR_Object = MibTableColumn
ipadPktSwCfgDefCIR = _IpadPktSwCfgDefCIR_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 10, 2, 1, 9),
    _IpadPktSwCfgDefCIR_Type()
)
ipadPktSwCfgDefCIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadPktSwCfgDefCIR.setStatus("mandatory")
_IpadPktSwCfgDefExBurst_Type = Integer32
_IpadPktSwCfgDefExBurst_Object = MibTableColumn
ipadPktSwCfgDefExBurst = _IpadPktSwCfgDefExBurst_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 10, 2, 1, 10),
    _IpadPktSwCfgDefExBurst_Type()
)
ipadPktSwCfgDefExBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadPktSwCfgDefExBurst.setStatus("mandatory")


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
    ipadPktSwCfgCIREE.setStatus("mandatory")


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
    ipadPktSwCfgLinkInjection.setStatus("mandatory")


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
    ipadPktSwCfgAutoDiagnostic.setStatus("mandatory")


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
    ipadPktSwCfgAutoDiscovery.setStatus("mandatory")


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
    ipadPktSwCfgMgmtDLCI.setStatus("mandatory")
_IpadTrapDest_ObjectIdentity = ObjectIdentity
ipadTrapDest = _IpadTrapDest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 11)
)
_IpadTrapDestTable_Object = MibTable
ipadTrapDestTable = _IpadTrapDestTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 11, 1)
)
if mibBuilder.loadTexts:
    ipadTrapDestTable.setStatus("optional")
_IpadTrapDestTableEntry_Object = MibTableRow
ipadTrapDestTableEntry = _IpadTrapDestTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 11, 1, 1)
)
ipadTrapDestTableEntry.setIndexNames(
    (0, "IPAD-MIB", "ipadTrapDestIndex"),
)
if mibBuilder.loadTexts:
    ipadTrapDestTableEntry.setStatus("mandatory")
_IpadTrapDestIndex_Type = Integer32
_IpadTrapDestIndex_Object = MibTableColumn
ipadTrapDestIndex = _IpadTrapDestIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 11, 1, 1, 1),
    _IpadTrapDestIndex_Type()
)
ipadTrapDestIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadTrapDestIndex.setStatus("mandatory")
_IpadTrapDestination_Type = IpAddress
_IpadTrapDestination_Object = MibTableColumn
ipadTrapDestination = _IpadTrapDestination_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 11, 1, 1, 2),
    _IpadTrapDestination_Type()
)
ipadTrapDestination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadTrapDestination.setStatus("mandatory")
_IpadMisc_ObjectIdentity = ObjectIdentity
ipadMisc = _IpadMisc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 12)
)
_IpadMiscPortSettings_Object = MibTable
ipadMiscPortSettings = _IpadMiscPortSettings_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 12, 1)
)
if mibBuilder.loadTexts:
    ipadMiscPortSettings.setStatus("optional")
_IpadMiscPortSettingsEntry_Object = MibTableRow
ipadMiscPortSettingsEntry = _IpadMiscPortSettingsEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 12, 1, 1)
)
ipadMiscPortSettingsEntry.setIndexNames(
    (0, "IPAD-MIB", "ipadMiscPortSettingsIndex"),
)
if mibBuilder.loadTexts:
    ipadMiscPortSettingsEntry.setStatus("mandatory")


class _IpadMiscPortSettingsIndex_Type(Integer32):
    """Custom type ipadMiscPortSettingsIndex based on Integer32"""
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
        *(("ethernet", 6),
          ("network1", 2),
          ("network2", 3),
          ("supervisor", 1),
          ("user1", 4),
          ("user2", 5))
    )


_IpadMiscPortSettingsIndex_Type.__name__ = "Integer32"
_IpadMiscPortSettingsIndex_Object = MibTableColumn
ipadMiscPortSettingsIndex = _IpadMiscPortSettingsIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 12, 1, 1, 1),
    _IpadMiscPortSettingsIndex_Type()
)
ipadMiscPortSettingsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadMiscPortSettingsIndex.setStatus("mandatory")


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
    ipadMiscPortSettingsSerialType.setStatus("mandatory")


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
        *(("clear", 2),
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
    ipadMiscClearStatusCounts.setStatus("mandatory")
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
    ipadSoftKeyTable.setStatus("mandatory")
_IpadSoftKeyTableEntry_Object = MibTableRow
ipadSoftKeyTableEntry = _IpadSoftKeyTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 14, 1, 1)
)
ipadSoftKeyTableEntry.setIndexNames(
    (0, "IPAD-MIB", "ipadSoftKeyIndex"),
)
if mibBuilder.loadTexts:
    ipadSoftKeyTableEntry.setStatus("mandatory")
_IpadSoftKeyIndex_Type = Integer32
_IpadSoftKeyIndex_Object = MibTableColumn
ipadSoftKeyIndex = _IpadSoftKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 14, 1, 1, 1),
    _IpadSoftKeyIndex_Type()
)
ipadSoftKeyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadSoftKeyIndex.setStatus("mandatory")


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
    ipadSoftKeyAcronym.setStatus("mandatory")


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
    ipadSoftKeyDescription.setStatus("mandatory")


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
    ipadSoftKeyExpirationDate.setStatus("mandatory")


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
    ipadSoftKeyEntry.setStatus("mandatory")

# Managed Objects groups


# Notification objects

ipadFrPortRxInvalidFramesExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 100, 0, 25000)
)
if mibBuilder.loadTexts:
    ipadFrPortRxInvalidFramesExceeded.setStatus(
        ""
    )

ipadFrPortRxThroughputExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 100, 0, 25001)
)
if mibBuilder.loadTexts:
    ipadFrPortRxThroughputExceeded.setStatus(
        ""
    )

ipadFrPortTxThroughputExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 100, 0, 25002)
)
if mibBuilder.loadTexts:
    ipadFrPortTxThroughputExceeded.setStatus(
        ""
    )

ipadDLCItxCIRexceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 100, 0, 25003)
)
if mibBuilder.loadTexts:
    ipadDLCItxCIRexceeded.setStatus(
        ""
    )

ipadDLCItxBEexceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 100, 0, 25004)
)
if mibBuilder.loadTexts:
    ipadDLCItxBEexceeded.setStatus(
        ""
    )

ipadDLCIRxCongestionExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 100, 0, 25005)
)
if mibBuilder.loadTexts:
    ipadDLCIRxCongestionExceeded.setStatus(
        ""
    )

ipadUserTxExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 100, 0, 25006)
)
if mibBuilder.loadTexts:
    ipadUserTxExceeded.setStatus(
        ""
    )

ipadDlciRxBECNinCIRAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 100, 0, 25007)
)
if mibBuilder.loadTexts:
    ipadDlciRxBECNinCIRAlarm.setStatus(
        ""
    )

ipadDlciUASExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 100, 0, 25008)
)
if mibBuilder.loadTexts:
    ipadDlciUASExceeded.setStatus(
        ""
    )

ipadserialDteDTRAlarmExists = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 100, 0, 25009)
)
if mibBuilder.loadTexts:
    ipadserialDteDTRAlarmExists.setStatus(
        ""
    )

ipadt1e1ESAlarmDeclared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 100, 0, 25010)
)
if mibBuilder.loadTexts:
    ipadt1e1ESAlarmDeclared.setStatus(
        ""
    )

ipadt1e1SESAlarmDeclared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 100, 0, 25011)
)
if mibBuilder.loadTexts:
    ipadt1e1SESAlarmDeclared.setStatus(
        ""
    )

ipadt1e1LOSSAlarmDeclared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 100, 0, 25012)
)
if mibBuilder.loadTexts:
    ipadt1e1LOSSAlarmDeclared.setStatus(
        ""
    )

ipadt1e1UASAlarmDeclared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 100, 0, 25013)
)
if mibBuilder.loadTexts:
    ipadt1e1UASAlarmDeclared.setStatus(
        ""
    )

ipadt1e1CSSAlarmDeclared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 100, 0, 25014)
)
if mibBuilder.loadTexts:
    ipadt1e1CSSAlarmDeclared.setStatus(
        ""
    )

ipadt1e1BPVSAlarmDeclared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 100, 0, 25015)
)
if mibBuilder.loadTexts:
    ipadt1e1BPVSAlarmDeclared.setStatus(
        ""
    )

ipadt1e1OOFSAlarmDeclared = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 100, 0, 25016)
)
if mibBuilder.loadTexts:
    ipadt1e1OOFSAlarmDeclared.setStatus(
        ""
    )

ipadt1e1AISAlarmExists = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 100, 0, 25017)
)
if mibBuilder.loadTexts:
    ipadt1e1AISAlarmExists.setStatus(
        ""
    )

ipadt1e1RASAlarmExists = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 100, 0, 25018)
)
if mibBuilder.loadTexts:
    ipadt1e1RASAlarmExists.setStatus(
        ""
    )

ipadDLCIremoteSOSAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 100, 0, 25019)
)
if mibBuilder.loadTexts:
    ipadDLCIremoteSOSAlarm.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IPAD-MIB",
    **{"verilink": verilink,
       "hbu": hbu,
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
       "ipad": ipad,
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
       "ipadService": ipadService,
       "ipadServiceTable": ipadServiceTable,
       "ipadServiceTableEntry": ipadServiceTableEntry,
       "ipadServiceIndex": ipadServiceIndex,
       "ipadServiceifIndex": ipadServiceifIndex,
       "ipadServiceType": ipadServiceType,
       "ipadServicePair": ipadServicePair,
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
       "ipadModemDataTable": ipadModemDataTable,
       "ipadModemDataTableEntry": ipadModemDataTableEntry,
       "ipadModemDataTableIndex": ipadModemDataTableIndex,
       "ipadModemDataModemName": ipadModemDataModemName,
       "ipadModemDataSetupScript": ipadModemDataSetupScript,
       "ipadModemDataDialingScript": ipadModemDataDialingScript,
       "ipadModemDataAnswerScript": ipadModemDataAnswerScript,
       "ipadModemDataHangupScript": ipadModemDataHangupScript,
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
       "ipadMiscClearStatusCounts": ipadMiscClearStatusCounts,
       "ipadRouter": ipadRouter,
       "ipadSoftKey": ipadSoftKey,
       "ipadSoftKeyTable": ipadSoftKeyTable,
       "ipadSoftKeyTableEntry": ipadSoftKeyTableEntry,
       "ipadSoftKeyIndex": ipadSoftKeyIndex,
       "ipadSoftKeyAcronym": ipadSoftKeyAcronym,
       "ipadSoftKeyDescription": ipadSoftKeyDescription,
       "ipadSoftKeyExpirationDate": ipadSoftKeyExpirationDate,
       "ipadSoftKeyEntry": ipadSoftKeyEntry}
)
