# SNMP MIB module (BAS-IP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BAS-IP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:45:27 2024
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

(BasCardClass,
 BasChassisId,
 BasInterfaceId,
 BasLogicalPortId,
 BasSlotId,
 basExtIp) = mibBuilder.importSymbols(
    "BAS-MIB",
    "BasCardClass",
    "BasChassisId",
    "BasInterfaceId",
    "BasLogicalPortId",
    "BasSlotId",
    "basExtIp")

(IANAifType,) = mibBuilder.importSymbols(
    "IANAifType-MIB",
    "IANAifType")

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

basIpMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 2, 3, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BasIp_ObjectIdentity = ObjectIdentity
basIp = _BasIp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 2, 3, 1, 1)
)
_BasIpAddrTable_Object = MibTable
basIpAddrTable = _BasIpAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 3, 1, 1, 1)
)
if mibBuilder.loadTexts:
    basIpAddrTable.setStatus("current")
_BasIpAddrEntry_Object = MibTableRow
basIpAddrEntry = _BasIpAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 3, 1, 1, 1, 1)
)
basIpAddrEntry.setIndexNames(
    (0, "BAS-IP-MIB", "basIpAdEntChassis"),
    (0, "BAS-IP-MIB", "basIpAdEntSlot"),
    (0, "BAS-IP-MIB", "basIpAdEntIf"),
    (0, "BAS-IP-MIB", "basIpAdEntLPort"),
    (0, "BAS-IP-MIB", "basIpAdEntAddr"),
)
if mibBuilder.loadTexts:
    basIpAddrEntry.setStatus("current")
_BasIpAdEntChassis_Type = BasChassisId
_BasIpAdEntChassis_Object = MibTableColumn
basIpAdEntChassis = _BasIpAdEntChassis_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 3, 1, 1, 1, 1, 1),
    _BasIpAdEntChassis_Type()
)
basIpAdEntChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basIpAdEntChassis.setStatus("current")
_BasIpAdEntSlot_Type = BasSlotId
_BasIpAdEntSlot_Object = MibTableColumn
basIpAdEntSlot = _BasIpAdEntSlot_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 3, 1, 1, 1, 1, 2),
    _BasIpAdEntSlot_Type()
)
basIpAdEntSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basIpAdEntSlot.setStatus("current")
_BasIpAdEntIf_Type = BasInterfaceId
_BasIpAdEntIf_Object = MibTableColumn
basIpAdEntIf = _BasIpAdEntIf_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 3, 1, 1, 1, 1, 3),
    _BasIpAdEntIf_Type()
)
basIpAdEntIf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basIpAdEntIf.setStatus("current")
_BasIpAdEntLPort_Type = BasLogicalPortId
_BasIpAdEntLPort_Object = MibTableColumn
basIpAdEntLPort = _BasIpAdEntLPort_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 3, 1, 1, 1, 1, 4),
    _BasIpAdEntLPort_Type()
)
basIpAdEntLPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basIpAdEntLPort.setStatus("current")
_BasIpAdEntAddr_Type = IpAddress
_BasIpAdEntAddr_Object = MibTableColumn
basIpAdEntAddr = _BasIpAdEntAddr_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 3, 1, 1, 1, 1, 5),
    _BasIpAdEntAddr_Type()
)
basIpAdEntAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basIpAdEntAddr.setStatus("current")


class _BasIpAdEntIfIndex_Type(Integer32):
    """Custom type basIpAdEntIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_BasIpAdEntIfIndex_Type.__name__ = "Integer32"
_BasIpAdEntIfIndex_Object = MibTableColumn
basIpAdEntIfIndex = _BasIpAdEntIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 3, 1, 1, 1, 1, 6),
    _BasIpAdEntIfIndex_Type()
)
basIpAdEntIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basIpAdEntIfIndex.setStatus("current")
_BasIpAdEntNetMask_Type = IpAddress
_BasIpAdEntNetMask_Object = MibTableColumn
basIpAdEntNetMask = _BasIpAdEntNetMask_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 3, 1, 1, 1, 1, 7),
    _BasIpAdEntNetMask_Type()
)
basIpAdEntNetMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basIpAdEntNetMask.setStatus("current")


class _BasIpAdEntBcastAddr_Type(Integer32):
    """Custom type basIpAdEntBcastAddr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_BasIpAdEntBcastAddr_Type.__name__ = "Integer32"
_BasIpAdEntBcastAddr_Object = MibTableColumn
basIpAdEntBcastAddr = _BasIpAdEntBcastAddr_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 3, 1, 1, 1, 1, 8),
    _BasIpAdEntBcastAddr_Type()
)
basIpAdEntBcastAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basIpAdEntBcastAddr.setStatus("current")


class _BasIpAdEntReasmMaxSize_Type(Integer32):
    """Custom type basIpAdEntReasmMaxSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BasIpAdEntReasmMaxSize_Type.__name__ = "Integer32"
_BasIpAdEntReasmMaxSize_Object = MibTableColumn
basIpAdEntReasmMaxSize = _BasIpAdEntReasmMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 3, 1, 1, 1, 1, 9),
    _BasIpAdEntReasmMaxSize_Type()
)
basIpAdEntReasmMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basIpAdEntReasmMaxSize.setStatus("current")
_BasIpAdEntStatus_Type = RowStatus
_BasIpAdEntStatus_Object = MibTableColumn
basIpAdEntStatus = _BasIpAdEntStatus_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 3, 1, 1, 1, 1, 10),
    _BasIpAdEntStatus_Type()
)
basIpAdEntStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basIpAdEntStatus.setStatus("current")
_BasIpAdEntCardType_Type = BasCardClass
_BasIpAdEntCardType_Object = MibTableColumn
basIpAdEntCardType = _BasIpAdEntCardType_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 3, 1, 1, 1, 1, 11),
    _BasIpAdEntCardType_Type()
)
basIpAdEntCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basIpAdEntCardType.setStatus("current")


class _BasIpAdEntPriority_Type(Integer32):
    """Custom type basIpAdEntPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_BasIpAdEntPriority_Type.__name__ = "Integer32"
_BasIpAdEntPriority_Object = MibTableColumn
basIpAdEntPriority = _BasIpAdEntPriority_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 3, 1, 1, 1, 1, 12),
    _BasIpAdEntPriority_Type()
)
basIpAdEntPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basIpAdEntPriority.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BAS-IP-MIB",
    **{"basIpMib": basIpMib,
       "basIp": basIp,
       "basIpAddrTable": basIpAddrTable,
       "basIpAddrEntry": basIpAddrEntry,
       "basIpAdEntChassis": basIpAdEntChassis,
       "basIpAdEntSlot": basIpAdEntSlot,
       "basIpAdEntIf": basIpAdEntIf,
       "basIpAdEntLPort": basIpAdEntLPort,
       "basIpAdEntAddr": basIpAdEntAddr,
       "basIpAdEntIfIndex": basIpAdEntIfIndex,
       "basIpAdEntNetMask": basIpAdEntNetMask,
       "basIpAdEntBcastAddr": basIpAdEntBcastAddr,
       "basIpAdEntReasmMaxSize": basIpAdEntReasmMaxSize,
       "basIpAdEntStatus": basIpAdEntStatus,
       "basIpAdEntCardType": basIpAdEntCardType,
       "basIpAdEntPriority": basIpAdEntPriority}
)
