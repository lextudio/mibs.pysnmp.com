# SNMP MIB module (EXTREME-IDMGR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EXTREME-IDMGR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:41:44 2024
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

(extremeAgent,) = mibBuilder.importSymbols(
    "EXTREME-BASE-MIB",
    "extremeAgent")

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

extremeIdMgr = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 36)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ExtremeIdMgrTraps_ObjectIdentity = ObjectIdentity
extremeIdMgrTraps = _ExtremeIdMgrTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 36, 1)
)
_ExtremeIdMgrTrapPrefix_ObjectIdentity = ObjectIdentity
extremeIdMgrTrapPrefix = _ExtremeIdMgrTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 36, 1, 0)
)


class _ExtremeIdMgrTrapSeverity_Type(Integer32):
    """Custom type extremeIdMgrTrapSeverity based on Integer32"""
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
        *(("critical", 1),
          ("debug-data", 8),
          ("debug-summary", 6),
          ("debug-verbose", 7),
          ("error", 2),
          ("info", 5),
          ("notice", 4),
          ("warning", 3))
    )


_ExtremeIdMgrTrapSeverity_Type.__name__ = "Integer32"
_ExtremeIdMgrTrapSeverity_Object = MibScalar
extremeIdMgrTrapSeverity = _ExtremeIdMgrTrapSeverity_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 36, 1, 1),
    _ExtremeIdMgrTrapSeverity_Type()
)
extremeIdMgrTrapSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeIdMgrTrapSeverity.setStatus("current")


class _ExtremeIdMgrMemUsageLevel_Type(Integer32):
    """Custom type extremeIdMgrMemUsageLevel based on Integer32"""
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
        *(("critical", 3),
          ("high", 2),
          ("maximum", 4),
          ("normal", 1))
    )


_ExtremeIdMgrMemUsageLevel_Type.__name__ = "Integer32"
_ExtremeIdMgrMemUsageLevel_Object = MibScalar
extremeIdMgrMemUsageLevel = _ExtremeIdMgrMemUsageLevel_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 36, 1, 2),
    _ExtremeIdMgrMemUsageLevel_Type()
)
extremeIdMgrMemUsageLevel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeIdMgrMemUsageLevel.setStatus("current")
_ExtremeIdMgrMemUsage_Type = Integer32
_ExtremeIdMgrMemUsage_Object = MibScalar
extremeIdMgrMemUsage = _ExtremeIdMgrMemUsage_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 36, 1, 3),
    _ExtremeIdMgrMemUsage_Type()
)
extremeIdMgrMemUsage.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeIdMgrMemUsage.setStatus("current")
_ExtremeIdMgrMemMaxSize_Type = Integer32
_ExtremeIdMgrMemMaxSize_Object = MibScalar
extremeIdMgrMemMaxSize = _ExtremeIdMgrMemMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 36, 1, 4),
    _ExtremeIdMgrMemMaxSize_Type()
)
extremeIdMgrMemMaxSize.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeIdMgrMemMaxSize.setStatus("current")
_ExtremeIdMgrEffectiveStaleAgingTime_Type = Integer32
_ExtremeIdMgrEffectiveStaleAgingTime_Object = MibScalar
extremeIdMgrEffectiveStaleAgingTime = _ExtremeIdMgrEffectiveStaleAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 36, 1, 5),
    _ExtremeIdMgrEffectiveStaleAgingTime_Type()
)
extremeIdMgrEffectiveStaleAgingTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeIdMgrEffectiveStaleAgingTime.setStatus("current")

# Managed Objects groups


# Notification objects

extremeIdMgrMemLevelChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 1, 36, 1, 0, 1)
)
extremeIdMgrMemLevelChange.setObjects(
      *(("EXTREME-IDMGR-MIB", "extremeIdMgrTrapSeverity"),
        ("EXTREME-IDMGR-MIB", "extremeIdMgrMemUsageLevel"),
        ("EXTREME-IDMGR-MIB", "extremeIdMgrMemUsage"),
        ("EXTREME-IDMGR-MIB", "extremeIdMgrMemMaxSize"),
        ("EXTREME-IDMGR-MIB", "extremeIdMgrEffectiveStaleAgingTime"))
)
if mibBuilder.loadTexts:
    extremeIdMgrMemLevelChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EXTREME-IDMGR-MIB",
    **{"extremeIdMgr": extremeIdMgr,
       "extremeIdMgrTraps": extremeIdMgrTraps,
       "extremeIdMgrTrapPrefix": extremeIdMgrTrapPrefix,
       "extremeIdMgrMemLevelChange": extremeIdMgrMemLevelChange,
       "extremeIdMgrTrapSeverity": extremeIdMgrTrapSeverity,
       "extremeIdMgrMemUsageLevel": extremeIdMgrMemUsageLevel,
       "extremeIdMgrMemUsage": extremeIdMgrMemUsage,
       "extremeIdMgrMemMaxSize": extremeIdMgrMemMaxSize,
       "extremeIdMgrEffectiveStaleAgingTime": extremeIdMgrEffectiveStaleAgingTime}
)
