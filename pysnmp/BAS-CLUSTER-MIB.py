# SNMP MIB module (BAS-CLUSTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BAS-CLUSTER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:45:21 2024
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
 basCluster) = mibBuilder.importSymbols(
    "BAS-MIB",
    "BasChassisId",
    "BasInterfaceId",
    "BasLogicalPortId",
    "BasSlotId",
    "basCluster")

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

basClusterMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 2, 18, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BasClusterConfig_ObjectIdentity = ObjectIdentity
basClusterConfig = _BasClusterConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 2, 18, 1, 1)
)
_BasClChTable_Object = MibTable
basClChTable = _BasClChTable_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 18, 1, 1, 1)
)
if mibBuilder.loadTexts:
    basClChTable.setStatus("current")
_BasClChEntry_Object = MibTableRow
basClChEntry = _BasClChEntry_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 18, 1, 1, 1, 1)
)
basClChEntry.setIndexNames(
    (0, "BAS-CLUSTER-MIB", "basClChLocalChassis"),
    (0, "BAS-CLUSTER-MIB", "basClChLocalSlot"),
    (0, "BAS-CLUSTER-MIB", "basClChLocalIf"),
    (0, "BAS-CLUSTER-MIB", "basClChLocalLPort"),
    (0, "BAS-CLUSTER-MIB", "basClChRemoteChassis"),
)
if mibBuilder.loadTexts:
    basClChEntry.setStatus("current")
_BasClChLocalChassis_Type = BasChassisId
_BasClChLocalChassis_Object = MibTableColumn
basClChLocalChassis = _BasClChLocalChassis_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 18, 1, 1, 1, 1, 1),
    _BasClChLocalChassis_Type()
)
basClChLocalChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basClChLocalChassis.setStatus("current")
_BasClChLocalSlot_Type = BasSlotId
_BasClChLocalSlot_Object = MibTableColumn
basClChLocalSlot = _BasClChLocalSlot_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 18, 1, 1, 1, 1, 2),
    _BasClChLocalSlot_Type()
)
basClChLocalSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basClChLocalSlot.setStatus("current")
_BasClChLocalIf_Type = BasInterfaceId
_BasClChLocalIf_Object = MibTableColumn
basClChLocalIf = _BasClChLocalIf_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 18, 1, 1, 1, 1, 3),
    _BasClChLocalIf_Type()
)
basClChLocalIf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basClChLocalIf.setStatus("current")
_BasClChLocalLPort_Type = BasLogicalPortId
_BasClChLocalLPort_Object = MibTableColumn
basClChLocalLPort = _BasClChLocalLPort_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 18, 1, 1, 1, 1, 4),
    _BasClChLocalLPort_Type()
)
basClChLocalLPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basClChLocalLPort.setStatus("current")
_BasClChRemoteChassis_Type = BasChassisId
_BasClChRemoteChassis_Object = MibTableColumn
basClChRemoteChassis = _BasClChRemoteChassis_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 18, 1, 1, 1, 1, 5),
    _BasClChRemoteChassis_Type()
)
basClChRemoteChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basClChRemoteChassis.setStatus("current")


class _BasClChLocalNextSlot_Type(Integer32):
    """Custom type basClChLocalNextSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_BasClChLocalNextSlot_Type.__name__ = "Integer32"
_BasClChLocalNextSlot_Object = MibTableColumn
basClChLocalNextSlot = _BasClChLocalNextSlot_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 18, 1, 1, 1, 1, 6),
    _BasClChLocalNextSlot_Type()
)
basClChLocalNextSlot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basClChLocalNextSlot.setStatus("current")
_BasClChLocalNextIf_Type = BasInterfaceId
_BasClChLocalNextIf_Object = MibTableColumn
basClChLocalNextIf = _BasClChLocalNextIf_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 18, 1, 1, 1, 1, 7),
    _BasClChLocalNextIf_Type()
)
basClChLocalNextIf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basClChLocalNextIf.setStatus("current")
_BasClChLocalNextLPort_Type = BasLogicalPortId
_BasClChLocalNextLPort_Object = MibTableColumn
basClChLocalNextLPort = _BasClChLocalNextLPort_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 18, 1, 1, 1, 1, 8),
    _BasClChLocalNextLPort_Type()
)
basClChLocalNextLPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basClChLocalNextLPort.setStatus("current")


class _BasClChTargetStatus_Type(Integer32):
    """Custom type basClChTargetStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_BasClChTargetStatus_Type.__name__ = "Integer32"
_BasClChTargetStatus_Object = MibTableColumn
basClChTargetStatus = _BasClChTargetStatus_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 18, 1, 1, 1, 1, 9),
    _BasClChTargetStatus_Type()
)
basClChTargetStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basClChTargetStatus.setStatus("current")


class _BasClChArpFlags_Type(Bits):
    """Custom type basClChArpFlags based on Bits"""
    namedValues = NamedValues(
        *(("clear", 0),
          ("cmtsOk", 5),
          ("cmtsWaiting", 4),
          ("doNotQueue", 2),
          ("doNotTimeout", 3),
          ("waiting", 1))
    )

_BasClChArpFlags_Type.__name__ = "Bits"
_BasClChArpFlags_Object = MibTableColumn
basClChArpFlags = _BasClChArpFlags_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 18, 1, 1, 1, 1, 10),
    _BasClChArpFlags_Type()
)
basClChArpFlags.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basClChArpFlags.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BAS-CLUSTER-MIB",
    **{"basClusterMib": basClusterMib,
       "basClusterConfig": basClusterConfig,
       "basClChTable": basClChTable,
       "basClChEntry": basClChEntry,
       "basClChLocalChassis": basClChLocalChassis,
       "basClChLocalSlot": basClChLocalSlot,
       "basClChLocalIf": basClChLocalIf,
       "basClChLocalLPort": basClChLocalLPort,
       "basClChRemoteChassis": basClChRemoteChassis,
       "basClChLocalNextSlot": basClChLocalNextSlot,
       "basClChLocalNextIf": basClChLocalNextIf,
       "basClChLocalNextLPort": basClChLocalNextLPort,
       "basClChTargetStatus": basClChTargetStatus,
       "basClChArpFlags": basClChArpFlags}
)
