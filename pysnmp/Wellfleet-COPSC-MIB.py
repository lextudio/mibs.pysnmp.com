# SNMP MIB module (Wellfleet-COPSC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-COPSC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:15:58 2024
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

(wfCopsCGroup,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfCopsCGroup")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfCopsCBase_ObjectIdentity = ObjectIdentity
wfCopsCBase = _WfCopsCBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 25, 1, 1)
)


class _WfCopsCDelete_Type(Integer32):
    """Custom type wfCopsCDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfCopsCDelete_Type.__name__ = "Integer32"
_WfCopsCDelete_Object = MibScalar
wfCopsCDelete = _WfCopsCDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 25, 1, 1, 1),
    _WfCopsCDelete_Type()
)
wfCopsCDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCopsCDelete.setStatus("mandatory")


class _WfCopsCDisable_Type(Integer32):
    """Custom type wfCopsCDisable based on Integer32"""
    defaultValue = 1

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


_WfCopsCDisable_Type.__name__ = "Integer32"
_WfCopsCDisable_Object = MibScalar
wfCopsCDisable = _WfCopsCDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 25, 1, 1, 2),
    _WfCopsCDisable_Type()
)
wfCopsCDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCopsCDisable.setStatus("mandatory")


class _WfCopsCState_Type(Integer32):
    """Custom type wfCopsCState based on Integer32"""
    defaultValue = 5

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
        *(("down", 4),
          ("init", 3),
          ("localrecovery", 2),
          ("notpresent", 5),
          ("up", 1))
    )


_WfCopsCState_Type.__name__ = "Integer32"
_WfCopsCState_Object = MibScalar
wfCopsCState = _WfCopsCState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 25, 1, 1, 3),
    _WfCopsCState_Type()
)
wfCopsCState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCopsCState.setStatus("mandatory")


class _WfCopsCCurrentSlotMask_Type(Gauge32):
    """Custom type wfCopsCCurrentSlotMask based on Gauge32"""
    defaultValue = 0


_WfCopsCCurrentSlotMask_Object = MibScalar
wfCopsCCurrentSlotMask = _WfCopsCCurrentSlotMask_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 25, 1, 1, 4),
    _WfCopsCCurrentSlotMask_Type()
)
wfCopsCCurrentSlotMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCopsCCurrentSlotMask.setStatus("mandatory")


class _WfCopsCSoloSlot_Type(Integer32):
    """Custom type wfCopsCSoloSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_WfCopsCSoloSlot_Type.__name__ = "Integer32"
_WfCopsCSoloSlot_Object = MibScalar
wfCopsCSoloSlot = _WfCopsCSoloSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 25, 1, 1, 5),
    _WfCopsCSoloSlot_Type()
)
wfCopsCSoloSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCopsCSoloSlot.setStatus("mandatory")


class _WfCopsCSoloSlotMask_Type(Gauge32):
    """Custom type wfCopsCSoloSlotMask based on Gauge32"""
    defaultValue = 4294705152


_WfCopsCSoloSlotMask_Object = MibScalar
wfCopsCSoloSlotMask = _WfCopsCSoloSlotMask_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 25, 1, 1, 6),
    _WfCopsCSoloSlotMask_Type()
)
wfCopsCSoloSlotMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCopsCSoloSlotMask.setStatus("mandatory")


class _WfCopsCDebugLogFilter_Type(Integer32):
    """Custom type wfCopsCDebugLogFilter based on Integer32"""
    defaultValue = 0


_WfCopsCDebugLogFilter_Object = MibScalar
wfCopsCDebugLogFilter = _WfCopsCDebugLogFilter_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 25, 1, 1, 7),
    _WfCopsCDebugLogFilter_Type()
)
wfCopsCDebugLogFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCopsCDebugLogFilter.setStatus("mandatory")
_WfCopsCIPAddr_Type = IpAddress
_WfCopsCIPAddr_Object = MibScalar
wfCopsCIPAddr = _WfCopsCIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 25, 1, 1, 8),
    _WfCopsCIPAddr_Type()
)
wfCopsCIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCopsCIPAddr.setStatus("mandatory")
_WfCopsCID_Type = DisplayString
_WfCopsCID_Object = MibScalar
wfCopsCID = _WfCopsCID_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 25, 1, 1, 9),
    _WfCopsCID_Type()
)
wfCopsCID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCopsCID.setStatus("mandatory")
_WfCopsSvrTable_Object = MibTable
wfCopsSvrTable = _WfCopsSvrTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 25, 1, 2)
)
if mibBuilder.loadTexts:
    wfCopsSvrTable.setStatus("mandatory")
_WfCopsSvrEntry_Object = MibTableRow
wfCopsSvrEntry = _WfCopsSvrEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 25, 1, 2, 1)
)
wfCopsSvrEntry.setIndexNames(
    (0, "Wellfleet-COPSC-MIB", "wfCopsSvrIPAddr"),
)
if mibBuilder.loadTexts:
    wfCopsSvrEntry.setStatus("mandatory")


class _WfCopsSvrDelete_Type(Integer32):
    """Custom type wfCopsSvrDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfCopsSvrDelete_Type.__name__ = "Integer32"
_WfCopsSvrDelete_Object = MibTableColumn
wfCopsSvrDelete = _WfCopsSvrDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 25, 1, 2, 1, 1),
    _WfCopsSvrDelete_Type()
)
wfCopsSvrDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCopsSvrDelete.setStatus("mandatory")


class _WfCopsSvrDisable_Type(Integer32):
    """Custom type wfCopsSvrDisable based on Integer32"""
    defaultValue = 1

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


_WfCopsSvrDisable_Type.__name__ = "Integer32"
_WfCopsSvrDisable_Object = MibTableColumn
wfCopsSvrDisable = _WfCopsSvrDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 25, 1, 2, 1, 2),
    _WfCopsSvrDisable_Type()
)
wfCopsSvrDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCopsSvrDisable.setStatus("mandatory")
_WfCopsSvrIPAddr_Type = IpAddress
_WfCopsSvrIPAddr_Object = MibTableColumn
wfCopsSvrIPAddr = _WfCopsSvrIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 25, 1, 2, 1, 3),
    _WfCopsSvrIPAddr_Type()
)
wfCopsSvrIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCopsSvrIPAddr.setStatus("mandatory")


class _WfCopsSvrPriority_Type(Integer32):
    """Custom type wfCopsSvrPriority based on Integer32"""
    defaultValue = 1


_WfCopsSvrPriority_Object = MibTableColumn
wfCopsSvrPriority = _WfCopsSvrPriority_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 25, 1, 2, 1, 4),
    _WfCopsSvrPriority_Type()
)
wfCopsSvrPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCopsSvrPriority.setStatus("mandatory")


class _WfCopsSvrConnState_Type(Integer32):
    """Custom type wfCopsSvrConnState based on Integer32"""
    defaultValue = 5

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
        *(("connnegotiation", 2),
          ("connrecovery", 3),
          ("noconn", 5),
          ("servercontacted", 4),
          ("serverready", 1))
    )


_WfCopsSvrConnState_Type.__name__ = "Integer32"
_WfCopsSvrConnState_Object = MibTableColumn
wfCopsSvrConnState = _WfCopsSvrConnState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 25, 1, 2, 1, 5),
    _WfCopsSvrConnState_Type()
)
wfCopsSvrConnState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfCopsSvrConnState.setStatus("mandatory")


class _WfCopsSvrConnTimer_Type(Integer32):
    """Custom type wfCopsSvrConnTimer based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WfCopsSvrConnTimer_Type.__name__ = "Integer32"
_WfCopsSvrConnTimer_Object = MibTableColumn
wfCopsSvrConnTimer = _WfCopsSvrConnTimer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 25, 1, 2, 1, 6),
    _WfCopsSvrConnTimer_Type()
)
wfCopsSvrConnTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCopsSvrConnTimer.setStatus("mandatory")


class _WfCopsSvrConnRetryCount_Type(Integer32):
    """Custom type wfCopsSvrConnRetryCount based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_WfCopsSvrConnRetryCount_Type.__name__ = "Integer32"
_WfCopsSvrConnRetryCount_Object = MibTableColumn
wfCopsSvrConnRetryCount = _WfCopsSvrConnRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 25, 1, 2, 1, 7),
    _WfCopsSvrConnRetryCount_Type()
)
wfCopsSvrConnRetryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCopsSvrConnRetryCount.setStatus("mandatory")


class _WfCopsSvrKeepAliveTimer_Type(Integer32):
    """Custom type wfCopsSvrKeepAliveTimer based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WfCopsSvrKeepAliveTimer_Type.__name__ = "Integer32"
_WfCopsSvrKeepAliveTimer_Object = MibTableColumn
wfCopsSvrKeepAliveTimer = _WfCopsSvrKeepAliveTimer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 25, 1, 2, 1, 8),
    _WfCopsSvrKeepAliveTimer_Type()
)
wfCopsSvrKeepAliveTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCopsSvrKeepAliveTimer.setStatus("mandatory")


class _WfCopsSvrReportTimer_Type(Integer32):
    """Custom type wfCopsSvrReportTimer based on Integer32"""
    defaultValue = 360

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WfCopsSvrReportTimer_Type.__name__ = "Integer32"
_WfCopsSvrReportTimer_Object = MibTableColumn
wfCopsSvrReportTimer = _WfCopsSvrReportTimer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 25, 1, 2, 1, 9),
    _WfCopsSvrReportTimer_Type()
)
wfCopsSvrReportTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCopsSvrReportTimer.setStatus("mandatory")


class _WfCopsSvrTCPKeepAliveInterval_Type(Integer32):
    """Custom type wfCopsSvrTCPKeepAliveInterval based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WfCopsSvrTCPKeepAliveInterval_Type.__name__ = "Integer32"
_WfCopsSvrTCPKeepAliveInterval_Object = MibTableColumn
wfCopsSvrTCPKeepAliveInterval = _WfCopsSvrTCPKeepAliveInterval_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 25, 1, 2, 1, 10),
    _WfCopsSvrTCPKeepAliveInterval_Type()
)
wfCopsSvrTCPKeepAliveInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCopsSvrTCPKeepAliveInterval.setStatus("mandatory")


class _WfCopsSvrTCPKeepAliveRetryTimeOut_Type(Integer32):
    """Custom type wfCopsSvrTCPKeepAliveRetryTimeOut based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WfCopsSvrTCPKeepAliveRetryTimeOut_Type.__name__ = "Integer32"
_WfCopsSvrTCPKeepAliveRetryTimeOut_Object = MibTableColumn
wfCopsSvrTCPKeepAliveRetryTimeOut = _WfCopsSvrTCPKeepAliveRetryTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 25, 1, 2, 1, 11),
    _WfCopsSvrTCPKeepAliveRetryTimeOut_Type()
)
wfCopsSvrTCPKeepAliveRetryTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCopsSvrTCPKeepAliveRetryTimeOut.setStatus("mandatory")


class _WfCopsSvrTCPKeepAliveMaxRetryCount_Type(Integer32):
    """Custom type wfCopsSvrTCPKeepAliveMaxRetryCount based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WfCopsSvrTCPKeepAliveMaxRetryCount_Type.__name__ = "Integer32"
_WfCopsSvrTCPKeepAliveMaxRetryCount_Object = MibTableColumn
wfCopsSvrTCPKeepAliveMaxRetryCount = _WfCopsSvrTCPKeepAliveMaxRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 25, 1, 2, 1, 12),
    _WfCopsSvrTCPKeepAliveMaxRetryCount_Type()
)
wfCopsSvrTCPKeepAliveMaxRetryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCopsSvrTCPKeepAliveMaxRetryCount.setStatus("mandatory")


class _WfCopsSvrRemotePort_Type(Integer32):
    """Custom type wfCopsSvrRemotePort based on Integer32"""
    defaultValue = 3288

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WfCopsSvrRemotePort_Type.__name__ = "Integer32"
_WfCopsSvrRemotePort_Object = MibTableColumn
wfCopsSvrRemotePort = _WfCopsSvrRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 25, 1, 2, 1, 13),
    _WfCopsSvrRemotePort_Type()
)
wfCopsSvrRemotePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCopsSvrRemotePort.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-COPSC-MIB",
    **{"wfCopsCBase": wfCopsCBase,
       "wfCopsCDelete": wfCopsCDelete,
       "wfCopsCDisable": wfCopsCDisable,
       "wfCopsCState": wfCopsCState,
       "wfCopsCCurrentSlotMask": wfCopsCCurrentSlotMask,
       "wfCopsCSoloSlot": wfCopsCSoloSlot,
       "wfCopsCSoloSlotMask": wfCopsCSoloSlotMask,
       "wfCopsCDebugLogFilter": wfCopsCDebugLogFilter,
       "wfCopsCIPAddr": wfCopsCIPAddr,
       "wfCopsCID": wfCopsCID,
       "wfCopsSvrTable": wfCopsSvrTable,
       "wfCopsSvrEntry": wfCopsSvrEntry,
       "wfCopsSvrDelete": wfCopsSvrDelete,
       "wfCopsSvrDisable": wfCopsSvrDisable,
       "wfCopsSvrIPAddr": wfCopsSvrIPAddr,
       "wfCopsSvrPriority": wfCopsSvrPriority,
       "wfCopsSvrConnState": wfCopsSvrConnState,
       "wfCopsSvrConnTimer": wfCopsSvrConnTimer,
       "wfCopsSvrConnRetryCount": wfCopsSvrConnRetryCount,
       "wfCopsSvrKeepAliveTimer": wfCopsSvrKeepAliveTimer,
       "wfCopsSvrReportTimer": wfCopsSvrReportTimer,
       "wfCopsSvrTCPKeepAliveInterval": wfCopsSvrTCPKeepAliveInterval,
       "wfCopsSvrTCPKeepAliveRetryTimeOut": wfCopsSvrTCPKeepAliveRetryTimeOut,
       "wfCopsSvrTCPKeepAliveMaxRetryCount": wfCopsSvrTCPKeepAliveMaxRetryCount,
       "wfCopsSvrRemotePort": wfCopsSvrRemotePort}
)
