# SNMP MIB module (CENTILLION-PORT-RING-MASTER-MONITOR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CENTILLION-PORT-RING-MASTER-MONITOR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:54:11 2024
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

(MacAddress,
 sysMonitor) = mibBuilder.importSymbols(
    "CENTILLION-ROOT-MIB",
    "MacAddress",
    "sysMonitor")

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

_PortRmLastChg_Type = TimeTicks
_PortRmLastChg_Object = MibScalar
portRmLastChg = _PortRmLastChg_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 3, 2),
    _PortRmLastChg_Type()
)
portRmLastChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portRmLastChg.setStatus("mandatory")
_PortRmTable_Object = MibTable
portRmTable = _PortRmTable_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 3, 3)
)
if mibBuilder.loadTexts:
    portRmTable.setStatus("mandatory")
_PortRmEntry_Object = MibTableRow
portRmEntry = _PortRmEntry_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 3, 3, 1)
)
portRmEntry.setIndexNames(
    (0, "CENTILLION-PORT-RING-MASTER-MONITOR-MIB", "portRmSlotNum"),
    (0, "CENTILLION-PORT-RING-MASTER-MONITOR-MIB", "portRmPortNum"),
)
if mibBuilder.loadTexts:
    portRmEntry.setStatus("mandatory")


class _PortRmSlotNum_Type(Integer32):
    """Custom type portRmSlotNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PortRmSlotNum_Type.__name__ = "Integer32"
_PortRmSlotNum_Object = MibTableColumn
portRmSlotNum = _PortRmSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 3, 3, 1, 1),
    _PortRmSlotNum_Type()
)
portRmSlotNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portRmSlotNum.setStatus("mandatory")


class _PortRmPortNum_Type(Integer32):
    """Custom type portRmPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PortRmPortNum_Type.__name__ = "Integer32"
_PortRmPortNum_Object = MibTableColumn
portRmPortNum = _PortRmPortNum_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 3, 3, 1, 2),
    _PortRmPortNum_Type()
)
portRmPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portRmPortNum.setStatus("mandatory")
_PortRmIpAddr_Type = IpAddress
_PortRmIpAddr_Object = MibTableColumn
portRmIpAddr = _PortRmIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 3, 3, 1, 3),
    _PortRmIpAddr_Type()
)
portRmIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portRmIpAddr.setStatus("mandatory")
_PortRmMacAddr_Type = MacAddress
_PortRmMacAddr_Object = MibTableColumn
portRmMacAddr = _PortRmMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 3, 3, 1, 4),
    _PortRmMacAddr_Type()
)
portRmMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portRmMacAddr.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CENTILLION-PORT-RING-MASTER-MONITOR-MIB",
    **{"portRmLastChg": portRmLastChg,
       "portRmTable": portRmTable,
       "portRmEntry": portRmEntry,
       "portRmSlotNum": portRmSlotNum,
       "portRmPortNum": portRmPortNum,
       "portRmIpAddr": portRmIpAddr,
       "portRmMacAddr": portRmMacAddr}
)
