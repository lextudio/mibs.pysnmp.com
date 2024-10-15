# SNMP MIB module (BAS-UDP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BAS-UDP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:45:37 2024
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
 basAliasUdp) = mibBuilder.importSymbols(
    "BAS-MIB",
    "BasChassisId",
    "BasInterfaceId",
    "BasLogicalPortId",
    "BasSlotId",
    "basAliasUdp")

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

basAliasUdpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 4, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BasUdpObjects_ObjectIdentity = ObjectIdentity
basUdpObjects = _BasUdpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 4, 1, 1)
)
_BasUdpGroupTable_Object = MibTable
basUdpGroupTable = _BasUdpGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 4, 1, 1, 1)
)
if mibBuilder.loadTexts:
    basUdpGroupTable.setStatus("current")
_BasUdpGroupEntry_Object = MibTableRow
basUdpGroupEntry = _BasUdpGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 4, 1, 1, 1, 1)
)
basUdpGroupEntry.setIndexNames(
    (0, "BAS-UDP-MIB", "basUdpGroupChassis"),
    (0, "BAS-UDP-MIB", "basUdpGroupSlot"),
    (0, "BAS-UDP-MIB", "basUdpGroupIf"),
    (0, "BAS-UDP-MIB", "basUdpGroupLPort"),
)
if mibBuilder.loadTexts:
    basUdpGroupEntry.setStatus("current")
_BasUdpInDatagrams_Type = Counter32
_BasUdpInDatagrams_Object = MibTableColumn
basUdpInDatagrams = _BasUdpInDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 4, 1, 1, 1, 1, 1),
    _BasUdpInDatagrams_Type()
)
basUdpInDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basUdpInDatagrams.setStatus("current")
_BasUdpNoPorts_Type = Counter32
_BasUdpNoPorts_Object = MibTableColumn
basUdpNoPorts = _BasUdpNoPorts_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 4, 1, 1, 1, 1, 2),
    _BasUdpNoPorts_Type()
)
basUdpNoPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basUdpNoPorts.setStatus("current")
_BasUdpInErrors_Type = Counter32
_BasUdpInErrors_Object = MibTableColumn
basUdpInErrors = _BasUdpInErrors_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 4, 1, 1, 1, 1, 3),
    _BasUdpInErrors_Type()
)
basUdpInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basUdpInErrors.setStatus("current")
_BasUdpOutDatagrams_Type = Counter32
_BasUdpOutDatagrams_Object = MibTableColumn
basUdpOutDatagrams = _BasUdpOutDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 4, 1, 1, 1, 1, 4),
    _BasUdpOutDatagrams_Type()
)
basUdpOutDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basUdpOutDatagrams.setStatus("current")
_BasUdpGroupChassis_Type = BasChassisId
_BasUdpGroupChassis_Object = MibTableColumn
basUdpGroupChassis = _BasUdpGroupChassis_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 4, 1, 1, 1, 1, 5),
    _BasUdpGroupChassis_Type()
)
basUdpGroupChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basUdpGroupChassis.setStatus("current")
_BasUdpGroupSlot_Type = BasSlotId
_BasUdpGroupSlot_Object = MibTableColumn
basUdpGroupSlot = _BasUdpGroupSlot_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 4, 1, 1, 1, 1, 6),
    _BasUdpGroupSlot_Type()
)
basUdpGroupSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basUdpGroupSlot.setStatus("current")
_BasUdpGroupIf_Type = BasInterfaceId
_BasUdpGroupIf_Object = MibTableColumn
basUdpGroupIf = _BasUdpGroupIf_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 4, 1, 1, 1, 1, 7),
    _BasUdpGroupIf_Type()
)
basUdpGroupIf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basUdpGroupIf.setStatus("current")
_BasUdpGroupLPort_Type = BasLogicalPortId
_BasUdpGroupLPort_Object = MibTableColumn
basUdpGroupLPort = _BasUdpGroupLPort_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 4, 1, 1, 1, 1, 8),
    _BasUdpGroupLPort_Type()
)
basUdpGroupLPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basUdpGroupLPort.setStatus("current")
_BasUdpTable_Object = MibTable
basUdpTable = _BasUdpTable_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 4, 1, 1, 2)
)
if mibBuilder.loadTexts:
    basUdpTable.setStatus("current")
_BasUdpEntry_Object = MibTableRow
basUdpEntry = _BasUdpEntry_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 4, 1, 1, 2, 1)
)
basUdpEntry.setIndexNames(
    (0, "BAS-UDP-MIB", "basUdpLisChassis"),
    (0, "BAS-UDP-MIB", "basUdpLisSlot"),
    (0, "BAS-UDP-MIB", "basUdpLisIf"),
    (0, "BAS-UDP-MIB", "basUdpLisLPort"),
    (0, "BAS-UDP-MIB", "basUdpLocalAddress"),
    (0, "BAS-UDP-MIB", "basUdpLocalPort"),
)
if mibBuilder.loadTexts:
    basUdpEntry.setStatus("current")
_BasUdpLocalAddress_Type = IpAddress
_BasUdpLocalAddress_Object = MibTableColumn
basUdpLocalAddress = _BasUdpLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 4, 1, 1, 2, 1, 1),
    _BasUdpLocalAddress_Type()
)
basUdpLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basUdpLocalAddress.setStatus("current")


class _BasUdpLocalPort_Type(Integer32):
    """Custom type basUdpLocalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BasUdpLocalPort_Type.__name__ = "Integer32"
_BasUdpLocalPort_Object = MibTableColumn
basUdpLocalPort = _BasUdpLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 4, 1, 1, 2, 1, 2),
    _BasUdpLocalPort_Type()
)
basUdpLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basUdpLocalPort.setStatus("current")
_BasUdpLisChassis_Type = BasChassisId
_BasUdpLisChassis_Object = MibTableColumn
basUdpLisChassis = _BasUdpLisChassis_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 4, 1, 1, 2, 1, 3),
    _BasUdpLisChassis_Type()
)
basUdpLisChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basUdpLisChassis.setStatus("current")
_BasUdpLisSlot_Type = BasSlotId
_BasUdpLisSlot_Object = MibTableColumn
basUdpLisSlot = _BasUdpLisSlot_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 4, 1, 1, 2, 1, 4),
    _BasUdpLisSlot_Type()
)
basUdpLisSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basUdpLisSlot.setStatus("current")
_BasUdpLisIf_Type = BasInterfaceId
_BasUdpLisIf_Object = MibTableColumn
basUdpLisIf = _BasUdpLisIf_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 4, 1, 1, 2, 1, 5),
    _BasUdpLisIf_Type()
)
basUdpLisIf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basUdpLisIf.setStatus("current")
_BasUdpLisLPort_Type = BasLogicalPortId
_BasUdpLisLPort_Object = MibTableColumn
basUdpLisLPort = _BasUdpLisLPort_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 4, 1, 1, 2, 1, 6),
    _BasUdpLisLPort_Type()
)
basUdpLisLPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basUdpLisLPort.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BAS-UDP-MIB",
    **{"basAliasUdpMIB": basAliasUdpMIB,
       "basUdpObjects": basUdpObjects,
       "basUdpGroupTable": basUdpGroupTable,
       "basUdpGroupEntry": basUdpGroupEntry,
       "basUdpInDatagrams": basUdpInDatagrams,
       "basUdpNoPorts": basUdpNoPorts,
       "basUdpInErrors": basUdpInErrors,
       "basUdpOutDatagrams": basUdpOutDatagrams,
       "basUdpGroupChassis": basUdpGroupChassis,
       "basUdpGroupSlot": basUdpGroupSlot,
       "basUdpGroupIf": basUdpGroupIf,
       "basUdpGroupLPort": basUdpGroupLPort,
       "basUdpTable": basUdpTable,
       "basUdpEntry": basUdpEntry,
       "basUdpLocalAddress": basUdpLocalAddress,
       "basUdpLocalPort": basUdpLocalPort,
       "basUdpLisChassis": basUdpLisChassis,
       "basUdpLisSlot": basUdpLisSlot,
       "basUdpLisIf": basUdpLisIf,
       "basUdpLisLPort": basUdpLisLPort}
)
