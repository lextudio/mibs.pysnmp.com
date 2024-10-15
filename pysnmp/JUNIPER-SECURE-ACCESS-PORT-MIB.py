# SNMP MIB module (JUNIPER-SECURE-ACCESS-PORT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JUNIPER-SECURE-ACCESS-PORT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:14:10 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(jnxExSecureAccessPort,) = mibBuilder.importSymbols(
    "JUNIPER-EX-SMI",
    "jnxExSecureAccessPort")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

jnxExSecureAccessPortMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 2, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class JnxMacLimitExceededAction(Integer32, TextualConvention):
    status = "current"
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
        *(("alarm", 3),
          ("drop", 2),
          ("none", 1),
          ("shutdown", 4))
    )



# MIB Managed Objects in the order of their OIDs

_JnxSecAccessPortMIBNotifications_ObjectIdentity = ObjectIdentity
jnxSecAccessPortMIBNotifications = _JnxSecAccessPortMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 2, 1, 0)
)
_JnxSecAccessPortMIBObjects_ObjectIdentity = ObjectIdentity
jnxSecAccessPortMIBObjects = _JnxSecAccessPortMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 2, 1, 1)
)
_JnxSecAccessPortVlanTable_Object = MibTable
jnxSecAccessPortVlanTable = _JnxSecAccessPortVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    jnxSecAccessPortVlanTable.setStatus("current")
_JnxSecAccessPortVlanEntry_Object = MibTableRow
jnxSecAccessPortVlanEntry = _JnxSecAccessPortVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 2, 1, 1, 1, 1)
)
jnxSecAccessPortVlanEntry.setIndexNames(
    (0, "JUNIPER-SECURE-ACCESS-PORT-MIB", "jnxSecAccessVlanName"),
)
if mibBuilder.loadTexts:
    jnxSecAccessPortVlanEntry.setStatus("current")


class _JnxSecAccessVlanName_Type(DisplayString):
    """Custom type jnxSecAccessVlanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_JnxSecAccessVlanName_Type.__name__ = "DisplayString"
_JnxSecAccessVlanName_Object = MibTableColumn
jnxSecAccessVlanName = _JnxSecAccessVlanName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 2, 1, 1, 1, 1, 1),
    _JnxSecAccessVlanName_Type()
)
jnxSecAccessVlanName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxSecAccessVlanName.setStatus("current")
_JnxSecAccessVlanDhcpSnoopStatus_Type = TruthValue
_JnxSecAccessVlanDhcpSnoopStatus_Object = MibTableColumn
jnxSecAccessVlanDhcpSnoopStatus = _JnxSecAccessVlanDhcpSnoopStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 2, 1, 1, 1, 1, 2),
    _JnxSecAccessVlanDhcpSnoopStatus_Type()
)
jnxSecAccessVlanDhcpSnoopStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSecAccessVlanDhcpSnoopStatus.setStatus("current")
_JnxSecAccessVlanDAIStatus_Type = TruthValue
_JnxSecAccessVlanDAIStatus_Object = MibTableColumn
jnxSecAccessVlanDAIStatus = _JnxSecAccessVlanDAIStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 2, 1, 1, 1, 1, 3),
    _JnxSecAccessVlanDAIStatus_Type()
)
jnxSecAccessVlanDAIStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSecAccessVlanDAIStatus.setStatus("current")
_JnxSecAccessPortIfTable_Object = MibTable
jnxSecAccessPortIfTable = _JnxSecAccessPortIfTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 2, 1, 1, 2)
)
if mibBuilder.loadTexts:
    jnxSecAccessPortIfTable.setStatus("current")
_JnxSecAccessPortIfEntry_Object = MibTableRow
jnxSecAccessPortIfEntry = _JnxSecAccessPortIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 2, 1, 1, 2, 1)
)
jnxSecAccessPortIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    jnxSecAccessPortIfEntry.setStatus("current")
_JnxSecAccessdsIfTrustState_Type = TruthValue
_JnxSecAccessdsIfTrustState_Object = MibTableColumn
jnxSecAccessdsIfTrustState = _JnxSecAccessdsIfTrustState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 2, 1, 1, 2, 1, 1),
    _JnxSecAccessdsIfTrustState_Type()
)
jnxSecAccessdsIfTrustState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSecAccessdsIfTrustState.setStatus("current")
_JnxSecAccessdsIfRateLimit_Type = Unsigned32
_JnxSecAccessdsIfRateLimit_Object = MibTableColumn
jnxSecAccessdsIfRateLimit = _JnxSecAccessdsIfRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 2, 1, 1, 2, 1, 2),
    _JnxSecAccessdsIfRateLimit_Type()
)
jnxSecAccessdsIfRateLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSecAccessdsIfRateLimit.setStatus("current")
if mibBuilder.loadTexts:
    jnxSecAccessdsIfRateLimit.setUnits("packets per second")


class _JnxSecAccessIfMacLimit_Type(Unsigned32):
    """Custom type jnxSecAccessIfMacLimit based on Unsigned32"""
    defaultValue = 5


_JnxSecAccessIfMacLimit_Object = MibTableColumn
jnxSecAccessIfMacLimit = _JnxSecAccessIfMacLimit_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 2, 1, 1, 2, 1, 3),
    _JnxSecAccessIfMacLimit_Type()
)
jnxSecAccessIfMacLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSecAccessIfMacLimit.setStatus("current")
_JnxSecAccessIfMacLimitExceed_Type = JnxMacLimitExceededAction
_JnxSecAccessIfMacLimitExceed_Object = MibTableColumn
jnxSecAccessIfMacLimitExceed = _JnxSecAccessIfMacLimitExceed_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 2, 1, 1, 2, 1, 4),
    _JnxSecAccessIfMacLimitExceed_Type()
)
jnxSecAccessIfMacLimitExceed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSecAccessIfMacLimitExceed.setStatus("current")
_JnxSecAccessIfIpSrcGuardStatus_Type = TruthValue
_JnxSecAccessIfIpSrcGuardStatus_Object = MibTableColumn
jnxSecAccessIfIpSrcGuardStatus = _JnxSecAccessIfIpSrcGuardStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 2, 1, 1, 2, 1, 5),
    _JnxSecAccessIfIpSrcGuardStatus_Type()
)
jnxSecAccessIfIpSrcGuardStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSecAccessIfIpSrcGuardStatus.setStatus("current")
_JnxSecAccessIfMacSrcGuardStatus_Type = TruthValue
_JnxSecAccessIfMacSrcGuardStatus_Object = MibTableColumn
jnxSecAccessIfMacSrcGuardStatus = _JnxSecAccessIfMacSrcGuardStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 2, 1, 1, 2, 1, 6),
    _JnxSecAccessIfMacSrcGuardStatus_Type()
)
jnxSecAccessIfMacSrcGuardStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSecAccessIfMacSrcGuardStatus.setStatus("current")
_JnxStormCtlTable_Object = MibTable
jnxStormCtlTable = _JnxStormCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 2, 1, 1, 3)
)
if mibBuilder.loadTexts:
    jnxStormCtlTable.setStatus("current")
_JnxStormCtlEntry_Object = MibTableRow
jnxStormCtlEntry = _JnxStormCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 2, 1, 1, 3, 1)
)
jnxStormCtlEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "JUNIPER-SECURE-ACCESS-PORT-MIB", "jnxStormCtlIfTrafficType"),
)
if mibBuilder.loadTexts:
    jnxStormCtlEntry.setStatus("current")


class _JnxStormCtlIfTrafficType_Type(Integer32):
    """Custom type jnxStormCtlIfTrafficType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("broadcast", 1),
          ("multicast", 2),
          ("unicast", 3))
    )


_JnxStormCtlIfTrafficType_Type.__name__ = "Integer32"
_JnxStormCtlIfTrafficType_Object = MibTableColumn
jnxStormCtlIfTrafficType = _JnxStormCtlIfTrafficType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 2, 1, 1, 3, 1, 1),
    _JnxStormCtlIfTrafficType_Type()
)
jnxStormCtlIfTrafficType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxStormCtlIfTrafficType.setStatus("current")
_JnxStormCtlRisingThreshold_Type = Integer32
_JnxStormCtlRisingThreshold_Object = MibTableColumn
jnxStormCtlRisingThreshold = _JnxStormCtlRisingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 2, 1, 1, 3, 1, 2),
    _JnxStormCtlRisingThreshold_Type()
)
jnxStormCtlRisingThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxStormCtlRisingThreshold.setStatus("current")
if mibBuilder.loadTexts:
    jnxStormCtlRisingThreshold.setUnits("packets per second")
_JnxStormCtlFallingThreshold_Type = Integer32
_JnxStormCtlFallingThreshold_Object = MibTableColumn
jnxStormCtlFallingThreshold = _JnxStormCtlFallingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 2, 1, 1, 3, 1, 3),
    _JnxStormCtlFallingThreshold_Type()
)
jnxStormCtlFallingThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxStormCtlFallingThreshold.setStatus("current")
if mibBuilder.loadTexts:
    jnxStormCtlFallingThreshold.setUnits("packets per second")


class _JnxStormCtlAction_Type(Integer32):
    """Custom type jnxStormCtlAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("filter", 2),
          ("shutdown", 1))
    )


_JnxStormCtlAction_Type.__name__ = "Integer32"
_JnxStormCtlAction_Object = MibTableColumn
jnxStormCtlAction = _JnxStormCtlAction_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 2, 1, 1, 3, 1, 4),
    _JnxStormCtlAction_Type()
)
jnxStormCtlAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxStormCtlAction.setStatus("current")

# Managed Objects groups


# Notification objects

jnxSecAccessdsRateLimitCrossed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 2, 1, 0, 1)
)
jnxSecAccessdsRateLimitCrossed.setObjects(
    ("JUNIPER-SECURE-ACCESS-PORT-MIB", "jnxSecAccessdsIfRateLimit")
)
if mibBuilder.loadTexts:
    jnxSecAccessdsRateLimitCrossed.setStatus(
        "current"
    )

jnxSecAccessIfMacLimitExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 2, 1, 0, 2)
)
jnxSecAccessIfMacLimitExceeded.setObjects(
      *(("JUNIPER-SECURE-ACCESS-PORT-MIB", "jnxSecAccessIfMacLimit"),
        ("JUNIPER-SECURE-ACCESS-PORT-MIB", "jnxSecAccessIfMacLimitExceed"))
)
if mibBuilder.loadTexts:
    jnxSecAccessIfMacLimitExceeded.setStatus(
        "current"
    )

jnxStormEventNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 2, 1, 0, 3)
)
jnxStormEventNotification.setObjects(
    ("JUNIPER-SECURE-ACCESS-PORT-MIB", "jnxStormCtlRisingThreshold")
)
if mibBuilder.loadTexts:
    jnxStormEventNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-SECURE-ACCESS-PORT-MIB",
    **{"JnxMacLimitExceededAction": JnxMacLimitExceededAction,
       "jnxExSecureAccessPortMIB": jnxExSecureAccessPortMIB,
       "jnxSecAccessPortMIBNotifications": jnxSecAccessPortMIBNotifications,
       "jnxSecAccessdsRateLimitCrossed": jnxSecAccessdsRateLimitCrossed,
       "jnxSecAccessIfMacLimitExceeded": jnxSecAccessIfMacLimitExceeded,
       "jnxStormEventNotification": jnxStormEventNotification,
       "jnxSecAccessPortMIBObjects": jnxSecAccessPortMIBObjects,
       "jnxSecAccessPortVlanTable": jnxSecAccessPortVlanTable,
       "jnxSecAccessPortVlanEntry": jnxSecAccessPortVlanEntry,
       "jnxSecAccessVlanName": jnxSecAccessVlanName,
       "jnxSecAccessVlanDhcpSnoopStatus": jnxSecAccessVlanDhcpSnoopStatus,
       "jnxSecAccessVlanDAIStatus": jnxSecAccessVlanDAIStatus,
       "jnxSecAccessPortIfTable": jnxSecAccessPortIfTable,
       "jnxSecAccessPortIfEntry": jnxSecAccessPortIfEntry,
       "jnxSecAccessdsIfTrustState": jnxSecAccessdsIfTrustState,
       "jnxSecAccessdsIfRateLimit": jnxSecAccessdsIfRateLimit,
       "jnxSecAccessIfMacLimit": jnxSecAccessIfMacLimit,
       "jnxSecAccessIfMacLimitExceed": jnxSecAccessIfMacLimitExceed,
       "jnxSecAccessIfIpSrcGuardStatus": jnxSecAccessIfIpSrcGuardStatus,
       "jnxSecAccessIfMacSrcGuardStatus": jnxSecAccessIfMacSrcGuardStatus,
       "jnxStormCtlTable": jnxStormCtlTable,
       "jnxStormCtlEntry": jnxStormCtlEntry,
       "jnxStormCtlIfTrafficType": jnxStormCtlIfTrafficType,
       "jnxStormCtlRisingThreshold": jnxStormCtlRisingThreshold,
       "jnxStormCtlFallingThreshold": jnxStormCtlFallingThreshold,
       "jnxStormCtlAction": jnxStormCtlAction}
)
