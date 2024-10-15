# SNMP MIB module (BAS-IF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BAS-IF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:45:25 2024
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
 basExtIf) = mibBuilder.importSymbols(
    "BAS-MIB",
    "BasChassisId",
    "BasInterfaceId",
    "BasLogicalPortId",
    "BasSlotId",
    "basExtIf")

(InterfaceIndex,
 ifEntry) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifEntry")

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

basIfMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 2, 2, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BasIfTable_Object = MibTable
basIfTable = _BasIfTable_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 2, 1, 2)
)
if mibBuilder.loadTexts:
    basIfTable.setStatus("current")
_BasIfEntry_Object = MibTableRow
basIfEntry = _BasIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    basIfEntry.setStatus("current")
_BasIfChassis_Type = BasChassisId
_BasIfChassis_Object = MibTableColumn
basIfChassis = _BasIfChassis_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 2, 1, 2, 1, 1),
    _BasIfChassis_Type()
)
basIfChassis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basIfChassis.setStatus("current")
_BasIfSlot_Type = BasSlotId
_BasIfSlot_Object = MibTableColumn
basIfSlot = _BasIfSlot_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 2, 1, 2, 1, 2),
    _BasIfSlot_Type()
)
basIfSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basIfSlot.setStatus("current")
_BasIfInterface_Type = BasInterfaceId
_BasIfInterface_Object = MibTableColumn
basIfInterface = _BasIfInterface_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 2, 1, 2, 1, 3),
    _BasIfInterface_Type()
)
basIfInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basIfInterface.setStatus("current")
_BasIfLPort_Type = BasLogicalPortId
_BasIfLPort_Object = MibTableColumn
basIfLPort = _BasIfLPort_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 2, 1, 2, 1, 4),
    _BasIfLPort_Type()
)
basIfLPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basIfLPort.setStatus("current")


class _BasIfClass_Type(Integer32):
    """Custom type basIfClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ccl", 2),
          ("egress", 3),
          ("icl", 1))
    )


_BasIfClass_Type.__name__ = "Integer32"
_BasIfClass_Object = MibTableColumn
basIfClass = _BasIfClass_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 2, 1, 2, 1, 5),
    _BasIfClass_Type()
)
basIfClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basIfClass.setStatus("current")


class _BasIfSimpleProxyArp_Type(Integer32):
    """Custom type basIfSimpleProxyArp based on Integer32"""
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


_BasIfSimpleProxyArp_Type.__name__ = "Integer32"
_BasIfSimpleProxyArp_Object = MibTableColumn
basIfSimpleProxyArp = _BasIfSimpleProxyArp_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 2, 1, 2, 1, 6),
    _BasIfSimpleProxyArp_Type()
)
basIfSimpleProxyArp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basIfSimpleProxyArp.setStatus("current")
_BasIfDhcpCmSubnet_Type = IpAddress
_BasIfDhcpCmSubnet_Object = MibTableColumn
basIfDhcpCmSubnet = _BasIfDhcpCmSubnet_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 2, 1, 2, 1, 7),
    _BasIfDhcpCmSubnet_Type()
)
basIfDhcpCmSubnet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basIfDhcpCmSubnet.setStatus("current")
_BasIfDhcpHostSubnet_Type = IpAddress
_BasIfDhcpHostSubnet_Object = MibTableColumn
basIfDhcpHostSubnet = _BasIfDhcpHostSubnet_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 2, 1, 2, 1, 8),
    _BasIfDhcpHostSubnet_Type()
)
basIfDhcpHostSubnet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basIfDhcpHostSubnet.setStatus("current")


class _BasIfArpAgingDisable_Type(Integer32):
    """Custom type basIfArpAgingDisable based on Integer32"""
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


_BasIfArpAgingDisable_Type.__name__ = "Integer32"
_BasIfArpAgingDisable_Object = MibTableColumn
basIfArpAgingDisable = _BasIfArpAgingDisable_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 2, 1, 2, 1, 9),
    _BasIfArpAgingDisable_Type()
)
basIfArpAgingDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basIfArpAgingDisable.setStatus("current")


class _BasIfSecurityFilter_Type(Integer32):
    """Custom type basIfSecurityFilter based on Integer32"""
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


_BasIfSecurityFilter_Type.__name__ = "Integer32"
_BasIfSecurityFilter_Object = MibTableColumn
basIfSecurityFilter = _BasIfSecurityFilter_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 2, 1, 2, 1, 10),
    _BasIfSecurityFilter_Type()
)
basIfSecurityFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basIfSecurityFilter.setStatus("current")
ifEntry.registerAugmentions(
    ("BAS-IF-MIB",
     "basIfEntry")
)
basIfEntry.setIndexNames(*ifEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BAS-IF-MIB",
    **{"basIfMIB": basIfMIB,
       "basIfTable": basIfTable,
       "basIfEntry": basIfEntry,
       "basIfChassis": basIfChassis,
       "basIfSlot": basIfSlot,
       "basIfInterface": basIfInterface,
       "basIfLPort": basIfLPort,
       "basIfClass": basIfClass,
       "basIfSimpleProxyArp": basIfSimpleProxyArp,
       "basIfDhcpCmSubnet": basIfDhcpCmSubnet,
       "basIfDhcpHostSubnet": basIfDhcpHostSubnet,
       "basIfArpAgingDisable": basIfArpAgingDisable,
       "basIfSecurityFilter": basIfSecurityFilter}
)
