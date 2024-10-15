# SNMP MIB module (BAS-RBP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BAS-RBP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:45:31 2024
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

(BasChassisId,
 BasInterfaceId,
 BasLogicalPortId,
 BasSlotId,
 basRbp) = mibBuilder.importSymbols(
    "BAS-MIB",
    "BasChassisId",
    "BasInterfaceId",
    "BasLogicalPortId",
    "BasSlotId",
    "basRbp")

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

basRbpMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 2, 6, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BasRbpConfig_ObjectIdentity = ObjectIdentity
basRbpConfig = _BasRbpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 2, 6, 1, 1)
)
_BasRbpTargetTable_Object = MibTable
basRbpTargetTable = _BasRbpTargetTable_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 6, 1, 1, 1)
)
if mibBuilder.loadTexts:
    basRbpTargetTable.setStatus("current")
_BasRbpTargetEntry_Object = MibTableRow
basRbpTargetEntry = _BasRbpTargetEntry_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 6, 1, 1, 1, 1)
)
basRbpTargetEntry.setIndexNames(
    (0, "BAS-RBP-MIB", "basRbpChassis"),
    (0, "BAS-RBP-MIB", "basRbpSlot"),
    (0, "BAS-RBP-MIB", "basRbpIf"),
    (0, "BAS-RBP-MIB", "basRbpLPort"),
    (0, "BAS-RBP-MIB", "basRbpTargetChassis"),
    (0, "BAS-RBP-MIB", "basRbpTargetSlot"),
    (0, "BAS-RBP-MIB", "basRbpTargetIf"),
    (0, "BAS-RBP-MIB", "basRbpTargetLPort"),
)
if mibBuilder.loadTexts:
    basRbpTargetEntry.setStatus("current")
_BasRbpChassis_Type = BasChassisId
_BasRbpChassis_Object = MibTableColumn
basRbpChassis = _BasRbpChassis_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 6, 1, 1, 1, 1, 1),
    _BasRbpChassis_Type()
)
basRbpChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basRbpChassis.setStatus("current")
_BasRbpSlot_Type = BasSlotId
_BasRbpSlot_Object = MibTableColumn
basRbpSlot = _BasRbpSlot_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 6, 1, 1, 1, 1, 2),
    _BasRbpSlot_Type()
)
basRbpSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basRbpSlot.setStatus("current")
_BasRbpIf_Type = BasInterfaceId
_BasRbpIf_Object = MibTableColumn
basRbpIf = _BasRbpIf_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 6, 1, 1, 1, 1, 3),
    _BasRbpIf_Type()
)
basRbpIf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basRbpIf.setStatus("current")
_BasRbpLPort_Type = BasLogicalPortId
_BasRbpLPort_Object = MibTableColumn
basRbpLPort = _BasRbpLPort_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 6, 1, 1, 1, 1, 4),
    _BasRbpLPort_Type()
)
basRbpLPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basRbpLPort.setStatus("current")
_BasRbpTargetChassis_Type = BasChassisId
_BasRbpTargetChassis_Object = MibTableColumn
basRbpTargetChassis = _BasRbpTargetChassis_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 6, 1, 1, 1, 1, 5),
    _BasRbpTargetChassis_Type()
)
basRbpTargetChassis.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basRbpTargetChassis.setStatus("current")
_BasRbpTargetSlot_Type = BasSlotId
_BasRbpTargetSlot_Object = MibTableColumn
basRbpTargetSlot = _BasRbpTargetSlot_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 6, 1, 1, 1, 1, 6),
    _BasRbpTargetSlot_Type()
)
basRbpTargetSlot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basRbpTargetSlot.setStatus("current")
_BasRbpTargetIf_Type = BasInterfaceId
_BasRbpTargetIf_Object = MibTableColumn
basRbpTargetIf = _BasRbpTargetIf_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 6, 1, 1, 1, 1, 7),
    _BasRbpTargetIf_Type()
)
basRbpTargetIf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basRbpTargetIf.setStatus("current")
_BasRbpTargetLPort_Type = BasLogicalPortId
_BasRbpTargetLPort_Object = MibTableColumn
basRbpTargetLPort = _BasRbpTargetLPort_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 6, 1, 1, 1, 1, 8),
    _BasRbpTargetLPort_Type()
)
basRbpTargetLPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basRbpTargetLPort.setStatus("current")
_BasRbpTargetStatus_Type = RowStatus
_BasRbpTargetStatus_Object = MibTableColumn
basRbpTargetStatus = _BasRbpTargetStatus_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 6, 1, 1, 1, 1, 9),
    _BasRbpTargetStatus_Type()
)
basRbpTargetStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basRbpTargetStatus.setStatus("current")
_BasRbpAppTable_Object = MibTable
basRbpAppTable = _BasRbpAppTable_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 6, 1, 1, 2)
)
if mibBuilder.loadTexts:
    basRbpAppTable.setStatus("current")
_BasRbpAppEntry_Object = MibTableRow
basRbpAppEntry = _BasRbpAppEntry_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 6, 1, 1, 2, 1)
)
basRbpAppEntry.setIndexNames(
    (0, "BAS-RBP-MIB", "basRbpAppChassis"),
    (0, "BAS-RBP-MIB", "basRbpAppSlot"),
    (0, "BAS-RBP-MIB", "basRbpAppIf"),
    (0, "BAS-RBP-MIB", "basRbpAppLPort"),
    (0, "BAS-RBP-MIB", "basRbpAppType"),
)
if mibBuilder.loadTexts:
    basRbpAppEntry.setStatus("current")
_BasRbpAppChassis_Type = BasChassisId
_BasRbpAppChassis_Object = MibTableColumn
basRbpAppChassis = _BasRbpAppChassis_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 6, 1, 1, 2, 1, 1),
    _BasRbpAppChassis_Type()
)
basRbpAppChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basRbpAppChassis.setStatus("current")
_BasRbpAppSlot_Type = BasSlotId
_BasRbpAppSlot_Object = MibTableColumn
basRbpAppSlot = _BasRbpAppSlot_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 6, 1, 1, 2, 1, 2),
    _BasRbpAppSlot_Type()
)
basRbpAppSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basRbpAppSlot.setStatus("current")
_BasRbpAppIf_Type = BasInterfaceId
_BasRbpAppIf_Object = MibTableColumn
basRbpAppIf = _BasRbpAppIf_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 6, 1, 1, 2, 1, 3),
    _BasRbpAppIf_Type()
)
basRbpAppIf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basRbpAppIf.setStatus("current")
_BasRbpAppLPort_Type = BasLogicalPortId
_BasRbpAppLPort_Object = MibTableColumn
basRbpAppLPort = _BasRbpAppLPort_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 6, 1, 1, 2, 1, 4),
    _BasRbpAppLPort_Type()
)
basRbpAppLPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basRbpAppLPort.setStatus("current")


class _BasRbpAppType_Type(Integer32):
    """Custom type basRbpAppType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("rbpFwdType", 1),
          ("rbpGFilterType", 3),
          ("rbpMcastType", 2))
    )


_BasRbpAppType_Type.__name__ = "Integer32"
_BasRbpAppType_Object = MibTableColumn
basRbpAppType = _BasRbpAppType_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 6, 1, 1, 2, 1, 5),
    _BasRbpAppType_Type()
)
basRbpAppType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basRbpAppType.setStatus("current")


class _BasRbpAppBusy_Type(Integer32):
    """Custom type basRbpAppBusy based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("busy", 1),
          ("notBusy", 2))
    )


_BasRbpAppBusy_Type.__name__ = "Integer32"
_BasRbpAppBusy_Object = MibTableColumn
basRbpAppBusy = _BasRbpAppBusy_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 6, 1, 1, 2, 1, 6),
    _BasRbpAppBusy_Type()
)
basRbpAppBusy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basRbpAppBusy.setStatus("current")
_BasRbpAppBroadcastPktSent_Type = Counter32
_BasRbpAppBroadcastPktSent_Object = MibTableColumn
basRbpAppBroadcastPktSent = _BasRbpAppBroadcastPktSent_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 6, 1, 1, 2, 1, 7),
    _BasRbpAppBroadcastPktSent_Type()
)
basRbpAppBroadcastPktSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basRbpAppBroadcastPktSent.setStatus("current")
_BasRbpAppPktRcv_Type = Counter32
_BasRbpAppPktRcv_Object = MibTableColumn
basRbpAppPktRcv = _BasRbpAppPktRcv_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 6, 1, 1, 2, 1, 8),
    _BasRbpAppPktRcv_Type()
)
basRbpAppPktRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basRbpAppPktRcv.setStatus("current")
_BasRbpAppUnicastPktSent_Type = Counter32
_BasRbpAppUnicastPktSent_Object = MibTableColumn
basRbpAppUnicastPktSent = _BasRbpAppUnicastPktSent_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 6, 1, 1, 2, 1, 9),
    _BasRbpAppUnicastPktSent_Type()
)
basRbpAppUnicastPktSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basRbpAppUnicastPktSent.setStatus("current")
_BasRbpAppAckRcv_Type = Counter32
_BasRbpAppAckRcv_Object = MibTableColumn
basRbpAppAckRcv = _BasRbpAppAckRcv_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 6, 1, 1, 2, 1, 10),
    _BasRbpAppAckRcv_Type()
)
basRbpAppAckRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basRbpAppAckRcv.setStatus("current")
_BasRbpAppAckSent_Type = Counter32
_BasRbpAppAckSent_Object = MibTableColumn
basRbpAppAckSent = _BasRbpAppAckSent_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 6, 1, 1, 2, 1, 11),
    _BasRbpAppAckSent_Type()
)
basRbpAppAckSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basRbpAppAckSent.setStatus("current")
_BasRbpAppRetryCount_Type = Counter32
_BasRbpAppRetryCount_Object = MibTableColumn
basRbpAppRetryCount = _BasRbpAppRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 6, 1, 1, 2, 1, 12),
    _BasRbpAppRetryCount_Type()
)
basRbpAppRetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basRbpAppRetryCount.setStatus("current")
_BasRbpAppRequestFailCount_Type = Counter32
_BasRbpAppRequestFailCount_Object = MibTableColumn
basRbpAppRequestFailCount = _BasRbpAppRequestFailCount_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 6, 1, 1, 2, 1, 13),
    _BasRbpAppRequestFailCount_Type()
)
basRbpAppRequestFailCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basRbpAppRequestFailCount.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BAS-RBP-MIB",
    **{"basRbpMib": basRbpMib,
       "basRbpConfig": basRbpConfig,
       "basRbpTargetTable": basRbpTargetTable,
       "basRbpTargetEntry": basRbpTargetEntry,
       "basRbpChassis": basRbpChassis,
       "basRbpSlot": basRbpSlot,
       "basRbpIf": basRbpIf,
       "basRbpLPort": basRbpLPort,
       "basRbpTargetChassis": basRbpTargetChassis,
       "basRbpTargetSlot": basRbpTargetSlot,
       "basRbpTargetIf": basRbpTargetIf,
       "basRbpTargetLPort": basRbpTargetLPort,
       "basRbpTargetStatus": basRbpTargetStatus,
       "basRbpAppTable": basRbpAppTable,
       "basRbpAppEntry": basRbpAppEntry,
       "basRbpAppChassis": basRbpAppChassis,
       "basRbpAppSlot": basRbpAppSlot,
       "basRbpAppIf": basRbpAppIf,
       "basRbpAppLPort": basRbpAppLPort,
       "basRbpAppType": basRbpAppType,
       "basRbpAppBusy": basRbpAppBusy,
       "basRbpAppBroadcastPktSent": basRbpAppBroadcastPktSent,
       "basRbpAppPktRcv": basRbpAppPktRcv,
       "basRbpAppUnicastPktSent": basRbpAppUnicastPktSent,
       "basRbpAppAckRcv": basRbpAppAckRcv,
       "basRbpAppAckSent": basRbpAppAckSent,
       "basRbpAppRetryCount": basRbpAppRetryCount,
       "basRbpAppRequestFailCount": basRbpAppRequestFailCount}
)
