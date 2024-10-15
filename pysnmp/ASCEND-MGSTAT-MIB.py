# SNMP MIB module (ASCEND-MGSTAT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MGSTAT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:41:00 2024
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

(mgGroup,) = mibBuilder.importSymbols(
    "ASCEND-MIB",
    "mgGroup")

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


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MgNumLinks_Type = Integer32
_MgNumLinks_Object = MibScalar
mgNumLinks = _MgNumLinks_Object(
    (1, 3, 6, 1, 4, 1, 529, 29, 1),
    _MgNumLinks_Type()
)
mgNumLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgNumLinks.setStatus("mandatory")
_MgTable_Object = MibTable
mgTable = _MgTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 29, 2)
)
if mibBuilder.loadTexts:
    mgTable.setStatus("mandatory")
_MgTableEntry_Object = MibTableRow
mgTableEntry = _MgTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 29, 2, 1)
)
mgTableEntry.setIndexNames(
    (0, "ASCEND-MGSTAT-MIB", "mgLinkName"),
)
if mibBuilder.loadTexts:
    mgTableEntry.setStatus("mandatory")
_MgLinkName_Type = OctetString
_MgLinkName_Object = MibTableColumn
mgLinkName = _MgLinkName_Object(
    (1, 3, 6, 1, 4, 1, 529, 29, 2, 1, 1),
    _MgLinkName_Type()
)
mgLinkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgLinkName.setStatus("mandatory")


class _MgProtocol_Type(Integer32):
    """Custom type mgProtocol based on Integer32"""
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
        *(("asgcp", 3),
          ("ipdc", 4),
          ("notApplicable", 1),
          ("other", 2))
    )


_MgProtocol_Type.__name__ = "Integer32"
_MgProtocol_Object = MibTableColumn
mgProtocol = _MgProtocol_Object(
    (1, 3, 6, 1, 4, 1, 529, 29, 2, 1, 2),
    _MgProtocol_Type()
)
mgProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgProtocol.setStatus("mandatory")


class _MgAdminStatus_Type(Integer32):
    """Custom type mgAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_MgAdminStatus_Type.__name__ = "Integer32"
_MgAdminStatus_Object = MibTableColumn
mgAdminStatus = _MgAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 529, 29, 2, 1, 3),
    _MgAdminStatus_Type()
)
mgAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgAdminStatus.setStatus("mandatory")


class _MgOperStatus_Type(Integer32):
    """Custom type mgOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("unknown", 3),
          ("up", 1))
    )


_MgOperStatus_Type.__name__ = "Integer32"
_MgOperStatus_Object = MibTableColumn
mgOperStatus = _MgOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 529, 29, 2, 1, 4),
    _MgOperStatus_Type()
)
mgOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgOperStatus.setStatus("mandatory")
_MgLastStatusChange_Type = TimeTicks
_MgLastStatusChange_Object = MibTableColumn
mgLastStatusChange = _MgLastStatusChange_Object(
    (1, 3, 6, 1, 4, 1, 529, 29, 2, 1, 5),
    _MgLastStatusChange_Type()
)
mgLastStatusChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgLastStatusChange.setStatus("mandatory")
_MgNumInMessages_Type = Counter32
_MgNumInMessages_Object = MibTableColumn
mgNumInMessages = _MgNumInMessages_Object(
    (1, 3, 6, 1, 4, 1, 529, 29, 2, 1, 6),
    _MgNumInMessages_Type()
)
mgNumInMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgNumInMessages.setStatus("mandatory")
_MgNumInOctets_Type = Counter32
_MgNumInOctets_Object = MibTableColumn
mgNumInOctets = _MgNumInOctets_Object(
    (1, 3, 6, 1, 4, 1, 529, 29, 2, 1, 7),
    _MgNumInOctets_Type()
)
mgNumInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgNumInOctets.setStatus("mandatory")
_MgNumOutMessages_Type = Counter32
_MgNumOutMessages_Object = MibTableColumn
mgNumOutMessages = _MgNumOutMessages_Object(
    (1, 3, 6, 1, 4, 1, 529, 29, 2, 1, 8),
    _MgNumOutMessages_Type()
)
mgNumOutMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgNumOutMessages.setStatus("mandatory")
_MgNumOutOctets_Type = Counter32
_MgNumOutOctets_Object = MibTableColumn
mgNumOutOctets = _MgNumOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 529, 29, 2, 1, 9),
    _MgNumOutOctets_Type()
)
mgNumOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgNumOutOctets.setStatus("mandatory")
_MgNumErrors_Type = Counter32
_MgNumErrors_Object = MibTableColumn
mgNumErrors = _MgNumErrors_Object(
    (1, 3, 6, 1, 4, 1, 529, 29, 2, 1, 10),
    _MgNumErrors_Type()
)
mgNumErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgNumErrors.setStatus("mandatory")
_MgNumTimerRecovery_Type = Counter32
_MgNumTimerRecovery_Object = MibTableColumn
mgNumTimerRecovery = _MgNumTimerRecovery_Object(
    (1, 3, 6, 1, 4, 1, 529, 29, 2, 1, 11),
    _MgNumTimerRecovery_Type()
)
mgNumTimerRecovery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgNumTimerRecovery.setStatus("mandatory")
_MgTransportNumLosses_Type = Counter32
_MgTransportNumLosses_Object = MibTableColumn
mgTransportNumLosses = _MgTransportNumLosses_Object(
    (1, 3, 6, 1, 4, 1, 529, 29, 2, 1, 12),
    _MgTransportNumLosses_Type()
)
mgTransportNumLosses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgTransportNumLosses.setStatus("mandatory")
_MgTransportNumSwitchover_Type = Counter32
_MgTransportNumSwitchover_Object = MibTableColumn
mgTransportNumSwitchover = _MgTransportNumSwitchover_Object(
    (1, 3, 6, 1, 4, 1, 529, 29, 2, 1, 13),
    _MgTransportNumSwitchover_Type()
)
mgTransportNumSwitchover.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgTransportNumSwitchover.setStatus("mandatory")
_MgTransportTotalNumAlarms_Type = Counter32
_MgTransportTotalNumAlarms_Object = MibTableColumn
mgTransportTotalNumAlarms = _MgTransportTotalNumAlarms_Object(
    (1, 3, 6, 1, 4, 1, 529, 29, 2, 1, 14),
    _MgTransportTotalNumAlarms_Type()
)
mgTransportTotalNumAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgTransportTotalNumAlarms.setStatus("mandatory")


class _MgTransportLastEvent_Type(Integer32):
    """Custom type mgTransportLastEvent based on Integer32"""
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
        *(("linkLoss", 4),
          ("linkShutdown", 6),
          ("linkUp", 3),
          ("notApplicable", 1),
          ("other", 2),
          ("persistentError", 5),
          ("switchOver", 7))
    )


_MgTransportLastEvent_Type.__name__ = "Integer32"
_MgTransportLastEvent_Object = MibTableColumn
mgTransportLastEvent = _MgTransportLastEvent_Object(
    (1, 3, 6, 1, 4, 1, 529, 29, 2, 1, 15),
    _MgTransportLastEvent_Type()
)
mgTransportLastEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgTransportLastEvent.setStatus("mandatory")
_MgTransportLastEventTime_Type = TimeTicks
_MgTransportLastEventTime_Object = MibTableColumn
mgTransportLastEventTime = _MgTransportLastEventTime_Object(
    (1, 3, 6, 1, 4, 1, 529, 29, 2, 1, 16),
    _MgTransportLastEventTime_Type()
)
mgTransportLastEventTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgTransportLastEventTime.setStatus("mandatory")


class _MgResetStatistics_Type(Integer32):
    """Custom type mgResetStatistics based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("other", 2),
          ("reset", 3))
    )


_MgResetStatistics_Type.__name__ = "Integer32"
_MgResetStatistics_Object = MibTableColumn
mgResetStatistics = _MgResetStatistics_Object(
    (1, 3, 6, 1, 4, 1, 529, 29, 2, 1, 17),
    _MgResetStatistics_Type()
)
mgResetStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgResetStatistics.setStatus("mandatory")
_MgLastStatisticsReset_Type = TimeTicks
_MgLastStatisticsReset_Object = MibTableColumn
mgLastStatisticsReset = _MgLastStatisticsReset_Object(
    (1, 3, 6, 1, 4, 1, 529, 29, 2, 1, 18),
    _MgLastStatisticsReset_Type()
)
mgLastStatisticsReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgLastStatisticsReset.setStatus("mandatory")
_MgControllerTable_Object = MibTable
mgControllerTable = _MgControllerTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 29, 3)
)
if mibBuilder.loadTexts:
    mgControllerTable.setStatus("mandatory")
_MgControllerEntry_Object = MibTableRow
mgControllerEntry = _MgControllerEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 29, 3, 1)
)
mgControllerEntry.setIndexNames(
    (0, "ASCEND-MGSTAT-MIB", "mgControllerLinkName"),
    (0, "ASCEND-MGSTAT-MIB", "mgControllerIndex"),
)
if mibBuilder.loadTexts:
    mgControllerEntry.setStatus("mandatory")
_MgControllerLinkName_Type = OctetString
_MgControllerLinkName_Object = MibTableColumn
mgControllerLinkName = _MgControllerLinkName_Object(
    (1, 3, 6, 1, 4, 1, 529, 29, 3, 1, 1),
    _MgControllerLinkName_Type()
)
mgControllerLinkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgControllerLinkName.setStatus("mandatory")
_MgControllerIndex_Type = Integer32
_MgControllerIndex_Object = MibTableColumn
mgControllerIndex = _MgControllerIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 29, 3, 1, 2),
    _MgControllerIndex_Type()
)
mgControllerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgControllerIndex.setStatus("mandatory")
_MgControllerIPAddress_Type = IpAddress
_MgControllerIPAddress_Object = MibTableColumn
mgControllerIPAddress = _MgControllerIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 529, 29, 3, 1, 3),
    _MgControllerIPAddress_Type()
)
mgControllerIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgControllerIPAddress.setStatus("mandatory")


class _MgControllerPort_Type(Integer32):
    """Custom type mgControllerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MgControllerPort_Type.__name__ = "Integer32"
_MgControllerPort_Object = MibTableColumn
mgControllerPort = _MgControllerPort_Object(
    (1, 3, 6, 1, 4, 1, 529, 29, 3, 1, 4),
    _MgControllerPort_Type()
)
mgControllerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgControllerPort.setStatus("mandatory")


class _MgControllerOperStatus_Type(Integer32):
    """Custom type mgControllerOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("standby", 3),
          ("up", 1))
    )


_MgControllerOperStatus_Type.__name__ = "Integer32"
_MgControllerOperStatus_Object = MibTableColumn
mgControllerOperStatus = _MgControllerOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 529, 29, 3, 1, 5),
    _MgControllerOperStatus_Type()
)
mgControllerOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgControllerOperStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MGSTAT-MIB",
    **{"mgNumLinks": mgNumLinks,
       "mgTable": mgTable,
       "mgTableEntry": mgTableEntry,
       "mgLinkName": mgLinkName,
       "mgProtocol": mgProtocol,
       "mgAdminStatus": mgAdminStatus,
       "mgOperStatus": mgOperStatus,
       "mgLastStatusChange": mgLastStatusChange,
       "mgNumInMessages": mgNumInMessages,
       "mgNumInOctets": mgNumInOctets,
       "mgNumOutMessages": mgNumOutMessages,
       "mgNumOutOctets": mgNumOutOctets,
       "mgNumErrors": mgNumErrors,
       "mgNumTimerRecovery": mgNumTimerRecovery,
       "mgTransportNumLosses": mgTransportNumLosses,
       "mgTransportNumSwitchover": mgTransportNumSwitchover,
       "mgTransportTotalNumAlarms": mgTransportTotalNumAlarms,
       "mgTransportLastEvent": mgTransportLastEvent,
       "mgTransportLastEventTime": mgTransportLastEventTime,
       "mgResetStatistics": mgResetStatistics,
       "mgLastStatisticsReset": mgLastStatisticsReset,
       "mgControllerTable": mgControllerTable,
       "mgControllerEntry": mgControllerEntry,
       "mgControllerLinkName": mgControllerLinkName,
       "mgControllerIndex": mgControllerIndex,
       "mgControllerIPAddress": mgControllerIPAddress,
       "mgControllerPort": mgControllerPort,
       "mgControllerOperStatus": mgControllerOperStatus}
)
