# SNMP MIB module (GSWITCH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/GSWITCH-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:49:16 2024
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

_Nbase_ObjectIdentity = ObjectIdentity
nbase = _Nbase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629)
)
_Gswitch_ObjectIdentity = ObjectIdentity
gswitch = _Gswitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 2)
)
_NbsNPorts_Type = Integer32
_NbsNPorts_Object = MibScalar
nbsNPorts = _NbsNPorts_Object(
    (1, 3, 6, 1, 4, 1, 629, 2, 1),
    _NbsNPorts_Type()
)
nbsNPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsNPorts.setStatus("mandatory")
_NbsDevIdentify_ObjectIdentity = ObjectIdentity
nbsDevIdentify = _NbsDevIdentify_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 2, 2)
)


class _NbsUpLinkType_Type(Integer32):
    """Custom type nbsUpLinkType based on Integer32"""
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
        *(("FDDI", 15),
          ("ISDN", 12),
          ("VPN", 13),
          ("atm", 5),
          ("fast1Ethernet1000BaseGE", 14),
          ("fast2Ethernet1000BaseGE", 16),
          ("fast2Ethernet100BaseFX", 4),
          ("fast2Ethernet100BaseTX", 2),
          ("fast2Ethernet100BaseTxFx", 3),
          ("fast4Ethernet100BaseFO", 11),
          ("fast5Ethernet100BaseFX", 9),
          ("fast5Ethernet100BaseTX", 8),
          ("fast8Ethernet100BaseTP", 10),
          ("fast8Ethernet100BaseTX", 6),
          ("fast8Ethernet10or100BaseTX", 7),
          ("notExist", 1))
    )


_NbsUpLinkType_Type.__name__ = "Integer32"
_NbsUpLinkType_Object = MibScalar
nbsUpLinkType = _NbsUpLinkType_Object(
    (1, 3, 6, 1, 4, 1, 629, 2, 2, 1),
    _NbsUpLinkType_Type()
)
nbsUpLinkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsUpLinkType.setStatus("mandatory")
_NbsBaseHardVers_Type = Integer32
_NbsBaseHardVers_Object = MibScalar
nbsBaseHardVers = _NbsBaseHardVers_Object(
    (1, 3, 6, 1, 4, 1, 629, 2, 2, 3),
    _NbsBaseHardVers_Type()
)
nbsBaseHardVers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsBaseHardVers.setStatus("mandatory")
_NbsCardHardVers_Type = Integer32
_NbsCardHardVers_Object = MibScalar
nbsCardHardVers = _NbsCardHardVers_Object(
    (1, 3, 6, 1, 4, 1, 629, 2, 2, 4),
    _NbsCardHardVers_Type()
)
nbsCardHardVers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCardHardVers.setStatus("mandatory")
_NbsUpLinkHardVers_Type = Integer32
_NbsUpLinkHardVers_Object = MibScalar
nbsUpLinkHardVers = _NbsUpLinkHardVers_Object(
    (1, 3, 6, 1, 4, 1, 629, 2, 2, 5),
    _NbsUpLinkHardVers_Type()
)
nbsUpLinkHardVers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsUpLinkHardVers.setStatus("mandatory")
_NbsSoftVers_Type = Integer32
_NbsSoftVers_Object = MibScalar
nbsSoftVers = _NbsSoftVers_Object(
    (1, 3, 6, 1, 4, 1, 629, 2, 2, 6),
    _NbsSoftVers_Type()
)
nbsSoftVers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSoftVers.setStatus("mandatory")
_NbsSnifferPort_Type = Integer32
_NbsSnifferPort_Object = MibScalar
nbsSnifferPort = _NbsSnifferPort_Object(
    (1, 3, 6, 1, 4, 1, 629, 2, 2, 9),
    _NbsSnifferPort_Type()
)
nbsSnifferPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSnifferPort.setStatus("mandatory")
_NbsCreatinDate_Type = DisplayString
_NbsCreatinDate_Object = MibScalar
nbsCreatinDate = _NbsCreatinDate_Object(
    (1, 3, 6, 1, 4, 1, 629, 2, 2, 10),
    _NbsCreatinDate_Type()
)
nbsCreatinDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCreatinDate.setStatus("mandatory")
_NbsDeviceControl_ObjectIdentity = ObjectIdentity
nbsDeviceControl = _NbsDeviceControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 2, 3)
)


class _NbsSpanningTree_Type(Integer32):
    """Custom type nbsSpanningTree based on Integer32"""
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


_NbsSpanningTree_Type.__name__ = "Integer32"
_NbsSpanningTree_Object = MibScalar
nbsSpanningTree = _NbsSpanningTree_Object(
    (1, 3, 6, 1, 4, 1, 629, 2, 3, 6),
    _NbsSpanningTree_Type()
)
nbsSpanningTree.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsSpanningTree.setStatus("mandatory")


class _NbsLearningProcess_Type(Integer32):
    """Custom type nbsLearningProcess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_NbsLearningProcess_Type.__name__ = "Integer32"
_NbsLearningProcess_Object = MibScalar
nbsLearningProcess = _NbsLearningProcess_Object(
    (1, 3, 6, 1, 4, 1, 629, 2, 3, 7),
    _NbsLearningProcess_Type()
)
nbsLearningProcess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsLearningProcess.setStatus("mandatory")


class _NbsParitionEnable_Type(Integer32):
    """Custom type nbsParitionEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_NbsParitionEnable_Type.__name__ = "Integer32"
_NbsParitionEnable_Object = MibScalar
nbsParitionEnable = _NbsParitionEnable_Object(
    (1, 3, 6, 1, 4, 1, 629, 2, 3, 8),
    _NbsParitionEnable_Type()
)
nbsParitionEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsParitionEnable.setStatus("mandatory")


class _NbsRMONmode_Type(Integer32):
    """Custom type nbsRMONmode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_NbsRMONmode_Type.__name__ = "Integer32"
_NbsRMONmode_Object = MibScalar
nbsRMONmode = _NbsRMONmode_Object(
    (1, 3, 6, 1, 4, 1, 629, 2, 3, 9),
    _NbsRMONmode_Type()
)
nbsRMONmode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsRMONmode.setStatus("mandatory")


class _NbsBufferThreshold_Type(Integer32):
    """Custom type nbsBufferThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("limited", 1),
          ("not-limited", 2))
    )


_NbsBufferThreshold_Type.__name__ = "Integer32"
_NbsBufferThreshold_Object = MibScalar
nbsBufferThreshold = _NbsBufferThreshold_Object(
    (1, 3, 6, 1, 4, 1, 629, 2, 3, 10),
    _NbsBufferThreshold_Type()
)
nbsBufferThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsBufferThreshold.setStatus("mandatory")


class _NbsForwardMulticast_Type(Integer32):
    """Custom type nbsForwardMulticast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_NbsForwardMulticast_Type.__name__ = "Integer32"
_NbsForwardMulticast_Object = MibScalar
nbsForwardMulticast = _NbsForwardMulticast_Object(
    (1, 3, 6, 1, 4, 1, 629, 2, 3, 12),
    _NbsForwardMulticast_Type()
)
nbsForwardMulticast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsForwardMulticast.setStatus("mandatory")


class _NbsForwardUnkPkts_Type(Integer32):
    """Custom type nbsForwardUnkPkts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_NbsForwardUnkPkts_Type.__name__ = "Integer32"
_NbsForwardUnkPkts_Object = MibScalar
nbsForwardUnkPkts = _NbsForwardUnkPkts_Object(
    (1, 3, 6, 1, 4, 1, 629, 2, 3, 15),
    _NbsForwardUnkPkts_Type()
)
nbsForwardUnkPkts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsForwardUnkPkts.setStatus("mandatory")


class _NbsBackOffMode_Type(Integer32):
    """Custom type nbsBackOffMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aggressive", 2),
          ("normal", 1))
    )


_NbsBackOffMode_Type.__name__ = "Integer32"
_NbsBackOffMode_Object = MibScalar
nbsBackOffMode = _NbsBackOffMode_Object(
    (1, 3, 6, 1, 4, 1, 629, 2, 3, 16),
    _NbsBackOffMode_Type()
)
nbsBackOffMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsBackOffMode.setStatus("mandatory")
_NbsPortsControl_ObjectIdentity = ObjectIdentity
nbsPortsControl = _NbsPortsControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 2, 5)
)
_NbsPortsContTable_Object = MibTable
nbsPortsContTable = _NbsPortsContTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 2, 5, 1)
)
if mibBuilder.loadTexts:
    nbsPortsContTable.setStatus("mandatory")
_NbsPortsContEntry_Object = MibTableRow
nbsPortsContEntry = _NbsPortsContEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 2, 5, 1, 1)
)
nbsPortsContEntry.setIndexNames(
    (0, "GSWITCH-MIB", "nbsPortIndex1"),
)
if mibBuilder.loadTexts:
    nbsPortsContEntry.setStatus("mandatory")
_NbsPortIndex1_Type = Integer32
_NbsPortIndex1_Object = MibTableColumn
nbsPortIndex1 = _NbsPortIndex1_Object(
    (1, 3, 6, 1, 4, 1, 629, 2, 5, 1, 1, 1),
    _NbsPortIndex1_Type()
)
nbsPortIndex1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsPortIndex1.setStatus("mandatory")


class _NbsPortEnable_Type(Integer32):
    """Custom type nbsPortEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_NbsPortEnable_Type.__name__ = "Integer32"
_NbsPortEnable_Object = MibTableColumn
nbsPortEnable = _NbsPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 629, 2, 5, 1, 1, 2),
    _NbsPortEnable_Type()
)
nbsPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsPortEnable.setStatus("mandatory")


class _NbsPortDuplex_Type(Integer32):
    """Custom type nbsPortDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("full", 2),
          ("half", 1))
    )


_NbsPortDuplex_Type.__name__ = "Integer32"
_NbsPortDuplex_Object = MibTableColumn
nbsPortDuplex = _NbsPortDuplex_Object(
    (1, 3, 6, 1, 4, 1, 629, 2, 5, 1, 1, 3),
    _NbsPortDuplex_Type()
)
nbsPortDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsPortDuplex.setStatus("mandatory")


class _NbsPortMonitor_Type(Integer32):
    """Custom type nbsPortMonitor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("sniffer", 2))
    )


_NbsPortMonitor_Type.__name__ = "Integer32"
_NbsPortMonitor_Object = MibTableColumn
nbsPortMonitor = _NbsPortMonitor_Object(
    (1, 3, 6, 1, 4, 1, 629, 2, 5, 1, 1, 5),
    _NbsPortMonitor_Type()
)
nbsPortMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsPortMonitor.setStatus("mandatory")


class _NbsPortPolDetection_Type(Integer32):
    """Custom type nbsPortPolDetection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabel", 2),
          ("enable", 1))
    )


_NbsPortPolDetection_Type.__name__ = "Integer32"
_NbsPortPolDetection_Object = MibTableColumn
nbsPortPolDetection = _NbsPortPolDetection_Object(
    (1, 3, 6, 1, 4, 1, 629, 2, 5, 1, 1, 6),
    _NbsPortPolDetection_Type()
)
nbsPortPolDetection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsPortPolDetection.setStatus("mandatory")


class _NbsPortBroadcast_Type(Integer32):
    """Custom type nbsPortBroadcast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discard", 2),
          ("forward", 1))
    )


_NbsPortBroadcast_Type.__name__ = "Integer32"
_NbsPortBroadcast_Object = MibTableColumn
nbsPortBroadcast = _NbsPortBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 629, 2, 5, 1, 1, 7),
    _NbsPortBroadcast_Type()
)
nbsPortBroadcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsPortBroadcast.setStatus("mandatory")


class _NbsPortForwardUnk_Type(Integer32):
    """Custom type nbsPortForwardUnk based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discard", 2),
          ("forward", 1))
    )


_NbsPortForwardUnk_Type.__name__ = "Integer32"
_NbsPortForwardUnk_Object = MibTableColumn
nbsPortForwardUnk = _NbsPortForwardUnk_Object(
    (1, 3, 6, 1, 4, 1, 629, 2, 5, 1, 1, 8),
    _NbsPortForwardUnk_Type()
)
nbsPortForwardUnk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsPortForwardUnk.setStatus("mandatory")


class _NbsPortSpaning_Type(Integer32):
    """Custom type nbsPortSpaning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("discard", 2))
    )


_NbsPortSpaning_Type.__name__ = "Integer32"
_NbsPortSpaning_Object = MibTableColumn
nbsPortSpaning = _NbsPortSpaning_Object(
    (1, 3, 6, 1, 4, 1, 629, 2, 5, 1, 1, 9),
    _NbsPortSpaning_Type()
)
nbsPortSpaning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsPortSpaning.setStatus("mandatory")


class _NbsPortSpeed_Type(Integer32):
    """Custom type nbsPortSpeed based on Integer32"""
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
        *(("none", 1),
          ("s10000MBps", 5),
          ("s1000MBps", 4),
          ("s100MBps", 3),
          ("s10MBps", 2))
    )


_NbsPortSpeed_Type.__name__ = "Integer32"
_NbsPortSpeed_Object = MibTableColumn
nbsPortSpeed = _NbsPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 629, 2, 5, 1, 1, 10),
    _NbsPortSpeed_Type()
)
nbsPortSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsPortSpeed.setStatus("mandatory")
_NbsPortsStatus_ObjectIdentity = ObjectIdentity
nbsPortsStatus = _NbsPortsStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 2, 6)
)
_NbsPortsStatTable_Object = MibTable
nbsPortsStatTable = _NbsPortsStatTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 2, 6, 1)
)
if mibBuilder.loadTexts:
    nbsPortsStatTable.setStatus("mandatory")
_NbsPortsStatEntry_Object = MibTableRow
nbsPortsStatEntry = _NbsPortsStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 2, 6, 1, 1)
)
nbsPortsStatEntry.setIndexNames(
    (0, "GSWITCH-MIB", "nbsPortIndex"),
)
if mibBuilder.loadTexts:
    nbsPortsStatEntry.setStatus("mandatory")
_NbsPortIndex_Type = Integer32
_NbsPortIndex_Object = MibTableColumn
nbsPortIndex = _NbsPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 2, 6, 1, 1, 1),
    _NbsPortIndex_Type()
)
nbsPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsPortIndex.setStatus("mandatory")


class _NbsPortType_Type(Integer32):
    """Custom type nbsPortType based on Integer32"""
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
        *(("empty", 1),
          ("fastCopper", 3),
          ("fastFiber", 4),
          ("gigaCopper", 6),
          ("normal", 2),
          ("slowFiber", 5))
    )


_NbsPortType_Type.__name__ = "Integer32"
_NbsPortType_Object = MibTableColumn
nbsPortType = _NbsPortType_Object(
    (1, 3, 6, 1, 4, 1, 629, 2, 6, 1, 1, 2),
    _NbsPortType_Type()
)
nbsPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsPortType.setStatus("mandatory")


class _NbsPartition_Type(Integer32):
    """Custom type nbsPartition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_NbsPartition_Type.__name__ = "Integer32"
_NbsPartition_Object = MibTableColumn
nbsPartition = _NbsPartition_Object(
    (1, 3, 6, 1, 4, 1, 629, 2, 6, 1, 1, 3),
    _NbsPartition_Type()
)
nbsPartition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsPartition.setStatus("mandatory")


class _NbsLinkTest_Type(Integer32):
    """Custom type nbsLinkTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fail", 2),
          ("pass", 1))
    )


_NbsLinkTest_Type.__name__ = "Integer32"
_NbsLinkTest_Object = MibTableColumn
nbsLinkTest = _NbsLinkTest_Object(
    (1, 3, 6, 1, 4, 1, 629, 2, 6, 1, 1, 4),
    _NbsLinkTest_Type()
)
nbsLinkTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsLinkTest.setStatus("mandatory")
_NbsPortsCounters_ObjectIdentity = ObjectIdentity
nbsPortsCounters = _NbsPortsCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 2, 7)
)
_NbsPortsCountTable_Object = MibTable
nbsPortsCountTable = _NbsPortsCountTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 2, 7, 1)
)
if mibBuilder.loadTexts:
    nbsPortsCountTable.setStatus("mandatory")
_NbsPortsCountEntry_Object = MibTableRow
nbsPortsCountEntry = _NbsPortsCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 2, 7, 1, 1)
)
nbsPortsCountEntry.setIndexNames(
    (0, "GSWITCH-MIB", "nbsPortIndex2"),
)
if mibBuilder.loadTexts:
    nbsPortsCountEntry.setStatus("mandatory")
_NbsPortIndex2_Type = Integer32
_NbsPortIndex2_Object = MibTableColumn
nbsPortIndex2 = _NbsPortIndex2_Object(
    (1, 3, 6, 1, 4, 1, 629, 2, 7, 1, 1, 1),
    _NbsPortIndex2_Type()
)
nbsPortIndex2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsPortIndex2.setStatus("mandatory")
_NbsPortByteRec_Type = Counter32
_NbsPortByteRec_Object = MibTableColumn
nbsPortByteRec = _NbsPortByteRec_Object(
    (1, 3, 6, 1, 4, 1, 629, 2, 7, 1, 1, 2),
    _NbsPortByteRec_Type()
)
nbsPortByteRec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsPortByteRec.setStatus("mandatory")
_NbsPortMulByteRec_Type = Counter32
_NbsPortMulByteRec_Object = MibTableColumn
nbsPortMulByteRec = _NbsPortMulByteRec_Object(
    (1, 3, 6, 1, 4, 1, 629, 2, 7, 1, 1, 3),
    _NbsPortMulByteRec_Type()
)
nbsPortMulByteRec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsPortMulByteRec.setStatus("mandatory")
_NbsPortBroadByteRec_Type = Counter32
_NbsPortBroadByteRec_Object = MibTableColumn
nbsPortBroadByteRec = _NbsPortBroadByteRec_Object(
    (1, 3, 6, 1, 4, 1, 629, 2, 7, 1, 1, 4),
    _NbsPortBroadByteRec_Type()
)
nbsPortBroadByteRec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsPortBroadByteRec.setStatus("mandatory")
_NbsPortByteSent_Type = Counter32
_NbsPortByteSent_Object = MibTableColumn
nbsPortByteSent = _NbsPortByteSent_Object(
    (1, 3, 6, 1, 4, 1, 629, 2, 7, 1, 1, 5),
    _NbsPortByteSent_Type()
)
nbsPortByteSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsPortByteSent.setStatus("mandatory")
_NbsPortFramesRec_Type = Counter32
_NbsPortFramesRec_Object = MibTableColumn
nbsPortFramesRec = _NbsPortFramesRec_Object(
    (1, 3, 6, 1, 4, 1, 629, 2, 7, 1, 1, 6),
    _NbsPortFramesRec_Type()
)
nbsPortFramesRec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsPortFramesRec.setStatus("mandatory")
_NbsPortMulFramesRec_Type = Counter32
_NbsPortMulFramesRec_Object = MibTableColumn
nbsPortMulFramesRec = _NbsPortMulFramesRec_Object(
    (1, 3, 6, 1, 4, 1, 629, 2, 7, 1, 1, 7),
    _NbsPortMulFramesRec_Type()
)
nbsPortMulFramesRec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsPortMulFramesRec.setStatus("mandatory")
_NbsPortBroadFramesRec_Type = Counter32
_NbsPortBroadFramesRec_Object = MibTableColumn
nbsPortBroadFramesRec = _NbsPortBroadFramesRec_Object(
    (1, 3, 6, 1, 4, 1, 629, 2, 7, 1, 1, 8),
    _NbsPortBroadFramesRec_Type()
)
nbsPortBroadFramesRec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsPortBroadFramesRec.setStatus("mandatory")
_NbsPortFramesSent_Type = Counter32
_NbsPortFramesSent_Object = MibTableColumn
nbsPortFramesSent = _NbsPortFramesSent_Object(
    (1, 3, 6, 1, 4, 1, 629, 2, 7, 1, 1, 9),
    _NbsPortFramesSent_Type()
)
nbsPortFramesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsPortFramesSent.setStatus("mandatory")
_NbsPortCollisions_Type = Counter32
_NbsPortCollisions_Object = MibTableColumn
nbsPortCollisions = _NbsPortCollisions_Object(
    (1, 3, 6, 1, 4, 1, 629, 2, 7, 1, 1, 10),
    _NbsPortCollisions_Type()
)
nbsPortCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsPortCollisions.setStatus("mandatory")
_NbsPortLateColl_Type = Counter32
_NbsPortLateColl_Object = MibTableColumn
nbsPortLateColl = _NbsPortLateColl_Object(
    (1, 3, 6, 1, 4, 1, 629, 2, 7, 1, 1, 11),
    _NbsPortLateColl_Type()
)
nbsPortLateColl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsPortLateColl.setStatus("mandatory")
_NbsPortCRCAligErr_Type = Counter32
_NbsPortCRCAligErr_Object = MibTableColumn
nbsPortCRCAligErr = _NbsPortCRCAligErr_Object(
    (1, 3, 6, 1, 4, 1, 629, 2, 7, 1, 1, 12),
    _NbsPortCRCAligErr_Type()
)
nbsPortCRCAligErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsPortCRCAligErr.setStatus("mandatory")
_NbsPortFramesShort_Type = Counter32
_NbsPortFramesShort_Object = MibTableColumn
nbsPortFramesShort = _NbsPortFramesShort_Object(
    (1, 3, 6, 1, 4, 1, 629, 2, 7, 1, 1, 13),
    _NbsPortFramesShort_Type()
)
nbsPortFramesShort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsPortFramesShort.setStatus("mandatory")
_NbsPortFrameLong_Type = Counter32
_NbsPortFrameLong_Object = MibTableColumn
nbsPortFrameLong = _NbsPortFrameLong_Object(
    (1, 3, 6, 1, 4, 1, 629, 2, 7, 1, 1, 14),
    _NbsPortFrameLong_Type()
)
nbsPortFrameLong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsPortFrameLong.setStatus("mandatory")
_NbsPortJabber_Type = Counter32
_NbsPortJabber_Object = MibTableColumn
nbsPortJabber = _NbsPortJabber_Object(
    (1, 3, 6, 1, 4, 1, 629, 2, 7, 1, 1, 15),
    _NbsPortJabber_Type()
)
nbsPortJabber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsPortJabber.setStatus("mandatory")
_NbsPortBadByteRec_Type = Counter32
_NbsPortBadByteRec_Object = MibTableColumn
nbsPortBadByteRec = _NbsPortBadByteRec_Object(
    (1, 3, 6, 1, 4, 1, 629, 2, 7, 1, 1, 16),
    _NbsPortBadByteRec_Type()
)
nbsPortBadByteRec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsPortBadByteRec.setStatus("mandatory")
_NbsAddressTable_ObjectIdentity = ObjectIdentity
nbsAddressTable = _NbsAddressTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 2, 8)
)
_NbsMACAddrTable_Object = MibTable
nbsMACAddrTable = _NbsMACAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 2, 8, 1)
)
if mibBuilder.loadTexts:
    nbsMACAddrTable.setStatus("mandatory")
_NbsMACAddrEntry_Object = MibTableRow
nbsMACAddrEntry = _NbsMACAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 2, 8, 1, 1)
)
nbsMACAddrEntry.setIndexNames(
    (0, "GSWITCH-MIB", "nbsAddrIndex"),
)
if mibBuilder.loadTexts:
    nbsMACAddrEntry.setStatus("mandatory")
_NbsAddrIndex_Type = Integer32
_NbsAddrIndex_Object = MibTableColumn
nbsAddrIndex = _NbsAddrIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 2, 8, 1, 1, 1),
    _NbsAddrIndex_Type()
)
nbsAddrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsAddrIndex.setStatus("mandatory")


class _NbsMACAddress_Type(OctetString):
    """Custom type nbsMACAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_NbsMACAddress_Type.__name__ = "OctetString"
_NbsMACAddress_Object = MibTableColumn
nbsMACAddress = _NbsMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 629, 2, 8, 1, 1, 3),
    _NbsMACAddress_Type()
)
nbsMACAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsMACAddress.setStatus("mandatory")
_NbsAddrPort_Type = Integer32
_NbsAddrPort_Object = MibTableColumn
nbsAddrPort = _NbsAddrPort_Object(
    (1, 3, 6, 1, 4, 1, 629, 2, 8, 1, 1, 4),
    _NbsAddrPort_Type()
)
nbsAddrPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsAddrPort.setStatus("mandatory")


class _NbsAddrStatic_Type(Integer32):
    """Custom type nbsAddrStatic based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_NbsAddrStatic_Type.__name__ = "Integer32"
_NbsAddrStatic_Object = MibTableColumn
nbsAddrStatic = _NbsAddrStatic_Object(
    (1, 3, 6, 1, 4, 1, 629, 2, 8, 1, 1, 5),
    _NbsAddrStatic_Type()
)
nbsAddrStatic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsAddrStatic.setStatus("mandatory")


class _NbsAddrForwardTo_Type(Integer32):
    """Custom type nbsAddrForwardTo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("all-ports", 2),
          ("destination-port", 1))
    )


_NbsAddrForwardTo_Type.__name__ = "Integer32"
_NbsAddrForwardTo_Object = MibTableColumn
nbsAddrForwardTo = _NbsAddrForwardTo_Object(
    (1, 3, 6, 1, 4, 1, 629, 2, 8, 1, 1, 6),
    _NbsAddrForwardTo_Type()
)
nbsAddrForwardTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsAddrForwardTo.setStatus("mandatory")
_NbsSlotsTable_ObjectIdentity = ObjectIdentity
nbsSlotsTable = _NbsSlotsTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 2, 9)
)
_NbsCardsTable_Object = MibTable
nbsCardsTable = _NbsCardsTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 2, 9, 1)
)
if mibBuilder.loadTexts:
    nbsCardsTable.setStatus("mandatory")
_NbsCardsEntry_Object = MibTableRow
nbsCardsEntry = _NbsCardsEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 2, 9, 1, 1)
)
nbsCardsEntry.setIndexNames(
    (0, "GSWITCH-MIB", "nbsAddrIndex"),
)
if mibBuilder.loadTexts:
    nbsCardsEntry.setStatus("mandatory")
_NbsCardIndex_Type = Integer32
_NbsCardIndex_Object = MibTableColumn
nbsCardIndex = _NbsCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 2, 9, 1, 1, 1),
    _NbsCardIndex_Type()
)
nbsCardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCardIndex.setStatus("mandatory")


class _NbsCardType_Type(Integer32):
    """Custom type nbsCardType based on Integer32"""
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
        *(("copper20Ethernet10or100Base", 2),
          ("copper40Ethernet10Base", 3),
          ("emptySlot", 1),
          ("fansUnitError", 7),
          ("fansUnitOK", 8),
          ("fibre10Ethernet100Base", 6),
          ("powerSupplyError", 4),
          ("powerSupplyOK", 5),
          ("universal", 9))
    )


_NbsCardType_Type.__name__ = "Integer32"
_NbsCardType_Object = MibTableColumn
nbsCardType = _NbsCardType_Object(
    (1, 3, 6, 1, 4, 1, 629, 2, 9, 1, 1, 2),
    _NbsCardType_Type()
)
nbsCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCardType.setStatus("mandatory")
_NbsNMacRecords_Type = Integer32
_NbsNMacRecords_Object = MibScalar
nbsNMacRecords = _NbsNMacRecords_Object(
    (1, 3, 6, 1, 4, 1, 629, 2, 10),
    _NbsNMacRecords_Type()
)
nbsNMacRecords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsNMacRecords.setStatus("mandatory")
_NbsMacFirstGap_Type = Integer32
_NbsMacFirstGap_Object = MibScalar
nbsMacFirstGap = _NbsMacFirstGap_Object(
    (1, 3, 6, 1, 4, 1, 629, 2, 11),
    _NbsMacFirstGap_Type()
)
nbsMacFirstGap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsMacFirstGap.setStatus("mandatory")
_NbsPALPorts_ObjectIdentity = ObjectIdentity
nbsPALPorts = _NbsPALPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 2, 12)
)
_NbsPALPortsTable_Object = MibTable
nbsPALPortsTable = _NbsPALPortsTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 2, 12, 1)
)
if mibBuilder.loadTexts:
    nbsPALPortsTable.setStatus("mandatory")
_NbsPALPortsEntry_Object = MibTableRow
nbsPALPortsEntry = _NbsPALPortsEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 2, 12, 1, 1)
)
nbsPALPortsEntry.setIndexNames(
    (0, "GSWITCH-MIB", "nbsPALPortIndex"),
)
if mibBuilder.loadTexts:
    nbsPALPortsEntry.setStatus("mandatory")
_NbsPALPortIndex_Type = Integer32
_NbsPALPortIndex_Object = MibTableColumn
nbsPALPortIndex = _NbsPALPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 2, 12, 1, 1, 1),
    _NbsPALPortIndex_Type()
)
nbsPALPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsPALPortIndex.setStatus("mandatory")
_NbsPALPortOpticPower_Type = Integer32
_NbsPALPortOpticPower_Object = MibTableColumn
nbsPALPortOpticPower = _NbsPALPortOpticPower_Object(
    (1, 3, 6, 1, 4, 1, 629, 2, 12, 1, 1, 2),
    _NbsPALPortOpticPower_Type()
)
nbsPALPortOpticPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsPALPortOpticPower.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GSWITCH-MIB",
    **{"nbase": nbase,
       "gswitch": gswitch,
       "nbsNPorts": nbsNPorts,
       "nbsDevIdentify": nbsDevIdentify,
       "nbsUpLinkType": nbsUpLinkType,
       "nbsBaseHardVers": nbsBaseHardVers,
       "nbsCardHardVers": nbsCardHardVers,
       "nbsUpLinkHardVers": nbsUpLinkHardVers,
       "nbsSoftVers": nbsSoftVers,
       "nbsSnifferPort": nbsSnifferPort,
       "nbsCreatinDate": nbsCreatinDate,
       "nbsDeviceControl": nbsDeviceControl,
       "nbsSpanningTree": nbsSpanningTree,
       "nbsLearningProcess": nbsLearningProcess,
       "nbsParitionEnable": nbsParitionEnable,
       "nbsRMONmode": nbsRMONmode,
       "nbsBufferThreshold": nbsBufferThreshold,
       "nbsForwardMulticast": nbsForwardMulticast,
       "nbsForwardUnkPkts": nbsForwardUnkPkts,
       "nbsBackOffMode": nbsBackOffMode,
       "nbsPortsControl": nbsPortsControl,
       "nbsPortsContTable": nbsPortsContTable,
       "nbsPortsContEntry": nbsPortsContEntry,
       "nbsPortIndex1": nbsPortIndex1,
       "nbsPortEnable": nbsPortEnable,
       "nbsPortDuplex": nbsPortDuplex,
       "nbsPortMonitor": nbsPortMonitor,
       "nbsPortPolDetection": nbsPortPolDetection,
       "nbsPortBroadcast": nbsPortBroadcast,
       "nbsPortForwardUnk": nbsPortForwardUnk,
       "nbsPortSpaning": nbsPortSpaning,
       "nbsPortSpeed": nbsPortSpeed,
       "nbsPortsStatus": nbsPortsStatus,
       "nbsPortsStatTable": nbsPortsStatTable,
       "nbsPortsStatEntry": nbsPortsStatEntry,
       "nbsPortIndex": nbsPortIndex,
       "nbsPortType": nbsPortType,
       "nbsPartition": nbsPartition,
       "nbsLinkTest": nbsLinkTest,
       "nbsPortsCounters": nbsPortsCounters,
       "nbsPortsCountTable": nbsPortsCountTable,
       "nbsPortsCountEntry": nbsPortsCountEntry,
       "nbsPortIndex2": nbsPortIndex2,
       "nbsPortByteRec": nbsPortByteRec,
       "nbsPortMulByteRec": nbsPortMulByteRec,
       "nbsPortBroadByteRec": nbsPortBroadByteRec,
       "nbsPortByteSent": nbsPortByteSent,
       "nbsPortFramesRec": nbsPortFramesRec,
       "nbsPortMulFramesRec": nbsPortMulFramesRec,
       "nbsPortBroadFramesRec": nbsPortBroadFramesRec,
       "nbsPortFramesSent": nbsPortFramesSent,
       "nbsPortCollisions": nbsPortCollisions,
       "nbsPortLateColl": nbsPortLateColl,
       "nbsPortCRCAligErr": nbsPortCRCAligErr,
       "nbsPortFramesShort": nbsPortFramesShort,
       "nbsPortFrameLong": nbsPortFrameLong,
       "nbsPortJabber": nbsPortJabber,
       "nbsPortBadByteRec": nbsPortBadByteRec,
       "nbsAddressTable": nbsAddressTable,
       "nbsMACAddrTable": nbsMACAddrTable,
       "nbsMACAddrEntry": nbsMACAddrEntry,
       "nbsAddrIndex": nbsAddrIndex,
       "nbsMACAddress": nbsMACAddress,
       "nbsAddrPort": nbsAddrPort,
       "nbsAddrStatic": nbsAddrStatic,
       "nbsAddrForwardTo": nbsAddrForwardTo,
       "nbsSlotsTable": nbsSlotsTable,
       "nbsCardsTable": nbsCardsTable,
       "nbsCardsEntry": nbsCardsEntry,
       "nbsCardIndex": nbsCardIndex,
       "nbsCardType": nbsCardType,
       "nbsNMacRecords": nbsNMacRecords,
       "nbsMacFirstGap": nbsMacFirstGap,
       "nbsPALPorts": nbsPALPorts,
       "nbsPALPortsTable": nbsPALPortsTable,
       "nbsPALPortsEntry": nbsPALPortsEntry,
       "nbsPALPortIndex": nbsPALPortIndex,
       "nbsPALPortOpticPower": nbsPALPortOpticPower}
)
