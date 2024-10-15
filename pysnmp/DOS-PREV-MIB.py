# SNMP MIB module (DOS-PREV-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DOS-PREV-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:33:10 2024
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

(dlink_common_mgmt,) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "dlink-common-mgmt")

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
 MacAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

swDoSMgmtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 59)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SwDoSCtrl_ObjectIdentity = ObjectIdentity
swDoSCtrl = _SwDoSCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 59, 1)
)


class _SwDoSTrapLog_Type(Integer32):
    """Custom type swDoSTrapLog based on Integer32"""
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
          ("enable", 1),
          ("other", 3))
    )


_SwDoSTrapLog_Type.__name__ = "Integer32"
_SwDoSTrapLog_Object = MibScalar
swDoSTrapLog = _SwDoSTrapLog_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 59, 1, 1),
    _SwDoSTrapLog_Type()
)
swDoSTrapLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swDoSTrapLog.setStatus("current")


class _SwDoSClearCounters_Type(Integer32):
    """Custom type swDoSClearCounters based on Integer32"""
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
              23)
        )
    )
    namedValues = NamedValues(
        *(("all", 8),
          ("arp-mac-sa-mismatch", 10),
          ("blat-attack", 2),
          ("fraggle-attack", 11),
          ("icmp-redirect-attack", 12),
          ("icmp-unreachable-attack", 13),
          ("ip-route-record-attac", 14),
          ("ip-source-route-attack", 15),
          ("land-attack", 1),
          ("other", 9),
          ("ping-death-attack", 16),
          ("smurf-attack", 3),
          ("tcp-flag-synrst", 17),
          ("tcp-null-scan", 4),
          ("tcp-over-mac-mcbc", 18),
          ("tcp-syn-srcport-less-1024", 7),
          ("tcp-syn-with-data", 19),
          ("tcp-synfin", 6),
          ("tcp-tiny-frag-attack", 20),
          ("tcp-xmascan", 5),
          ("tcpudp-port-zero", 21),
          ("tracert-attack", 22),
          ("winnuke-attack", 23))
    )


_SwDoSClearCounters_Type.__name__ = "Integer32"
_SwDoSClearCounters_Object = MibScalar
swDoSClearCounters = _SwDoSClearCounters_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 59, 1, 2),
    _SwDoSClearCounters_Type()
)
swDoSClearCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swDoSClearCounters.setStatus("current")
_SwDoSCtrlTable_Object = MibTable
swDoSCtrlTable = _SwDoSCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 59, 1, 3)
)
if mibBuilder.loadTexts:
    swDoSCtrlTable.setStatus("current")
_SwDoSCtrlEntry_Object = MibTableRow
swDoSCtrlEntry = _SwDoSCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 59, 1, 3, 1)
)
swDoSCtrlEntry.setIndexNames(
    (0, "DOS-PREV-MIB", "swDoSCtrlType"),
)
if mibBuilder.loadTexts:
    swDoSCtrlEntry.setStatus("current")


class _SwDoSCtrlType_Type(Integer32):
    """Custom type swDoSCtrlType based on Integer32"""
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
              23)
        )
    )
    namedValues = NamedValues(
        *(("arp-mac-sa-mismatch", 10),
          ("blat-attack", 2),
          ("fraggle-attack", 11),
          ("icmp-redirect-attack", 12),
          ("icmp-unreachable-attack", 13),
          ("ip-route-record-attac", 14),
          ("ip-source-route-attack", 15),
          ("land-attack", 1),
          ("ping-death-attack", 16),
          ("smurf-attack", 3),
          ("tcp-flag-synrst", 17),
          ("tcp-null-scan", 4),
          ("tcp-over-mac-mcbc", 18),
          ("tcp-syn-srcport-less-1024", 7),
          ("tcp-syn-with-data", 19),
          ("tcp-synfin", 6),
          ("tcp-tiny-frag-attack", 20),
          ("tcp-xmascan", 5),
          ("tcpudp-port-zero", 21),
          ("tracert-attack", 22),
          ("winnuke-attack", 23))
    )


_SwDoSCtrlType_Type.__name__ = "Integer32"
_SwDoSCtrlType_Object = MibTableColumn
swDoSCtrlType = _SwDoSCtrlType_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 59, 1, 3, 1, 1),
    _SwDoSCtrlType_Type()
)
swDoSCtrlType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDoSCtrlType.setStatus("current")


class _SwDoSCtrlState_Type(Integer32):
    """Custom type swDoSCtrlState based on Integer32"""
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


_SwDoSCtrlState_Type.__name__ = "Integer32"
_SwDoSCtrlState_Object = MibTableColumn
swDoSCtrlState = _SwDoSCtrlState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 59, 1, 3, 1, 2),
    _SwDoSCtrlState_Type()
)
swDoSCtrlState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swDoSCtrlState.setStatus("current")


class _SwDoSCtrlActionType_Type(Integer32):
    """Custom type swDoSCtrlActionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("drop", 1),
          ("mirror", 2))
    )


_SwDoSCtrlActionType_Type.__name__ = "Integer32"
_SwDoSCtrlActionType_Object = MibTableColumn
swDoSCtrlActionType = _SwDoSCtrlActionType_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 59, 1, 3, 1, 3),
    _SwDoSCtrlActionType_Type()
)
swDoSCtrlActionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swDoSCtrlActionType.setStatus("current")


class _SwDoSCtrlMirrorPort_Type(Integer32):
    """Custom type swDoSCtrlMirrorPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwDoSCtrlMirrorPort_Type.__name__ = "Integer32"
_SwDoSCtrlMirrorPort_Object = MibTableColumn
swDoSCtrlMirrorPort = _SwDoSCtrlMirrorPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 59, 1, 3, 1, 4),
    _SwDoSCtrlMirrorPort_Type()
)
swDoSCtrlMirrorPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swDoSCtrlMirrorPort.setStatus("current")


class _SwDoSCtrlMirrorPriority_Type(Integer32):
    """Custom type swDoSCtrlMirrorPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_SwDoSCtrlMirrorPriority_Type.__name__ = "Integer32"
_SwDoSCtrlMirrorPriority_Object = MibTableColumn
swDoSCtrlMirrorPriority = _SwDoSCtrlMirrorPriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 59, 1, 3, 1, 5),
    _SwDoSCtrlMirrorPriority_Type()
)
swDoSCtrlMirrorPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swDoSCtrlMirrorPriority.setStatus("current")


class _SwDoSCtrlMirrorRxRate_Type(Integer32):
    """Custom type swDoSCtrlMirrorRxRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024000),
    )


_SwDoSCtrlMirrorRxRate_Type.__name__ = "Integer32"
_SwDoSCtrlMirrorRxRate_Object = MibTableColumn
swDoSCtrlMirrorRxRate = _SwDoSCtrlMirrorRxRate_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 59, 1, 3, 1, 6),
    _SwDoSCtrlMirrorRxRate_Type()
)
swDoSCtrlMirrorRxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swDoSCtrlMirrorRxRate.setStatus("current")
_SwDoSCtrlFrameCount_Type = Integer32
_SwDoSCtrlFrameCount_Object = MibTableColumn
swDoSCtrlFrameCount = _SwDoSCtrlFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 59, 1, 3, 1, 7),
    _SwDoSCtrlFrameCount_Type()
)
swDoSCtrlFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDoSCtrlFrameCount.setStatus("current")


class _SwDoSTrapState_Type(Integer32):
    """Custom type swDoSTrapState based on Integer32"""
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


_SwDoSTrapState_Type.__name__ = "Integer32"
_SwDoSTrapState_Object = MibScalar
swDoSTrapState = _SwDoSTrapState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 59, 1, 4),
    _SwDoSTrapState_Type()
)
swDoSTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swDoSTrapState.setStatus("current")


class _SwDoSLogState_Type(Integer32):
    """Custom type swDoSLogState based on Integer32"""
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


_SwDoSLogState_Type.__name__ = "Integer32"
_SwDoSLogState_Object = MibScalar
swDoSLogState = _SwDoSLogState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 59, 1, 5),
    _SwDoSLogState_Type()
)
swDoSLogState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swDoSLogState.setStatus("current")


class _SwDoSFunctionVersion_Type(DisplayString):
    """Custom type swDoSFunctionVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SwDoSFunctionVersion_Type.__name__ = "DisplayString"
_SwDoSFunctionVersion_Object = MibScalar
swDoSFunctionVersion = _SwDoSFunctionVersion_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 59, 1, 6),
    _SwDoSFunctionVersion_Type()
)
swDoSFunctionVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDoSFunctionVersion.setStatus("current")
_SwDoSNotify_ObjectIdentity = ObjectIdentity
swDoSNotify = _SwDoSNotify_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 59, 4)
)
_SwDoSNotifyPrefix_ObjectIdentity = ObjectIdentity
swDoSNotifyPrefix = _SwDoSNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 59, 4, 0)
)
_SwDoSNotifyVarBindings_ObjectIdentity = ObjectIdentity
swDoSNotifyVarBindings = _SwDoSNotifyVarBindings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 59, 4, 1)
)
_SwDoSNotifyVarIpAddr_Type = IpAddress
_SwDoSNotifyVarIpAddr_Object = MibScalar
swDoSNotifyVarIpAddr = _SwDoSNotifyVarIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 59, 4, 1, 1),
    _SwDoSNotifyVarIpAddr_Type()
)
swDoSNotifyVarIpAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    swDoSNotifyVarIpAddr.setStatus("current")
_SwDoSNotifyVarPortNumber_Type = DisplayString
_SwDoSNotifyVarPortNumber_Object = MibScalar
swDoSNotifyVarPortNumber = _SwDoSNotifyVarPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 59, 4, 1, 2),
    _SwDoSNotifyVarPortNumber_Type()
)
swDoSNotifyVarPortNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    swDoSNotifyVarPortNumber.setStatus("current")

# Managed Objects groups


# Notification objects

swDoSAttackDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 12, 59, 4, 0, 1)
)
swDoSAttackDetected.setObjects(
      *(("DOS-PREV-MIB", "swDoSCtrlType"),
        ("DOS-PREV-MIB", "swDoSNotifyVarIpAddr"),
        ("DOS-PREV-MIB", "swDoSNotifyVarPortNumber"))
)
if mibBuilder.loadTexts:
    swDoSAttackDetected.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DOS-PREV-MIB",
    **{"swDoSMgmtMIB": swDoSMgmtMIB,
       "swDoSCtrl": swDoSCtrl,
       "swDoSTrapLog": swDoSTrapLog,
       "swDoSClearCounters": swDoSClearCounters,
       "swDoSCtrlTable": swDoSCtrlTable,
       "swDoSCtrlEntry": swDoSCtrlEntry,
       "swDoSCtrlType": swDoSCtrlType,
       "swDoSCtrlState": swDoSCtrlState,
       "swDoSCtrlActionType": swDoSCtrlActionType,
       "swDoSCtrlMirrorPort": swDoSCtrlMirrorPort,
       "swDoSCtrlMirrorPriority": swDoSCtrlMirrorPriority,
       "swDoSCtrlMirrorRxRate": swDoSCtrlMirrorRxRate,
       "swDoSCtrlFrameCount": swDoSCtrlFrameCount,
       "swDoSTrapState": swDoSTrapState,
       "swDoSLogState": swDoSLogState,
       "swDoSFunctionVersion": swDoSFunctionVersion,
       "swDoSNotify": swDoSNotify,
       "swDoSNotifyPrefix": swDoSNotifyPrefix,
       "swDoSAttackDetected": swDoSAttackDetected,
       "swDoSNotifyVarBindings": swDoSNotifyVarBindings,
       "swDoSNotifyVarIpAddr": swDoSNotifyVarIpAddr,
       "swDoSNotifyVarPortNumber": swDoSNotifyVarPortNumber}
)
