# SNMP MIB module (SYSLOG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SYSLOG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:00:12 2024
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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

swSysLogMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 12)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _SwSysLogCtrlState_Type(Integer32):
    """Custom type swSysLogCtrlState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_SwSysLogCtrlState_Type.__name__ = "Integer32"
_SwSysLogCtrlState_Object = MibScalar
swSysLogCtrlState = _SwSysLogCtrlState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 12, 1),
    _SwSysLogCtrlState_Type()
)
swSysLogCtrlState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSysLogCtrlState.setStatus("current")
_SwSysLogServerTable_Object = MibTable
swSysLogServerTable = _SwSysLogServerTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 12, 2)
)
if mibBuilder.loadTexts:
    swSysLogServerTable.setStatus("current")
_SwSysLogServerEntry_Object = MibTableRow
swSysLogServerEntry = _SwSysLogServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 12, 2, 1)
)
swSysLogServerEntry.setIndexNames(
    (0, "SYSLOG-MIB", "swSysLogServerIndex"),
)
if mibBuilder.loadTexts:
    swSysLogServerEntry.setStatus("current")


class _SwSysLogServerIndex_Type(Integer32):
    """Custom type swSysLogServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_SwSysLogServerIndex_Type.__name__ = "Integer32"
_SwSysLogServerIndex_Object = MibTableColumn
swSysLogServerIndex = _SwSysLogServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 12, 2, 1, 1),
    _SwSysLogServerIndex_Type()
)
swSysLogServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSysLogServerIndex.setStatus("current")
_SwSysLogServerIPAddress_Type = IpAddress
_SwSysLogServerIPAddress_Object = MibTableColumn
swSysLogServerIPAddress = _SwSysLogServerIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 12, 2, 1, 2),
    _SwSysLogServerIPAddress_Type()
)
swSysLogServerIPAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swSysLogServerIPAddress.setStatus("current")


class _SwSysLogServerFacility_Type(Integer32):
    """Custom type swSysLogServerFacility based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("local0", 0),
          ("local1", 1),
          ("local2", 2),
          ("local3", 3),
          ("local4", 4),
          ("local5", 5),
          ("local6", 6),
          ("local7", 7))
    )


_SwSysLogServerFacility_Type.__name__ = "Integer32"
_SwSysLogServerFacility_Object = MibTableColumn
swSysLogServerFacility = _SwSysLogServerFacility_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 12, 2, 1, 3),
    _SwSysLogServerFacility_Type()
)
swSysLogServerFacility.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swSysLogServerFacility.setStatus("current")


class _SwSysLogServerSeverity_Type(Integer32):
    """Custom type swSysLogServerSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("all", 1),
          ("informational", 3),
          ("warning", 2))
    )


_SwSysLogServerSeverity_Type.__name__ = "Integer32"
_SwSysLogServerSeverity_Object = MibTableColumn
swSysLogServerSeverity = _SwSysLogServerSeverity_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 12, 2, 1, 4),
    _SwSysLogServerSeverity_Type()
)
swSysLogServerSeverity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swSysLogServerSeverity.setStatus("current")


class _SwSysLogServerUDPPort_Type(Integer32):
    """Custom type swSysLogServerUDPPort based on Integer32"""
    defaultValue = 514


_SwSysLogServerUDPPort_Object = MibTableColumn
swSysLogServerUDPPort = _SwSysLogServerUDPPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 12, 2, 1, 5),
    _SwSysLogServerUDPPort_Type()
)
swSysLogServerUDPPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swSysLogServerUDPPort.setStatus("current")


class _SwSysLogServerState_Type(Integer32):
    """Custom type swSysLogServerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_SwSysLogServerState_Type.__name__ = "Integer32"
_SwSysLogServerState_Object = MibTableColumn
swSysLogServerState = _SwSysLogServerState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 12, 2, 1, 6),
    _SwSysLogServerState_Type()
)
swSysLogServerState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swSysLogServerState.setStatus("current")
_SwSysLogServerRowStatus_Type = RowStatus
_SwSysLogServerRowStatus_Object = MibTableColumn
swSysLogServerRowStatus = _SwSysLogServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 12, 2, 1, 7),
    _SwSysLogServerRowStatus_Type()
)
swSysLogServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swSysLogServerRowStatus.setStatus("current")
_SwLogSaveCtrl_ObjectIdentity = ObjectIdentity
swLogSaveCtrl = _SwLogSaveCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 12, 3)
)


class _SwLogSaveMethod_Type(Integer32):
    """Custom type swLogSaveMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("log-trigger", 3),
          ("on-demand", 2),
          ("time-interval", 1))
    )


_SwLogSaveMethod_Type.__name__ = "Integer32"
_SwLogSaveMethod_Object = MibScalar
swLogSaveMethod = _SwLogSaveMethod_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 12, 3, 1),
    _SwLogSaveMethod_Type()
)
swLogSaveMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swLogSaveMethod.setStatus("current")


class _SwLogSaveTimeInterval_Type(Integer32):
    """Custom type swLogSaveTimeInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SwLogSaveTimeInterval_Type.__name__ = "Integer32"
_SwLogSaveTimeInterval_Object = MibScalar
swLogSaveTimeInterval = _SwLogSaveTimeInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 12, 3, 2),
    _SwLogSaveTimeInterval_Type()
)
swLogSaveTimeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swLogSaveTimeInterval.setStatus("current")
_SwSysLogCtrl_ObjectIdentity = ObjectIdentity
swSysLogCtrl = _SwSysLogCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 12, 4)
)


class _SwSysLogCtrlClearLog_Type(Integer32):
    """Custom type swSysLogCtrlClearLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("start", 2))
    )


_SwSysLogCtrlClearLog_Type.__name__ = "Integer32"
_SwSysLogCtrlClearLog_Object = MibScalar
swSysLogCtrlClearLog = _SwSysLogCtrlClearLog_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 12, 4, 1),
    _SwSysLogCtrlClearLog_Type()
)
swSysLogCtrlClearLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSysLogCtrlClearLog.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SYSLOG-MIB",
    **{"swSysLogMIB": swSysLogMIB,
       "swSysLogCtrlState": swSysLogCtrlState,
       "swSysLogServerTable": swSysLogServerTable,
       "swSysLogServerEntry": swSysLogServerEntry,
       "swSysLogServerIndex": swSysLogServerIndex,
       "swSysLogServerIPAddress": swSysLogServerIPAddress,
       "swSysLogServerFacility": swSysLogServerFacility,
       "swSysLogServerSeverity": swSysLogServerSeverity,
       "swSysLogServerUDPPort": swSysLogServerUDPPort,
       "swSysLogServerState": swSysLogServerState,
       "swSysLogServerRowStatus": swSysLogServerRowStatus,
       "swLogSaveCtrl": swLogSaveCtrl,
       "swLogSaveMethod": swLogSaveMethod,
       "swLogSaveTimeInterval": swLogSaveTimeInterval,
       "swSysLogCtrl": swSysLogCtrl,
       "swSysLogCtrlClearLog": swSysLogCtrlClearLog}
)
