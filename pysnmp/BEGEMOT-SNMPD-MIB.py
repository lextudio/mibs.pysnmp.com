# SNMP MIB module (BEGEMOT-SNMPD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BEGEMOT-SNMPD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:46:47 2024
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

(begemot,) = mibBuilder.importSymbols(
    "BEGEMOT-MIB",
    "begemot")

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

(DisplayString,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

begemotSnmpd = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 12325, 1, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class SectionName(OctetString, TextualConvention):
    status = "current"
    displayHint = "14a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 14),
    )



# MIB Managed Objects in the order of their OIDs

_BegemotSnmpdObjects_ObjectIdentity = ObjectIdentity
begemotSnmpdObjects = _BegemotSnmpdObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12325, 1, 1, 1)
)
_BegemotSnmpdConfig_ObjectIdentity = ObjectIdentity
begemotSnmpdConfig = _BegemotSnmpdConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12325, 1, 1, 1, 1)
)


class _BegemotSnmpdTransmitBuffer_Type(Integer32):
    """Custom type begemotSnmpdTransmitBuffer based on Integer32"""
    defaultValue = 2048

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(484, 65535),
    )


_BegemotSnmpdTransmitBuffer_Type.__name__ = "Integer32"
_BegemotSnmpdTransmitBuffer_Object = MibScalar
begemotSnmpdTransmitBuffer = _BegemotSnmpdTransmitBuffer_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 1, 1, 1, 1),
    _BegemotSnmpdTransmitBuffer_Type()
)
begemotSnmpdTransmitBuffer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    begemotSnmpdTransmitBuffer.setStatus("current")


class _BegemotSnmpdReceiveBuffer_Type(Integer32):
    """Custom type begemotSnmpdReceiveBuffer based on Integer32"""
    defaultValue = 2048

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(484, 65535),
    )


_BegemotSnmpdReceiveBuffer_Type.__name__ = "Integer32"
_BegemotSnmpdReceiveBuffer_Object = MibScalar
begemotSnmpdReceiveBuffer = _BegemotSnmpdReceiveBuffer_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 1, 1, 1, 2),
    _BegemotSnmpdReceiveBuffer_Type()
)
begemotSnmpdReceiveBuffer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    begemotSnmpdReceiveBuffer.setStatus("current")


class _BegemotSnmpdCommunityDisable_Type(TruthValue):
    """Custom type begemotSnmpdCommunityDisable based on TruthValue"""


_BegemotSnmpdCommunityDisable_Object = MibScalar
begemotSnmpdCommunityDisable = _BegemotSnmpdCommunityDisable_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 1, 1, 1, 3),
    _BegemotSnmpdCommunityDisable_Type()
)
begemotSnmpdCommunityDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    begemotSnmpdCommunityDisable.setStatus("current")
_BegemotSnmpdTrap1Addr_Type = IpAddress
_BegemotSnmpdTrap1Addr_Object = MibScalar
begemotSnmpdTrap1Addr = _BegemotSnmpdTrap1Addr_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 1, 1, 1, 4),
    _BegemotSnmpdTrap1Addr_Type()
)
begemotSnmpdTrap1Addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    begemotSnmpdTrap1Addr.setStatus("current")


class _BegemotSnmpdVersionEnable_Type(Unsigned32):
    """Custom type begemotSnmpdVersionEnable based on Unsigned32"""
    defaultValue = 3


_BegemotSnmpdVersionEnable_Object = MibScalar
begemotSnmpdVersionEnable = _BegemotSnmpdVersionEnable_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 1, 1, 1, 5),
    _BegemotSnmpdVersionEnable_Type()
)
begemotSnmpdVersionEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    begemotSnmpdVersionEnable.setStatus("current")
_BegemotTrapSinkTable_Object = MibTable
begemotTrapSinkTable = _BegemotTrapSinkTable_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    begemotTrapSinkTable.setStatus("current")
_BegemotTrapSinkEntry_Object = MibTableRow
begemotTrapSinkEntry = _BegemotTrapSinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 1, 1, 2, 1)
)
begemotTrapSinkEntry.setIndexNames(
    (0, "BEGEMOT-SNMPD-MIB", "begemotTrapSinkAddr"),
    (0, "BEGEMOT-SNMPD-MIB", "begemotTrapSinkPort"),
)
if mibBuilder.loadTexts:
    begemotTrapSinkEntry.setStatus("current")
_BegemotTrapSinkAddr_Type = IpAddress
_BegemotTrapSinkAddr_Object = MibTableColumn
begemotTrapSinkAddr = _BegemotTrapSinkAddr_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 1, 1, 2, 1, 1),
    _BegemotTrapSinkAddr_Type()
)
begemotTrapSinkAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    begemotTrapSinkAddr.setStatus("current")


class _BegemotTrapSinkPort_Type(Integer32):
    """Custom type begemotTrapSinkPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_BegemotTrapSinkPort_Type.__name__ = "Integer32"
_BegemotTrapSinkPort_Object = MibTableColumn
begemotTrapSinkPort = _BegemotTrapSinkPort_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 1, 1, 2, 1, 2),
    _BegemotTrapSinkPort_Type()
)
begemotTrapSinkPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    begemotTrapSinkPort.setStatus("current")
_BegemotTrapSinkStatus_Type = RowStatus
_BegemotTrapSinkStatus_Object = MibTableColumn
begemotTrapSinkStatus = _BegemotTrapSinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 1, 1, 2, 1, 3),
    _BegemotTrapSinkStatus_Type()
)
begemotTrapSinkStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    begemotTrapSinkStatus.setStatus("current")
_BegemotSnmpdPortTable_Object = MibTable
begemotSnmpdPortTable = _BegemotSnmpdPortTable_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 1, 1, 4)
)
if mibBuilder.loadTexts:
    begemotSnmpdPortTable.setStatus("current")
_BegemotSnmpdPortEntry_Object = MibTableRow
begemotSnmpdPortEntry = _BegemotSnmpdPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 1, 1, 4, 1)
)
begemotSnmpdPortEntry.setIndexNames(
    (0, "BEGEMOT-SNMPD-MIB", "begemotSnmpdPortAddress"),
    (0, "BEGEMOT-SNMPD-MIB", "begemotSnmpdPortPort"),
)
if mibBuilder.loadTexts:
    begemotSnmpdPortEntry.setStatus("current")
_BegemotSnmpdPortAddress_Type = IpAddress
_BegemotSnmpdPortAddress_Object = MibTableColumn
begemotSnmpdPortAddress = _BegemotSnmpdPortAddress_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 1, 1, 4, 1, 1),
    _BegemotSnmpdPortAddress_Type()
)
begemotSnmpdPortAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    begemotSnmpdPortAddress.setStatus("current")


class _BegemotSnmpdPortPort_Type(Integer32):
    """Custom type begemotSnmpdPortPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_BegemotSnmpdPortPort_Type.__name__ = "Integer32"
_BegemotSnmpdPortPort_Object = MibTableColumn
begemotSnmpdPortPort = _BegemotSnmpdPortPort_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 1, 1, 4, 1, 2),
    _BegemotSnmpdPortPort_Type()
)
begemotSnmpdPortPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    begemotSnmpdPortPort.setStatus("current")


class _BegemotSnmpdPortStatus_Type(Integer32):
    """Custom type begemotSnmpdPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_BegemotSnmpdPortStatus_Type.__name__ = "Integer32"
_BegemotSnmpdPortStatus_Object = MibTableColumn
begemotSnmpdPortStatus = _BegemotSnmpdPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 1, 1, 4, 1, 3),
    _BegemotSnmpdPortStatus_Type()
)
begemotSnmpdPortStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    begemotSnmpdPortStatus.setStatus("current")
_BegemotSnmpdCommunityTable_Object = MibTable
begemotSnmpdCommunityTable = _BegemotSnmpdCommunityTable_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 1, 1, 5)
)
if mibBuilder.loadTexts:
    begemotSnmpdCommunityTable.setStatus("current")
_BegemotSnmpdCommunityEntry_Object = MibTableRow
begemotSnmpdCommunityEntry = _BegemotSnmpdCommunityEntry_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 1, 1, 5, 1)
)
begemotSnmpdCommunityEntry.setIndexNames(
    (0, "BEGEMOT-SNMPD-MIB", "begemotSnmpdCommunityModule"),
    (0, "BEGEMOT-SNMPD-MIB", "begemotSnmpdCommunityIndex"),
)
if mibBuilder.loadTexts:
    begemotSnmpdCommunityEntry.setStatus("current")
_BegemotSnmpdCommunityModule_Type = SectionName
_BegemotSnmpdCommunityModule_Object = MibTableColumn
begemotSnmpdCommunityModule = _BegemotSnmpdCommunityModule_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 1, 1, 5, 1, 1),
    _BegemotSnmpdCommunityModule_Type()
)
begemotSnmpdCommunityModule.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    begemotSnmpdCommunityModule.setStatus("current")


class _BegemotSnmpdCommunityIndex_Type(Unsigned32):
    """Custom type begemotSnmpdCommunityIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_BegemotSnmpdCommunityIndex_Type.__name__ = "Unsigned32"
_BegemotSnmpdCommunityIndex_Object = MibTableColumn
begemotSnmpdCommunityIndex = _BegemotSnmpdCommunityIndex_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 1, 1, 5, 1, 2),
    _BegemotSnmpdCommunityIndex_Type()
)
begemotSnmpdCommunityIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    begemotSnmpdCommunityIndex.setStatus("current")
_BegemotSnmpdCommunityString_Type = OctetString
_BegemotSnmpdCommunityString_Object = MibTableColumn
begemotSnmpdCommunityString = _BegemotSnmpdCommunityString_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 1, 1, 5, 1, 3),
    _BegemotSnmpdCommunityString_Type()
)
begemotSnmpdCommunityString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    begemotSnmpdCommunityString.setStatus("current")
_BegemotSnmpdCommunityDescr_Type = OctetString
_BegemotSnmpdCommunityDescr_Object = MibTableColumn
begemotSnmpdCommunityDescr = _BegemotSnmpdCommunityDescr_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 1, 1, 5, 1, 4),
    _BegemotSnmpdCommunityDescr_Type()
)
begemotSnmpdCommunityDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    begemotSnmpdCommunityDescr.setStatus("current")
_BegemotSnmpdModuleTable_Object = MibTable
begemotSnmpdModuleTable = _BegemotSnmpdModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 1, 1, 6)
)
if mibBuilder.loadTexts:
    begemotSnmpdModuleTable.setStatus("current")
_BegemotSnmpdModuleEntry_Object = MibTableRow
begemotSnmpdModuleEntry = _BegemotSnmpdModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 1, 1, 6, 1)
)
begemotSnmpdModuleEntry.setIndexNames(
    (0, "BEGEMOT-SNMPD-MIB", "begemotSnmpdModuleSection"),
)
if mibBuilder.loadTexts:
    begemotSnmpdModuleEntry.setStatus("current")
_BegemotSnmpdModuleSection_Type = SectionName
_BegemotSnmpdModuleSection_Object = MibTableColumn
begemotSnmpdModuleSection = _BegemotSnmpdModuleSection_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 1, 1, 6, 1, 1),
    _BegemotSnmpdModuleSection_Type()
)
begemotSnmpdModuleSection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    begemotSnmpdModuleSection.setStatus("current")
_BegemotSnmpdModulePath_Type = OctetString
_BegemotSnmpdModulePath_Object = MibTableColumn
begemotSnmpdModulePath = _BegemotSnmpdModulePath_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 1, 1, 6, 1, 2),
    _BegemotSnmpdModulePath_Type()
)
begemotSnmpdModulePath.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    begemotSnmpdModulePath.setStatus("current")
_BegemotSnmpdModuleComment_Type = OctetString
_BegemotSnmpdModuleComment_Object = MibTableColumn
begemotSnmpdModuleComment = _BegemotSnmpdModuleComment_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 1, 1, 6, 1, 3),
    _BegemotSnmpdModuleComment_Type()
)
begemotSnmpdModuleComment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    begemotSnmpdModuleComment.setStatus("current")
_BegemotSnmpdStats_ObjectIdentity = ObjectIdentity
begemotSnmpdStats = _BegemotSnmpdStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12325, 1, 1, 1, 7)
)
_BegemotSnmpdStatsNoRxBufs_Type = Counter32
_BegemotSnmpdStatsNoRxBufs_Object = MibScalar
begemotSnmpdStatsNoRxBufs = _BegemotSnmpdStatsNoRxBufs_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 1, 1, 7, 1),
    _BegemotSnmpdStatsNoRxBufs_Type()
)
begemotSnmpdStatsNoRxBufs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    begemotSnmpdStatsNoRxBufs.setStatus("current")
_BegemotSnmpdStatsNoTxBufs_Type = Counter32
_BegemotSnmpdStatsNoTxBufs_Object = MibScalar
begemotSnmpdStatsNoTxBufs = _BegemotSnmpdStatsNoTxBufs_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 1, 1, 7, 2),
    _BegemotSnmpdStatsNoTxBufs_Type()
)
begemotSnmpdStatsNoTxBufs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    begemotSnmpdStatsNoTxBufs.setStatus("current")
_BegemotSnmpdStatsInTooLongPkts_Type = Counter32
_BegemotSnmpdStatsInTooLongPkts_Object = MibScalar
begemotSnmpdStatsInTooLongPkts = _BegemotSnmpdStatsInTooLongPkts_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 1, 1, 7, 3),
    _BegemotSnmpdStatsInTooLongPkts_Type()
)
begemotSnmpdStatsInTooLongPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    begemotSnmpdStatsInTooLongPkts.setStatus("current")
_BegemotSnmpdStatsInBadPduTypes_Type = Counter32
_BegemotSnmpdStatsInBadPduTypes_Object = MibScalar
begemotSnmpdStatsInBadPduTypes = _BegemotSnmpdStatsInBadPduTypes_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 1, 1, 7, 4),
    _BegemotSnmpdStatsInBadPduTypes_Type()
)
begemotSnmpdStatsInBadPduTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    begemotSnmpdStatsInBadPduTypes.setStatus("current")
_BegemotSnmpdDebug_ObjectIdentity = ObjectIdentity
begemotSnmpdDebug = _BegemotSnmpdDebug_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12325, 1, 1, 1, 8)
)


class _BegemotSnmpdDebugDumpPdus_Type(TruthValue):
    """Custom type begemotSnmpdDebugDumpPdus based on TruthValue"""


_BegemotSnmpdDebugDumpPdus_Object = MibScalar
begemotSnmpdDebugDumpPdus = _BegemotSnmpdDebugDumpPdus_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 1, 1, 8, 1),
    _BegemotSnmpdDebugDumpPdus_Type()
)
begemotSnmpdDebugDumpPdus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    begemotSnmpdDebugDumpPdus.setStatus("current")


class _BegemotSnmpdDebugSnmpTrace_Type(Unsigned32):
    """Custom type begemotSnmpdDebugSnmpTrace based on Unsigned32"""
    defaultValue = 0


_BegemotSnmpdDebugSnmpTrace_Object = MibScalar
begemotSnmpdDebugSnmpTrace = _BegemotSnmpdDebugSnmpTrace_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 1, 1, 8, 2),
    _BegemotSnmpdDebugSnmpTrace_Type()
)
begemotSnmpdDebugSnmpTrace.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    begemotSnmpdDebugSnmpTrace.setStatus("current")


class _BegemotSnmpdDebugSyslogPri_Type(Integer32):
    """Custom type begemotSnmpdDebugSyslogPri based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_BegemotSnmpdDebugSyslogPri_Type.__name__ = "Integer32"
_BegemotSnmpdDebugSyslogPri_Object = MibScalar
begemotSnmpdDebugSyslogPri = _BegemotSnmpdDebugSyslogPri_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 1, 1, 8, 3),
    _BegemotSnmpdDebugSyslogPri_Type()
)
begemotSnmpdDebugSyslogPri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    begemotSnmpdDebugSyslogPri.setStatus("current")
_BegemotSnmpdLocalPortTable_Object = MibTable
begemotSnmpdLocalPortTable = _BegemotSnmpdLocalPortTable_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 1, 1, 9)
)
if mibBuilder.loadTexts:
    begemotSnmpdLocalPortTable.setStatus("current")
_BegemotSnmpdLocalPortEntry_Object = MibTableRow
begemotSnmpdLocalPortEntry = _BegemotSnmpdLocalPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 1, 1, 9, 1)
)
begemotSnmpdLocalPortEntry.setIndexNames(
    (0, "BEGEMOT-SNMPD-MIB", "begemotSnmpdLocalPortPath"),
)
if mibBuilder.loadTexts:
    begemotSnmpdLocalPortEntry.setStatus("current")


class _BegemotSnmpdLocalPortPath_Type(OctetString):
    """Custom type begemotSnmpdLocalPortPath based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 104),
    )


_BegemotSnmpdLocalPortPath_Type.__name__ = "OctetString"
_BegemotSnmpdLocalPortPath_Object = MibTableColumn
begemotSnmpdLocalPortPath = _BegemotSnmpdLocalPortPath_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 1, 1, 9, 1, 1),
    _BegemotSnmpdLocalPortPath_Type()
)
begemotSnmpdLocalPortPath.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    begemotSnmpdLocalPortPath.setStatus("current")


class _BegemotSnmpdLocalPortStatus_Type(Integer32):
    """Custom type begemotSnmpdLocalPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_BegemotSnmpdLocalPortStatus_Type.__name__ = "Integer32"
_BegemotSnmpdLocalPortStatus_Object = MibTableColumn
begemotSnmpdLocalPortStatus = _BegemotSnmpdLocalPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 1, 1, 9, 1, 2),
    _BegemotSnmpdLocalPortStatus_Type()
)
begemotSnmpdLocalPortStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    begemotSnmpdLocalPortStatus.setStatus("current")


class _BegemotSnmpdLocalPortType_Type(Integer32):
    """Custom type begemotSnmpdLocalPortType based on Integer32"""
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
        *(("dgram-priv", 2),
          ("dgram-unpriv", 1),
          ("stream-priv", 4),
          ("stream-unpriv", 3))
    )


_BegemotSnmpdLocalPortType_Type.__name__ = "Integer32"
_BegemotSnmpdLocalPortType_Object = MibTableColumn
begemotSnmpdLocalPortType = _BegemotSnmpdLocalPortType_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 1, 1, 9, 1, 3),
    _BegemotSnmpdLocalPortType_Type()
)
begemotSnmpdLocalPortType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    begemotSnmpdLocalPortType.setStatus("current")
_BegemotSnmpdTransportMappings_ObjectIdentity = ObjectIdentity
begemotSnmpdTransportMappings = _BegemotSnmpdTransportMappings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12325, 1, 1, 1, 10)
)
_BegemotSnmpdTransportTable_Object = MibTable
begemotSnmpdTransportTable = _BegemotSnmpdTransportTable_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 1, 1, 10, 1)
)
if mibBuilder.loadTexts:
    begemotSnmpdTransportTable.setStatus("current")
_BegemotSnmpdTransportEntry_Object = MibTableRow
begemotSnmpdTransportEntry = _BegemotSnmpdTransportEntry_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 1, 1, 10, 1, 1)
)
begemotSnmpdTransportEntry.setIndexNames(
    (0, "BEGEMOT-SNMPD-MIB", "begemotSnmpdTransportName"),
)
if mibBuilder.loadTexts:
    begemotSnmpdTransportEntry.setStatus("current")


class _BegemotSnmpdTransportName_Type(OctetString):
    """Custom type begemotSnmpdTransportName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_BegemotSnmpdTransportName_Type.__name__ = "OctetString"
_BegemotSnmpdTransportName_Object = MibTableColumn
begemotSnmpdTransportName = _BegemotSnmpdTransportName_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 1, 1, 10, 1, 1, 1),
    _BegemotSnmpdTransportName_Type()
)
begemotSnmpdTransportName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    begemotSnmpdTransportName.setStatus("current")
_BegemotSnmpdTransportStatus_Type = RowStatus
_BegemotSnmpdTransportStatus_Object = MibTableColumn
begemotSnmpdTransportStatus = _BegemotSnmpdTransportStatus_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 1, 1, 10, 1, 1, 2),
    _BegemotSnmpdTransportStatus_Type()
)
begemotSnmpdTransportStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    begemotSnmpdTransportStatus.setStatus("current")
_BegemotSnmpdTransportOid_Type = ObjectIdentifier
_BegemotSnmpdTransportOid_Object = MibTableColumn
begemotSnmpdTransportOid = _BegemotSnmpdTransportOid_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 1, 1, 10, 1, 1, 3),
    _BegemotSnmpdTransportOid_Type()
)
begemotSnmpdTransportOid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    begemotSnmpdTransportOid.setStatus("current")
_BegemotSnmpdTransUdp_ObjectIdentity = ObjectIdentity
begemotSnmpdTransUdp = _BegemotSnmpdTransUdp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12325, 1, 1, 1, 10, 2)
)
_BegemotSnmpdTransLsock_ObjectIdentity = ObjectIdentity
begemotSnmpdTransLsock = _BegemotSnmpdTransLsock_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12325, 1, 1, 1, 10, 3)
)
_BegemotSnmpdDefs_ObjectIdentity = ObjectIdentity
begemotSnmpdDefs = _BegemotSnmpdDefs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12325, 1, 1, 2)
)
_BegemotSnmpdAgent_ObjectIdentity = ObjectIdentity
begemotSnmpdAgent = _BegemotSnmpdAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12325, 1, 1, 2, 1)
)
_BegemotSnmpdAgentFreeBSD_ObjectIdentity = ObjectIdentity
begemotSnmpdAgentFreeBSD = _BegemotSnmpdAgentFreeBSD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12325, 1, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    begemotSnmpdAgentFreeBSD.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BEGEMOT-SNMPD-MIB",
    **{"SectionName": SectionName,
       "begemotSnmpd": begemotSnmpd,
       "begemotSnmpdObjects": begemotSnmpdObjects,
       "begemotSnmpdConfig": begemotSnmpdConfig,
       "begemotSnmpdTransmitBuffer": begemotSnmpdTransmitBuffer,
       "begemotSnmpdReceiveBuffer": begemotSnmpdReceiveBuffer,
       "begemotSnmpdCommunityDisable": begemotSnmpdCommunityDisable,
       "begemotSnmpdTrap1Addr": begemotSnmpdTrap1Addr,
       "begemotSnmpdVersionEnable": begemotSnmpdVersionEnable,
       "begemotTrapSinkTable": begemotTrapSinkTable,
       "begemotTrapSinkEntry": begemotTrapSinkEntry,
       "begemotTrapSinkAddr": begemotTrapSinkAddr,
       "begemotTrapSinkPort": begemotTrapSinkPort,
       "begemotTrapSinkStatus": begemotTrapSinkStatus,
       "begemotSnmpdPortTable": begemotSnmpdPortTable,
       "begemotSnmpdPortEntry": begemotSnmpdPortEntry,
       "begemotSnmpdPortAddress": begemotSnmpdPortAddress,
       "begemotSnmpdPortPort": begemotSnmpdPortPort,
       "begemotSnmpdPortStatus": begemotSnmpdPortStatus,
       "begemotSnmpdCommunityTable": begemotSnmpdCommunityTable,
       "begemotSnmpdCommunityEntry": begemotSnmpdCommunityEntry,
       "begemotSnmpdCommunityModule": begemotSnmpdCommunityModule,
       "begemotSnmpdCommunityIndex": begemotSnmpdCommunityIndex,
       "begemotSnmpdCommunityString": begemotSnmpdCommunityString,
       "begemotSnmpdCommunityDescr": begemotSnmpdCommunityDescr,
       "begemotSnmpdModuleTable": begemotSnmpdModuleTable,
       "begemotSnmpdModuleEntry": begemotSnmpdModuleEntry,
       "begemotSnmpdModuleSection": begemotSnmpdModuleSection,
       "begemotSnmpdModulePath": begemotSnmpdModulePath,
       "begemotSnmpdModuleComment": begemotSnmpdModuleComment,
       "begemotSnmpdStats": begemotSnmpdStats,
       "begemotSnmpdStatsNoRxBufs": begemotSnmpdStatsNoRxBufs,
       "begemotSnmpdStatsNoTxBufs": begemotSnmpdStatsNoTxBufs,
       "begemotSnmpdStatsInTooLongPkts": begemotSnmpdStatsInTooLongPkts,
       "begemotSnmpdStatsInBadPduTypes": begemotSnmpdStatsInBadPduTypes,
       "begemotSnmpdDebug": begemotSnmpdDebug,
       "begemotSnmpdDebugDumpPdus": begemotSnmpdDebugDumpPdus,
       "begemotSnmpdDebugSnmpTrace": begemotSnmpdDebugSnmpTrace,
       "begemotSnmpdDebugSyslogPri": begemotSnmpdDebugSyslogPri,
       "begemotSnmpdLocalPortTable": begemotSnmpdLocalPortTable,
       "begemotSnmpdLocalPortEntry": begemotSnmpdLocalPortEntry,
       "begemotSnmpdLocalPortPath": begemotSnmpdLocalPortPath,
       "begemotSnmpdLocalPortStatus": begemotSnmpdLocalPortStatus,
       "begemotSnmpdLocalPortType": begemotSnmpdLocalPortType,
       "begemotSnmpdTransportMappings": begemotSnmpdTransportMappings,
       "begemotSnmpdTransportTable": begemotSnmpdTransportTable,
       "begemotSnmpdTransportEntry": begemotSnmpdTransportEntry,
       "begemotSnmpdTransportName": begemotSnmpdTransportName,
       "begemotSnmpdTransportStatus": begemotSnmpdTransportStatus,
       "begemotSnmpdTransportOid": begemotSnmpdTransportOid,
       "begemotSnmpdTransUdp": begemotSnmpdTransUdp,
       "begemotSnmpdTransLsock": begemotSnmpdTransLsock,
       "begemotSnmpdDefs": begemotSnmpdDefs,
       "begemotSnmpdAgent": begemotSnmpdAgent,
       "begemotSnmpdAgentFreeBSD": begemotSnmpdAgentFreeBSD}
)
