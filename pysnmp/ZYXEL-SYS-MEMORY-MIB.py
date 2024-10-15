# SNMP MIB module (ZYXEL-SYS-MEMORY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZYXEL-SYS-MEMORY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:22:53 2024
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

(esMgmt,) = mibBuilder.importSymbols(
    "ZYXEL-ES-SMI",
    "esMgmt")


# MODULE-IDENTITY

zyxelSysMemory = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 50)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZyxelSysMemoryPoolStatus_ObjectIdentity = ObjectIdentity
zyxelSysMemoryPoolStatus = _ZyxelSysMemoryPoolStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 50, 1)
)
_ZyxelSysMemoryPoolTable_Object = MibTable
zyxelSysMemoryPoolTable = _ZyxelSysMemoryPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 50, 1, 1)
)
if mibBuilder.loadTexts:
    zyxelSysMemoryPoolTable.setStatus("current")
_ZyxelSysMemoryPoolEntry_Object = MibTableRow
zyxelSysMemoryPoolEntry = _ZyxelSysMemoryPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 50, 1, 1, 1)
)
zyxelSysMemoryPoolEntry.setIndexNames(
    (0, "ZYXEL-SYS-MEMORY-MIB", "zySysMemoryPoolId"),
)
if mibBuilder.loadTexts:
    zyxelSysMemoryPoolEntry.setStatus("current")
_ZySysMemoryPoolId_Type = Unsigned32
_ZySysMemoryPoolId_Object = MibTableColumn
zySysMemoryPoolId = _ZySysMemoryPoolId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 50, 1, 1, 1, 1),
    _ZySysMemoryPoolId_Type()
)
zySysMemoryPoolId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zySysMemoryPoolId.setStatus("current")


class _ZySysMemoryPoolName_Type(OctetString):
    """Custom type zySysMemoryPoolName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ZySysMemoryPoolName_Type.__name__ = "OctetString"
_ZySysMemoryPoolName_Object = MibTableColumn
zySysMemoryPoolName = _ZySysMemoryPoolName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 50, 1, 1, 1, 2),
    _ZySysMemoryPoolName_Type()
)
zySysMemoryPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zySysMemoryPoolName.setStatus("current")
_ZySysMemoryPoolTotalSize_Type = Unsigned32
_ZySysMemoryPoolTotalSize_Object = MibTableColumn
zySysMemoryPoolTotalSize = _ZySysMemoryPoolTotalSize_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 50, 1, 1, 1, 3),
    _ZySysMemoryPoolTotalSize_Type()
)
zySysMemoryPoolTotalSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zySysMemoryPoolTotalSize.setStatus("current")
_ZySysMemoryPoolUsedSize_Type = Unsigned32
_ZySysMemoryPoolUsedSize_Object = MibTableColumn
zySysMemoryPoolUsedSize = _ZySysMemoryPoolUsedSize_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 50, 1, 1, 1, 4),
    _ZySysMemoryPoolUsedSize_Type()
)
zySysMemoryPoolUsedSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zySysMemoryPoolUsedSize.setStatus("current")


class _ZySysMemoryPoolUtilization_Type(Unsigned32):
    """Custom type zySysMemoryPoolUtilization based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ZySysMemoryPoolUtilization_Type.__name__ = "Unsigned32"
_ZySysMemoryPoolUtilization_Object = MibTableColumn
zySysMemoryPoolUtilization = _ZySysMemoryPoolUtilization_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 50, 1, 1, 1, 5),
    _ZySysMemoryPoolUtilization_Type()
)
zySysMemoryPoolUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zySysMemoryPoolUtilization.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-SYS-MEMORY-MIB",
    **{"zyxelSysMemory": zyxelSysMemory,
       "zyxelSysMemoryPoolStatus": zyxelSysMemoryPoolStatus,
       "zyxelSysMemoryPoolTable": zyxelSysMemoryPoolTable,
       "zyxelSysMemoryPoolEntry": zyxelSysMemoryPoolEntry,
       "zySysMemoryPoolId": zySysMemoryPoolId,
       "zySysMemoryPoolName": zySysMemoryPoolName,
       "zySysMemoryPoolTotalSize": zySysMemoryPoolTotalSize,
       "zySysMemoryPoolUsedSize": zySysMemoryPoolUsedSize,
       "zySysMemoryPoolUtilization": zySysMemoryPoolUtilization}
)
