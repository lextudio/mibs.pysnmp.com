# SNMP MIB module (CENTILLION-SYSTEM-EVENT-LOG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CENTILLION-SYSTEM-EVENT-LOG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:54:15 2024
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

(CardId,
 PortId,
 sysEvtLogMgmt) = mibBuilder.importSymbols(
    "CENTILLION-ROOT-MIB",
    "CardId",
    "PortId",
    "sysEvtLogMgmt")

(TimeIntervalSec,) = mibBuilder.importSymbols(
    "S5-TCS-MIB",
    "TimeIntervalSec")

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



class _SysEvtLogDuration_Type(TimeIntervalSec):
    """Custom type sysEvtLogDuration based on TimeIntervalSec"""
    defaultValue = 0


_SysEvtLogDuration_Object = MibScalar
sysEvtLogDuration = _SysEvtLogDuration_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 5, 1),
    _SysEvtLogDuration_Type()
)
sysEvtLogDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysEvtLogDuration.setStatus("mandatory")


class _SysEvtLogPreFilterEntityMap_Type(OctetString):
    """Custom type sysEvtLogPreFilterEntityMap based on OctetString"""
    defaultHexValue = "FFFFFFFFFFFFFFFF"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_SysEvtLogPreFilterEntityMap_Type.__name__ = "OctetString"
_SysEvtLogPreFilterEntityMap_Object = MibScalar
sysEvtLogPreFilterEntityMap = _SysEvtLogPreFilterEntityMap_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 5, 2),
    _SysEvtLogPreFilterEntityMap_Type()
)
sysEvtLogPreFilterEntityMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysEvtLogPreFilterEntityMap.setStatus("mandatory")


class _SysEvtLogPreFilterSeverity_Type(Integer32):
    """Custom type sysEvtLogPreFilterSeverity based on Integer32"""
    defaultValue = 4

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
        *(("alert", 2),
          ("critical", 3),
          ("debug", 8),
          ("emergency", 1),
          ("error", 4),
          ("info", 7),
          ("notice", 6),
          ("warning", 5))
    )


_SysEvtLogPreFilterSeverity_Type.__name__ = "Integer32"
_SysEvtLogPreFilterSeverity_Object = MibScalar
sysEvtLogPreFilterSeverity = _SysEvtLogPreFilterSeverity_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 5, 3),
    _SysEvtLogPreFilterSeverity_Type()
)
sysEvtLogPreFilterSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysEvtLogPreFilterSeverity.setStatus("mandatory")
_SysEvtLogSlotPreFilterTable_Object = MibTable
sysEvtLogSlotPreFilterTable = _SysEvtLogSlotPreFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 5, 4)
)
if mibBuilder.loadTexts:
    sysEvtLogSlotPreFilterTable.setStatus("mandatory")
_SysEvtLogSlotPreFilterEntry_Object = MibTableRow
sysEvtLogSlotPreFilterEntry = _SysEvtLogSlotPreFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 5, 4, 1)
)
sysEvtLogSlotPreFilterEntry.setIndexNames(
    (0, "CENTILLION-SYSTEM-EVENT-LOG-MIB", "sysEvtLogSlotPreFilterCardId"),
)
if mibBuilder.loadTexts:
    sysEvtLogSlotPreFilterEntry.setStatus("mandatory")
_SysEvtLogSlotPreFilterCardId_Type = CardId
_SysEvtLogSlotPreFilterCardId_Object = MibTableColumn
sysEvtLogSlotPreFilterCardId = _SysEvtLogSlotPreFilterCardId_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 5, 4, 1, 1),
    _SysEvtLogSlotPreFilterCardId_Type()
)
sysEvtLogSlotPreFilterCardId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysEvtLogSlotPreFilterCardId.setStatus("mandatory")


class _SysEvtLogSlotPreFilterControl_Type(Integer32):
    """Custom type sysEvtLogSlotPreFilterControl based on Integer32"""
    defaultValue = 2

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


_SysEvtLogSlotPreFilterControl_Type.__name__ = "Integer32"
_SysEvtLogSlotPreFilterControl_Object = MibTableColumn
sysEvtLogSlotPreFilterControl = _SysEvtLogSlotPreFilterControl_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 5, 4, 1, 2),
    _SysEvtLogSlotPreFilterControl_Type()
)
sysEvtLogSlotPreFilterControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysEvtLogSlotPreFilterControl.setStatus("mandatory")
_SysEvtLogPortPreFilterTable_Object = MibTable
sysEvtLogPortPreFilterTable = _SysEvtLogPortPreFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 5, 5)
)
if mibBuilder.loadTexts:
    sysEvtLogPortPreFilterTable.setStatus("mandatory")
_SysEvtLogPortPreFilterEntry_Object = MibTableRow
sysEvtLogPortPreFilterEntry = _SysEvtLogPortPreFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 5, 5, 1)
)
sysEvtLogPortPreFilterEntry.setIndexNames(
    (0, "CENTILLION-SYSTEM-EVENT-LOG-MIB", "sysEvtLogPortPreFilterCardId"),
    (0, "CENTILLION-SYSTEM-EVENT-LOG-MIB", "sysEvtLogPortPreFilterPortId"),
)
if mibBuilder.loadTexts:
    sysEvtLogPortPreFilterEntry.setStatus("mandatory")
_SysEvtLogPortPreFilterCardId_Type = CardId
_SysEvtLogPortPreFilterCardId_Object = MibTableColumn
sysEvtLogPortPreFilterCardId = _SysEvtLogPortPreFilterCardId_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 5, 5, 1, 1),
    _SysEvtLogPortPreFilterCardId_Type()
)
sysEvtLogPortPreFilterCardId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysEvtLogPortPreFilterCardId.setStatus("mandatory")
_SysEvtLogPortPreFilterPortId_Type = PortId
_SysEvtLogPortPreFilterPortId_Object = MibTableColumn
sysEvtLogPortPreFilterPortId = _SysEvtLogPortPreFilterPortId_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 5, 5, 1, 2),
    _SysEvtLogPortPreFilterPortId_Type()
)
sysEvtLogPortPreFilterPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysEvtLogPortPreFilterPortId.setStatus("mandatory")


class _SysEvtLogPortPreFilterControl_Type(Integer32):
    """Custom type sysEvtLogPortPreFilterControl based on Integer32"""
    defaultValue = 2

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


_SysEvtLogPortPreFilterControl_Type.__name__ = "Integer32"
_SysEvtLogPortPreFilterControl_Object = MibTableColumn
sysEvtLogPortPreFilterControl = _SysEvtLogPortPreFilterControl_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 5, 5, 1, 3),
    _SysEvtLogPortPreFilterControl_Type()
)
sysEvtLogPortPreFilterControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysEvtLogPortPreFilterControl.setStatus("mandatory")


class _SysEvtLogDestMap_Type(Integer32):
    """Custom type sysEvtLogDestMap based on Integer32"""
    defaultValue = 0


_SysEvtLogDestMap_Object = MibScalar
sysEvtLogDestMap = _SysEvtLogDestMap_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 5, 6),
    _SysEvtLogDestMap_Type()
)
sysEvtLogDestMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysEvtLogDestMap.setStatus("mandatory")
_SysEvtLogSysLogCfg_ObjectIdentity = ObjectIdentity
sysEvtLogSysLogCfg = _SysEvtLogSysLogCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 5, 7)
)


class _SysEvtLogSysLogHostIp_Type(IpAddress):
    """Custom type sysEvtLogSysLogHostIp based on IpAddress"""
    defaultHexValue = "00000000"


_SysEvtLogSysLogHostIp_Object = MibScalar
sysEvtLogSysLogHostIp = _SysEvtLogSysLogHostIp_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 5, 7, 1),
    _SysEvtLogSysLogHostIp_Type()
)
sysEvtLogSysLogHostIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysEvtLogSysLogHostIp.setStatus("mandatory")


class _SysEvtLogSysLogSeverity_Type(Integer32):
    """Custom type sysEvtLogSysLogSeverity based on Integer32"""
    defaultValue = 4

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
        *(("alert", 2),
          ("critical", 3),
          ("debug", 8),
          ("error", 4),
          ("info", 7),
          ("notice", 6),
          ("panic", 1),
          ("warning", 5))
    )


_SysEvtLogSysLogSeverity_Type.__name__ = "Integer32"
_SysEvtLogSysLogSeverity_Object = MibScalar
sysEvtLogSysLogSeverity = _SysEvtLogSysLogSeverity_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 5, 7, 2),
    _SysEvtLogSysLogSeverity_Type()
)
sysEvtLogSysLogSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysEvtLogSysLogSeverity.setStatus("mandatory")


class _SysEvtLogSysLogFacility_Type(Integer32):
    """Custom type sysEvtLogSysLogFacility based on Integer32"""
    defaultValue = 1

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
        *(("local0", 1),
          ("local1", 2),
          ("local2", 3),
          ("local3", 4),
          ("local4", 5),
          ("local5", 6),
          ("local6", 7),
          ("local7", 8))
    )


_SysEvtLogSysLogFacility_Type.__name__ = "Integer32"
_SysEvtLogSysLogFacility_Object = MibScalar
sysEvtLogSysLogFacility = _SysEvtLogSysLogFacility_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 5, 7, 3),
    _SysEvtLogSysLogFacility_Type()
)
sysEvtLogSysLogFacility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysEvtLogSysLogFacility.setStatus("mandatory")
_SysEvtLogTftpsaveCfg_ObjectIdentity = ObjectIdentity
sysEvtLogTftpsaveCfg = _SysEvtLogTftpsaveCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 5, 8)
)


class _SysEvtLogTftpsaveHostIp_Type(IpAddress):
    """Custom type sysEvtLogTftpsaveHostIp based on IpAddress"""
    defaultHexValue = "00000000"


_SysEvtLogTftpsaveHostIp_Object = MibScalar
sysEvtLogTftpsaveHostIp = _SysEvtLogTftpsaveHostIp_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 5, 8, 1),
    _SysEvtLogTftpsaveHostIp_Type()
)
sysEvtLogTftpsaveHostIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysEvtLogTftpsaveHostIp.setStatus("mandatory")


class _SysEvtLogTftpsaveFileName_Type(DisplayString):
    """Custom type sysEvtLogTftpsaveFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SysEvtLogTftpsaveFileName_Type.__name__ = "DisplayString"
_SysEvtLogTftpsaveFileName_Object = MibScalar
sysEvtLogTftpsaveFileName = _SysEvtLogTftpsaveFileName_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 5, 8, 2),
    _SysEvtLogTftpsaveFileName_Type()
)
sysEvtLogTftpsaveFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysEvtLogTftpsaveFileName.setStatus("mandatory")
_SysEvtLogTftpsaveMaxMsgCount_Type = Integer32
_SysEvtLogTftpsaveMaxMsgCount_Object = MibScalar
sysEvtLogTftpsaveMaxMsgCount = _SysEvtLogTftpsaveMaxMsgCount_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 5, 8, 3),
    _SysEvtLogTftpsaveMaxMsgCount_Type()
)
sysEvtLogTftpsaveMaxMsgCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysEvtLogTftpsaveMaxMsgCount.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CENTILLION-SYSTEM-EVENT-LOG-MIB",
    **{"sysEvtLogDuration": sysEvtLogDuration,
       "sysEvtLogPreFilterEntityMap": sysEvtLogPreFilterEntityMap,
       "sysEvtLogPreFilterSeverity": sysEvtLogPreFilterSeverity,
       "sysEvtLogSlotPreFilterTable": sysEvtLogSlotPreFilterTable,
       "sysEvtLogSlotPreFilterEntry": sysEvtLogSlotPreFilterEntry,
       "sysEvtLogSlotPreFilterCardId": sysEvtLogSlotPreFilterCardId,
       "sysEvtLogSlotPreFilterControl": sysEvtLogSlotPreFilterControl,
       "sysEvtLogPortPreFilterTable": sysEvtLogPortPreFilterTable,
       "sysEvtLogPortPreFilterEntry": sysEvtLogPortPreFilterEntry,
       "sysEvtLogPortPreFilterCardId": sysEvtLogPortPreFilterCardId,
       "sysEvtLogPortPreFilterPortId": sysEvtLogPortPreFilterPortId,
       "sysEvtLogPortPreFilterControl": sysEvtLogPortPreFilterControl,
       "sysEvtLogDestMap": sysEvtLogDestMap,
       "sysEvtLogSysLogCfg": sysEvtLogSysLogCfg,
       "sysEvtLogSysLogHostIp": sysEvtLogSysLogHostIp,
       "sysEvtLogSysLogSeverity": sysEvtLogSysLogSeverity,
       "sysEvtLogSysLogFacility": sysEvtLogSysLogFacility,
       "sysEvtLogTftpsaveCfg": sysEvtLogTftpsaveCfg,
       "sysEvtLogTftpsaveHostIp": sysEvtLogTftpsaveHostIp,
       "sysEvtLogTftpsaveFileName": sysEvtLogTftpsaveFileName,
       "sysEvtLogTftpsaveMaxMsgCount": sysEvtLogTftpsaveMaxMsgCount}
)
