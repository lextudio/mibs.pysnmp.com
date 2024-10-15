# SNMP MIB module (CADANT-CMTS-IP-VIDEO-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CADANT-CMTS-IP-VIDEO-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:52:33 2024
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

(cadCmtsIpVideo,) = mibBuilder.importSymbols(
    "CADANT-PRODUCTS-MIB",
    "cadCmtsIpVideo")

(CardId,
 PortId) = mibBuilder.importSymbols(
    "CADANT-TC",
    "CardId",
    "PortId")

(TenthdB,) = mibBuilder.importSymbols(
    "DOCS-IF-MIB",
    "TenthdB")

(AttributeMask,) = mibBuilder.importSymbols(
    "DOCS-IF3-MIB",
    "AttributeMask")

(InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero",
    "ifIndex")

(SnmpAdminString,
 SnmpEngineID) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString",
    "SnmpEngineID")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

cadCmtsIpVideoMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 125, 1)
)
cadCmtsIpVideoMib.setRevisions(
        ("2011-08-04 00:00",
         "2011-07-11 00:00",
         "2011-04-20 00:00",
         "2011-04-19 00:00",
         "2010-12-16 00:00",
         "2010-07-07 00:00",
         "2010-04-20 00:00",
         "2010-04-15 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CadSysIpVideoCfg_ObjectIdentity = ObjectIdentity
cadSysIpVideoCfg = _CadSysIpVideoCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 125, 1, 1)
)


class _CadSysIpVideoAttributeMask_Type(AttributeMask):
    """Custom type cadSysIpVideoAttributeMask based on AttributeMask"""
    defaultHexValue = "00000000"


_CadSysIpVideoAttributeMask_Object = MibScalar
cadSysIpVideoAttributeMask = _CadSysIpVideoAttributeMask_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 125, 1, 1, 1),
    _CadSysIpVideoAttributeMask_Type()
)
cadSysIpVideoAttributeMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadSysIpVideoAttributeMask.setStatus("current")


class _CadSysIpVideoVodThreshold_Type(Unsigned32):
    """Custom type cadSysIpVideoVodThreshold based on Unsigned32"""
    defaultValue = 5000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 10000),
    )


_CadSysIpVideoVodThreshold_Type.__name__ = "Unsigned32"
_CadSysIpVideoVodThreshold_Object = MibScalar
cadSysIpVideoVodThreshold = _CadSysIpVideoVodThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 125, 1, 1, 2),
    _CadSysIpVideoVodThreshold_Type()
)
cadSysIpVideoVodThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadSysIpVideoVodThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cadSysIpVideoVodThreshold.setUnits("milliseconds")


class _CadSysIpVideoLinearThreshold_Type(Unsigned32):
    """Custom type cadSysIpVideoLinearThreshold based on Unsigned32"""
    defaultValue = 1000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 10000),
    )


_CadSysIpVideoLinearThreshold_Type.__name__ = "Unsigned32"
_CadSysIpVideoLinearThreshold_Object = MibScalar
cadSysIpVideoLinearThreshold = _CadSysIpVideoLinearThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 125, 1, 1, 3),
    _CadSysIpVideoLinearThreshold_Type()
)
cadSysIpVideoLinearThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadSysIpVideoLinearThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cadSysIpVideoLinearThreshold.setUnits("milliseconds")


class _CadSysIpVideoInterDbcDelayTimer_Type(Unsigned32):
    """Custom type cadSysIpVideoInterDbcDelayTimer based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3000),
    )


_CadSysIpVideoInterDbcDelayTimer_Type.__name__ = "Unsigned32"
_CadSysIpVideoInterDbcDelayTimer_Object = MibScalar
cadSysIpVideoInterDbcDelayTimer = _CadSysIpVideoInterDbcDelayTimer_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 125, 1, 1, 4),
    _CadSysIpVideoInterDbcDelayTimer_Type()
)
cadSysIpVideoInterDbcDelayTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadSysIpVideoInterDbcDelayTimer.setStatus("current")
if mibBuilder.loadTexts:
    cadSysIpVideoInterDbcDelayTimer.setUnits("milliseconds")


class _CadSysIpVideoMulticastControlled_Type(TruthValue):
    """Custom type cadSysIpVideoMulticastControlled based on TruthValue"""


_CadSysIpVideoMulticastControlled_Object = MibScalar
cadSysIpVideoMulticastControlled = _CadSysIpVideoMulticastControlled_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 125, 1, 1, 5),
    _CadSysIpVideoMulticastControlled_Type()
)
cadSysIpVideoMulticastControlled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadSysIpVideoMulticastControlled.setStatus("current")


class _CadSysIpVideoMulticastAllowedUsage_Type(Integer32):
    """Custom type cadSysIpVideoMulticastAllowedUsage based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CadSysIpVideoMulticastAllowedUsage_Type.__name__ = "Integer32"
_CadSysIpVideoMulticastAllowedUsage_Object = MibScalar
cadSysIpVideoMulticastAllowedUsage = _CadSysIpVideoMulticastAllowedUsage_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 125, 1, 1, 6),
    _CadSysIpVideoMulticastAllowedUsage_Type()
)
cadSysIpVideoMulticastAllowedUsage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadSysIpVideoMulticastAllowedUsage.setStatus("current")
if mibBuilder.loadTexts:
    cadSysIpVideoMulticastAllowedUsage.setUnits("percent")
_CadIpVideoMonitor_ObjectIdentity = ObjectIdentity
cadIpVideoMonitor = _CadIpVideoMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 125, 1, 3)
)
_CadIPVideoMonitorDropsTable_Object = MibTable
cadIPVideoMonitorDropsTable = _CadIPVideoMonitorDropsTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 125, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cadIPVideoMonitorDropsTable.setStatus("current")
_CadIpVideoMonitorDropsEntry_Object = MibTableRow
cadIpVideoMonitorDropsEntry = _CadIpVideoMonitorDropsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 125, 1, 3, 1, 1)
)
cadIpVideoMonitorDropsEntry.setIndexNames(
    (0, "CADANT-CMTS-IP-VIDEO-MIB", "cadIpVideoMonitorCardId"),
    (0, "CADANT-CMTS-IP-VIDEO-MIB", "cadIpVideoMonitorPortConnectorId"),
    (0, "CADANT-CMTS-IP-VIDEO-MIB", "cadIpVideoMonitorCurTimeIdx"),
)
if mibBuilder.loadTexts:
    cadIpVideoMonitorDropsEntry.setStatus("current")
_CadIpVideoMonitorCurTimeIdx_Type = Unsigned32
_CadIpVideoMonitorCurTimeIdx_Object = MibTableColumn
cadIpVideoMonitorCurTimeIdx = _CadIpVideoMonitorCurTimeIdx_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 125, 1, 3, 1, 1, 1),
    _CadIpVideoMonitorCurTimeIdx_Type()
)
cadIpVideoMonitorCurTimeIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadIpVideoMonitorCurTimeIdx.setStatus("current")
_CadIpVideoMonitorMulticastDrops_Type = Unsigned32
_CadIpVideoMonitorMulticastDrops_Object = MibTableColumn
cadIpVideoMonitorMulticastDrops = _CadIpVideoMonitorMulticastDrops_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 125, 1, 3, 1, 1, 2),
    _CadIpVideoMonitorMulticastDrops_Type()
)
cadIpVideoMonitorMulticastDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIpVideoMonitorMulticastDrops.setStatus("current")
_CadIpVideoMonitorUnicastDrops_Type = Unsigned32
_CadIpVideoMonitorUnicastDrops_Object = MibTableColumn
cadIpVideoMonitorUnicastDrops = _CadIpVideoMonitorUnicastDrops_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 125, 1, 3, 1, 1, 3),
    _CadIpVideoMonitorUnicastDrops_Type()
)
cadIpVideoMonitorUnicastDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIpVideoMonitorUnicastDrops.setStatus("current")
_CadIpVideoMonitorDropsSuspectFlag_Type = TruthValue
_CadIpVideoMonitorDropsSuspectFlag_Object = MibTableColumn
cadIpVideoMonitorDropsSuspectFlag = _CadIpVideoMonitorDropsSuspectFlag_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 125, 1, 3, 1, 1, 4),
    _CadIpVideoMonitorDropsSuspectFlag_Type()
)
cadIpVideoMonitorDropsSuspectFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIpVideoMonitorDropsSuspectFlag.setStatus("current")
_CadIpVideoMonitorCreateTime_Type = DateAndTime
_CadIpVideoMonitorCreateTime_Object = MibTableColumn
cadIpVideoMonitorCreateTime = _CadIpVideoMonitorCreateTime_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 125, 1, 3, 1, 1, 5),
    _CadIpVideoMonitorCreateTime_Type()
)
cadIpVideoMonitorCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIpVideoMonitorCreateTime.setStatus("current")
_CadIpVideoMonitorCardId_Type = CardId
_CadIpVideoMonitorCardId_Object = MibTableColumn
cadIpVideoMonitorCardId = _CadIpVideoMonitorCardId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 125, 1, 3, 1, 1, 6),
    _CadIpVideoMonitorCardId_Type()
)
cadIpVideoMonitorCardId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadIpVideoMonitorCardId.setStatus("current")
_CadIpVideoMonitorPortConnectorId_Type = PortId
_CadIpVideoMonitorPortConnectorId_Object = MibTableColumn
cadIpVideoMonitorPortConnectorId = _CadIpVideoMonitorPortConnectorId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 125, 1, 3, 1, 1, 7),
    _CadIpVideoMonitorPortConnectorId_Type()
)
cadIpVideoMonitorPortConnectorId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadIpVideoMonitorPortConnectorId.setStatus("current")
_CadIpVideoMonitorDsChlTable_Object = MibTable
cadIpVideoMonitorDsChlTable = _CadIpVideoMonitorDsChlTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 125, 1, 3, 2)
)
if mibBuilder.loadTexts:
    cadIpVideoMonitorDsChlTable.setStatus("current")
_CadIpVideoMonitorDsChlEntry_Object = MibTableRow
cadIpVideoMonitorDsChlEntry = _CadIpVideoMonitorDsChlEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 125, 1, 3, 2, 1)
)
cadIpVideoMonitorDsChlEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CADANT-CMTS-IP-VIDEO-MIB", "cadIpVideoMonitorCurTimeIdx"),
)
if mibBuilder.loadTexts:
    cadIpVideoMonitorDsChlEntry.setStatus("current")
_CadIpVideoMonitorDsChlCurTimeIdx_Type = Unsigned32
_CadIpVideoMonitorDsChlCurTimeIdx_Object = MibTableColumn
cadIpVideoMonitorDsChlCurTimeIdx = _CadIpVideoMonitorDsChlCurTimeIdx_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 125, 1, 3, 2, 1, 1),
    _CadIpVideoMonitorDsChlCurTimeIdx_Type()
)
cadIpVideoMonitorDsChlCurTimeIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadIpVideoMonitorDsChlCurTimeIdx.setStatus("current")
_CadIpVideoMonitorMcastPkts_Type = Unsigned32
_CadIpVideoMonitorMcastPkts_Object = MibTableColumn
cadIpVideoMonitorMcastPkts = _CadIpVideoMonitorMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 125, 1, 3, 2, 1, 2),
    _CadIpVideoMonitorMcastPkts_Type()
)
cadIpVideoMonitorMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIpVideoMonitorMcastPkts.setStatus("current")
_CadIpVideoMonitorMcastFlows_Type = Unsigned32
_CadIpVideoMonitorMcastFlows_Object = MibTableColumn
cadIpVideoMonitorMcastFlows = _CadIpVideoMonitorMcastFlows_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 125, 1, 3, 2, 1, 3),
    _CadIpVideoMonitorMcastFlows_Type()
)
cadIpVideoMonitorMcastFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIpVideoMonitorMcastFlows.setStatus("current")
_CadIpVideoMonitorUcastPkts_Type = Unsigned32
_CadIpVideoMonitorUcastPkts_Object = MibTableColumn
cadIpVideoMonitorUcastPkts = _CadIpVideoMonitorUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 125, 1, 3, 2, 1, 5),
    _CadIpVideoMonitorUcastPkts_Type()
)
cadIpVideoMonitorUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIpVideoMonitorUcastPkts.setStatus("current")
_CadIpVideoMonitorUcastFlows_Type = Unsigned32
_CadIpVideoMonitorUcastFlows_Object = MibTableColumn
cadIpVideoMonitorUcastFlows = _CadIpVideoMonitorUcastFlows_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 125, 1, 3, 2, 1, 7),
    _CadIpVideoMonitorUcastFlows_Type()
)
cadIpVideoMonitorUcastFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIpVideoMonitorUcastFlows.setStatus("current")
_CadIpVideoMonitorDsChlSuspectFlag_Type = TruthValue
_CadIpVideoMonitorDsChlSuspectFlag_Object = MibTableColumn
cadIpVideoMonitorDsChlSuspectFlag = _CadIpVideoMonitorDsChlSuspectFlag_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 125, 1, 3, 2, 1, 9),
    _CadIpVideoMonitorDsChlSuspectFlag_Type()
)
cadIpVideoMonitorDsChlSuspectFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIpVideoMonitorDsChlSuspectFlag.setStatus("current")
_CadIpVideoMonitorDsChlCreateTime_Type = DateAndTime
_CadIpVideoMonitorDsChlCreateTime_Object = MibTableColumn
cadIpVideoMonitorDsChlCreateTime = _CadIpVideoMonitorDsChlCreateTime_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 125, 1, 3, 2, 1, 10),
    _CadIpVideoMonitorDsChlCreateTime_Type()
)
cadIpVideoMonitorDsChlCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIpVideoMonitorDsChlCreateTime.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CADANT-CMTS-IP-VIDEO-MIB",
    **{"cadCmtsIpVideoMib": cadCmtsIpVideoMib,
       "cadSysIpVideoCfg": cadSysIpVideoCfg,
       "cadSysIpVideoAttributeMask": cadSysIpVideoAttributeMask,
       "cadSysIpVideoVodThreshold": cadSysIpVideoVodThreshold,
       "cadSysIpVideoLinearThreshold": cadSysIpVideoLinearThreshold,
       "cadSysIpVideoInterDbcDelayTimer": cadSysIpVideoInterDbcDelayTimer,
       "cadSysIpVideoMulticastControlled": cadSysIpVideoMulticastControlled,
       "cadSysIpVideoMulticastAllowedUsage": cadSysIpVideoMulticastAllowedUsage,
       "cadIpVideoMonitor": cadIpVideoMonitor,
       "cadIPVideoMonitorDropsTable": cadIPVideoMonitorDropsTable,
       "cadIpVideoMonitorDropsEntry": cadIpVideoMonitorDropsEntry,
       "cadIpVideoMonitorCurTimeIdx": cadIpVideoMonitorCurTimeIdx,
       "cadIpVideoMonitorMulticastDrops": cadIpVideoMonitorMulticastDrops,
       "cadIpVideoMonitorUnicastDrops": cadIpVideoMonitorUnicastDrops,
       "cadIpVideoMonitorDropsSuspectFlag": cadIpVideoMonitorDropsSuspectFlag,
       "cadIpVideoMonitorCreateTime": cadIpVideoMonitorCreateTime,
       "cadIpVideoMonitorCardId": cadIpVideoMonitorCardId,
       "cadIpVideoMonitorPortConnectorId": cadIpVideoMonitorPortConnectorId,
       "cadIpVideoMonitorDsChlTable": cadIpVideoMonitorDsChlTable,
       "cadIpVideoMonitorDsChlEntry": cadIpVideoMonitorDsChlEntry,
       "cadIpVideoMonitorDsChlCurTimeIdx": cadIpVideoMonitorDsChlCurTimeIdx,
       "cadIpVideoMonitorMcastPkts": cadIpVideoMonitorMcastPkts,
       "cadIpVideoMonitorMcastFlows": cadIpVideoMonitorMcastFlows,
       "cadIpVideoMonitorUcastPkts": cadIpVideoMonitorUcastPkts,
       "cadIpVideoMonitorUcastFlows": cadIpVideoMonitorUcastFlows,
       "cadIpVideoMonitorDsChlSuspectFlag": cadIpVideoMonitorDsChlSuspectFlag,
       "cadIpVideoMonitorDsChlCreateTime": cadIpVideoMonitorDsChlCreateTime}
)
