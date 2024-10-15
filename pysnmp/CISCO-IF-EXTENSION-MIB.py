# SNMP MIB module (CISCO-IF-EXTENSION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-IF-EXTENSION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:58:13 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(IfOperStatusReason,) = mibBuilder.importSymbols(
    "CISCO-TC",
    "IfOperStatusReason")

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

(InterfaceIndexOrZero,
 ifAdminStatus,
 ifIndex,
 ifName,
 ifOperStatus,
 ifType) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero",
    "ifAdminStatus",
    "ifIndex",
    "ifName",
    "ifOperStatus",
    "ifType")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoIfExtensionMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 276)
)
ciscoIfExtensionMIB.setRevisions(
        ("2013-03-13 00:00",
         "2012-09-05 00:00",
         "2011-06-27 00:00",
         "2009-02-26 00:00",
         "2008-12-09 00:00",
         "2008-10-06 00:00",
         "2008-07-31 00:00",
         "2008-07-08 00:00",
         "2008-06-23 00:00",
         "2007-07-23 00:00",
         "2006-11-01 00:00",
         "2005-04-28 00:00",
         "2005-01-25 00:00",
         "2004-09-08 00:00",
         "2003-11-14 00:00",
         "2003-08-12 00:00",
         "2003-07-17 00:00",
         "2003-06-25 00:00",
         "2002-10-12 00:00",
         "2002-07-24 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class InterfaceIndexList(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class InterfaceOperModeList(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )



class InterfaceOperCauseList(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )



class InterfaceOwnershipList(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )



class IfIndexPersistenceState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("global", 3))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoIfExtensionMIBNotifications_ObjectIdentity = ObjectIdentity
ciscoIfExtensionMIBNotifications = _CiscoIfExtensionMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 0)
)
_CiscoIfExtensionMIBObjects_ObjectIdentity = ObjectIdentity
ciscoIfExtensionMIBObjects = _CiscoIfExtensionMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 1)
)
_CiscoIfExtensionStats_ObjectIdentity = ObjectIdentity
ciscoIfExtensionStats = _CiscoIfExtensionStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 1)
)
_CieIfPacketStatsTable_Object = MibTable
cieIfPacketStatsTable = _CieIfPacketStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cieIfPacketStatsTable.setStatus("current")
_CieIfPacketStatsEntry_Object = MibTableRow
cieIfPacketStatsEntry = _CieIfPacketStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 1, 1, 1)
)
cieIfPacketStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cieIfPacketStatsEntry.setStatus("current")
_CieIfLastInTime_Type = Gauge32
_CieIfLastInTime_Object = MibTableColumn
cieIfLastInTime = _CieIfLastInTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 1, 1, 1, 1),
    _CieIfLastInTime_Type()
)
cieIfLastInTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cieIfLastInTime.setStatus("current")
if mibBuilder.loadTexts:
    cieIfLastInTime.setUnits("milliseconds")
_CieIfLastOutTime_Type = Gauge32
_CieIfLastOutTime_Object = MibTableColumn
cieIfLastOutTime = _CieIfLastOutTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 1, 1, 1, 2),
    _CieIfLastOutTime_Type()
)
cieIfLastOutTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cieIfLastOutTime.setStatus("current")
if mibBuilder.loadTexts:
    cieIfLastOutTime.setUnits("milliseconds")
_CieIfLastOutHangTime_Type = Gauge32
_CieIfLastOutHangTime_Object = MibTableColumn
cieIfLastOutHangTime = _CieIfLastOutHangTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 1, 1, 1, 3),
    _CieIfLastOutHangTime_Type()
)
cieIfLastOutHangTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cieIfLastOutHangTime.setStatus("current")
if mibBuilder.loadTexts:
    cieIfLastOutHangTime.setUnits("milliseconds")
_CieIfInRuntsErrs_Type = Counter32
_CieIfInRuntsErrs_Object = MibTableColumn
cieIfInRuntsErrs = _CieIfInRuntsErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 1, 1, 1, 4),
    _CieIfInRuntsErrs_Type()
)
cieIfInRuntsErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cieIfInRuntsErrs.setStatus("current")
_CieIfInGiantsErrs_Type = Counter32
_CieIfInGiantsErrs_Object = MibTableColumn
cieIfInGiantsErrs = _CieIfInGiantsErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 1, 1, 1, 5),
    _CieIfInGiantsErrs_Type()
)
cieIfInGiantsErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cieIfInGiantsErrs.setStatus("current")
_CieIfInFramingErrs_Type = Counter32
_CieIfInFramingErrs_Object = MibTableColumn
cieIfInFramingErrs = _CieIfInFramingErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 1, 1, 1, 6),
    _CieIfInFramingErrs_Type()
)
cieIfInFramingErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cieIfInFramingErrs.setStatus("current")
_CieIfInOverrunErrs_Type = Counter32
_CieIfInOverrunErrs_Object = MibTableColumn
cieIfInOverrunErrs = _CieIfInOverrunErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 1, 1, 1, 7),
    _CieIfInOverrunErrs_Type()
)
cieIfInOverrunErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cieIfInOverrunErrs.setStatus("current")
_CieIfInIgnored_Type = Counter32
_CieIfInIgnored_Object = MibTableColumn
cieIfInIgnored = _CieIfInIgnored_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 1, 1, 1, 8),
    _CieIfInIgnored_Type()
)
cieIfInIgnored.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cieIfInIgnored.setStatus("current")
_CieIfInAbortErrs_Type = Counter32
_CieIfInAbortErrs_Object = MibTableColumn
cieIfInAbortErrs = _CieIfInAbortErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 1, 1, 1, 9),
    _CieIfInAbortErrs_Type()
)
cieIfInAbortErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cieIfInAbortErrs.setStatus("current")
_CieIfInputQueueDrops_Type = Counter32
_CieIfInputQueueDrops_Object = MibTableColumn
cieIfInputQueueDrops = _CieIfInputQueueDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 1, 1, 1, 10),
    _CieIfInputQueueDrops_Type()
)
cieIfInputQueueDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cieIfInputQueueDrops.setStatus("current")
_CieIfOutputQueueDrops_Type = Counter32
_CieIfOutputQueueDrops_Object = MibTableColumn
cieIfOutputQueueDrops = _CieIfOutputQueueDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 1, 1, 1, 11),
    _CieIfOutputQueueDrops_Type()
)
cieIfOutputQueueDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cieIfOutputQueueDrops.setStatus("current")
_CieIfPacketDiscontinuityTime_Type = TimeStamp
_CieIfPacketDiscontinuityTime_Object = MibTableColumn
cieIfPacketDiscontinuityTime = _CieIfPacketDiscontinuityTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 1, 1, 1, 12),
    _CieIfPacketDiscontinuityTime_Type()
)
cieIfPacketDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cieIfPacketDiscontinuityTime.setStatus("current")
_CieIfInterfaceTable_Object = MibTable
cieIfInterfaceTable = _CieIfInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cieIfInterfaceTable.setStatus("current")
_CieIfInterfaceEntry_Object = MibTableRow
cieIfInterfaceEntry = _CieIfInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 1, 2, 1)
)
cieIfInterfaceEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cieIfInterfaceEntry.setStatus("current")
_CieIfResetCount_Type = Counter32
_CieIfResetCount_Object = MibTableColumn
cieIfResetCount = _CieIfResetCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 1, 2, 1, 1),
    _CieIfResetCount_Type()
)
cieIfResetCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cieIfResetCount.setStatus("current")
_CieIfKeepAliveEnabled_Type = TruthValue
_CieIfKeepAliveEnabled_Object = MibTableColumn
cieIfKeepAliveEnabled = _CieIfKeepAliveEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 1, 2, 1, 2),
    _CieIfKeepAliveEnabled_Type()
)
cieIfKeepAliveEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cieIfKeepAliveEnabled.setStatus("current")
_CieIfStateChangeReason_Type = SnmpAdminString
_CieIfStateChangeReason_Object = MibTableColumn
cieIfStateChangeReason = _CieIfStateChangeReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 1, 2, 1, 3),
    _CieIfStateChangeReason_Type()
)
cieIfStateChangeReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cieIfStateChangeReason.setStatus("current")
_CieIfCarrierTransitionCount_Type = Counter32
_CieIfCarrierTransitionCount_Object = MibTableColumn
cieIfCarrierTransitionCount = _CieIfCarrierTransitionCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 1, 2, 1, 4),
    _CieIfCarrierTransitionCount_Type()
)
cieIfCarrierTransitionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cieIfCarrierTransitionCount.setStatus("current")
_CieIfInterfaceDiscontinuityTime_Type = TimeStamp
_CieIfInterfaceDiscontinuityTime_Object = MibTableColumn
cieIfInterfaceDiscontinuityTime = _CieIfInterfaceDiscontinuityTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 1, 2, 1, 5),
    _CieIfInterfaceDiscontinuityTime_Type()
)
cieIfInterfaceDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cieIfInterfaceDiscontinuityTime.setStatus("current")


class _CieIfDhcpMode_Type(TruthValue):
    """Custom type cieIfDhcpMode based on TruthValue"""


_CieIfDhcpMode_Object = MibTableColumn
cieIfDhcpMode = _CieIfDhcpMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 1, 2, 1, 6),
    _CieIfDhcpMode_Type()
)
cieIfDhcpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cieIfDhcpMode.setStatus("current")


class _CieIfMtu_Type(Integer32):
    """Custom type cieIfMtu based on Integer32"""
    defaultValue = 1500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(40, 2147483647),
    )


_CieIfMtu_Type.__name__ = "Integer32"
_CieIfMtu_Object = MibTableColumn
cieIfMtu = _CieIfMtu_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 1, 2, 1, 7),
    _CieIfMtu_Type()
)
cieIfMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cieIfMtu.setStatus("current")


class _CieIfContextName_Type(OctetString):
    """Custom type cieIfContextName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CieIfContextName_Type.__name__ = "OctetString"
_CieIfContextName_Object = MibTableColumn
cieIfContextName = _CieIfContextName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 1, 2, 1, 8),
    _CieIfContextName_Type()
)
cieIfContextName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cieIfContextName.setStatus("current")
_CieIfOperStatusCause_Type = IfOperStatusReason
_CieIfOperStatusCause_Object = MibTableColumn
cieIfOperStatusCause = _CieIfOperStatusCause_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 1, 2, 1, 9),
    _CieIfOperStatusCause_Type()
)
cieIfOperStatusCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cieIfOperStatusCause.setStatus("current")
_CieIfOperStatusCauseDescr_Type = SnmpAdminString
_CieIfOperStatusCauseDescr_Object = MibTableColumn
cieIfOperStatusCauseDescr = _CieIfOperStatusCauseDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 1, 2, 1, 10),
    _CieIfOperStatusCauseDescr_Type()
)
cieIfOperStatusCauseDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cieIfOperStatusCauseDescr.setStatus("current")
_CieIfSpeedReceive_Type = Gauge32
_CieIfSpeedReceive_Object = MibTableColumn
cieIfSpeedReceive = _CieIfSpeedReceive_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 1, 2, 1, 11),
    _CieIfSpeedReceive_Type()
)
cieIfSpeedReceive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cieIfSpeedReceive.setStatus("current")
_CieIfHighSpeedReceive_Type = Gauge32
_CieIfHighSpeedReceive_Object = MibTableColumn
cieIfHighSpeedReceive = _CieIfHighSpeedReceive_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 1, 2, 1, 12),
    _CieIfHighSpeedReceive_Type()
)
cieIfHighSpeedReceive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cieIfHighSpeedReceive.setStatus("current")


class _CieIfOwner_Type(DisplayString):
    """Custom type cieIfOwner based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_CieIfOwner_Type.__name__ = "DisplayString"
_CieIfOwner_Object = MibTableColumn
cieIfOwner = _CieIfOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 1, 2, 1, 13),
    _CieIfOwner_Type()
)
cieIfOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cieIfOwner.setStatus("current")


class _CieIfSharedConfig_Type(Integer32):
    """Custom type cieIfSharedConfig based on Integer32"""
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
        *(("notApplicable", 1),
          ("ownerDedicated", 2),
          ("ownerShared", 3),
          ("sharedOnly", 4))
    )


_CieIfSharedConfig_Type.__name__ = "Integer32"
_CieIfSharedConfig_Object = MibTableColumn
cieIfSharedConfig = _CieIfSharedConfig_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 1, 2, 1, 14),
    _CieIfSharedConfig_Type()
)
cieIfSharedConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cieIfSharedConfig.setStatus("current")


class _CieIfSpeedGroupConfig_Type(Integer32):
    """Custom type cieIfSpeedGroupConfig based on Integer32"""
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
        *(("notApplicable", 1),
          ("oneTwoFourEightG", 3),
          ("tenG", 2),
          ("twoFourEightSixteenG", 4))
    )


_CieIfSpeedGroupConfig_Type.__name__ = "Integer32"
_CieIfSpeedGroupConfig_Object = MibTableColumn
cieIfSpeedGroupConfig = _CieIfSpeedGroupConfig_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 1, 2, 1, 15),
    _CieIfSpeedGroupConfig_Type()
)
cieIfSpeedGroupConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cieIfSpeedGroupConfig.setStatus("current")


class _CieIfTransceiverFrequencyConfig_Type(Integer32):
    """Custom type cieIfTransceiverFrequencyConfig based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 3),
          ("fibreChannel", 2),
          ("notApplicable", 1))
    )


_CieIfTransceiverFrequencyConfig_Type.__name__ = "Integer32"
_CieIfTransceiverFrequencyConfig_Object = MibTableColumn
cieIfTransceiverFrequencyConfig = _CieIfTransceiverFrequencyConfig_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 1, 2, 1, 16),
    _CieIfTransceiverFrequencyConfig_Type()
)
cieIfTransceiverFrequencyConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cieIfTransceiverFrequencyConfig.setStatus("current")


class _CieIfFillPatternConfig_Type(Integer32):
    """Custom type cieIfFillPatternConfig based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("arbff8G", 1),
          ("idle8G", 2))
    )


_CieIfFillPatternConfig_Type.__name__ = "Integer32"
_CieIfFillPatternConfig_Object = MibTableColumn
cieIfFillPatternConfig = _CieIfFillPatternConfig_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 1, 2, 1, 17),
    _CieIfFillPatternConfig_Type()
)
cieIfFillPatternConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cieIfFillPatternConfig.setStatus("current")


class _CieIfIgnoreBitErrorsConfig_Type(TruthValue):
    """Custom type cieIfIgnoreBitErrorsConfig based on TruthValue"""


_CieIfIgnoreBitErrorsConfig_Object = MibTableColumn
cieIfIgnoreBitErrorsConfig = _CieIfIgnoreBitErrorsConfig_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 1, 2, 1, 18),
    _CieIfIgnoreBitErrorsConfig_Type()
)
cieIfIgnoreBitErrorsConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cieIfIgnoreBitErrorsConfig.setStatus("current")


class _CieIfIgnoreInterruptThresholdConfig_Type(TruthValue):
    """Custom type cieIfIgnoreInterruptThresholdConfig based on TruthValue"""


_CieIfIgnoreInterruptThresholdConfig_Object = MibTableColumn
cieIfIgnoreInterruptThresholdConfig = _CieIfIgnoreInterruptThresholdConfig_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 1, 2, 1, 19),
    _CieIfIgnoreInterruptThresholdConfig_Type()
)
cieIfIgnoreInterruptThresholdConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cieIfIgnoreInterruptThresholdConfig.setStatus("current")
_CieIfStatusListTable_Object = MibTable
cieIfStatusListTable = _CieIfStatusListTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 1, 3)
)
if mibBuilder.loadTexts:
    cieIfStatusListTable.setStatus("current")
_CieIfStatusListEntry_Object = MibTableRow
cieIfStatusListEntry = _CieIfStatusListEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 1, 3, 1)
)
cieIfStatusListEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-IF-EXTENSION-MIB", "cieIfStatusListIndex"),
)
if mibBuilder.loadTexts:
    cieIfStatusListEntry.setStatus("current")


class _CieIfStatusListIndex_Type(Unsigned32):
    """Custom type cieIfStatusListIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 33554432),
    )


_CieIfStatusListIndex_Type.__name__ = "Unsigned32"
_CieIfStatusListIndex_Object = MibTableColumn
cieIfStatusListIndex = _CieIfStatusListIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 1, 3, 1, 1),
    _CieIfStatusListIndex_Type()
)
cieIfStatusListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cieIfStatusListIndex.setStatus("current")
_CieInterfacesIndex_Type = InterfaceIndexList
_CieInterfacesIndex_Object = MibTableColumn
cieInterfacesIndex = _CieInterfacesIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 1, 3, 1, 2),
    _CieInterfacesIndex_Type()
)
cieInterfacesIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cieInterfacesIndex.setStatus("current")
_CieInterfacesOperMode_Type = InterfaceOperModeList
_CieInterfacesOperMode_Object = MibTableColumn
cieInterfacesOperMode = _CieInterfacesOperMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 1, 3, 1, 3),
    _CieInterfacesOperMode_Type()
)
cieInterfacesOperMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cieInterfacesOperMode.setStatus("current")
_CieInterfacesOperCause_Type = InterfaceOperCauseList
_CieInterfacesOperCause_Object = MibTableColumn
cieInterfacesOperCause = _CieInterfacesOperCause_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 1, 3, 1, 4),
    _CieInterfacesOperCause_Type()
)
cieInterfacesOperCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cieInterfacesOperCause.setStatus("current")
_CieInterfaceOwnershipBitmap_Type = InterfaceOwnershipList
_CieInterfaceOwnershipBitmap_Object = MibTableColumn
cieInterfaceOwnershipBitmap = _CieInterfaceOwnershipBitmap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 1, 3, 1, 5),
    _CieInterfaceOwnershipBitmap_Type()
)
cieInterfaceOwnershipBitmap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cieInterfaceOwnershipBitmap.setStatus("current")
_CieIfVlStatsTable_Object = MibTable
cieIfVlStatsTable = _CieIfVlStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 1, 4)
)
if mibBuilder.loadTexts:
    cieIfVlStatsTable.setStatus("current")
_CieIfVlStatsEntry_Object = MibTableRow
cieIfVlStatsEntry = _CieIfVlStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 1, 4, 1)
)
cieIfVlStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cieIfVlStatsEntry.setStatus("current")
_CieIfNoDropVlInPkts_Type = Counter64
_CieIfNoDropVlInPkts_Object = MibTableColumn
cieIfNoDropVlInPkts = _CieIfNoDropVlInPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 1, 4, 1, 1),
    _CieIfNoDropVlInPkts_Type()
)
cieIfNoDropVlInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cieIfNoDropVlInPkts.setStatus("current")
_CieIfNoDropVlInOctets_Type = Counter64
_CieIfNoDropVlInOctets_Object = MibTableColumn
cieIfNoDropVlInOctets = _CieIfNoDropVlInOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 1, 4, 1, 2),
    _CieIfNoDropVlInOctets_Type()
)
cieIfNoDropVlInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cieIfNoDropVlInOctets.setStatus("current")
_CieIfNoDropVlOutPkts_Type = Counter64
_CieIfNoDropVlOutPkts_Object = MibTableColumn
cieIfNoDropVlOutPkts = _CieIfNoDropVlOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 1, 4, 1, 3),
    _CieIfNoDropVlOutPkts_Type()
)
cieIfNoDropVlOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cieIfNoDropVlOutPkts.setStatus("current")
_CieIfNoDropVlOutOctets_Type = Counter64
_CieIfNoDropVlOutOctets_Object = MibTableColumn
cieIfNoDropVlOutOctets = _CieIfNoDropVlOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 1, 4, 1, 4),
    _CieIfNoDropVlOutOctets_Type()
)
cieIfNoDropVlOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cieIfNoDropVlOutOctets.setStatus("current")
_CieIfDropVlInPkts_Type = Counter64
_CieIfDropVlInPkts_Object = MibTableColumn
cieIfDropVlInPkts = _CieIfDropVlInPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 1, 4, 1, 5),
    _CieIfDropVlInPkts_Type()
)
cieIfDropVlInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cieIfDropVlInPkts.setStatus("current")
_CieIfDropVlInOctets_Type = Counter64
_CieIfDropVlInOctets_Object = MibTableColumn
cieIfDropVlInOctets = _CieIfDropVlInOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 1, 4, 1, 6),
    _CieIfDropVlInOctets_Type()
)
cieIfDropVlInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cieIfDropVlInOctets.setStatus("current")
_CieIfDropVlOutPkts_Type = Counter64
_CieIfDropVlOutPkts_Object = MibTableColumn
cieIfDropVlOutPkts = _CieIfDropVlOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 1, 4, 1, 7),
    _CieIfDropVlOutPkts_Type()
)
cieIfDropVlOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cieIfDropVlOutPkts.setStatus("current")
_CieIfDropVlOutOctets_Type = Counter64
_CieIfDropVlOutOctets_Object = MibTableColumn
cieIfDropVlOutOctets = _CieIfDropVlOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 1, 4, 1, 8),
    _CieIfDropVlOutOctets_Type()
)
cieIfDropVlOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cieIfDropVlOutOctets.setStatus("current")
_CiscoIfExtSystemConfig_ObjectIdentity = ObjectIdentity
ciscoIfExtSystemConfig = _CiscoIfExtSystemConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 2)
)


class _CieSystemMtu_Type(Integer32):
    """Custom type cieSystemMtu based on Integer32"""
    defaultValue = 1500


_CieSystemMtu_Object = MibScalar
cieSystemMtu = _CieSystemMtu_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 2, 1),
    _CieSystemMtu_Type()
)
cieSystemMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cieSystemMtu.setStatus("current")


class _CieLinkUpDownEnable_Type(Bits):
    """Custom type cieLinkUpDownEnable based on Bits"""
    defaultBinValue = "1"

    namedValues = NamedValues(
        *(("cisco", 1),
          ("standard", 0))
    )

_CieLinkUpDownEnable_Type.__name__ = "Bits"
_CieLinkUpDownEnable_Object = MibScalar
cieLinkUpDownEnable = _CieLinkUpDownEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 2, 2),
    _CieLinkUpDownEnable_Type()
)
cieLinkUpDownEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cieLinkUpDownEnable.setStatus("deprecated")


class _CieStandardLinkUpDownVarbinds_Type(Integer32):
    """Custom type cieStandardLinkUpDownVarbinds based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("additional", 2),
          ("other", 3),
          ("standard", 1))
    )


_CieStandardLinkUpDownVarbinds_Type.__name__ = "Integer32"
_CieStandardLinkUpDownVarbinds_Object = MibScalar
cieStandardLinkUpDownVarbinds = _CieStandardLinkUpDownVarbinds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 2, 3),
    _CieStandardLinkUpDownVarbinds_Type()
)
cieStandardLinkUpDownVarbinds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cieStandardLinkUpDownVarbinds.setStatus("deprecated")


class _CieIfIndexPersistence_Type(TruthValue):
    """Custom type cieIfIndexPersistence based on TruthValue"""


_CieIfIndexPersistence_Object = MibScalar
cieIfIndexPersistence = _CieIfIndexPersistence_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 2, 4),
    _CieIfIndexPersistence_Type()
)
cieIfIndexPersistence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cieIfIndexPersistence.setStatus("deprecated")
_CieIfIndexPersistenceTable_Object = MibTable
cieIfIndexPersistenceTable = _CieIfIndexPersistenceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 2, 5)
)
if mibBuilder.loadTexts:
    cieIfIndexPersistenceTable.setStatus("current")
_CieIfIndexPersistenceEntry_Object = MibTableRow
cieIfIndexPersistenceEntry = _CieIfIndexPersistenceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 2, 5, 1)
)
cieIfIndexPersistenceEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cieIfIndexPersistenceEntry.setStatus("current")


class _CieIfIndexPersistenceEnabled_Type(TruthValue):
    """Custom type cieIfIndexPersistenceEnabled based on TruthValue"""


_CieIfIndexPersistenceEnabled_Object = MibTableColumn
cieIfIndexPersistenceEnabled = _CieIfIndexPersistenceEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 2, 5, 1, 1),
    _CieIfIndexPersistenceEnabled_Type()
)
cieIfIndexPersistenceEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cieIfIndexPersistenceEnabled.setStatus("deprecated")


class _CieIfIndexPersistenceControl_Type(IfIndexPersistenceState):
    """Custom type cieIfIndexPersistenceControl based on IfIndexPersistenceState"""


_CieIfIndexPersistenceControl_Object = MibTableColumn
cieIfIndexPersistenceControl = _CieIfIndexPersistenceControl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 2, 5, 1, 2),
    _CieIfIndexPersistenceControl_Type()
)
cieIfIndexPersistenceControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cieIfIndexPersistenceControl.setStatus("current")


class _CieDelayedLinkUpDownNotifEnable_Type(TruthValue):
    """Custom type cieDelayedLinkUpDownNotifEnable based on TruthValue"""


_CieDelayedLinkUpDownNotifEnable_Object = MibScalar
cieDelayedLinkUpDownNotifEnable = _CieDelayedLinkUpDownNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 2, 6),
    _CieDelayedLinkUpDownNotifEnable_Type()
)
cieDelayedLinkUpDownNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cieDelayedLinkUpDownNotifEnable.setStatus("current")


class _CieDelayedLinkUpDownNotifDelay_Type(Unsigned32):
    """Custom type cieDelayedLinkUpDownNotifDelay based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_CieDelayedLinkUpDownNotifDelay_Type.__name__ = "Unsigned32"
_CieDelayedLinkUpDownNotifDelay_Object = MibScalar
cieDelayedLinkUpDownNotifDelay = _CieDelayedLinkUpDownNotifDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 2, 7),
    _CieDelayedLinkUpDownNotifDelay_Type()
)
cieDelayedLinkUpDownNotifDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cieDelayedLinkUpDownNotifDelay.setStatus("current")
if mibBuilder.loadTexts:
    cieDelayedLinkUpDownNotifDelay.setUnits("minutes")


class _CieIfIndexGlobalPersistence_Type(IfIndexPersistenceState):
    """Custom type cieIfIndexGlobalPersistence based on IfIndexPersistenceState"""


_CieIfIndexGlobalPersistence_Object = MibScalar
cieIfIndexGlobalPersistence = _CieIfIndexGlobalPersistence_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 2, 8),
    _CieIfIndexGlobalPersistence_Type()
)
cieIfIndexGlobalPersistence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cieIfIndexGlobalPersistence.setStatus("current")


class _CieLinkUpDownConfig_Type(Bits):
    """Custom type cieLinkUpDownConfig based on Bits"""
    namedValues = NamedValues(
        *(("additionalLinkDown", 3),
          ("additionalLinkUp", 2),
          ("ciscoLinkDown", 5),
          ("ciscoLinkUp", 4),
          ("standardLinkDown", 1),
          ("standardLinkUp", 0))
    )

_CieLinkUpDownConfig_Type.__name__ = "Bits"
_CieLinkUpDownConfig_Object = MibScalar
cieLinkUpDownConfig = _CieLinkUpDownConfig_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 2, 9),
    _CieLinkUpDownConfig_Type()
)
cieLinkUpDownConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cieLinkUpDownConfig.setStatus("current")
_CiscoIfExtDot1qCustomEtherType_ObjectIdentity = ObjectIdentity
ciscoIfExtDot1qCustomEtherType = _CiscoIfExtDot1qCustomEtherType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 3)
)
_CieIfDot1qCustomEtherTypeTable_Object = MibTable
cieIfDot1qCustomEtherTypeTable = _CieIfDot1qCustomEtherTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cieIfDot1qCustomEtherTypeTable.setStatus("current")
_CieIfDot1qCustomEtherTypeEntry_Object = MibTableRow
cieIfDot1qCustomEtherTypeEntry = _CieIfDot1qCustomEtherTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 3, 1, 1)
)
cieIfDot1qCustomEtherTypeEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cieIfDot1qCustomEtherTypeEntry.setStatus("current")


class _CieIfDot1qCustomAdminEtherType_Type(Integer32):
    """Custom type cieIfDot1qCustomAdminEtherType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CieIfDot1qCustomAdminEtherType_Type.__name__ = "Integer32"
_CieIfDot1qCustomAdminEtherType_Object = MibTableColumn
cieIfDot1qCustomAdminEtherType = _CieIfDot1qCustomAdminEtherType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 3, 1, 1, 1),
    _CieIfDot1qCustomAdminEtherType_Type()
)
cieIfDot1qCustomAdminEtherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cieIfDot1qCustomAdminEtherType.setStatus("current")


class _CieIfDot1qCustomOperEtherType_Type(Integer32):
    """Custom type cieIfDot1qCustomOperEtherType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CieIfDot1qCustomOperEtherType_Type.__name__ = "Integer32"
_CieIfDot1qCustomOperEtherType_Object = MibTableColumn
cieIfDot1qCustomOperEtherType = _CieIfDot1qCustomOperEtherType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 3, 1, 1, 2),
    _CieIfDot1qCustomOperEtherType_Type()
)
cieIfDot1qCustomOperEtherType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cieIfDot1qCustomOperEtherType.setStatus("current")
_CiscoIfExtUtilization_ObjectIdentity = ObjectIdentity
ciscoIfExtUtilization = _CiscoIfExtUtilization_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 4)
)
_CieIfUtilTable_Object = MibTable
cieIfUtilTable = _CieIfUtilTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cieIfUtilTable.setStatus("current")
_CieIfUtilEntry_Object = MibTableRow
cieIfUtilEntry = _CieIfUtilEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 4, 1, 1)
)
cieIfUtilEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cieIfUtilEntry.setStatus("current")
_CieIfInPktRate_Type = Counter64
_CieIfInPktRate_Object = MibTableColumn
cieIfInPktRate = _CieIfInPktRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 4, 1, 1, 1),
    _CieIfInPktRate_Type()
)
cieIfInPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cieIfInPktRate.setStatus("current")
if mibBuilder.loadTexts:
    cieIfInPktRate.setUnits("packets per second")
_CieIfInOctetRate_Type = Counter64
_CieIfInOctetRate_Object = MibTableColumn
cieIfInOctetRate = _CieIfInOctetRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 4, 1, 1, 2),
    _CieIfInOctetRate_Type()
)
cieIfInOctetRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cieIfInOctetRate.setStatus("current")
if mibBuilder.loadTexts:
    cieIfInOctetRate.setUnits("octets per second")
_CieIfOutPktRate_Type = Counter64
_CieIfOutPktRate_Object = MibTableColumn
cieIfOutPktRate = _CieIfOutPktRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 4, 1, 1, 3),
    _CieIfOutPktRate_Type()
)
cieIfOutPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cieIfOutPktRate.setStatus("current")
if mibBuilder.loadTexts:
    cieIfOutPktRate.setUnits("packets per second")
_CieIfOutOctetRate_Type = Counter64
_CieIfOutOctetRate_Object = MibTableColumn
cieIfOutOctetRate = _CieIfOutOctetRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 4, 1, 1, 4),
    _CieIfOutOctetRate_Type()
)
cieIfOutOctetRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cieIfOutOctetRate.setStatus("current")
if mibBuilder.loadTexts:
    cieIfOutOctetRate.setUnits("octets per second")


class _CieIfInterval_Type(Unsigned32):
    """Custom type cieIfInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CieIfInterval_Type.__name__ = "Unsigned32"
_CieIfInterval_Object = MibTableColumn
cieIfInterval = _CieIfInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 4, 1, 1, 5),
    _CieIfInterval_Type()
)
cieIfInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cieIfInterval.setStatus("current")
if mibBuilder.loadTexts:
    cieIfInterval.setUnits("seconds")
_CiscoIfExtDot1dBaseMapping_ObjectIdentity = ObjectIdentity
ciscoIfExtDot1dBaseMapping = _CiscoIfExtDot1dBaseMapping_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 5)
)
_CieIfDot1dBaseMappingTable_Object = MibTable
cieIfDot1dBaseMappingTable = _CieIfDot1dBaseMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 5, 1)
)
if mibBuilder.loadTexts:
    cieIfDot1dBaseMappingTable.setStatus("current")
_CieIfDot1dBaseMappingEntry_Object = MibTableRow
cieIfDot1dBaseMappingEntry = _CieIfDot1dBaseMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 5, 1, 1)
)
cieIfDot1dBaseMappingEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cieIfDot1dBaseMappingEntry.setStatus("current")


class _CieIfDot1dBaseMappingPort_Type(Integer32):
    """Custom type cieIfDot1dBaseMappingPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CieIfDot1dBaseMappingPort_Type.__name__ = "Integer32"
_CieIfDot1dBaseMappingPort_Object = MibTableColumn
cieIfDot1dBaseMappingPort = _CieIfDot1dBaseMappingPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 5, 1, 1, 1),
    _CieIfDot1dBaseMappingPort_Type()
)
cieIfDot1dBaseMappingPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cieIfDot1dBaseMappingPort.setStatus("current")
_CiscoIfExtIfNameMapping_ObjectIdentity = ObjectIdentity
ciscoIfExtIfNameMapping = _CiscoIfExtIfNameMapping_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 6)
)
_CieIfNameMappingTable_Object = MibTable
cieIfNameMappingTable = _CieIfNameMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 6, 1)
)
if mibBuilder.loadTexts:
    cieIfNameMappingTable.setStatus("current")
_CieIfNameMappingEntry_Object = MibTableRow
cieIfNameMappingEntry = _CieIfNameMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 6, 1, 1)
)
cieIfNameMappingEntry.setIndexNames(
    (0, "CISCO-IF-EXTENSION-MIB", "cieIfName"),
)
if mibBuilder.loadTexts:
    cieIfNameMappingEntry.setStatus("current")


class _CieIfName_Type(DisplayString):
    """Custom type cieIfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 112),
    )


_CieIfName_Type.__name__ = "DisplayString"
_CieIfName_Object = MibTableColumn
cieIfName = _CieIfName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 6, 1, 1, 1),
    _CieIfName_Type()
)
cieIfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cieIfName.setStatus("current")
_CieIfIndex_Type = InterfaceIndexOrZero
_CieIfIndex_Object = MibTableColumn
cieIfIndex = _CieIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 1, 6, 1, 1, 2),
    _CieIfIndex_Type()
)
cieIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cieIfIndex.setStatus("current")
_CiscoIfExtensionMIBConformance_ObjectIdentity = ObjectIdentity
ciscoIfExtensionMIBConformance = _CiscoIfExtensionMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 2)
)
_CiscoIfExtensionMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoIfExtensionMIBCompliances = _CiscoIfExtensionMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 2, 1)
)
_CiscoIfExtensionMIBGroups_ObjectIdentity = ObjectIdentity
ciscoIfExtensionMIBGroups = _CiscoIfExtensionMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 2, 2)
)

# Managed Objects groups

ciscoIfExtensionTablePacketGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 2, 2, 1)
)
ciscoIfExtensionTablePacketGroup.setObjects(
      *(("CISCO-IF-EXTENSION-MIB", "cieIfLastInTime"),
        ("CISCO-IF-EXTENSION-MIB", "cieIfLastOutTime"),
        ("CISCO-IF-EXTENSION-MIB", "cieIfLastOutHangTime"),
        ("CISCO-IF-EXTENSION-MIB", "cieIfInRuntsErrs"),
        ("CISCO-IF-EXTENSION-MIB", "cieIfInGiantsErrs"),
        ("CISCO-IF-EXTENSION-MIB", "cieIfInFramingErrs"),
        ("CISCO-IF-EXTENSION-MIB", "cieIfInOverrunErrs"),
        ("CISCO-IF-EXTENSION-MIB", "cieIfInIgnored"),
        ("CISCO-IF-EXTENSION-MIB", "cieIfInAbortErrs"),
        ("CISCO-IF-EXTENSION-MIB", "cieIfInputQueueDrops"),
        ("CISCO-IF-EXTENSION-MIB", "cieIfOutputQueueDrops"),
        ("CISCO-IF-EXTENSION-MIB", "cieIfPacketDiscontinuityTime"))
)
if mibBuilder.loadTexts:
    ciscoIfExtensionTablePacketGroup.setStatus("current")

ciscoIfExtensionTableIntfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 2, 2, 2)
)
ciscoIfExtensionTableIntfGroup.setObjects(
      *(("CISCO-IF-EXTENSION-MIB", "cieIfResetCount"),
        ("CISCO-IF-EXTENSION-MIB", "cieIfKeepAliveEnabled"),
        ("CISCO-IF-EXTENSION-MIB", "cieIfStateChangeReason"),
        ("CISCO-IF-EXTENSION-MIB", "cieIfCarrierTransitionCount"),
        ("CISCO-IF-EXTENSION-MIB", "cieIfInterfaceDiscontinuityTime"))
)
if mibBuilder.loadTexts:
    ciscoIfExtensionTableIntfGroup.setStatus("current")

ciscoIfExtensionTableIntfGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 2, 2, 3)
)
ciscoIfExtensionTableIntfGroup1.setObjects(
      *(("CISCO-IF-EXTENSION-MIB", "cieIfDhcpMode"),
        ("CISCO-IF-EXTENSION-MIB", "cieIfMtu"),
        ("CISCO-IF-EXTENSION-MIB", "cieIfContextName"))
)
if mibBuilder.loadTexts:
    ciscoIfExtensionTableIntfGroup1.setStatus("deprecated")

ciscoIfExtensionSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 2, 2, 4)
)
ciscoIfExtensionSystemGroup.setObjects(
    ("CISCO-IF-EXTENSION-MIB", "cieSystemMtu")
)
if mibBuilder.loadTexts:
    ciscoIfExtensionSystemGroup.setStatus("current")

ciscoIfExtDot1qEtherTypeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 2, 2, 5)
)
ciscoIfExtDot1qEtherTypeGroup.setObjects(
      *(("CISCO-IF-EXTENSION-MIB", "cieIfDot1qCustomAdminEtherType"),
        ("CISCO-IF-EXTENSION-MIB", "cieIfDot1qCustomOperEtherType"))
)
if mibBuilder.loadTexts:
    ciscoIfExtDot1qEtherTypeGroup.setStatus("current")

ciscoIfExtUtilizationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 2, 2, 6)
)
ciscoIfExtUtilizationGroup.setObjects(
      *(("CISCO-IF-EXTENSION-MIB", "cieIfInPktRate"),
        ("CISCO-IF-EXTENSION-MIB", "cieIfInOctetRate"),
        ("CISCO-IF-EXTENSION-MIB", "cieIfOutPktRate"),
        ("CISCO-IF-EXTENSION-MIB", "cieIfOutOctetRate"))
)
if mibBuilder.loadTexts:
    ciscoIfExtUtilizationGroup.setStatus("current")

ciscoIfExtDot1dBaseMappingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 2, 2, 7)
)
ciscoIfExtDot1dBaseMappingGroup.setObjects(
    ("CISCO-IF-EXTENSION-MIB", "cieIfDot1dBaseMappingPort")
)
if mibBuilder.loadTexts:
    ciscoIfExtDot1dBaseMappingGroup.setStatus("current")

ciscoIfExtIfNameMappingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 2, 2, 8)
)
ciscoIfExtIfNameMappingGroup.setObjects(
    ("CISCO-IF-EXTENSION-MIB", "cieIfIndex")
)
if mibBuilder.loadTexts:
    ciscoIfExtIfNameMappingGroup.setStatus("current")

ciscoIfExtensionTableIntfGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 2, 2, 9)
)
ciscoIfExtensionTableIntfGroup2.setObjects(
      *(("CISCO-IF-EXTENSION-MIB", "cieIfDhcpMode"),
        ("CISCO-IF-EXTENSION-MIB", "cieIfMtu"),
        ("CISCO-IF-EXTENSION-MIB", "cieIfContextName"),
        ("CISCO-IF-EXTENSION-MIB", "cieIfOperStatusCause"),
        ("CISCO-IF-EXTENSION-MIB", "cieIfOperStatusCauseDescr"))
)
if mibBuilder.loadTexts:
    ciscoIfExtensionTableIntfGroup2.setStatus("deprecated")

cieIfStatusListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 2, 2, 10)
)
cieIfStatusListGroup.setObjects(
      *(("CISCO-IF-EXTENSION-MIB", "cieInterfacesIndex"),
        ("CISCO-IF-EXTENSION-MIB", "cieInterfacesOperMode"),
        ("CISCO-IF-EXTENSION-MIB", "cieInterfacesOperCause"))
)
if mibBuilder.loadTexts:
    cieIfStatusListGroup.setStatus("current")

cieLinkUpDownNotifEnableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 2, 2, 11)
)
cieLinkUpDownNotifEnableGroup.setObjects(
      *(("CISCO-IF-EXTENSION-MIB", "cieLinkUpDownEnable"),
        ("CISCO-IF-EXTENSION-MIB", "cieStandardLinkUpDownVarbinds"))
)
if mibBuilder.loadTexts:
    cieLinkUpDownNotifEnableGroup.setStatus("deprecated")

ciscoIfExtensionAsymmetricalSpeedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 2, 2, 13)
)
ciscoIfExtensionAsymmetricalSpeedGroup.setObjects(
      *(("CISCO-IF-EXTENSION-MIB", "cieIfSpeedReceive"),
        ("CISCO-IF-EXTENSION-MIB", "cieIfHighSpeedReceive"))
)
if mibBuilder.loadTexts:
    ciscoIfExtensionAsymmetricalSpeedGroup.setStatus("current")

ciscoIfExtUtilIntervalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 2, 2, 14)
)
ciscoIfExtUtilIntervalGroup.setObjects(
    ("CISCO-IF-EXTENSION-MIB", "cieIfInterval")
)
if mibBuilder.loadTexts:
    ciscoIfExtUtilIntervalGroup.setStatus("current")

cieIfIndexPersistenceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 2, 2, 15)
)
cieIfIndexPersistenceGroup.setObjects(
      *(("CISCO-IF-EXTENSION-MIB", "cieIfIndexPersistence"),
        ("CISCO-IF-EXTENSION-MIB", "cieIfIndexPersistenceEnabled"))
)
if mibBuilder.loadTexts:
    cieIfIndexPersistenceGroup.setStatus("deprecated")

cieDelayedLinkUpDownNotifNotifEnableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 2, 2, 16)
)
cieDelayedLinkUpDownNotifNotifEnableGroup.setObjects(
      *(("CISCO-IF-EXTENSION-MIB", "cieDelayedLinkUpDownNotifEnable"),
        ("CISCO-IF-EXTENSION-MIB", "cieDelayedLinkUpDownNotifDelay"))
)
if mibBuilder.loadTexts:
    cieDelayedLinkUpDownNotifNotifEnableGroup.setStatus("current")

cieIfIndexPersistenceControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 2, 2, 18)
)
cieIfIndexPersistenceControlGroup.setObjects(
      *(("CISCO-IF-EXTENSION-MIB", "cieIfIndexGlobalPersistence"),
        ("CISCO-IF-EXTENSION-MIB", "cieIfIndexPersistenceControl"))
)
if mibBuilder.loadTexts:
    cieIfIndexPersistenceControlGroup.setStatus("current")

ciscoIfExtensionTableIntfGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 2, 2, 19)
)
ciscoIfExtensionTableIntfGroup3.setObjects(
      *(("CISCO-IF-EXTENSION-MIB", "cieIfDhcpMode"),
        ("CISCO-IF-EXTENSION-MIB", "cieIfMtu"),
        ("CISCO-IF-EXTENSION-MIB", "cieIfContextName"),
        ("CISCO-IF-EXTENSION-MIB", "cieIfOperStatusCause"),
        ("CISCO-IF-EXTENSION-MIB", "cieIfOperStatusCauseDescr"),
        ("CISCO-IF-EXTENSION-MIB", "cieIfOwner"))
)
if mibBuilder.loadTexts:
    ciscoIfExtensionTableIntfGroup3.setStatus("current")

cieIfStatusListGroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 2, 2, 20)
)
cieIfStatusListGroupSup1.setObjects(
    ("CISCO-IF-EXTENSION-MIB", "cieInterfaceOwnershipBitmap")
)
if mibBuilder.loadTexts:
    cieIfStatusListGroupSup1.setStatus("current")

cieIfVlStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 2, 2, 21)
)
cieIfVlStatsGroup.setObjects(
      *(("CISCO-IF-EXTENSION-MIB", "cieIfNoDropVlInPkts"),
        ("CISCO-IF-EXTENSION-MIB", "cieIfNoDropVlInOctets"),
        ("CISCO-IF-EXTENSION-MIB", "cieIfNoDropVlOutPkts"),
        ("CISCO-IF-EXTENSION-MIB", "cieIfNoDropVlOutOctets"),
        ("CISCO-IF-EXTENSION-MIB", "cieIfDropVlInPkts"),
        ("CISCO-IF-EXTENSION-MIB", "cieIfDropVlInOctets"),
        ("CISCO-IF-EXTENSION-MIB", "cieIfDropVlOutPkts"),
        ("CISCO-IF-EXTENSION-MIB", "cieIfDropVlOutOctets"))
)
if mibBuilder.loadTexts:
    cieIfVlStatsGroup.setStatus("current")

ciscoIfExtensionTableIntfGroup3SupR01 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 2, 2, 22)
)
ciscoIfExtensionTableIntfGroup3SupR01.setObjects(
      *(("CISCO-IF-EXTENSION-MIB", "cieIfSharedConfig"),
        ("CISCO-IF-EXTENSION-MIB", "cieIfSpeedGroupConfig"))
)
if mibBuilder.loadTexts:
    ciscoIfExtensionTableIntfGroup3SupR01.setStatus("current")

cieLinkUpDownNotifConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 2, 2, 23)
)
cieLinkUpDownNotifConfigGroup.setObjects(
    ("CISCO-IF-EXTENSION-MIB", "cieLinkUpDownConfig")
)
if mibBuilder.loadTexts:
    cieLinkUpDownNotifConfigGroup.setStatus("current")

ciscoIfExtensionTableIntfGroup3SupR02 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 2, 2, 24)
)
ciscoIfExtensionTableIntfGroup3SupR02.setObjects(
      *(("CISCO-IF-EXTENSION-MIB", "cieIfTransceiverFrequencyConfig"),
        ("CISCO-IF-EXTENSION-MIB", "cieIfFillPatternConfig"),
        ("CISCO-IF-EXTENSION-MIB", "cieIfIgnoreBitErrorsConfig"),
        ("CISCO-IF-EXTENSION-MIB", "cieIfIgnoreInterruptThresholdConfig"))
)
if mibBuilder.loadTexts:
    ciscoIfExtensionTableIntfGroup3SupR02.setStatus("current")


# Notification objects

cieLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 0, 1)
)
cieLinkDown.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifAdminStatus"),
        ("IF-MIB", "ifOperStatus"),
        ("IF-MIB", "ifName"),
        ("IF-MIB", "ifType"))
)
if mibBuilder.loadTexts:
    cieLinkDown.setStatus(
        "current"
    )

cieLinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 0, 2)
)
cieLinkUp.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifAdminStatus"),
        ("IF-MIB", "ifOperStatus"),
        ("IF-MIB", "ifName"),
        ("IF-MIB", "ifType"))
)
if mibBuilder.loadTexts:
    cieLinkUp.setStatus(
        "current"
    )

cieDelayedLinkUpDownNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 0, 3)
)
cieDelayedLinkUpDownNotif.setObjects(
      *(("IF-MIB", "ifAdminStatus"),
        ("IF-MIB", "ifOperStatus"),
        ("IF-MIB", "ifName"),
        ("IF-MIB", "ifType"),
        ("CISCO-IF-EXTENSION-MIB", "cieIfOperStatusCause"))
)
if mibBuilder.loadTexts:
    cieDelayedLinkUpDownNotif.setStatus(
        "current"
    )


# Notifications groups

cieLinkUpDownNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 2, 2, 12)
)
cieLinkUpDownNotifGroup.setObjects(
      *(("CISCO-IF-EXTENSION-MIB", "cieLinkDown"),
        ("CISCO-IF-EXTENSION-MIB", "cieLinkUp"))
)
if mibBuilder.loadTexts:
    cieLinkUpDownNotifGroup.setStatus(
        "current"
    )

cieDelayedLinkUpDownNotifNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 2, 2, 17)
)
cieDelayedLinkUpDownNotifNotifGroup.setObjects(
    ("CISCO-IF-EXTENSION-MIB", "cieDelayedLinkUpDownNotif")
)
if mibBuilder.loadTexts:
    cieDelayedLinkUpDownNotifNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoIfExtensionMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoIfExtensionMIBCompliance.setStatus(
        "deprecated"
    )

ciscoIfExtensionMIBCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoIfExtensionMIBCompliance1.setStatus(
        "deprecated"
    )

ciscoIfExtensionMIBCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 2, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoIfExtensionMIBCompliance2.setStatus(
        "deprecated"
    )

ciscoIfExtensionMIBCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 2, 1, 4)
)
if mibBuilder.loadTexts:
    ciscoIfExtensionMIBCompliance3.setStatus(
        "deprecated"
    )

ciscoIfExtensionMIBCompliance4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 2, 1, 5)
)
if mibBuilder.loadTexts:
    ciscoIfExtensionMIBCompliance4.setStatus(
        "deprecated"
    )

ciscoIfExtensionMIBCompliance5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 2, 1, 6)
)
if mibBuilder.loadTexts:
    ciscoIfExtensionMIBCompliance5.setStatus(
        "deprecated"
    )

ciscoIfExtensionMIBCompliance6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 2, 1, 7)
)
if mibBuilder.loadTexts:
    ciscoIfExtensionMIBCompliance6.setStatus(
        "deprecated"
    )

ciscoIfExtensionMIBCompliance7 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 2, 1, 8)
)
if mibBuilder.loadTexts:
    ciscoIfExtensionMIBCompliance7.setStatus(
        "deprecated"
    )

ciscoIfExtensionMIBCompliance8 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 2, 1, 9)
)
if mibBuilder.loadTexts:
    ciscoIfExtensionMIBCompliance8.setStatus(
        "deprecated"
    )

ciscoIfExtensionMIBCompliance9 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 2, 1, 10)
)
if mibBuilder.loadTexts:
    ciscoIfExtensionMIBCompliance9.setStatus(
        "deprecated"
    )

ciscoIfExtensionMIBCompliance10 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 2, 1, 11)
)
if mibBuilder.loadTexts:
    ciscoIfExtensionMIBCompliance10.setStatus(
        "deprecated"
    )

ciscoIfExtensionMIBCompliance11 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 2, 1, 12)
)
if mibBuilder.loadTexts:
    ciscoIfExtensionMIBCompliance11.setStatus(
        "deprecated"
    )

ciscoIfExtensionMIBCompliance12 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 2, 1, 13)
)
if mibBuilder.loadTexts:
    ciscoIfExtensionMIBCompliance12.setStatus(
        "deprecated"
    )

ciscoIfExtensionMIBCompliance13 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 2, 1, 14)
)
if mibBuilder.loadTexts:
    ciscoIfExtensionMIBCompliance13.setStatus(
        "deprecated"
    )

ciscoIfExtensionMIBCompliance14 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 2, 1, 15)
)
if mibBuilder.loadTexts:
    ciscoIfExtensionMIBCompliance14.setStatus(
        "deprecated"
    )

ciscoIfExtensionMIBCompliance15 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 276, 2, 1, 16)
)
if mibBuilder.loadTexts:
    ciscoIfExtensionMIBCompliance15.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-IF-EXTENSION-MIB",
    **{"InterfaceIndexList": InterfaceIndexList,
       "InterfaceOperModeList": InterfaceOperModeList,
       "InterfaceOperCauseList": InterfaceOperCauseList,
       "InterfaceOwnershipList": InterfaceOwnershipList,
       "IfIndexPersistenceState": IfIndexPersistenceState,
       "ciscoIfExtensionMIB": ciscoIfExtensionMIB,
       "ciscoIfExtensionMIBNotifications": ciscoIfExtensionMIBNotifications,
       "cieLinkDown": cieLinkDown,
       "cieLinkUp": cieLinkUp,
       "cieDelayedLinkUpDownNotif": cieDelayedLinkUpDownNotif,
       "ciscoIfExtensionMIBObjects": ciscoIfExtensionMIBObjects,
       "ciscoIfExtensionStats": ciscoIfExtensionStats,
       "cieIfPacketStatsTable": cieIfPacketStatsTable,
       "cieIfPacketStatsEntry": cieIfPacketStatsEntry,
       "cieIfLastInTime": cieIfLastInTime,
       "cieIfLastOutTime": cieIfLastOutTime,
       "cieIfLastOutHangTime": cieIfLastOutHangTime,
       "cieIfInRuntsErrs": cieIfInRuntsErrs,
       "cieIfInGiantsErrs": cieIfInGiantsErrs,
       "cieIfInFramingErrs": cieIfInFramingErrs,
       "cieIfInOverrunErrs": cieIfInOverrunErrs,
       "cieIfInIgnored": cieIfInIgnored,
       "cieIfInAbortErrs": cieIfInAbortErrs,
       "cieIfInputQueueDrops": cieIfInputQueueDrops,
       "cieIfOutputQueueDrops": cieIfOutputQueueDrops,
       "cieIfPacketDiscontinuityTime": cieIfPacketDiscontinuityTime,
       "cieIfInterfaceTable": cieIfInterfaceTable,
       "cieIfInterfaceEntry": cieIfInterfaceEntry,
       "cieIfResetCount": cieIfResetCount,
       "cieIfKeepAliveEnabled": cieIfKeepAliveEnabled,
       "cieIfStateChangeReason": cieIfStateChangeReason,
       "cieIfCarrierTransitionCount": cieIfCarrierTransitionCount,
       "cieIfInterfaceDiscontinuityTime": cieIfInterfaceDiscontinuityTime,
       "cieIfDhcpMode": cieIfDhcpMode,
       "cieIfMtu": cieIfMtu,
       "cieIfContextName": cieIfContextName,
       "cieIfOperStatusCause": cieIfOperStatusCause,
       "cieIfOperStatusCauseDescr": cieIfOperStatusCauseDescr,
       "cieIfSpeedReceive": cieIfSpeedReceive,
       "cieIfHighSpeedReceive": cieIfHighSpeedReceive,
       "cieIfOwner": cieIfOwner,
       "cieIfSharedConfig": cieIfSharedConfig,
       "cieIfSpeedGroupConfig": cieIfSpeedGroupConfig,
       "cieIfTransceiverFrequencyConfig": cieIfTransceiverFrequencyConfig,
       "cieIfFillPatternConfig": cieIfFillPatternConfig,
       "cieIfIgnoreBitErrorsConfig": cieIfIgnoreBitErrorsConfig,
       "cieIfIgnoreInterruptThresholdConfig": cieIfIgnoreInterruptThresholdConfig,
       "cieIfStatusListTable": cieIfStatusListTable,
       "cieIfStatusListEntry": cieIfStatusListEntry,
       "cieIfStatusListIndex": cieIfStatusListIndex,
       "cieInterfacesIndex": cieInterfacesIndex,
       "cieInterfacesOperMode": cieInterfacesOperMode,
       "cieInterfacesOperCause": cieInterfacesOperCause,
       "cieInterfaceOwnershipBitmap": cieInterfaceOwnershipBitmap,
       "cieIfVlStatsTable": cieIfVlStatsTable,
       "cieIfVlStatsEntry": cieIfVlStatsEntry,
       "cieIfNoDropVlInPkts": cieIfNoDropVlInPkts,
       "cieIfNoDropVlInOctets": cieIfNoDropVlInOctets,
       "cieIfNoDropVlOutPkts": cieIfNoDropVlOutPkts,
       "cieIfNoDropVlOutOctets": cieIfNoDropVlOutOctets,
       "cieIfDropVlInPkts": cieIfDropVlInPkts,
       "cieIfDropVlInOctets": cieIfDropVlInOctets,
       "cieIfDropVlOutPkts": cieIfDropVlOutPkts,
       "cieIfDropVlOutOctets": cieIfDropVlOutOctets,
       "ciscoIfExtSystemConfig": ciscoIfExtSystemConfig,
       "cieSystemMtu": cieSystemMtu,
       "cieLinkUpDownEnable": cieLinkUpDownEnable,
       "cieStandardLinkUpDownVarbinds": cieStandardLinkUpDownVarbinds,
       "cieIfIndexPersistence": cieIfIndexPersistence,
       "cieIfIndexPersistenceTable": cieIfIndexPersistenceTable,
       "cieIfIndexPersistenceEntry": cieIfIndexPersistenceEntry,
       "cieIfIndexPersistenceEnabled": cieIfIndexPersistenceEnabled,
       "cieIfIndexPersistenceControl": cieIfIndexPersistenceControl,
       "cieDelayedLinkUpDownNotifEnable": cieDelayedLinkUpDownNotifEnable,
       "cieDelayedLinkUpDownNotifDelay": cieDelayedLinkUpDownNotifDelay,
       "cieIfIndexGlobalPersistence": cieIfIndexGlobalPersistence,
       "cieLinkUpDownConfig": cieLinkUpDownConfig,
       "ciscoIfExtDot1qCustomEtherType": ciscoIfExtDot1qCustomEtherType,
       "cieIfDot1qCustomEtherTypeTable": cieIfDot1qCustomEtherTypeTable,
       "cieIfDot1qCustomEtherTypeEntry": cieIfDot1qCustomEtherTypeEntry,
       "cieIfDot1qCustomAdminEtherType": cieIfDot1qCustomAdminEtherType,
       "cieIfDot1qCustomOperEtherType": cieIfDot1qCustomOperEtherType,
       "ciscoIfExtUtilization": ciscoIfExtUtilization,
       "cieIfUtilTable": cieIfUtilTable,
       "cieIfUtilEntry": cieIfUtilEntry,
       "cieIfInPktRate": cieIfInPktRate,
       "cieIfInOctetRate": cieIfInOctetRate,
       "cieIfOutPktRate": cieIfOutPktRate,
       "cieIfOutOctetRate": cieIfOutOctetRate,
       "cieIfInterval": cieIfInterval,
       "ciscoIfExtDot1dBaseMapping": ciscoIfExtDot1dBaseMapping,
       "cieIfDot1dBaseMappingTable": cieIfDot1dBaseMappingTable,
       "cieIfDot1dBaseMappingEntry": cieIfDot1dBaseMappingEntry,
       "cieIfDot1dBaseMappingPort": cieIfDot1dBaseMappingPort,
       "ciscoIfExtIfNameMapping": ciscoIfExtIfNameMapping,
       "cieIfNameMappingTable": cieIfNameMappingTable,
       "cieIfNameMappingEntry": cieIfNameMappingEntry,
       "cieIfName": cieIfName,
       "cieIfIndex": cieIfIndex,
       "ciscoIfExtensionMIBConformance": ciscoIfExtensionMIBConformance,
       "ciscoIfExtensionMIBCompliances": ciscoIfExtensionMIBCompliances,
       "ciscoIfExtensionMIBCompliance": ciscoIfExtensionMIBCompliance,
       "ciscoIfExtensionMIBCompliance1": ciscoIfExtensionMIBCompliance1,
       "ciscoIfExtensionMIBCompliance2": ciscoIfExtensionMIBCompliance2,
       "ciscoIfExtensionMIBCompliance3": ciscoIfExtensionMIBCompliance3,
       "ciscoIfExtensionMIBCompliance4": ciscoIfExtensionMIBCompliance4,
       "ciscoIfExtensionMIBCompliance5": ciscoIfExtensionMIBCompliance5,
       "ciscoIfExtensionMIBCompliance6": ciscoIfExtensionMIBCompliance6,
       "ciscoIfExtensionMIBCompliance7": ciscoIfExtensionMIBCompliance7,
       "ciscoIfExtensionMIBCompliance8": ciscoIfExtensionMIBCompliance8,
       "ciscoIfExtensionMIBCompliance9": ciscoIfExtensionMIBCompliance9,
       "ciscoIfExtensionMIBCompliance10": ciscoIfExtensionMIBCompliance10,
       "ciscoIfExtensionMIBCompliance11": ciscoIfExtensionMIBCompliance11,
       "ciscoIfExtensionMIBCompliance12": ciscoIfExtensionMIBCompliance12,
       "ciscoIfExtensionMIBCompliance13": ciscoIfExtensionMIBCompliance13,
       "ciscoIfExtensionMIBCompliance14": ciscoIfExtensionMIBCompliance14,
       "ciscoIfExtensionMIBCompliance15": ciscoIfExtensionMIBCompliance15,
       "ciscoIfExtensionMIBGroups": ciscoIfExtensionMIBGroups,
       "ciscoIfExtensionTablePacketGroup": ciscoIfExtensionTablePacketGroup,
       "ciscoIfExtensionTableIntfGroup": ciscoIfExtensionTableIntfGroup,
       "ciscoIfExtensionTableIntfGroup1": ciscoIfExtensionTableIntfGroup1,
       "ciscoIfExtensionSystemGroup": ciscoIfExtensionSystemGroup,
       "ciscoIfExtDot1qEtherTypeGroup": ciscoIfExtDot1qEtherTypeGroup,
       "ciscoIfExtUtilizationGroup": ciscoIfExtUtilizationGroup,
       "ciscoIfExtDot1dBaseMappingGroup": ciscoIfExtDot1dBaseMappingGroup,
       "ciscoIfExtIfNameMappingGroup": ciscoIfExtIfNameMappingGroup,
       "ciscoIfExtensionTableIntfGroup2": ciscoIfExtensionTableIntfGroup2,
       "cieIfStatusListGroup": cieIfStatusListGroup,
       "cieLinkUpDownNotifEnableGroup": cieLinkUpDownNotifEnableGroup,
       "cieLinkUpDownNotifGroup": cieLinkUpDownNotifGroup,
       "ciscoIfExtensionAsymmetricalSpeedGroup": ciscoIfExtensionAsymmetricalSpeedGroup,
       "ciscoIfExtUtilIntervalGroup": ciscoIfExtUtilIntervalGroup,
       "cieIfIndexPersistenceGroup": cieIfIndexPersistenceGroup,
       "cieDelayedLinkUpDownNotifNotifEnableGroup": cieDelayedLinkUpDownNotifNotifEnableGroup,
       "cieDelayedLinkUpDownNotifNotifGroup": cieDelayedLinkUpDownNotifNotifGroup,
       "cieIfIndexPersistenceControlGroup": cieIfIndexPersistenceControlGroup,
       "ciscoIfExtensionTableIntfGroup3": ciscoIfExtensionTableIntfGroup3,
       "cieIfStatusListGroupSup1": cieIfStatusListGroupSup1,
       "cieIfVlStatsGroup": cieIfVlStatsGroup,
       "ciscoIfExtensionTableIntfGroup3SupR01": ciscoIfExtensionTableIntfGroup3SupR01,
       "cieLinkUpDownNotifConfigGroup": cieLinkUpDownNotifConfigGroup,
       "ciscoIfExtensionTableIntfGroup3SupR02": ciscoIfExtensionTableIntfGroup3SupR02}
)
